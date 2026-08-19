---
name: ark-tdd-unit
description: Execute exactly one test-driven build unit from an ARK Agent phase document. Use when asked to "build the next unit", "continue the ARK build", "implement unit N", "pick up where the build left off", or when starting any implementation session on the ARK Agent. Reads the ledger to find the next unit, runs the red-green-gate loop, and stops. One unit per session, always.
---

# Execute one ARK Agent build unit

This skill runs a single unit of the ARK Agent build. It stops when that unit is done. It never runs two units in one session.

The build is executed across many short sessions with no shared memory. Everything below exists to make that survivable.

## Before you start

Read `plan/ark-agent/00-build-protocol.md` in full. This skill is a runner for that protocol, not a replacement for it. If the two ever disagree, the protocol wins.

## Step 1 — Cold start

Run these in order and report the result of each:

1. Read `plan/ark-agent/ledger.md`. Find the last row with status `DONE`.
2. The next unit is the next numbered unit in the phase document. If there are no `DONE` rows, the next unit is Unit 0 of Phase 1.
3. Open the phase document and read that unit's section in full.
4. Check the unit's stated dependencies. Every one must be `DONE` in the ledger. If any is not, stop and say so.
5. Run `./scripts/test`. It must be green before you touch anything.

If step 5 is red, a previous session left the tree broken. Do not start a new unit. Fix the breakage or write a blocker, then stop.

State plainly in your first message: which unit you are starting, and whether the suite was green.

## Step 2 — RED

Create the test file exactly as written in the unit. Copy it. Do not improve it, rename anything, or adjust an assertion because it looks wrong.

Create any fixture files the unit specifies, with exactly the content given.

Run the unit's test command. **It must fail.** If it passes before you have written the implementation, something is wrong with the test — stop and report it rather than continuing.

## Step 3 — GREEN

Create only the implementation file the unit names. Write the least code that makes the given tests pass.

Do not add functions the unit did not ask for. Do not add configuration options, logging, caching, or abstraction layers that no test exercises. Untested code is a liability, not a bonus.

## Step 4 — GATE

Run two commands in order:

```
<the unit's own test command>
./scripts/test
```

Both must be fully green. Not "green apart from one unrelated failure." Fully green.

## Step 5 — LEDGER

Append one row to `plan/ark-agent/ledger.md`:

```
| YYYY-MM-DD | 1.3 | Chunker | DONE | app/chunk.py, tests/test_chunk.py | ./scripts/test tests/test_chunk.py | 8 passed | — |
```

Append. Never edit or reorder an existing row.

## Step 6 — COMMIT AND STOP

```
git add <the files you created>
git commit -m "phase-1 unit-3: chunker"
```

One commit per unit. Never commit to the default branch. Never merge your own pull request.

Then report:

- Unit number and title
- Every file created or modified, by exact path
- The test command and its result line
- Anything you noticed but did not act on

Then stop. Do not start the next unit, even if you have capacity.

## Never do these

- Never edit a test to make it pass. The tests are the specification.
- Never edit a fixture to match your output. Fixtures were derived by hand as an independent check.
- Never compute an expected value by calling the code under test.
- Never use `skip`, `xfail`, or a commented-out assertion to get past a failure.
- Never proceed on red.
- Never mark a unit `DONE` you did not complete. `PARTIAL` and `BLOCKED` are honest outcomes.
- Never modify `~/.hermes/` — not `config.yaml`, not `.env`, not `SOUL.md`, not the skills directory.
- Never commit a credential. Check for `sk-`, `key=`, `token=`, `password=`, `Bearer ` first.

## When you get stuck

After more than two tool calls on the same problem, stop. Write an entry in `~/need-human-help.md` using its existing format, append a `BLOCKED` row to the ledger, and report it.

A reported blocker is a successful session. A plausible workaround that nobody reviewed is not.

## When the specification is wrong

You will find errors. These documents were written before the code existed.

If a unit is impossible, self-contradictory, or clearly wrong: stop, write a blocker describing the specific contradiction, mark the ledger row `BLOCKED`, and report. Do not quietly reinterpret a requirement — a wrong specification followed honestly costs one session, while one silently "fixed" five different ways across five sessions costs the project.
