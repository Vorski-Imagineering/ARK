# ARK Agent build protocol

**Status:** Active. This governs every implementation session on the ARK Agent.
**Applies to:** any agent or human implementing a unit from `plan/ark-agent/01-phase-1-vertical-slice.md` or its sibling phase documents.
**Read time:** 10 minutes. Read it fully before your first unit. Re-read section 4 before every unit.

---

## 1. What this document is

This is the operating protocol for building the ARK Agent. It defines how work is broken into units, how each unit is proved correct, and when you are allowed to move on.

The protocol exists because the build is executed by AI agents across many short sessions with no shared memory. Every rule below exists to make that survivable.

Three properties matter more than speed:

1. **Determinism.** A unit either passes its named tests or it does not. No judgement call.
2. **Resumability.** Any agent, with no memory of prior sessions, can read the repository and know exactly what to do next.
3. **Honesty.** A failing test is reported as failing. Work that was skipped is recorded as skipped.

This protocol is reproduced in full at the top of every phase document. That duplication is deliberate. Do not replace it with a cross-reference.

---

## 2. The two agent identities

The ARK Agent has two distinct roles. Confusing them causes permission errors and wasted work.

| Identity | What it is | What it may do | What it must never do |
|---|---|---|---|
| **Agent as builder** | The agent implementing units from these phase documents | Read the repository, write code and tests on a branch, run tests, open a pull request | Push to the default branch, merge its own pull request, edit its own runtime configuration |
| **Agent as service** | The participant-facing ARK Agent that answers questions | Read approved sources and the active index, generate drafts and answers | Write the canonical corpus, administer the index, expand its own tools, delete backups |

You are operating as **builder** when following this protocol.

The builder identity maps to the `Contribute` permission level in the access model: *"propose changes through a branch or pull request without direct production mutation."* [see: proposal/hackathon-1/execution/05-technical-specification.md#7a-access-control-model]

---

## 3. Session rules

### 3.1 One unit per session

Do exactly one unit per session. Stop when it is done. Do not begin the next unit even if you have capacity.

This is not a productivity limit. Long multi-unit sessions drift: context fills, earlier instructions lose force, and errors compound silently. One unit per session keeps every result verifiable.

### 3.2 The file system is the memory

Never rely on remembering a previous session. All state lives in the repository:

- `plan/ark-agent/ledger.md` — what is done, what is next
- `plan/ark-agent/decisions.md` — why things are the way they are
- `plan/ark-agent/open-questions.md` — what is unresolved
- `~/need-human-help.md` — what is blocked and who owns it

### 3.3 Cold start procedure

Run this at the start of every session, before anything else:

1. Read `plan/ark-agent/ledger.md`. Find the last row with status `DONE`.
2. The next unit is the next numbered unit in the phase document.
3. Open the phase document. Read that unit's section in full.
4. Confirm the unit's stated dependencies are all marked `DONE` in the ledger.
5. Run the existing test suite. It must be green before you start. If it is red, stop and fix that first — a red suite means a prior session left the tree broken.
6. State in your first message: which unit you are starting, and the result of step 5.

If the ledger is empty, start at Unit 0.

---

## 4. The unit loop

Every unit follows the same five steps. Do not reorder them. Do not skip step 1.

### Step 1 — RED

Create the test file exactly as specified in the unit. The test content is **given to you in the phase document**. Copy it as written.

Run the test command. It must **fail**. A test that passes before the implementation exists is a broken test — stop and report it.

### Step 2 — GREEN

Create only the implementation file named in the unit. Write the minimum code that makes the given tests pass.

Do not add functions the unit did not ask for. Do not add configuration options, logging, or abstraction layers that no test exercises. Extra code is not free — it is untested code.

### Step 3 — GATE

Run these two commands in order:

```
# 1. the unit's own tests
<the unit's test command>

# 2. the full suite, to prove no regression
./scripts/test
```

Both must be fully green. Not "green except one unrelated failure." Fully green.

### Step 4 — LEDGER

Append one row to `plan/ark-agent/ledger.md`. Format in section 6.

### Step 5 — STOP

Report what you did:

- Unit number and title
- Files created or modified, by exact path
- The test command and its result line (e.g. `14 passed in 0.42s`)
- Anything you noticed but did not act on

Then stop. Do not start the next unit.

---

## 5. Forbidden moves

These are the specific ways a build like this fails. Each one has happened in real projects. If you catch yourself doing any of them, stop and write a blocker entry instead.

**Never edit a test to make it pass.** The tests are the specification. If a test seems wrong, it may genuinely be wrong — record it as a blocker and stop. Do not adjust it and continue.

**Never edit a fixture to match your output.** Fixture values were derived by hand, independently of any implementation. Changing a fixture to match what your code produced destroys the only independent check in the system.

**Never compute an expected value by calling the code under test.** If a test needs to know that `chunk_id` is `"abc-0003"`, that string is written literally in the test. A test that computes its expectation from the implementation will pass no matter how wrong the implementation is.

**Never use `skip`, `xfail`, or a commented-out assertion** to get past a failure.

**Never proceed on red.** If the gate does not pass, the unit is not done, regardless of how close it looks.

**Never mark a unit `DONE` you did not fully complete.** `BLOCKED` and `PARTIAL` are legitimate outcomes. A false `DONE` corrupts every session that follows.

**Never modify the Hermes runtime configuration.** `~/.hermes/` is out of scope for every unit in every phase. That includes `config.yaml`, `.env`, `SOUL.md`, and the skills directory.

**Never commit a credential.** Before every commit, check for `sk-`, `key=`, `token=`, `password=`, and `Bearer `. `.env.example` holds variable names only, never values.

---

## 6. The ledger

`plan/ark-agent/ledger.md` is append-only. Never rewrite or reorder existing rows. If a unit previously marked `DONE` turns out to be broken, append a new row recording that — do not edit the old one.

One row per unit attempt:

```
| 2026-08-20 | 1.3 | Chunker | DONE | app/chunk.py, tests/test_ingest_fixture.py | pytest tests/test_ingest_fixture.py -q | 9 passed | — |
```

Columns, in order:

| Column | Meaning |
|---|---|
| Date | `YYYY-MM-DD` |
| Unit | Unit number from the phase document |
| Title | Unit title, copied exactly |
| Status | `DONE`, `PARTIAL`, `BLOCKED`, or `SUPERSEDED` |
| Files | Every file created or modified, comma-separated, exact paths |
| Command | The exact test command run |
| Result | The test runner's summary line |
| Notes | Blocker reference, or `—` |

---

## 7. When you are blocked

Use the existing blocker protocol at `~/need-human-help.md` on the ARK server. Do not invent a second one.

Write an entry when you have spent more than two tool calls on a problem and are still stuck. Then stop working on that unit.

Entry format, newest on top:

```
### YYYY-MM-DD HH:MM — Short title
- **Status:** OPEN | WAITING | RESOLVED (date) | WONTFIX
- **Category:** environment | permissions | auth | network | tooling | data | ambiguity | other
- **What I tried:** bullet list of attempted fixes
- **Where it blocks me:** which unit is stuck
- **What I need from you:** concrete ask, one line if possible
- **Owner:** role name
```

Also append a `BLOCKED` row to the ledger referencing the blocker title.

A blocker is a successful outcome for a session. Reporting one honestly is better than a plausible workaround that nobody reviews.

---

## 8. Git discipline

- Work on a branch named `build/phase-<n>-unit-<m>`. Never commit directly to the default branch.
- Open a draft pull request when you begin a unit, before code exists. This follows the established contribution cadence. [see: proposal/hackathon-1/execution/06-roles-and-readiness.md]
- Commit after the gate passes, not before.
- One commit per unit. Message format: `phase-<n> unit-<m>: <title>`.
- Never force-push. Never delete a branch that has an open pull request.
- Never merge your own pull request. A human merges.

---

## 9. Public repository rules

This repository is public and CC0-licensed. Everything committed is permanent and world-readable.

Before writing any file, confirm all of the following:

- [ ] No names of private individuals — use role labels
- [ ] No private conversations, chat excerpts, or direct messages
- [ ] No credentials, API keys, tokens, or `.env` values
- [ ] No internal URLs, ticket identifiers, or meeting links
- [ ] No personal contact details
- [ ] No non-public organisational, financial, or contractual material

If any box is unchecked, do not write the file. Write a blocker entry and ask.

This is not advisory. It is the repository's highest-priority standing policy. [see: AGENTS.md#2-sensitive-information-policy-highest-priority--non-negotiable]

Raw agent conversation transcripts are **never** committed to this repository. They stay in the local working repository on the server. Only sanitised, role-labelled summaries may be published here.

---

## 10. Two kinds of test, and why the difference matters

This build has deterministic components and a language model. They cannot be tested the same way, and conflating them is the single most likely way this project produces a green suite that proves nothing.

### 10.1 Deterministic components — real assertions

The loader, normaliser, chunker, index, and retrieval ranking are ordinary code. Given the same input they produce the same output, every time.

These get real unit tests with literal expected values. Exact strings, exact counts, exact identifiers. If a chunker splits a fixture into nine chunks, the test asserts `len(chunks) == 9` and checks the text of chunk 3 against a literal string.

### 10.2 Model-dependent components — contract tests with an injected fake

The answer and digest functions call a language model. Model output is not reproducible, so no test may assert on its prose.

What *is* testable is the structure around the model. Every model-calling function takes the model as an injected dependency:

```python
def answer(question: str, index: Index, llm: LLM) -> Answer:
    ...
```

Tests pass a `FakeLLM` that returns a fixed canned response. That makes the following fully deterministic and therefore genuinely testable:

- every citation in the answer resolves to a `source_id` that exists in the index
- no citation points to a URL outside the approved source packs
- an empty retrieval result produces an explicit insufficient-evidence response, never a guess
- retrieved source text is delimited as quoted evidence and cannot act as an instruction
- usage and cost are recorded for every call

Never call a real model inside the test suite. It is slow, costs money, and is not reproducible.

### 10.3 Answer quality — the evaluation harness, not the test suite

"Is the digest accurate enough that representatives sign off?" is a real and necessary gate. It is not a unit test.

It runs once per phase, against the real model, over a fixed set of representative questions, and is scored by a human or a stronger reviewing model. It lives in `evals/`, never in `tests/`, and it never gates a unit.

Keeping these separate means the test suite stays fast, free, and deterministic, while quality is still measured — just measured honestly, by the people whose material is being described.

---

## 11. Phase gates

A unit gate proves one component. A phase gate proves the phase.

A phase is complete only when all of the following hold:

1. Every unit in the phase is marked `DONE` in the ledger.
2. The full test suite passes from a clean checkout on a second machine.
3. The phase's named acceptance criteria all pass. These are listed at the end of each phase document and derive from the ratified acceptance set. [see: proposal/hackathon-1/execution/05-technical-specification.md#9-acceptance-tests]
4. The evaluation harness has been run and its results recorded.
5. A human has reviewed and merged the work.

No phase opens until the prior phase's gate has passed. This is the sequencing rule from the working document: do not layer on top of an unproven foundation.

---

## 12. What to do when the specification is wrong

You will find errors in these documents. They were written before the code existed.

When a unit's specification is impossible, contradictory, or clearly wrong:

1. Stop. Do not improvise a fix and continue.
2. Write a blocker entry describing the specific contradiction.
3. Append a `BLOCKED` row to the ledger.
4. Report it and stop.

Do not silently reinterpret a requirement. A wrong specification followed honestly is recoverable in one session. A wrong specification quietly "fixed" in five different ways across five sessions is not.
