> **Redacted for public publication.** This is the working record of the two-day
> hackathon session. Personal names have been replaced with role labels, and the
> private recording link and contact details have been removed, in line with the
> repository's sensitive-information policy.
> [see: AGENTS.md#2-sensitive-information-policy-highest-priority--non-negotiable]

# Hackathon Working Doc

*August 18, 2026 · Session participants: event lead, technical lead, product lead, and two contributors*

**Reference documents:**
- **[Vision doc](https://github.com/Vorski-Imagineering/ARK/blob/main/proposal/hackathon-1/arc-community-agent-vision.md)** — the product lead's full vision for the agent (long-term north star)
- **[Technical spec](https://github.com/Vorski-Imagineering/ARK/blob/main/proposal/hackathon-1/execution/05-technical-specification.md)** — the product lead's evidence-based technical sequencing
- **[Participant invitation](https://github.com/Vorski-Imagineering/ARK/blob/main/proposal/hackathon-1/execution/01-participant-invitation.md)** — canonical scope anchor for what we promised

---

## TL;DR

Day 1 stood up the foundation: Contabo VPS with Hermes installed, wildcard DNS on `*.ark.audax.earth`, a shared project inbox, SSH access provisioned for two operators, MiniMax connected to the first Hermes profile, and the bot live in Telegram in mentions-only mode (thanks to the technical lead working after the call). A contributor's second Hermes profile using their Claude Code Max seat is still to come. **Agent name and image are open — the product lead is working on this.**

Day 2 opens with the full roadmap now visible. The **[vision doc](https://github.com/Vorski-Imagineering/ARK/blob/main/proposal/hackathon-1/arc-community-agent-vision.md)** is the north star; the **[tech spec's](https://github.com/Vorski-Imagineering/ARK/blob/main/proposal/hackathon-1/execution/05-technical-specification.md)** evidence-based sequencing keeps us honest about what actually ships. The hackathon-scoped commitment is the **source-to-answer-to-digest** vertical slice (Phase 1). Everything beyond that is stretch or post-hackathon — buildable this weekend if the group has energy and dependencies clear, but not required to declare success.

**Portability** — that someone else can replicate our setup — is a first-principles consideration for every decision from here.

---

# Day 1 — What Happened

## What we accomplished today

**Infrastructure standing:**
- **VPS live:** Contabo €5/month + €2/month backups (auto snapshots to Contabo)
- **Hermes installed** on VPS by the technical lead
- **MiniMax connected** to the first Hermes profile (the technical lead's subscription)
- **Telegram bot live** in the ARK group, mentions-only mode
- **SSH access:** provisioned for two operators
- **Wildcard DNS:** `*.ark.audax.earth` pointing to VPS (via the product lead's AUDAX domain)
- **Shared email:** a shared project inbox created, forwards to the event lead and the product lead
- **Backup path considered:** Google Drive via cron job (the technical lead's pattern from a prior project, not yet implemented)

**Decisions locked:**
- Agent identity in Telegram is **mentions-only** — no ambient monitoring, no interjections into private conversations
- Two Hermes profiles will run on the same VPS: one on MiniMax (low-cost, always-on, ✅ live), one on Claude Code Max (frontier intelligence via a contributor's nonprofit seat, ⏳ to come)
- MiniMax first, everything else layered from there
- Aggregator/per-token APIs (OpenRouter, Groq free tier, etc.) rejected for now — cost predictability matters more than intelligence maximization at this stage

**Explored and parked:**
- **Groq (with Q) free tier** — tool-call limits (6k tokens/min ceiling) make it unusable for Hermes
- **Coasys (Holochain-based)** — genuinely interesting but too complex to set up for a 2-day hackathon. The event lead knows the main developer for Coasys / ADAM / AD4M and can bring them in later.
- **Buzz (buzz.xyz)** — the technical lead to spin up a relay in parallel on the VPS, but explicitly not on the critical path

## Current state (Day 1 EOD snapshot)

| Component | Status | Owner |
|---|---|---|
| VPS (Contabo) | ✅ Live | the event lead (billing) |
| Hermes install | ✅ Complete | the technical lead |
| MiniMax profile | ✅ Connected & live | the technical lead |
| Telegram bot | ✅ Live (mentions-only) | the technical lead |
| Claude Code Max profile | ⏳ Not yet connected | a contributor |
| DNS (`*.ark.audax.earth`) | ✅ Live | the product lead |
| Email (shared project inbox) | ✅ Live | the product lead |
| Agent name and image | ⏳ In progress | the product lead |
| GitHub repo access | ❌ Not connected | TBD |
| Identity/system prompt file | ❌ Doesn't exist yet | TBD |
| Conversation logging | ❌ Not configured | TBD (the technical lead likely primary) |
| Public source ingest pipeline | ❌ Not designed | TBD (group) |
| Tip jar / cost tracking | ❌ Not formalized | TBD |
| `SETUP.md` documentation | ❌ Not yet written | TBD |

---

# Day 2 — What We're Building

## The Day 2 shelf

**How to read this section:** each phase below is a *card on the shelf.* A phase has:
- A **goal** (what does this prove?)
- **Dependencies** (what must be true before starting)
- **Concrete buildable tasks** (what someone can actually pick up)
- **Definition of done** (what proves this phase is complete)
- **Scope tag** — `Committed` (invitation promise, must ship), `Stretch` (hackathon-buildable if capacity allows)

**How to work with the shelf during Day 2:** if something you're working on gets blocked or the group energy shifts, pick a different card whose dependencies are met. Don't wait — parallel work is welcome. Just don't start a card whose upstream isn't proven. Sequencing is the only rule.

**The full vision** is in **[the product lead's vision doc](https://github.com/Vorski-Imagineering/ARK/blob/main/proposal/hackathon-1/arc-community-agent-vision.md)** — read that for the deep "why." This shelf is the "what to build in what order."

### Phase 0 — Foundation `Committed` (mostly done)

**Goal:** the agent exists, is reachable, and has consistent self-knowledge.

**Dependencies:** none.

**Buildable tasks:**
- ✅ VPS provisioned (the event lead)
- ✅ Hermes installed (the technical lead)
- ✅ MiniMax connected (the technical lead)
- ✅ Telegram bot in ARK group, mentions-only (the technical lead)
- ⏳ A contributor's Claude Max Hermes profile (a contributor)
- ⏳ **Agent identity file** — a system prompt that gives the agent consistent self-knowledge across sessions. Lives in the repo. ~30 min task. Requires the product lead's name/image decision.
- ⏳ **GitHub repo access from VPS** — git clone + scheduled pull so agent can read the repo. ~30 min task.
- ⏳ **`SETUP.md`** — running document of every setup step (see Documented Setup section below).

**Definition of done:** an operator can ask the agent "what are we trying to prove?" and get an answer sourced from repo documents. Matches the product lead's tech spec's "definition of working after two hours" from the [2-hour bootstrap section](https://github.com/Vorski-Imagineering/ARK/blob/main/proposal/hackathon-1/execution/05-technical-specification.md).

### Phase 1 — Source-to-Answer-to-Digest vertical slice `Committed`

**Goal:** three organizations' public information can be queried together; the agent produces sourced answers and a cross-org digest that participating org reps can inspect for accuracy.

**This is the hackathon's core commitment.** Anchored directly in the product lead's [tech spec section 1](https://github.com/Vorski-Imagineering/ARK/blob/main/proposal/hackathon-1/execution/05-technical-specification.md) and the participant invitation.

**Dependencies:** Phase 0 complete + at least three source packs from participating orgs.

**Buildable tasks:**
- **Source pack template** — a markdown/YAML format for each org listing: profile, approved URLs, permission basis, 2-3 representative questions their reps would want the agent to answer. Uses [the product lead's source-pack template](https://github.com/Vorski-Imagineering/ARK/blob/main/proposal/hackathon-1/execution/02-participation-and-source-pack.md) as starting point.
- **Source loader** — reads markdown/text, selected public HTML pages, RSS/Atom entries. Simple Python starts fine.
- **Normaliser** — emits a common document record with stable provenance (URL, title, publication date, retrieval date, org identifier).
- **Chunker** — splits text while retaining heading and source metadata.
- **Retrieval index** — disposable local index (SQLite + embeddings, or the runtime's built-in file/source handling if it can pass the acceptance test).
- **Q&A with citation** — agent answers a question by retrieving from the index and citing the source URL for each material claim.
- **Cross-org digest** — agent produces a synthesis across multiple orgs' sources, with citations.
- **Representative review** — participating org reps inspect answers about their org and flag inaccuracies.

**Definition of done:** Three organizations' info can be queried together. The prototype creates a sourced digest. Representatives can inspect the evidence behind material claims. Matches the product lead's tech spec's Day 1 & Day 2 focus.

**What proves this before Phase 2 opens:** the digest is accurate enough that reps sign off on it. If accuracy fails, Phase 1 continues — do not layer on top of a broken foundation.

### Phase 2 — Conversational onboarding `Stretch`

**Goal:** a new person can arrive and be walked through what ARK is, what orgs participate, what they can do, in a conversation with the agent (not a static info dump).

**Dependencies:** Phase 1 proven (agent can answer sourced questions about orgs).

**Buildable tasks:**
- **Onboarding conversation flow** — agent asks: what brought you to ARK? Which themes interest you? What would you like to contribute? Which kinds of updates would be useful?
- **Registration capture** — record consent, permitted delivery channel, interests, update-frequency preference. Storage decision depends on Open Decision §2 (logging).
- **First-message welcome** — when someone new joins Telegram, agent detects and (with permission) starts conversation.

**Definition of done:** three people can be onboarded conversationally, end-to-end, and their preferences are stored.

**What proves this before Phase 3 opens:** onboarded people report the conversation felt useful, not scripted. If it feels like a form, keep iterating before adding proactive contact.

### Phase 3 — Ongoing member activation `Stretch`

**Goal:** the agent maintains rhythm with registered members based on their consented preferences.

**Dependencies:** Phase 2 (registration + preferences exist).

**Buildable tasks:**
- **Scheduled delivery** — daily/weekly summaries to registered members via their chosen channel (Telegram DM most likely).
- **Preference respect** — agent applies changes (frequency, interests, opt-out) before next delivery.
- **Interest-tailored updates** — the summary sent to a member reflects the interests they registered.
- **Prompt without pressure** — occasional invitations to participate (contribute, respond to a question) but not turning every update into engagement bait.

**Definition of done:** a member can register, choose weekly frequency + a specific interest, receive their first weekly summary shaped by that interest, change to daily, and receive a daily summary the next day.

**Important:** this phase is where the [cadence question](#4-cadence-beyond-reactive-how-often-does-the-agent-speak-proactively) gets answered. **Requires group input before starting.**

### Phase 4 — Cross-org synthesis with tech-stack awareness `Stretch`

**Goal:** the agent recognizes patterns across orgs' updates and can answer questions like "which orgs use tool X?" or "what pattern is emerging across regenerative networks?"

**Dependencies:** Phase 1 proven; at least three orgs' source packs live.

**Buildable tasks:**
- **Tech-stack extraction** — for each org, agent identifies (from their sources) what tools, models, protocols, and platforms they use. Stores structured tech-stack info per org.
- **Interoperability queries** — agent can answer "which orgs use tool X?" and "which pairs of orgs have overlapping stacks?"
- **Pattern detection** — agent identifies themes recurring across multiple orgs' updates.
- **Cross-org connection prompts** — agent surfaces when work in two orgs might benefit from a conversation (this borders on Phase 7 / the product lead's Phase 2 vision — start light).

**Definition of done:** the agent can answer three specific interoperability questions with sourced evidence about the participating orgs.

**Note:** this is the test use case the event lead proposed. It's a specific instance of the product lead's [vision section 4 (cross-org synthesis)](https://github.com/Vorski-Imagineering/ARK/blob/main/proposal/hackathon-1/arc-community-agent-vision.md) with a narrow, testable scope.

## Parallel experimental tracks (opt-in)

These aren't in the main phase sequence — they're experiments running alongside the shelf. Whoever's interested can spike them without blocking the main path.

**Track A — a contributor's parallel-tables federation approach**
- Explores whether Supabase-style tables can serve as a shared read/write substrate for agents at different intelligence levels to escalate queries to each other
- If it works, could be foundational for cost-conscious agent federation
- Explicitly not on hackathon critical path; the contributor rabbit-holes and comes back with a concrete proposal

**Track B — Buzz relay on VPS**
- The technical lead to set up a Buzz (buzz.xyz) relay on the VPS in parallel
- Different pattern than the ARK agent (workspace for many agents, not one shared agent), but worth having spun up for future exploration
- Not on critical path

**Track C — Coasys / ADAM / AD4M exploration**
- The event lead can call in the main developer if the group wants to explore multi-perspectival systems as a substrate direction
- Not for this hackathon, but the connection is available

## Open decisions requiring group input

Each decision below has context, options, and a recommendation where I have a strong view. Some are needed *before* certain phases can start — noted in each.

### 1. Agent name and image

**Context:** the product lead is working on both. The infrastructure names are set (`ark.audax.earth`, a shared project inbox), but the agent's user-facing name and avatar are still TBD. Any previous naming (ARC, Community Weaving Agent, Arco) is off the table.

**When needed:** Phase 0 completion (identity file).

**Options:** the product lead to propose; group to react.

**My (the drafting assistant's) recommendation:** Let the product lead drive this and bring options to the group. Low-stakes decision if we pick something workable and don't over-brand it.

### 2. Conversation logging — where and how?

**Context:** Hermes logs conversations by default in its own filesystem, but we need a formalized approach so logs are queryable, portable, and shared across profiles. The technical lead is the natural primary; a contributor's parallel-tables approach (Track A) is a secondary consideration that could layer on later.

**When needed:** Before serious cross-session memory use in Phase 1+.

**Options:**
- **Filesystem only** (default Hermes) — simplest, not queryable, not shareable across agent profiles
- **Skill that writes to markdown files in the repo** — CC0-friendly, git-versioned, portable to any future substrate
- **Skill that writes to a structured DB (SQLite on VPS or Supabase)** — queryable, structured, agent-independent
- **Hybrid** — filesystem for hot state, markdown-in-repo for canonical durability, optional DB layer later

**My (the drafting assistant's) recommendation:** The technical lead drives this as the primary technical call. My lean: hybrid — filesystem hot, markdown-in-repo canonical. Preserves portability without adding dependencies. A contributor's proposal (if compelling) can layer on later.

**Portability note:** whichever we choose, the log format itself should be simple enough (markdown, JSONL, or similar) to migrate to any future storage.

### 3. Public source ingestion — how do organizations plug in?

**Context:** Core question for Phase 1. Options range from "someone tells the agent a URL in Telegram" to "structured source pack in the repo."

**When needed:** Beginning of Phase 1.

**Options:**
- **Telegram-only for now** — orgs share links, feeds, or docs by @-mentioning the agent
- **Repo-based source pack** — each participating org submits a markdown file listing their public sources. Agent reads the repo on schedule. Uses [the product lead's source pack template](https://github.com/Vorski-Imagineering/ARK/blob/main/proposal/hackathon-1/execution/02-participation-and-source-pack.md).
- **Structured onboarding flow via the agent** — user says "I want to add my org," agent walks them through it

**My (the drafting assistant's) recommendation:** **Repo-based source pack** for Phase 1 — matches the product lead's tech spec, is portable, is versioned, is transparent. The conversational onboarding (option 3) is a Phase 2 target.

### 4. Cadence beyond reactive — how often does the agent speak proactively?

**Context:** The bot is mentions-only. Phase 3 introduces proactive contact. Cadence needs group input before Phase 3 can start.

**When needed:** Before Phase 3.

**Options:**
- **Reactive only** — safest, least noise, limits value
- **Scheduled digest** — daily or weekly synthesis at fixed time
- **Event-triggered** — posts when a threshold is crossed
- **Hybrid** — scheduled + event-triggered

**My (the drafting assistant's) recommendation:** **Explicitly a group decision.** Prior view holds: start reactive, add proactive later once we have proof the agent says useful things.

### 5. Opinion vs. summarize — what's the agent's voice?

**Context:** The agent could be neutral (report what happened) or opinionated (add signal, engage). Different agents.

**When needed:** Before Phase 3 (proactive delivery makes voice more consequential).

**Options:**
- Neutral summarizer
- Opinionated participant
- Neutral by default, opinionated when explicitly asked

**My (the drafting assistant's) recommendation:** **Start neutral, evolve later.** A neutral agent that surprises with utility beats an opinionated agent that annoys early. Group input on this ultimately, but I have a strong lean.

### 6. Memory persistence — where does long-term memory live?

**Context:** Beyond raw conversation logs (§2), the agent accumulates structured memory: what orgs are, what's been decided, what's been tried.

**When needed:** Phase 2+ (registration + preferences), Phase 4 (structured tech-stack data).

**Options:**
- Filesystem on VPS
- Git repo
- Structured DB
- Hybrid (VPS hot, repo canonical, optional DB for querying)

**My (the drafting assistant's) recommendation:** **Group decision.** My default: repo as canonical source of truth (portability wins), with VPS as working cache. DB layer only if a contributor's Track A proves valuable.

### 7. Tech-stack awareness as a test use case

**Context:** The event lead proposed the agent understand each participating org's tech stack for interoperability. Concrete, testable, valuable. See Phase 4 above.

**When needed:** Beginning of Phase 4.

**My (the drafting assistant's) recommendation:** **Group approval sought tomorrow.** Minimal version is a good hackathon test case if Phase 1 completes with time to spare.

## Proposed design principles (for team ratification)

**These are proposed, not decided.** Team to ratify, amend, or reject at the start of Day 2.

**Portability principles:**

- **UP-P1 · All configuration in the repo** — never in someone's head, never only on the VPS. Environment variables in `.env.example` with dummy values.
- **UP-P2 · Setup process documented as you go** — every command gets captured in `SETUP.md`. Someone should be able to spin up their own equivalent in an afternoon.
- **UP-P3 · Substrate choices reviewable** — Contabo is fine but the setup should work on Hetzner, DigitalOcean, self-hosted, or anywhere else. No Contabo-specific dependencies.
- **UP-P4 · LLM subscription is a soft dependency, not hard** — the pattern should work with any subscription that Hermes supports. Someone replicating us shouldn't need MiniMax specifically.
- **UP-P5 · Data formats simple and portable** — markdown, JSONL, or similar. Even if we use a DB, the export format should be trivial.
- **UP-P6 · CC0 by default** — all code, configs, and documentation. Someone should be able to fork this without a legal conversation.
- **UP-P7 · Bus factor > 1 on every dependency** — multiple people should have credentials, know the setup, and be able to run recovery.

**Usage & scope principles:**

- **UP-U1 · The agent's compute is scoped to group work only.** Shared VPS + shared LLM subscriptions must not be used by any individual for personal or unrelated work. Enforcement: (a) explicit system-prompt guardrails, (b) visible logs so misuse is discoverable, (c) soft social norm reinforced in onboarding.
- **UP-U2 · Rate limits per user** — no single person monopolizes shared quota. Concrete limits TBD.
- **UP-U3 · Transparent usage** — running tally of who's calling the agent how much, visible to the group. Makes UP-U1 and UP-U2 self-enforcing.

**Portability audit for Day 2:** at end of Day 2, ask: "if all our infrastructure evaporated tomorrow, how quickly could someone replicate it?" That's the test.

## Documented setup (`SETUP.md`)

A living doc that captures every step of standing up the agent from scratch. Someone else — even next month, even without any of us involved — should be able to follow it end to end.

**Proposed structure for `SETUP.md`:**

1. **Prerequisites** — accounts, credentials, tools you need before starting
2. **VPS provisioning** — Contabo instructions with alternatives noted
3. **DNS setup** — wildcard DNS pattern for `*.your-domain`
4. **Email forwarding** — shared inbox for account signups
5. **SSH access** — key management for multiple contributors
6. **Hermes install** — step-by-step
7. **LLM connection** — MiniMax pattern; alternatives (Claude Max, ChatGPT Plus, local models) noted
8. **Telegram bot creation** — @BotFather flow, mentions-only configuration
9. **Repo connection** — git clone on VPS + scheduled pull
10. **Identity file** — where the agent's system prompt lives, what belongs in it
11. **Conversation logging** — depends on Open Decision §2
12. **Backup strategy** — Google Drive cron pattern from the technical lead's work on a prior project
13. **Rotation & recovery** — how to rotate credentials, how to recover from VPS loss
14. **Rate limits & usage scoping** — how UP-U1/U2/U3 are enforced technically

**Ownership:** whoever does a setup step captures it in-flight. The technical lead owns technical steps; the product lead owns domain/email; the event lead owns billing/VPS/SSH. No writing "later" — writing happens as it happens.

## Immediate next steps (Day 2 opening)

**Ordered by dependency, most-blocking first:**

1. **The product lead:** Share proposed agent name and image → group reacts (5 min)
2. **Group:** Ratify (or amend) proposed design principles UP-P1–P7 and UP-U1–U3 (10 min)
3. **Group:** Walk through open decisions §2–§7, decide what we're doing for Phase 1 (20 min)
4. **A contributor:** Create second Hermes profile with Claude Code Max seat → add to Telegram
5. **The technical lead (primary):** Implement conversation logging based on group decision §2
6. **Someone:** Create identity/system prompt file in the repo
7. **Someone:** Connect agent to GitHub repo (git clone + scheduled pull)
8. **Someone:** Begin `SETUP.md` capture from what's already been done
9. **Group:** Formalize tip jar mechanics + usage scope agreement (UP-U1–U3)
10. **Group (or subgroup):** Start Phase 1 — source pack template + first source pack from a willing org
11. **A contributor (secondary track):** Parallel-tables research spike
12. **The technical lead (background):** Buzz relay setup on VPS

## Tomorrow's agenda (proposed)

Suggested structure — refine at the top of Day 2:

1. **5 min:** The product lead shares agent name and image → group reacts
2. **10 min:** Group ratifies (or amends) proposed design principles
3. **20 min:** Group walks through open decisions §2–§7, decides for Phase 1
4. **10 min:** Portability audit — what's captured in `SETUP.md` so far, what still needs writing, who's writing what
5. **Rest of session:** Building. Whoever is closest to a task, drives it. Use the phase shelf. Sequencing is the only rule.

At end of day: retrospective (30 min) — what worked, what didn't, what we prove-tested, what phase is done vs blocked. Decide what pilot (if any) deserves continuation.

## Honoring the chaos

Hackathons are chaotic and that's fine. Some things to hold in mind:

- **Parallel work is welcome.** Multiple phases and tracks can progress simultaneously. Just don't start a Phase whose upstream Phase isn't proven.
- **Discoveries reshape plans.** If someone finds a better path, we adjust — the doc updates as we learn.
- **Blockage is a signal to move.** If your current work is blocked (waiting on another person, waiting on a decision, stuck on a bug), don't wait. Pick a different card whose dependencies are met.
- **Stretch is real.** Five people plus AI agents can do more in a day than expected. If Phase 1 lands early, keep going. But the invitation-scoped commitment (Phase 1) is the floor; stretch is the ceiling.
- **What matters is what ships.** Fanciness in the vision doesn't matter if the vertical slice doesn't work. Prove Phase 1, then earn each addition by evidence.

---

# Beyond Day 2 — Post-Hackathon Roadmap

These phases are explicitly **not** hackathon deliverables. They're the roadmap for what comes after Phase 1 (and any stretch phases) prove out. Referenced here so the whole picture stays visible and so the group can point at them when deciding what to explore next.

## Continuation of the shelf

### Phase 5 — Public build-in-public feed `Post-hackathon`

**Goal:** the agent publishes ARK's collective activity externally on a rhythm.

**Dependencies:** Phase 1 + Phase 4 proven.

**Buildable tasks:**
- **Publishing rhythm** — decide daily vs weekly cadence and format
- **Public personality** — the voice ARK uses externally
- **Distribution channel** — website update, RSS feed, or social post
- **Accuracy gate** — publishing goes through org rep review before external distribution

**Definition of done:** an external person can subscribe to ARK's public feed and receive genuine, sourced updates about what the community is doing.

### Phase 6 — Cost & funding accounting `Post-hackathon`

**Goal:** the agent tracks its own operating costs transparently and manages contribution requests (with human approval).

**Dependencies:** Phase 1 + Phase 3 (needs registered members to request contributions from).

**Buildable tasks:**
- **Token/cost tracking** — model, input tokens, output tokens, estimated cost per generation
- **Contribution ledger** — dated entries for pledges, confirmations, disbursements
- **Runway forecast** — current balance + burn rate = runway estimate
- **Low-funds alerts** — when runway crosses threshold, agent drafts contribution request; human approves and sends
- **Stop-spend threshold** — if reached, agent suspends non-essential paid activity

**Definition of done:** agent reports accurate cost + runway on request. Test alert triggers correctly (with mock threshold). Matches [the product lead's vision section on cost/funding accounting](https://github.com/Vorski-Imagineering/ARK/blob/main/proposal/hackathon-1/arc-community-agent-vision.md).

**Note:** the shared-cost norm (design principle UP-U1) is needed *before* the hackathon starts using shared quota, even though the automation of Phase 6 is post-hackathon.

### Phase 7 — Alignment suggestions (the product lead's "Phase 2 vision") `Post-hackathon`

**Goal:** the agent uses updates and consented member context to suggest possible alignments and worthwhile conversations.

**Dependencies:** Phases 1-4 solid; consent architecture proven.

**Not for this hackathon.** This is a whole product surface — matchmaking, consent management, evidence-based suggestions, feedback loops. Genuinely valuable but its own Phase 2 event.

### Phase 8 — Inter-organizational agent network `Post-hackathon (long horizon)`

**Goal:** each org runs its own agent; agents federate updates; ARK maintains network-level view.

**Explicitly the longer-term vision.** Referenced from [the product lead's vision section 8](https://github.com/Vorski-Imagineering/ARK/blob/main/proposal/hackathon-1/arc-community-agent-vision.md).

---

*Doc drafted Aug 18 EOD. To be updated after each session with what shifted, what was decided, and what remains open. Reference documents (invitation, vision, tech spec) are linked at the top — read them for the full context.*
