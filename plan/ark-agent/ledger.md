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
| 2026-08-20 | 0 | Scaffold and test harness | DONE | pyproject.toml, app/__init__.py, tests/test_smoke.py, scripts/setup, scripts/test, .env.example, .gitignore | ./scripts/test | 2 passed | RED confirmed first (1 failed, AttributeError on `app.__version__`). Three spec corrections recorded in the unit: explicit setuptools package list, uv-preferred setup, `*.egg-info/` ignored. Built on Python 3.13 via uv; server runs 3.11.16 and is unverified until the phase gate. |
| 2026-08-20 | 1 | Source pack schema and validator | DONE | app/schema.py, app/source_pack.py, tests/test_source_schema.py, tests/fixtures/source-packs/{valid-org,bad-permission,bad-source-id}.md | ./scripts/test tests/test_source_schema.py | 8 passed | RED confirmed (ModuleNotFoundError). No spec corrections needed. One implementation note: YAML parses an unquoted ISO date into a date object, so published_at is coerced to string to honour the contract. |
| 2026-08-20 | 2 | Source loader | DONE | app/source_loader.py, tests/test_source_loader.py, tests/fixtures/snapshots/{valid-org-about.md,valid-org-updates.md,sample-page.html} | ./scripts/test tests/test_source_loader.py | 8 passed | RED confirmed. No spec corrections. Standard library only; no network access in the loader. |
| 2026-08-20 | 3 | Normaliser | DONE | app/normalise.py, tests/test_normalise.py | ./scripts/test tests/test_normalise.py | 7 passed | RED confirmed. **Test caught a real spec defect**: the prose rule said strip trailing whitespace per line, but the hand-derived expected value requires stripping both ends. Implementation and spec corrected; the test was not touched. Permission enforcement verified: a link-and-summarise source stores empty text and retains metadata. |
| 2026-08-20 | 4 | Chunker | DONE | app/chunk.py, tests/test_chunk.py | ./scripts/test tests/test_chunk.py | 8 passed | RED confirmed. Chunk text is always an exact slice of the source, never stripped, so every passage is locatable. Headings are located by line start rather than by the position of the heading text, without which a chunk at offset 0 is governed by no heading. |
| 2026-08-20 | 5 | Embedder | DONE | app/embed.py, tests/test_embed.py | ./scripts/test tests/test_embed.py | 7 passed | RED confirmed. Manual LocalEmbedder check per spec: all-MiniLM-L6-v2 loads, 384 dims, unit length 1.0, no API key. D-3 memory assumption discharged: server has 7.0 GiB available, 89 GB disk. sentence-transformers stays an optional extra and is never imported at module level, so the suite runs without it. |
| 2026-08-20 | 6 | Retrieval index | DONE | app/index.py, tests/test_index.py | ./scripts/test tests/test_index.py | 8 passed | RED confirmed. Implements four ratified acceptance criteria: deterministic rebuild, failed ingestion leaves the active index untouched, prior indexes stay selectable, and the index is rebuildable from the corpus. Monotonic counter for filenames as the spec correction required. Index.open uses SQLite read-only URI mode so the query path cannot mutate the live index. |

---

## Phase 2 — Conversational onboarding

*Not open. Phase 1 gate must pass first.*

---

## Phase 3 — Ongoing member activation

*Not open. Phase 2 gate must pass first, and open decisions §4, §5, and §6 must be ruled.*

---

## Phase 4 — Cross-organisation synthesis

*Not open. Phase 1 gate must pass first, and at least three source packs must be live.*
