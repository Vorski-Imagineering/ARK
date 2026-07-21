# ARC Community Agent capability audit

## Scope

This audit checks `proposal/hackathon-1/ARC Community Agent Proposal.md` against three requested capabilities: organisation-selected update inputs, personalised member updates, and self-accounting with a funding-response loop.

## Result

| Requested capability | Status | Evidence and boundary |
|---|---|---|
| Each organisation chooses how to provide public updates | Present | Organisations instruct the agent how to reach their public stream. V1 supports feeds, URLs, documents, and manual submissions, rather than mandating every integration. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#43-organisational-update-streams] |
| Each signed-up member receives updates based on interests and preferred frequency | Present, with delivery design deferred | The proposal covers interest-based updates, followed organisations, preferred frequency, and member control of update type/frequency. It does not yet define registration, consent, opt-out, or subscription storage. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#42-ongoing-member-activation] [see: proposal/hackathon-1/ARC Community Agent Proposal.md#45-personalised-updates] [see: proposal/hackathon-1/ARC Community Agent Proposal.md#17-open-questions] |
| The agent tracks token use and costs | Present | The proposal requires per-task, daily, and monthly cost records. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#115-cost-management] |
| The agent accounts for member contributions, detects low funds, and asks members to contribute | Absent | The proposal only asks participating organisations to help cover costs and leaves contribution level open. The adjacent technical specification gives billing and spend control to a human budget owner, not the agent. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#19-decision-requested] [see: proposal/hackathon-1/execution/05-technical-specification.md#human-and-service-roles] |

## Interpretation

The proposal already describes the first two loops: configurable public organisational inputs and lightweight personalised member distribution. It also includes operational cost telemetry.

It does not yet describe a funding loop. Cost measurement is not equivalent to financial accounting: no financial ledger, available-funds source, contribution allocation, low-balance threshold, notification policy, approval boundary, or contribution-request workflow is defined.

The adjacent specification makes this distinction sharper. It requires usage controls and caps, while reserving billing administration for a human budget owner. Therefore, the requested funding feature should be designed as an approved notification/escalation workflow, not as autonomous payment collection or billing control by the agent. [see: proposal/hackathon-1/execution/05-technical-specification.md#model-access] [see: proposal/hackathon-1/execution/05-technical-specification.md#human-and-service-roles]

## Smallest proposal addition needed

Add an explicit operating-funds section that defines:

1. A human-approved funding ledger containing available balance, committed contributions, received contributions, and attributed operating costs.
2. Per-run token/cost logging aggregated into current and forecast spend.
3. Low-funds and stop-spend thresholds, with the responsible human role and review cadence.
4. A member or organisation contribution request that is drafted or sent only under a defined approval/consent policy.
5. A clear statement that the agent cannot access payment instruments, change provider budgets, or make financial commitments.

[CONFIDENCE: high] These findings follow direct statements in the proposal and its adjacent technical specification.

## 2026-07-21 amendment — current status

This section supersedes the pre-amendment result above.

[CONTRADICTS: research/synthesis/arc-community-agent-capability-audit.md] The proposal has now been amended, so the earlier “absent” status for the funding loop no longer describes the current proposal.

All three requested capabilities are now explicit and included in the MVP:

1. Each organisation chooses its technically and legally accessible public update method, with a manual route available. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#43-organisational-update-streams]
2. The agent proactively contacts only registered and authorised users and follows their stated interests, requested update frequency, delivery permissions, and opt-out choices. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#42-ongoing-member-activation] [see: proposal/hackathon-1/ARC Community Agent Proposal.md#45-personalised-updates]
3. The agent records token and operating costs, maintains a human-reconciled funding ledger, calculates balance and runway, and sends an approved contribution request to eligible registered recipients when the low-funds threshold is crossed. It does not control payment instruments or billing limits. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#115-cost-management] [see: proposal/hackathon-1/ARC Community Agent Proposal.md#116-operating-funds-and-contribution-accounting]

[CONFIDENCE: high] The proposal now states the requested behaviours directly in its executive summary, functional sections, MVP, success criteria, open decisions, and one-page brief.

## 2026-07-21 document split — canonical locations

The combined proposal has been separated by concern:

- The current source of truth for what the agent is and does is `proposal/hackathon-1/arc-community-agent-vision.md`.
- The current source of truth for how the hackathon will build and test it is `proposal/hackathon-1/arc-community-agent-hackathon-proposal.md`.
- The former `proposal/hackathon-1/ARC Community Agent Proposal.md` path is retained as a compatibility index for prior links and citations.

The audited capabilities are defined in the vision and included as testable MVP requirements in the hackathon proposal. [CONFIDENCE: high]

## 2026-07-21 public personality and build-in-public extension

The agent is now explicitly defined as a public participant with a distinctive, versioned personality and a candid self-reporting feed. The canonical GitHub feed must explain its activity, learning, capability growth, successes, failures, corrections, aggregate operating position, and next steps. Approved social media versions link back to that record. The hackathon must demonstrate the personality, AI disclosure, substantive GitHub update, and shorter social post. [see: proposal/hackathon-1/arc-community-agent-vision.md#410-public-personality] [see: proposal/hackathon-1/arc-community-agent-hackathon-proposal.md#5-minimum-viable-prototype]

[CONFIDENCE: high] The requirement is present in the enduring vision, a dedicated public-observer journey, hackathon scope, MVP, roles, deliverables, success criteria, event decisions, and one-page brief.

## 2026-07-21 relationship stewardship extension

Relationship stewardship is now a core agent function. Phase 1 maintains the relationship between each member and ARC through consented context, relevant updates, two-way response, participation support, and useful follow-up. Phase 2 uses attributable organisational updates and consented member context to suggest possible alignments and purposeful conversations between members. Suggestions must explain their evidence, value, and uncertainty and require every proposed participant to opt in before an introduction. [see: proposal/hackathon-1/arc-community-agent-vision.md#411-relationship-stewardship-and-alignment]

The hackathon tests the Phase 1 loop and documents a safeguarded Phase 2 scenario; it does not attempt a comprehensive private CRM or production recommendation system. [see: proposal/hackathon-1/arc-community-agent-hackathon-proposal.md#5-minimum-viable-prototype]

[CONFIDENCE: high] The relationship model is represented in the core operating loop, functional specification, two user journeys, data boundary, runtime, governance principles, hackathon scope, MVP, demonstration, deliverables, success criteria, event questions, and one-page brief.

## 2026-07-21 two-function synthesis

The canonical framing now gives the agent exactly two high-level functions: **updates** and **relationship management**. Updates transform collected organisational information into shared and participant-specific intelligence. Relationship management connects onboarding, engagement, participant-to-ARC continuity, and relationships among participating people and organisations, with proactive alignment and conversation suggestions introduced in Phase 2. All other capabilities are enabling foundations for these two functions. [see: proposal/hackathon-1/arc-community-agent-vision.md#1-vision-and-purpose]
