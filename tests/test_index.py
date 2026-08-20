"""Unit 6 — index build, atomic promotion, and rollback."""

import pytest

from app.chunk import Chunk
from app.embed import FakeEmbedder
from app.index import Index, IndexBuildError, build_index, promote, list_indexes

CHUNKS = [
    Chunk(
        chunk_id="valid-org-about-0000",
        source_id="valid-org-about",
        organisation_id="valid-org",
        heading_path=["About Valid Organisation"],
        text="Valid Organisation restores degraded soil.",
        start_offset=0,
        end_offset=41,
    ),
    Chunk(
        chunk_id="valid-org-about-0001",
        source_id="valid-org-about",
        organisation_id="valid-org",
        heading_path=["About Valid Organisation", "Our work"],
        text="We run three field programmes.",
        start_offset=41,
        end_offset=71,
    ),
]


def test_build_writes_to_staging_not_active(tmp_path):
    staging = build_index(CHUNKS, FakeEmbedder(dim=8), tmp_path)
    assert staging.exists()
    assert not (tmp_path / "active.sqlite3").exists()


def test_promotion_makes_index_active(tmp_path):
    staging = build_index(CHUNKS, FakeEmbedder(dim=8), tmp_path)
    promote(staging, tmp_path)
    assert (tmp_path / "active.sqlite3").exists()


def test_index_stores_every_chunk_with_metadata(tmp_path):
    staging = build_index(CHUNKS, FakeEmbedder(dim=8), tmp_path)
    promote(staging, tmp_path)
    index = Index.open(tmp_path / "active.sqlite3")
    assert index.count() == 2
    stored = index.get("valid-org-about-0001")
    assert stored.source_id == "valid-org-about"
    assert stored.organisation_id == "valid-org"
    assert stored.heading_path == ["About Valid Organisation", "Our work"]


def test_rebuild_is_deterministic(tmp_path):
    first = build_index(CHUNKS, FakeEmbedder(dim=8), tmp_path / "a")
    second = build_index(CHUNKS, FakeEmbedder(dim=8), tmp_path / "b")
    assert Index.open(first).fingerprint() == Index.open(second).fingerprint()


def test_failed_build_leaves_active_index_untouched(tmp_path):
    staging = build_index(CHUNKS, FakeEmbedder(dim=8), tmp_path)
    promote(staging, tmp_path)
    before = (tmp_path / "active.sqlite3").read_bytes()
    with pytest.raises(IndexBuildError):
        build_index([], FakeEmbedder(dim=8), tmp_path)
    assert (tmp_path / "active.sqlite3").read_bytes() == before


def test_previous_indexes_are_retained(tmp_path):
    for _ in range(3):
        promote(build_index(CHUNKS, FakeEmbedder(dim=8), tmp_path), tmp_path)
    assert len(list_indexes(tmp_path)) >= 3


def test_no_more_than_four_indexes_are_kept(tmp_path):
    for _ in range(6):
        promote(build_index(CHUNKS, FakeEmbedder(dim=8), tmp_path), tmp_path)
    assert len(list_indexes(tmp_path)) <= 4


def test_empty_chunk_list_raises_rather_than_building_empty_index(tmp_path):
    with pytest.raises(IndexBuildError):
        build_index([], FakeEmbedder(dim=8), tmp_path)
