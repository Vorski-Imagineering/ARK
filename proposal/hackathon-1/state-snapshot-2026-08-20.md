# ARK state snapshot — 2026-08-20

A factual record of where the ARK Agent stands after the two-day hackathon, written so that someone arriving cold — next week or next month, with none of the participants available — can tell what exists, what was decided, and what is blocked.

Role labels are used throughout. This repository is public and permanent. [see: AGENTS.md#2-sensitive-information-policy-highest-priority--non-negotiable]

---

## Infrastructure — live

| Component | State |
|---|---|
| Server | Live. Small European VPS with provider backups enabled. |
| Agent runtime | Installed and running. Hermes Agent v0.20.4. |
| Model access | One OAuth provider connected, valid into 2027. Gateway running. |
| Telegram bot | Live in the working group, mentions-only. No ambient monitoring. |
| Wildcard DNS | Live, pointing at the server. |
| Operator access | SSH provisioned for two operators using individual keys. |

## Infrastructure — not yet in place

| Component | State | Consequence |
|---|---|---|
| Second runtime profile | Not created. `profile list` shows one profile. | The planned split between a low-cost always-on profile and a frontier-intelligence profile does not exist. Everything runs on one model. |
| API keys | **None configured.** Every provider slot is unset. | No hosted embedding or generation API is reachable from the server. This is why embeddings are local by decision. [see: plan/ark-agent/decisions.md#d-3] |
| Version control on the server | No git repository exists anywhere in the agent's home directory. | Nothing the agent has produced is versioned or recoverable. A local working repository is the immediate next step, with the public repository connected afterwards. |
| Repository write access from the server | Read-only. The agent confirmed public read works; write authentication is unresolved. | The agent can read this repository but cannot open a pull request. Logged in the server's blocker file, owner: product lead. |
| Application code | None. | See below. |

## Application state

**No application code exists.** The build ledger is empty and Unit 0 is the next action. [see: plan/ark-agent/ledger.md]

The technical specification's §8 "Prepared vertical slice" — load a fixture, normalise, chunk, embed, index, query, answer, refuse, digest, show cost — was scheduled to be complete before Day 1. It was not built; the available time went into standing up infrastructure. Phase 1 Units 0 through 11 are that work, sequenced honestly rather than reported as behind. [see: proposal/hackathon-1/execution/05-technical-specification.md#8-prepared-vertical-slice]

## Agent identity

An identity file exists on the server and gives the agent a consistent voice and self-knowledge across sessions, which was the Phase 0 requirement. Its current content scopes the agent to a single individual as its user and instructs it to anonymise everyone else.

That scope conflicted with usage principle UP-U1, under which the agent's compute is for group work.

**Rewritten 2026-08-20.** The consequence was not theoretical. Asked in the group to add an organisation, the agent treated the request as a fact about a third party, researched the site by hand, and saved a memory note instead of running the corpus tooling — producing exactly the unsourced claim the corpus exists to prevent. The identity file now states that the agent serves the ARK group rather than one person, that participants are participants rather than topics, and that requests to add or query an organisation go through the corpus tooling. The previous file is retained as a timestamped backup on the host. The operating decision is to keep one profile and rewrite the identity file; whether the participant-facing ARK Agent eventually earns its own separate profile is recorded as an open question. [see: plan/ark-agent/open-questions.md]

Useful infrastructure the agent has built for itself and which the build track now adopts rather than duplicates:

- A structured blocker log with numbered entries, status, category, attempted fixes, and an owning role. The build protocol uses this file rather than inventing a second one.
- A daily, weekly, and monthly journalling structure.
- Local search scripts, after several search endpoints proved unreachable or captcha-gated from the server.

## Decisions ruled since Day 1

| Reference | Decision |
|---|---|
| D-1 | Build specifications live in `plan/ark-agent/`, honouring the standing rule against adding planning files elsewhere. |
| D-2 | Application code follows the repository shape already set out in the technical specification. |
| D-3 | Embeddings run locally with no API key. |
| D-4 | Phase numbering follows the working document, with an explicit mapping to the vision document's different numbering. |
| D-5 | Conversation logs are hybrid: raw transcripts stay local, only sanitised summaries are published here. Resolves working-document open decision §2. |
| D-6 | Organisations plug in through repository source packs with machine-readable frontmatter. Resolves working-document open decision §3. |
| D-7 | Agent skills use `SKILL.md` with frontmatter. |
| D-8 | Test-driven development is the build method; tests are written in the specification, not by the implementing agent. |

Full reasoning for each is in `plan/ark-agent/decisions.md`.

## Still open and blocking

Four working-document decisions remain unruled, and three of them block Phase 3 entirely:

- **§4 cadence** — how often the agent speaks proactively. The working document marks Phase 3 "Requires group input before starting."
- **§5 voice** — neutral summariser or opinionated participant.
- **§6 memory persistence** — where structured long-term memory lives. Distinct from conversation logging, which D-5 settles.
- **Identity** — whether the participant-facing agent keeps the current shared profile or gets its own.

Several ownership roles from `00-start-here.md` are still unassigned, including the recovery custodian, who the access model requires to be a different person from the infrastructure owner. Until those are named, the technical readiness gate cannot be assessed.

The three agreed representative questions — the fixed acceptance set for the evaluation harness — have not been chosen. Phase 1's quality gate cannot run without them.

## Corrections to earlier records

`[CONTRADICTS: proposal/hackathon-1/execution/06-roles-and-readiness.md]` That document cites three GitHub Actions workflows that were removed from this repository on 2026-08-06 in commit `8247400`. Only `pages.yml` remains. The coordination guidance depending on those workflows is stale.

The Day 1 record listed a second runtime profile as pending. It was never created. This snapshot supersedes any reading of that table which assumed two profiles exist.

## Immediate next actions

1. Initialise a local working repository on the server so the agent's output is versioned.
2. Resolve repository write authentication so the agent can open pull requests.
3. Rewrite the identity file for group scope.
4. Run Phase 1 Unit 0 — scaffold and test harness.
5. Collect source packs from three organisations.
6. Choose the three representative questions.
7. Name the unassigned ownership roles, recovery custodian first.

---

*Snapshot taken 2026-08-20. Supersedes the Day 1 end-of-day status table in the hackathon working document where the two disagree.*
