"""Ratified data contracts for the ARK Agent.

Field names and types come from the technical specification, section 5.
Do not add, rename, or retype fields without amending that document first.
"""

from dataclasses import dataclass

PERMISSION_MODES = ("open-reuse", "experiment-use", "link-and-summarise")
SOURCE_TYPES = ("markdown", "text", "html", "rss")


@dataclass(frozen=True)
class Organisation:
    organisation_id: str
    display_name: str
    profile: str
    themes: list[str]
    participation_url: str | None


@dataclass(frozen=True)
class Source:
    source_id: str
    organisation_id: str
    source_type: str
    canonical_url: str
    title: str
    permission_mode: str
    published_at: str | None
    snapshot_path: str | None


@dataclass(frozen=True)
class SourcePack:
    organisation: Organisation
    sources: list[Source]
    representative_questions: list[str]
