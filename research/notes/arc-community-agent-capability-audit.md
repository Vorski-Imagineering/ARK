# ARC Community Agent capability audit — working notes

## 2026-07-21 — decomposition

Purpose: audit `proposal/hackathon-1/ARC Community Agent Proposal.md` against three requested capabilities without inferring requirements that the proposal does not state.

1. Does the proposal let each participating organisation choose how it supplies public updates, including a manual route where integration is unavailable?
2. Does it specify delivery of updates to signed-up/registered users based on their interests and their chosen update frequency, rather than merely describing generic digests?
3. Does it specify autonomous operational accounting: token usage, costs, member contributions, a low-funds threshold, and a request to members for further contributions?

Audit method:

- Treat explicit proposal language as primary evidence.
- Separate present capability, partial capability, and absent capability.
- Check the adjacent technical specification only to identify whether it resolves a proposal gap; it does not change the proposal's scope.

[QUESTION TO VERIFY: Does the implementation specification include a member-funding ledger or low-balance contribution-request workflow that the proposal does not describe?]

## 2026-07-21 — evidence and findings

### 1. Organisation-selected update routes — present

- The proposal says that each organisation instructs the agent how to access its public update stream and lists websites, APIs, feeds, repositories, social channels, public documents, and an organisation-specific agent interface. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#43-organisational-update-streams]
- Its V1 explicitly permits a small list of public URLs, selected public documents, and a manual update submission form or structured file. The source-collection design separately includes manual organisational updates. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#43-organisational-update-streams] [see: proposal/hackathon-1/ARC Community Agent Proposal.md#111-source-collection]
- The proposal deliberately avoids requiring full integration with every platform. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#8-proposed-hackathon-scope]

Conclusion: the requested choice of organisation update mechanism is explicit, provided that the material is public.

### 2. Interest- and frequency-based updates to signed-up members — present, with implementation detail deferred

- The agent maintains periodic contact with active, signed-up members, including updates related to a person’s interests. Members control the frequency and type of updates they receive. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#42-ongoing-member-activation]
- Personalisation includes followed organisations, themes, and preferred update frequency; V1 may start with member-selected topics or organisations. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#45-personalised-updates]
- Onboarding asks about themes, organisations, and useful update kinds, and the member journey offers a preferred update rhythm. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#41-new-member-onboarding] [see: proposal/hackathon-1/ARC Community Agent Proposal.md#journey-1-onboarding-a-new-member]
- The data model for storing individual interests and update preferences is explicitly deferred to the pilot. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#17-open-questions]

Conclusion: the intended behaviour is explicit. The proposal uses “active, signed-up members,” not a formal registration or consent model, and does not define a subscription schema, consent record, delivery failure handling, or opt-out flow.

### 3. Token/cost accounting and contribution request — partial

- The proposal requires recording the model used, token use, cost per task, daily/monthly cost, processed updates, and member interactions. It also identifies cost measurement as a technical success criterion and includes costs and usage statistics in public development reporting. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#115-cost-management] [see: proposal/hackathon-1/ARC Community Agent Proposal.md#15-success-criteria] [see: proposal/hackathon-1/ARC Community Agent Proposal.md#49-building-the-agent-in-public]
- It asks organisations to help cover operating costs according to capacity and agreement, while leaving the level of operating contribution as a pilot question. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#19-decision-requested] [see: proposal/hackathon-1/ARC Community Agent Proposal.md#17-open-questions]
- The adjacent technical specification strengthens operational measurement with per-generation token/cost records, provider spend limits, warnings, and a hard stop/manual approval. It assigns billing and usage review to a human budget owner and expressly denies the agent service identity billing authority. [see: proposal/hackathon-1/execution/05-technical-specification.md#11-cost-and-operational-controls] [see: proposal/hackathon-1/execution/05-technical-specification.md#model-access] [see: proposal/hackathon-1/execution/05-technical-specification.md#human-and-service-roles]

Conclusion: token and cost accounting are present. Accounting for individual member contributions, a fund/balance calculation, a low-funds threshold, and an agent-initiated request for contributions are absent. The technical specification instead makes spending limits and billing human-owned.

Resolution: no member-funding ledger or low-balance contribution-request workflow was found in the proposal or adjacent technical specification.

## 2026-07-21 — proposal amendment

The proposal was amended after the audit at the user's request.

- Organisation-selected update methods are now stated as a requirement, including automated, agent-to-agent, document-based, and manual routes. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#43-organisational-update-streams]
- Proactive communication is now limited to registered, authorised users, with explicit interests, requested update frequency, delivery permission, and opt-out controls. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#42-ongoing-member-activation] [see: proposal/hackathon-1/ARC Community Agent Proposal.md#45-personalised-updates]
- Token/cost tracking, operating-fund accounting, confirmed member and organisation contributions, runway forecasting, low-funds and stop-spend thresholds, and an approved contribution-request workflow are now explicit. Billing authority and payment instruments remain human-controlled. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#115-cost-management] [see: proposal/hackathon-1/ARC Community Agent Proposal.md#116-operating-funds-and-contribution-accounting]
- These capabilities were moved into the MVP must-have list and technical success criteria. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#10-minimum-viable-prototype] [see: proposal/hackathon-1/ARC Community Agent Proposal.md#15-success-criteria]

[CONTRADICTS: research/synthesis/arc-community-agent-capability-audit.md] The earlier finding that the funding loop was absent was accurate before this amendment and is now superseded.

## 2026-07-21 — document separation

The former combined proposal mixed enduring product requirements with a temporary event plan. It was separated into:

- `proposal/hackathon-1/arc-community-agent-vision.md` — canonical agent purpose, capabilities, user journeys, technical and funding model, governance, and longer-term questions.
- `proposal/hackathon-1/arc-community-agent-hackathon-proposal.md` — canonical hackathon case, scope, MVP, format, roles, deliverables, success criteria, event questions, and decision request.
- `proposal/hackathon-1/ARC Community Agent Proposal.md` — compatibility index preserving the former headings and redirecting readers to the two canonical documents.

The three audited capabilities remain explicit in both the enduring vision and the hackathon MVP. Existing internal references to former section anchors remain resolvable through the compatibility index.

## 2026-07-21 — public personality and self-reporting feed

The agent vision and hackathon proposal now make the agent itself a public, inspectable participant:

- A versioned public personality defines the agent's name, purpose, values, voice, uncertainty language, boundaries, and change process while requiring clear disclosure that it is AI. [see: proposal/hackathon-1/arc-community-agent-vision.md#410-public-personality]
- A candid first-person feed reports what the agent is doing and learning, how its capabilities are changing, evidence of success, failures and limitations, corrections, aggregate costs, and next experiments. [see: proposal/hackathon-1/arc-community-agent-vision.md#49-building-the-agent-in-public]
- GitHub is the canonical auditable record; shorter approved social media posts link back to it. [see: proposal/hackathon-1/arc-community-agent-vision.md#48-public-publishing]
- The hackathon MVP requires a personality specification, a substantive GitHub self-update, and a shorter human-reviewed social post. [see: proposal/hackathon-1/arc-community-agent-hackathon-proposal.md#5-minimum-viable-prototype]

The personality is explicitly prevented from obscuring uncertainty, impersonating a person or organisation, or replacing source attribution.

## 2026-07-21 — relationship stewardship and Phase 2 alignment

The agent vision now defines relationship stewardship as a core function across two relationship types and two phases:

- Member-to-community: consented continuity from onboarding through relevant updates, response, participation, contribution, and follow-up.
- Member-to-member: awareness of relevant work and, in Phase 2, evidence-based suggestions for possible alignment and purposeful conversations.
- Phase 1 establishes the member relationship loop without constructing a comprehensive private CRM.
- Phase 2 uses public updates and consented member context to explain possible alignment, uncertainty, and a proposed conversation purpose; every participant must opt in before an introduction or non-public context is shared. [see: proposal/hackathon-1/arc-community-agent-vision.md#411-relationship-stewardship-and-alignment]

The design separates public organisational knowledge from access-controlled member relationship state, gives members inspection/correction/pause/removal rights, and prohibits hidden ranking, social scoring, or pressure to accept introductions. [see: proposal/hackathon-1/arc-community-agent-vision.md#79-relationship-consent-and-member-agency]

## 2026-07-21 — two-function model

The agent's high-level purpose is now explicitly reduced to two functions:

1. **Updates:** collect attributable organisational information and synthesise it into general community updates and participant-specific updates.
2. **Relationship management:** onboard and engage participants, maintain participant-to-ARC relationships, and support relationships among participating people and organisations; Phase 2 adds evidence-based alignment and conversation suggestions.

Personality, public self-reporting, source memory, consent, delivery, and cost/funding accounting are classified as shared supporting capabilities rather than additional primary functions. [see: proposal/hackathon-1/arc-community-agent-vision.md#1-vision-and-purpose]
