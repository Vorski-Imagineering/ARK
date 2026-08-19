"""Unit 1 — source pack parsing and validation."""

from pathlib import Path

import pytest

from app.source_pack import SourcePackError, load_source_pack

FIXTURES = Path("tests/fixtures/source-packs")


def test_valid_pack_parses_organisation():
    pack = load_source_pack(FIXTURES / "valid-org.md")
    org = pack.organisation
    assert org.organisation_id == "valid-org"
    assert org.display_name == "Valid Organisation"
    assert org.themes == ["soil restoration", "community finance"]
    assert org.participation_url == "https://valid-org.example/join"


def test_valid_pack_parses_two_sources():
    pack = load_source_pack(FIXTURES / "valid-org.md")
    assert len(pack.sources) == 2
    assert [s.source_id for s in pack.sources] == [
        "valid-org-about",
        "valid-org-updates",
    ]


def test_source_fields_are_typed_correctly():
    pack = load_source_pack(FIXTURES / "valid-org.md")
    first = pack.sources[0]
    assert first.organisation_id == "valid-org"
    assert first.source_type == "markdown"
    assert first.canonical_url == "https://valid-org.example/about"
    assert first.title == "About Valid Organisation"
    assert first.permission_mode == "experiment-use"
    assert first.published_at == "2026-05-01"
    assert first.snapshot_path == "tests/fixtures/snapshots/valid-org-about.md"


def test_null_published_at_is_none_not_string():
    pack = load_source_pack(FIXTURES / "valid-org.md")
    assert pack.sources[1].published_at is None


def test_representative_questions_are_parsed():
    pack = load_source_pack(FIXTURES / "valid-org.md")
    assert pack.representative_questions == [
        "What does Valid Organisation do?",
        "Which themes does Valid Organisation work on?",
    ]


def test_unknown_permission_mode_is_rejected():
    with pytest.raises(SourcePackError) as excinfo:
        load_source_pack(FIXTURES / "bad-permission.md")
    assert "permission_mode" in str(excinfo.value)


def test_source_id_must_start_with_organisation_id():
    with pytest.raises(SourcePackError) as excinfo:
        load_source_pack(FIXTURES / "bad-source-id.md")
    assert "source_id" in str(excinfo.value)


def test_missing_file_raises_source_pack_error():
    with pytest.raises(SourcePackError):
        load_source_pack(FIXTURES / "does-not-exist.md")
