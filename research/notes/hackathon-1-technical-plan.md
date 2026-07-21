# Hackathon 1 technical plan — working notes

## 2026-07-21 — Decomposition and source scan

### Planning questions

1. What technical choices must be fixed before Day 1 so the event does not become an architecture workshop?
2. What choices benefit from comparison using real organisation sources during the event?
3. What complete vertical slice must already run before the event?
4. What is the smallest source model that retains organisation, source URL, publication date, retrieval text, and provenance?
5. Does the proof require a graph database, managed vector database, object storage, message queue, MCP server, or production agent runtime?
6. What interface proves the value if Telegram is not ready?
7. What remote development and staging infrastructure gives all builders a reproducible environment?
8. How are API credentials and runtime state kept outside the public repository?
9. What test fixtures and acceptance questions must exist before the event?
10. What model, embedding, hosting, repository, storage, and delivery costs should be authorised?
11. Which costs are truly required for the two-day event, and which belong only to a pilot?
12. What evidence would justify adding graph extraction, scheduled ingestion, Telegram, or a managed database after the baseline works?

### Internal source findings

- The ARC proposal requires a complete information loop with public organisational sources, sourced question answering, a digest, one accessible delivery path, and measurable cost. It also says the runtime should be replaceable without rebuilding the knowledge layer. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#10-minimum-viable-prototype] [see: proposal/hackathon-1/ARC Community Agent Proposal.md#11-high-level-technical-approach]
- The execution plan has already narrowed the two-day proof to three or more organisations, representative questions, one digest, one delivery channel, visible provenance, and a continuation decision. [see: proposal/hackathon-1/execution/00-start-here.md#minimum-demonstration]
- Genesis Brain Light separates an editable Git document layer from a derived query layer. [see: research/regentribe/GENESIS-BRAIN-LIGHT-DESIGN.md#1-overview]
- The Coherence/Hermes MVP makes the same durable decision: the markdown corpus is canonical and the graph can be rebuilt. It also defers webhooks, REST, multi-tenancy, and community clustering. [see: plan/The Coherence Company/metis-hermes-01/mvp.md#2-scope-vs-broader-hermes-memory-model] [see: plan/The Coherence Company/metis-hermes-01/mvp.md#3-what-is-explicitly-out-of-scope-mvp]
- The current Genesis architecture documents a missing automated document-to-database sync. This is a warning against making an incomplete inherited integration part of the critical demo path. [see: research/regentribe/GENESIS-BRAIN-ARCHITECTURE.md#whats-missing-needs-work]
- The alternatives review says a dedicated vector or graph system is justified by its query requirements; pure retrieval-augmented generation does not inherently require graph traversal. [see: research/regentribe/SURREALDB-ALTERNATIVES-RESEARCH.md#3-dedicated-vector-dbs-pinecone-weaviate-qdrant]

### External rate findings

- GitHub Free is listed at USD 0 per month with unlimited public/private repositories; standard GitHub Actions use remains free for public repositories. [source: https://github.com/pricing, accessed 2026-07-21]
- Hetzner's current EU CX23 price is EUR 5.49 per month excluding IPv4 and VAT following the 2026-06-15 price change. [source: https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/, accessed 2026-07-21]
- Cloudflare's Zero Trust Free plan is USD 0 for teams below 50 users and may be used to expose the shared staging service without a public IPv4. [source: https://www.cloudflare.com/plans/zero-trust-services/, accessed 2026-07-21]
- Telegram states that its bot platform is free for users and developers, but the bot's application code still runs on infrastructure controlled by the project. [source: https://core.telegram.org/bots, accessed 2026-07-21]
- OpenAI lists `text-embedding-3-small` at USD 0.02 per million input tokens. [source: https://developers.openai.com/api/docs/models/text-embedding-3-small, accessed 2026-07-21]
- OpenAI lists `gpt-5.6-luna`, its current cost-sensitive GPT-5.6 tier, at USD 1 per million input tokens and USD 6 per million output tokens. [source: https://developers.openai.com/api/docs/models/gpt-5.6-luna, accessed 2026-07-21]
- Cloudflare R2 includes 10 GB-month of Standard storage, one million Class A operations, and ten million Class B operations in its monthly free tier, but object storage is not required for the hackathon baseline. [source: https://developers.cloudflare.com/r2/pricing/, accessed 2026-07-21]

### Architecture pressure

The repo contains thoughtful graph, multi-source, multi-agent, and production deployment designs. They solve larger problems than the hackathon must prove. Importing them would create the following Day 1 failure risks:

- Schema and database setup before any representative question can be tested.
- Connector work for unstable sources.
- Authentication, webhook, and public-endpoint work unrelated to the value proof.
- Entity and relation extraction before plain retrieval quality is known.
- Several services that builders must understand and integrate remotely.
- A false sense that the graph, agent runtime, or Telegram interface is the product rather than one replaceable implementation.

### Recommended minimum baseline

Use a single Python application and a Git-backed public corpus.

1. Approved source packs and source snapshots are canonical, human-inspectable inputs.
2. One normaliser converts HTML, RSS, markdown, and prepared text snapshots to a common document record.
3. One chunker produces chunks with immutable source metadata.
4. One embedding model creates vectors.
5. For the small corpus, store metadata and chunks in SQLite and store vectors as arrays; brute-force cosine similarity is adequate and removes a database service.
6. One retrieval function returns ranked chunks with organisation, title, URL, publication date, and score.
7. One response generator receives only retrieved chunks and must emit a sourced answer or state that evidence is insufficient.
8. One digest function uses a selected update set and emits a sourced cross-organisation summary.
9. One thin web interface or command interface supports the demonstration.
10. Telegram is an adapter on top of the same query and digest functions, never the core.

SQLite is not a permanent architecture decision. It is a disposable derived index whose data can be rebuilt from Git. If the pilot needs concurrent writes, richer filtering, or graph traversal, it can be replaced after evidence exists.

### Working cost assumptions

- [ASSUMPTION: Five organisations provide no more than three sources each.]
- [ASSUMPTION: The prepared corpus is no more than one million tokens for the first event.]
- [ASSUMPTION: Preparation, testing, and the event consume no more than 300 generation calls averaging 8,000 input tokens and 1,000 output tokens.]
- [ASSUMPTION: One small shared EU server is provisioned for one month and exposed through an existing domain or a free tunnel.]
- [ASSUMPTION: Participants use existing video, chat, and local development tools at no incremental event cost.]

At current rates, one million embedding tokens cost approximately USD 0.02. The generation assumption costs approximately USD 4.20 with `gpt-5.6-luna`; doubling for prompt iteration, failed runs, and the pre-event build remains below USD 10. A USD 20 model credit therefore provides a wide hackathon buffer.

The server baseline is approximately EUR 5.49 per month excluding tax. GitHub, Telegram's platform, and a small Cloudflare Zero Trust account can remain at USD 0. Object storage is unnecessary; if later used within the R2 free tier, it remains at USD 0 for this scale.

### Budget recommendation

- Expected direct spend: approximately EUR 15–25 equivalent for one month, dominated by model credit and the server.
- Authorised hackathon ceiling: EUR 50 equivalent, including taxes, a model-use buffer, and small incidentals.
- Optional domain purchase: add EUR 10–20 if no suitable domain or stable temporary URL exists.
- One-month pilot ceiling: EUR 75 equivalent, including continued hosting, model use, and contingency.

### Decisions required before Day 1

- Technical lead and repository owner.
- Canonical corpus location and document metadata schema.
- Included source types and fallback snapshots.
- Python/runtime version and reproducible setup command.
- Default model provider, embedding model, answer model, and spend cap.
- Derived-index implementation and rebuild command.
- Source-citation contract and insufficient-evidence behaviour.
- Shared staging host, access method, and fallback local demo.
- Secrets owner and secret-delivery method outside Git.
- Three representative questions, one digest format, and acceptance tests.
- Whether Telegram is ready as the delivery adapter; if not, the fallback is locked.

### Questions suitable for the event

- Chunk size and overlap.
- Retrieval `top-k`, score threshold, keyword/vector blend, and query rewriting.
- Prompt structure and citation rendering.
- `gpt-5.6-luna` versus a stronger model for the final digest.
- Whether metadata filters improve organisation and time-bounded questions.
- Whether graph extraction reveals useful overlaps beyond retrieved evidence.
- Which source type should be automated first.
- Whether Telegram improves the tested journey enough to justify its maintenance.
- What collection and digest frequency a pilot should use.

### Reflection

[OPEN QUESTION: Does an existing public repository and deployment account already have an approved owner, or must new project infrastructure be created?]

[OPEN QUESTION: Is there an existing domain that may be used for a stable staging URL without creating a new public dependency?]

[OPEN QUESTION: Will the first cohort's sources remain below the assumed one-million-token corpus and avoid formats requiring OCR or licensed extraction?]

[OPEN QUESTION: Does the technical team have an existing working component worth reusing, provided it can pass the baseline source-to-answer test before the event?]

## 2026-07-21 — Access control, backup, and recovery refinement

The event remains an unpaid experimental service, but it must behave like a professionally operated playground: least privilege, clear control boundaries, routine backups, and rehearsed recovery.

[CONTRADICTS: proposal/hackathon-1/execution/05-technical-specification.md] The prior technical plan placed production hardening, backups, and disaster recovery outside the first two-hour runtime bootstrap and did not require a backup service for the event baseline. Production high availability remains out of scope, but event-level access control, backups, rollback, and a tested restore are now mandatory before Day 1.

### Access and recovery sub-questions

1. Which distinct access domains exist across repository, cloud control plane, server operating system, runtime, data, model provider, delivery channel, backups, and audit logs?
2. Which participant roles need read, operate, write, deploy, restore, billing, or administrative rights in each domain?
3. Which domains must never be reachable by participants or the agent?
4. How is server root access separated from routine deployment and application operation?
5. How are read-only query access and write-capable ingestion access separated?
6. How is the agent prevented from modifying canonical sources, deleting an index, rotating credentials, altering its own policy, or deleting backups?
7. Where is the private identity-to-role mapping stored, given that the public repository cannot contain private participant details or access URLs?
8. Which mutable artifacts are canonical, derived, operational, or ephemeral?
9. What backup schedule provides a tolerable recovery point during preparation, the event, and a pilot?
10. How are backups protected from the same credentials and mistakes that affect the live service?
11. What restore test proves that a backup is usable rather than merely present?
12. What is the deprovisioning process after the event or pilot?

### Mature playground principles

- Human users receive individual identities; no shared human administrator accounts.
- Multi-factor authentication is required on repository, cloud, tunnel/DNS, backup, and model-provider control planes where supported.
- The agent and its runtime service never run as `root` and never receive cloud-control or backup-control credentials.
- Root is an emergency and infrastructure-maintenance capability, not a builder convenience.
- Builders use repository branches and a controlled deployment path, not unrestricted server access.
- The participant-facing query process reads the live index but cannot write or delete it.
- Ingestion builds a new derived index and publishes it atomically after tests; it does not mutate the active index in place.
- Canonical source packs, approved snapshots, prompts, and reviewed outputs change through Git history and protected-branch review.
- Agent memory and runtime caches are non-canonical and may be discarded.
- Destructive operations are unavailable to the agent; human operators use explicit runbook commands after a fresh backup.
- Backups are off-host, time-stamped, checksum-verified, retained, and protected against immediate overwrite or deletion.
- A restore drill is part of the readiness gate.

### Access domains identified

1. Public repository and code review.
2. Continuous integration and deployment identity.
3. Cloud provider account and project control plane.
4. DNS or tunnel control plane.
5. Server SSH and emergency `root`/`sudo`.
6. Application deployment and service management.
7. Canonical source corpus.
8. Derived retrieval datastore.
9. Agent runtime, prompts, and control/kill switch.
10. Participant-facing agent interface.
11. Model-provider API project and billing.
12. Telegram bot or other delivery adapter.
13. Runtime logs and cost/audit summaries.
14. Off-host logical backups.
15. Cloud-server snapshots or automatic backups.
16. Private access inventory and recovery material.

The public technical plan can define these domains and map public roles. The actual account identifiers, access URLs, participant identities, SSH public keys, group membership, recovery codes, and secret locations belong in a private access register controlled by the infrastructure owner.

### Proposed role set

- Infrastructure owner: cloud project, DNS/tunnel, deletion protection, emergency server recovery, and final account ownership.
- Technical lead: deployment, service operation, datastore maintenance, agent control, and technical access review.
- Recovery custodian: independent backup visibility and restore capability; may be combined with the infrastructure owner for the event if a second person can still recover the system.
- Budget owner: model-provider billing, spend limits, and invoice visibility.
- Product/event lead: participant admission, agent pause/disable authority, publication approval, and access-expiry decisions; no root by default.
- Maintainer/builder: repository write through branches and deployment only through the agreed mechanism; no root, cloud billing, backup deletion, or direct production datastore write.
- Organisation representative/tester: participant-facing agent use and output review only.
- Agent service identity: read canonical sources and active index, write only bounded runtime logs/drafts; no shell, infrastructure, canonical write, restore, billing, or backup-delete rights.
- Ingest service identity: read canonical sources, build a new derived index, and atomically promote after tests; no root, cloud control, agent policy update, or backup-delete rights.
- Backup service identity: create new backup objects only; no live-service control and no deletion of retained backups.

### Update and rollback map

- Source packs and approved snapshots: Git pull request; rollback by Git revert.
- Agent instructions and prompts: Git pull request; rollback to prior commit and restart.
- Application code and dependency lock: Git pull request plus versioned deployment; rollback to prior release.
- Runtime configuration: private configuration managed by technical lead; rollback from a redacted version record plus secret re-injection.
- Derived index: created as a new file/database from canonical sources; validate, then atomic swap; rollback by selecting the previous index or rebuilding.
- Agent memory/cache: non-canonical runtime state; discard or restore only if useful.
- Draft outputs: separate draft path; human review before promotion to public reviewed outputs.
- Reviewed outputs: Git-tracked; rollback by revert with an explanatory correction.
- Logs: local operational state with sanitised summary; never a source of organisational truth.

### Backup and recovery target

- Canonical Git material is continuously recoverable from the remote repository and local clones.
- Enable the cloud provider's daily server backups; the current Hetzner reference provides seven rotating daily slots and prices the feature at 20% of server cost. [source: https://docs.hetzner.com/cloud/servers/backups-snapshots/overview/, accessed 2026-07-21] [source: https://docs.hetzner.com/cloud/billing/faq/, accessed 2026-07-21]
- Use SQLite's Online Backup API or `VACUUM INTO` for consistent live-database copies; do not use a plain file copy while transactions may be active. [source: https://www.sqlite.org/backup.html, accessed 2026-07-21] [source: https://www.sqlite.org/howtocorrupt.html, accessed 2026-07-21]
- Upload time-stamped logical backup archives to a separate private object-storage bucket. Apply a retention lock so the live server credential cannot immediately overwrite or delete them. Cloudflare R2 bucket locks prevent object deletion and overwriting during the configured retention period. [source: https://developers.cloudflare.com/r2/buckets/bucket-locks/, accessed 2026-07-21]
- During preparation and pilot: daily logical backup, retained 30 days.
- During the two event days: hourly logical backup, retained 14 days.
- Before every deploy, ingestion schema change, data migration, or manual repair: named restore point.
- Preserve a pre-event baseline and final-event snapshot for 90 days.
- Target recovery point: one hour during the event; 24 hours outside the event.
- Target recovery time: 60 minutes for the single-server playground.
- Run a complete restore into an isolated path or replacement server before the readiness gate and run the smoke/acceptance tests against it.

### Budget impact

On the current EUR 5.49 reference server, the provider's 20% automatic-backup charge is approximately EUR 1.10 per month before tax. Logical backups remain within the previously verified R2 free tier at this scale. The expected event cost rises only marginally; the EUR 50 event ceiling and EUR 75 pilot ceiling remain sufficient.

[OPEN QUESTION: Which private password manager or access-register system will hold the actual identity mapping, recovery material, and access-expiry dates?]

[OPEN QUESTION: Can infrastructure ownership and recovery custody be held by two different people for the event, or must the minimum team combine them while retaining a second recovery-capable operator?]

[OPEN QUESTION: Will the selected runtime allow a clean read-only query identity and a separate write-capable ingestion identity, or must the separation be enforced through operating-system permissions and separate processes?]

## 2026-07-21 — Runtime-first correction

The existing custom Python retrieval baseline remains useful as a build-on-top layer, but it is no longer the first technical milestone.

[CONTRADICTS: research/synthesis/hackathon-1-technical-plan.md] Before the two-week participant ramp, the technical lead installs and configures OpenClaw or Hermes in a two-hour block. The runtime reads public planning documents and one approved sample source, answers three smoke-test questions with repository paths, drafts an action list, restarts predictably, and exposes no credentials or private data.

The Python normaliser, chunker, embedding, retrieval, answer, and digest components are added only when runtime-native file/source handling cannot pass the event’s sourced-answer and digest acceptance tests. The Git corpus remains canonical and rebuildable regardless of runtime.

[ASSUMPTION: The target machine, model-provider access, repository checkout, and primary operator are ready before the two-hour clock begins.]

[OPEN QUESTION: Which primary runtime is selected by the decision rule: Hermes for one evolving preparation agent, or OpenClaw for immediate multi-channel routing?]
