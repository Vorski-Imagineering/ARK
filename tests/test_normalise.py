"""Unit 3 — normalisation, provenance, and permission enforcement."""

import hashlib
from pathlib import Path

from app.normalise import normalise
from app.source_loader import load_raw
from app.source_pack import load_source_pack

FIXTURES = Path("tests/fixtures/source-packs")
RETRIEVED_AT = "2026-08-20T10:00:00Z"


def _pack():
    return load_source_pack(FIXTURES / "valid-org.md")


def test_document_carries_full_provenance():
    pack = _pack()
    source = pack.sources[0]
    raw = load_raw(Path(source.snapshot_path), source.source_type)
    doc = normalise(raw, source, RETRIEVED_AT)
    assert doc.source_id == "valid-org-about"
    assert doc.organisation_id == "valid-org"
    assert doc.canonical_url == "https://valid-org.example/about"
    assert doc.title == "About Valid Organisation"
    assert doc.published_at == "2026-05-01"
    assert doc.retrieved_at == RETRIEVED_AT


def test_content_hash_is_sha256_of_normalised_text():
    pack = _pack()
    source = pack.sources[0]
    raw = load_raw(Path(source.snapshot_path), source.source_type)
    doc = normalise(raw, source, RETRIEVED_AT)
    expected = hashlib.sha256(doc.text.encode("utf-8")).hexdigest()
    assert doc.content_hash == expected
    assert len(doc.content_hash) == 64


def test_normalisation_is_deterministic():
    pack = _pack()
    source = pack.sources[0]
    raw = load_raw(Path(source.snapshot_path), source.source_type)
    first = normalise(raw, source, RETRIEVED_AT)
    second = normalise(raw, source, RETRIEVED_AT)
    assert first.content_hash == second.content_hash
    assert first.text == second.text


def test_whitespace_is_collapsed_deterministically():
    from app.source_loader import RawDocument

    pack = _pack()
    messy = RawDocument(text="a  \n\n\n  b\t\tc   \n", headings=[])
    doc = normalise(messy, pack.sources[0], RETRIEVED_AT)
    assert doc.text == "a\n\nb c"


def test_link_and_summarise_source_stores_no_body_text():
    pack = _pack()
    restricted = pack.sources[1]
    assert restricted.permission_mode == "link-and-summarise"
    raw = load_raw(Path(restricted.snapshot_path), restricted.source_type)
    doc = normalise(raw, restricted, RETRIEVED_AT)
    assert doc.text == ""
    assert "forty hectares" not in doc.text


def test_link_and_summarise_source_keeps_metadata():
    pack = _pack()
    restricted = pack.sources[1]
    raw = load_raw(Path(restricted.snapshot_path), restricted.source_type)
    doc = normalise(raw, restricted, RETRIEVED_AT)
    assert doc.canonical_url == "https://valid-org.example/updates"
    assert doc.title == "Valid Organisation Updates"
    assert doc.content_hash != ""


def test_experiment_use_source_keeps_body_text():
    pack = _pack()
    source = pack.sources[0]
    raw = load_raw(Path(source.snapshot_path), source.source_type)
    doc = normalise(raw, source, RETRIEVED_AT)
    assert "restores degraded soil" in doc.text
