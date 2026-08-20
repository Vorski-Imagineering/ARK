# Shared agent skills

Reusable capabilities an AI collaborator can pull in to do a specific job
consistently. Each skill is a directory containing `SKILL.md` with frontmatter.

| Skill | What it does | Installed on the ARK agent |
|---|---|---|
| `ark-query` | Answer questions from the ARK corpus with citations; generate the digest | Yes |
| `ark-add-organisation` | Capture an organisation's public pages, draft its source pack, reindex | Yes |
| `ark-source-pack` | Help a representative draft and validate a pack by hand | No — reference |
| `ark-tdd-unit` | Execute one test-driven build unit from a phase document | No — reference |
| `ark-session-log` | Write the sanitised session record, route transcripts locally | No — reference |
| `export-chatgpt-as-markdown` | Export one ChatGPT conversation to markdown | No — standalone tool |

## Installing on a Hermes agent

```
mkdir -p ~/.hermes/skills/ark
cp -r skills/ark-query skills/ark-add-organisation ~/.hermes/skills/ark/
hermes skills list | grep ark-
hermes gateway restart
```

The agent needs read access to the ARK checkout and permission to run
`./scripts/query`, `./scripts/digest`, and `./scripts/add-org`. It needs nothing
else — no write access to the canonical corpus, no ability to change its own
configuration, no push credentials. That boundary is deliberate and is the
access model the technical specification sets out.

## The rule these skills share

Both ARK skills instruct the agent to report a refusal as a refusal rather than
answering from its own knowledge. The corpus is only worth having because every
claim traces to a public source someone can open. An answer composed from
general knowledge looks identical to a sourced one and is worth far less.
