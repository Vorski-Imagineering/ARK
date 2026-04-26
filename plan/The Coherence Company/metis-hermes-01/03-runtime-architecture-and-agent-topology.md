# 03. Runtime Architecture And Agent Topology

## Purpose

Define how HERMES is used inside METIS and what kinds of agents exist at runtime.

## Topics to answer

- Whether HERMES is the main runtime, a specialist reflective worker, or one layer in a larger orchestration stack.
- What the METIS control plane is that creates and manages HERMES-backed agents.
- Whether to use one HERMES profile per role, cohort, environment, or tenant.
- Whether to use one agent per project, one per conversation, one per user-facing thread, or a mix.
- The standard topology for a guide agent attached to an event, organization, or workstream.
- The initial agent roles.
- Which roles need separate state, credentials, and memory scopes.
- Which capabilities are shared platform capabilities versus per-agent capabilities.
- Where subagent delegation should be used and where workflows should stay deterministic.
- What events trigger agent activity.
- Whether a second orchestration layer such as LangGraph or equivalent is needed.

## Included answers from current materials

- HERMES is attractive for profile-isolated, long-lived agents with stronger learning and memory loops.
- One major open question is whether HERMES is the primary runtime or a specialist worker inside a broader orchestration spine.
- METIS needs to support agents across projects, conversations, and collaborations rather than one isolated agent.

## Still to answer

- The actual runtime topology for guide agents.
- The division between control plane and agent runtime.
- The right mix of project-level and conversation-level agents.
- Which roles exist in v1 and which are deferred.
