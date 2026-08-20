"""The language model behind a swappable, injectable interface.

Model output is not reproducible, so no test may assert on its prose. Every
model-calling function therefore takes the model as a dependency, and the test
suite passes a fake that returns canned output. What the tests assert is the
structure around the model: that citations resolve, that an empty retrieval
refuses rather than guesses, that usage is recorded.

A real model is never called from the test suite. It is slow, it costs money,
and it is not deterministic.
"""

import json
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


@dataclass(frozen=True)
class LLMResponse:
    text: str
    input_tokens: int
    output_tokens: int


class LLM(Protocol):
    model_id: str

    def generate(self, prompt: str) -> LLMResponse: ...


def _rough_tokens(text: str) -> int:
    """A crude token estimate for the fake. Never used for real accounting."""
    return max(1, len(text) // 4)


class FakeLLM:
    """Returns a fixed response. Test use only."""

    def __init__(self, response: str, model_id: str = "fake-model") -> None:
        self._response = response
        self.model_id = model_id
        self.call_count = 0

    def generate(self, prompt: str) -> LLMResponse:
        self.call_count += 1
        return LLMResponse(
            text=self._response,
            input_tokens=_rough_tokens(prompt),
            output_tokens=_rough_tokens(self._response),
        )


class HermesLLM:
    """Calls the configured Hermes model by subprocess. Never used in tests.

    Transport verified on the ARK server, 2026-08-20:

        hermes -z "<prompt>" --usage-file <path>

    The call deliberately keeps the runtime's own context: the agent's persona,
    memory, and skill index ride along with the evidence. That costs about
    20,000 tokens per answer, almost all of it cache-read, and it is the reason
    a sourced answer sounds like the same agent people talk to elsewhere. A
    corpus answer in a different voice reads as a separate system bolted on.

    Passing ``--ignore-rules`` suppresses that injection and reduces the call
    from roughly 20,227 input tokens to 131, with the citation contract and the
    refusal path both intact. It is available as a cost lever and is not the
    default, because the saving buys tokens at the price of voice.

    Generated text arrives on stdout; token accounting is written as JSON to
    the usage file. The local proxy is not an option, since it supports only
    Nous Portal and xAI upstreams and neither is authenticated. Do not pass
    ``-t none``: it suppresses the reply entirely.
    """

    def __init__(self, binary: str = "hermes", timeout: int = 180) -> None:
        self._binary = binary
        self._timeout = timeout
        self.model_id = "hermes-configured"

    def generate(self, prompt: str) -> LLMResponse:
        with tempfile.TemporaryDirectory() as work:
            usage_path = Path(work) / "usage.json"
            completed = subprocess.run(
                [self._binary, "-z", prompt, "--usage-file", str(usage_path)],
                capture_output=True,
                text=True,
                timeout=self._timeout,
                check=False,
            )
            if completed.returncode != 0:
                raise RuntimeError(
                    f"hermes exited {completed.returncode}: {completed.stderr[:400]}"
                )

            input_tokens = output_tokens = 0
            if usage_path.exists():
                data = json.loads(usage_path.read_text(encoding="utf-8"))
                input_tokens = int(data.get("input_tokens") or 0)
                output_tokens = int(data.get("output_tokens") or 0)
                if data.get("model"):
                    self.model_id = str(data["model"])

            return LLMResponse(
                text=completed.stdout.strip(),
                input_tokens=input_tokens,
                output_tokens=output_tokens,
            )
