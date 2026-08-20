# ARK Agent build decisions

Append-only record of decisions that shape the build. Newest at the bottom.

**Source for the open-decision numbers (§2 to §7) referenced throughout:** the hackathon working document, now committed at `proposal/hackathon-1/hackathon-working-doc-2026-08-18.md` (redacted for public publication). [see: proposal/hackathon-1/hackathon-working-doc-2026-08-18.md]


Every decision records what was chosen, what was rejected, why, and who ruled. A decision that is later reversed gets a new entry marked `SUPERSEDES` — the original entry is never edited or deleted.

Format:

```
## D-<n> · <title>
- **Date:** YYYY-MM-DD
- **Ruled by:** role
- **Status:** ACTIVE | SUPERSEDED by D-<n>
- **Decision:** one sentence
- **Rejected:** what else was considered
- **Why:** the reasoning
- **Affects:** which units or documents
```

---

## D-1 · Build documents live in `plan/ark-agent/`

- **Date:** 2026-08-20
- **Ruled by:** Event lead
- **Status:** ACTIVE
- **Decision:** Implementation specifications for the ARK Agent live in `plan/ark-agent/`, not under `proposal/hackathon-1/`.
- **Rejected:** A new `proposal/hackathon-1/build/` directory.
- **Why:** `00-start-here.md` states "Do not add separate planning files unless a real coordination problem has no home above," and the execution synthesis lists document types nobody may create. Build specifications genuinely have no home in the execution series, which is participant-facing. The root README sanctions `plan/` for "design specs, workstream breakdowns, and implementation sequencing" — that is exactly what these are. Using `plan/` respects the standing rule instead of requiring an exception to it.
- **Affects:** all phase documents; `proposal/hackathon-1/README.md` index entry

## D-2 · Application code follows the ratified repository shape

- **Date:** 2026-08-20
- **Ruled by:** Technical lead
- **Status:** ACTIVE
- **Decision:** Code uses the layout already specified in the technical specification — a flat `app/` package, `tests/`, `prompts/`, `scripts/`, with source packs under `proposal/hackathon-1/execution/source-packs/`.
- **Rejected:** A `src/` layout; a separate application repository.
- **Why:** The technical specification §6 already names the modules and test files. Inventing a second layout would create two incompatible conventions in one repository. The spec says "equivalent names are acceptable" but gives no reason to diverge. [see: proposal/hackathon-1/execution/05-technical-specification.md#6-repository-and-application-shape-to-prepare]
- **Affects:** Unit 0, and every unit thereafter

## D-3 · Embeddings run locally, not through a hosted API

- **Date:** 2026-08-20
- **Ruled by:** Event lead
- **Status:** ACTIVE
- **Decision:** Use a local sentence-transformer model for embeddings. No embedding API key is required.
- **Rejected:** OpenAI `text-embedding-3-small` as named in the technical specification; a provider-agnostic dual implementation.
- **Why:** The server currently holds no API keys of any kind. A local model removes a credential to provision, store, rotate, and keep out of git; costs nothing; runs offline; and is fully deterministic, which matters because the retrieval tests assert on exact ranking. It also honours portability principle UP-P4 — the pattern should not require a specific subscription. The technical specification permits this: the index is "a derived cache, not a system of record," and the retrieval baseline is explicitly replaceable. Generation still uses the configured Hermes model.
- **Affects:** Unit 5 (embedder), Unit 6 (index), Unit 7 (retrieval)
- **Verified 2026-08-20 (Unit 5):** assumption discharged. The ARK server reports 7.0 GiB available memory and 89 GB free disk with the runtime up. `all-MiniLM-L6-v2` loads and returns 384-dimensional unit-length vectors with no API key and no network call after the initial model download. The decision holds.

## D-4 · Phase numbering follows the working document, with an explicit mapping

- **Date:** 2026-08-20
- **Ruled by:** Event lead
- **Status:** ACTIVE
- **Decision:** These documents use Phase 1 through Phase 4 as numbered in the hackathon working document. Each phase document opens with a table mapping itself to the vision document's actual section numbers.
- **Rejected:** Renaming the phases after the vision's functional sections; amending the vision document's own phase language.
- **Why:** The group already speaks in Phase 1–4 from the working document, and breaking that vocabulary mid-hackathon costs more than it saves. But the vision document uses "Phase 1" and "Phase 2" for something entirely different — relationship stewardship — and has onboarding, activation, and synthesis as unnumbered sections. Leaving that collision undocumented would cause real confusion. Amending the vision document is a governance action requiring its author's sign-off, not something to bundle into a build specification.
- **Affects:** all phase documents
- **Note:** `[OPEN QUESTION: Should the vision document's Phase 1 / Phase 2 relationship-stewardship numbering be renamed to avoid the collision with the working document's Phase 1-4? Owner: vision document author.]`

## D-5 · Conversation logs are hybrid: local raw, public sanitised

- **Date:** 2026-08-19
- **Ruled by:** Event lead
- **Status:** ACTIVE
- **Decision:** Raw agent conversation transcripts stay in the local working repository on the server and are never pushed here. Only sanitised, role-labelled summaries are committed to this public repository. Redaction runs automatically as part of export.
- **Rejected:** Filesystem-only (not shareable, not portable); raw transcripts committed to this repository; a structured database as the primary store.
- **Why:** This resolves open decision §2 from the hackathon working document. The hybrid keeps the runtime's SQLite store as hot state while making the durable record portable markdown. The public half is constrained by standing repository policy, which forbids private conversations and chat excerpts without exception, and by the technical specification, which states raw logs are for operational evidence with "only a sanitised summary" published. [see: AGENTS.md#2-sensitive-information-policy-highest-priority--non-negotiable] [see: proposal/hackathon-1/execution/05-technical-specification.md#7b-update-ownership-and-rollback-map]
- **Affects:** the session-log skill; Phase 2 registration storage

## D-6 · Organisations plug in through repository source packs

- **Date:** 2026-08-19
- **Ruled by:** Event lead
- **Status:** ACTIVE
- **Decision:** Each participating organisation submits one source pack file at `proposal/hackathon-1/execution/source-packs/<organisation-slug>.md`. The human-authored markdown body follows the existing participation template. A YAML frontmatter block carries the machine-readable contract that the loader parses.
- **Rejected:** Organisations sharing links through Telegram; a conversational onboarding flow as the primary route.
- **Why:** This resolves open decision §3 from the hackathon working document. Repository packs are versioned, transparent, reviewable, and portable, and they match the technical specification's canonical-corpus model. Frontmatter rather than prose parsing means the loader has an exact contract and its tests can assert on literal values instead of matching regular expressions against English. The conversational route is not rejected permanently — it becomes "the agent drafts a pull request adding a source pack," which is Phase 2 work.
- **Affects:** Unit 1 (source pack schema), Unit 2 (loader)
- **Note:** The participation template suggests `source-packs/<slug>.md` and the technical specification shows `execution/source-packs/`. Both are satisfied by the path above. [see: proposal/hackathon-1/execution/02-participation-and-source-pack.md]

## D-7 · Agent skills use `SKILL.md` with frontmatter

- **Date:** 2026-08-20
- **Ruled by:** Technical lead
- **Status:** ACTIVE
- **Decision:** Skills in `skills/` are directories containing a `SKILL.md` file with YAML frontmatter carrying `name` and `description`.
- **Rejected:** Continuing the existing ad-hoc pattern (`<tool-name>-README.md` beside `<tool-name>.js`).
- **Why:** The repository has exactly one prior skill and no stated convention beyond "package it as a skill." `SKILL.md` with frontmatter is read natively by common agent runtimes, which makes the skills usable by a collaborator's own agent without translation — the stated goal for this folder. The existing skill is left untouched.
- **Affects:** `skills/ark-tdd-unit/`, `skills/ark-source-pack/`, `skills/ark-session-log/`

## D-8 · Test-driven development is introduced as the build method

- **Date:** 2026-08-20
- **Ruled by:** Event lead
- **Status:** ACTIVE
- **Decision:** Every unit is specified as a test first. Test files and fixture values are written into the phase documents by the specification author, not by the implementing agent.
- **Rejected:** Implementation-first with tests added afterwards; letting the implementing agent author its own tests.
- **Why:** The build is executed by a mid-capability model across many short sessions. Pre-written tests give each session an unambiguous, machine-checkable completion signal, which no amount of prose instruction achieves. Critically, an agent that writes its own tests tends to compute expected values by calling the code under test — producing a suite that passes regardless of correctness. Hand-derived literal fixtures are the only defence against that.
- **Affects:** every unit in every phase
- **Note:** No prior document in this repository specifies test-driven development. "Acceptance tests" elsewhere means human readiness gates, not automated tests. This decision introduces a new practice rather than extending an existing one.
