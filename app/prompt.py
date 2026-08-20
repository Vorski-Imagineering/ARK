"""Build model prompts with retrieved evidence clearly quarantined.

Retrieved source text is untrusted data. It comes from public web pages that
the project does not control, and it can contain anything, including text
shaped like an instruction.

The defence is structural rather than clever. Evidence appears in exactly one
place, between explicit delimiters, after the rules that tell the model to
treat everything inside those delimiters as quoted data. Retrieved text is
never interpolated into the rules section, and never appears outside the
evidence block.
"""

from pathlib import Path

from app.retrieve import RetrievalResult

ANSWER_PROMPT_VERSION = "prompts/answer.md"
DIGEST_PROMPT_VERSION = "prompts/digest.md"

EVIDENCE_BEGIN = "===== BEGIN EVIDENCE (untrusted data) ====="
EVIDENCE_END = "===== END EVIDENCE ====="

_PROMPT_ROOT = Path(__file__).resolve().parent.parent


def _load_template(relative_path: str) -> str:
    return (_PROMPT_ROOT / relative_path).read_text(encoding="utf-8")


def render_evidence(results: list[RetrievalResult]) -> str:
    """Render retrieved chunks as labelled, quoted evidence.

    Each item is prefixed with its source id so the model can cite it, and with
    its heading path so a claim can be located inside the source.
    """
    if not results:
        return "(no evidence was retrieved)"

    lines: list[str] = []
    for result in results:
        chunk = result.chunk
        heading = " > ".join(chunk.heading_path) if chunk.heading_path else ""
        label = f"[{chunk.source_id}]"
        prefix = f"{label} {heading} — " if heading else f"{label} "
        lines.append(f"{prefix}{chunk.text}")
    return "\n\n".join(lines)


def build_answer_prompt(question: str, results: list[RetrievalResult]) -> str:
    """Build the sourced-answer prompt for one question."""
    template = _load_template(ANSWER_PROMPT_VERSION)
    return template.replace("{question}", question).replace(
        "{evidence}", render_evidence(results)
    )


def build_digest_prompt(scope: str, results: list[RetrievalResult]) -> str:
    """Build the cross-organisation digest prompt."""
    template = _load_template(DIGEST_PROMPT_VERSION)
    return template.replace("{scope}", scope).replace(
        "{evidence}", render_evidence(results)
    )
