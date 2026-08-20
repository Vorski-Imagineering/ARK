"""Usage and cost accounting for model calls.

The run log records identifiers and counts only, never prompt text, question
text, or generated output. That constraint is what allows a sanitised usage
summary to be published to the public repository while the raw content stays
local. It is enforced by construction here rather than by reviewer discipline
later.

Cost is estimated locally from a rate table. The configured provider is an
OAuth subscription rather than a metered API, so it frequently reports a cost
of zero with an unknown status. A zero from the provider is not an error, and
it is not the same thing as free.
"""

import json
from dataclasses import dataclass
from pathlib import Path

TOKENS_PER_MILLION = 1_000_000

# Reference rates in USD per million tokens. Configuration, not truth: update
# from the provider's published pricing rather than trusting this table.
DEFAULT_RATES: dict[str, dict[str, float]] = {
    "gpt-5.6-luna": {"input_per_m": 1.0, "output_per_m": 6.0},
    "text-embedding-3-small": {"input_per_m": 0.02, "output_per_m": 0.0},
}


@dataclass(frozen=True)
class Usage:
    input_tokens: int
    output_tokens: int
    estimated_cost_usd: float


def estimate_cost(
    model: str,
    input_tokens: int,
    output_tokens: int,
    rates: dict[str, dict[str, float]] | None = None,
) -> float:
    """Estimate the cost of one call in USD.

    An unrecognised model costs zero. That is a deliberate choice: a missing
    rate is a gap in configuration, and refusing to run over it would block a
    subscription-backed provider that reports no per-call price at all.
    """
    table = DEFAULT_RATES if rates is None else rates
    rate = table.get(model)
    if rate is None:
        return 0.0

    input_cost = (input_tokens / TOKENS_PER_MILLION) * rate.get("input_per_m", 0.0)
    output_cost = (output_tokens / TOKENS_PER_MILLION) * rate.get("output_per_m", 0.0)
    return input_cost + output_cost


def log_run(path: Path, run_id: str, model: str, usage: Usage, kind: str) -> None:
    """Append one accounting record. Counts and identifiers only."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    record = {
        "run_id": run_id,
        "kind": kind,
        "model": model,
        "input_tokens": usage.input_tokens,
        "output_tokens": usage.output_tokens,
        "estimated_cost_usd": usage.estimated_cost_usd,
    }

    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")


def total_cost(path: Path) -> float:
    """Sum estimated cost across a run log. Returns zero if the log is absent."""
    path = Path(path)
    if not path.exists():
        return 0.0
    running = 0.0
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            running += float(json.loads(line).get("estimated_cost_usd") or 0.0)
    return running
