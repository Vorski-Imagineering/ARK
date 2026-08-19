# ARK Agent build ledger

Append-only. One row per unit attempt. Newest at the bottom.

**Never edit or reorder an existing row.** If a unit previously marked `DONE` turns out to be broken, append a new row for the re-attempt and mark the original `SUPERSEDED` only by adding a note in the new row — do not modify the old one.

This file is the build's memory. An agent starting cold reads this file first to learn what is done and what comes next.

**Status values:**

| Status | Meaning |
|---|---|
| `DONE` | All named tests pass, full suite green, gate passed |
| `PARTIAL` | Some tests pass; unit is not complete; next session resumes it |
| `BLOCKED` | Cannot proceed; a blocker entry exists in `~/need-human-help.md` |
| `SUPERSEDED` | A later row replaces this attempt |

---

## Phase 1 — Source-to-answer-to-digest vertical slice

| Date | Unit | Title | Status | Files | Command | Result | Notes |
|---|---|---|---|---|---|---|---|
| — | — | *No units attempted yet. Start at Unit 0.* | — | — | — | — | — |

---

## Phase 2 — Conversational onboarding

*Not open. Phase 1 gate must pass first.*

---

## Phase 3 — Ongoing member activation

*Not open. Phase 2 gate must pass first, and open decisions §4, §5, and §6 must be ruled.*

---

## Phase 4 — Cross-organisation synthesis

*Not open. Phase 1 gate must pass first, and at least three source packs must be live.*
