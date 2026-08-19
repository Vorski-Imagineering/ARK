"""Split a document into retrieval chunks that keep their heading context.

Two invariants hold for every chunk produced here.

Exact slicing: ``document.text[chunk.start_offset:chunk.end_offset]`` is always
identical to ``chunk.text``. Chunk text is never stripped or rewritten, because
a retrieved passage must be locatable at an exact position in an exact source.

Determinism: the same document and parameters always yield the same chunks with
the same identifiers, so re-ingestion of unchanged content is a no-op.
"""

from dataclasses import dataclass, field

from app.normalise import Document

PARAGRAPH_BREAK = "\n\n"


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    source_id: str
    organisation_id: str
    heading_path: list[str]
    text: str
    start_offset: int
    end_offset: int
    embedding: list[float] = field(default_factory=list)


def _heading_line_offsets(text: str, headings: list[str]) -> list[tuple[int, str]]:
    """Locate each heading by the start of the line it sits on.

    The line start is used rather than the position of the heading text itself.
    In markdown a heading is preceded by its hashes, so a chunk beginning at
    offset 0 would otherwise not be governed by a heading whose text begins at
    offset 2.
    """
    located: list[tuple[int, str]] = []
    cursor = 0
    for heading in headings:
        found = text.find(heading, cursor)
        if found == -1:
            continue
        line_start = text.rfind("\n", 0, found) + 1
        located.append((line_start, heading))
        cursor = found + len(heading)
    return located


def _heading_path_for(offset: int, located: list[tuple[int, str]]) -> list[str]:
    return [heading for line_start, heading in located if line_start <= offset]


def _split_point(text: str, start: int, max_chars: int) -> int:
    """Choose where this chunk ends, preferring a paragraph boundary."""
    window_end = min(len(text), start + max_chars)
    if window_end >= len(text):
        return len(text)

    boundary = text.rfind(PARAGRAPH_BREAK, start, window_end)
    if boundary > start:
        return boundary

    boundary = text.rfind("\n", start, window_end)
    if boundary > start:
        return boundary

    return window_end


def chunk_document(doc: Document, max_chars: int, overlap: int) -> list[Chunk]:
    """Split one document into ordered, deterministically identified chunks."""
    text = doc.text
    if not text:
        # A link-and-summarise source stores no body text and therefore
        # contributes no chunks. That is the intended behaviour, not a failure.
        return []

    if max_chars <= 0:
        raise ValueError("max_chars must be positive")
    if overlap < 0 or overlap >= max_chars:
        raise ValueError("overlap must be non-negative and smaller than max_chars")

    located = _heading_line_offsets(text, doc.headings)

    chunks: list[Chunk] = []
    start = 0
    position = 0

    while start < len(text):
        end = _split_point(text, start, max_chars)
        piece = text[start:end]

        if piece:
            chunks.append(
                Chunk(
                    chunk_id=f"{doc.source_id}-{position:04d}",
                    source_id=doc.source_id,
                    organisation_id=doc.organisation_id,
                    heading_path=_heading_path_for(start, located),
                    text=piece,
                    start_offset=start,
                    end_offset=end,
                )
            )
            position += 1

        if end >= len(text):
            break

        next_start = end - overlap
        if overlap == 0:
            # Step over the separator so chunks do not open with blank lines.
            while next_start < len(text) and text[next_start] in "\n\r\t ":
                next_start += 1
        if next_start <= start:
            next_start = start + 1
        start = next_start

    return chunks
