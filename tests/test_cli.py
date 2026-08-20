"""Unit 12 — the command surface."""

import pytest

from app.cli import build_parser, ingest_command


def test_parser_exposes_every_required_command():
    parser = build_parser()
    commands = set(parser._subparsers._group_actions[0].choices)
    assert {"ingest", "query", "digest", "run"} <= commands


def test_query_requires_a_question():
    parser = build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["query"])


def test_query_accepts_a_question():
    parser = build_parser()
    args = parser.parse_args(["query", "What does Org A do?"])
    assert args.question == "What does Org A do?"


def test_ingest_reports_counts(tmp_path, monkeypatch):
    monkeypatch.setenv("ARK_INDEX_PATH", str(tmp_path))
    result = ingest_command(
        source_pack_dir="tests/fixtures/source-packs",
        index_root=tmp_path,
        only=["valid-org.md"],
    )
    assert result.packs_loaded == 1
    assert result.sources_loaded == 2
    assert result.chunks_indexed > 0


def test_ingest_skips_link_and_summarise_content(tmp_path):
    result = ingest_command(
        source_pack_dir="tests/fixtures/source-packs",
        index_root=tmp_path,
        only=["valid-org.md"],
    )
    assert result.sources_skipped_for_permission == 1
