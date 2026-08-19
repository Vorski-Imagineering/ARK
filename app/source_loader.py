"""Read a source snapshot into a uniform raw document.

Reads local snapshot files only. This module performs no network access:
fetching is a separate operational step, and a network call inside the test
suite is neither deterministic nor free.

Only the standard library is used for HTML parsing.
"""

import re
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree

SUPPORTED_TYPES = ("markdown", "text", "html", "rss")

_MD_HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
_HIDDEN_STYLE = re.compile(r"display\s*:\s*none", re.IGNORECASE)

_SKIP_TAGS = {"script", "style", "noscript", "template"}
_HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
_BLOCK_TAGS = {
    "p", "div", "section", "article", "li", "tr", "br",
    "h1", "h2", "h3", "h4", "h5", "h6",
}


class SourceLoadError(Exception):
    """A snapshot is missing, unreadable, or of an unsupported type."""


@dataclass(frozen=True)
class RawDocument:
    text: str
    headings: list[str]


class _VisibleTextParser(HTMLParser):
    """Collect visible text and headings, skipping scripts, styles, and hidden nodes."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.headings: list[str] = []
        self._skip_depth = 0
        self._hidden_stack: list[str] = []
        self._heading_tag: str | None = None
        self._heading_parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in _SKIP_TAGS:
            self._skip_depth += 1
            return
        style = dict(attrs).get("style") or ""
        hidden = dict(attrs).get("hidden") is not None
        if hidden or _HIDDEN_STYLE.search(style):
            self._hidden_stack.append(tag)
            return
        if tag in _HEADING_TAGS and not self._suppressed:
            self._heading_tag = tag
            self._heading_parts = []
        if tag in _BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in _SKIP_TAGS:
            self._skip_depth = max(0, self._skip_depth - 1)
            return
        if self._hidden_stack and self._hidden_stack[-1] == tag:
            self._hidden_stack.pop()
            return
        if tag == self._heading_tag:
            heading = " ".join("".join(self._heading_parts).split())
            if heading:
                self.headings.append(heading)
            self._heading_tag = None
            self._heading_parts = []
        if tag in _BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if self._suppressed:
            return
        self.parts.append(data)
        if self._heading_tag is not None:
            self._heading_parts.append(data)

    @property
    def _suppressed(self) -> bool:
        return self._skip_depth > 0 or bool(self._hidden_stack)


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise SourceLoadError(f"cannot read snapshot {path}: {exc}") from exc


def _load_markdown(path: Path) -> RawDocument:
    text = _read(path)
    headings = [
        match.group(2).strip()
        for line in text.splitlines()
        if (match := _MD_HEADING.match(line))
    ]
    return RawDocument(text=text, headings=headings)


def _load_text(path: Path) -> RawDocument:
    return RawDocument(text=_read(path), headings=[])


def _load_html(path: Path) -> RawDocument:
    parser = _VisibleTextParser()
    parser.feed(_read(path))
    parser.close()
    lines = [" ".join(part.split()) for part in "".join(parser.parts).split("\n")]
    text = "\n".join(line for line in lines if line)
    return RawDocument(text=text, headings=parser.headings)


def _load_rss(path: Path) -> RawDocument:
    raw = _read(path)
    try:
        root = ElementTree.fromstring(raw)
    except ElementTree.ParseError as exc:
        raise SourceLoadError(f"{path} is not parseable XML: {exc}") from exc

    titles: list[str] = []
    blocks: list[str] = []
    for entry in root.iter():
        tag = entry.tag.rsplit("}", 1)[-1]
        if tag not in {"item", "entry"}:
            continue
        title = ""
        body = ""
        for child in entry:
            name = child.tag.rsplit("}", 1)[-1]
            if name == "title" and child.text:
                title = child.text.strip()
            elif name in {"description", "summary", "content"} and child.text:
                body = child.text.strip()
        if title:
            titles.append(title)
            blocks.append(f"# {title}")
        if body:
            blocks.append(body)

    return RawDocument(text="\n\n".join(blocks), headings=titles)


_LOADERS = {
    "markdown": _load_markdown,
    "text": _load_text,
    "html": _load_html,
    "rss": _load_rss,
}


def load_raw(path: Path, source_type: str) -> RawDocument:
    """Read one local snapshot and return its text plus heading structure."""
    loader = _LOADERS.get(source_type)
    if loader is None:
        raise SourceLoadError(
            f"unsupported source_type {source_type!r}, expected one of "
            f"{list(SUPPORTED_TYPES)}"
        )
    return loader(Path(path))
