"""Produce a digest across several organisations' material.

Retrieval for a digest differs from retrieval for a question. A global top-k
would let whichever organisation happens to rank highest crowd out the rest,
which defeats the point: the digest exists to say something across
organisations, not about the best-matching one.

So evidence is gathered per organisation and then merged. Every organisation
present in the index gets a share of the budget.
"""

from app.answer import (
    Answer,
    build_answer_record,
    embedder_for,
    insufficient_answer,
)
from app.index import Index
from app.llm import LLM
from app.prompt import DIGEST_PROMPT_VERSION, build_digest_prompt
from app.retrieve import RetrievalResult, retrieve
from app.usage import Usage


def _spread_across_organisations(
    scope: str, index: Index, k: int
) -> list[RetrievalResult]:
    """Gather up to an even share of evidence from each organisation."""
    organisation_ids = sorted({chunk.organisation_id for chunk in index.all()})
    if not organisation_ids:
        return []

    embedder = embedder_for(index)
    per_organisation = max(1, k // len(organisation_ids))

    gathered: list[RetrievalResult] = []
    for organisation_id in organisation_ids:
        gathered.extend(
            retrieve(
                scope,
                index,
                embedder,
                k=per_organisation,
                organisation_id=organisation_id,
            )
        )

    gathered.sort(key=lambda result: (-result.score, result.chunk.chunk_id))
    return gathered


def digest(scope: str, index: Index, llm: LLM, k: int) -> Answer:
    """Generate one cross-organisation digest, or refuse."""
    results = _spread_across_organisations(scope, index, k)

    if not results:
        return insufficient_answer(
            scope,
            getattr(llm, "model_id", "unknown"),
            "no evidence was retrieved for this digest scope",
        )

    response = llm.generate(build_digest_prompt(scope, results))

    return build_answer_record(
        scope=scope,
        output=response.text,
        model_id=getattr(llm, "model_id", "unknown"),
        prompt_version=DIGEST_PROMPT_VERSION,
        known_source_ids={chunk.source_id for chunk in index.all()},
        usage=Usage(
            input_tokens=response.input_tokens,
            output_tokens=response.output_tokens,
            estimated_cost_usd=0.0,
        ),
    )
