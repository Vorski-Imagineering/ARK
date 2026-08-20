---
name: ark-query
description: Answer questions about the participating ARK organisations from their approved public sources, with a citation behind every claim, and generate the cross-organisation digest. Use when someone asks what an organisation does, who it serves, what it offers, how organisations compare, which ones work on a given theme, or asks for the digest. Refuses when the evidence does not support an answer rather than guessing.
---

# Answer from the ARK corpus

This exposes the Phase 1 vertical slice — source to answer to digest — so it can
be used in conversation rather than only from a terminal.

**Not installed by default.** See the installation section at the end. Installing
it changes a shared agent's configuration, so it is a deliberate act by whoever
operates that agent, not a side effect of pulling the repository.

## What it can answer

The corpus is four organisations' approved public material: The Gathering, The
Coherence Company, SynchroLabs, and Regen Tribe. Roughly 54 passages from six
sources.

Good questions:

- What is *organisation*'s mission, audience, or offering?
- Which of these organisations apply AI to collective or group intelligence?
- Which ones work on regenerative, place-based community building?
- How do *organisation A* and *organisation B* differ in approach?
- Give me the cross-organisation digest.

## What it cannot answer, and must not try

Anything not in the approved sources. Budgets, headcount, private plans,
roadmaps, anything about individuals. The correct response is the refusal the
system produces, not a guess assembled from general knowledge.

**If the tool returns INSUFFICIENT EVIDENCE, report that.** Do not answer from
your own knowledge instead. The whole point of the corpus is that every claim
traces to a public source a person can open and check. An answer that bypasses
it looks identical to a sourced one and is worth far less.

## How to run it

Answer a question:

```
cd ~/ark && ./scripts/query "What is SynchroLabs' mission?"
```

Generate the digest:

```
cd ~/ark && ./scripts/digest
```

Both print the answer, the cited source ids, any limitations the system
recorded, and the token usage.

## How to relay the result

Report the answer as given. Then list the sources, resolving each id to its
public URL using the source packs in
`proposal/hackathon-1/execution/source-packs/`. A reader must be able to click
through and check the claim.

If the system recorded limitations — a dropped citation, no resolvable source —
say so plainly. Those exist to be surfaced, not filtered out.

Never present a refusal as an answer. Never add a claim the tool did not make.

## Adding an organisation or a source

You cannot do this from a conversation today. Source packs are added by pull
request to the repository, reviewed by the organisers, and confirmed by that
organisation's representative before use.

If someone asks to add their organisation, point them at
`proposal/hackathon-1/execution/02-participation-and-source-pack.md` and the
`ark-source-pack` skill, and tell them a human reviews it. Conversational
onboarding is Phase 2 and is not built.

## Installation

The operator of the agent installs this, having read it.

1. Ensure the repository is cloned on the host and its environment is set up:
   `cd ~/ark && ./scripts/setup && ./scripts/test` — expect 92 passed.
2. Build the index: `./scripts/ingest --local-embedder`
3. Copy this directory into the agent's skills location.
4. Restart the agent gateway.

The agent needs read access to `~/ark` and permission to run `./scripts/query`
and `./scripts/digest`. It needs nothing else — no write access to the corpus, no
ability to change its own configuration. That boundary is deliberate.
