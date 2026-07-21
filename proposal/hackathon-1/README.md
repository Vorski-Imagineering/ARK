# ARC Agent remote hackathon

This folder contains the ARC Community Agent vision, the hackathon proposal, and the working execution package for a remote-only, two-day build event.

The aim is deliberately small: bring several organisations together, place approved public information into one shared agent, test whether it can answer useful cross-organisation questions with visible sources, produce one concise digest, and decide whether a short pilot is worthwhile.

This is a prepared build event, not a cold start. A basic agent must already be running before invitations are sent. Participant preparation then aligns the sources, use case, test questions, delivery route, access boundaries, and demonstration so the two event days can focus on improving and proving the information loop.

## Start here

1. Read [ARC Community Agent: Vision and Functionality](arc-community-agent-vision.md) for the enduring product purpose, users, capabilities, operating model, and governance boundaries.
2. Read the [ARC Community Agent Hackathon Proposal](arc-community-agent-hackathon-proposal.md) for the event challenge, scope, MVP, roles, evidence, and decision process.
3. Read the [Hackathon Planning Guide](<Hackathon Planning Guide.md>) for the broader planning method and participant preparation journey.
4. Use [execution/00-start-here.md](execution/00-start-here.md) as the operational index. It contains the preparation sequence, readiness gates, mandatory owners, and current next actions.
5. Use [execution/05-technical-specification.md](execution/05-technical-specification.md) before creating infrastructure or granting access. It defines the two-hour agent bootstrap, technical baseline, access domains, role boundaries, backup and restore plan, acceptance tests, and budget.

## Documents in this folder

| Document | Purpose | Current use |
|---|---|---|
| [ARC Community Agent: Vision and Functionality](arc-community-agent-vision.md) | Defines the enduring agent purpose, functionality, user journeys, technical operating model, and governance | Canonical product vision |
| [ARC Community Agent Hackathon Proposal](arc-community-agent-hackathon-proposal.md) | Defines the event proposition, scope, MVP, format, roles, deliverables, and decisions | Canonical hackathon proposal |
| [Combined proposal compatibility index](<ARC Community Agent Proposal.md>) | Redirects links into the former combined document | Legacy-link compatibility only |
| [Hackathon Planning Guide](<Hackathon Planning Guide.md>) | Describes how to organise participation and prepare a useful collaborative event | Planning reference |
| [execution/00-start-here.md](execution/00-start-here.md) | Connects the proposal to an executable remote event | Primary organiser checklist and status page |
| [execution/01-participant-invitation.md](execution/01-participant-invitation.md) | Provides the invitation, reply request, follow-up, and confirmation language | Complete dates and sender details, then send privately |
| [execution/02-participation-and-source-pack.md](execution/02-participation-and-source-pack.md) | Collects each organisation's participation commitment and approved public sources | Complete one pack per organisation |
| [execution/05-technical-specification.md](execution/05-technical-specification.md) | Defines the runtime bootstrap, minimal architecture, access control, data boundaries, recovery, infrastructure, acceptance tests, and budget | Technical preparation and readiness authority |

## Documents to create after participants commit

Do not create these prematurely. They should reflect actual participants, sources, decisions, and availability rather than guesses.

| Planned document | Create when | Purpose |
|---|---|---|
| `execution/03-hackathon-brief.md` | After commitments and source review | Lock the primary user, journey, three test questions, digest, scope, and final demonstration |
| `execution/04-run-of-show.md` | After the design-lock session | Define the two-day remote timetable, checkpoints, decision moments, and fallbacks |
| `execution/06-roles-and-readiness.md` | Once actual roles are accepted | Track public role ownership, attendance coverage, access readiness, and gate status |
| `execution/07-demo-test-and-pilot.md` | Begin before Day 1; complete on Day 2 | Hold the demo script, representative feedback, limitations, pilot decision, and handoff |

Private participant identities, contact details, meeting links, account identifiers, credentials, recovery material, and actual identity-to-access mappings must remain outside this public repository.

## Minimal operating model

- One primary agent runtime: OpenClaw or Hermes.
- One Git-backed canonical collection of approved public sources, prompts, code, and reviewed outputs.
- One simple participant interface and one fallback demonstration route.
- One disposable, rebuildable retrieval index; query access is read-only and ingestion promotes a tested replacement atomically.
- Human review before publication or any change to scope, source approval, access policy, or agent authority.
- Separate infrastructure, recovery, budget, builder, agent, ingest, deployment, and backup responsibilities.
- Hourly logical backups during the event, daily backups during preparation, an off-host retained copy, and a tested restore path.
- Expected direct spend of approximately EUR 16–27 equivalent, with an authorised EUR 50 preparation-and-event ceiling.

## Next steps

1. Replace the `[TO SET]` fields in the execution documents: dates, timezone, daily live window, response deadline, product name, and private reply route.
2. Name the event lead, product lead, technical lead, infrastructure owner, distinct recovery custodian, budget owner, and post-event steward.
3. Choose one primary runtime and one approved public sample source.
4. Complete the two-hour bootstrap in [execution/05-technical-specification.md](execution/05-technical-specification.md). Confirm that the agent works, follows the public-data boundary, and restarts from written instructions.
5. Select the minimal remote workspace: video room and fallback, coordination chat, repository, shared working surface, participant-facing agent route, and digest-delivery route.
6. Create the private access register. Map every human and service identity to the documented access domains, grant only necessary access, set expiry dates, and keep all private values outside this repository.
7. Enable protected repository rules, individual server access, server deletion protection, bounded service identities, spend limits, provider backups, and the off-host logical-backup path.
8. Send invitations to three to five organisations only after the bootstrap smoke test passes.
9. Collect one participation and source pack per organisation. Review public reuse permission, provenance, accessibility, and representative availability before ingestion.
10. Run the three preparation events described in [execution/00-start-here.md](execution/00-start-here.md): orientation and commitment, source review and design lock, then technical readiness and remote rehearsal.
11. Before Day 1, prove the full vertical slice and rehearse denied access, agent pause, credential revocation, deployment rollback, backup verification, and an isolated restore within 60 minutes.
12. Run the two build days around the minimum demonstration. End Day 2 with a documented decision to pilot, revise, or stop, followed by access expiry and recovery handoff.

## Definition of ready

The hackathon is ready to start when at least three organisations have approved source packs and representatives; all essential roles are owned; every builder can use the prepared environment; the complete source-to-answer-to-digest path works; source links and insufficient-evidence behaviour pass; access boundaries and deletion protections are tested; a current off-host backup is verified; an isolated restore succeeds within 60 minutes; the fallback demonstration works; and the event lead records `proceed` or `proceed with narrowed scope`.

If a readiness requirement fails, narrow or postpone. Do not spend Day 1 repairing basic access, infrastructure, or recovery setup.
