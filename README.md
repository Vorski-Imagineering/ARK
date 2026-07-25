![ARK](ARK-sml.png)

# [Audax](https://audax.earth/) Lab №1 — Agentic Collaboration

Welcome. If you are reading this, you have been invited into a small working lab building **agentic collaboration between organisations** — shared AI agents that make a distributed community's work visible, understandable, and connected, so its people and organisations can find each other and act on what they learn.

This repository is our **commons**. It is the working surface where a live build, research, design, and tooling accumulate in public — not as a polished product, but as an honest, append-only trail of how we build collaboration infrastructure.

---

## What this lab is

[Audax](https://audax.earth/) Lab №1 exists to test one proposition: that a shared agent can make participating organisations more visible, connected, and useful to one another. The current, and first, test of that proposition is the **ARC Community Agent hackathon** — see [`proposal/hackathon-1/`](./proposal/hackathon-1/).

Memory, recall, and knowledge infrastructure are **not the point of this lab — they are the tool**. A shared agent that helps organisations collaborate has to remember what each one is doing, reason over it faithfully, attribute it correctly, and share it without confusing whose it is. That engineering problem is where most of our research effort goes, but it is in service of the collaboration the agent is actually for, not an end in itself.

So the questions we chase are collaboration questions first, memory questions second:

- What does an organisation need to share, and how, before a shared agent can represent it faithfully to the rest of a network?
- How does a group of agents remember things together without each one re-deriving context, or misattributing one organisation's work to another?
- What is the right substrate for **transcript-native** institutional intelligence — conversations as the source of truth, not documents as the artifact?
- How do we build knowledge systems that **dream**, **consolidate**, and surface emergent structure rather than just retrieve — reliably enough that a cross-organisational digest can be trusted?
- What does a knowledge commons look like when contributors — human, AI, and organisational — are visible, attributable, and welcome to fork?

The research work is grounded in two long-running threads in this repo: the **Coherence Company** thread (transcript-native intelligence, dreaming architectures, the Living Book) and the **Regentribe** thread (decentralized knowledge infrastructure on Radicle + SurrealDB). Both feed the tooling the ARC Community Agent needs.

---

## Current build — the ARC Community Agent hackathon

Our flagship collaboration experiment: a hackathon to build the first working version of a shared AI agent for the ARC network — a community of people who participate through organisations.

The agent has two connected functions:

1. **Updates** — collecting and synthesising organisational information into general community intelligence and participant-specific digests.
2. **Relationship management** — onboarding and engaging participants, maintaining their relationship with the community, and (in a later phase) surfacing worthwhile conversations between aligned people and organisations, always with consent.

The hackathon should produce one complete, observable loop:

```
Organisational public updates
        ↓
Collection and source-linked memory
        ↓
Cross-organisational synthesis
        ↓
Permission-controlled member delivery
        ↓
Member response, follow-up, and continued relationship
        ↓
Public learning and a pilot decision
```

The memory and knowledge-store work shows up here too — it's what lets the agent answer questions across organisations instead of parroting one feed — but the loop is not built to demonstrate memory. It is built to test whether a shared agent can make participating organisations more visible, connected, and useful to one another.

- **[`proposal/hackathon-1/arc-community-agent-hackathon-proposal.md`](./proposal/hackathon-1/arc-community-agent-hackathon-proposal.md)** — the event: scope, roles, format, evidence, and decision process.
- **[`proposal/hackathon-1/arc-community-agent-vision.md`](./proposal/hackathon-1/arc-community-agent-vision.md)** — the enduring product purpose and functionality.

---

## License — CC0 1.0 Universal

Everything in this repository is released under [**CC0 1.0 Universal**](./LICENSE) — a public domain dedication.

In plain language:

- **No copyright is asserted.** You can copy, fork, remix, redistribute, or build commercial products on this work without asking.
- **No attribution is required** (though if our work helps you, we would love to know).
- **Contributions you make become part of the commons.** When you push to this repo, you are dedicating your contribution to the public domain too. Do not contribute material you cannot release that way.

The license choice is deliberate. This is a **commons *and* a portfolio**.

A commons, because every artifact here is dedicated to the public domain so anyone can build on it. A portfolio, because everything you write here is signed by your commits and visible to anyone who wants to see how you think — your research, your syntheses, your judgment under uncertainty, the questions you choose to chase. We work in the open so we can:

- **show our thinking** — not just conclusions, but the reasoning, the assumptions, and the open questions;
- **share research and synthesis** — so the group's collective output compounds instead of being trapped in private notes;
- **learn together** — by reading each other's work, challenging it, and extending it;
- **show what each of us is capable of** — this is a working record of craft, taste, and rigor, and a legitimate thing to point at.

Both readings are intended. Contribute work you would be proud to put your name on, and contribute it in a way that helps the next person.

---

## Repository structure

The repo is organized around five kinds of artifact: **proposals**, **research**, **plans**, **needs**, and **tooling**. Each is a separate top-level folder so the kind of thinking is obvious from the path.

```
ARK/
├── README.md            ← you are here
├── AGENT.md             ← operating instructions for agents (read this)
├── LICENSE              ← CC0 public domain dedication
├── ARK.jpg              ← project mark
│
├── proposal/            ← agentic collaboration builds (the hackathon)
├── research/            ← the tools we have learned — memory, knowledge, runtimes
├── plan/                ← design specs and workstream plans
├── needs/               ← invitations, roles, calls for collaborators
├── scripts/             ← repo-wide tooling
└── skills/              ← shared agent skills
```

### `proposal/` — the collaboration builds

The live tests of the lab's core proposition — a proposal document defines the event, scope, roles, and decision process for each build.

- **`proposal/hackathon-1/`** — the ARC Community Agent hackathon proposal and vision (see above).

### `research/` — the tools we have learned

Durable, public, citable knowledge about the infrastructure a collaborating agent needs — not the collaboration itself. The point of this folder is that another agent or human can **find, cite, supersede, or fork** what is here later.

Current threads:

- **`research/The Coherence Company/`** — transcript-native institutional intelligence; comparisons of agent runtimes (OpenClaw vs HERMES); dreaming and consolidation architectures; the **Living Book Manifesto** (the philosophical anchor for much of this group's thinking on knowledge that grows).
- **`research/regentribe/`** — decentralized knowledge infrastructure: Genesis Brain architecture, Radicle + SurrealDB design, SurrealDB alternatives.

Per `AGENT.md`, research artifacts use uncertainty markers (`[ASSUMPTION: ...]`, `[OPEN QUESTION: ...]`, `[CONTRADICTS: ...]`, `[CONFIDENCE: low|medium|high]`) so that another contributor can see exactly where the load-bearing claims are and where they break.

### `plan/` — what we intend to build

Design specs, workstream breakdowns, and implementation sequencing. Plans cite research and produce explicit decisions.

- **`plan/The Coherence Company/metis-hermes-01/`** — a 13-part workstream covering the product/operating model, system boundary, runtime architecture, transcript and event model, memory and retrieval policy, dreaming/consolidation, knowledge graph, tooling, governance, evaluation, deployment, and migration sequencing. The `00-workstreams-index.md` is the entry point. `mvp.md` and `design-spec-research-agenda.md` set the scope.

### `needs/` — who we are looking for

Open calls for collaborators, role descriptions, invitations. If you are evaluating whether to step in on a workstream, this is where you find the framing.

- **`needs/The Coherence Company/AI-Dev Engineer.md`** — invitation to co-create as an AI orchestrator (not coder) on the Coherence build sprint.

### `scripts/` — repo-wide tooling

Small, dependency-light utilities meant for everyone in the group.

- **`scripts/chatgpt_project_to_markdown.py`** — turns a ChatGPT data export (zip, folder, or `conversations.json`) into repository-friendly Markdown, one file per conversation, with an `inventory.json` audit trail. See [`scripts/docs/chatgpt-export/README.md`](./scripts/docs/chatgpt-export/README.md) for usage.

### `skills/` — shared agent skills

Skills are reusable agent capabilities — packaged instructions an AI collaborator can pull in to do a specific job consistently across the group.

- **`skills/export-chatgpt-as-markdown/`** — companion skill for the export script above, so any agent in the group can run a ChatGPT export the same way.

This folder is intentionally young. New skills should be added as they prove useful to more than one collaborator. If you build something twice, package it as a skill.

---

## How we collaborate — the `AGENT.md` operating guide

[`AGENT.md`](./AGENT.md) is the document any AI agent (and any human contributor working with comparable diligence) reads before touching this repo. Read it once, end to end. What follows is the *shape of the experience* it describes — so you know what working here actually feels like.

When you sit down to contribute, the first thing you feel is the weight of this being **public and permanent**. Every word can be read, cited, and forked by anyone, forever. So you carry a quiet checklist with you: no PII, no names of private individuals (you use roles instead), no private chat excerpts, no credentials, no NDA-bound material, no internal URLs or ticket IDs. The rule of thumb is simple — if it would be inappropriate on a public website, it does not belong here. When in doubt, you leave it out.

Next you notice that you are being treated as a **research collaborator, not an assistant**. The expectation is transparent, auditable work: explicit assumptions, structured markdown, inline citations, no hidden reasoning, no answer-first shortcuts. You write for the next person who will walk into your thread cold and need to pick up where you left off, challenge your assumptions, or fork your direction.

When you start a real research task, the work moves through a familiar arc. You **scan** first — what is already in `research/` on this topic, what can you cite or supersede. Then you **decompose** — you write the sub-questions into a notes file *before* you go exploring, so the shape of the inquiry is visible. Then you **explore** — gathering data, citing inline as you go. Then you **synthesize** — pulling the threads into a document that stands on its own. Then you **reflect** — leaving open-question markers for what is still unclear. And finally you **persist** — a short dated entry in the topic's log so the trail is visible to whoever comes next. You append; you do not silently overwrite.

Throughout, citation and uncertainty are not optional. External sources are tagged with where you found them and when. Internal references link to the file and section you are building on. Load-bearing assumptions are marked so the next reader can challenge them. And you never fabricate a source — if you cannot verify it, you ask before citing it.

You also learn to recognise the **stop-and-ask moments** — the points where the right move is to pause and check in rather than push through. Before deleting or rewriting research, before publishing a name not already public, before citing something you cannot verify, before closing out a synthesis while open questions are still in the air. No approval, no action.

### What this means for the kind of collaboration this is

The research work described above is not a hackathon and it is not a Slack thread. It is closer to a **public lab notebook** that a small group keeps together. The hackathon itself runs to a tighter, event-scoped process (defined in `proposal/hackathon-1/`), but its outputs land back in the same notebook. The norms are tilted toward:

- **Slow, append-only work** over fast, throwaway output.
- **Visible reasoning** over polished conclusions.
- **Reproducibility for the next agent** over efficiency for the current one.
- **Disagreement made explicit** over silent consensus.
- **Public domain contribution** over private ownership.

If those norms appeal to you, you are in the right place. If they feel constraining, they will probably feel less so once you walk into a research thread someone else started six months ago and find that you can actually pick it up.

---

## Getting started as a new contributor

1. **Read [`README.md`](./README.md) this document end to end.** It is your welcome.
2. **Read `proposal/hackathon-1/`** first — it's the current build, and the clearest picture of what the lab is actually for.
3. **Skim `research/` and `plan/`** for the tooling threads that feed it. Start with `research/The Coherence Company/LIVING-BOOK-MANIFESTO.md` for the philosophical frame, and `plan/The Coherence Company/metis-hermes-01/00-workstreams-index.md` for what is being designed.
4. **Check `needs/`** if you are looking for an explicit role to step into.
5. **Pick a small first contribution** — a research note, a citation cleanup, a `[OPEN QUESTION]` you can answer. Follow the six-verb loop.
6. **Open a PR** with a short description of what you scanned, what you added, and what open questions remain.

Welcome to [Audax](https://audax.earth/) Lab №1
![ARK](./ARK.png)
