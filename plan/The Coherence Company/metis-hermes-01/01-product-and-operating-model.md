# 01. Product And Operating Model

## Purpose

Clarify what METIS is for, who it serves, and what the guide-agent model is meant to do.

## Scope of this file

This file takes the answers already captured in the main design agenda and turns them into a first-pass product and operating model. It does not add new external research. Where a point is still unresolved, it is kept in `Open Questions` at the end.

## Core design answer

METIS should be designed as both:

- an agent framework for creating, configuring, and operating many agents across projects, conversations, and collaborations;
- a relation, management, configuration, and journey-management platform that coordinates those agents and the contexts they serve.

In practice, this means METIS is not just a chat surface and not just a memory layer. It is the platform that binds together:

- agent identity and configuration;
- memory and knowledge infrastructure;
- project, event, organization, and workstream context;
- human membership and access scope;
- operational workflows for creating and managing agents.

HERMES is one runtime layer inside this broader METIS system, not the whole system.

## Primary use case

The primary pattern is `agent as guide`.

The core use cases are:

- a guide for a coherence event;
- a guide for an organization;
- a guide for a workstream.

METIS should also support adjacent patterns that reuse the same framework:

- project agents for spaces such as The Gathering global, The Gathering local, The Coherence Company, and ARK;
- conversation agents with bounded context for coherence conversations;
- collaboration agents for team or partnership spaces;
- experimental agentic projects such as living-book style systems.

The key design principle is that these should all feel like variations of one platform model, not unrelated agent types built from scratch every time.

## What `guide` means in this system

`Guide` is an umbrella operating role rather than a single narrow behavior.

Depending on scope and context, a guide agent may act as:

- navigator: helping people orient inside an event, organization, or workstream;
- explainer: answering questions and translating context into understandable language;
- memory steward: maintaining awareness of relevant knowledge, history, and prior decisions;
- matchmaker: helping connect people, ideas, and opportunities;
- facilitator support: helping organizers or team members prepare, summarize, and coordinate;
- workflow assistant: supporting practical follow-through where appropriate.

The important design choice is that these are configurable guide behaviors, not separate product categories. A given agent may emphasize different guide functions depending on where it is attached.

## Product definition

### What METIS is

METIS is the platform that lets the team define and operate scoped agents with shared infrastructure and configurable identity.

Its job is to make it easy to:

- create an agent for a new project, event, organization, workstream, or conversation;
- attach the right people, memory, tools, and permissions to that agent;
- clone or adapt an existing agent pattern for a new group;
- support both foreground human-facing agents and background support agents;
- coordinate experimentation without turning every experiment into a bespoke infrastructure problem.

### What METIS is not

METIS should not be treated as:

- only a RAG frontend;
- only a memory database;
- only a HERMES deployment wrapper;
- a system that gives every agent unrestricted autonomy.

## Operating model

### Primary actors in v1

The primary actors are:

- team members;
- event organizers;
- event participants.

Secondary actors likely include:

- operators who configure and maintain agents;
- facilitators who use guide outputs in human processes;
- background agents that support human-facing agents.

### Core jobs to be done

The first release should help people:

- understand what is happening in a given event, organization, or workstream;
- navigate relevant knowledge and context;
- see issues from multiple viewpoints and layers;
- support dialogue and collaboration between humans and, where useful, between agents;
- create reusable support agents for teams without rebuilding the stack each time.

### Highest-value outputs

The stated desired output is `knowledge, understanding and wisdom`.

Translated into system behavior, the first release should prioritize:

- answers grounded in the right local context;
- summaries that improve shared understanding;
- recommendations that help people navigate or act;
- structured support for collaboration and sense-making.

Match suggestions, memory pages, workflow actions, and alerts may all be useful, but they should be treated as supporting formats rather than the core goal.

## Standard lifecycle for creating a new agent

For v1, the lifecycle is manual by design.

### Proposed v1 lifecycle

1. Define the scope.
   The team decides whether the new agent is attached to an event, organization, workstream, project, collaboration, or conversation.
2. Choose or clone a base agent.
   A pre-existing guide pattern is copied or adapted rather than starting from zero.
3. Configure identity and role.
   The agent receives its name, purpose, personality or stance, and role definition.
4. Attach membership and boundaries.
   The relevant people, groups, and access scope are assigned.
5. Attach memory and skills.
   The agent receives the relevant shared skills, local context, and selected memory scope.
6. Decide whether to clone memory or only structure.
   Some agents may duplicate a full setup for a new group, while others may copy only skills, templates, or behavior without copying memory.
7. Launch and observe.
   The agent starts in a controlled mode and is reviewed in real usage.
8. Refine manually.
   Since v1 is manual, iteration happens through operator updates rather than self-provisioning.

This matches the current stated intent: manual configuration first, with better provisioning and templates designed later.

## Agent categories in the product model

### Event guide agents

These help participants and organizers navigate a coherence event. They should prioritize orientation, explanation, connection, and facilitator support.

### Organization guide agents

These help people understand the structure, memory, people, and current work of an organization. They should prioritize continuity, context, and stewardship across time.

### Workstream guide agents

These help teams within a bounded workstream maintain alignment, memory, and coordination. They should prioritize practical understanding and follow-through.

### Collaboration agents

These support shared spaces between organizations or teams, such as ARK. They should prioritize scoped collaboration and cross-context understanding without assuming a single organizational center.

### Conversation agents

These are bounded agents for individual coherence conversations. In v1 they should be treated as scoped child contexts rather than assumed to be fully independent top-level products.

## Decisions this system must support better than a normal RAG assistant

This system is meant to do more than retrieve relevant text.

It should be better than a normal RAG assistant at:

- understanding across many layers and viewpoints;
- holding context at the level of event, organization, workstream, and conversation;
- supporting dialogue and collaboration between agents where useful;
- preserving continuity across time instead of answering in isolated sessions;
- helping humans navigate living social context, not just documents.

## Autonomy limits for v1

The clearest hard constraint already stated is simple:

- the system should not spend money autonomously.

A practical first-pass operating rule for v1 is therefore:

- guide agents may answer, summarize, organize, and support understanding;
- guide agents may perform bounded background work where configured;
- guide agents should not initiate spending or financially consequential actions on their own.

Human-facing communication should also be treated as a configured capability, not a default property of every background agent.

## Role boundaries

### Assistant

A foreground agent that interacts directly with humans in a scoped context.

### Delegate

An agent that acts on behalf of another agent, team, or workflow within bounded permissions.

### Worker

A background agent that performs support tasks, processing, or synthesis without necessarily talking to humans directly.

### Institutional memory compiler

A background function or agent role that turns raw materials into structured memory, summaries, or reusable knowledge.

### Boundary rule

Some agents work in the foreground and some in the background. Only some agents should talk directly with humans. This boundary should be explicit in configuration.

## Boundary between project agent, conversation agent, and platform service

The current design direction implies three layers:

- project or scope agent: the primary guide for an event, organization, workstream, or collaboration;
- conversation agent: a bounded child context attached to a specific conversation or thread;
- platform service: shared capabilities that are not tied to one agent identity, such as configuration, provisioning, shared skills, or common memory infrastructure.

This boundary still needs formal templates and definition formats, but the design direction is already clear: not everything should be implemented as a standalone agent.

## Success criteria for the first release

The stated outcome is:

- it works for CoCo v1.0;
- it allows the team to create team support agents.

### Proposed first-release interpretation

The first release succeeds if:

- METIS can support a real CoCo v1.0 guide-agent use case;
- the team can create at least one additional team support agent without rebuilding the architecture;
- the created agents feel like instances of one framework, not one-off prototypes;
- operators can manually configure and maintain them with acceptable effort;
- the agents improve knowledge, understanding, and coordination in practice.

## Non-goals for v1

The current material implies several useful non-goals:

- fully automated agent self-provisioning;
- complete autonomy across all workflows;
- finalizing every agent type before the first deployment;
- solving all group-memory complexity before proving the guide-agent model;
- treating conversation agents as fully mature independent systems from day one.

## Expected output of this workstream

A one-page operating model should ultimately capture:

- who METIS serves;
- what a guide agent is;
- the main agent categories;
- the lifecycle for creating a new agent;
- the core jobs and outputs;
- the autonomy boundaries;
- the success criteria for v1.

## Open Questions

- Is METIS best described internally as an agent framework with memory features, or as a memory and journey platform with agent runtime features?
- What is the minimal guide-agent template that works across an event, an organization, and a workstream without becoming too generic?
- Should conversation agents be lightweight child contexts by default, or first-class independent agents from the start?
- Which guide behaviors are required in every guide agent, and which should remain optional modules?
- What exact operator workflow should replace the current manual setup once provisioning becomes more structured?
- What measurable indicators best represent `knowledge, understanding and wisdom` in the first release?
