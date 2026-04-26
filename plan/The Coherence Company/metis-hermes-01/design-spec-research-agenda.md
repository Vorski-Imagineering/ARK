# Metis Hermes 01 - Design Spec Research Agenda

## Purpose

This document defines the research and decision checklist required before writing the build spec for a HERMES-based agent system that works with the Genesis Brain Light direction.

The goal is not to answer these questions yet. The goal is to make sure the eventual design spec is based on explicit decisions instead of hidden assumptions.

## Reframed objective

The core thing to build is a reusable METIS framework for setting up agents easily across many projects, not a one-off agent for a single workspace.

The framework should make it straightforward to create:

- guide agents for a coherence event, an organization, or a workstream;
- project agents for spaces such as The Gathering global, The Gathering local, The Coherence Company, and ARK;
- conversation agents where each coherence conversation can have its own bounded agent context;
- collaboration agents for shared workspaces that cut across organizations;
- shared platform services that support all of these agent types consistently.
- openess to experimentation with different agentic projects by our teams

The primary pattern is "agent as guide" with bounded context and responsibility. This means the design spec must answer not only how one HERMES-based agent works, but how METIS provisions, scopes, governs, and operates many guide agents reliably.

## Current starting point

The existing repo material suggests a few strong starting assumptions:

- Genesis Brain Light should keep an editable document layer and a separate queryable memory/knowledge layer.
- The agent runtime should not become the system of record.
- HERMES is attractive for profile-isolated, long-lived agents with stronger learning and memory loops.
- "Dreaming" should mean governed periodic consolidation over evidence, not free-form memory promotion.
- Transcript-native institutional memory will require richer primitives than `document`, `chunk`, and `concept` alone.

[ASSUMPTION: "HERMES" here means the Hermes Agent runtime discussed in the existing Coherence Company research files.]
[ASSUMPTION: SurrealDB remains the default canonical memory candidate unless research shows a blocking mismatch.]

## Inputs that should anchor the spec

- `research/regentribe/GENESIS-BRAIN-LIGHT-DESIGN.md`
- `research/regentribe/GENESIS-BRAIN-ARCHITECTURE.md`
- `research/The Coherence Company/CoCo-OpenClaw-vs-Hermes.md`
- `research/The Coherence Company/OpenClaw Dreams and a HERMES Dreaming Architecture.md`
- `research/The Coherence Company/Agent orchestration and memory systems for transcript-native institutional intelligence.md`

## Definition of done for the design spec

The design spec is ready to write only when we can answer all of the following at a clear architectural level:

- How METIS works as the common framework for creating and operating agents across projects and conversations.
- What the system is for, for whom, and what success looks like.
- How the guide role is defined for an event, organization, or workstream.
- How a new project or conversation gets its own agent with minimal setup.
- Which runtime components are HERMES-native versus custom.
- What the canonical memory plane is, and what data lives there.
- How agents write, read, consolidate, and verify memory.
- How transcripts, documents, entities, decisions, and procedures are represented.
- How agent instances are scoped at the project, collaboration, and conversation level.
- How multi-agent coordination works without collapsing privacy, trust, or provenance.
- How humans review, override, rollback, and audit the system.
- How the first production slice will be evaluated, deployed, and operated.

## Research workstreams

## 1. Product and operating model

This workstream defines the actual job of the system.

Questions to answer:

- Is METIS primarily an agent framework, an institutional memory platform, or both?
-> METIS is the relation, management and configuration and journey management platform, let's say that memory, surrealDB is also part of 
-> we want to be able to configure on this server both METIS-managed agents, and HERMES-agents, 
-> we want to be able to clone agents to create duplicates for different groups, copy either whole agent and same DB, just different membership, or just copy skills not memory

- What is the standard lifecycle for creating a new agent in METIS?
-> manualy configured for now.

- Is the core use case best defined as a guide for a coherence event, an organization, or a workstream?
-> we have three types of agents we'll me running here: coherence event agents, collaboration space agents (for teams, or for partnerships such as this ARK), we also want to experiment with living book ideas - see LIVING-BOOK-MANIFESTO.md

- What does "guide" mean operationally in this system: navigator, explainer, memory steward, matchmaker, facilitator support, workflow assistant?
-> all of those depending on context, we want to be able to configure all those in our system

- Who are the primary actors in v1: participants, facilitators, operators, researchers, admins, autonomous agents?
-> team, event organisers, event participants

- What are the highest-value outputs: answers, summaries, recommendations, match suggestions, memory pages, workflow actions, alerts?
-> knowledge, understanding and wisdom

- What decisions must the system support better than a normal RAG assistant?
-> understanding across many layers and viewpoints, seeing from different angles
-> dialogue and collaboration between agents

- What should the system never do autonomously in v1?
-> spend money

- What is the boundary between "assistant", "delegate", "worker", and "institutional memory compiler"?
-> some work in the background, some in the foreground, only some of the agents talk directly with humans

- What is the boundary between a project agent, a conversation agent, and a platform service?
-> we need to define clear templates and definition formats for agents

- What are the success metrics for the first release?
-> works for CoCo v1.0, allow us to create team support agents.

Expected output:

- A one-page operating model with primary users, core jobs, non-goals, and success criteria.

## 2. System boundary and source of truth

This workstream settles which subsystem owns truth.

Questions to answer:

- What is the system of record for raw transcripts, editable notes, derived knowledge, and agent procedures?
-> git repo of .md files of extraction, and different for others...

- Which data is immutable raw evidence, and which data is derived or promotable?
-> need a clear metadata describing who produced what -> git record can do this

- Which parts live in GitHub, which in SurrealDB, which in object storage, and which in HERMES-local state?
-> need the design!

- What must never be stored only in HERMES memory files or profile state?
-> tokens, access keys

- Do we need a compiled wiki layer in addition to graph memory?
-> yes! where and how is best?

- What are the durability and deletion requirements for each data class?


Expected output:

- A source-of-truth map covering every major data type and its lifecycle.

## 3. Runtime architecture and agent topology

This workstream determines how HERMES is actually used.

Questions to answer:

- Is HERMES the main runtime, a specialist reflective worker, or one layer in a larger orchestration stack?
-> one layer

- What is the METIS control plane that creates and manages HERMES-backed agents?
see ../METIS/

- Do we want one HERMES profile per role, per cohort, per environment, or per tenant?
-> desrive what this means?

- Do we want one agent per project, one per conversation, one per user-facing thread, or a mix of these?
per project (some projects could have multiple agents, each with a personality..)

- What is the standard topology for a guide agent attached to an event, organization, or workstream?
-> more info? what do we need to decide?

- What are the initial agent roles: intake, retriever, planner, synthesizer, verifier, procedural distiller, group-memory coordinator, operator interface?
-> need to design.

- Which roles need separate state, credentials, and memory scopes?
-> design

- Which capabilities are shared platform capabilities versus per-agent capabilities?
-> agents can share skills, and some memories are shared between agents, each agent should have it's own SOUL.md

- Where should subagent delegation be used, and where should workflows stay deterministic?
-> more info.

- What events trigger agent activity: incoming messages, webhook updates, schedules, manual review, failed tasks, weekly sweeps?
-> all

- Do we need a second orchestration layer such as LangGraph or equivalent for checkpointed institutional workflows?
-> We will use METIS - see ../METIS/

Expected output:

- A runtime topology diagram with named agents, triggers, boundaries, and responsibilities.

## 3A. Provisioning, templates, and tenancy

This workstream defines how METIS makes agent setup easy and repeatable.

Questions to answer:

- What is the unit of provisioning: project, organization, conversation, cohort, region, or workspace?
we should be able to attach agents to any of those. we will use ../METIS/core/model.py for our topology

- What baseline template should every new METIS agent receive?
-> need design

- What baseline template should every new guide agent receive?
-> need design

- Which configuration surfaces should be declarative: tools, memory scopes, policies, schedules, identity, model routing, review gates?
-> need design

- What defaults should exist so a new project can launch an agent with minimal manual setup?
-> and how do we have an effective template and DNA system allowing us to combine and breed agents.

- How are project-level agents related to child conversation-level agents?
-> need design

- How are names, identities, and state directories generated and managed?\
-> need design

- How do we clone, fork, archive, pause, or delete agents safely?
-> need design

- What tenancy boundaries are required between The Gathering global, The Gathering local, The Coherence Company, ARK, and future collaborations?
-> need design

Expected output:

- A provisioning model with templates, inheritance rules, and tenancy boundaries.

## 4. Transcript and event model

This workstream upgrades the system from "document ingestion" to transcript-native memory.

Questions to answer:

- What is the canonical schema for conversations, turns, participants, channels, attachments, replies, timestamps, and sessions?
- Which derived objects do we need in v1: claims, questions, decisions, commitments, interests, summaries, contradictions, affinities, tasks?
- How do we represent provenance from every derived object back to exact source turns or documents?
- How are edits, redactions, deletions, and reversals represented over time?
- What access-control or sensitivity labels must exist at the event level?
- What is the ingestion path for chat transcripts versus markdown docs versus uploaded files?

Expected output:

- A core event and transcript schema with provenance rules.

## 5. Memory model and retrieval policy

This workstream defines what "memory" means operationally.

Questions to answer:

- Which memory layers are required in v1: working, episodic, mid-term, durable semantic, durable procedural, group memory?
- What data belongs in each layer?
- What is HERMES allowed to read directly from its built-in memory versus the external memory plane?
- What retrieval modes are required: lexical, vector, graph traversal, temporal lookup, procedural recall, user-model recall?
- What should be retrieved at interaction time versus only during offline consolidation?
- How should memory freshness, contradiction, and confidence be surfaced to agents and humans?
- Do we need per-agent local memory plus shared group memory from day one, or should shared memory wait?

Expected output:

- A layered memory model and retrieval contract for both online and offline use.

## 6. Dreaming and consolidation architecture

This workstream is the most HERMES-specific design question.

Questions to answer:

- What exactly counts as a "dream" in this system: clustering, reflection, contradiction repair, procedure distillation, human-readable reports?
- What are the promotion rules from episodic evidence into durable memory?
- What candidate types can be promoted: facts, relations, summaries, procedures, user-model updates, shared conventions?
- What must always be verified before promotion?
- What is the difference between local dreams and group dreams?
- What cadence should be used for micro-dreams, nightly deep dreams, and group dreams?
- Which dream outputs are explanatory only and must never be treated as truth?
- What rollback and reindex mechanisms exist if a dream writes something wrong?

Expected output:

- A consolidation design with promotion thresholds, sweep cadence, and rollback rules.

## 7. Knowledge graph and compiled knowledge design

This workstream settles the external memory schema.

Questions to answer:

- Is the current `document/chunk/concept/community` model enough, or what new entities and edges are required?
- Do we need explicit `claim`, `evidence`, `decision`, `person`, `project`, `question`, `procedure`, `affinity`, or `trend_shift` records?
- What temporal semantics are needed: valid-from, valid-to, superseded-by, contradicted-by?
- What graph queries must the system support in v1?
- Do we want generated entity pages or wiki pages compiled from the graph?
- How should graph memory and markdown/wiki memory stay in sync?
- What indexing strategy is needed for hybrid retrieval and graph traversal at expected scale?

Expected output:

- A target memory schema and list of required query patterns.

## 8. Tooling and interface surface

This workstream defines how agents and humans touch the system.

Questions to answer:

- What "create a new agent" interface should METIS expose to operators?
- Which interfaces are required in v1: MCP, REST, CLI, messaging gateway, admin dashboard, review queue?
- Which tools should be exposed to HERMES directly?
- Which actions should require an intermediate service instead of direct database or storage access?
- How will agents search transcripts, inspect provenance, propose memory writes, and request human approval?
- What operator tools are needed for audit, rollback, replay, and manual correction?
- What controls are needed to inspect all active agents by project and conversation scope?
- What external systems must integrate now versus later?

Expected output:

- A tool and interface matrix covering agent tools, human tools, and service APIs.

## 9. Governance, privacy, and trust

This workstream keeps the architecture from becoming an elegant compliance failure.

Questions to answer:

- What categories of data are allowed into the memory plane?
- What must be redacted, anonymized, encrypted, or excluded before ingestion?
- What are the visibility scopes for participant, cohort, operator, and agent memories?
- What trust model applies to cross-agent messages and group-memory proposals?
- Which writes require human review?
- What approval, rollback, and deletion guarantees are mandatory?
- How are provenance, signed writes, and policy decisions recorded?
- What is the policy for sharing or publishing dream reports or summaries externally?

Expected output:

- A governance model with data classes, trust boundaries, review gates, and rollback policy.

## 10. Evaluation and benchmark design

This workstream defines how we will know the system is good.

Questions to answer:

- What task-level benchmarks matter most for this system?
- How do we measure factual recall, update handling, contradiction detection, matchmaking usefulness, and summary fidelity?
- What safety tests are required for memory poisoning, cross-domain leakage, sycophancy, and unauthorized retention?
- What multi-agent quality metrics matter: agreement, diversity of contribution, contradiction rate, repair success?
- What cost and latency budgets are acceptable for online interaction and offline consolidation?
- What offline benchmark suite should be run before rollout?
- What live acceptance tests should gate deployment?

Expected output:

- An evaluation plan with benchmark set, acceptance thresholds, and regression tests.

## 11. Deployment, scaling, and operations

This workstream turns architecture into something operable.

Questions to answer:

- What is the first deployment shape: one VPS, one database, one object store, multiple HERMES profiles?
- How many concurrent project agents and conversation agents should the first architecture support?
- How are secrets, credentials, and per-agent identities managed?
- What background jobs, queues, and schedulers are required?
- What observability is required for runs, memory writes, failures, and dream sweeps?
- What are the backup and disaster-recovery requirements?
- What operational limits should exist on token budgets, sweep frequency, and background job concurrency?
- What scale assumptions should shape the v1 design: users, cohorts, transcripts per day, documents per day?

Expected output:

- An operations blueprint with deployment shape, observability, and resource controls.

## 12. Migration and implementation sequencing

This workstream makes the design buildable.

Questions to answer:

- What can be reused from the current Genesis Brain pipeline without major redesign?
- What must be built first to de-risk the architecture?
- What is the minimum end-to-end slice that proves the design?
- What is the smallest slice that proves easy agent setup in METIS rather than only one successful custom agent?
- What should be explicitly deferred from v1?
- What data migrations or backfills are needed?
- What experiments should happen before schema lock-in?
- What is the phase plan from local dreams to governed group memory?

Expected output:

- A phased roadmap with prerequisites, pilot slice, and deferrals.

## Cross-cutting decision register

The design spec should not be written until each of these decisions has an explicit answer:

- METIS control-plane responsibilities.
- Agent provisioning template and setup flow.
- Guide-agent role definition and template.
- HERMES role in the stack.
- Project-agent versus conversation-agent model.
- Canonical memory plane.
- Transcript/event schema.
- Durable semantic memory schema.
- Durable procedural memory schema.
- Local versus shared memory boundary.
- Dream cadence and promotion rules.
- Human review gates.
- Provenance and rollback model.
- Evaluation thresholds for go/no-go.
- First production slice and what is deferred.

## Recommended order of research

1. Settle product scope and operating model.
2. Lock the source-of-truth model and data boundaries.
3. Define transcript/event schema and memory layers.
4. Define HERMES runtime topology and consolidation flow.
5. Define governance and trust model.
6. Define evaluation plan.
7. Only then write the implementation spec and roadmap.

## What the final design spec should include

When the research above is complete, the build spec should contain:

- System goals and non-goals.
- METIS platform model and provisioning flow.
- Guide-agent model for events, organizations, and workstreams.
- Architecture diagram.
- Agent topology.
- Tenancy and scoping model.
- Data model and schemas.
- Memory and dreaming policies.
- Interface and tool contracts.
- Governance and review rules.
- Evaluation gates.
- Deployment architecture.
- Implementation phases.

## Open questions to keep visible from the start

- [OPEN QUESTION: What is the minimal METIS agent template that works across projects without becoming too generic to be useful?]
- [OPEN QUESTION: What is the minimal guide-agent template that still works across an event, an organization, and a workstream?]
- [OPEN QUESTION: Should each coherence conversation have a first-class child agent, or should conversations stay as scoped contexts inside a project agent until scale forces a split?]
- [OPEN QUESTION: Is HERMES the primary runtime or a specialist worker inside a broader orchestration spine?]
- [OPEN QUESTION: Can SurrealDB carry the full temporal institutional-memory model cleanly, or does the graph/query shape force a second memory system later?]
- [OPEN QUESTION: How much shared memory is safe in v1 before message trust and privacy boundaries are mature enough?]
- [OPEN QUESTION: Which outputs need human approval by default: memory promotion, summaries, recommendations, or external messages?]
- [OPEN QUESTION: What is the smallest pilot that proves this architecture without prematurely committing to full group-memory complexity?]
