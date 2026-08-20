"""Unit 7 — ranked retrieval with provenance attached."""

from app.chunk import Chunk
from app.embed import FakeEmbedder
from app.index import Index, build_index, promote
from app.retrieve import retrieve

CHUNKS = [
    Chunk("org-a-0000", "org-a-about", "org-a", ["Org A"],
          "Org A restores degraded soil in temperate regions.", 0, 49),
    Chunk("org-a-0001", "org-a-about", "org-a", ["Org A", "Funding"],
          "Org A is funded by community bonds.", 49, 84),
    Chunk("org-b-0000", "org-b-about", "org-b", ["Org B"],
          "Org B builds open source mapping tools.", 0, 39),
]


def _index(tmp_path):
    promote(build_index(CHUNKS, FakeEmbedder(dim=16), tmp_path), tmp_path)
    return Index.open(tmp_path / "active.sqlite3")


def test_returns_requested_number_of_results(tmp_path):
    results = retrieve("soil", _index(tmp_path), FakeEmbedder(dim=16), k=2)
    assert len(results) == 2


def test_k_larger_than_corpus_returns_all_chunks(tmp_path):
    results = retrieve("soil", _index(tmp_path), FakeEmbedder(dim=16), k=99)
    assert len(results) == 3


def test_results_are_sorted_by_descending_score(tmp_path):
    results = retrieve("soil", _index(tmp_path), FakeEmbedder(dim=16), k=3)
    scores = [r.score for r in results]
    assert scores == sorted(scores, reverse=True)


def test_every_result_carries_source_metadata(tmp_path):
    results = retrieve("soil", _index(tmp_path), FakeEmbedder(dim=16), k=3)
    for result in results:
        assert result.chunk.source_id
        assert result.chunk.organisation_id
        assert result.chunk.chunk_id


def test_retrieval_is_deterministic(tmp_path):
    index = _index(tmp_path)
    first = retrieve("soil", index, FakeEmbedder(dim=16), k=3)
    second = retrieve("soil", index, FakeEmbedder(dim=16), k=3)
    assert [r.chunk.chunk_id for r in first] == [r.chunk.chunk_id for r in second]


def test_organisation_filter_restricts_results(tmp_path):
    results = retrieve(
        "soil", _index(tmp_path), FakeEmbedder(dim=16), k=3, organisation_id="org-b"
    )
    assert {r.chunk.organisation_id for r in results} == {"org-b"}


def test_scores_are_within_cosine_range(tmp_path):
    results = retrieve("soil", _index(tmp_path), FakeEmbedder(dim=16), k=3)
    for result in results:
        assert -1.0 <= result.score <= 1.0
