"""Load and validate an organisation source pack.

A source pack is one markdown file. YAML frontmatter carries the machine
readable contract; the markdown body is for humans and is not parsed.

Validation raises rather than warns. A malformed pack must fail at submission
time, not silently corrupt the index.
"""

import datetime as _datetime
import re
from pathlib import Path

import yaml

from app.schema import (
    DEFAULT_LICENSE,
    LAWFUL_BASES,
    PERMISSION_MODES,
    SENSITIVITIES,
    SOURCE_TYPES,
    Organisation,
    Source,
    SourcePack,
)

_FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
_SLUG = re.compile(r"\A[a-z0-9]+(?:-[a-z0-9]+)*\Z")

MAX_THEMES = 5
MAX_SOURCES = 3


class SourcePackError(Exception):
    """A source pack is missing, unreadable, or violates the contract."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise SourcePackError(message)


def _as_optional_str(value: object) -> str | None:
    """Normalise a scalar to a string, preserving None.

    YAML parses an unquoted ISO date into a date object. The contract stores
    timestamps as ISO-8601 strings, so coerce rather than leaking the type.
    """
    if value is None:
        return None
    if isinstance(value, (_datetime.date, _datetime.datetime)):
        return value.isoformat()
    return str(value)


def _parse_frontmatter(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise SourcePackError(f"cannot read source pack {path}: {exc}") from exc

    match = _FRONTMATTER.match(text)
    _require(match is not None, f"{path} has no YAML frontmatter block")

    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise SourcePackError(f"{path} has invalid YAML frontmatter: {exc}") from exc

    _require(isinstance(data, dict), f"{path} frontmatter must be a mapping")
    return data


def _build_organisation(data: dict) -> Organisation:
    organisation_id = _as_optional_str(data.get("organisation_id"))
    _require(bool(organisation_id), "organisation_id is required")
    _require(
        bool(_SLUG.match(organisation_id)),
        f"organisation_id must be lowercase ASCII kebab-case, got {organisation_id!r}",
    )

    display_name = _as_optional_str(data.get("display_name"))
    _require(bool(display_name and display_name.strip()), "display_name is required")

    profile = _as_optional_str(data.get("profile"))
    _require(bool(profile and profile.strip()), "profile is required")

    themes = data.get("themes") or []
    _require(isinstance(themes, list), "themes must be a list")
    _require(
        1 <= len(themes) <= MAX_THEMES,
        f"themes must hold between 1 and {MAX_THEMES} entries, got {len(themes)}",
    )

    return Organisation(
        organisation_id=organisation_id,
        display_name=display_name,
        profile=profile.strip(),
        themes=[str(theme) for theme in themes],
        participation_url=_as_optional_str(data.get("participation_url")),
    )


def _build_sources(data: dict, organisation_id: str) -> list[Source]:
    raw_sources = data.get("sources") or []
    _require(isinstance(raw_sources, list), "sources must be a list")
    _require(
        1 <= len(raw_sources) <= MAX_SOURCES,
        f"sources must hold between 1 and {MAX_SOURCES} entries, got {len(raw_sources)}",
    )

    sources: list[Source] = []
    seen: set[str] = set()

    for entry in raw_sources:
        _require(isinstance(entry, dict), "each source must be a mapping")

        source_id = _as_optional_str(entry.get("source_id"))
        _require(bool(source_id), "source_id is required")
        _require(
            source_id.startswith(organisation_id),
            f"source_id {source_id!r} must start with organisation_id "
            f"{organisation_id!r}",
        )
        _require(source_id not in seen, f"duplicate source_id {source_id!r}")
        seen.add(source_id)

        source_type = _as_optional_str(entry.get("source_type"))
        _require(
            source_type in SOURCE_TYPES,
            f"source_type must be one of {list(SOURCE_TYPES)}, got {source_type!r}",
        )

        permission_mode = _as_optional_str(entry.get("permission_mode"))
        _require(
            permission_mode in PERMISSION_MODES,
            f"permission_mode must be one of {list(PERMISSION_MODES)}, "
            f"got {permission_mode!r}",
        )

        canonical_url = _as_optional_str(entry.get("canonical_url"))
        _require(
            bool(canonical_url)
            and canonical_url.startswith(("http://", "https://")),
            f"canonical_url must be an http or https URL, got {canonical_url!r}",
        )

        lawful_basis = _as_optional_str(entry.get("lawful_basis")) or "legitimate-interest"
        _require(
            lawful_basis in LAWFUL_BASES,
            f"lawful_basis must be one of {list(LAWFUL_BASES)}, got {lawful_basis!r}",
        )

        sensitivity = _as_optional_str(entry.get("sensitivity")) or "commons"
        _require(
            sensitivity in SENSITIVITIES,
            f"sensitivity must be one of {list(SENSITIVITIES)}, got {sensitivity!r}",
        )

        title = _as_optional_str(entry.get("title"))
        _require(bool(title and title.strip()), f"title is required for {source_id!r}")

        sources.append(
            Source(
                source_id=source_id,
                organisation_id=organisation_id,
                source_type=source_type,
                canonical_url=canonical_url,
                title=title,
                permission_mode=permission_mode,
                published_at=_as_optional_str(entry.get("published_at")),
                snapshot_path=_as_optional_str(entry.get("snapshot_path")),
                license=_as_optional_str(entry.get("license")) or DEFAULT_LICENSE,
                lawful_basis=lawful_basis,
                sensitivity=sensitivity,
            )
        )

    return sources


def load_source_pack(path: Path) -> SourcePack:
    """Parse and validate one source pack. Raises SourcePackError on any fault."""
    data = _parse_frontmatter(Path(path))
    organisation = _build_organisation(data)
    sources = _build_sources(data, organisation.organisation_id)

    questions = data.get("representative_questions") or []
    _require(isinstance(questions, list), "representative_questions must be a list")

    return SourcePack(
        organisation=organisation,
        sources=sources,
        representative_questions=[str(q) for q in questions],
    )
