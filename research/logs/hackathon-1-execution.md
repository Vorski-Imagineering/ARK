# Hackathon 1 execution log

## 2026-07-21

- Files touched: `research/notes/hackathon-1-execution.md`, `research/synthesis/hackathon-1-execution-plan.md`, `research/logs/hackathon-1-execution.md`
- Status: synthesized
- Summary: Reviewed both proposal files and converted the broad product vision into a minimal execution package for a prepared two-day hackathon. Defined eight core event files, a four-week preparation runway, one 90-minute design session, an hour-by-hour run-of-show, explicit owner roles, acceptance criteria, fallbacks, and readiness gates.
- Open questions: public product name; named event, technical, and post-event owners; whether Telegram is essential; reuse permission or licence; final representative test questions.

## 2026-07-21

- Files touched: `proposal/hackathon-1/execution/00-start-here.md`, `proposal/hackathon-1/execution/01-participant-invitation.md`, `proposal/hackathon-1/execution/02-participation-and-source-pack.md`, `research/notes/hackathon-1-execution.md`, `research/synthesis/hackathon-1-execution-plan.md`, `research/logs/hackathon-1-execution.md`
- Status: open
- Summary: Implemented the first three operational documents for a remote-only two-day hackathon. Added a minimal preparation sequence consisting of a 60-minute orientation, a 90-minute design lock, and a 45-minute core-team technical readiness session; also appended the remote-format decision to the research note and synthesis.
- Open questions: build dates; event timezone and daily live window; minimal remote tool set; named role owners; private reply route; product name; source reuse basis; whether Telegram will be ready as the delivery channel.

## 2026-07-21

- Files touched: `proposal/hackathon-1/execution/00-start-here.md`, `proposal/hackathon-1/execution/05-technical-specification.md`, `research/notes/hackathon-1-technical-plan.md`, `research/synthesis/hackathon-1-technical-plan.md`, `research/logs/hackathon-1-execution.md`
- Status: synthesized
- Summary: Reviewed the repo's ARC proposal, Genesis Brain, SurrealDB, Hermes/Coherence, source-of-truth, tooling, and deployment work, then produced a minimal technical plan for the remote event. Recommended a Git-backed canonical corpus, one Python process, disposable SQLite/file retrieval, a small shared server, configurable embedding/generation models, prepared acceptance fixtures, explicit readiness gates, and a EUR 50 event ceiling.
- Open questions: repository and deployment owners; event dates; staging domain or tunnel; first-cohort source formats; whether Telegram is required or a stretch adapter.

## 2026-07-21

- Files touched: `proposal/hackathon-1/execution/00-start-here.md`, `proposal/hackathon-1/execution/01-participant-invitation.md`, `proposal/hackathon-1/execution/02-participation-and-source-pack.md`, `research/notes/hackathon-1-execution.md`, `research/synthesis/hackathon-1-execution-plan.md`, `research/logs/hackathon-1-execution.md`
- Status: open
- Summary: Compressed the event runway from four weeks to two weeks and raised the technical readiness session from 45 to 60 minutes so every scheduled preparation session is at least one hour. Changed the operating model to launch a starter agent within 48 hours, use it throughout participant preparation, load approved sources before design lock, and build on the same agent during the two hackathon days.
- Open questions: technical lead; starter-agent interface and runtime; first approved sample source; build dates and timezone; remote tools; public product name; source reuse basis; Telegram readiness.

## 2026-07-21

- Files touched: `proposal/hackathon-1/execution/00-start-here.md`, `proposal/hackathon-1/execution/01-participant-invitation.md`, `proposal/hackathon-1/execution/05-technical-specification.md`, `research/notes/hackathon-1-execution.md`, `research/synthesis/hackathon-1-execution-plan.md`, `research/notes/hackathon-1-technical-plan.md`, `research/synthesis/hackathon-1-technical-plan.md`, `research/logs/hackathon-1-execution.md`, `research/logs/hackathon-1-technical-plan.md`
- Status: open
- Summary: Moved the starter agent outside the two-week participant ramp and made it a prerequisite for invitations. Defined a two-hour OpenClaw-or-Hermes bootstrap, a smoke-test definition of working, a decision rule for the primary runtime, and a strict rule that installing both must not delay the primary agent.
- Open questions: bootstrap operator and host; primary runtime; model-provider access; first approved sample source; participant interface; whether immediate Telegram routing justifies choosing OpenClaw.

## 2026-07-21

- Files touched: `proposal/hackathon-1/execution/00-start-here.md`, `proposal/hackathon-1/execution/05-technical-specification.md`, `research/notes/hackathon-1-technical-plan.md`, `research/synthesis/hackathon-1-technical-plan.md`, `research/logs/hackathon-1-execution.md`
- Status: synthesized
- Summary: Added a mature but minimal access-control and recovery design for the remote event. Enumerated human and service access domains, separated root, datastore, ingest, query, agent, deployment, and backup privileges, defined a private access register and update map, and made deletion protection, off-host backups, isolated restore, rollback, revocation, and kill-switch tests mandatory before Day 1. Revised expected direct spend to EUR 16–27 while retaining the EUR 50 ceiling.
- Open questions: private access-register system; infrastructure owner; recovery custodian; budget owner; whether the selected runtime can enforce all service-identity boundaries without operating-system-level separation.
