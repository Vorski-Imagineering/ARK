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
| 2026-08-20 | 7 | Retrieval | DONE | app/retrieve.py, tests/test_retrieval.py | ./scripts/test tests/test_retrieval.py | 7 passed | RED confirmed. Cosine clamped to [-1,1] against floating-point drift. Ties break on chunk_id so ordering is stable across runs. Every result carries full chunk provenance. |
| 2026-08-20 | 8 | Prompt builder and untrusted-content boundary | DONE | app/prompt.py, prompts/answer.md, prompts/digest.md, tests/test_untrusted_source_content.py | ./scripts/test tests/test_untrusted_source_content.py | 7 passed | RED confirmed. Adversarial fixture verified to appear only inside the evidence delimiters, with the ignore-instructions rule positioned before the evidence block. Prompts are versioned files, not inline strings, so a prompt change is reviewable in git. |
| 2026-08-20 | 9 | Answer function | DONE | app/answer.py, app/llm.py, app/usage.py (Usage only), tests/helpers.py, tests/__init__.py, tests/test_citations.py, tests/test_insufficient_evidence.py | ./scripts/test tests/test_citations.py tests/test_insufficient_evidence.py | 13 passed | RED confirmed. **Spec ordering defect found**: Unit 9 needs Usage, which the spec defines in Unit 11. Usage now lives in app/usage.py from this unit; Unit 11 adds estimate_cost and log_run alongside it. Added Index.embedding_signature() so the query embedder is chosen from stored metadata rather than by reaching into a private connection. |
| 2026-08-20 | 10 | Cross-organisation digest | DONE | app/digest.py, tests/test_digest.py | ./scripts/test tests/test_digest.py | 6 passed | RED confirmed. Digest retrieval spreads the budget evenly across organisations rather than taking a global top-k, otherwise the best-matching organisation crowds out the rest and the digest stops being cross-organisational. Returns the same Answer record as unit 9, one shape for every generated artefact. |
| 2026-08-20 | 11 | Usage and cost logging | DONE | app/usage.py, tests/test_usage.py | ./scripts/test tests/test_usage.py | 6 passed | RED confirmed. The run log is enforced by construction to carry identifiers and counts only, never prompt, question, or output text, which is what lets a sanitised usage summary be published while raw content stays local. An unrecognised model costs zero rather than raising, since the configured provider is a subscription and reports no per-call price. |

---

## Phase 2 — Conversational onboarding

*Not open. Phase 1 gate must pass first.*

---

## Phase 3 — Ongoing member activation

*Not open. Phase 2 gate must pass first, and open decisions §4, §5, and §6 must be ruled.*

---

## Phase 4 — Cross-organisation synthesis

*Not open. Phase 1 gate must pass first, and at least three source packs must be live.*
