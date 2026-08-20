# ARK Agent open questions

Unresolved questions that affect the build. Uses the repository's standard greppable markers. [see: AGENTS.md#5-citation-uncertainty--provenance-markers]

**Source for the open-decision numbers (§2 to §7) referenced throughout:** the hackathon working document, now committed at `proposal/hackathon-1/hackathon-working-doc-2026-08-18.md` (redacted for public publication). [see: proposal/hackathon-1/hackathon-working-doc-2026-08-18.md]


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

## Representative approval — how does sign-off actually happen?

`[OPEN QUESTION: By what mechanism does an organisation representative review generated answers and record approval, and what does approval attach to? Owner: whole group. Blocks: the Phase 1 gate, which cannot close without it.]`

This is the last thing standing between Phase 1 and done, and it is the one part
nobody has designed. Everything technical is built and evidenced. The gate says
"representatives find no unresolved material misrepresentation", and there is
currently no defined way for a representative to say so.

Four things need answers, and they are separable:

**Where does review happen?** A pull request comment on the review sheet keeps
everything in git and auditable, but assumes every representative is comfortable
in GitHub. A shared document is easier for non-technical reps and harder to
audit. In conversation with the agent is the friendliest and the least durable.
A hybrid — review anywhere, organiser records the outcome in the repository — is
the least elegant and probably the most likely to actually happen.

**What does approval attach to?** Approving *an answer* is precise and does not
generalise: the next question produces a new answer nobody has seen. Approving
*a source snapshot* generalises to every answer drawn from it, which is far more
useful, and is what makes the weekly re-capture question below tractable. The
snapshot is the better unit, but it means a representative is vouching for
answers they have not read.

**What is the standing of an unreviewed answer?** Today every generated record
carries `review_status: unreviewed` and nothing stops it being shown. Options
range from marking unreviewed output visibly, to withholding it entirely until a
representative has approved its sources.

**Who can approve, and can it be delegated?** Each organisation currently has one
named representative. If that person is away, does the organisation's material go
stale, or can approval be delegated, and to whom?

A concrete starting proposal, offered so the group is choosing rather than
starting from nothing: approval attaches to a **source snapshot**, is recorded as
a signed line in the source pack itself with a date and the snapshot's content
hash, and is given by a comment on the pull request that adds it. Answers drawn
only from approved snapshots are shown normally; anything else is marked
unreviewed. A changed hash on re-capture drops that source back to unapproved
until the representative confirms again.

That is a proposal, not a decision. The group should amend or replace it.

---

## Repository protection — a ratified requirement that is not met

`[OPEN QUESTION: The default branch has no protection rules. The technical specification lists "Repository rules protect the default branch from force push and deletion" among the checks required before Day 1. Enabling it needs repository admin. Owner: a repository admin.]`

Verified 2026-08-20: querying the branch-protection API for `main` returns 404,
meaning no rules exist. Seven collaborators hold write access. Any of them can
force-push or delete the default branch today, and nothing would stop it or
record that it happened.

This matters more than usual right now because a history rewrite is under
discussion. Deciding whether to rewrite is a group decision. Being *able* to
rewrite by accident is a different problem, and it is the one protection fixes.

Recommended: require pull requests or at minimum block force-push and deletion
on `main`. [see: proposal/hackathon-1/execution/05-technical-specification.md#9-acceptance-tests]

---

## Data governance

`[OPEN QUESTION: Does holding captured organisational material under legitimate interest meet EU requirements, and what does that oblige us to produce — a privacy notice, a legitimate-interest assessment, an erasure path? Owner: named by the product lead; unanswered.]`

The working position is legitimate interest rather than consent, on the grounds
that consent cannot be obtained from people whose published pages were read, and
that a consent record which nobody gave is worse than none. D-12 keeps
contributors and data subjects separate for this reason.

That position is reasoned but unverified. Nobody on the build has confirmed it
against the actual regulation, and the note it came from says plainly that it is
not legal advice. Treat it as the shape of an answer, not the answer.

What it would oblige us to produce if it holds: a short privacy notice saying who
holds what and why, a written legitimate-interest assessment, a working erasure
path, and evidence of minimisation. We currently have none of those. What we do
have is minimisation in practice — personal names and contact addresses found in
captured pages are redacted at capture time by an explicit auditable list.

`[OPEN QUESTION: Do captured snapshots and structured records move to the shared Postgres tables, and what is the boundary between what lives there and what stays in git? Owner: technical lead plus the contributor running those tables.]`

Ruled in principle: the corpus moves to Postgres. Unruled: the seam. The
canonical-versus-derived split already in place survives the move, since the
index is a disposable cache rebuildable from the corpus — only the loader
changes. What needs deciding is whether the source packs themselves move, or
whether git keeps the packs while Postgres holds the captured rows.

---

## Source freshness and re-approval

`[OPEN QUESTION: When a weekly re-capture finds that a source has changed, does the agent keep serving the last representative-approved snapshot until the new one is signed off, or does it index the new snapshot immediately and flag it as unreviewed? Owner: product lead plus organisation representatives.]`

Context. Sources are captured to snapshots and re-captured weekly, because the underlying pages change. `content_hash` on the Source record already makes change detection deterministic, and the technical specification already requires hashing normalised content and ingesting only changed snapshots. What it does not settle is what happens to a representative's approval when the content moves underneath it.

Permission and accuracy are granted against a specific capture, not against a URL in perpetuity. A representative who confirmed "yes, that describes us accurately" reviewed particular words. When those words change, that confirmation no longer covers what the agent will say.

Two candidate behaviours:

**Serve last-approved until re-approved.** The index keeps the previously signed-off snapshot. The new capture is staged and waits. Nothing the agent says is ever unreviewed. Cost: the corpus can go stale while waiting on a human, and staleness is invisible unless surfaced.

**Index immediately, mark unreviewed.** The new capture goes live and every claim drawn from it is flagged as not yet confirmed. Cost: the agent can state something no representative has checked, which is precisely the failure the accuracy gate exists to prevent.

The first is the current lean. It maps cleanly onto machinery the build already has: the index is built into a staging path and promoted atomically only after checks pass, so "representative has approved this snapshot" becomes one more promotion gate rather than new architecture. It also matches the existing rule that a failed ingestion leaves the active index untouched. [see: proposal/hackathon-1/execution/05-technical-specification.md#datastore-and-filesystem-boundary]

Whichever is chosen, the staleness has to be visible. A corpus quietly serving three-week-old approved content is a different failure from one quietly serving unreviewed fresh content, and both are worse than either being stated plainly.

`[ASSUMPTION: weekly is the right cadence. It is a guess, not a measurement. Revisit once there is evidence of how often these four sources actually change.]`

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
