# Hackathon 1 execution — working notes

## 2026-07-21 — Decomposition

### Source basis

- The planning guide requires minimum viable organisation and design, three to five organisations, explicit ownership, one preparation session, a short brief, readiness gates, and a compact route from interest to a build event. [see: proposal/hackathon-1/Hackathon Planning Guide.md#core-planning-principle]
- The proposal recommends two build days with preparation, but its prototype scope includes source collection, shared memory, question answering, a digest, Telegram, onboarding, public publishing, documentation, and cost tracking. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#10-minimum-viable-prototype] [see: proposal/hackathon-1/ARC Community Agent Proposal.md#12-hackathon-format]
- The proposal identifies unresolved pre-event decisions including project naming, initial users, participants, delivery channel, demonstration journey, ownership, budget, repository, and licensing. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#17-open-questions]

No separate hackathon execution package was found in prior research. Adjacent agent and memory research exists, but the proposal already contains enough concept-level technical direction for this planning task.

### Planning sub-questions

1. What is the single end-to-end outcome that can credibly be demonstrated after two days?
2. What must be prepared before the event so builders do not spend Day 1 chasing access, content, or decisions?
3. What is the minimum explicit commitment required from each participating organisation?
4. Which roles must have named owners, and which roles can one person combine?
5. What small set of files will turn the proposal into an executable event without creating administrative overhead?
6. Which files are required before invitations go out, before the event is confirmed, before Day 1, and only after the event?
7. What should the invitation promise, and what exact action should it request?
8. What belongs in a concept-level technical specification versus a detailed engineering backlog that should wait for the participants?
9. How should the two days alternate between alignment, building, testing with organisational representatives, integration, and demonstration?
10. What readiness gates prevent a polite but unprepared group from consuming two days without producing a usable result?
11. What decisions can be made by the event lead to avoid consensus overhead, and which require participating organisations?
12. What evidence supports a two-to-four-week pilot rather than immediate expansion?

### Working assumptions

- [ASSUMPTION: The two proposal files are public repo material and may be cited and adapted within this public repository.]
- [ASSUMPTION: The event will involve three to five organisations and roughly eight to twelve active participants.]
- [ASSUMPTION: The event may be remote, in person, or hybrid; the operating plan should work in any format, with one shared live room as the default collaboration surface.]
- [ASSUMPTION: All content supplied to the prototype will be intentionally public, redistributable, and free of credentials or private participant data.]
- [ASSUMPTION: A technical lead can prepare a running skeleton and one sample source before Day 1. Without this, the event should be postponed.]
- [ASSUMPTION: The working product name remains “ARC Agent” until the organiser resolves the ARC/ARK naming question.]

### Scope pressure identified

The proposal’s full “must have” list is not a minimum two-day scope. It mixes the proof of value with distribution, onboarding, automation, extensibility, cost reporting, and public storytelling. The event should instead protect one vertical slice:

Public source packs from at least three organisations  
→ content is loaded into one shared knowledge surface  
→ a participant asks questions and receives sourced answers  
→ the system creates one cross-organisation digest  
→ the digest is delivered through one accessible channel  
→ representatives check accuracy and usefulness.

Scheduled ingestion can be demonstrated with one source and simulated or manually triggered for the others. Telegram should be used only if its bot and group access are ready before the event; otherwise a simple web or command interface plus a pasted/published digest proves the same loop.

### Minimal document architecture

Use one folder for event execution. Prefer a small set of documents with templates embedded rather than many narrow files.

#### Core files

1. `00-start-here.md` — one-page index, current state, owners, links, and next decision.
2. `01-participant-invitation.md` — invitation, commitment requested, response deadline, and confirmation reply.
3. `02-participation-and-source-pack.md` — organisation profile, one desired outcome, public sources, licences/permissions confirmation, nominees, capacity, and readiness checklist.
4. `03-hackathon-brief.md` — challenge, single primary journey, in/out of scope, success test, participating organisations, and post-event steward.
5. `04-run-of-show.md` — pre-event work, two-day schedule, checkpoints, facilitation rules, demo, and retrospective.
6. `05-technical-specification.md` — acceptance tests, information inputs/outputs, source provenance, prepared environment, interfaces, constraints, fallback path, and decisions to make; no framework-heavy architecture.
7. `06-roles-and-readiness.md` — combined owner table, participant roster by role, readiness gates, and contact/coordination protocol. Public roles only; do not publish private participant details.
8. `07-demo-test-and-pilot.md` — demo script, representative feedback rubric, known limitations, pilot decision, and two-to-four-week steward checklist.

#### Optional files, created only if needed

- `decision-log.md` if decisions cannot be kept in `00-start-here.md`.
- `budget-and-logistics.md` only if venue, travel, catering, or shared costs require coordination.
- `communications-kit.md` only if public build-in-public communications need more than the final event note.

Avoid separate files for agendas, surveys, FAQs, backlogs, team charters, risk registers, or retrospectives. The core files already have a home for each of these concerns.

### Ownership model

The minimum named owners are:

- Event lead and decision owner: invitations, date, format, readiness, facilitation, and final calls.
- Product lead: primary journey, scope, acceptance criteria, representative testing, and demonstration story.
- Technical lead: feasibility, prepared environment, integration, fallback plan, and technical continuation.
- Post-event steward: two-to-four-week pilot operations and continuation decision.
- One representative per organisation: source pack, accuracy check, and usefulness judgment.

The event lead may also be product lead. The technical lead may also be post-event steward. Documentation rotates among participants or is owned by the product lead. A separate communications, onboarding, or data lead is optional at this scale.

### Decision rights

- Event lead decides logistics, schedule, facilitation method, and whether readiness is sufficient.
- Product lead decides scope during the event, after listening to representatives and the technical lead.
- Technical lead decides implementation approach and whether a technical request can fit the timebox.
- Organisation representatives decide whether their organisation is accurately represented and whether the result is useful.
- Named post-event steward and participating organisations decide whether to run the pilot.

### Key open decisions and when they are required

- Working product name: before the invitation is final.
- Event lead: before invitations are sent.
- Target date and event format: proposed in the invitation; confirmed after sufficient commitment.
- Initial user and primary journey: drafted before invitation, locked in the preparation session.
- Delivery channel: locked seven days before the event, based on readiness.
- Technical lead and post-event steward: before confirming the event.
- Shared repository and public-content licence: before source packs are ingested.
- Exact technical stack: selected by the technical lead before the event, not decided by a broad workshop.

No key unanswered question prevents production of an adaptable execution plan. The open items above are inputs to explicit readiness gates rather than prerequisites to writing the plan.

### Reflection

[OPEN QUESTION: Which working product name should appear in participant-facing material: ARC Agent, ARK Agent, or another name?]

[OPEN QUESTION: Is a Telegram demonstration essential to stakeholder confidence, or is it only one possible delivery channel?]

[OPEN QUESTION: Is there already a willing event lead, technical lead, and post-event steward?]

[OPEN QUESTION: Are participating organisations already able to license or authorise reuse of their selected public sources, or will the event use links and summaries under a narrower permission model?]

## 2026-07-21 — Remote-only execution refinement

The event format is now fixed as remote-only. Preparation will use a small sequence of pre-events so that the build days begin with shared context, a locked plan, and working access.

[CONTRADICTS: research/synthesis/hackathon-1-execution-plan.md] The earlier synthesis was deliberately format-neutral and proposed one whole-group preparation session. The user has now fixed the event as remote-only and requested multiple preparation events.

### Minimal pre-event sequence

1. **Orientation and commitment — 60 minutes, approximately three weeks before.** All confirmed representatives and builders hear the same proposition, meet the group, understand the end-to-end proof, and confirm responsibilities.
2. **Design lock — 90 minutes, approximately two weeks before.** All confirmed participants review source packs, select the primary user journey and representative questions, lock scope and the delivery channel, and approve the working brief.
3. **Technical readiness and remote rehearsal — 45 minutes, 48 hours before.** The event, product, and technical leads, builders, and post-event steward verify repository access, runtime, video room, coordination channel, sample source, fallback path, and demo outline. Organisation representatives attend only if needed.

An optional source-pack clinic may be offered as office hours, but it is not another mandatory whole-group meeting. This keeps required shared preparation to 150 minutes for organisation representatives and adds only 45 minutes for the core delivery team.

### Remote design implications

- Use one persistent video room, one coordination chat, one repository, and one shared working document or board.
- Publish the event timezone and daily live hours in every invitation and calendar entry.
- Use a main room for integration and short breakout rooms only for timeboxed tasks.
- Record decisions in the repository rather than relying on meeting recall.
- Confirm access and fallback communication before the event.
- Do not store private contact details, access credentials, or unapproved participant identities in the public repository.

[OPEN QUESTION: Which event timezone and daily live window allow the confirmed participants to attend both days?]

[OPEN QUESTION: Which video, chat, repository, and shared-document tools will form the minimal remote workspace?]

## 2026-07-21 — Two-week, agent-first refinement

The event now uses a two-week ramp-up. Every scheduled preparation session must be at least 60 minutes. The technical work starts immediately: a small agent should be running within 48 hours over the public proposal, execution documents, and one approved sample source.

[CONTRADICTS: research/synthesis/hackathon-1-execution-plan.md] The earlier four-week runway and later remote-only addendum are superseded. The previous 45-minute technical readiness session is also superseded by a 60-minute session.

### Revised preparation sequence

1. **Starter agent launch — within 48 hours.** The technical lead publishes a simple working interface with retrieval over public planning material and one approved public sample source.
2. **Orientation and commitment — 60 minutes, T−11 to T−10.** Participants use the starter agent and confirm contributions and source-pack work.
3. **Source submission and early use — T−9 to T−7.** Approved organisation sources are loaded into the running agent and representatives test initial answers.
4. **Source review and design lock — 90 minutes, T−7 to T−6.** Participants make scope and demo decisions from observed agent behaviour.
5. **Agent-assisted iteration — T−5 to T−3.** The same agent helps check sources, draft the brief, maintain actions, test retrieval, and document decisions.
6. **Technical readiness and remote rehearsal — 60 minutes, T−2.** The core team runs the complete path and tests fallbacks.
7. **Two build days — T and T+1.** Improve accuracy and usefulness, deliver the digest, demonstrate, and decide on a pilot.

### Agent role during preparation

The agent may answer event questions from public documents, check source-pack completeness and URL access, draft source-linked test questions, prepare draft briefs and progress summaries, propose actions, support retrieval testing, and help prepare the final demonstration.

Humans remain responsible for participation commitments, source permission, organisational accuracy, public release approval, dates, ownership, scope, and readiness. The agent must not receive private contact details, access credentials, private meeting transcripts, or non-public organisational material.

[ASSUMPTION: A technical lead can launch a simple source-linked agent over existing public documents within 48 hours. If this is not possible, the two-week schedule should narrow the initial interface rather than delay all participant activity.]

[OPEN QUESTION: Which approved public source will be the starter agent’s first non-planning source?]

[OPEN QUESTION: Through which simple interface will confirmed participants use the starter agent during the two-week ramp-up?]

## 2026-07-21 — Two-hour pre-ramp agent bootstrap

The basic agent must now be running before the two-week participant ramp and before invitations are sent. The technical lead receives one two-hour block to install and configure a primary OpenClaw or Hermes runtime over public planning material and one approved public sample source.

[CONTRADICTS: research/synthesis/hackathon-1-execution-plan.md] The earlier 48-hour starter-agent target is superseded by a two-hour pre-ramp bootstrap.

Use one primary runtime. Hermes is the default when one evolving preparation agent is the immediate need; OpenClaw is the default when immediate multi-channel or Telegram gateway routing is the primary need. Both may be installed only by parallel operators and only if the second installation cannot delay the primary smoke test. This decision follows the repository’s prior analysis while keeping runtime state separate from canonical public source material. [see: research/The Coherence Company/CoCo-OpenClaw-vs-Hermes.md#recommended-architecture-for-coco]

The two-hour definition of working is: predictable start and restart; one usable interface; correct answers to three event questions from repository documents with paths; one summary of an approved public sample source; a draft action list; inspectable safety instructions; no credentials or private data in Git; and one operator able to control the process.

[OPEN QUESTION: Who owns the two-hour bootstrap and which already-provisioned machine or server will be used?]

[OPEN QUESTION: Is the primary immediate requirement an evolving preparation agent, favouring Hermes, or Telegram/multi-channel routing, favouring OpenClaw?]
