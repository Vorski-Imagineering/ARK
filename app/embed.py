"""Turn text into vectors behind a swappable interface.

Embeddings run locally with no API key. The server holds no provider
credentials, a local model costs nothing and works offline, and determinism
matters because the retrieval tests assert on exact ranking.

``FakeEmbedder`` is used by the whole test suite. It is derived from a hash, so
it is stable across processes and machines and needs no model download.
``LocalEmbedder`` is the production path and is deliberately not covered by the
unit suite: it is slow and fetches a model. Verify it by hand once, per the
unit specification.
"""

import hashlib
import math
from typing import Protocol

DEFAULT_LOCAL_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


class Embedder(Protocol):
    """Anything that can turn a list of texts into a list of vectors."""

    model_id: str

    def embed(self, texts: list[str]) -> list[list[float]]: ...


def _unit(vector: list[float]) -> list[float]:
    magnitude = math.sqrt(sum(value * value for value in vector))
    if magnitude == 0.0:
        # Degenerate only if every derived byte was zero; fall back to a fixed
        # basis vector so the result stays unit length and deterministic.
        result = [0.0] * len(vector)
        result[0] = 1.0
        return result
    return [value / magnitude for value in vector]


class FakeEmbedder:
    """Deterministic, offline, hash-derived. Test use only."""

    def __init__(self, dim: int = 8) -> None:
        if dim <= 0:
            raise ValueError("dim must be positive")
        self.dim = dim
        self.model_id = f"fake-embedder-{dim}"

    def embed(self, texts: list[str]) -> list[list[float]]:
        return [self._one(text) for text in texts]

    def _one(self, text: str) -> list[float]:
        needed = self.dim
        raw = bytearray()
        counter = 0
        while len(raw) < needed:
            digest = hashlib.sha256(f"{counter}:{text}".encode("utf-8")).digest()
            raw.extend(digest)
            counter += 1
        # Centre each byte on zero so vectors spread across the space rather
        # than clustering in the positive orthant.
        values = [(byte - 127.5) / 127.5 for byte in raw[:needed]]
        return _unit(values)


class LocalEmbedder:
    """Sentence-transformers running locally. Production path, not tested here."""

    def __init__(self, model_name: str = DEFAULT_LOCAL_MODEL) -> None:
        # Imported here rather than at module level so the test suite runs
        # without sentence-transformers installed.
        from sentence_transformers import SentenceTransformer

        self._model = SentenceTransformer(model_name)
        self.model_id = model_name

    def embed(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        vectors = self._model.encode(texts, normalize_embeddings=True)
        return [[float(value) for value in vector] for vector in vectors]
