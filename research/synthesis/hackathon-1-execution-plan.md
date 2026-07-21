# Hackathon 1 execution plan

**Status:** Planning basis for a two-day event  
**Date:** 2026-07-21  
**Scope:** Minimum preparation that makes two live build days worth attending

## 1. Basis and design choice

The source proposal describes a broad ARC Agent: it would gather public organisational activity, answer questions, produce shared summaries, support onboarding, participate in Telegram, and publish in public. Its stated purpose is to test a useful shared intelligence loop rather than build a finished platform. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#1-executive-summary]

The planning guide explicitly calls for minimum viable organisation and minimum viable design, converting existing interest from three to five organisations into named participation and usable preparation. [see: proposal/hackathon-1/Hackathon Planning Guide.md#core-planning-principle]

For a two-day event, the proposal should therefore be treated as the product vision, not as the two-day backlog. The event should prove one thin end-to-end experience:

> At least three organisations provide prepared public source packs; the prototype makes their material jointly explorable through sourced answers; it creates one useful cross-organisation digest; the digest is delivered through one simple channel; organisation representatives verify the result.

This is the minimum credible proof that the shared agent deserves a short pilot. It preserves the source proposal’s core information loop while removing features that do not need to be proven simultaneously. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#10-minimum-viable-prototype]

## 2. Minimal-effort operating principles

1. **Prepare inputs, not presentations.** Every organisation supplies a short profile and a small set of approved public sources before the event.
2. **Use a running skeleton.** Day 1 must not begin with repository setup, account creation, framework selection, or bot credentials.
3. **Prove one journey.** The primary journey is an active member asking what is happening across participating organisations and receiving a sourced answer and digest.
4. **Use one delivery channel.** Telegram is preferred only if access works before the event. Otherwise use the simplest working interface and publish or paste the digest manually.
5. **Allow manual seams.** Manual ingestion, triggering, review, or publishing is acceptable when it proves value without hiding the seam.
6. **Build together in one room.** Use one shared live collaboration space even if participants are remote. Avoid parallel tracks that only meet at the final demo.
7. **One owner may hold several roles.** Do not recruit a large organising committee.
8. **Stop adding scope after the preparation session.** New ideas go to a post-event list.
9. **Test with representatives twice.** Accuracy and usefulness checks happen at the end of each day, not only at the final presentation.
10. **Do not run without a steward.** A prototype with no named owner for the following two to four weeks is not ready for the event.

## 3. The execution package

Create one directory, proposed as `proposal/hackathon-1/execution/`. These eight files are the entire core operating system for the event.

| Order | File | What it decides or enables | Owner | Needed by | Done when |
|---|---|---|---|---|---|
| 1 | `00-start-here.md` | Current status, owners, dates, links, next decision, and document index | Event lead | Before outreach | A newcomer can see the state and next action in two minutes |
| 2 | `01-participant-invitation.md` | Invitation, exact participation ask, response deadline, confirmation message | Event lead | Outreach | It asks for named people, preparation, both build days, and a decision by a date |
| 3 | `02-participation-and-source-pack.md` | One compact response form per organisation: profile, desired value, nominees, sources, permissions, and readiness | Organisation representative | Commitment gate | At least three usable and approved source packs exist |
| 4 | `03-hackathon-brief.md` | Challenge, primary user and journey, scope, acceptance test, organisations, and continuation owner | Product lead | End of preparation session | Participants approve a two-page maximum brief |
| 5 | `04-run-of-show.md` | Pre-event checklist, two-day timetable, checkpoints, decision rules, demo, and retrospective | Event lead | Seven days before event | Every session has a purpose, owner, output, and timebox |
| 6 | `05-technical-specification.md` | Inputs, expected behaviours, provenance rules, interfaces, prepared environment, fallbacks, constraints, and acceptance tests | Technical lead | Seven days before event | Another builder can run the skeleton and understand the proof without an architecture workshop |
| 7 | `06-roles-and-readiness.md` | Named role owners, organisation participation, readiness gates, coordination channel, and escalation path | Event lead | Event confirmation | All mandatory roles and gates have explicit status |
| 8 | `07-demo-test-and-pilot.md` | Demo script, accuracy/usefulness rubric, limitations, pilot decision, and stewardship checklist | Product lead and steward | Day 2 morning | The team can run the demo, record evidence, and make a continuation decision |

### Files not to create by default

Do not create separate agendas, surveys, FAQs, risk registers, team charters, ideation canvases, architecture option papers, feature backlogs, retrospective documents, or communications plans. Put the small amount of necessary material in the eight files above.

Add `budget-and-logistics.md` only when venue, travel, catering, equipment, or shared costs require a real decision. Add `decision-log.md` only when `00-start-here.md` becomes too long. Add `communications-kit.md` only when public communication has a named owner and a concrete publication commitment.

## 4. What the invitation asks for

The invitation is not an invitation to discuss the idea. It asks an organisation to confirm a small package of work:

- Nominate one representative who can describe and verify the organisation’s public information.
- Nominate one builder or hands-on contributor if available; this is optional.
- Attend one 90-minute preparation session.
- Attend both hackathon days, or ensure the representative is present at defined testing checkpoints.
- Complete one source pack: a short public profile, one desired outcome, and one to three stable public sources.
- Confirm that the selected material may be accessed, summarised, and cited for this public experiment.
- Test whether the prototype is accurate and useful.
- Join a 45-minute review after the event.
- State any offered support such as venue, facilitation, communication, building, or modest shared costs.

The organisation receives a functioning shared prototype, visibility across participating public material, reusable documentation, and direct participation in the pilot decision. An organisation without a technical contributor can still participate fully through source preparation, product decisions, testing, and accuracy review.

## 5. Minimum team and decision rights

### Mandatory named roles

| Role | Before the event | During the event | Time expectation | Can combine with |
|---|---|---|---|---|
| Event lead and decision owner | Outreach, date, format, readiness, logistics, run-of-show | Facilitation, timeboxes, blockers, final calls | 2–4 hours/week for four weeks, plus event | Product lead |
| Product and scope lead | Primary journey, brief, acceptance tests, representative preparation | Scope protection, testing, demo narrative | 2–3 hours/week, plus event | Event lead, documentation |
| Technical lead | Feasibility, running skeleton, repository, access, fallback | Implementation decisions and integration | 4–8 hours preparation, plus event | Builder, post-event steward |
| Post-event steward | Pilot plan, operating assumptions, continuation conditions | Capture limitations and operational needs | 1–2 hours preparation; 2–4 hours/week during pilot | Technical or product lead |
| One representative per organisation | Complete source pack and nominate participants | Answer questions; verify accuracy and usefulness | 60–90 minutes preparation, plus checkpoints or event | Test user, contributor |

Two or three additional builders are sufficient. Documentation should rotate or be held by the product lead. A separate AI architect, data engineer, onboarding designer, communications lead, or project manager is optional unless a participant is already available and the role solves an observed need.

### Decision rights

- The event lead decides logistics and whether readiness gates pass.
- The product lead decides scope and acceptance, informed by representatives and technical feasibility.
- The technical lead decides the implementation route and rejects work that cannot fit the timebox.
- Organisation representatives decide whether their own information is represented accurately and whether the shared output is useful.
- The named steward and participating organisations decide whether to run the pilot.

If a decision remains unresolved for more than ten minutes during the event, the relevant owner decides, records the choice, and work continues.

## 6. Minimum outcome and acceptance test

### Must work by the final demonstration

1. Public information from at least three participating organisations is available in one shared retrieval surface.
2. A participant can ask at least three representative questions across the combined material.
3. Answers distinguish source material from generated synthesis and point to original sources.
4. The system creates one concise cross-organisation digest from the prepared material.
5. The digest is delivered through one accessible channel.
6. Each organisation representative reviews its relevant content for material inaccuracies.
7. A new or updated public source can be added through a documented process.
8. The group records limitations and makes a pilot, revise, or stop decision.

### May be manual or simulated

- Triggering ingestion or the digest.
- Copying the digest into the delivery channel.
- Reviewing and approving the digest.
- Loading static exports where a live platform is difficult to access.
- Adding a source through a configuration file with technical assistance.
- Collecting test feedback in the event document.

Manual seams must be declared in the demo. They are learning, not failure.

### Deferred until a pilot proves value

- Full scheduled ingestion for every source type.
- Deep Telegram participation or conversation memory.
- New-member onboarding beyond a short scripted example.
- Personalised feeds and member profiles.
- Automated public social publishing.
- Cross-agent protocols, knowledge graphs, dashboards, or production infrastructure.
- Private data, permissions systems, advanced governance, or scale optimisation.

These deferrals follow the proposal’s own distinction between the immediate information loop and the longer-term platform. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#8-proposed-hackathon-scope]

## 7. Preparation timeline

Use a four-week runway. It is short enough to preserve momentum and long enough to secure people and usable inputs. Compress to three weeks only if the mandatory owners and likely organisations are already known.

### Week 1 — Make the offer concrete

**Goal:** convert broad interest into explicit responses.

- Name the event lead and provisional product lead.
- Draft `00-start-here.md` and `01-participant-invitation.md`.
- Set a provisional date, format, and response deadline.
- Send the same concise invitation to three to five organisations.
- Hold calls only where an organisation has a material question; do not schedule calls as a default ritual.

**Output:** named organiser, provisional date, invitations sent, response deadline seven days later.

### Week 2 — Confirm people and inputs

**Goal:** establish whether the event is real.

- Collect `02-participation-and-source-pack.md` from each organisation.
- Confirm one representative and actual attendance windows per organisation.
- Name the technical lead and post-event steward.
- Reject unstable, inaccessible, unclear, or inappropriate sources early.
- Confirm at least three source packs.

**Decision:** pass Commitment Gate or postpone.

### Week 3 — Lock the proof

**Goal:** agree the one journey and make it technically credible.

- Hold one 90-minute preparation session.
- Finish `03-hackathon-brief.md`.
- Select the single delivery channel.
- Draft `05-technical-specification.md` around acceptance tests and fallbacks.
- Assign builders to the shared outcome, not isolated feature tracks.

**Output:** approved brief, acceptance test, technical route, owner map.

### Week 4 — Remove Day 1 setup work

**Goal:** arrive ready to integrate and test.

- Technical lead prepares and demonstrates a running skeleton using one sample source.
- Confirm repository access, model/API access, delivery channel, cost limit, and secrets handling outside the public repo.
- Validate all source packs and prepare static fallback copies where needed.
- Finish `04-run-of-show.md`, `06-roles-and-readiness.md`, and the demo section of `07-demo-test-and-pilot.md`.
- Run a 30-minute readiness check 48 hours before the event.

**Decision:** pass Readiness Gate or postpone. Do not use Day 1 to repair failed preparation.

## 8. The 90-minute preparation session

### Required participants

Event lead, product lead, technical lead, post-event steward, and one representative from every participating organisation.

### Preparation

Each organisation submits its source pack at least two days earlier. The product lead circulates a draft one-page brief. The technical lead states what is already running and identifies only decisions the group must make.

### Agenda

| Time | Activity | Required output |
|---|---|---|
| 0:00–0:10 | Restate purpose and two-day constraint | Shared understanding of the proof, not the full vision |
| 0:10–0:25 | Representatives state one desired benefit and one risk | Concise value and risk list |
| 0:25–0:40 | Choose the primary user and journey | One user, one main question pattern, one digest audience |
| 0:40–0:55 | Review source packs and permission constraints | Included organisations and approved sources |
| 0:55–1:10 | Lock in-scope, deferred work, and manual seams | Scope boundary and fallback path |
| 1:10–1:20 | Confirm acceptance test and demo story | Observable end-to-end proof |
| 1:20–1:30 | Confirm owners, attendance, steward, and readiness date | Named responsibilities and next actions |

The product lead updates the two-page brief within 24 hours. Silence for one working day counts as acceptance only if that rule was announced in the session; otherwise each representative gives an explicit approval.

## 9. Two-day run-of-show

Use two consecutive days, approximately 09:30–17:30, with a shared live room. The event lead protects breaks and avoids a late-night culture; prepared teams make better decisions than exhausted teams.

### Day 1 — Make the shared knowledge useful

| Time | Session | Output |
|---|---|---|
| 09:30–10:00 | Welcome, purpose, demo target, scope, decision rights | Everyone knows the one proof and their role |
| 10:00–10:30 | Technical skeleton and source-pack walkthrough | Common starting point; no framework debate |
| 10:30–12:30 | Load and normalise organisation sources | At least one usable source per organisation |
| 12:30–13:30 | Lunch | — |
| 13:30–15:00 | Build and test sourced question answering | Three representative questions return traceable answers |
| 15:00–15:20 | Representative accuracy check | Corrections and severity-ranked failures |
| 15:20–16:40 | Integrate corrections and create first digest | Draft cross-organisation digest |
| 16:40–17:10 | End-to-end checkpoint | Source → answer → digest works once |
| 17:10–17:30 | Record decisions, blockers, and Day 2 priorities | Maximum three priorities for Day 2 |

**Day 1 exit test:** at least one source from each organisation is usable, one cross-organisation question has a sourced answer, and a rough digest exists. If this fails, Day 2 narrows the number or type of sources; it does not add features.

### Day 2 — Make the proof reliable and judge it

| Time | Session | Output |
|---|---|---|
| 09:30–09:45 | Reset and confirm the three priorities | Shared Day 2 focus |
| 09:45–11:15 | Repair provenance, retrieval, and major accuracy failures | Demo path is credible |
| 11:15–12:15 | Connect the single delivery channel and document one source-add flow | Digest reaches a user; adding a source is repeatable |
| 12:15–13:15 | Lunch | — |
| 13:15–14:15 | Representative scenario testing | Accuracy and usefulness evidence |
| 14:15–15:15 | Fix only demo-blocking defects; document the rest | Stable vertical slice and known limitations |
| 15:15–16:00 | Rehearse the demo and publish the build note | Clear, reproducible demonstration |
| 16:00–16:45 | Final demonstration | Observable acceptance test |
| 16:45–17:15 | Retrospective and pilot decision | Pilot, revise, or stop decision with reasons |
| 17:15–17:30 | Steward handoff and recognition | Next owner, next date, contributors recorded by role or approved public identity |

## 10. Technical specification boundary

`05-technical-specification.md` should be short and implementation-enabling. It should contain:

1. **Demonstration scenario:** the exact source-to-answer-to-digest flow.
2. **Inputs:** organisation profile fields, allowed source types, source metadata, update dates, and licence or permission confirmation.
3. **Outputs:** sourced answer shape, digest shape, delivery target, and limitations notice.
4. **Required behaviours:** load prepared sources, retrieve across organisations, retain provenance, answer representative questions, create digest, and add one source predictably.
5. **Quality rules:** do not invent missing information; separate direct organisational material from generated synthesis; include source links; allow representative correction.
6. **Prepared environment:** repository, runtime, one working example, credentials supplied outside the public repository, development instructions, and cost ceiling.
7. **Fallbacks:** static source snapshot, manual trigger, manual publishing, and non-Telegram demonstration interface.
8. **Acceptance tests:** the eight tests in Section 6.
9. **Constraints:** public data only, no private participant profiles, no production security claims, no dependence on a fragile integration for the core demo.
10. **Deferred decisions:** scale architecture, framework replacement, personalisation, production operations, and broad platform integrations.

The proposal correctly requires source traceability and recommends keeping the agent runtime replaceable from the knowledge layer. Those are durable constraints; a detailed architecture choice is not a group prerequisite. [see: proposal/hackathon-1/ARC Community Agent Proposal.md#11-high-level-technical-approach]

## 11. Readiness and continuation gates

### Gate A — Send invitations

Proceed when an event lead, provisional date and format, concise participation ask, response deadline, and draft outcome exist.

### Gate B — Confirm the event

Proceed when at least three organisations have named representatives, supplied plausible public sources, and confirmed attendance; the event, product, technical, and stewardship roles also have owners.

Polite interest, a logo, or a promise to “find someone” does not count.

### Gate C — Start Day 1

Proceed when the brief is approved, sources are accessible, a skeleton runs with one example, repository and delivery access work, secrets handling is clear, fallbacks exist, and the final demo can be described in under two minutes.

If a mandatory item is missing 48 hours before the event, the event lead narrows scope or postpones.

### Gate D — Run a pilot

Run a two-to-four-week pilot only if:

- representatives judge the output materially accurate and at least moderately useful;
- source provenance is visible;
- the primary loop works more than once;
- major limitations are documented;
- operating effort and costs are tolerable for the pilot;
- one steward accepts responsibility and a review date is booked.

Otherwise narrow and repair, pause, or stop and document the learning.

## 12. Success evidence

### Organising success

- Three to five organisations cross the commitment gate.
- Every participating organisation submits a usable source pack and names a representative.
- Event, product, technical, and stewardship roles have owners.
- The brief, primary journey, demo, date, format, and delivery channel are locked before Day 1.
- A running skeleton and fallback sources exist.

### Hackathon success

- One end-to-end experience passes the acceptance test.
- At least three organisations appear in the shared knowledge and digest.
- Source links support material generated claims.
- Representatives identify no unresolved material misrepresentation in the final demo.
- Test users judge whether the output saved attention or revealed useful cross-organisation context.
- The team makes an evidence-based continuation decision.

Attendance, idea count, code volume, connector count, and social reach are not success measures.

## 13. Main risks and minimal responses

| Risk | Early warning | Prevention | Response |
|---|---|---|---|
| Interest without commitment | No named person or source pack by deadline | Invitation asks for concrete inputs | Exclude from V1; keep the door open for the pilot |
| Event has no real owner | Logistics and decisions drift among a group | Name one event lead before outreach | Pause outreach until one person accepts |
| Scope expands to the full proposal | Multiple “must-have” journeys remain after preparation | Lock the brief and one acceptance test | Product lead defers additions publicly |
| Day 1 becomes setup day | Accounts, repository, or runtime are untested | Running skeleton gate | Postpone or use prepared fallback environment |
| Sources cannot be used | Access, permission, format, or quality is unclear | Validate source packs in Week 2 | Use static approved sources or exclude the source |
| Technical builders detach from community value | Architecture discussions replace representative tests | Two daily representative checkpoints | Stop feature work and run the next test scenario |
| Telegram blocks the demo | Bot/group access is unresolved | Treat Telegram as conditional | Use the fallback interface and manual delivery |
| Representatives become spectators | They are invited only for opening and demo | Give them accuracy and usefulness decisions | Pause integration for representative review |
| Prototype dies after the event | No named steward or review date | Make stewardship a confirmation gate | Do not label the event ready; postpone |
| Public repository receives sensitive material | Participants submit private or credential-bearing data | Public-only source pack and explicit screening | Do not ingest; remove from the working set and rotate exposed credentials outside the repo if needed |

## 14. Creation sequence for the eight files

Do not draft everything at once.

### Before outreach

Create:

1. `00-start-here.md`
2. `01-participant-invitation.md`
3. `02-participation-and-source-pack.md`

These convert interest into commitment and reveal whether the event is viable.

### After three organisations respond

Create:

4. `03-hackathon-brief.md`
5. `06-roles-and-readiness.md`

These lock the human, product, and ownership structure.

### After the preparation session

Create:

6. `05-technical-specification.md`
7. `04-run-of-show.md`

The technical lead and event lead write from agreed decisions, avoiding speculative detail.

### During final preparation and the event

Create:

8. `07-demo-test-and-pilot.md`

Start with the demo script before Day 1; add evidence, limitations, and the pilot decision during Day 2.

## 15. Immediate next ten actions

| Sequence | Action | Owner | Definition of done |
|---|---|---|---|
| 1 | Name the event lead | Initiating group | One person explicitly accepts decision ownership |
| 2 | Resolve the working public name | Event lead | Invitation uses one consistent name |
| 3 | Choose a provisional two-day date and format | Event lead | Date is four to five weeks away and can be offered concretely |
| 4 | Draft the first three execution files | Event lead with product lead | Index, invitation, and source-pack template are reviewable |
| 5 | Send invitations to three to five organisations | Event lead | Each receives the same ask and seven-day deadline |
| 6 | Confirm representatives and source packs | Organisation representatives | At least three complete commitments exist |
| 7 | Name technical lead and post-event steward | Event lead | Both accept pre-event and follow-through responsibilities |
| 8 | Schedule and run the 90-minute preparation session | Product lead | Primary journey, sources, scope, demo, and owners are locked |
| 9 | Prepare and test the skeleton and fallback | Technical lead | One sample source completes the intended path before the event |
| 10 | Hold the 48-hour readiness gate | Event lead | Proceed, narrow, or postpone is recorded with evidence |

## 16. Decisions still required

These are not reasons to delay organising; each has a defined deadline in the plan.

- [OPEN QUESTION: Should participant-facing materials use ARC Agent, ARK Agent, or another working name? Resolve before invitations are sent.]
- [OPEN QUESTION: Who accepts the event-lead, technical-lead, and post-event-steward roles? Resolve before the event is confirmed.]
- [OPEN QUESTION: Is Telegram essential to the value proof, or merely the preferred delivery channel? Resolve in the preparation session and lock seven days before the event.]
- [OPEN QUESTION: Which reuse permission or licence applies to organisation-provided sources and generated public outputs? Resolve before source ingestion.]
- [OPEN QUESTION: Which three representative questions best test cross-organisation value? Draft before and approve during the preparation session.]

[CONFIDENCE: high] The event can be organised with this eight-file package and a four-week runway if the mandatory roles, source packs, and running skeleton cross the stated gates. The primary uncertainty is not planning complexity; it is whether named people accept ownership and preparation commitments.

## 2026-07-21 addendum — Remote-only format and pre-events

The event is now confirmed as remote-only. This supersedes the format-neutral passages above.

[CONTRADICTS: research/synthesis/hackathon-1-execution-plan.md] Replace the single 90-minute preparation session described above with the following minimal sequence:

1. A 60-minute orientation and commitment session approximately three weeks before the event, required for confirmed representatives and builders.
2. A 90-minute design-lock session approximately two weeks before the event, required for confirmed representatives and builders.
3. A 45-minute technical readiness and remote rehearsal 48 hours before the event, required only for the core delivery team and builders.

The remote workspace should use one video room, one coordination chat, one repository, and one shared working surface. The invitation must state the event timezone, daily live hours, pre-event dates, and attendance expectations. Platform access, repository access, a sample source, the fallback demonstration path, and the final demo outline must be verified during the readiness session.

## 2026-07-21 addendum — Two-week agent-first runway

This addendum supersedes the four-week runway and the preparation timings above.

[CONTRADICTS: research/synthesis/hackathon-1-execution-plan.md] The final operating model uses a two-week ramp-up, makes every scheduled preparation session at least 60 minutes, and requires a working starter agent within 48 hours of organiser start.

The sequence is:

1. T−14 to T−12: launch a simple agent over public proposal and execution material plus one approved sample source.
2. T−13: send invitations.
3. T−11 or T−10: run a 60-minute orientation in which participants use the agent.
4. T−9: collect source packs; load approved sources immediately.
5. T−8 to T−7: representatives test the agent against their sources.
6. T−7 or T−6: run a 90-minute design lock based on observed behaviour.
7. T−5 to T−3: improve the same agent and use it to help prepare the brief, actions, source checks, tests, and demo.
8. T−2: run a 60-minute technical readiness and remote rehearsal.
9. T and T+1: conduct the two build days on top of the working agent.

The agent may assist with public event Q&A, source-pack completeness, public URL checks, source-linked test questions, draft briefs, action lists, progress summaries, retrieval testing, and demo preparation. Human owners retain commitments, permissions, accuracy approval, public release approval, scope, dates, ownership, and readiness decisions. Private participant data, credentials, access links, private meeting transcripts, and non-public organisational information remain outside the agent and public repository.

## 2026-07-21 addendum — Agent exists before the ramp

This addendum supersedes the 48-hour launch target above. The primary agent runtime must be installed, configured, smoke-tested, and restartable in a single two-hour block before invitations and before the two-week participant countdown.

[CONTRADICTS: research/synthesis/hackathon-1-execution-plan.md] The starter agent is no longer a T−14 to T−12 deliverable. It is a Gate A prerequisite.

Use Hermes as the default first runtime when the priority is one evolving agent assisting preparation. Use OpenClaw when immediate Telegram or multi-channel routing is the priority. Install both only through parallel owners; the secondary runtime must not delay the primary smoke test. Public source packs and reviewed outputs remain canonical outside either runtime. [see: research/The Coherence Company/CoCo-OpenClaw-vs-Hermes.md#recommended-architecture-for-coco]

The detailed bootstrap and smoke test are specified in `proposal/hackathon-1/execution/05-technical-specification.md`.
