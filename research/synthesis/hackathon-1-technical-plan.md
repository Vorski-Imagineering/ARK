# Hackathon 1 technical plan — synthesis

**Status:** Synthesized recommendation  
**Date:** 2026-07-21  
**Operational specification:** `proposal/hackathon-1/execution/05-technical-specification.md`

## Question

What technical decisions and infrastructure must be prepared before a remote two-day ARC Agent hackathon, what should be explored using real sources during the event, and what budget is sufficient for the minimum viable proof?

## Conclusion

The hackathon should begin from a complete but deliberately small vertical slice:

Approved public source packs  
→ normalised documents with provenance  
→ chunks and embeddings  
→ lightweight similarity retrieval  
→ sourced answers and one cross-organisation digest  
→ one participant interface  
→ representative review.

Use a single Python application, a Git-backed canonical corpus, a disposable SQLite/file-based retrieval index, one model-provider account, and one small shared staging server. Do not require a graph database, managed vector store, object storage, message queue, MCP server, webhook pipeline, multi-tenant auth system, or production monitoring before the event.

This is not a rejection of the repo’s graph architecture. It is an order-of-operations decision. The repo consistently separates editable canonical documents from derived query state and keeps the runtime replaceable. [see: research/regentribe/GENESIS-BRAIN-LIGHT-DESIGN.md#1-overview] [see: plan/The Coherence Company/metis-hermes-01/mvp.md#2-scope-vs-broader-hermes-memory-model] The hackathon should first establish that sourced cross-organisation retrieval creates value; graph extraction becomes a justified experiment only when representative questions require relationship traversal that the baseline cannot support.

## Required decisions before the event

The following must be fixed before Day 1:

1. A technical lead and budget owner.
2. One repository and contribution workflow.
3. Source packs and approved snapshots as the canonical event corpus.
4. Included source types: prepared text/markdown, stable HTML, and RSS by default.
5. A minimal document, source, chunk, output, and usage schema.
6. Python 3.12 and a reproducible locked environment.
7. A lightweight chunk-embedding-cosine retrieval baseline.
8. One provider account, default embedding and generation models, and a hard spend limit.
9. A citation contract and an explicit insufficient-evidence response.
10. One participant interface and one fallback.
11. One shared staging host and a tested local screen-share path.
12. Private secret delivery outside the public repository.
13. Three representative questions, a negative question, one digest scope, and acceptance tests.
14. A decision on whether Telegram is ready; otherwise it leaves the critical path.

These choices are preparation, not collaborative exploration. Leaving them open would spend the two build days on tooling and account setup rather than community value.

## Appropriate hackathon experiments

The event should use real sources and representative judgment to explore:

- Chunk size, overlap, retrieval depth, and relevance threshold.
- Vector-only versus keyword-plus-vector retrieval.
- Organisation and date filtering.
- Query rewriting and its risk of changing intent.
- Answer and digest prompts.
- Citation clarity and correction workflow.
- Cost-sensitive versus stronger generation models on a fixed test set.
- Digest length, structure, and frequency.
- Whether Telegram improves the primary journey.
- Which source type is worth automating first.
- Whether graph relation extraction reveals useful connections that the baseline misses.

The baseline must pass before graph, interface, or connector stretch work begins.

## Infrastructure that should exist before Day 1

### Repository

- Source packs, safe fixture, prompts, tests, and reviewed outputs.
- A readable separation between canonical inputs and derived index state.
- Locked dependencies and one-command setup, ingest, query, digest, test, and run operations.
- A public CI path or shared test command.

GitHub's Free tier and public-repository Actions are sufficient at USD 0 for this scale. [source: https://github.com/pricing, accessed 2026-07-21] [source: https://docs.github.com/en/billing/concepts/product-billing/github-actions, accessed 2026-07-21]

### Application

- Source loader for prepared text, markdown, stable HTML, and RSS.
- Normaliser and chunker retaining source metadata.
- Embedding and retrieval functions.
- Sourced answer and digest functions.
- Minimal web or command interface.
- Optional Telegram adapter using the same core functions.
- Structured usage and cost logging.
- Tests for schema, ingest, retrieval, citations, and insufficient evidence.

### Staging

- One small EU Linux server running the single application process.
- Local persistent state that can be deleted and rebuilt.
- A free outbound tunnel or existing reverse proxy.
- A restart procedure known by two people.
- A local fallback that can be demonstrated through screen sharing.

A current CX23-class reference server is EUR 5.49 per month excluding IPv4 and VAT. [source: https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/, accessed 2026-07-21] Cloudflare lists a USD 0 Zero Trust plan for teams under 50 users, sufficient as a reference route for a small tunnel-based setup. [source: https://www.cloudflare.com/plans/zero-trust-services/, accessed 2026-07-21]

### Model access

- A project-owned account with USD 20 authorised usage.
- Credential injection outside Git.
- Visible usage and cost accounting.
- Configurable model identifiers.
- Cached embeddings and content-hash-based re-ingestion.

Current reference prices are USD 0.02 per million embedding input tokens for `text-embedding-3-small` and USD 1 input / USD 6 output per million tokens for `gpt-5.6-luna`. [source: https://developers.openai.com/api/docs/models/text-embedding-3-small, accessed 2026-07-21] [source: https://developers.openai.com/api/docs/models/gpt-5.6-luna, accessed 2026-07-21]

## Budget

### Assumptions

- [ASSUMPTION: Five organisations contribute no more than three sources each.]
- [ASSUMPTION: The first corpus is no more than one million tokens.]
- [ASSUMPTION: Preparation and the event use no more than 300 generation calls averaging 8,000 input and 1,000 output tokens.]
- [ASSUMPTION: One small server is retained for one month.]
- [ASSUMPTION: Existing video, chat, developer devices, and an existing domain or free tunnel are available.]

Under these assumptions:

- Embedding the corpus costs approximately USD 0.02.
- Generation costs approximately USD 4.20; doubling for retries and prompt iteration remains below USD 10.
- A one-month reference server costs EUR 5.49 plus applicable tax.
- Repository, public CI, Telegram platform use, and the reference tunnel plan can cost zero.
- Object storage is unnecessary; Cloudflare R2's Standard free tier would cover 10 GB-month if a pilot later requires it. [source: https://developers.cloudflare.com/r2/pricing/, accessed 2026-07-21]

The expected direct spend is approximately EUR 15–25 equivalent. Authorise a EUR 50 ceiling for preparation and the event, including taxes, exchange-rate movement, model retries, and small incidentals. Add EUR 10–20 only if a new domain is necessary.

Authorise up to EUR 75 equivalent for a one-month pilot only after the Day 2 continuation decision.

## Why the larger repo architecture is deferred

The Genesis and Coherence work describes Git-based canonical documents, SurrealDB, vector and graph retrieval, several source integrations, runtime skills, and scheduled or webhook ingestion. This is a coherent longer-term architecture. It also documents incomplete sync paths and explicitly defers several production surfaces in its own MVP. [see: research/regentribe/GENESIS-BRAIN-ARCHITECTURE.md#whats-missing-needs-work] [see: plan/The Coherence Company/metis-hermes-01/mvp.md#3-what-is-explicitly-out-of-scope-mvp]

The ARC hackathon has a smaller question: does a shared, sourced information loop produce useful cross-organisation awareness? A graph is warranted only if this value proposition survives and graph-specific queries materially outperform simpler retrieval.

## Readiness conclusion

The technical setup is ready when a safe fixture completes the full path locally and on staging; a second builder can set up the project; source provenance survives retrieval; supported and unsupported questions behave correctly; the digest contains sources; usage cost is visible; and the fallback demonstration works without live sources or staging.

- [OPEN QUESTION: Which repository and deployment account will own the event infrastructure?]
- [OPEN QUESTION: Is an existing domain available for staging?]
- [OPEN QUESTION: Will the first cohort require PDF, video, social-platform, or OCR handling that must be converted to approved text snapshots before Day 1?]
- [OPEN QUESTION: Is Telegram part of the acceptance test or a stretch adapter?]

[CONFIDENCE: high] The proposed baseline is sufficient for the two-day proof. Compute and model costs are minor; source readiness, provenance, reproducible setup, and scope discipline are the material technical risks.

## 2026-07-21 addendum — Two-hour runtime bootstrap

The technical plan now begins with an installed agent runtime rather than a custom application.

[CONTRADICTS: research/synthesis/hackathon-1-technical-plan.md] The single Python application described above is a conditional retrieval extension, not the first milestone. Before invitations, a technical operator uses one two-hour block to install and configure Hermes or OpenClaw, connect one provider privately, load public planning material and one approved public sample source, apply public-data and human-approval instructions, run smoke tests, and prove restartability.

Hermes is the recommended default for one evolving agent that assists preparation. OpenClaw is the recommended default when Telegram or multi-channel gateway routing is the immediate priority. Both are permitted only with parallel operators and must remain replaceable clients of the Git-backed canonical corpus. [see: research/The Coherence Company/CoCo-OpenClaw-vs-Hermes.md#recommended-architecture-for-coco]

After bootstrap, add the detailed Python retrieval layer only where measured source attribution, retrieval, or digest tests require it. The operational specification is `proposal/hackathon-1/execution/05-technical-specification.md`.

## 2026-07-21 addendum — Access control and a recoverable playground

The event environment should remain minimal, but minimal does not mean fragile. Before Day 1, the organisers must establish an access inventory, role boundaries, deletion protection, an off-host logical backup, and a tested restore path. These are event-readiness controls rather than a production high-availability programme.

[CONTRADICTS: research/synthesis/hackathon-1-technical-plan.md] The earlier baseline treated object storage as unnecessary. A small off-host backup bucket is now part of the baseline so a server, operator, or agent mistake cannot destroy both the working state and its recovery copy. The expected volume remains within Cloudflare R2's Standard free tier under the stated assumptions. [source: https://developers.cloudflare.com/r2/pricing/, accessed 2026-07-21]

### Control model

The private access register must enumerate the repository, CI, cloud account, DNS or tunnel, SSH, root or sudo, deployment, canonical data, active index, agent control plane, participant interface, model provider, delivery channel, logs, logical backups, provider backups, and the register itself. For every human and service identity it records the owner, permitted actions, authentication method, grant and expiry dates, approver, and revocation and recovery routes. It contains no credential values and is not committed to this public repository.

Routine participation must not imply infrastructure control. Builders may contribute through branches and operate the documented application path; only the infrastructure owner and technical lead receive routine administration rights. A separate recovery custodian must be able to restore service if the technical lead is unavailable. The agent, ingest process, backup process, and deployment process use separate service identities with only the capabilities each needs.

The agent must not receive root or sudo, unrestricted shell access, canonical-source write access, datastore administration, backup deletion, credential-management rights, or the ability to grant itself new tools. Query access is read-only. Ingestion builds a new disposable index and promotes it only after checks pass, preserving the prior indexes for immediate rollback. Prompts and tool policy are versioned in Git and changed through human review.

### Recovery model

The operational target is a one-hour recovery-point objective during the event, a 24-hour target during preparation and a pilot, and a 60-minute recovery-time objective for the demonstrated path. The backup stack consists of Git history for code and public configuration, consistent SQLite logical backups before material changes and at least hourly during the event, versioned runtime configuration, daily provider backups, named snapshots around high-risk changes, and an off-host locked copy of logical backups. SQLite backups must use its Online Backup API or another documented consistent method rather than copying a live database file casually. [source: https://www.sqlite.org/backup.html, accessed 2026-07-21] [source: https://www.sqlite.org/howtocorrupt.html, accessed 2026-07-21]

A backup is accepted only after checksum verification and an isolated restore test. Pre-event 3 rehearses restoration, deployment rollback, the agent kill switch, and access revocation. Recovery should rebuild from canonical sources and reviewed configuration wherever possible; generated drafts, caches, and disposable indexes are recoverable convenience state rather than sources of truth.

### Cost impact

The provider's automatic backup option adds approximately 20% of the reference server price, about EUR 1.10 before tax for a EUR 5.49 server, and provides seven backup slots. [source: https://docs.hetzner.com/cloud/billing/faq/, accessed 2026-07-21] The expected event spend therefore becomes approximately EUR 16–27 equivalent, while the existing EUR 50 preparation-and-event ceiling remains adequate. The off-host logical backup is expected to cost EUR 0 at this scale under the R2 free-tier assumptions.

[OPEN QUESTION: Which private system will hold the access register and recovery contacts?]
[OPEN QUESTION: Who will hold the infrastructure-owner, recovery-custodian, and budget-owner roles?]
[OPEN QUESTION: Does the selected runtime support clean separation of query, ingest, agent-control, and backup service identities, or must the event enforce part of that separation at the operating-system layer?]

[CONFIDENCE: high] These controls materially reduce the risk of user or agent error without turning the two-day experiment into a production-platform project. The complete domain matrix, update map, backup schedule, restore procedure, acceptance gates, and budget are maintained in `proposal/hackathon-1/execution/05-technical-specification.md`.
