"""Rank stored chunks against a question by cosine similarity.

Every result carries the full provenance of its chunk. That is not a
convenience: a claim in an answer must always be traceable to an exact position
in an exact public source, and retrieval is where that link is established.

Ranking is deterministic. Ties break on chunk identifier, so the same question
against the same index always returns the same ordering.
"""

import math
from dataclasses import dataclass

from app.embed import Embedder
from app.index import Index, StoredChunk


@dataclass(frozen=True)
class RetrievalResult:
    chunk: StoredChunk
    score: float


def cosine(left: list[float], right: list[float]) -> float:
    """Cosine similarity, clamped to the valid range."""
    if not left or not right or len(left) != len(right):
        return 0.0

    dot = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(a * a for a in left))
    right_norm = math.sqrt(sum(b * b for b in right))
    if left_norm == 0.0 or right_norm == 0.0:
        return 0.0

    # Clamp: floating point can push a unit-vector dot product a hair outside
    # [-1, 1], and callers are entitled to a real cosine.
    return max(-1.0, min(1.0, dot / (left_norm * right_norm)))


def retrieve(
    question: str,
    index: Index,
    embedder: Embedder,
    k: int,
    organisation_id: str | None = None,
) -> list[RetrievalResult]:
    """Return the k best-matching chunks, most similar first."""
    if k <= 0:
        return []

    candidates = index.all()
    if organisation_id is not None:
        candidates = [
            chunk for chunk in candidates if chunk.organisation_id == organisation_id
        ]
    if not candidates:
        return []

    query_vector = embedder.embed([question])[0]

    scored = [
        RetrievalResult(chunk=chunk, score=cosine(query_vector, chunk.embedding))
        for chunk in candidates
    ]
    # Descending score, then ascending chunk_id so ordering is stable.
    scored.sort(key=lambda result: (-result.score, result.chunk.chunk_id))
    return scored[:k]
