"""Add one organisation to the ARK corpus, end to end.

Captures the approved public pages, drafts a source pack, validates it, and
rebuilds the index. What took a person an afternoon becomes one command, which
is what makes it usable from a conversation.

What this deliberately does NOT do:

It does not publish. The draft lands in the working tree and nothing is pushed.
Publishing to the public repository stays a human action, because a source pack
asserts that an organisation approved this use of its material, and only a
person can obtain that.

It does not mark anything approved. Every pack it writes is a draft with an
empty sign-off block. The representative fills that in.

Usage:
    python scripts/add_organisation.py \
        --organisation-id example-org \
        --display-name "Example Organisation" \
        --url https://example.org/ "Example Organisation" \
        --url https://example.org/about "About"
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

SNAPSHOT_ROOT = ROOT / "proposal/hackathon-1/execution/snapshots"
PACK_ROOT = ROOT / "proposal/hackathon-1/execution/source-packs"
STAGING_ROOT = ROOT / "proposal/hackathon-1/execution/source-packs-staging"
CAPTURE = ROOT / "scripts/capture-snapshots.mjs"
SLUG = re.compile(r"\A[a-z0-9]+(?:-[a-z0-9]+)*\Z")

MAX_SOURCES = 3
MAX_THEMES = 5


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(2)


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "source"


def find_node() -> str:
    for candidate in ("node", str(Path.home() / ".hermes/node/bin/node")):
        try:
            subprocess.run([candidate, "--version"], capture_output=True, check=True)
            return candidate
        except (OSError, subprocess.CalledProcessError):
            continue
    fail("node was not found; it is required to render pages")
    return ""


def capture(organisation_id: str, sources: list[dict]) -> None:
    """Render each page to a snapshot using the existing capture script."""
    existing = json.loads((SNAPSHOT_ROOT / "sources.json").read_text())

    config = {
        "captured_at": os.environ.get("ARK_CAPTURE_DATE", "unknown"),
        "redact_names": existing.get("redact_names", []),
        "organisations": [
            {
                "organisation_id": organisation_id,
                "sources": [
                    {
                        "source_id": s["source_id"],
                        "slug": s["slug"],
                        "url": s["url"],
                        "title": s["title"],
                    }
                    for s in sources
                ],
            }
        ],
    }

    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
        json.dump(config, handle)
        config_path = handle.name

    node = find_node()
    # The capture script resolves `playwright` from its own node_modules, so it
    # must run from a directory where that resolves.
    runner = Path.home() / ".hermes/hermes-agent"
    result = subprocess.run(
        [node, str(CAPTURE), "--config", config_path, "--out", str(SNAPSHOT_ROOT)],
        capture_output=True,
        text=True,
        cwd=str(runner if runner.exists() else ROOT),
    )
    print(result.stdout.strip())
    if result.returncode != 0:
        fail(f"capture failed: {result.stderr[:400]}")


def provisional_profile(snapshot: Path, limit: int = 3) -> str:
    """Take the first few substantial lines as a starting profile.

    This is a draft for a human or an agent to replace, not a description the
    organisation has approved. It exists so the pack validates and can be
    ingested immediately; the words still need a person.
    """
    lines = [
        line.strip()
        for line in snapshot.read_text(encoding="utf-8").splitlines()
        if len(line.split()) >= 10 and not line.startswith("#")
    ]
    return " ".join(lines[:limit])[:700] or "PROFILE NEEDED - no prose found in snapshot"


def write_pack(
    organisation_id: str,
    display_name: str,
    sources: list[dict],
    themes: list[str],
    participation_url: str | None,
    target_root: Path,
) -> Path:
    first_snapshot = SNAPSHOT_ROOT / organisation_id / f"{sources[0]['slug']}.md"
    profile = provisional_profile(first_snapshot)

    source_blocks = "\n".join(
        f"""  - source_id: {s['source_id']}
    source_type: markdown
    canonical_url: {s['url']}
    title: {s['title']}
    permission_mode: experiment-use
    published_at: null
    snapshot_path: proposal/hackathon-1/execution/snapshots/{organisation_id}/{s['slug']}.md"""
        for s in sources
    )
    theme_block = "\n".join(f"  - {t}" for t in themes)
    rows = "\n".join(f"| `{s['source_id']}` | (see manifest) | ☐ | |" for s in sources)

    content = f"""---
organisation_id: {organisation_id}
display_name: {display_name}
profile: >
  {profile}
themes:
{theme_block}
participation_url: {participation_url or 'null'}
sources:
{source_blocks}
representative_questions:
  - What is {display_name}'s mission?
  - Who is {display_name}'s intended audience?
  - What does {display_name} offer?
---

> **DRAFT — auto-generated, not yet approved.** The profile below was extracted
> from the organisation's own page and is a placeholder, not an approved
> description. The permission mode is proposed, not granted. A representative
> must confirm the profile, sources, permission basis, and questions before this
> pack is used in a demonstration.

# {display_name} — public source pack

## 1. Participation commitment

- **Approved public organisation name:** {display_name}
- **Public website:** {participation_url or sources[0]['url']}
- **Organisation representative role:** `[NOT YET NAMED]`
- **Status:** draft. Sources captured, representative and approval outstanding.

## 6. Permission and representation confirmation

- [ ] The profile and selected sources are intentionally public
- [ ] The organisation has the right to provide these materials for the stated experiment
- [ ] Generated answers and digests may cite and link to the original sources
- [ ] The organisation will review material concerning it and identify material inaccuracies

**Scope of approved use:** proposed **experiment use**.

## 10. Representative sign-off

| Source | Snapshot hash | Approved | Notes |
|---|---|---|---|
{rows}

- **Approved by (role label):** `[TO COMPLETE]`
- **Date:** `[YYYY-MM-DD]`
- **Material misrepresentation found:** `[NONE / DESCRIBE]`
- **Verdict:** `[APPROVED / APPROVED WITH CORRECTION / NOT APPROVED]`
"""
    target_root.mkdir(parents=True, exist_ok=True)
    path = target_root / f"{organisation_id}.md"
    path.write_text(content, encoding="utf-8")
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Add an organisation to the corpus")
    parser.add_argument("--organisation-id", required=True)
    parser.add_argument("--display-name", required=True)
    parser.add_argument(
        "--url", nargs=2, action="append", metavar=("URL", "TITLE"), required=True
    )
    parser.add_argument("--theme", action="append", default=[])
    parser.add_argument("--participation-url", default=None)
    parser.add_argument(
        "--activate",
        action="store_true",
        help="write straight to the live pool and reindex. Operator action: "
        "requires shell access on the host. Without it the pack is staged only.",
    )
    args = parser.parse_args()

    organisation_id = args.organisation_id.strip().lower()
    if not SLUG.match(organisation_id):
        fail(f"organisation-id must be lowercase kebab-case, got {organisation_id!r}")
    STAGING_ROOT.mkdir(parents=True, exist_ok=True)
    target_root = PACK_ROOT if args.activate else STAGING_ROOT
    for existing in (PACK_ROOT, STAGING_ROOT):
        if (existing / f"{organisation_id}.md").exists():
            fail(
                f"a pack for {organisation_id} already exists at "
                f"{(existing / f'{organisation_id}.md').relative_to(ROOT)}; "
                "edit it rather than re-adding"
            )
    if len(args.url) > MAX_SOURCES:
        fail(f"at most {MAX_SOURCES} sources per organisation, got {len(args.url)}")

    sources = []
    for url, title in args.url:
        if not url.startswith(("http://", "https://")):
            fail(f"url must be http or https, got {url!r}")
        slug = slugify(title)
        sources.append(
            {
                "url": url,
                "title": title,
                "slug": slug,
                "source_id": f"{organisation_id}-{slug}",
            }
        )

    themes = [t for t in args.theme][:MAX_THEMES] or ["to be confirmed"]

    print(f"capturing {len(sources)} page(s) for {organisation_id} ...")
    capture(organisation_id, sources)

    pack_path = write_pack(
        organisation_id, args.display_name, sources, themes,
        args.participation_url, target_root,
    )
    print(f"drafted {pack_path.relative_to(ROOT)}")

    from app.source_pack import SourcePackError, load_source_pack

    try:
        pack = load_source_pack(pack_path)
    except SourcePackError as exc:
        fail(f"the drafted pack does not validate: {exc}")
    print(f"validated: {len(pack.sources)} source(s)")

    if args.activate:
        from app.cli import ingest_command

        result = ingest_command(
            source_pack_dir=str(PACK_ROOT),
            index_root=ROOT / "index",
            prefer_local_embedder=True,
        )
        print(
            f"reindexed: packs={result.packs_loaded} sources={result.sources_loaded} "
            f"chunks={result.chunks_indexed}"
        )
        for error in result.errors:
            print(f"  warning: {error}")
        print()
        print("ACTIVE. The organisation is now in the query pool on this host.")
        print("Still NOT published and NOT approved. A person must:")
        print(f"  1. review {pack_path.relative_to(ROOT)} and replace the placeholder profile")
        print("  2. name a representative and obtain their sign-off")
        print("  3. commit and push the pack and its snapshots")
    else:
        print()
        print("STAGED. The organisation is NOT in the query pool and will not")
        print("appear in any answer.")
        print()
        print("To activate it, someone with shell access on this host runs:")
        print(f"  ./scripts/activate-org {organisation_id}")
        print()
        print("Staging is the permission boundary. Anyone who can reach the agent")
        print("can propose an organisation; only an operator can admit one.")
    return 0
