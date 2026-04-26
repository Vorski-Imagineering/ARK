# CoCo - Branch · OpenClaw vs Hermes Agents

## You

Give me a clear analysis of the similarities and differences between openclaw and Hermes agents 

Include a section on ability to run multiple instances on one server

Add a section on connection to memory systems

Add a section on ability to use multiple models for token cost optimization

---

## Assistant

I’ll treat this as an architecture comparison for CoCo-style agent infrastructure, not a generic “which mascot is shinier” survey. I’ll verify current docs first, because agent frameworks mutate faster than deployment diagrams.

---

## Assistant

A useful distinction is emerging: OpenClaw is more “multi-agent routing in one gateway,” while Hermes is more “profile-isolated agents plus strong learning/memory loops.” That difference matters more for CoCo than raw feature count.

---

## Assistant

Assumption: by **OpenClaw** you mean the open-source personal AI assistant / gateway project, and by **Hermes agents** you mean **Nous Research’s Hermes Agent**.


## Executive take


For **CoCo**, I would lean **Hermes** if the priority is long-running learning, memory providers, model routing, and multiple isolated agent profiles. I would lean **OpenClaw** if the priority is a single always-on gateway that routes many channels, people, accounts, and agent personas from one operational control plane.


My pushback: do **not** let either framework become CoCo’s source of truth. CoCo needs participant profiles, consent, journey state, session transcripts, facilitator-visible records, and structured collective memory. That should live in your own database/RAG layer, with the agent runtime as orchestration and interface. The CoCo brief explicitly requires navigation, Q&A, people discovery, between-session prompts, role clarity, consent-aware profiles, and facilitator oversight, not just a clever autonomous bot. CoCo_ Coherence Companion AI Ag…




---


## Similarities


Both are self-hostable, channel-connected agent runtimes designed for “agent with tools” use cases rather than simple chatbot wrappers.


**OpenClaw** positions itself as a personal AI assistant running on your devices, reachable through channels like WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, Microsoft Teams, Matrix, WeChat, and others. Its gateway is described as the control plane for sessions, channels, tools, and events. [GitHub](https://github.com/openclaw/openclaw)


**Hermes** positions itself as an autonomous server-resident agent that “grows” over time, with persistent memory, auto-generated skills, scheduled automations, subagent delegation, multi-platform messaging, and support for many inference providers. [Hermes Agent](https://hermes-agent.nousresearch.com/docs)


In practice, both give you:


| Capability | OpenClaw | Hermes |
| --- | --- | --- |
| Messaging gateway | Strong | Strong |
| Tool execution | Strong | Strong |
| Skills/procedural extensions | Strong | Strong |
| Persistent memory | Strong | Very strong |
| Multi-model support | Strong | Very strong |
| Multi-agent/multi-person setup | Strong single-gateway routing | Strong profile isolation |
| Local/self-hosted operation | Yes | Yes |
| Production suitability for CoCo | Needs external app/data layer | Needs external app/data layer |


---


## Core differences


### 1. Architectural center of gravity


**OpenClaw is gateway-first.** Its strongest pattern is one gateway routing messages from many channels/accounts/peers into isolated agents. The docs define an OpenClaw agent as a scoped “brain” with its own workspace, state directory, auth profiles, model registry, config, and session store. The same gateway can host one or many agents side by side. [OpenClaw](https://docs.openclaw.ai/concepts/multi-agent)


**Hermes is learning-agent-first.** It emphasizes a closed learning loop: persistent memory, autonomous skill creation, skill improvement, session search, user modeling, subagents, scheduled jobs, and research/evaluation affordances. [GitHub](https://github.com/nousresearch/hermes-agent)


For CoCo: OpenClaw maps more naturally to **many participants/channels/agent personas**. Hermes maps more naturally to **a long-lived companion that accumulates context and improves its procedures**.


---


### 2. Product orientation


OpenClaw is closer to an **always-on personal/team assistant gateway**. Its own README says the product is the assistant, with the gateway as the control plane, and frames the ideal use case as a “personal, single-user assistant that feels local, fast, and always-on.” [GitHub](https://github.com/openclaw/openclaw)


Hermes is closer to an **agent operating system / autonomous worker**. It exposes CLI, messaging, terminal backends, subagents, cron, memory, skills, research trajectories, and model-provider abstractions. [Hermes Agent](https://hermes-agent.nousresearch.com/docs)


For CoCo: if you are building a cohort-facing journey guide, neither product orientation is perfect. You want a **journey-state machine plus agent interface**, not an unconstrained autonomous assistant wandering through your participant data with a candle and a shell prompt.


---


## Ability to run multiple instances on one server


### OpenClaw


OpenClaw is strong here.


It supports **multiple isolated agents inside one running Gateway**, with inbound routing through bindings. Each agent can have its own workspace, state directory, auth profiles, model registry, config, and sessions. [OpenClaw](https://docs.openclaw.ai/concepts/multi-agent)


It also explicitly supports **multiple gateways on the same host**, but recommends using one gateway unless you need stronger isolation or redundancy. If running multiple gateways, each instance needs unique config, state directory, workspace root, gateway port, and derived browser/canvas/CDP ports. [OpenClaw](https://docs.openclaw.ai/gateway/multiple-gateways)


**Implication:** OpenClaw gives you two deployment patterns:


1. 
**One Gateway, many agents**: good for CoCo personas, channels, cohorts, or participant routing.
2. 
**Many Gateways, isolated profiles/ports**: good for tenant-level isolation, staging/prod separation, or rescue/admin bots.


For CoCo, the first pattern is attractive, but you still need strong application-level tenancy. Agent workspace isolation is not the same as privacy isolation.


### Hermes


Hermes is also strong, but with a different model.


Hermes supports **profiles** for running multiple independent agents on the same machine. Each profile gets its own config, API keys, memory, sessions, skills, cron jobs, gateway state, and state database. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/profiles/)


Each Hermes profile can run its own gateway as a separate process with its own bot token, and installed services are named per profile so they run independently. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/profiles/)


Hermes also allows multiple users to interact with the same Hermes instance via messaging platforms, with access controlled by allowlists and DM pairing. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/faq)


**Implication:** Hermes is better if you want **one agent profile per role/persona/cohort**, with clean state separation. OpenClaw is better if you want **one gateway process to route many channels/accounts/peers into agent personas**.


**My judgment:**

For a CoCo MVP with 15-30 seed participants, Hermes profiles are cleaner for isolated experiments. For later ecosystem-scale deployment with many channels and routing rules, OpenClaw’s gateway model becomes more compelling.


---


## Connection to memory systems


### OpenClaw


OpenClaw uses explicit file-backed memory in the agent workspace. Its docs say the model only remembers what is saved to disk, with `MEMORY.md` for durable facts, daily notes under `memory/YYYY-MM-DD.md`, and optional `DREAMS.md` for consolidation review. [OpenClaw](https://docs.openclaw.ai/concepts/memory)


It also provides `memory_search` and `memory_get`, supports hybrid search when embeddings are configured, and supports multiple memory backends: built-in SQLite, QMD, and Honcho. [OpenClaw](https://docs.openclaw.ai/concepts/memory)


OpenClaw also has optional “dreaming,” a background consolidation pass that scores short-term signals and promotes qualified items into long-term memory. [OpenClaw](https://docs.openclaw.ai/concepts/memory)


**Strength:** transparent local memory, readable files, useful for human audit.

**Weakness:** for CoCo, markdown memory is not enough. Participant consent, profile fields, visibility rules, facilitator notes, and cohort-level memory require a structured database.


### Hermes


Hermes has built-in bounded curated memory via `MEMORY.md` and `USER.md`, injected into the system prompt at session start. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)


Hermes goes further with external memory provider plugins. It ships with eight external memory provider plugins, only one active at a time, while built-in memory remains active. When a provider is active, Hermes injects provider context, prefetches relevant memories, syncs conversation turns, extracts memories on session end, mirrors built-in writes, and adds provider-specific tools. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers)


Supported providers include Honcho, Mem0, Hindsight, Holographic, RetainDB, ByteRover, Supermemory, and OpenViking according to the current docs. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers)


**Strength:** stronger memory-provider story, more suitable for experimentation with user modeling and cross-session recall.

**Weakness:** external memory providers can become opaque. CoCo needs explainability, consent, deletion, and facilitator review. A seductive memory system without governance is just surveillance with nicer shoes.


**My judgment:**

Hermes is ahead for plug-in memory architecture. OpenClaw is simpler and more inspectable. For CoCo, use either only as a **memory client**, not the memory authority. Recommended memory architecture:


```
Postgres  participants  consent_rules  journey_state  session_attendance  reflections  facilitator_flags  public_profile_fields  private/admin fieldsVector store / pgvector  source docs  session transcripts  approved knowledge base  public cohort memory  per-user permitted memoriesAgent runtime  OpenClaw or Hermes  retrieval tools only  no uncontrolled durable writes
```


---


## Ability to use multiple models for token cost optimization


### OpenClaw


OpenClaw has a clear model-selection and fallback mechanism. It selects a primary model first, then configured fallbacks, with provider auth failover happening inside a provider before moving to the next model. [OpenClaw](https://docs.openclaw.ai/models)


It also supports per-agent model overrides, image/PDF/media-specific model settings, session-level model switching via `/model`, model allowlists, model fallbacks, and OpenRouter free-model scanning. [OpenClaw](https://docs.openclaw.ai/models)


The docs explicitly recommend using fallbacks for cost/latency-sensitive tasks and lower-stakes chat, while avoiding weak models for tool-enabled agents or untrusted inputs. [OpenClaw](https://docs.openclaw.ai/models)


**Cost optimization pattern in OpenClaw:**


| Task | Model tier |
| --- | --- |
| Onboarding FAQ | cheap/fast model |
| RAG answer with citations | mid-tier model |
| Sensitive commitment/consensus support | stronger reasoning model |
| Summarization/transcript cleanup | cheap long-context model |
| Tool-heavy actions | stronger model with reliable tool use |


### Hermes


Hermes has a broader cost-optimization surface.


It supports multiple inference providers, including OpenRouter, Anthropic, OpenAI/Codex, GitHub Copilot, AI Gateway, z.ai/GLM, Kimi/Moonshot, custom OpenAI-compatible endpoints, Ollama, and vLLM. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/integrations/providers)


Hermes supports fallback models for CLI and messaging gateway sessions, while auxiliary tasks use separate lightweight models and their own provider resolution chain. Auxiliary tasks include vision, web extraction, compression, session search, memory flush, approval classification, and title generation. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers)


Hermes also supports OpenRouter provider routing, including sorting providers by price, throughput, or latency. That gives a direct mechanism for cost-first routing when using OpenRouter. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)


**Cost optimization pattern in Hermes:**


| Task | Model strategy |
| --- | --- |
| Main conversation | reliable mid/high-tier model |
| Memory flush | cheap auxiliary model |
| Session search summary | cheap auxiliary model |
| Transcript compression | cheap long-context model |
| Browser/vision | vision-specific auxiliary model |
| High-stakes synthesis | manually route to stronger model |
| High-volume dev/testing | OpenRouter sorted by price |


**My judgment:**

Hermes is stronger for token cost optimization because auxiliary model routing is more explicit and task-specific. OpenClaw supports solid primary/fallback/per-agent model selection, but Hermes has a more developed “side tasks should not use the expensive brain” architecture.


---


## CoCo-specific fit


CoCo’s MVP needs journey navigation, Q&A, people discovery, reflection prompts, role clarity, and facilitator-visible escalation. It also has explicit success criteria around participant clarity, engagement, correct answers, connection formation, and reduced facilitator admin. CoCo_ Coherence Companion AI Ag…




### OpenClaw fit


**Good for:**


- 
Multi-channel participant access.
- 
One gateway routing different participants, groups, or channels.
- 
Agent personas such as Navigator, Connector, Facilitator, Agreements Steward.
- 
Operationally simple deployment if one server runs many channel integrations.


**Watch-outs:**


- 
Single gateway can become a blast-radius problem.
- 
File/workspace memory is not enough for consentful participant data.
- 
Skills/extensions increase security surface.
- 
You will need your own participant database and admin dashboard anyway.


### Hermes fit


**Good for:**


- 
Long-lived companion behavior.
- 
Rich memory-provider experimentation.
- 
Multiple isolated profiles on one server.
- 
Auxiliary model routing for token cost control.
- 
Subagents for research/summarization/pattern extraction.
- 
Cleaner “agent per context” development flow.


**Watch-outs:**


- 
Profile-per-agent is clean, but many profiles/gateways can become operationally noisy.
- 
The learning loop should be constrained for CoCo. You do not want agents autonomously rewriting participant-facing procedures without review.
- 
Memory-provider sophistication creates governance burden.


---


## Recommended architecture for CoCo


I would not choose “OpenClaw vs Hermes” as the whole architecture. I would choose:


```
CoCo App Layer  Web chat / Telegram / WhatsApp / admin dashboard  Auth, consent, cohort routingCore Data Layer  Postgres + pgvector  Journey state  Participant profiles  Consent matrix  Session transcripts  Facilitator flags  Cohort memoryAgent Runtime  Hermes for MVP if memory/model-cost optimization is priority  OpenClaw if multi-channel gateway routing is priorityModel Router  Cheap model: FAQs, summaries, reminders  Mid model: standard RAG answers  Strong model: facilitation, commitments, ambiguity, conflict  Human escalation: consent, equity, conflict, sensitive commitments
```


## Bottom line


For **CoCo MVP**, I would choose **Hermes** unless your immediate deployment requirement is heavy multi-channel routing through a single gateway. Hermes gives you stronger memory-provider integration, cleaner profile isolation, better auxiliary-model cost optimization, and more explicit support for subagents and learning loops.


For **CoCo as ecosystem infrastructure**, keep an eye on **OpenClaw**. Its single-gateway multi-agent routing model may become valuable when CoCo needs many participant groups, channels, cohorts, and AI personas running from one operational substrate.


The sober answer: **Hermes for the first brain, OpenClaw for the nervous system later.**

---

## You

**Implication:** Hermes is better if you want **one agent profile per role/persona/cohort**, with clean state separation. OpenClaw is better if you want **one gateway process to route many channels/accounts/peers into agent personas**.

Explain this in more depth, research links and give me articles on this, it feels like the key differention.

---

## Assistant

You’re right to zoom in on this — the **real differentiation is not “features”**, it’s *how the agent thinks about itself over time*. That’s where OpenClaw and Hermes quietly diverge in ways that matter a lot for CoCo.


I’ll go deeper on the three dimensions you implicitly pointed at:


1. 
**Memory philosophy (file-based vs evolving cognitive loop)**
2. 
**Agent lifecycle (router vs self-developing organism)**
3. 
**Model orchestration (fallback vs task-specialized cognition)**


Then I’ll give you concrete articles/docs to read and how they map to your architecture decisions.


---


# 1. The deepest difference: memory is not storage — it’s identity


## OpenClaw: memory as **structured persistence**


OpenClaw treats memory like a **filesystem + retrieval layer**:


- 
`MEMORY.md` → curated facts
- 
daily logs → short-term traces
- 
optional embeddings → search
- 
optional “dreaming” → consolidation pass


This is basically:


> 
> “Store things. Retrieve them when needed. Occasionally summarize.”
> 
> 
> 


This is **explicit, inspectable, controllable** — and that’s a big deal.


But here’s the limitation:


👉 The agent does **not fundamentally change how it thinks** based on memory

It just **has more context to reference**


So the loop looks like:


```
User input → retrieve memory → respond → optionally write memory
```


That’s not learning. That’s *augmented recall*.


---


## Hermes: memory as **ongoing cognitive evolution**


Hermes is closer to:


> 
> “The agent is continuously rewriting its own operating manual.”
> 
> 
> 


Its memory system is not just storage — it’s **part of the reasoning loop**:


- 
Built-in memory (`MEMORY.md`, `USER.md`) injected into prompt
- 
External memory providers (Mem0, Hindsight, etc.)
- 
Memory extraction at end of sessions
- 
Session search + compression
- 
Memory-aware tool usage
- 
Skills generated *from experience*


The loop becomes:


```
User interaction→ reasoning→ memory extraction→ memory restructuring→ skill creation/update→ future behavior changes
```


That’s a **closed learning loop**.


---


## Why this matters for CoCo


Your product explicitly requires:


- 
evolving participant understanding
- 
pattern detection across people
- 
journey progression awareness
- 
facilitation memory across sessions


This is not just “remembering facts” — it’s **tracking transformation**.


From your doc:


> 
> “The app reads these signals and reflects the living pulse of coherence in real time” Coherence App Concept
> 
> 
> 
> 
> 


That’s Hermes territory.


OpenClaw can *store* that data

Hermes can *internalize* that data


But here’s the catch:


👉 Hermes will happily internalize things you should **not let it internalize**


Which brings us to the real architectural constraint:


---


## Critical insight (most people miss this)


For CoCo:


> 
> **Neither system should own the “truth” of participant memory**
> 
> 
> 


Because you need:


- 
consent boundaries
- 
facilitator visibility
- 
reversibility (delete/edit memory)
- 
structured roles + commitments
- 
auditability


Your system requires:


```
Agent memory = derived / ephemeralApp memory = canonical / governed
```


So Hermes is powerful — but dangerous if you let it become the source of truth.


---


# 2. Agent lifecycle: router vs organism


## OpenClaw = **orchestration layer**


Think:


> 
> “A gateway that routes inputs to agent personas”
> 
> 
> 


- 
multiple agents
- 
multiple channels
- 
shared runtime
- 
strong operational control


Agents are:


- 
scoped
- 
static-ish
- 
configured


This is great for:


- 
many users
- 
many contexts
- 
predictable behavior


---


## Hermes = **self-developing agent**


Think:


> 
> “An agent that evolves through experience”
> 
> 
> 


Capabilities:


- 
skill generation
- 
skill improvement
- 
subagents
- 
cron jobs
- 
research loops
- 
model switching mid-task


It behaves more like:


```
Agent → builds tools → uses tools → improves tools
```


This is closer to:


- 
AutoGPT-style evolution
- 
tool-learning agents
- 
internal procedural memory


---


## Why this matters for CoCo


Your CoCo agent has roles like:


- 
Navigator
- 
Connector
- 
Facilitator
- 
Agreements Steward CoCo_ Coherence Companion AI Ag…


These are not static personas — they are **contextual modes**.


So the question is:


👉 Do you want:


A) Many agents, each fixed role (OpenClaw style)

B) One agent that shifts roles dynamically (Hermes style)


---


### My honest take


For CoCo:


- 
Early stage → **Hermes-style single evolving agent**
- 
Later stage → **OpenClaw-style routing across personas + channels**


Because:


- 
You need coherence in tone and memory early
- 
You need scaling and routing later


---


# 3. Model orchestration: cost optimization vs cognitive specialization


## OpenClaw: **fallback and routing**


- 
primary model
- 
fallback models
- 
per-agent overrides
- 
manual switching


This is:


> 
> “If expensive fails, use cheaper”
> 
> 
> 


or


> 
> “Use different models per agent”
> 
> 
> 


It’s practical, but relatively coarse.


---


## Hermes: **task-level model specialization**


Hermes separates:


### Main cognition


- 
reasoning
- 
conversation


### Auxiliary cognition


- 
memory extraction
- 
summarization
- 
search compression
- 
classification
- 
vision


Each can use different models.


So instead of:


```
1 model does everything
```


You get:


```
cheap model → summarizecheap model → extract memorymid model → search contextstrong model → respond
```


This is a **cognitive pipeline**, not just fallback.


---


## Why this matters for CoCo


Your system will generate:


- 
session transcripts
- 
reflections
- 
summaries
- 
facilitator insights
- 
participant matching
- 
Q&A responses


If you use one model for everything:


💸 You will burn money fast


If you use Hermes-style orchestration:


💡 You can reduce cost 5–20x while increasing quality


---


# 4. The real hidden differentiation


Here’s the cleanest way to think about it:


| Dimension | OpenClaw | Hermes |
| --- | --- | --- |
| Memory | Stored context | Evolving cognition |
| Identity | Config-defined | Experience-defined |
| Learning | Minimal | Continuous |
| Control | High | Medium |
| Predictability | High | Medium |
| Cost optimization | Basic routing | Task-level optimization |
| Risk | Low drift | High drift |


---


# 5. What you should read (curated, high-signal)


These are not random links — these are the exact areas that matter for your architecture decisions.


---


## Hermes (Nous Research)


- 
Nous Research Hermes Agent docs

Focus on:


  - 
memory providers
  - 
skills system
  - 
auxiliary models
  - 
profiles


Search:


- 
“Hermes agent memory providers Nous”
- 
“Hermes agent skills generation Nous”
- 
“Hermes auxiliary models routing”


---


## OpenClaw


- 
OpenClaw docs


Focus on:


- 
gateway architecture
- 
multi-agent routing
- 
memory system
- 
model failover


Search:


- 
“OpenClaw gateway architecture”
- 
“OpenClaw multi agent routing”
- 
“OpenClaw memory dreaming”


---


## Deeper conceptual reading (this is where it clicks)


### 1. Memory as cognition (important for Hermes-style thinking)


- 
Retrieval-Augmented Generation limitations
- 
“LLM memory systems beyond RAG”
- 
“agentic memory vs retrieval memory”


---


### 2. Tool learning / skill formation


- 
“LLM agents skill acquisition papers”
- 
“procedural memory in AI agents”
- 
“toolformer / self-improving agents”


---


### 3. Multi-agent vs single-agent architectures


- 
“multi agent orchestration vs single agent cognition”
- 
“agent routing vs agent learning”


---


# 6. My blunt recommendation for CoCo


If I strip everything down to what actually matters for you:


### Use Hermes if:


- 
you want **learning + evolution**
- 
you need **cost-efficient pipelines**
- 
you want **one coherent companion**
- 
you are okay constraining behavior


### Use OpenClaw if:


- 
you want **many agents / many channels**
- 
you need **tight operational control**
- 
you want **predictable behavior at scale**


---


## But the real answer (and I’ll push you here)


You shouldn’t choose one.


You should build:


```
Hermes = cognitive engineOpenClaw (or similar) = routing + interface layerYour backend = truth + memory + consent + structure
```


Because CoCo is not:


> 
> “an AI agent”
> 
> 
> 


It’s:


> 
> **a guided social system with AI as interface**
> 
> 
> 


And that means:


👉 The hardest problem is not the agent

👉 It’s the **memory + consent + coordination layer underneath it**


---


If you want, I can map a **full CoCo architecture** (agents + DB + RAG + model routing + facilitator dashboard) that fits exactly your MVP constraints.

---

## You

So is there anything openclaw can do, easily that Hermes cannot do or cannot do easily?

---

## Assistant

I’ll treat this as a capability-difference check, not a fan-club debate. The key test: “what becomes simple in OpenClaw but awkward in Hermes?”

---

## Assistant

The sharp edge is not “OpenClaw has channels, Hermes doesn’t.” Hermes has a serious gateway too. The actual OpenClaw advantage is more like switchboard choreography: many agents, many accounts, deterministic bindings, one control plane.

---

## Assistant

Yes. **OpenClaw has a few “boringly powerful” gateway capabilities that Hermes does not seem to make as easy.** Hermes is stronger as a self-improving cognitive agent. OpenClaw is stronger as a **multi-agent communications switchboard**.


## The big one: one gateway, many routed agents


OpenClaw can run **multiple isolated agents inside one Gateway**, each with its own workspace, state directory, auth profiles, model registry, config, and session store. Inbound messages are routed to agents through bindings. The docs explicitly frame this as “multiple isolated agents… plus multiple channel accounts… in one running Gateway.” [OpenClaw](https://docs.openclaw.ai/concepts/multi-agent)


Hermes can run multiple agents too, but the pattern is different: **profiles**. Each profile has its own config, memory, sessions, skills, cron jobs, and gateway state, but each profile runs its own gateway as a separate process with its own bot token. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)


So the difference is:


| Need | OpenClaw | Hermes |
| --- | --- | --- |
| One gateway routes many personas/accounts | Native | Awkward |
| One profile/agent per process | Possible | Native |
| Multi-agent ops dashboard/control plane | More natural | More fragmented |
| “Who gets this message?” routing rules | Core concept | More profile/process-based |


For CoCo, this matters if you want:


```
one CoCo Gateway  → Navigator agent  → Facilitator agent  → Connector agent  → Steward agent  → Cohort-specific agents  → channel-specific agents
```


Hermes can approximate this, but you’re juggling profiles, processes, tokens, and gateway services. Tiny octopus, many clipboards. 🐙


---


## OpenClaw can do deterministic channel/account/agent routing more cleanly


OpenClaw’s routing is host-configured: the model does **not** choose the outbound channel. Replies go back through deterministic routing controlled by configuration. It has explicit concepts for channel, account ID, agent ID, and session key. [OpenClaw](https://docs.openclaw.ai/channels/channel-routing)


Hermes has a serious gateway too. It connects many platforms and stores sessions, but the documented architecture routes platform messages through adapters into the AIAgent pipeline, rather than presenting the same kind of first-class multi-agent binding layer. [Hermes Agent+1](https://hermes-agent.nousresearch.com/docs/user-guide/messaging)


This is a genuine OpenClaw advantage if your product is more **communications infrastructure** than **single evolving companion**.


---


## OpenClaw has “broadcast groups”: multiple agents respond to the same chat event


OpenClaw has an experimental feature called **Broadcast Groups** where multiple agents can process and respond to the same WhatsApp group or DM message, using one phone number. The docs describe use cases like specialist agent teams, multi-language support, QA workflows, and task automation. [OpenClaw](https://docs.openclaw.ai/channels/broadcast-groups)


That is highly relevant for CoCo. Imagine one participant asks:


> 
> “What should I do before tomorrow’s session?”
> 
> 
> 


OpenClaw-style broadcast could let:


- 
Navigator answer logistics
- 
Steward check commitments
- 
Connector suggest people to meet
- 
Facilitator quietly flag ambiguity


Hermes has subagents, but that is more task delegation inside an agent run. OpenClaw’s version is closer to **platform-level multi-agent choreography**.


---


## OpenClaw has broader “messaging weirdness” coverage


Hermes supports many platforms: Telegram, Discord, Slack, WhatsApp, Signal, SMS, Email, Home Assistant, Mattermost, Matrix, DingTalk, Feishu/Lark, WeCom, Weixin, BlueBubbles, QQ, and browser. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/messaging)


OpenClaw’s channel list includes several extra or more niche surfaces: Microsoft Teams, Google Chat, LINE, IRC, Nextcloud Talk, Nostr, Synology Chat, Twitch, Tlon/Urbit, Zalo, Zalo Personal, and voice-call plugins, alongside the usual Telegram, WhatsApp, Slack, Discord, Signal, Matrix, and BlueBubbles/iMessage. [OpenClaw](https://docs.openclaw.ai/channels)


So if CoCo eventually needs to live in odd corners of the ecosystem, OpenClaw has more “message bus barnacles” already attached.


---


## OpenClaw has a first-class device/node architecture


This is underrated.


OpenClaw has **nodes**: companion devices such as macOS, iOS, Android, or headless machines that connect to the Gateway and expose commands like `canvas.*`, `camera.*`, `device.*`, `notifications.*`, and `system.*` through `node.invoke`. [OpenClaw](https://docs.openclaw.ai/nodes)


It also has a single WebSocket Gateway protocol used by CLI, web UI, macOS app, iOS/Android nodes, and headless nodes, with clients declaring role and scope at handshake time. [OpenClaw](https://docs.openclaw.ai/gateway/protocol)


Hermes has strong browser automation and multiple execution backends, but I do not see the same first-class paired mobile/device-node command plane in the official docs. Hermes’ browser automation docs focus on local/cloud browser providers, CDP, Browserbase, Browser Use, Firecrawl, and related web automation tooling. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/browser?utm_source=chatgpt.com)


For CoCo, OpenClaw nodes could matter if you imagine:


- 
room-based facilitation devices
- 
kiosk/tablet experiences
- 
local camera/canvas workflows
- 
node-hosted execution on separate machines
- 
participant-facing companion devices later


That is less important for the MVP, but interesting for embodied/physical gatherings.


---


## OpenClaw has a more explicit “delegate” model for organizational agents


OpenClaw has a documented **Delegate Architecture**: an agent with its own identity, email/display name/calendar, acting on behalf of people without pretending to be them, using explicit identity-provider permissions. [OpenClaw](https://docs.openclaw.ai/concepts/delegate-architecture)


Hermes can obviously be configured as a bot with credentials, but OpenClaw’s delegate framing is more directly aligned with organizational accountability:


```
Not: “The AI is pretending to be Alice”But: “CoCo Steward is acting on behalf of the facilitation team”
```


For CoCo, that matters. You want agents with clear roles, visible authority, and bounded permissions. The “who is speaking?” question should never be foggy soup.


---


## OpenClaw has stronger gateway operations and safety tooling around channels


OpenClaw has a built-in `openclaw security audit` command, including deep, fix, and JSON modes. The docs say it checks common risks such as Gateway auth exposure, browser control exposure, filesystem permissions, permissive exec approvals, and open-channel tool exposure. [OpenClaw](https://docs.openclaw.ai/gateway/security)


It also has channel troubleshooting commands like `openclaw status`, `openclaw gateway status`, `openclaw logs --follow`, `openclaw doctor`, and `openclaw channels status --probe`, with channel-specific checks for WhatsApp, Telegram, Discord, Slack, iMessage/BlueBubbles, Signal, QQ, and Matrix. [OpenClaw](https://docs.openclaw.ai/channels/troubleshooting)


Hermes also has `doctor` commands and profile health checks, so this is not exclusive. But OpenClaw feels more mature as a **gateway operator’s toolkit**.


---


# So, what can OpenClaw do more easily?


The honest list:


1. 
**Run many isolated agents in one gateway with deterministic routing.**
2. 
**Bind specific agents to specific channels, accounts, groups, or senders.**
3. 
**Let multiple agents process the same WhatsApp group/DM message via Broadcast Groups.**
4. 
**Support more niche/community/enterprise messaging surfaces.**
5. 
**Pair local/mobile/headless device nodes as command surfaces.**
6. 
**Represent agents as organizational delegates with their own identity and permission scope.**
7. 
**Operate and troubleshoot a messy real-world messaging gateway more directly.**


# Bottom line for CoCo


Hermes is the better **mind**.


OpenClaw is the better **switchboard**.


For the CoCo MVP, Hermes still feels better for memory, learning, and cost-routing. But if CoCo becomes a multi-channel facilitation infrastructure with many cohorts, personas, rooms, WhatsApp groups, Telegram bots, dashboards, and device nodes, OpenClaw starts looking less like a side option and more like the nervous system.


My architecture instinct:


```
Hermes = evolving companion cognitionOpenClaw = multi-agent, multi-channel routing fabricCoCo backend = consent, truth, memory, participant state
```


Do not make OpenClaw the brain. Do not make Hermes the router. Do not make either one the source of truth. That way madness lies, wearing a YAML cape.

---

## You

how does memory implementation differ between OpenClaw and Hermes?

---

## Assistant

I’ll ground this in current docs because both projects are moving targets. The useful lens is: **what gets stored, who controls consolidation, and how retrieval enters the prompt.**

---

## Assistant

The key difference is this:


**OpenClaw treats memory as a workspace-native knowledge store. Hermes treats memory as a bounded cognitive layer plus session recall plus optional external memory intelligence.**


In plainer words: **OpenClaw is more like a well-organized notebook with search and review rituals. Hermes is more like a compact working memory with a long archive and optional memory organs plugged in.** Tiny cyber-hippocampus zoo. 🧠🦎


## 1. What is stored


### OpenClaw


OpenClaw’s default memory is explicitly file-based. It writes plain Markdown files into the agent workspace, and the docs are very direct: the model only “remembers” what gets saved to disk. Its core files are:


| File | Role |
| --- | --- |
| MEMORY.md | Long-term durable facts, preferences, decisions |
| memory/YYYY-MM-DD.md | Daily notes, observations, running context |
| DREAMS.md | Optional human-reviewable consolidation diary |


Today and yesterday’s daily notes are loaded automatically, while `MEMORY.md` is loaded at the start of every DM session. [OpenClaw](https://docs.openclaw.ai/concepts/memory)


### Hermes


Hermes has two built-in memory files:


| File | Role | Limit |
| --- | --- | --- |
| MEMORY.md | Agent’s personal notes, environment facts, conventions, lessons learned | 2,200 chars |
| USER.md | User profile, preferences, communication style | 1,375 chars |


Both live under `~/.hermes/memories/` and are injected into the system prompt at session start. The key implementation detail: Hermes intentionally keeps these memories **small and bounded**. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)


So OpenClaw’s native memory is more expansive and document-like. Hermes’ native memory is more compressed and prompt-budget aware.


---


## 2. How memory enters the prompt


### OpenClaw


OpenClaw loads durable memory and recent daily notes into context, then gives the agent tools to search or fetch memory when needed. The agent has `memory_search` and `memory_get`; `memory_search` can use semantic search, and `memory_get` reads a specific file or line range. [OpenClaw](https://docs.openclaw.ai/concepts/memory)


The implementation pattern is:


```
Workspace files  ↓Index / search backend  ↓memory_search / memory_get  ↓selected notes enter context
```


This makes OpenClaw memory feel closer to **RAG over a living workspace**.


### Hermes


Hermes injects its compact `MEMORY.md` and `USER.md` directly into the system prompt at the start of each session as a **frozen snapshot**. Changes made during a session are persisted immediately, but they do not appear in the prompt until the next session. Hermes says this is intentional to preserve prefix-cache performance. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)


The implementation pattern is:


```
Small curated memory files  ↓frozen prompt block at session start  ↓agent uses memory as always-present identity/context
```


Hermes has no `read` action for built-in memory because the memory is already injected into the prompt; the `memory` tool supports add, replace, and remove. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)


That is a very different philosophy. OpenClaw retrieves memory. Hermes inhabits a compact memory snapshot.


---


## 3. Retrieval and search


### OpenClaw


OpenClaw’s memory system is retrieval-first. With embeddings configured, `memory_search` combines vector similarity with keyword matching. It also auto-detects embedding providers from configured API keys for OpenAI, Gemini, Voyage, or Mistral. [OpenClaw](https://docs.openclaw.ai/concepts/memory)


It has multiple backends:


| Backend | Function |
| --- | --- |
| Builtin | SQLite-based, keyword, vector, hybrid search |
| QMD | Local-first sidecar with reranking, query expansion, external directory indexing |
| Honcho | AI-native cross-session memory with user modeling, semantic search, multi-agent awareness |


[OpenClaw](https://docs.openclaw.ai/concepts/memory)


This makes OpenClaw better when your memory problem is:

**“I have a growing corpus of notes, logs, vaults, decisions, project files, and I need good retrieval.”**


### Hermes


Hermes separates **always-on memory** from **session search**.


The always-on part is the bounded `MEMORY.md` and `USER.md`. For longer recall, Hermes stores CLI and messaging sessions in SQLite at `~/.hermes/state.db` with FTS5 full-text search. The `session_search` tool can retrieve past conversations and summarize them with Gemini Flash. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)


Its own docs contrast the two:


| Hermes layer | Capacity | Purpose |
| --- | --- | --- |
| Persistent memory | ~1,300 tokens | Critical facts always in context |
| Session search | Unlimited sessions | “Did we discuss X last week?” recall |


[Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)


So Hermes is better when your memory problem is:

**“Keep the agent’s active identity compact, but let it search its conversational past on demand.”**


---


## 4. Consolidation


### OpenClaw


OpenClaw has two notable consolidation mechanisms.


First, it has **automatic memory flush** before conversation compaction. Before compaction summarizes a conversation, OpenClaw runs a silent turn that reminds the agent to save important context to memory files. This is on by default. [OpenClaw](https://docs.openclaw.ai/concepts/memory)


Second, it has optional **Dreaming**, a background consolidation pass that collects short-term signals, scores candidates, and promotes qualified items into `MEMORY.md`. It is opt-in, scheduled, thresholded, and reviewable through `DREAMS.md`. [OpenClaw](https://docs.openclaw.ai/concepts/memory)


This is important: OpenClaw’s consolidation is **file-promotion oriented**. It decides what should graduate from daily/short-term memory into durable long-term memory.


### Hermes


Hermes does consolidation mostly through bounded memory management. When memory is full, the agent must remove or consolidate entries before adding new ones. The docs recommend compact, information-dense entries and consolidation above 80 percent capacity. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)


Hermes also saves proactively when it learns user preferences, environment facts, corrections, conventions, completed work, and explicit remember requests. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory)


So Hermes consolidation is **compression oriented**. It keeps a tiny executive summary of what matters, rather than growing a large native memory store.


---


## 5. External memory providers


This is where Hermes becomes more ambitious.


Hermes ships with eight external memory provider plugins: Honcho, OpenViking, Mem0, Hindsight, Holographic, RetainDB, ByteRover, and Supermemory. Only one external provider can be active at a time, and the built-in memory remains active alongside it. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers)


When an external provider is active, Hermes automatically injects provider context into the prompt, prefetches relevant memories before each turn, syncs conversation turns after responses, extracts memories at session end where supported, mirrors built-in memory writes, and adds provider-specific memory tools. [Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers)


This is the strongest argument for Hermes as a **memory experimentation platform**.


OpenClaw also supports multiple memory backends, including QMD and Honcho, but its shape is more “active memory plugin owns recall, promotion, indexing, dreaming.” Hermes’ provider system is more explicitly designed around **external user modeling and cross-session context enrichment**. [OpenClaw+1](https://docs.openclaw.ai/concepts/memory)


---


## 6. Knowledge layer


OpenClaw has something Hermes does not appear to mirror as directly: **Memory Wiki**.


`memory-wiki` turns durable memory into a compiled knowledge vault with deterministic pages, structured claims, provenance, dashboards, and machine-readable digests. It does not replace the active memory plugin; it sits beside it. [OpenClaw](https://docs.openclaw.ai/plugins/memory-wiki)


This matters for CoCo. Memory Wiki is closer to a **governed knowledge base** than a personal memory stream. It can track claims, evidence, confidence, contradictions, and open questions. [OpenClaw](https://docs.openclaw.ai/plugins/memory-wiki)


For a regenerative network or facilitator system, that is not ornamental. That is the difference between “the bot vaguely remembers” and “the system can explain why it believes something.”


---


# The practical difference


| Dimension | OpenClaw | Hermes |
| --- | --- | --- |
| Native memory style | Markdown workspace memory | Small curated prompt memory |
| Main files | MEMORY.md, daily notes, DREAMS.md | MEMORY.md, USER.md |
| Size philosophy | Expandable workspace corpus | Strictly bounded memory |
| Retrieval | Central: memory_search, memory_get | Built-in memory is injected; session search is separate |
| Search | Hybrid semantic + keyword search | FTS5 session search + summarization |
| Consolidation | Flush + optional dreaming promotion | Compression/replacement within limits |
| External memory | Backends/plugins like QMD, Honcho | Eight provider plugins, additive to built-in memory |
| Governance layer | Stronger via Memory Wiki | Stronger external provider ecosystem |
| Best at | Auditable knowledge, workspace recall, durable notes | User modeling, compact identity, cross-session conversational memory |


---


# My read for CoCo


For CoCo, this distinction is decisive.


**OpenClaw memory is better for collective, auditable, facilitator-facing knowledge.**

It is better for session notes, commitments, claims, decisions, contradictions, evidence, and “what did this group agree?” The Memory Wiki angle is especially relevant.


**Hermes memory is better for personal companion continuity.**

It is better for “who is this participant?”, “what do they prefer?”, “what patterns have emerged across conversations?”, and “what should the agent remember about how to work with them?”


The architecture I would trust:


```
CoCo canonical memory  Postgres + pgvector  consent rules  participant state  commitments  session records  facilitator notesHermes-style memory  per-participant companion profile  bounded user preferences  cross-session conversational recallOpenClaw-style memory  cohort knowledge vault  claims/evidence  session digests  facilitator-facing collective memory
```


The mistake would be letting either agent framework become the canonical memory of CoCo. For participant trust, **memory must be governed, editable, consent-aware, and inspectable**. Agents can sip from the well, but they should not own the aquifer.

---

## You

so it sounds like openclaw memory is better for cohort or team or organisation use?

---

## Assistant

Yes, **directionally that’s right**.


**OpenClaw memory is better suited to cohort, team, organisation, or knowledge-vault use** because it behaves more like a shared institutional memory system: durable files, daily notes, search, promotion, review, and wiki compilation. Its memory model includes `MEMORY.md` for durable facts and decisions, dated daily notes for running context, and optional `DREAMS.md` summaries for human review. [OpenClaw](https://docs.openclaw.ai/concepts/memory?utm_source=chatgpt.com)


The strongest organisational clue is **Memory Wiki**. OpenClaw’s `memory-wiki` compiles durable memory into a navigable knowledge vault with deterministic pages, structured claims, provenance, dashboards, and machine-readable digests. That is much closer to “what does this group know, believe, decide, and need to revisit?” than “what does this assistant remember about one person?” [OpenClaw](https://docs.openclaw.ai/plugins/memory-wiki?utm_source=chatgpt.com)


Hermes, by contrast, is better for **personal continuity and adaptive companionship**. Its built-in memory is deliberately bounded through `MEMORY.md` and `USER.md`, and external memory providers add personalization, semantic search, knowledge graphs, automatic extraction, and cross-session user modeling. [Hermes Agent+1](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers?utm_source=chatgpt.com)


So the clean split is:


| Use case | Better fit |
| --- | --- |
| Personal companion that learns a user | Hermes |
| Participant profile and preferences | Hermes-style memory |
| Cohort agreements and session decisions | OpenClaw |
| Team/organisation knowledge vault | OpenClaw |
| Claims, provenance, contradictions, stale knowledge | OpenClaw Memory Wiki |
| Deep user modeling | Hermes + provider like Honcho |


For CoCo, I would frame it this way:


```
Hermes memory = personal relational continuityOpenClaw memory = collective institutional memoryCoCo backend = governed truth, consent, permissions
```


The critical pushback: **OpenClaw may be better for cohort memory, but it still should not be the canonical source of truth**. For CoCo, the canonical layer should be your own database with permissions, consent, deletion, audit trails, and facilitator controls. OpenClaw can then act as the **collective memory interface**, not the legal or ethical memory vault.


A good architecture would be:


```
Participant companion  Hermes  remembers personal preferences, journey state, tone, support needsCohort memory  OpenClaw memory / Memory Wiki  remembers agreements, session summaries, roles, questions, tensions, decisionsCanonical CoCo backend  Postgres + pgvector  owns consent, privacy, profiles, commitments, access rules
```


So yes: **OpenClaw feels more naturally “team brain / organisation brain.” Hermes feels more naturally “personal companion brain.”**

Tiny distinction, huge architecture consequences.

---

