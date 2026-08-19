"""Normalise a raw document into the common record with stable provenance.

Two properties matter here and both are load-bearing.

Determinism: the same snapshot must always normalise to the same text and the
same content hash, so that re-ingestion is a no-op when nothing has changed.

Permission enforcement: a source marked ``link-and-summarise`` must never have
its substantive text stored. Only the link, the title, and generated summaries
may be retained. Getting this wrong is a licence violation, not a bug, so the
rule is applied unconditionally and cannot be overridden by a caller.
"""

import hashlib
import re
from dataclasses import dataclass

from app.schema import Source
from app.source_loader import RawDocument

LINK_AND_SUMMARISE = "link-and-summarise"

_HORIZONTAL_WS = re.compile(r"[ \t]+")
_EDGE_WS = re.compile(r"^[ \t]+|[ \t]+$", re.MULTILINE)
_EXCESS_NEWLINES = re.compile(r"\n{3,}")


@dataclass(frozen=True)
class Document:
    source_id: str
    organisation_id: str
    canonical_url: str
    title: str
    permission_mode: str
    published_at: str | None
    retrieved_at: str
    headings: list[str]
    text: str
    content_hash: str


def normalise_text(text: str) -> str:
    """Collapse whitespace deterministically.

    Runs of spaces and tabs become one space; horizontal whitespace is removed
    from *both* ends of each line; three or more newlines collapse to exactly
    two; the result is stripped.

    Stripping both ends of a line rather than only the trailing end matters:
    indented source text would otherwise carry a leading space into the stored
    document and into its content hash.
    """
    collapsed = _HORIZONTAL_WS.sub(" ", text)
    collapsed = _EDGE_WS.sub("", collapsed)
    collapsed = _EXCESS_NEWLINES.sub("\n\n", collapsed)
    return collapsed.strip()


def normalise(raw: RawDocument, source: Source, retrieved_at: str) -> Document:
    """Build the common document record for one source."""
    text = normalise_text(raw.text)

    if source.permission_mode == LINK_AND_SUMMARISE:
        # Substantive content may not be stored under this permission mode.
        # Metadata and the canonical link are retained so the source can still
        # be cited and summarised from the live page.
        text = ""

    content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()

    return Document(
        source_id=source.source_id,
        organisation_id=source.organisation_id,
        canonical_url=source.canonical_url,
        title=source.title,
        permission_mode=source.permission_mode,
        published_at=source.published_at,
        retrieved_at=retrieved_at,
        headings=list(raw.headings),
        text=text,
        content_hash=content_hash,
    )
