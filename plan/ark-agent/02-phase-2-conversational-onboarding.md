# Phase 2 — Conversational onboarding

**Scope tag:** `Stretch`.
**Status:** Contract depth. NOT executable. Do not start units from this document until the DECISIONS REQUIRED block below is cleared and the prior phase gate has passed.
**Prerequisite:** Phase 1 gate passed. [see: plan/ark-agent/01-phase-1-vertical-slice.md#phase-1-gate]

---

## What this phase proves

New members can move from discovering ARK to being known by the agent through a conversation, not a form, and their stated preferences are captured with explicit, revocable consent. The vision document is explicit that "the onboarding experience should be conversational rather than a static information dump," built around a small set of open questions: what brought the person to ARK, which themes or organisations interest them, what they would like to contribute, and which updates would be useful. [see: proposal/hackathon-1/arc-community-agent-vision.md#41-new-member-onboarding]

This is the commitment recorded in the hackathon working document — an external planning document, not itself committed to this repository; its relevant content is carried into this repository through `plan/ark-agent/decisions.md` and `plan/ark-agent/open-questions.md`:

> "three people can be onboarded conversationally, end-to-end, and their preferences are stored."

What proves this before Phase 3 opens, also from the working document:

> "onboarded people report the conversation felt useful, not scripted. If it feels like a form, keep iterating before adding proactive contact."

Nothing in this phase is speculative beyond what is marked. Where this document proposes a data shape or unit boundary that the source material does not specify directly, it is marked `[ASSUMPTION: ...]`.

---

## DECISIONS REQUIRED BEFORE THIS DOCUMENT IS EXECUTABLE

| # | Decision | Status | What it blocks | Owner |
|---|---|---|---|---|
| §2 | Conversation logging — hybrid, raw local / sanitised public | RESOLVED — D-5 | Was blocking storage of onboarding conversation content; now cleared. Onboarding conversations still follow D-5's rule: the raw transcript stays local, only a sanitised summary is ever committed. | Event lead (ruled) [see: D-5 in plan/ark-agent/decisions.md] |
| §6 | Structured long-term memory location — server filesystem, git repository, a database, or a hybrid | OPEN | The `Member` and `OnboardingSession` data contracts below cannot be finalised or built until this is ruled. Every unit in this phase's outline depends on it, directly or through Unit 2.3. | Whole group [see: plan/ark-agent/open-questions.md] |
| — | Phase 1 gate | Must have passed | The onboarding conversation grounds its questions in Phase 1's retrieval/answer substrate (organisation profiles, themes); nothing here works against an unproven index. | — [see: plan/ark-agent/01-phase-1-vertical-slice.md#phase-1-gate] |

Do not begin Unit 2.1 until §6 has a ruling. A schema built against the wrong storage medium is not a small fix later — it is a rewrite of every unit that follows it.

---

## Phase numbering — read this before citing a phase number

This document uses "Phase 2" as numbered in the hackathon working document. The vision document uses "Phase 1" and "Phase 2" to mean something completely different. Always say which document you mean.

| This document | Working document | Vision document | Technical specification |
|---|---|---|---|
| Phase 1 — vertical slice | Phase 1 `Committed` | §1 core operating loop; §6 technical architecture. *Not phase-numbered there.* | §1 technical objective; §8 prepared vertical slice |
| **Phase 2 — onboarding** | Phase 2 `Stretch` | §4.1 New-member onboarding. *Unnumbered.* | not covered |
| Phase 3 — member activation | Phase 3 `Stretch` | §4.2 Ongoing member activation. *Unnumbered.* | not covered |
| Phase 4 — cross-org synthesis | Phase 4 `Stretch` | §4.4 Community synthesis. *Unnumbered. Tech-stack awareness appears nowhere in the vision.* | not covered |

The vision document's own "Phase 1 / Phase 2" (§4.11) refers to relationship stewardship — maintaining relationships, then suggesting alignments. That is closest to this document's Phase 3 and beyond. It is not this phase. [see: D-4 in plan/ark-agent/decisions.md]

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

# GOVERNANCE CONSTRAINTS

These are not guidance. They are properties the units below must have, and each
one is checkable rather than promised.

**Contributors and data subjects never share a record.** A contributor is
someone who adds material; their basis is participation, recorded as an
agreement plus a timestamp at the moment access is granted. A data subject is
someone appearing inside captured material; their basis is legitimate interest
and consent is never sought from them. [see: D-12]

How this is enforced rather than asserted: `lawful_basis` is a validated field
with `consent` and `legitimate-interest` as distinct values, the onboarding units
write only contributor records, and nothing in the ingest path can write a
consent row. A data subject cannot acquire one by accident, because no code path
exists that would create it.

**Consent is revocable and revocation is a unit, not a policy.** Unit 2.4 exists
because a consent record with no working withdrawal is a record of nothing.

**Minimisation is a design constraint on the schema.** Hold what the coordination
actually needs. Every field added to `Member` should survive the question "what
breaks if this is absent", and a field that only exists because it might be
useful later does not go in.

**Sensitivity governs who sees a row.** `commons` is visible in the ecosystem
view; anything else is scoped and must not surface in a cross-organisation
answer. The personal feed and the ecosystem feed are one query with different
scoping, not two systems.

---

# DATA CONTRACTS

The `Organisation`, `Source`, `Chunk`, and generated `Answer`/digest shapes are ratified in Phase 1 and reused unchanged here. [see: plan/ark-agent/01-phase-1-vertical-slice.md#data-contracts] The records below are new to this phase. They are **not yet ratified** — refine them once §6 above clears. `[ASSUMPTION: field names and types below are this document's own proposal, drawn from vision §4.1, §4.2, and §7.9, not a ratified contract.]`

### Member

```yaml
member_id: generated identifier          # never a real name; never a public slug
joined_at: ISO-8601 timestamp
consent:
  status: granted | revoked
  scope: [permitted use, ...]            # e.g. "proactive-contact", "interest-personalisation"
  granted_at: ISO-8601 timestamp
  revoked_at: ISO-8601 timestamp or null
permitted_channel: telegram-dm | none
interests: [theme, ...]                  # drawn from participating Organisation.themes where possible
update_frequency: daily | weekly | on-request
registration_source: onboarding-conversation | manual
```

Consent is a first-class field on `Member`, not a boolean flag borrowed from some other record. The vision document treats consent, inspection, correction, and deletion as member rights, not agent conveniences. [see: proposal/hackathon-1/arc-community-agent-vision.md#79-relationship-consent-and-member-agency]

### OnboardingSession

```yaml
session_id: generated identifier
member_id: generated identifier or null   # null until the session completes and a Member is created
started_at: ISO-8601 timestamp
completed_at: ISO-8601 timestamp or null
channel: telegram-dm
answers:
  what_brought_you: text or null
  themes_of_interest: [theme, ...] or null
  what_to_contribute: text or null
  useful_update_types: [text, ...] or null
outcome: registered | declined | abandoned
```

The four `answers` fields map directly to the vision document's four onboarding questions. [see: proposal/hackathon-1/arc-community-agent-vision.md#41-new-member-onboarding]

**Never store**, in this public repository or in `OnboardingSession.answers`: a real name, a phone number, an email address, or the raw conversational transcript — only the structured answers extracted from it. No private participant identifier is ever committed to this repository, in any record, at any depth. [see: AGENTS.md#2-sensitive-information-policy-highest-priority--non-negotiable]

---

# UNIT OUTLINE

Roughly seven units, numbered 2.1–2.7 to keep phase and unit visually paired. Renumber to a flat sequence when this document is deepened, if the ledger format requires it.

## Unit 2.1 — Member and consent schema

**Story.** As the registration layer, I need a strict schema for consent state so an onboarding flow can never silently register someone without explicit, scoped permission.
**Depends on:** Phase 1 gate.
**Files:** `app/member.py`
**Test file:** `tests/test_member_schema.py`
**Gate:** a `Member` missing `consent.status`, or carrying an `update_frequency` outside the ratified enum, is rejected at construction.

## Unit 2.2 — Onboarding conversation flow

**Story.** As a new person talking to the agent, I want to be asked the four onboarding questions one at a time, in order, so the conversation feels like a conversation and not a form.
**Depends on:** Unit 2.1.
**Files:** `app/onboarding.py`
**Test file:** `tests/test_onboarding_flow.py`
**Gate:** the flow advances to the next question only once the current one has a captured answer, and terminates in exactly one of `registered`, `declined`, `abandoned`.

## Unit 2.3 — Onboarding persistence

**Story.** As the agent, I need a completed onboarding session written to durable storage so a person's stated preferences survive past the conversation that produced them.
**Depends on:** Unit 2.2, and the §6 memory-location ruling above.
**Files:** `app/onboarding_store.py`
**Test file:** `tests/test_onboarding_store.py`
**Gate:** a completed `OnboardingSession` round-trips through storage into a persisted `Member` with `consent` intact.

## Unit 2.4 — Consent revocation

**Story.** As a member, I need to be able to withdraw consent at any time and have that take effect immediately, so my agreement to be contacted stays genuinely revocable.
**Depends on:** Unit 2.1, Unit 2.3.
**Files:** `app/consent.py`
**Test file:** `tests/test_consent_revocation.py`
**Gate:** revoking consent flips `consent.status` to `revoked` without deleting the record, and a revoked `Member` is excluded from every contact-eligible query.

## Unit 2.5 — First-message welcome

**Story.** As a new Telegram joiner, I want the agent to greet me and ask permission before it asks me anything else, so I am never onboarded without knowing it is happening.
**Depends on:** Unit 2.2.
**Files:** `app/channel_adapter.py`
**Test file:** `tests/test_first_message_welcome.py`
**Gate:** a first-seen joiner is greeted and asked permission before Unit 2.2's first question fires; a person who already has a `Member` record is never re-greeted.

## Unit 2.6 — Registration capture

**Story.** As the agent, I need the flow's captured answers to map onto a `Member`'s `interests` and `update_frequency` fields without silent defaulting, so what a person actually said is what gets stored.
**Depends on:** Unit 2.3.
**Files:** `app/registration.py`
**Test file:** `tests/test_registration.py`
**Gate:** every non-empty answer in `OnboardingSession.answers` is traceable to a specific `Member` field; no field is populated from a default when the corresponding answer is empty.

## Unit 2.7 — Onboarding command surface

**Story.** As a builder verifying the phase, I need one command that runs a fixture conversation end-to-end so three people can be onboarded and inspected without a live Telegram session.
**Depends on:** Units 2.1–2.6.
**Files:** `scripts/onboard`, `app/cli.py` (extended)
**Test file:** `tests/test_onboarding_cli.py`
**Gate:** three fixture conversations, run through the command, produce three persisted, consented `Member` records with distinct `member_id`s.

Full test specifications — the pre-written pytest bodies, exact fixture values, and literal expected outputs — are written when this document is deepened, after the DECISIONS REQUIRED block above clears.

---

# PHASE 2 GATE

Phase 2 is complete only when every item passes.

### Automated — must be green

- [ ] Units 2.1 through 2.7 all marked `DONE` in the ledger
- [ ] `./scripts/test` passes from a clean checkout, Phase 1's suite included
- [ ] No credential-like value and no private participant identifier exists anywhere in the repository or its history
- [ ] A revoked member's consent state is honoured by every unit that reads `Member`
- [ ] Three fixture onboarding conversations complete end-to-end and each produces a stored `Member`

### Human — must be judged

- [ ] Three real people have been onboarded conversationally, end-to-end
- [ ] Their preferences (interests, update frequency, permitted channel) are stored correctly
- [ ] Onboarded people report the conversation felt useful, not scripted
- [ ] Consent language shown during onboarding is clear about what is being agreed to and how to withdraw it
- [ ] Known manual steps and limitations are written down
- [ ] A human has reviewed and merged the work

**The blocking criterion is the working document's own quality bar, not the automated suite.** "If it feels like a form, keep iterating before adding proactive contact." A green test suite behind a conversation nobody enjoyed is not a passed gate. Do not open Phase 3 on an onboarding flow that has not cleared this bar.

---

## What this phase deliberately does not do

Not in scope for Phase 2. `[ASSUMPTION: this list is inferred from the vision document and the working document's phase sequencing, not itself a ratified decision entry.]`

- Proactive or scheduled contact of any kind — that is Phase 3, and the working document places it after Phase 2's conversation quality is proven, not alongside it
- Deep behavioural profiling; the vision document is explicit that personalisation "should not attempt deep behavioural profiling" even once it exists [see: proposal/hackathon-1/arc-community-agent-vision.md#45-personalised-updates]
- Alignment or introduction suggestions between members — that is vision §4.11 Phase 2 (relationship stewardship), a different numbering track entirely [see: D-4 in plan/ark-agent/decisions.md]
- Onboarding through any channel other than the one adapter this phase builds
- Storing a raw onboarding transcript in this repository, at any point — only the structured `OnboardingSession.answers` extracted from it, per D-5
- A second agent runtime profile for the onboarding flow
