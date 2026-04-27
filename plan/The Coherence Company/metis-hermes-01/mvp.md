# Genesis Brain Light on Hermes — MVP Functional Specification

**Status:** Spec  
**Branch:** `feature/kb-mvp`  
**Last updated:** 2026-04-26

---

## 1. What This Is

The TCC knowledge base is the Genesis Brain Light pattern ([design doc](../../research/regentribe/GENESIS-BRAIN-LIGHT-DESIGN.md)) adapted for our context:

- **Document layer:** the existing `research/` directory in this git repo (markdown files)
- **Knowledge graph:** SurrealDB — same schema and purpose as Genesis Brain ([architecture doc](../../research/regentribe/GENESIS-BRAIN-ARCHITECTURE.md))
- **Trigger:** Hermes cron + `git diff` change detection, replacing the GitHub webhook in the Genesis design
- **Query interface:** Hermes skill scripts, replacing the Genesis Brain MCP server

The result: any agent working in this repo can query what TCC knows — across all research, synthesis, and notes — using the same tools Genesis uses (`query`, `relate`, `stats`, `capture`, `ingest`). See [Genesis TOOLS.md](../../research/regentribe/genesis-zero-bot/TOOLS.md) for how this already works in production.

---

## 2. Scope vs Broader Hermes Memory Model

This MVP implements **only the durable semantic memory of the `research/` corpus**. The wider Hermes memory architecture has multiple layers (see [05-memory-model-and-retrieval-policy.md](./05-memory-model-and-retrieval-policy.md) and [06-dreaming-and-consolidation-architecture.md](./06-dreaming-and-consolidation-architecture.md)) — this MVP touches one of them.

| Memory layer | Where it lives | Owned by |
|---|---|---|
| Working memory (current prompt) | Hermes session context | Hermes built-in |
| User memory (`MEMORY.md`, `USER.md`) | Hermes profile dir | Hermes built-in |
| Session / episodic STM | Hermes session store | Hermes built-in |
| **Durable semantic (research corpus)** | **SurrealDB knowledge graph** | **This MVP** |
| Durable procedural / skills | Hermes skills dir | Hermes built-in (out of scope) |
| Mid-term consolidation, group memory, dream reports | — | Post-MVP, see [06-dreaming-and-consolidation-architecture.md](./06-dreaming-and-consolidation-architecture.md) |

The knowledge graph is **derived** from the markdown corpus. The corpus is canonical (see [02-system-boundary-and-source-of-truth.md](./02-system-boundary-and-source-of-truth.md)); the graph can always be rebuilt from it via full reindex.

---

## 3. What Is Explicitly Out of Scope (MVP)

| Genesis Brain Light feature | Decision |
|---|---|
| GitHub webhook receiver | Replaced by Hermes cron |
| S3/R2 blob storage | Deferred — markdown only |
| REST API for external clients | Deferred — Hermes tools sufficient |
| API key auth system | Deferred — single Hermes profile |
| Multi-tenant namespacing | Deferred — single `tcc/knowledge_base` namespace |
| NARS epistemic truth values | Deferred — standard confidence weights |
| Community clustering | Deferred — add after graph exceeds ~500 concepts |

---

## 3. File Layout

Three classes of artifact, three locations. Code is in the repo; runtime state is under the Hermes profile; the venv is local to the skill but gitignored.

### 3.1 In this repo (git-tracked)

```
skills/knowledge-base/
├── pipeline/               # Python pipeline (adapted from genesis semantic-graph)
│   ├── requirements.txt
│   ├── setup.sh
│   ├── db.py               # SurrealDB connection + schema init
│   ├── chunker.py          # Markdown → text chunks
│   ├── embedder.py         # OpenRouter embeddings
│   ├── extractor.py        # LLM concept + relation extraction
│   ├── entity_resolver.py  # Deduplication against existing graph
│   ├── ingest.py           # Orchestrate one file end-to-end
│   ├── reindex.py          # Full or incremental reindex driver
│   └── tests/
├── scripts/
│   ├── query.sh
│   ├── relate.sh
│   ├── stats.sh
│   ├── capture.sh
│   └── ingest.sh
├── docker-compose.yml      # SurrealDB container (port 8765)
└── SKILL.md                # Hermes skill definition

research/                   # The corpus — already exists, system of record
```

### 3.2 Under the Hermes profile (runtime state, not git-tracked)

```
~/.hermes/<profile>/state/knowledge-base/
└── surreal-data/           # SurrealDB on-disk database files
```

This mirrors the Genesis pattern of `~/.openclaw/surreal-data/` — the agent's runtime state belongs with the agent, not in the code repo. The exact path uses Hermes's profile state directory convention (verify against current Hermes docs at install time).

The only writable pipeline state besides the DB itself is `kb_meta.last_indexed_commit`, which is stored **inside** SurrealDB. So "where does the SurrealDB data live" is the only state-location decision needed.

### 3.3 Local to the skill but gitignored

```
skills/knowledge-base/pipeline/.venv/   # Deterministic from requirements.txt
```

Same pattern as Genesis's `~/.openclaw/workspace-genesis/skills/semantic-graph/.venv/`. Add `skills/knowledge-base/pipeline/.venv/` to `.gitignore`.

---

## 4. Component Specifications

### 4.1 SurrealDB Container

Run SurrealDB on port **8765** (not 8000, to avoid collision with any existing Genesis instance). Persist data outside the repo at `${HERMES_KB_DATA_DIR}` (see § 3.2 — typically `~/.hermes/<profile>/state/knowledge-base/surreal-data/`). The `docker-compose.yml` bind-mounts that path into the container's `/data` volume. This keeps mutating binary state out of the code repo and aligns with the Genesis production setup ([TOOLS.md § Knowledge Graph](../../research/regentribe/genesis-zero-bot/TOOLS.md)).

---

### 4.2 SurrealDB Schema

Same schema as Genesis Brain ([GENESIS-BRAIN-ARCHITECTURE.md § Layer 2](../../research/regentribe/GENESIS-BRAIN-ARCHITECTURE.md)):

| Table | Purpose |
|---|---|
| `document` | One record per indexed markdown file. Tracks path, title, git commit hash, timestamps. |
| `chunk` | Text segments (~512 tokens) with vector embeddings. Linked to their parent document via `contains` edges. |
| `concept` | Named entities extracted from documents. Has kind (person/place/org/idea/event/process), description, embedding. |
| `community` | Thematic clusters of concepts. Deferred to post-MVP. |
| `contains` | Edge: document → chunk |
| `mentions` | Edge: chunk → concept |
| `relates` | Edge: concept → concept, with verb and confidence weight |
| `belongs_to` | Edge: concept → community. Deferred to post-MVP. |
| `kb_meta` | Key/value store for pipeline state — specifically the last indexed git commit hash. |

HNSW vector index on `chunk.embedding` and `concept.embedding` for semantic search. Dimension: 1536 (OpenAI `text-embedding-3-small`).

---

### 4.3 Python Pipeline

Adapted from the Genesis Brain semantic-graph skill at `~/.openclaw/workspace-genesis/skills/semantic-graph/pipeline.py` on the Genesis VPS. See [TOOLS.md § Genesis Brain scripts](../../research/regentribe/genesis-zero-bot/TOOLS.md) for the equivalent production scripts this mirrors.

**Components:**

**`db.py`** — Async SurrealDB connection using the `surrealdb` Python client. Exposes `get_db()`, `init_schema()`, `get_last_indexed_commit()`, `set_last_indexed_commit()`. Schema is defined as a SurrealQL string applied idempotently at startup.

**`chunker.py`** — Splits a markdown document into overlapping segments of ~512 tokens. Splits first on heading boundaries (preserves section context), then by token count. Uses `tiktoken` with the `cl100k_base` encoding. Also extracts document title from the first `#` heading (fallback: filename).

**`embedder.py`** — Calls OpenRouter with the `openai/text-embedding-3-small` model (same as Genesis Brain). Batches requests in groups of 20 to stay within API limits. Returns one 1536-dimension vector per input text.

**`extractor.py`** — Calls a small LLM via OpenRouter (default: `anthropic/claude-haiku-4-5` for cost) with a structured extraction prompt. Returns a JSON object with `concepts` (name, kind, description) and `relations` (from, to, verb, weight). Handles malformed LLM output gracefully (returns empty lists). Mirrors the extraction logic described in [GENESIS-BRAIN-LIGHT-DESIGN.md § 3.4 Reindex Pipeline](../../research/regentribe/GENESIS-BRAIN-LIGHT-DESIGN.md).

**`entity_resolver.py`** — Before upserting a new concept, checks existing graph concepts for: (1) exact name match (case-insensitive), (2) vector similarity ≥ 0.92 cosine. Returns the existing record if matched, allowing the ingest to link to it rather than create a duplicate. Same deduplication approach as Genesis Brain ([GENESIS-BRAIN-LIGHT-DESIGN.md § 3.4](../../research/regentribe/GENESIS-BRAIN-LIGHT-DESIGN.md)).

**`ingest.py`** — Orchestrates a single `.md` file through the full pipeline: read file → extract title → chunk → embed chunks → upsert document + chunks in SurrealDB → extract concepts+relations from full text → resolve entities → upsert concepts → upsert relations → link mentions. Accepts a git commit hash argument (passed by `reindex.py`) to stamp the document record. Callable as a script: `python ingest.py <path>`.

**`reindex.py`** — Two modes:
- **Incremental (default):** reads `kb_meta.last_indexed_commit` from SurrealDB, runs `git diff --name-only <last_commit>..HEAD -- research/` to get changed files, ingests only those. On completion, writes current HEAD hash to `kb_meta`.
- **Full:** traverses all `*.md` files under `research/`, ingests each. Safe to re-run (all SurrealDB writes use UPSERT).

Dry-run flag (`--dry-run`) prints the file list without writing anything — useful for verifying what would be indexed.

---

### 4.4 Shell Scripts (Hermes Skill Interface)

Same interface as the production Genesis Brain scripts documented in [TOOLS.md § Genesis Brain scripts](../../research/regentribe/genesis-zero-bot/TOOLS.md). Each script activates the Python venv, sets required env vars, and returns JSON.

| Script | Input | Output | Notes |
|---|---|---|---|
| `query.sh "<query>" [limit]` | Query string, optional result limit (default 5) | `{results: [{path, title, text, score}]}` | Vector search on chunk embeddings via SurrealDB HNSW |
| `relate.sh "<A>" "<B>"` | Two concept names | `{from, to, direct: [{verb, weight}], shared_neighbors: [...]}` | Graph traversal between concept nodes |
| `stats.sh` | — | `{document: N, chunk: N, concept: N, ...}` | Row counts per table |
| `capture.sh "<text>"` | Freeform text | Ingest result JSON | Writes to a temp file, ingests it, deletes the file |
| `ingest.sh <path>` | Path to a `.md` file | Ingest result JSON | Direct call to `ingest.py` |

---

### 4.5 SKILL.md

Instructs Hermes when to use the knowledge base. Mirrors [TOOLS.md § When to use the knowledge graph](../../research/regentribe/genesis-zero-bot/TOOLS.md). Specifies:

- Run `query.sh` before answering any question that could benefit from graph context
- Run `ingest.sh` when a new file is added
- Run `relate.sh` for "how does X connect to Y" questions
- Run `capture.sh` for freeform "remember this" requests
- Run `stats.sh` to report graph health

---

### 4.6 Cron Trigger (replaces GitHub webhook)

Hermes cron job runs `python reindex.py` (incremental mode) daily at 03:00. This replaces the GitHub webhook + VPS pipeline in the Genesis Brain Light design ([GENESIS-BRAIN-LIGHT-DESIGN.md § 3.3](../../research/regentribe/GENESIS-BRAIN-LIGHT-DESIGN.md)). Manual trigger: run `python reindex.py` or `python reindex.py --full` from the pipeline directory.

---

## 5. Data Flow

```
Edit markdown in research/
        ↓
git commit + push
        ↓
Hermes cron (03:00 daily) OR manual trigger
        ↓
reindex.py: git diff → changed .md files
        ↓
ingest.py per file:
  chunker → embedder → extractor → entity_resolver → SurrealDB upsert
        ↓
Graph updated
        ↓
Any agent: query.sh / relate.sh → fresh results with citations
```

Identical to the Genesis Brain Light data flow described in [§ 4](../../research/regentribe/GENESIS-BRAIN-LIGHT-DESIGN.md), with the webhook layer removed.

---

## 6. Environment Variables Required

| Variable | Purpose | Example |
|---|---|---|
| `SURREAL_URL` | SurrealDB WebSocket endpoint | `ws://127.0.0.1:8765/rpc` |
| `SURREAL_USER` | SurrealDB root user | `root` |
| `SURREAL_PASS` | SurrealDB root password | _(set in Hermes profile `.env`)_ |
| `SURREAL_NS` | SurrealDB namespace | `tcc` |
| `SURREAL_DB` | SurrealDB database | `knowledge_base` |
| `HERMES_KB_DATA_DIR` | Host path bind-mounted into the SurrealDB container's `/data` (see § 3.2) | `~/.hermes/tcc/state/knowledge-base/surreal-data` |
| `OPENROUTER_API_KEY` | OpenRouter API key (embeddings + extraction) | _(set in Hermes profile `.env`)_ |
| `EMBED_MODEL` | Embedding model via OpenRouter | `openai/text-embedding-3-small` |
| `EXTRACT_MODEL` | Extraction LLM via OpenRouter | `anthropic/claude-haiku-4-5` |

---

## 7. Key Design Decisions vs Genesis

| Decision point | Genesis Brain Light | This system |
|---|---|---|
| Document layer | GitHub repo | This git repo (`research/`) |
| Reindex trigger | GitHub webhook → VPS FastAPI | Hermes cron + `git diff` |
| Query interface | Separate MCP server (FastAPI + FastMCP) | Hermes skill scripts |
| Blob storage | Cloudflare R2 | Not implemented |
| Auth | API key per user | Single Hermes profile (no auth) |

The core pipeline logic (chunking, embedding, extraction, SurrealDB schema) is identical to Genesis. See [GENESIS-BRAIN-LIGHT-DESIGN.md](../../research/regentribe/GENESIS-BRAIN-LIGHT-DESIGN.md) for the authoritative design rationale.

---

## 8. References

| Document | What it covers |
|---|---|
| [GENESIS-BRAIN-LIGHT-DESIGN.md](../../research/regentribe/GENESIS-BRAIN-LIGHT-DESIGN.md) | Full Genesis Brain Light design — authoritative source |
| [GENESIS-BRAIN-ARCHITECTURE.md](../../research/regentribe/GENESIS-BRAIN-ARCHITECTURE.md) | SurrealDB schema, current live architecture |
| [genesis-zero-bot/TOOLS.md](../../research/regentribe/genesis-zero-bot/TOOLS.md) | Production script interface, env vars, SurrealDB location |
| [CoCo-OpenClaw-vs-Hermes.md](../../research/The Coherence Company/CoCo-OpenClaw-vs-Hermes.md) | Why Hermes over OpenClaw for this system |
| [OpenClaw Dreams and HERMES Dreaming Architecture.md](../../research/The Coherence Company/OpenClaw%20Dreams%20and%20a%20HERMES%20Dreaming%20Architecture.md) | Memory consolidation context (post-MVP dreaming layer) |
| [07-knowledge-graph-and-compiled-knowledge-design.md](./07-knowledge-graph-and-compiled-knowledge-design.md) | Open questions on schema evolution |
| [05-memory-model-and-retrieval-policy.md](./05-memory-model-and-retrieval-policy.md) | Retrieval policy decisions to revisit post-MVP |
