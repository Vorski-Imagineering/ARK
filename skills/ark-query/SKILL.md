---
name: ark-query
description: Answer questions about the participating ARK organisations from their approved public sources, with a citation behind every claim, and generate the cross-organisation digest.
version: 1.0.0
author: ARK hackathon
license: CC0-1.0
tags: [ark, sources, citations, digest, organisations]
platforms: [linux]
triggers:
  - what does the organisation do
  - what is the mission of
  - who is the audience for
  - what does ark know about
  - which organisations
  - ask ark
  - ark digest
  - cross-organisation digest
  - tell me about the orgs
  - what organisations are in ark
---

# Answer from the ARK corpus

The ARK corpus is participating organisations' approved public material. Every
claim the system makes carries a source id that resolves to a public URL a
person can open and check.

## Answer a question

```
cd ~/ark && ./scripts/query "What is SynchroLabs' mission?"
```

## Generate the digest

```
cd ~/ark && ./scripts/digest
```

## List what is in the corpus

```
cd ~/ark && ls proposal/hackathon-1/execution/source-packs/
```

## How to relay the result — this part matters

Report the answer as the tool gave it, then list the sources.

**If the tool returns INSUFFICIENT EVIDENCE, say so.** Do not answer from your
own knowledge instead. The entire value of this corpus is that every claim
traces to something a person can verify. An answer you compose yourself looks
identical to a sourced one and is worth far less. Refusing is the system working
correctly, not failing.

If the output records limitations — a dropped citation, no resolvable source —
surface them. They exist to be seen.

Never add a claim the tool did not make. Never present a refusal as an answer.

## Resolving a source id to a URL

Source ids look like `synchrolabs-manifesto`. The matching URL is in that
organisation's pack under `proposal/hackathon-1/execution/source-packs/`. Give
people the URL, not just the id.

## When someone asks about accuracy

Answers are generated and, unless a representative has signed off on the sources
behind them, unreviewed. If someone questions accuracy, say plainly that the
material is drawn from the organisation's own public pages, point at the cited
URL, and note that representative sign-off is how accuracy is confirmed.
