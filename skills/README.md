# Shared agent skills

Reusable capabilities an AI collaborator can pull in to do a specific job
consistently. If you build something twice, package it here.

## What is here

| Skill | What it does | Installed on the ARK agent |
|---|---|---|
| `ark-query` | Answer from the ARK corpus with citations; generate the digest | Yes |
| `ark-add-organisation` | Capture an organisation's pages, draft its pack, stage it | Yes |
| `ark-source-pack` | Help a representative draft and validate a pack by hand | No — reference |
| `ark-tdd-unit` | Execute one test-driven build unit from a phase document | No — reference |
| `ark-session-log` | Write the sanitised session record, route transcripts locally | No — reference |
| `export-chatgpt-as-markdown` | Export one ChatGPT conversation to markdown | No — standalone tool |

## Writing a skill

One directory per skill, containing `SKILL.md` with YAML frontmatter:

```yaml
---
name: my-skill                 # kebab-case, matches the directory
description: One sentence...   # how an agent decides whether this applies
version: 1.0.0
author: ARK hackathon
license: CC0-1.0
tags: [ark, sources]
platforms: [linux]
triggers:                      # phrases that should surface it
  - add my organisation
  - what does ark know about
---
```

Below the frontmatter, write instructions for the agent: exact commands, what to
collect first, how to report results, and what it must not do. Be concrete —
give literal commands rather than describing them.

Two rules worth copying from the existing ARK skills:

**State what did not happen.** In a chat, "I've added your org" is heard as
"you're in and approved". If a skill leaves something staged, unapproved, or
unpublished, make it say so.

**Never let the agent substitute its own knowledge for the tool's output.** If a
tool refuses, the skill must instruct the agent to report the refusal. An answer
composed from general knowledge is indistinguishable from a sourced one and
worth far less.

## Installing on a Hermes agent

```
mkdir -p ~/.hermes/skills/ark
cp -r skills/ark-query skills/ark-add-organisation ~/.hermes/skills/ark/
hermes skills list | grep ark-        # confirm both show as enabled
hermes gateway restart                # required before Telegram sees them
```

Skills live in `~/.hermes/skills/<category>/<skill-name>/SKILL.md`. The category
directory is how they are grouped; ARK's use `ark`.

Repo-local skills are also possible via `hermes skills trust <path>`, which loads
`./.hermes/skills` for that project. That works when the agent runs inside the
checkout, but Telegram conversations are not scoped to a directory, so ARK
installs globally instead.

**Keep the repository copy authoritative.** Edit here, then reinstall. A skill
edited only on the host is lost on the next rebuild and invisible to everyone
else.

## The permission boundary these skills run under

The agent may read the ARK checkout and run `./scripts/query`,
`./scripts/digest`, and `./scripts/add-org`. It has no write access to the
canonical corpus, no ability to change its own configuration, and no push
credentials.

`add-org` **stages** an organisation. Staged organisations are not indexed and
appear in no answer. Admitting one into the live query pool requires
`./scripts/activate-org <id>`, which only runs with shell access on the host and
prompts for confirmation after showing the draft.

Shell access is the permission boundary. It needs no allowlist to maintain, no
identity plumbing, and no trust in the agent to enforce a rule about itself.
