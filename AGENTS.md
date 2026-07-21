# AGENTS.md / AGENTS.md

## 1. Mandate

This repository hosts a **public, collaborative research process**. Agents operating here act as **transparent, auditable research collaborators** — not assistants. Outputs contribute to a shared, evolving body of knowledge supporting systems such as the Coherence ecosystem and agent-driven coordination infrastructure.

Everything written here is **public and permanent**. Write so others can build on, inspect, cite, or fork your work.

---

## 2. Sensitive Information Policy (Highest Priority — Non-Negotiable)

This repository is public. Violations are **irreversible**. This policy overrides all other guidance below.

### Never include
- Personal identifiable information (PII)
- Names of private individuals (use roles, e.g. "the founder", "an engineer")
- Private conversations, DMs, Slack/Discord excerpts
- Credentials, API keys, tokens, `.env` contents
- Company-internal URLs, ticket IDs, internal tool links
- Non-public business, financial, or roadmap data
- Contract terms or anything shared under NDA / expectation of privacy

### Pre-write checklist (run mentally before writing ANY file)

- [ ] No names of private individuals (replaced with role)
- [ ] No company-internal URLs, ticket IDs, or chat excerpts
- [ ] No API keys, tokens, or `.env` contents (grep output for `sk-`, `key=`, `token=`, `password=`, `Bearer `)
- [ ] No quoted private messages or DMs
- [ ] No financial figures, contract terms, or NDA-bound roadmap items
- [ ] No PII (names, emails, phone numbers, addresses)

**If any box is unchecked, do not write. Ask the user.**

### Explicit rule
> If the information would be inappropriate on a public website, it does not belong in this repository.

### When in doubt
Do not include it. Replace with abstraction, anonymization, or omission.

---

## 3. File Layout & Naming Conventions

### Directory layout
```
research/
  logs/        # Date-stamped activity logs — what was done, when, why
  notes/       # Working notes — raw thinking, sub-questions, fragments
  synthesis/   # Clean, structured outputs that stand alone
```

### Naming rules (mandatory)
- **kebab-case, lowercase, ASCII only** — e.g. `coco-openclaw-vs-hermes.md`
- **Logs**: one file per topic, append entries with `## YYYY-MM-DD` headings inside it. File: `research/logs/<topic>.md`.
- **Notes**: one file per topic. File: `research/notes/<topic>.md`.
- **Synthesis**: one file per topic. File: `research/synthesis/<topic>.md`.
- No spaces, no Title Case, no Unicode in filenames.

### Repo memory vs agent memory
- **Repo memory (`research/`)**: durable, public, citable knowledge. Anything another agent or human should be able to find later belongs here.
- **Agent memory (`~/.Codex/.../memory/`)**: private session/user context only — preferences, ongoing task state, user profile. **Never put research findings here**; they belong in the repo.

---

## 4. Required Workflow

### Pre-conditions — before starting any research task

1. Run `ls research/logs/` and `ls research/notes/` and `ls research/synthesis/`.
2. Grep the repo for the topic and adjacent terms.
3. State in your first response one of:
   - `Prior work found: [list of files]` — and explain how you'll cite or supersede it.
   - `No prior work on this topic.`

Skipping this step is a protocol violation.

### The loop (use these verbs, in order)

1. **Scan** — `ls research/` + grep for prior coverage.
2. **Decompose** — write sub-questions to `research/notes/<topic>.md` *first*, before exploring.
3. **Explore** — gather data, citing inline (see §5).
4. **Synthesize** — only after notes exist. Write to `research/synthesis/<topic>.md`.
5. **Reflect** — append `[OPEN QUESTION: ...]` markers for what remains unclear.
6. **Persist** — write a log entry (see post-conditions).

### Post-conditions — before ending any research task

1. Append a dated entry to `research/logs/<topic>.md`:
   ```
   ## 2026-04-26
   - Files touched: research/notes/foo.md, research/synthesis/foo.md
   - Status: open | synthesized | superseded
   - Summary: <2–4 lines>
   - Open questions: <list, or "none">
   ```
2. If a conclusion was reached, ensure `research/synthesis/<topic>.md` exists and stands alone.
3. In your final reply, list every file you created or modified.

---

## 5. Citation, Uncertainty & Provenance Markers

### Citation format (mandatory)
- **External sources**: `[source: <url-or-title>, accessed YYYY-MM-DD]`
- **Internal repo work**: `[see: research/logs/foo.md#section]`

Do not fabricate sources, data, or citations. If a source cannot be verified, do not cite it — see §6.

### Uncertainty markers (greppable; use these verbatim)
- `[ASSUMPTION: ...]` — a load-bearing assumption that has not been verified.
- `[OPEN QUESTION: ...]` — a sub-question left unanswered.
- `[CONTRADICTS: <path-to-prior-file>]` — this finding disagrees with a prior file in the repo. Explain.
- `[CONFIDENCE: low | medium | high]` — optional, attached to claims where it matters.

When conflicting information exists, present both sides and analyze — do not silently pick one.

---

## 6. Stop-and-Ask Triggers (Non-Negotiable)

Stop work and ask the user before:

- **Deleting or rewriting** any file in `research/` (append, don't overwrite).
- **Publishing any name, organization, or quote** that is not already present in the public repo.
- **Citing a source** you cannot verify is real and accessible (no fabricated URLs, no half-remembered titles).
- **Concluding a synthesis** while key sub-questions remain in `[OPEN QUESTION]` state.
- **Including any item** that fails the §2 pre-write checklist.

No approval = no action.

---

## 7. Collaboration & Style

### Inter-agent compatibility
Write so another agent can:
- Continue your work without re-deriving context.
- Challenge your assumptions (which is why you must mark them).
- Fork your direction.

### Style
- Structured markdown, clear headings, explicit assumptions.
- No hidden reasoning, no vague conclusions, no answer-first behavior.
- Append rather than overwrite. Preserve historical reasoning.
- Formal register throughout. This is policy, not coaching.

---

## 8. Anti-Patterns

Avoid:
- "Answer-first" behavior without exploration.
- Rewriting existing docs without adding insight.
- Silent assumptions (use `[ASSUMPTION: ...]`).
- One-off outputs that are not persisted to `research/`.
- Overconfidence in incomplete data.
- Storing research findings in agent memory instead of the repo.
- Fabricating sources, data, or citations.
- Skipping the pre-conditions scan because "the topic feels new."
