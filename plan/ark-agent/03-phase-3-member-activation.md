# Phase 3 — Member activation

**Scope tag:** `Stretch`.
**Status:** Contract depth. NOT executable. Do not start units from this document until the DECISIONS REQUIRED block below is cleared and the prior phase gate has passed.
**Prerequisite:** Phase 2 gate passed. [see: plan/ark-agent/02-phase-2-conversational-onboarding.md#phase-2-gate]

---

## What this phase proves

A registered member can set a delivery rhythm, receive updates shaped by their stated interest, and change that rhythm and have the change actually take effect on the next delivery — not the one already in flight. The vision document frames this as maintaining "a useful rhythm that keeps members connected to the living activity of ARC," explicitly not "constant automated chatter." [see: proposal/hackathon-1/arc-community-agent-vision.md#42-ongoing-member-activation]

Definition of done, from the hackathon working document — an external planning document; its relevant content is carried into this repository through `plan/ark-agent/decisions.md` and `plan/ark-agent/open-questions.md`:

> "a member can register, choose weekly frequency + a specific interest, receive their first weekly summary shaped by that interest, change to daily, and receive a daily summary the next day."

That sentence is also this phase's acceptance test. Unlike Phase 2, there is no separate quality bar layered on top of it — the working document treats the mechanism itself, working end to end for a real member, as the proof.

---

## DECISIONS REQUIRED BEFORE THIS DOCUMENT IS EXECUTABLE

| # | Decision | Status | What it blocks | Owner |
|---|---|---|---|---|
| §4 | Proactive cadence and trigger — reactive only, scheduled digest, event-triggered, or hybrid | OPEN. The working document states this "requires group input before starting." | The entire scheduled-delivery mechanism (Units 3.3, 3.5, 3.6) has no defined trigger without it. | Whole group [see: plan/ark-agent/open-questions.md] |
| §5 | Neutral summariser vs opinionated participant — the agent's delivery voice | OPEN | What tailored digest content actually says (Unit 3.4) and how invitations are worded (Unit 3.7) | Whole group [see: plan/ark-agent/open-questions.md] |
| §6 | Structured long-term memory location — server filesystem, git repository, a database, or a hybrid | OPEN | `DeliveryPreference` and `ScheduledDelivery` storage — the same open decision blocking Phase 2's `Member`/`OnboardingSession`, now also blocking this phase's records | Whole group [see: plan/ark-agent/open-questions.md] |
| — | Phase 2 gate | Must have passed | Every unit — there is no member to schedule delivery for until Phase 2's registration flow is proven, with real people, not fixtures | — [see: plan/ark-agent/02-phase-2-conversational-onboarding.md#phase-2-gate] |

§4 is the load-bearing one. The working document does not merely list it as open — it says Phase 3 cannot start without it. Do not treat a plausible default (for example, "reactive only for now") as a substitute for the ruling.

---

## Phase numbering — read this before citing a phase number

This document uses "Phase 3" as numbered in the hackathon working document. The vision document uses "Phase 1" and "Phase 2" to mean something completely different. Always say which document you mean.

| This document | Working document | Vision document | Technical specification |
|---|---|---|---|
| Phase 1 — vertical slice | Phase 1 `Committed` | §1 core operating loop; §6 technical architecture. *Not phase-numbered there.* | §1 technical objective; §8 prepared vertical slice |
| Phase 2 — onboarding | Phase 2 `Stretch` | §4.1 New-member onboarding. *Unnumbered.* | not covered |
| **Phase 3 — member activation** | Phase 3 `Stretch` | §4.2 Ongoing member activation. *Unnumbered.* | not covered |
| Phase 4 — cross-org synthesis | Phase 4 `Stretch` | §4.4 Community synthesis. *Unnumbered. Tech-stack awareness appears nowhere in the vision.* | not covered |

The vision document's own "Phase 1 / Phase 2" (§4.11) refers to relationship stewardship — maintaining relationships, then suggesting alignments. That is closest to this document's Phase 3 and beyond, but it is not the same thing as this phase. Relationship stewardship's own Phase 1 (maintaining relationships) is the broader frame this phase's scheduled delivery sits inside; its own Phase 2 (suggesting alignment) is out of scope here entirely. [see: D-4 in plan/ark-agent/decisions.md] [see: proposal/hackathon-1/arc-community-agent-vision.md#411-relationship-stewardship-and-alignment]

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

Reuses `Organisation`, `Source`, `Chunk`, and generated `Answer`/digest from Phase 1 [see: plan/ark-agent/01-phase-1-vertical-slice.md#data-contracts], and `Member`, `OnboardingSession` from Phase 2 [see: plan/ark-agent/02-phase-2-conversational-onboarding.md#data-contracts]. The records below are new to this phase and **not yet ratified**. `[ASSUMPTION: field names and types below are this document's own proposal, drawn from vision §4.2 and §4.5, not a ratified contract.]`

### DeliveryPreference

```yaml
member_id: generated identifier            # references Member.member_id
frequency: daily | weekly | on-request
interest_filter: [theme, ...] or null       # null = unfiltered
channel: telegram-dm | none
updated_at: ISO-8601 timestamp
```

### ScheduledDelivery

```yaml
delivery_id: generated identifier
member_id: generated identifier
scope: daily-summary | weekly-summary
scheduled_for: ISO-8601 timestamp
sent_at: ISO-8601 timestamp or null
channel: telegram-dm
cited_source_ids: [stable-source-id, ...]
status: scheduled | sent | skipped-no-consent | failed
```

### DeliveryLog

```yaml
delivery_id: generated identifier
member_id: generated identifier
attempted_at: ISO-8601 timestamp
status: sent | failed | skipped-no-consent
channel: telegram-dm
```

The log is append-only JSONL, one entry per attempted delivery, identifiers and status only — never a message body, never prompt text, never question text. Same discipline as Phase 1's usage log. [see: plan/ark-agent/01-phase-1-vertical-slice.md#unit-11--usage-and-cost-logging]

Every record above carries or references `member_id`, so every record above touches a person. `ScheduledDelivery.status` must respect `Member.consent.status`: a revoked member produces `skipped-no-consent`, never a silently dropped row and never a delivery. No private participant identifier — name, phone, email, message content — is ever committed to this repository, in these records or anywhere else. [see: AGENTS.md#2-sensitive-information-policy-highest-priority--non-negotiable]

---

# UNIT OUTLINE

Roughly seven units, numbered 3.1–3.7.

## Unit 3.1 — DeliveryPreference schema

**Story.** As the scheduling layer, I need a strict schema for a member's delivery choices so an invalid frequency or channel can never reach the scheduler.
**Depends on:** Phase 2 gate.
**Files:** `app/delivery_preference.py`
**Test file:** `tests/test_delivery_preference_schema.py`
**Gate:** a `DeliveryPreference` with a frequency or channel outside the ratified enum is rejected at construction.

## Unit 3.2 — Preference change semantics

**Story.** As a member, when I change my frequency or interest, I want that to apply to my next delivery, not retroactively disturb one already scheduled.
**Depends on:** Unit 3.1.
**Files:** `app/preference_change.py`
**Test file:** `tests/test_preference_change.py`
**Gate:** a preference change recorded after a delivery's scheduling cutoff does not alter that delivery, only the one after it.

## Unit 3.3 — Delivery scheduler

**Story.** As the agent, I need to compute each member's next scheduled delivery from their frequency and last-sent time, once §4's cadence ruling exists.
**Depends on:** Unit 3.1, and the §4 ruling above.
**Files:** `app/scheduler.py`
**Test file:** `tests/test_scheduler.py`
**Gate:** a daily member is scheduled at most once per calendar day, a weekly member at most once per ISO week, and a member with `consent.status == revoked` is never scheduled.

## Unit 3.4 — Interest-tailored content selection

**Story.** As a member with a stated interest, I want my summary drawn from material about that interest, not an undifferentiated firehose.
**Depends on:** Unit 3.3, Phase 1's `retrieve()`.
**Files:** `app/personalised_digest.py`
**Test file:** `tests/test_personalised_digest.py`
**Gate:** for a member with a non-null `interest_filter`, retrieval favours chunks whose organisation carries a matching theme over chunks that do not.

## Unit 3.5 — Delivery execution and logging

**Story.** As the agent, I need to actually send a scheduled delivery through the member's permitted channel and record that it happened, once §5's voice ruling exists.
**Depends on:** Unit 3.3, Unit 3.4, and the §5 ruling above.
**Files:** `app/deliver.py`
**Test file:** `tests/test_deliver.py`
**Gate:** a successful send sets `ScheduledDelivery.status` to `sent` and appends exactly one `DeliveryLog` row; the row never contains message content.

## Unit 3.6 — Frequency-change end-to-end

**Story.** As a member, when I switch from weekly to daily, I want my very next delivery to arrive the next day, not the following week.
**Depends on:** Unit 3.2, Unit 3.5.
**Files:** none new — exercises `app/preference_change.py` and `app/scheduler.py` together
**Test file:** `tests/test_frequency_change_e2e.py`
**Gate:** a fixture member who registers weekly, receives one weekly delivery, switches to daily, and receives a delivery the next calendar day — this phase's own definition-of-done sentence, encoded as one test.

## Unit 3.7 — Prompt without pressure

**Story.** As a member, I want the agent to occasionally invite me to participate, without that becoming a stream of engagement bait.
**Depends on:** Unit 3.5, and the §5 ruling above.
**Files:** `app/invitation.py`
**Test file:** `tests/test_invitation_rate_limit.py`
**Gate:** no member receives more than the ratified cap of invitations in a rolling window `[OPEN QUESTION: what is the ratified cap? Owner: whole group, folds into the §4/§5 ruling.]`, and no invitation fires for a member whose `permitted_channel` is `none`.

Full test specifications are written when this document is deepened, after the DECISIONS REQUIRED block above clears.

---

# PHASE 3 GATE

Phase 3 is complete only when every item passes.

### Automated — must be green

- [ ] Units 3.1 through 3.7 all marked `DONE` in the ledger
- [ ] `./scripts/test` fully green, Phases 1 and 2 included
- [ ] A revoked or unconsented member never receives a `ScheduledDelivery` with status `sent`
- [ ] A preference change applies to the next delivery only, verified by Unit 3.2's test
- [ ] The Unit 3.6 end-to-end fixture (weekly → daily) passes

### Human — must be judged

- [ ] A real member has registered, chosen weekly frequency plus an interest, and received a first weekly summary shaped by that interest
- [ ] The same member changed to daily and received a daily summary the next day
- [ ] Delivered content reads as connected to the stated interest, not generic
- [ ] Invitations feel occasional, not like engagement bait
- [ ] Known manual steps and limitations are written down
- [ ] A human has reviewed and merged the work

**The blocking criterion is the working document's own definition of done, verbatim** — the weekly-then-daily sequence above either happens for a real member or it does not. Do not open Phase 4 on a delivery mechanism that has not been watched working end-to-end for one real person.

---

## What this phase deliberately does not do

- Alignment or introduction suggestions between members or organisations — that is vision §4.11 Phase 2 (relationship stewardship). This document's own Phase 4 adds only light connection prompts on top of proven infrastructure, not full alignment mechanics. [see: D-4 in plan/ark-agent/decisions.md]
- Engagement optimisation, read receipts, open-rate tracking, or anything that turns invitations into a metric to maximise — the vision document rejects optimising "for the number of introductions rather than their relevance and value," and the same principle applies to plain engagement [see: proposal/hackathon-1/arc-community-agent-vision.md#79-relationship-consent-and-member-agency]
- Hidden social scoring or ranking of members
- Delivery channels beyond the one adapter Phase 2 built
- `[ASSUMPTION: cross-organisation tech-stack content in a member's digest — that belongs to Phase 4, not this one.]`
