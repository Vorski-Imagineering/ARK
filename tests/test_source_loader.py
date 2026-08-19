"""Unit 2 — reading source snapshots into raw documents."""

from pathlib import Path

import pytest

from app.source_loader import SourceLoadError, load_raw

SNAPSHOTS = Path("tests/fixtures/snapshots")


def test_markdown_snapshot_returns_full_text():
    raw = load_raw(SNAPSHOTS / "valid-org-about.md", "markdown")
    assert "restores degraded soil" in raw.text
    assert raw.text.startswith("# About Valid Organisation")


def test_markdown_headings_are_extracted_in_order():
    raw = load_raw(SNAPSHOTS / "valid-org-about.md", "markdown")
    assert raw.headings == [
        "About Valid Organisation",
        "Our work",
        "How to join",
    ]


def test_html_strips_script_and_style_content():
    raw = load_raw(SNAPSHOTS / "sample-page.html", "html")
    assert "console.log" not in raw.text
    assert "color:red" not in raw.text


def test_html_strips_hidden_elements():
    raw = load_raw(SNAPSHOTS / "sample-page.html", "html")
    assert "hidden text must not appear" not in raw.text


def test_html_keeps_visible_paragraphs():
    raw = load_raw(SNAPSHOTS / "sample-page.html", "html")
    assert "Visible paragraph one." in raw.text
    assert "Visible paragraph two." in raw.text


def test_html_headings_are_extracted():
    raw = load_raw(SNAPSHOTS / "sample-page.html", "html")
    assert raw.headings == ["Sample Heading", "Second Heading"]


def test_unknown_source_type_raises():
    with pytest.raises(SourceLoadError):
        load_raw(SNAPSHOTS / "valid-org-about.md", "pdf")


def test_missing_snapshot_raises_source_load_error():
    with pytest.raises(SourceLoadError):
        load_raw(SNAPSHOTS / "nope.md", "markdown")
