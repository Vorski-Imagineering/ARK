# Phase 4 — Cross-org synthesis

**Scope tag:** `Stretch`.
**Status:** Contract depth. NOT executable. Do not start units from this document until the DECISIONS REQUIRED block below is cleared and the prior phase gate has passed.
**Prerequisite:** Phase 1 gate passed, plus at least three live source packs. [see: plan/ark-agent/01-phase-1-vertical-slice.md#phase-1-gate]

This phase's stated prerequisite is Phase 1, not Phase 3 — its retrieval substrate is Phase 1's index, not Phase 3's delivery machinery. One unit in this phase's outline (Unit 4.7 below) reaches back into Phase 2/3 consent and delivery infrastructure; that dependency is called out on the unit itself rather than promoted to a phase-level prerequisite, since the rest of the phase does not need it. `[ASSUMPTION: this split is this document's own judgement call, not a ruling. A reviewer could reasonably require the full Phase 3 gate before this phase opens at all.]`

---

## What this phase proves

The agent can look across every participating organisation's own sources and answer questions about tools and technology that only make sense in aggregate — which organisations use which tools, and where two organisations' stacks overlap — with each claim carrying a source citation back to the organisation's own public material. This function does not exist in the vision document under any name; the closest the vision gets is "community synthesis," which is about projects, events, and themes, not tooling. [see: proposal/hackathon-1/arc-community-agent-vision.md#44-community-synthesis]

Definition of done, from the hackathon working document — an external planning document; its relevant content is carried into this repository through `plan/ark-agent/decisions.md` and `plan/ark-agent/open-questions.md`:

> "the agent can answer three specific interoperability questions with sourced evidence about the participating orgs."

`[OPEN QUESTION: which three specific interoperability questions are the agreed acceptance set? Owner: product lead plus organisation representatives — the same open pattern as Phase 1's evaluation harness question set.]` [see: plan/ark-agent/01-phase-1-vertical-slice.md#unit-13--evaluation-harness]

---

## DECISIONS REQUIRED BEFORE THIS DOCUMENT IS EXECUTABLE

| # | Decision | Status | What it blocks | Owner |
|---|---|---|---|---|
| — | Phase 1 gate | Must have passed | The retrieval/index substrate every extraction and query unit in this phase reads from | — [see: plan/ark-agent/01-phase-1-vertical-slice.md#phase-1-gate] |
| — | At least three organisations represented by live, ingested source packs — not fixture packs | OPEN / operational, not a governance ruling | `TechStackEntry` extraction has nothing real to extract from with fewer than three; the "cross-org" half of this phase's name is meaningless with two | Event lead, participating organisations |
| §6 | Memory persistence — where structured long-term memory lives: server filesystem, git repository, a database, or a hybrid | OPEN | `TechStackEntry` and `CrossOrgPattern` are structured extracted records, not generated text. They need a home, and that home is the same unresolved question Phase 2 faces for registration storage. Building extraction before the store is ruled means writing it twice. | Whole group [see: plan/ark-agent/open-questions.md] |
| — | Tech-stack awareness — the whole premise of this phase | **NOT PRESENT anywhere in the vision document.** Confirmed by search: the phrase does not occur in `arc-community-agent-vision.md`, nor in any proposal or working document in this repository. It appears to be the event lead's own proposal, layered onto vision §4.4's "community synthesis" and the longer-term §8 vision of an "inter-organisational intelligence network." | The acceptance criteria authored fresh in this document (Units 4.1–4.6) rest on nobody's ratified requirement but the event lead's own. Every criterion below needs product-lead sign-off before it is binding, not only technical-lead sign-off. | Product lead — ratification needed, not yet given |

This phase carries more unratified surface area than Phases 2 or 3. Phases 2 and 3 build out functions the vision document names explicitly (§4.1, §4.2), with open decisions blocking *how*. Phase 4 builds a function the vision document never names at all, with an open decision blocking *whether it should exist in this form*. Treat the DATA CONTRACTS and UNIT OUTLINE below as a considered proposal awaiting a decision, not as inherited scope.

---

## Phase numbering — read this before citing a phase number

This document uses "Phase 4" as numbered in the hackathon working document. The vision document uses "Phase 1" and "Phase 2" to mean something completely different, and does not number this phase's function at all. Always say which document you mean.

| This document | Working document | Vision document | Technical specification |
|---|---|---|---|
| Phase 1 — vertical slice | Phase 1 `Committed` | §1 core operating loop; §6 technical architecture. *Not phase-numbered there.* | §1 technical objective; §8 prepared vertical slice |
| Phase 2 — onboarding | Phase 2 `Stretch` | §4.1 New-member onboarding. *Unnumbered.* | not covered |
| Phase 3 — member activation | Phase 3 `Stretch` | §4.2 Ongoing member activation. *Unnumbered.* | not covered |
| **Phase 4 — cross-org synthesis** | Phase 4 `Stretch` | §4.4 Community synthesis. *Unnumbered. Tech-stack awareness appears nowhere in the vision.* | not covered |

The vision document's own "Phase 1 / Phase 2" (§4.11) refers to relationship stewardship — maintaining relationships, then suggesting alignments. That is not this phase, though Unit 4.7's connection prompts borrow its consent discipline in miniature. [see: D-4 in plan/ark-agent/decisions.md] [see: proposal/hackathon-1/arc-community-agent-vision.md#411-relationship-stewardship-and-alignment]

---

# BUILD PROTOCOL

*Reproduced in full so this document is executable on its own. Do not replace with a cross-reference. Canonical copy: `plan/ark-agent/00-build-protocol.md`.*

## The two agent identities

You are operating as **builder**: you may read the repository, write code and tests on a branch, run tests, and open a pull request. You may not push to the default branch, merge your own pull request, or edit the agent's runtime configuration.

The **service** identity — the participant-facing agent that answers questions — is read-only over sources and the index. Do not confuse the two.

## Session rules

**One unit per session.** Do exactly one unit. Stop when it is done, even if you have capacity. Long sessions drift; earlier instructions lose force and errors compound silently.

**The file system is the memory.** Never rely on recalling a previous session. State lives in `plan/ark-agent/ledger.md`, `decisions.md`, `open-questions.md`, and `~/need-human-help.md`.

**Cold start procedure**, run before anything else:

1. Read `plan/ark-agent/ledger.md`. Find the last row with status `DONE`.
2. The next unit is the next numbered unit below.
3. Read that unit's section in full.
4. Confirm its stated dependencies are all `DONE` in the ledger.
5. Run `./scripts/test`. It must be green before you start. If red, stop and fix that first.
6. State in your first message which unit you are starting and the result of step 5.

If the ledger has no `DONE` rows, start at Unit 0.

## The unit loop

**Step 1 — RED.** Create the test file exactly as given in the unit. Copy it as written. Run the test command. It must **fail**. A test that passes before the implementation exists is broken — stop and report it.

**Step 2 — GREEN.** Create only the implementation file named in the unit. Write the minimum code that makes the given tests pass. Do not add functions, options, or abstraction layers no test exercises.

**Step 3 — GATE.** Run the unit's test command, then `./scripts/test`. Both must be fully green — not "green except one unrelated failure."

**Step 4 — LEDGER.** Append one row to `plan/ark-agent/ledger.md`.

**Step 5 — STOP.** Report the unit number, files touched by exact path, the test result line, and anything you noticed but did not act on. Then stop.

## Forbidden moves

- **Never edit a test to make it pass.** The tests are the specification. If a test seems wrong it may genuinely be wrong — record a blocker and stop.
- **Never edit a fixture to match your output.** Fixture values were derived by hand, independently of any implementation.
- **Never compute an expected value by calling the code under test.** Expected values are written literally in the test.
- **Never use `skip`, `xfail`, or a commented-out assertion** to get past a failure.
- **Never proceed on red.**
- **Never mark a unit `DONE` you did not complete.** `BLOCKED` and `PARTIAL` are legitimate.
- **Never modify `~/.hermes/`** — not `config.yaml`, not `.env`, not `SOUL.md`, not the skills directory.
- **Never commit a credential.** Check for `sk-`, `key=`, `token=`, `password=`, `Bearer ` before every commit.

## When you are blocked

After more than two tool calls on the same problem, stop and write an entry in `~/need-human-help.md` using its existing format, then append a `BLOCKED` row to the ledger. A reported blocker is a successful session outcome. A plausible workaround nobody reviewed is not.

## Public repository rules

This repository is public and CC0. Before writing any file confirm: no private individuals' names (use role labels), no private conversations or chat excerpts, no credentials, no internal URLs or ticket identifiers, no personal contact details, no non-public organisational material. If any check fails, do not write the file — write a blocker and ask. [see: AGENTS.md#2-sensitive-information-policy-highest-priority--non-negotiable]

Raw agent conversation transcripts are never committed here.

## Two kinds of test

**Deterministic components** — loader, normaliser, chunker, index, retrieval ranking — get real unit tests with literal expected values. Exact strings, exact counts, exact identifiers.

**Model-dependent components** — answer, digest — take the model as an injected dependency and are tested with a `FakeLLM` returning canned output. Tests assert on *structure*: that every citation resolves to a real `source_id`, that no citation points outside the approved packs, that empty retrieval produces an explicit refusal, that retrieved text is delimited as quoted evidence. Never call a real model in the test suite.

**Answer quality** — "would a representative sign off on this digest?" — is not a unit test. It runs once per phase against the real model over a fixed question set, scored by a human or a stronger reviewing model. It lives in `evals/`, never in `tests/`, and never gates a unit.

## Git discipline

Branch per unit, named `build/phase-<n>-unit-<m>`. Open a draft pull request when you begin, before code exists. Commit after the gate passes, one commit per unit, message `phase-<n> unit-<m>: <title>`. Never force-push. Never merge your own pull request.

---

# DATA CONTRACTS

Reuses `Organisation`, `Source`, `Chunk`, and generated `Answer`/digest from Phase 1. [see: plan/ark-agent/01-phase-1-vertical-slice.md#data-contracts] This phase's new records are organisation-level, not member-level, so they carry less consent surface than Phase 2/3 — but Unit 4.7's connection prompts, once they reach a person, inherit Phase 2's `Member`/consent contract in full. Everything below is **not yet ratified**, and awaits the product-lead ratification named in DECISIONS REQUIRED above. `[ASSUMPTION: field names, types, and the category taxonomy below are this document's own proposal.]`

### TechStackEntry

```yaml
organisation_id: stable-public-slug
tool_name: public tool or platform name, as stated in the cited source
category: text                              # [ASSUMPTION: no taxonomy is ratified; free text pending product-lead input]
evidence_source_id: stable-source-id        # must resolve to a real ingested Source
confidence: low | medium | high
extracted_at: ISO-8601 timestamp
```

Never inferred from outside knowledge — every entry must trace to a specific `Source` an organisation itself contributed, per the same untrusted-content boundary Phase 1 Unit 8 established for retrieved text generally. [see: plan/ark-agent/01-phase-1-vertical-slice.md#unit-8--prompt-builder-and-the-untrusted-content-boundary]

### CrossOrgPattern

```yaml
pattern_id: generated identifier
kind: shared-tool | complementary-stack
organisation_ids: [stable-public-slug, ...]   # two or more
evidence: [stable-source-id, ...]             # every source backing the pattern
description: generated text
detected_at: ISO-8601 timestamp
```

No `TechStackEntry` or `CrossOrgPattern` names a person — both are organisation-level records. Unit 4.7's connection prompts are the one place this phase crosses back into member territory, and they inherit Phase 2's full consent contract there, not a lighter version of it. No private participant identifier is ever committed to this repository, in this phase's records or in Phase 2/3's. [see: AGENTS.md#2-sensitive-information-policy-highest-priority--non-negotiable]

---

# UNIT OUTLINE

Roughly seven units, numbered 4.1–4.7.

## Unit 4.1 — TechStackEntry schema and extraction prompt contract

**Story.** As the extraction layer, I need a strict schema plus a versioned prompt so tech-stack extraction is auditable the same way Phase 1's answer prompt is.
**Depends on:** Phase 1 gate.
**Files:** `app/techstack.py`, `prompts/techstack-extract.md`
**Test file:** `tests/test_techstack_schema.py`
**Gate:** a `TechStackEntry` whose `evidence_source_id` does not resolve to a real ingested `Source` is rejected at construction.

## Unit 4.2 — Extraction run

**Story.** As the agent, I need to run extraction over one organisation's ingested sources and get back only entries backed by real evidence.
**Depends on:** Unit 4.1.
**Files:** `app/techstack_extract.py`
**Test file:** `tests/test_techstack_extract.py`
**Gate:** with a `FakeLLM`, every produced `TechStackEntry` cites a `source_id` present in the index; an organisation with no matching evidence produces zero entries, never a guess — the same discipline as Phase 1's insufficient-evidence rule. [see: plan/ark-agent/01-phase-1-vertical-slice.md#unit-9--answer-function]

## Unit 4.3 — Tool-usage query

**Story.** As a member, I want to ask "which organisations use tool X?" and get a sourced answer, not a guess.
**Depends on:** Unit 4.2.
**Files:** `app/interop_query.py`
**Test file:** `tests/test_tool_usage_query.py`
**Gate:** querying a tool name with no matching `TechStackEntry` returns an explicit empty result, never a fabricated organisation.

## Unit 4.4 — Stack-overlap query

**Story.** As a member, I want to ask "which pairs of organisations have overlapping stacks?" and get pairs backed by two independent, cited entries.
**Depends on:** Unit 4.2.
**Files:** `app/interop_query.py` (shared module with Unit 4.3)
**Test file:** `tests/test_stack_overlap_query.py`
**Gate:** an overlap pair is reported only when both organisations have their own `TechStackEntry` naming the same normalised `tool_name`, each with its own `evidence_source_id`.

## Unit 4.5 — Cross-org pattern detection

**Story.** As the agent, I need to surface a `CrossOrgPattern` when the same tool or a complementary stack appears across organisations, so a member doesn't have to run the queries themselves.
**Depends on:** Unit 4.4.
**Files:** `app/pattern_detect.py`
**Test file:** `tests/test_pattern_detect.py`
**Gate:** every detected pattern's `evidence` list resolves entirely to real `source_id`s; a pattern naming fewer than two organisations is rejected.

## Unit 4.6 — The three interoperability questions, answered

**Story.** As a product lead, I need the phase's own definition-of-done question set answerable end-to-end through the standard `Answer` contract, so quality can be judged the same way Phase 1's answers were.
**Depends on:** Unit 4.5, Phase 1's `answer()`.
**Files:** `app/interop_answer.py`
**Test file:** `tests/test_interop_answer_evidence.py`
**Gate:** each of the three fixed interoperability questions produces an `Answer` whose `cited_source_ids` is non-empty and every id resolves to a real ingested `Source`.

## Unit 4.7 — Cross-org connection prompts (start light)

**Story.** As a member with a relevant interest, I want an occasional, low-pressure prompt pointing at a cross-org pattern that might matter to me — nothing that reads as an automated introduction.
**Depends on:** Unit 4.5, and Phase 2's `Member`/consent contract plus Phase 3's invitation rate-limit pattern (Unit 3.7) — this unit reaches outside this phase's stated prerequisite; see the note under the document title.
**Files:** `app/connection_prompt.py`
**Test file:** `tests/test_connection_prompt.py`
**Gate:** a prompt fires only for a member with active consent and a matching `interest_filter`, is rate-limited by the same cap as Unit 3.7, and never states a `CrossOrgPattern` as settled fact — it carries the same uncertainty language the vision document requires of alignment suggestions generally. [see: proposal/hackathon-1/arc-community-agent-vision.md#411-relationship-stewardship-and-alignment]

Full test specifications are written when this document is deepened, after the DECISIONS REQUIRED block above clears and product-lead ratification of the acceptance criteria has been obtained.

---

# PHASE 4 GATE

Phase 4 is complete only when every item passes.

### Automated — must be green

- [ ] Units 4.1 through 4.7 all marked `DONE` in the ledger
- [ ] `./scripts/test` fully green, Phases 1–3 included where Unit 4.7 depends on them
- [ ] Every `TechStackEntry` and `CrossOrgPattern` in the corpus resolves its evidence to a real `Source`
- [ ] No `TechStackEntry` or `CrossOrgPattern` names a person
- [ ] The three fixed interoperability questions (Unit 4.6) each produce a cited `Answer`

### Human — must be judged

- [ ] At least three organisations' real source packs are ingested, not fixtures
- [ ] Product lead has ratified this phase's acceptance criteria — see the DECISIONS REQUIRED block above
- [ ] Organisation representatives confirm their own tech-stack entries are accurate
- [ ] The three agreed interoperability questions have been tested against real answers
- [ ] Connection prompts, where triggered, read as light and optional, not as automated matchmaking
- [ ] Known manual steps and limitations are written down
- [ ] A human has reviewed and merged the work

**The blocking criterion is the working document's own definition of done**: three specific interoperability questions, answered with sourced evidence, about real participating organisations. A fixture-backed green suite does not satisfy this — the evidence has to be real.

---

## What this phase deliberately does not do

- Agent-to-agent protocols between organisations' own agents — that is vision §8's longer-term vision, explicitly framed as a later stage [see: proposal/hackathon-1/arc-community-agent-vision.md#8-longer-term-vision]
- A structured organisational-profile standard or a public dashboard
- Full alignment-suggestion mechanics — matching needs to offers, scoring potential collaborations, running the two-sided consent flow the vision document describes for vision §4.11 Phase 2. Unit 4.7 is a narrow, light-touch subset of that, not an implementation of it. [see: D-4 in plan/ark-agent/decisions.md]
- OCR or broad document-format extraction beyond what Phase 1's loader already supports [see: plan/ark-agent/01-phase-1-vertical-slice.md#what-phase-1-deliberately-does-not-do]
- Any claim about an organisation's tech stack that does not cite a `Source` the organisation itself contributed
