# ARC Agent remote hackathon — start here

**Status:** Draft for organiser completion  
**Format:** Remote only; two consecutive build days  
**Pre-ramp bootstrap:** Working agent in one two-hour setup block before invitations  
**Ramp-up:** Two weeks from organiser start to Hackathon Day 1  
**Working product name:** ARC Agent  
**Event timezone:** `[TO SET]`  
**Build dates:** `[TO SET: DAY 1]` and `[TO SET: DAY 2]`  
**Daily live window:** `[TO SET: START–END, INCLUDING TIMEZONE]`  
**Invitation response deadline:** `[TO SET]`

## Purpose

This directory turns the ARC Agent proposal into a small, executable remote event.

The hackathon will test one proposition: can public information from several participating organisations be made jointly useful through sourced questions and answers and one cross-organisation digest?

The technical work starts before the participant ramp-up. In one two-hour setup block, the technical lead should install and configure a primary agent runtime—OpenClaw or Hermes—over the public proposal and execution documents plus one approved sample source. The agent must pass the bootstrap smoke test before invitations are sent. Participants then use and improve that same agent throughout preparation and the two build days.

The hackathon is therefore not a cold start. The two build days extend an already-running agent until it proves one useful information loop and generates enough evidence for a short pilot. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#10-minimum-viable-prototype]

## Agent-first approach

The first version may be simple: a local or restricted chat or command interface, access to public documents, visible source references, and a manually triggered summary. Reliability and a short path to use matter more than framework sophistication.

Use one primary runtime. Install both OpenClaw and Hermes only when two operators can work in parallel and the second installation does not delay the primary smoke test. The event is not a framework comparison unless participants explicitly make that a secondary experiment after the core agent works.

### The starter agent helps with the preparation itself

Once running, use the agent to:

- Answer participant questions from the public proposal and execution documents.
- Explain the event outcome, schedule, roles, and current scope.
- Check public source packs for missing fields, inaccessible URLs, and unclear permission statements.
- Draft representative test questions from approved public sources.
- Draft the hackathon brief and update it from approved decisions.
- Produce public, source-linked summaries of preparation progress.
- Maintain a proposed action list and surface unresolved readiness items.
- Help builders inspect sources, test retrieval, document decisions, and prepare the demonstration.

### Human decisions remain human

The agent may propose and draft, but it may not:

- Commit an organisation or person to participate.
- Approve source permissions or licences.
- Decide whether an organisation is represented accurately.
- Publish externally without the designated human review.
- Store private contact details, private meeting transcripts, access links, credentials, or non-public organisational information.
- Change scope, dates, owners, or readiness status without approval from the responsible human role.

Record agent-generated proposals as drafts until the relevant owner approves them.

## Minimum demonstration

By the final demonstration:

1. At least three participating organisations have material in one shared knowledge surface.
2. A participant can ask representative questions across that material.
3. Answers point to original public sources and distinguish source material from generated synthesis.
4. The prototype creates one concise cross-organisation digest.
5. The digest reaches participants through one accessible delivery channel.
6. Organisation representatives check material concerning their organisations for accuracy and usefulness.
7. The group decides whether to run a two-to-four-week pilot, revise the concept, or stop and document the learning.

Manual ingestion, triggering, review, or publishing is acceptable if the manual step is declared. Telegram is the preferred delivery channel only if access is working before the event; it is not allowed to block the core demonstration.

## Core execution files

| File | Purpose | Status |
|---|---|---|
| `00-start-here.md` | Current state, preparation cadence, gates, owners, and next actions | Created; organiser fields remain |
| `01-participant-invitation.md` | Invitation, participation offer, reply request, follow-up, and confirmation | Created; dates and sender remain |
| `02-participation-and-source-pack.md` | Commitment and public-information template for each organisation | Created; complete one per organisation |
| `03-hackathon-brief.md` | Locked challenge, primary journey, scope, demonstration, and success test | Create after commitments; approve at Design Lock |
| `04-run-of-show.md` | Remote facilitation plan, two-day timetable, checkpoints, and fallback rules | Create after Design Lock |
| `05-technical-specification.md` | Two-hour runtime bootstrap, inputs, provenance, prepared environment, fallbacks, acceptance tests, and budget | Created; choose the primary runtime and operator before outreach |
| `06-roles-and-readiness.md` | Public role ownership, attendance coverage, access checks, and gate status | Create after commitments |
| `07-demo-test-and-pilot.md` | Demo script, representative feedback, limitations, pilot decision, and handoff | Begin before Day 1; complete on Day 2 |

Do not add separate planning files unless a real coordination problem has no home above.

## Remote preparation sequence

Preparation is deliberately short. Organisation representatives have 150 minutes of required shared preparation. The core delivery team has one additional 60-minute readiness check. Every scheduled preparation session is at least 60 minutes.

### Pre-event 1 — Orientation and commitment

**When:** Approximately 10–12 days before the hackathon  
**Duration:** 60 minutes  
**Required:** Event lead, product lead, technical lead, post-event steward, confirmed organisation representatives, confirmed builders  
**Working title:** “Meet the working agent and agree what we are proving”

**Purpose**

- Let everyone use or observe the starter agent rather than discuss an abstract proposal.
- Give everyone the same concise account of the problem and proposed experiment.
- Introduce participants by role and contribution.
- Make the participation commitment and two-day constraint explicit.
- Walk through the source-pack requirement.
- Surface blockers early without redesigning the full product.

**Agenda**

| Time | Activity | Output |
|---|---|---|
| 0:00–0:10 | Welcome, purpose, and remote working norms | Shared event frame |
| 0:10–0:25 | Use the starter agent: ask about the event and inspect one sample source | Shared experience of the starting point |
| 0:25–0:40 | Organisation introductions: desired value, offered source, participant role | Concise contribution map |
| 0:40–0:48 | Minimum scope and what is deferred | No expectation of a finished platform |
| 0:48–0:56 | Source-pack walkthrough and agent-assisted completion route | Clear preparation work |
| 0:56–1:00 | Decisions, blockers, and next event | Recorded actions and owners |

**Exit test:** Every organisation knows what it must submit, every participant understands the proof, and every blocker has one owner and date.

### Pre-event 2 — Source review and design lock

**When:** Approximately 6–8 days before the hackathon; after source packs are submitted and loaded into the agent  
**Duration:** 90 minutes  
**Required:** The same participants as Pre-event 1  
**Working title:** “Lock the two-day build”

**Purpose**

- Use the working agent over the submitted public sources rather than discussing hypothetical integrations.
- Select one primary user and one primary journey.
- Agree three representative questions and the digest audience.
- Decide the single delivery channel and its fallback.
- Lock in-scope work, manual seams, and deferred work.
- Approve the demonstration and assign preparation owners.

**Agenda**

| Time | Activity | Output |
|---|---|---|
| 0:00–0:10 | Reconfirm the decision to be made | Focus on a buildable proof |
| 0:10–0:30 | Use the agent across submitted sources and inspect failures | Included organisations, usable sources, and concrete gaps |
| 0:30–0:45 | Select primary user, journey, and test questions from observed behaviour | One journey and three questions |
| 0:45–1:00 | Agree digest purpose and delivery channel | One output and one route to users |
| 1:00–1:15 | Lock scope, fallbacks, and acceptance tests | Two-day boundary |
| 1:15–1:25 | Confirm roles and Day 1 preparation | Named owners |
| 1:25–1:30 | Approval and next actions | Hackathon brief ready for final edit |

**Exit test:** The product lead can describe the complete final demo in under two minutes, and the technical lead confirms that the path is feasible with the prepared sources.

### Pre-event 3 — Technical readiness and remote rehearsal

**When:** 48 hours before Day 1  
**Duration:** 60 minutes  
**Required:** Event lead, product lead, technical lead, post-event steward, and builders  
**Optional:** Organisation representatives, unless a source or accuracy issue requires them  
**Working title:** “Can we start building immediately?”

**Checks**

- Main video room and fallback meeting link open correctly.
- Coordination chat and shared working document are accessible.
- Repository access and development instructions work for every builder.
- The private access register identifies every human and service identity, its owner, access domains, privilege level, expiry, and recovery contact.
- Builder, operator, infrastructure-owner, recovery-custodian, and agent-service boundaries pass one allowed-action and one denied-action test each.
- Repository branch protection and server deletion protection are enabled; routine work does not use shared root access.
- The running agent and submitted sources complete the basic path.
- The agent cannot write canonical source material, administer the datastore, invoke unrestricted shell access, delete backups, or grant itself additional tools.
- The agent can help participants find the current brief, decisions, actions, and known limitations.
- Credentials are supplied securely and are not stored in the public repository.
- Organisation source packs and fallback snapshots are available.
- A current logical backup exists off-host, its checksum has been verified, and an isolated restore has completed within the 60-minute recovery target.
- The agent kill switch, access-revocation route, and last-known-good deployment rollback have been rehearsed.
- Delivery channel works or the fallback is selected.
- Day 1 opening, checkpoints, and final demo outline are understood.

**Agenda:** 15 minutes for access and runtime checks; 15 minutes for a complete agent-assisted demo rehearsal; 15 minutes for backup restore, rollback, and kill-switch rehearsal; 10 minutes for fallback testing; 5 minutes for the `proceed`, `narrow`, or `postpone` decision.

**Exit test:** The event lead records `proceed`, `narrow`, or `postpone`. Day 1 does not begin with unresolved platform setup.

### Optional office hours

Offer one 60-minute drop-in source-pack clinic between Pre-events 1 and 2 only if organisations request help. Participants may join only for the time they need. The agent should perform the first completeness check so the clinic focuses on unresolved questions rather than form filling.

## Two-week ramp-up

The schedule below assumes Hackathon Day 1 is `T`. The two-hour bootstrap happens before the 14-day participant countdown. Move individual days if needed, but preserve the order and deadlines.

| Timing | Action | Required output |
|---|---|---|
| Before T−14 | Name the technical lead and complete the two-hour bootstrap in `05-technical-specification.md` | Working, restartable agent over public planning material and one sample source |
| T−14 | Name the event and product leads; select remote tools and dates; send invitations with a response deadline no later than T−10 | Live agent, one owner per essential decision, and three to five concrete invitations |
| T−11 or T−10 | Pre-event 1: meet the working agent and agree the proof | Commitments, source-pack actions, and blockers recorded |
| T−9 | Source packs due; agent begins completeness and access checks | At least three candidate organisation packs |
| T−8 to T−7 | Technical lead loads approved sources into the running agent; representatives test initial answers | Concrete strengths, errors, and gaps before scope lock |
| T−7 or T−6 | Pre-event 2: use the agent and lock the build | Approved brief, three test questions, one digest, one delivery channel |
| T−5 to T−3 | Agent-assisted iteration: retrieval, source attribution, brief, action list, and demo path | A working vertical slice before the hackathon |
| T−2 | Pre-event 3: technical readiness and remote rehearsal | `Proceed`, `narrow`, or `postpone` decision |
| T−1 | Fix only readiness blockers; freeze new scope | Stable starting point and fallback material |
| T | Hackathon Day 1 | Improve accuracy, usefulness, and the cross-organisation digest |
| T+1 | Hackathon Day 2 | Deliver, test, demonstrate, document, and decide on the pilot |

This sequence requires the technical lead to start before invitations and organisation commitments. The starter agent should therefore use only the already-public proposal, execution files, and an approved sample source until source packs pass review.

## Minimal remote workspace

Choose one tool for each function and publish the links in the private calendar invitation or access message, not in this public repository if the links grant access.

| Function | Requirement | Selected tool |
|---|---|---|
| Video room | Persistent link, breakout support if needed, fallback link | `[TO SET]` |
| Coordination chat | One event channel for questions and blockers | `[TO SET]` |
| Code and public outputs | Versioned repository with clear setup instructions | `[TO SET]` |
| Shared working surface | One brief, action list, and visible decision record | `[TO SET]` |
| Delivery channel | One route for the digest; Telegram only if ready | `[TO SET]` |
| Starter-agent access | One simple interface participants can reach before Pre-event 1 | `[TO SET]` |

### Remote working rules

- Use the main room for integration, decisions, checkpoints, and representative tests.
- Open breakout rooms only for a named task and a fixed timebox.
- Keep cameras optional; make participation possible through voice and chat.
- Record decisions and outputs in the repository or shared working surface.
- Return to the main room at each checkpoint even when a task is incomplete.
- Raise blockers in the coordination chat with the owner needed to resolve them.
- Do not record the event unless participants have explicitly agreed how the recording will be used and published.
- Do not publish private names, personal contact details, meeting-access links, credentials, or non-public organisational material.

## Mandatory owners

Record public roles here. Handle private participant identities and contact details outside this repository unless publication has been explicitly approved.

| Role | Public owner label | Confirmed? | Required before |
|---|---|---|---|
| Event lead and decision owner | `[TO SET: ROLE OR APPROVED PUBLIC IDENTITY]` | No | Invitations sent |
| Product and scope lead | `[TO SET]` | No | Pre-event 1 |
| Technical lead | `[TO SET]` | No | Event confirmation |
| Infrastructure owner | `[TO SET]` | No | Server or cloud account created |
| Recovery custodian | `[TO SET]` | No | Pre-event 3 |
| Budget owner | `[TO SET]` | No | Paid infrastructure enabled |
| Post-event steward | `[TO SET]` | No | Event confirmation |
| Representative for each organisation | Track privately; publish roles only when approved | No | Pre-event 1 |

One person may hold the event and product roles. The technical lead may also be the infrastructure owner. The recovery custodian must be a second person who can restore the system if the technical lead is unavailable. The budget owner may hold another role but owns spend alerts and the stop-spend decision.

## Decision and readiness gates

### Gate A — Send invitations

- [ ] Event lead has accepted responsibility.
- [ ] Technical lead has completed the two-hour bootstrap.
- [ ] Working public product name is confirmed.
- [ ] Provisional build dates, event timezone, and daily live hours are stated.
- [ ] Dates for all three pre-events are stated.
- [ ] Response deadline and reply route are stated.
- [ ] The primary OpenClaw or Hermes runtime passes the two-hour bootstrap smoke test.
- [ ] Restart instructions and secret handling are documented without publishing secret values.

### Gate B — Confirm the hackathon

- [ ] At least three organisations have explicitly committed.
- [ ] Each has nominated a representative privately.
- [ ] Each has supplied a plausible public source set.
- [ ] Event, product, technical, and stewardship roles are owned.
- [ ] Attendance coverage across both build days is credible.
- [ ] The starter agent is running over public planning material and one approved sample source.

### Gate C — Lock the design

- [ ] Source packs have been reviewed.
- [ ] Primary user, journey, questions, digest, and delivery route are selected.
- [ ] In-scope, deferred, and manually handled work are explicit.
- [ ] Final demonstration and acceptance tests are agreed.
- [ ] Representatives have tested the running agent using submitted sources.

### Gate D — Start Day 1

- [ ] Remote tools and fallback links work.
- [ ] Every builder can access and run the prepared environment.
- [ ] The private access register is complete, current, and reviewed by the infrastructure owner and recovery custodian.
- [ ] Role boundaries have passed allowed-action and denied-action checks; no shared root credential is in routine use.
- [ ] Repository branch protection and server deletion protection are enabled.
- [ ] One sample source completes the intended path.
- [ ] The agent cannot modify canonical sources, administer the active datastore, delete backups, or expand its own permissions.
- [ ] Credentials and private access are handled outside the public repository.
- [ ] Organisation sources and fallback snapshots are ready.
- [ ] A verified off-host logical backup is current and an isolated restore has passed within 60 minutes.
- [ ] The kill switch, access-revocation route, and last-known-good rollback work.
- [ ] Product and technical leads can run through the demo story.

## Current next actions

1. Replace every `[TO SET]` field in this file and the invitation.
2. Name the event lead and working public product name.
3. Select two consecutive build dates, one event timezone, and a realistic live window two weeks from organiser start.
4. Name the technical lead and complete the bootstrap in `05-technical-specification.md` in one two-hour block.
5. Schedule the three pre-events and select the minimal remote workspace and fallback video link.
6. Send `01-participant-invitation.md` to three to five organisations only after the agent passes its smoke test.
7. Give confirmed participants access to the working agent.
8. Collect one `02-participation-and-source-pack.md` per organisation and load approved sources into the agent.
9. Apply Gate B, then create the hackathon brief and roles/readiness file from actual agent use and confirmed responses.
10. Use Pre-event 2 to lock the plan; continue improving the same agent and do not add major scope afterward.

## Source basis

This operating index implements the proposal’s two-day format, pre-event preparation, public-source contribution, and named ownership requirements. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#12-hackathon-format] [see: proposal/hackathon-1/Hackathon Planning Guide.md#7-preparation-journey-for-participating-organisations]
