"""Ratified data contracts for the ARK Agent.

Field names and types come from the technical specification, section 5.
Do not add, rename, or retype fields without amending that document first.
"""

from dataclasses import dataclass

PERMISSION_MODES = ("open-reuse", "experiment-use", "link-and-summarise")
SOURCE_TYPES = ("markdown", "text", "html", "rss")

# Why a source may be held at all. Scraped organisational material rests on
# legitimate interest rather than consent: you cannot obtain consent from people
# whose published pages you read, and pretending otherwise produces a consent
# record that means nothing. Consent is the right basis for material a person
# actively submits.
LAWFUL_BASES = ("legitimate-interest", "consent", "contract", "public-task")

# Who may see a row. "commons" is shared across the ecosystem view; anything
# else is scoped and must not leak into a cross-organisation answer.
SENSITIVITIES = ("commons", "holon-private", "restricted")

# The licence the SOURCE publishes under. This is recorded, never granted: this
# repository's own CC0 dedication has no power over other people's material.
DEFAULT_LICENSE = "unstated"


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
    # Governance, added 2026-08-20. Defaults keep older packs valid.
    license: str = DEFAULT_LICENSE
    lawful_basis: str = "legitimate-interest"
    sensitivity: str = "commons"


@dataclass(frozen=True)
class SourcePack:
    organisation: Organisation
    sources: list[Source]
    representative_questions: list[str]
