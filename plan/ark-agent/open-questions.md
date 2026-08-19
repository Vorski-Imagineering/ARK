# ARK Agent open questions

Unresolved questions that affect the build. Uses the repository's standard greppable markers. [see: AGENTS.md#5-citation-uncertainty--provenance-markers]

Each entry records who owns the answer and what it blocks. When a question is answered, move it to the Resolved section with the date and the ruling — do not delete it.

---

## Blocking — a phase cannot open until these are ruled

`[OPEN QUESTION: Does the ARK Agent keep its current single runtime profile, with its identity file rewritten for group scope, or does the participant-facing ARK Agent get its own separate profile? Owner: technical lead + event lead. Blocks: identity work in Phase 0; affects every phase thereafter.]`

The operating answer as of 2026-08-20 is: one profile, identity file rewritten. The formal ruling is still open because a second profile has real consequences for cost, isolation, and the usage-scoping principle UP-U1.

`[OPEN QUESTION: How often does the agent speak proactively, and on what trigger? Owner: whole group. Blocks: Phase 3 entirely.]`

This is open decision §4 in the hackathon working document. Phase 3 cannot start without it. Options recorded there: reactive only, scheduled digest, event-triggered, or hybrid.

`[OPEN QUESTION: Is the agent a neutral summariser or an opinionated participant? Owner: whole group. Blocks: Phase 3 delivery voice.]`

Open decision §5. Matters more once delivery is proactive rather than requested.

`[OPEN QUESTION: Where does structured long-term memory live — server filesystem, git repository, a database, or a hybrid? Owner: whole group. Blocks: Phase 2 registration storage and Phase 4 structured extraction.]`

Open decision §6. Distinct from conversation logging, which is ruled in D-5.

---

## Non-blocking — should be answered, but work can proceed

`[OPEN QUESTION: Should the vision document's Phase 1 / Phase 2 relationship-stewardship numbering be renamed to avoid colliding with the working document's Phase 1-4? Owner: vision document author.]`

See D-4. Mitigated for now by an explicit mapping table in each phase document.

`[OPEN QUESTION: Which three representative questions are the agreed acceptance set for the evaluation harness? Owner: product lead plus organisation representatives.]`

Carried forward from the execution synthesis, still unresolved. The evaluation harness needs these before the Phase 1 quality gate can run. Source packs supply candidate questions.

`[OPEN QUESTION: Which reuse permission or licence applies to organisation-provided sources and to generated public outputs? Owner: product lead. Resolve before source ingestion.]`

Carried forward from the execution synthesis. Each source pack states its own permission basis, so ingestion can begin, but the aggregate position for published outputs is unstated.

`[OPEN QUESTION: Is Telegram part of the acceptance test or only a stretch delivery adapter? Owner: product lead.]`

Carried forward. The technical specification treats it as conditional. The bot is live in mentions-only mode, which makes it tempting to treat as core — that would be a scope change, not a given.

`[OPEN QUESTION: Who holds the infrastructure-owner, recovery-custodian, budget-owner, technical-lead, and post-event-steward roles? Owner: event lead.]`

Carried forward from the execution synthesis and `00-start-here.md`, where every owner row is still marked "Confirmed? No." The access model requires the recovery custodian to be a different person from the infrastructure owner.

---

## Operational items with an owner and a date

`[OPEN QUESTION: When and how does the server's local working repository get connected to this public repository? Owner: technical lead. Target: the day after the hackathon.]`

As of 2026-08-20 the server holds two git repositories, both created during this session:

- `~/ark-local` — local-only, holds raw transcripts and unredacted notes, has no remote and must never gain one. [see: D-5]
- `~/ark` — a read-only clone of this repository, where the agent runs build units.

`~/ark` can fetch but cannot push: repository write authentication from the server is unresolved and is logged as an open blocker on the server, owner product lead. Until it is resolved the agent cannot open a pull request, so a human relays its commits. That is workable for a day and is not workable as a standing arrangement.

`[OPEN QUESTION: Should the agent's existing self-built artefacts on the server — the blocker log, the journal structure, and the local search scripts — be version-controlled in the local working repository, and should any of them be generalised into this repository as shared skills? Owner: technical lead.]`

None of them were under version control before 2026-08-20. The blocker log in particular is now load-bearing for the build protocol and is currently a single unversioned file in a home directory.

---

## Findings that may need a ruling

`[CONTRADICTS: proposal/hackathon-1/execution/06-roles-and-readiness.md]` That document cites three GitHub Actions workflows — `telegram-issues.yml`, `telegram-main-merge.yml`, and `telegram-tag-deploy.yml` — that were removed from the repository on 2026-08-06 in commit `8247400` ("Remove orphaned CI workflows"). The only workflow now present is `pages.yml`. The document's coordination guidance that depends on those workflows is stale. Owner: technical lead.

`[ASSUMPTION: The server has enough free memory to run a local embedding model alongside the Hermes runtime. Verify in Unit 5 before building the index.]` See D-3.

`[ASSUMPTION: The evaluation harness will be scored by a human or a stronger reviewing model. No scoring rubric has been agreed yet.]` Affects the Phase 1 quality gate.

---

## Resolved

| Date | Question | Ruling | Record |
|---|---|---|---|
| 2026-08-19 | Where do agent conversation logs live? (working document §2) | Hybrid — raw local, sanitised summaries published | D-5 |
| 2026-08-19 | How do organisations plug in their public sources? (working document §3) | Repository source packs with machine-readable frontmatter | D-6 |
| 2026-08-20 | Which embedding provider? | Local sentence-transformer, no API key | D-3 |
| 2026-08-20 | Where do build specifications live in the repository? | `plan/ark-agent/` | D-1 |
