"""Shared index builders for the model-dependent tests."""

from app.chunk import Chunk
from app.embed import FakeEmbedder
from app.index import Index, build_index, promote

CHUNKS = [
    Chunk("org-a-0000", "org-a-about", "org-a", ["Org A"],
          "Org A restores degraded soil in temperate regions.", 0, 49),
    Chunk("org-b-0000", "org-b-about", "org-b", ["Org B"],
          "Org B builds open source mapping tools.", 0, 39),
]


def build_test_index(tmp_path):
    promote(build_index(CHUNKS, FakeEmbedder(dim=16), tmp_path), tmp_path)
    return Index.open(tmp_path / "active.sqlite3")


def build_empty_index(tmp_path):
    """An index containing no chunks, built by bypassing the non-empty guard."""
    return Index.create_empty(tmp_path / "empty.sqlite3")
