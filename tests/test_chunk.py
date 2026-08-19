"""Unit 4 — deterministic chunking with heading context."""

from app.chunk import chunk_document
from app.normalise import Document

DOC = Document(
    source_id="valid-org-about",
    organisation_id="valid-org",
    canonical_url="https://valid-org.example/about",
    title="About Valid Organisation",
    permission_mode="experiment-use",
    published_at="2026-05-01",
    retrieved_at="2026-08-20T10:00:00Z",
    headings=["About Valid Organisation", "Our work"],
    text=(
        "# About Valid Organisation\n\n"
        "Valid Organisation restores degraded soil.\n\n"
        "## Our work\n\n"
        "We run three field programmes."
    ),
    content_hash="0" * 64,
)


def test_chunk_ids_are_deterministic_and_zero_padded():
    chunks = chunk_document(DOC, max_chars=60, overlap=0)
    assert chunks[0].chunk_id == "valid-org-about-0000"
    assert chunks[1].chunk_id == "valid-org-about-0001"


def test_same_input_produces_identical_chunks():
    first = chunk_document(DOC, max_chars=60, overlap=0)
    second = chunk_document(DOC, max_chars=60, overlap=0)
    assert [c.chunk_id for c in first] == [c.chunk_id for c in second]
    assert [c.text for c in first] == [c.text for c in second]


def test_every_chunk_carries_source_and_organisation():
    chunks = chunk_document(DOC, max_chars=60, overlap=0)
    for chunk in chunks:
        assert chunk.source_id == "valid-org-about"
        assert chunk.organisation_id == "valid-org"


def test_no_chunk_exceeds_max_chars():
    chunks = chunk_document(DOC, max_chars=60, overlap=0)
    for chunk in chunks:
        assert len(chunk.text) <= 60


def test_offsets_locate_chunk_text_in_source():
    chunks = chunk_document(DOC, max_chars=60, overlap=0)
    for chunk in chunks:
        assert DOC.text[chunk.start_offset : chunk.end_offset] == chunk.text


def test_heading_path_reflects_position_in_document():
    chunks = chunk_document(DOC, max_chars=60, overlap=0)
    assert chunks[0].heading_path == ["About Valid Organisation"]
    last = chunks[-1]
    assert last.heading_path == ["About Valid Organisation", "Our work"]


def test_overlap_repeats_tail_of_previous_chunk():
    chunks = chunk_document(DOC, max_chars=60, overlap=10)
    assert chunks[1].text[:10] == chunks[0].text[-10:]


def test_empty_document_produces_no_chunks():
    empty = Document(
        source_id="valid-org-updates",
        organisation_id="valid-org",
        canonical_url="https://valid-org.example/updates",
        title="Valid Organisation Updates",
        permission_mode="link-and-summarise",
        published_at=None,
        retrieved_at="2026-08-20T10:00:00Z",
        headings=[],
        text="",
        content_hash="0" * 64,
    )
    assert chunk_document(empty, max_chars=60, overlap=0) == []
