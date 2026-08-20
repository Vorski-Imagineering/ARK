# ARK Agent — build track

Implementation specifications for the ARK Agent. This is the "how it gets built" layer. The "why" lives in the vision document and the "what we promised" lives in the participant invitation.

Everything here is designed to be executed by an AI agent across many short sessions with no shared memory, and to be picked up by a human or a different agent at any point without re-deriving context.

---

## Start here

**If you are implementing:** read `00-build-protocol.md`, then open `01-phase-1-vertical-slice.md` and run the cold-start procedure. It tells you which unit is next. Do one unit, then stop.

**If you are reviewing:** read `decisions.md` for what was chosen and why, then `ledger.md` for what has actually been built.

**If you are picking this up cold, months later:** read this file, then `decisions.md`, then `open-questions.md`. Those three tell you the state of the world.

---

## The files

| File | What it is | Read when |
|---|---|---|
| `00-build-protocol.md` | The TDD loop, unit gates, forbidden moves, blocker handling | Before your first unit. Re-read section 4 before every unit. |
| `01-phase-1-vertical-slice.md` | Phase 1, fully executable. 14 units with pre-written tests. | You are building. |
| `02-phase-2-conversational-onboarding.md` | Phase 2 at contract depth | Planning. Not executable yet. |
| `03-phase-3-member-activation.md` | Phase 3 at contract depth | Planning. Not executable yet. |
| `04-phase-4-cross-org-synthesis.md` | Phase 4 at contract depth | Planning. Not executable yet. |
| `ledger.md` | Append-only unit progress. The build's memory. | Every session, first thing. |
| `decisions.md` | Dated record of what was chosen, rejected, and why | When something looks arbitrary. |
| `open-questions.md` | What is unresolved, who owns it, what it blocks | Before opening a new phase. |
| `permissions.md` | Who may add an organisation, and how to require approval | Before changing who can add organisations. |

---

## How the phases relate

Phase 1 is the hackathon's committed deliverable. Phases 2 through 4 are stretch.

```
Phase 1 — vertical slice          Committed   ← executable now
    │
    ├──► Phase 2 — onboarding     Stretch     ← needs Phase 1 gate
    │        │
    │        └──► Phase 3 — activation  Stretch  ← needs Phase 2 gate + decisions §4, §5, §6
    │
    └──► Phase 4 — cross-org synthesis  Stretch  ← needs Phase 1 gate + 3 live source packs
```

No phase opens until the prior phase's gate has passed. This is the working document's own rule: do not layer on top of an unproven foundation.

### A warning about phase numbers

This track numbers phases 1 to 4, following the hackathon working document. **The vision document uses "Phase 1" and "Phase 2" to mean something entirely different** — relationship stewardship, at §4.11. Onboarding, activation, and synthesis appear there as unnumbered sections §4.1, §4.2, and §4.4.

Always say which document you mean. Each phase document opens with a mapping table. [see: decisions.md#d-4]

---

## Why the documents look the way they do

**Each phase document is self-contained.** The build protocol is reproduced in full at the top of every one. That duplication is deliberate — an agent handed a single file must be able to execute it without following a cross-reference, and cross-references are the first thing a small model drops.

**Tests are written in the specification, not by the implementer.** Every unit's test file is given verbatim, with expected values derived by hand. An agent that writes its own tests tends to compute the expected value by calling the code under test, which produces a suite that passes no matter how wrong the implementation is. Hand-derived literal fixtures are the only defence. [see: decisions.md#d-8]

**Deterministic code and model output are tested differently.** The loader, normaliser, chunker, index, and retrieval ranking get real assertions on exact values. The answer and digest functions take the model as an injected dependency and are tested with a fake that returns canned output — asserting on structure, never on prose. Answer quality is measured separately, once per phase, by human review against a fixed question set. [see: `00-build-protocol.md` section 10]

**One unit per session.** Long multi-unit sessions drift: context fills, early instructions lose force, errors compound quietly. One unit per session keeps every result verifiable.

**Progress lives in files, not in context.** `ledger.md` is the build's memory. An agent with no recollection of yesterday reads it and knows exactly what to do next.

---

## Skills

Three packaged skills in `skills/` make this track usable by a collaborator's own agent:

| Skill | Use it to |
|---|---|
| `ark-tdd-unit` | Execute one build unit end to end, with the gates enforced |
| `ark-source-pack` | Help an organisation draft and validate its source pack |
| `ark-session-log` | Write the sanitised session record and route transcripts correctly |

Each is a `SKILL.md` with frontmatter, readable by common agent runtimes without translation. [see: decisions.md#d-7]

---

## Current state

Phase 1 is specified and ready. **No application code exists yet** — the ledger is empty and Unit 0 is the next action.

Live infrastructure: a server with the agent runtime installed and one profile configured, a Telegram bot in mentions-only mode, and wildcard DNS.

Known gaps that will bite if ignored:

- No API keys of any kind are configured on the server. Embeddings are therefore local by decision, and generation uses the runtime's configured model. [see: decisions.md#d-3]
- The technical specification's §8 prepared vertical slice, scheduled to be complete before Day 1, was not built. Units 0 through 11 of Phase 1 are that work.
- Several ownership roles named in `00-start-here.md` are still unassigned, including the recovery custodian, who must be a different person from the infrastructure owner.

See `open-questions.md` for the full list and who owns each.

---

## House rules

This repository is public, permanent, and CC0-licensed.

Never commit: names of private individuals, private conversations or chat excerpts, credentials, internal URLs or ticket identifiers, personal contact details, or non-public organisational material. Use role labels. If it would be inappropriate on a public website, it does not belong here. [see: AGENTS.md#2-sensitive-information-policy-highest-priority--non-negotiable]

Raw agent conversation transcripts are never committed here. They stay in the local working repository on the server, and only sanitised summaries are published. [see: decisions.md#d-5]
