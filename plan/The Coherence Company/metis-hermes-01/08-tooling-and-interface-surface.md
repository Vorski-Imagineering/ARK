# 08. Tooling And Interface Surface

## Purpose

Define how operators, agents, and external clients interact with METIS.

## Topics to answer

- What `create a new agent` interface METIS should expose to operators.
- Which interfaces are required in v1: MCP, REST, CLI, messaging gateway, admin dashboard, review queue.
- Which tools should be exposed to HERMES directly.
- Which actions should require an intermediate service instead of direct database or storage access.
- How agents search transcripts, inspect provenance, propose memory writes, and request human approval.
- What operator tools are needed for audit, rollback, replay, and manual correction.
- What controls are needed to inspect all active agents by project and conversation scope.
- What external systems must integrate now versus later.

## Included answers from current materials

- METIS needs an easy setup path for new agents.
- The platform needs to operate agents across project and conversation scope, which implies operator-facing visibility and control surfaces.

## Still to answer

- The actual operator experience for provisioning and managing agents.
- The v1 interface set.
- The boundary between direct agent tools and mediated platform services.
