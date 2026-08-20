"""Answer a question from retrieved evidence, or refuse honestly.

Two behaviours here are the whole point of the phase.

Every material claim must be traceable. Citations are extracted from the
model's output and checked against the index; anything that does not resolve to
a real source is dropped and recorded as a limitation rather than passed
through. A fabricated citation is worse than no citation, because it looks like
evidence.

An absence of evidence produces a refusal, not a guess. When retrieval returns
nothing the model is not called at all.
"""

import re
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone

from app.index import Index
from app.llm import LLM
from app.prompt import ANSWER_PROMPT_VERSION, build_answer_prompt
from app.retrieve import retrieve
from app.usage import Usage

REFUSAL_MARKER = "INSUFFICIENT EVIDENCE"
REVIEW_UNREVIEWED = "unreviewed"

_CITATION = re.compile(r"\[([A-Za-z0-9][A-Za-z0-9._-]*)\]")


@dataclass(frozen=True)
class Answer:
    run_id: str
    created_at: str
    model: str
    prompt_version: str
    question_or_digest_scope: str
    output: str
    cited_source_ids: list[str]
    review_status: str
    limitations: list[str]
    usage: Usage
    insufficient_evidence: bool


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def extract_citations(text: str) -> list[str]:
    """Every bracketed identifier, in order of first appearance."""
    seen: set[str] = set()
    ordered: list[str] = []
    for match in _CITATION.finditer(text):
        candidate = match.group(1)
        if candidate not in seen:
            seen.add(candidate)
            ordered.append(candidate)
    return ordered


def resolve_citations(
    cited: list[str], known_source_ids: set[str]
) -> tuple[list[str], list[str]]:
    """Split cited identifiers into those that resolve and a list of limitations."""
    resolved: list[str] = []
    limitations: list[str] = []
    for source_id in cited:
        if source_id in known_source_ids:
            resolved.append(source_id)
        else:
            limitations.append(
                f"the model cited {source_id!r}, which is not a source in the index; "
                "the citation was dropped"
            )
    return resolved, limitations


def _empty_answer(scope: str, model_id: str, reason: str) -> Answer:
    return Answer(
        run_id=str(uuid.uuid4()),
        created_at=_now(),
        model=model_id,
        prompt_version=ANSWER_PROMPT_VERSION,
        question_or_digest_scope=scope,
        output=f"{REFUSAL_MARKER}\n{reason}",
        cited_source_ids=[],
        review_status=REVIEW_UNREVIEWED,
        limitations=[reason],
        usage=Usage(input_tokens=0, output_tokens=0, estimated_cost_usd=0.0),
        insufficient_evidence=True,
    )


def build_answer_record(
    scope: str,
    output: str,
    model_id: str,
    prompt_version: str,
    known_source_ids: set[str],
    usage: Usage,
) -> Answer:
    """Turn raw model output into a checked Answer record."""
    cited, limitations = resolve_citations(
        extract_citations(output), known_source_ids
    )

    refused = output.strip().upper().startswith(REFUSAL_MARKER)
    if not cited and not refused:
        limitations.append(
            "the answer contains no resolvable citation, so no claim in it is "
            "supported by an inspectable source"
        )

    return Answer(
        run_id=str(uuid.uuid4()),
        created_at=_now(),
        model=model_id,
        prompt_version=prompt_version,
        question_or_digest_scope=scope,
        output=output,
        cited_source_ids=cited,
        review_status=REVIEW_UNREVIEWED,
        limitations=limitations,
        usage=usage,
        insufficient_evidence=refused,
    )


def answer(question: str, index: Index, llm: LLM, k: int) -> Answer:
    """Answer one question from the index, or refuse."""
    results = retrieve(question, index, _embedder_for(index), k)

    if not results:
        # No evidence at all. Do not call the model: there is nothing for it to
        # ground an answer in, and asking anyway invites invention.
        return _empty_answer(
            question,
            getattr(llm, "model_id", "unknown"),
            "no evidence was retrieved for this question",
        )

    prompt = build_answer_prompt(question, results)
    response = llm.generate(prompt)

    return build_answer_record(
        scope=question,
        output=response.text,
        model_id=getattr(llm, "model_id", "unknown"),
        prompt_version=ANSWER_PROMPT_VERSION,
        known_source_ids={chunk.source_id for chunk in index.all()},
        usage=Usage(
            input_tokens=response.input_tokens,
            output_tokens=response.output_tokens,
            estimated_cost_usd=0.0,
        ),
    )


def _embedder_for(index: Index):
    """Return an embedder matching the vectors stored in this index.

    The index records which model produced its vectors, so the query must be
    embedded the same way. A fake-embedded index is queried with the fake.
    """
    from app.embed import FakeEmbedder, LocalEmbedder

    signature = index.embedding_signature()
    if signature is None:
        return FakeEmbedder(dim=8)

    model_id, dimension = signature
    if model_id.startswith("fake-embedder-"):
        return FakeEmbedder(dim=dimension)
    return LocalEmbedder(model_id)
