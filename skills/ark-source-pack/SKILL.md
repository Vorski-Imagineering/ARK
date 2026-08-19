---
name: ark-source-pack
description: Help an organisation representative draft, complete, or validate an ARK source pack — the file listing an organisation's approved public sources, permission basis, and representative questions. Use when asked to "create a source pack", "add my organisation to ARK", "validate this source pack", "check our sources", or when someone wants their organisation's public material included in the ARK Agent.
---

# Draft and validate an ARK source pack

A source pack is how one organisation plugs its public information into the ARK Agent. One file per organisation, committed to the repository, reviewed before it is used.

You are helping a human produce a draft. **You do not approve it.** The organisation representative approves the profile, the sources, the permission statement, and the representative questions. Your output is a draft, always.

## The hard boundary, before anything else

This repository is public, permanent, and CC0-licensed. A source pack may contain only material that is already public or has been explicitly approved for publication.

Never put any of these in a source pack:

- Names of private individuals, or personal contact details — use role labels such as "organisation representative"
- Private conversations, messages, or quotations
- Internal URLs, meeting links, ticket identifiers, or access instructions
- Credentials, tokens, passwords, or environment values
- Confidential commercial, financial, contractual, or roadmap information
- Sources the organisation does not have the right to share

If information would be inappropriate on a public website, it does not belong here. When uncertain, leave it out and ask. [see: AGENTS.md#2-sensitive-information-policy-highest-priority--non-negotiable]

Never ask the representative to give you private material in order to complete the pack.

## Where the file goes

```
proposal/hackathon-1/execution/source-packs/<organisation-slug>.md
```

The slug is lowercase, ASCII, kebab-case, and matches the `organisation_id` inside the file.

## The file has two halves

**YAML frontmatter** carries the machine-readable contract the loader parses. It must validate exactly.

**The markdown body** carries the human-facing pack, following the participation template at `proposal/hackathon-1/execution/02-participation-and-source-pack.md` — commitment, desired value, profile, permission confirmation, readiness check.

## Frontmatter contract

```yaml
---
organisation_id: example-org
display_name: Example Organisation
profile: >
  A 75-120 word public description covering purpose, current work, and how
  people can learn more or participate.
themes:
  - first public theme
  - second public theme
participation_url: https://example.org/join
sources:
  - source_id: example-org-about
    source_type: markdown
    canonical_url: https://example.org/about
    title: About Example Organisation
    permission_mode: experiment-use
    published_at: 2026-05-01
    snapshot_path: null
representative_questions:
  - What does Example Organisation do?
---
```

### Rules the validator enforces

| Field | Rule |
|---|---|
| `organisation_id` | Required. Lowercase, ASCII, kebab-case. |
| `display_name` | Required, non-empty, approved for public use. |
| `profile` | Required, non-empty. 75–120 words. |
| `themes` | Between 1 and 5 entries. Simple public terms. |
| `participation_url` | Public URL or `null`. Never a private email or phone number. |
| `sources` | Between 1 and 3 entries. |
| `source_id` | Must start with `organisation_id`. Unique within the pack. |
| `source_type` | One of `markdown`, `text`, `html`, `rss`. |
| `canonical_url` | Must begin `http://` or `https://`. |
| `permission_mode` | One of `open-reuse`, `experiment-use`, `link-and-summarise`. |
| `published_at` | ISO date, or `null` if unknown. |
| `snapshot_path` | Repository path to an approved snapshot, or `null`. |

### What `permission_mode` actually does

This is not a label. It changes what the system stores.

- **`open-reuse`** — the material is under a stated public licence. Full text is stored, indexed, and quotable within that licence.
- **`experiment-use`** — the material may be indexed, summarised, cited, and demonstrated for this hackathon and any agreed pilot. Further reuse needs review. Full text is stored.
- **`link-and-summarise`** — **no substantive source content is stored at all.** Only the link, the title, and generated summaries. The normaliser enforces this by discarding the body text.

Choose the most restrictive mode the organisation is comfortable with. If the representative is uncertain whether they can authorise a use, the source does not go in until that is resolved.

## How to help

1. **Explain each field** from the public event documents. Do not guess on the representative's behalf.
2. **Check what is missing** against the rules above.
3. **Test that public URLs are reachable.** Report any that are not.
4. **Suggest a shorter public profile** built only from material the organisation has already published.
5. **Draft candidate representative questions** — questions a participant should be able to answer from public information. Good ones test understanding, recency, relationships, or useful action. Avoid anything needing private data or an authoritative organisational decision.
6. **Flag an unclear permission statement** for human review rather than interpreting it yourself.

Mark every draft clearly as a draft. State which fields you filled and which the representative still has to decide.

## Validate before submitting

```
./.venv/bin/python -c "from app.source_pack import load_source_pack; from pathlib import Path; p=load_source_pack(Path('proposal/hackathon-1/execution/source-packs/<slug>.md')); print(p.organisation.organisation_id, len(p.sources), 'ok')"
```

A `SourcePackError` names the offending field. Fix the field — never loosen the validator.

## Completion test

The pack is ready when:

1. The organisation has made an explicit participation commitment.
2. A concise public profile and one to three usable sources are present.
3. A permission basis is stated for every source.
4. At least one representative question is stated.
5. The sensitive-information check passes.
6. The frontmatter validates without error.
7. The organisation representative has approved the final content.

Item 7 is not yours to complete. Hand the draft over and say so.
