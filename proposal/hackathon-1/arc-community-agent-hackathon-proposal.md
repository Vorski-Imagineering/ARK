# ARC Community Agent Hackathon Proposal

This document proposes a focused collaborative hackathon to build and test the first working version of the ARC Community Agent. The enduring product purpose and functionality are defined in [ARC Community Agent: Vision and Functionality](./arc-community-agent-vision.md); this document defines the event, scope, roles, evidence, and decision process.

## 1. Event summary

The hackathon should test whether a shared agent can create meaningful community value by making the public work of participating organisations visible, understandable, and connected.

The event is organised around the agent's two high-level functions:

1. **Updates:** collect and synthesise organisational information into general community intelligence and participant-specific updates.
1. **Relationship management:** onboard and engage participants, maintain their relationship with ARC, and establish the foundations for Phase 2 alignment and conversation suggestions among participating people and organisations.

The public personality, build-in-public feed, source attribution, consent controls, and cost/funding accounting are shared foundations supporting both functions.

The event should produce one complete, observable loop:

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
Usage, cost, and funding accounting  
        ↓  
Public learning and a pilot decision

The goal is not a finished platform. It is credible evidence about whether the operating pattern deserves a short pilot.

## 2. Why build it through a hackathon

A hackathon is appropriate because the proposed agent is both a technical system and a shared community practice.

The project requires participating organisations to answer practical questions:
- What information will they share?
- In what format?
- Which sources are reliable?
- What kinds of summaries are useful?
- How should the agent communicate?
- Which channels should it publish to?
- How should members interact with it?
- What level of automation creates value rather than noise?

These questions are difficult to resolve through discussion alone.

A hackathon allows the organisations to create an end-to-end experiment and evaluate the experience directly.

The hackathon can produce:
- A functioning prototype.
- Real organisational update feeds.
- A shared knowledge structure.
- A Telegram agent.
- A public ARC update feed.
- An initial member onboarding flow.
- Documentation for future organisations.
- A backlog based on actual use rather than speculation.

The most important output is not the code alone. It is a tested operating pattern for how organisations contribute to and benefit from a shared agent.

## 3. Hackathon challenge

### Primary challenge

**How might we build an ARC Agent that performs two connected functions: turning organisational information into general and participant-specific updates, and managing relationships between participants, ARC, and one another?**

### Technical version

**How might we create an extensible agent pipeline that ingests public organisational feeds, stores and retrieves their content, generates sourced cross-organisational summaries, and distributes them through Telegram and public publishing channels?**

### Organisational version

**How might participating ARC organisations create a shared intelligence function that helps them remain aware of one another’s work and discover meaningful opportunities for collaboration?**

### Public-facing version

**How might ARC make the work of its organisations visible, connected, and easy to explore through one shared AI companion?**

## 4. Proposed scope

### In scope

The hackathon should include:
- Three to five participating organisations.
- A basic public profile for each organisation.
- One to three public information sources per organisation.
- Scheduled collection of new updates.
- A shared knowledge store.
- Source-linked question answering.
- A daily or hackathon-period synthesis.
- A basic Telegram interface.
- A basic new-member onboarding conversation.
- A Phase 1 relationship loop connecting member onboarding, preferences, relevant updates, response, and follow-up.
- A public GitHub repository or web feed.
- A documented public personality for the ARC Agent.
- A candid build-in-public feed on GitHub covering the agent's activity, learning, growth, successes, failures, corrections, and next steps.
- At least one approved social media feed carrying shorter agent updates that link back to the GitHub record.
- A repeatable process for adding another organisation.

### Out of scope

The hackathon should not attempt:
- Full integration with every social media platform.
- A production-scale member platform.
- Complex private-data systems.
- Autonomous organisational decision-making.
- Deep personal profiling.
- Perfect recommendation algorithms.
- Full agent-to-agent federation.
- Automated publishing to many platforms simultaneously.
- A comprehensive member relationship management system.
- Phase 2 proactive member-to-member alignment and conversation recommendations beyond a documented design and test scenario.
- Advanced mobile applications.
- Complex governance or licensing mechanisms.
- Large-scale analytics dashboards.

The test is whether the information loop works, not whether every possible interface has been decorated.

## 5. Minimum viable prototype

The minimum viable prototype should demonstrate one complete cycle:

Organisational public sources  
        ↓  
Scheduled collection  
        ↓  
Shared searchable memory  
        ↓  
Cross-organisational synthesis  
        ↓  
Member interaction through Telegram  
        ↓  
Public personality and candid build-in-public publication

### Must have

The minimum evidence should prove both functions: a complete source-to-update cycle and a complete onboarding-to-engagement-to-follow-up relationship cycle. The remaining requirements provide the shared foundations needed to operate those cycles safely and transparently.

- Three or more organisational profiles.
- At least one live or regularly updated public source per organisation.
- A documented organisation-selected update method for each organisation, including a manual route where automated integration is unavailable.
- Scheduled source collection.
- Detection of new content.
- Storage of source content and metadata.
- Question answering with source references.
- A generated ARC digest.
- Telegram access.
- Basic onboarding.
- Registration and contact permission for each user the agent communicates with.
- Member-selected interests, update type, and update frequency.
- Delivery of at least one personalised update that follows a registered member's preferences.
- One complete Phase 1 relationship loop: onboarding, permission and preference capture, relevant update, member response, and an agreed follow-up or preference change.
- Token-use, cost, available-funds, and member-contribution accounting.
- A tested low-funds threshold and approved member contribution-request workflow.
- A public personality specification that clearly identifies the agent as AI and defines its voice, values, uncertainty language, and boundaries.
- A canonical GitHub build-in-public feed explaining what the agent is doing and learning, how it is growing, where it is succeeding and failing, and what it will try next.
- At least one human-reviewed social media post in the agent's public voice linking back to the detailed GitHub update.
- Documentation for adding a new organisation.

### Useful if time allows

- More advanced personalisation beyond explicit member preferences.
- A paper or fixture-based Phase 2 alignment suggestion showing evidence, explanation, uncertainty, a proposed conversation purpose, and mutual-consent handling.
- Automated social publishing.
- Telegram conversation summaries.
- Organisational document upload.
- Email or RSS distribution.
- Identification of related activities across organisations.
- A basic activity dashboard.
- A richer funding and operating-cost dashboard.

### Future possibilities

- Organisation-specific agents.
- Agent-to-agent communication.
- Regional ARC agents.
- Rich member profiles.
- Event and opportunity matching.
- Evidence-based Phase 2 alignment suggestions and consented member introductions.
- Automated audio or video updates.
- Multi-language support.
- Advanced recommendation systems.
- Community knowledge graph.
- Public APIs for third-party tools.

## 6. Hackathon format

A two-day build event with preparation beforehand is likely the most practical format.

A one-day hackathon risks producing disconnected demonstrations. A three-day event may produce more complete infrastructure but requires greater commitment.

### Before the hackathon

Each participating organisation should:
- Nominate one representative.
- Provide a short public profile.
- Select one to three public update sources.
- Provide any public background documents.
- Identify one desired user journey.
- Confirm who can answer questions during the event.

The technical team should:
- Prepare the agent runtime.
- Prepare the source-ingestion skeleton.
- Set up the shared repository.
- Set up Telegram integration.
- Define the demonstration criteria.
- Prepare example data and fallback sources.

### Day 1: Alignment and construction

#### Opening

- Introduce the purpose.
- Demonstrate the current fragmentation.
- Agree the MVP.
- Present the architecture.
- Confirm team responsibilities.

#### Build tracks

Possible tracks:
1. Organisational source ingestion.
1. Knowledge and retrieval.
1. Telegram and onboarding.
1. Synthesis and publishing.
1. Testing and evaluation.
1. Documentation and build-in-public reporting.

#### Integration checkpoint

By the end of Day 1, the system should ingest at least one source from each organisation and answer a basic question using those sources.

### Day 2: End-to-end prototype

The second day should focus on:
- Completing the update pipeline.
- Generating the ARC digest.
- Testing member questions.
- Refining onboarding.
- Publishing the agent’s first build-in-public update.
- Publishing a shorter version through an approved social media feed.
- Adding another organisation through the documented process.
- Measuring costs and quality.
- Preparing the final demonstration.

### Final demonstration

The demonstration should show:
1. A new organisational update being detected.
1. The update being added to shared memory.
1. The agent answering a question about it.
1. The agent creating a cross-organisational synthesis.
1. A member receiving the synthesis in Telegram.
1. A public ARC update being published.
1. The agent publishing a candid self-update covering learning, growth, success, failure, and next steps on GitHub and an approved social media feed.
1. A member completing the Phase 1 relationship loop from onboarding through response and follow-up.
1. A Phase 2 alignment suggestion being demonstrated without disclosing private member information or making an introduction without mutual consent.
1. A new organisation being added using the documented process.

## 7. Participants and roles

The hackathon requires a small cross-functional group.

### Product and coordination

Responsible for:
- Defining the user journeys.
- Protecting scope.
- Coordinating organisations.
- Evaluating whether outputs are useful.

### Agent architect

Responsible for:
- Agent runtime.
- Skills and system instructions.
- Tool use.
- Scheduled behaviours.
- Telegram interaction.

### Integration developer

Responsible for:
- Public-source connectors.
- APIs.
- Polling.
- Document processing.

### Knowledge engineer

Responsible for:
- Data structure.
- Retrieval.
- Source metadata.
- Memory and citations.

### Conversation and onboarding designer

Responsible for:
- New-member onboarding.
- Update delivery.
- Telegram behaviour.
- Agent voice and interaction rhythm.
- Public personality definition and AI disclosure.

### Organisational representatives

Responsible for:
- Supplying sources.
- Explaining their organisations.
- Testing accuracy.
- Evaluating usefulness.

### Documentation and storytelling contributor

Responsible for:
- Public hackathon updates.
- The agent's GitHub build-in-public feed and social media adaptations.
- Setup documentation.
- Final demonstration.
- Recording lessons and decisions.

For a small event, several roles can be combined. The critical requirement is that organisational participants and technical builders work together rather than throwing requirements over an invisible hedge.

## 8. Deliverables

The hackathon should produce:
1. A working ARC Agent prototype.
1. Telegram interaction.
1. Three to five connected organisations.
1. A scheduled update-collection process.
1. A shared searchable knowledge base.
1. Source-linked question answering.
1. An ARC digest generated from real updates.
1. A public build-in-public repository.
1. A versioned ARC Agent public personality profile.
1. The ARC Agent’s first candid self-update on GitHub and an approved social media feed.
1. An onboarding flow for new members.
1. A tested Phase 1 member relationship loop and documented relationship-data boundary.
1. A Phase 2 alignment-suggestion scenario with evidence, explanation, uncertainty, and consent safeguards.
1. A standard organisation configuration format.
1. Documentation for adding a new organisation.
1. A high-level architecture diagram.
1. A record of model use and operating costs.
1. Test results and known limitations.
1. A prioritised backlog.
1. A recommendation on whether to continue into a pilot.

## 9. Success criteria

### Technical success

- The agent ingests public information from at least three organisations.
- New updates can be detected without manual copying.
- Members can ask questions across the combined sources.
- Answers include links or references to original sources.
- The agent generates a coherent cross-organisational digest.
- Another organisation can be added using documented steps.
- Telegram interaction works reliably.
- A registered user receives an update matching their chosen interests and requested frequency, while an unregistered or opted-out user does not receive proactive updates.
- Token use and operating costs can be measured and reconciled to the agent's operational funding ledger.
- Available funds, confirmed member or organisation contributions, and forecast runway can be calculated.
- Crossing a test low-funds threshold causes the agent to send an approved contribution request to eligible registered recipients.
- The agent uses a consistent, publicly documented personality and clearly identifies itself as AI.
- Its first self-update explains what it did, what it learned, how it changed, one success, one failure or limitation, any correction, and its next step.
- The detailed self-update is available in GitHub and a shorter approved social post links back to it.
- A member can complete the Phase 1 relationship loop and inspect, change, pause, or remove their stored preferences and contact permission.

### Community success

- Participants find the digest useful.
- New members understand ARC more quickly.
- Organisational representatives feel accurately represented.
- Members discover activity they would otherwise have missed.
- At least one meaningful organisational overlap is identified.
- Members report that the agent helps them maintain a useful relationship with ARC rather than merely sending announcements.
- Participants want to keep receiving updates.

### Learning success

- The group understands which source types are easiest to integrate.
- The group identifies what information organisations need to provide.
- The group learns how often updates should be sent.
- The group understands realistic operating costs.
- The group leaves with a clear next development priority.

## 10. Event questions

### Must answer before the hackathon

1. Is the project called ARC, ARK, or something else? A consistent name is needed.
1. Which three to five organisations will participate first?
1. Which public sources will each organisation provide?
1. Who is the initial user: prospective members, active members, or organisational representatives?
1. Which Telegram group or bot will the agent use?
1. What is the primary demonstration journey?
1. Who will coordinate the hackathon?
1. Who will maintain the prototype afterward?
1. What budget is available for hosting and model use?
1. Who is the budget owner, what are the low-funds and stop-spend thresholds, and which registered recipients may receive contribution requests?
1. Which public repository will hold the build-in-public outputs?
1. What public name, personality, AI disclosure, social accounts, publishing permissions, and review process will the agent use?
1. What minimal member relationship context can the first version store, where will it be protected, and how can a member inspect, correct, pause, or remove it?
1. Which open licences will apply to content and code?

### Can answer during the hackathon

1. How often should sources be polled?
1. Should summaries be daily, weekly, or event-driven?
1. Which update format produces the best synthesis?
1. How much personalisation is useful in V1?
1. When should the agent speak in Telegram?
1. Which model provides sufficient quality at reasonable cost?
1. How should organisational corrections be submitted?
1. Which sources are reliable enough for automated ingestion?
1. How should duplicate or repeated updates be handled?
1. What makes a cross-organisational insight genuinely useful?
1. Which evidence and consent safeguards should govern a Phase 2 member-alignment suggestion?

## 11. Recommended next steps

### Step 1: Confirm the proposition

**Owner:** ARC initiator or product lead.

**Output:** A one-page challenge brief.

Confirm:
- The agent’s primary purpose.
- The first user group.
- The initial organisations.
- The hackathon outcome.

### Step 2: Recruit participating organisations

**Owner:** Community coordinator.

**Output:** Three to five confirmed organisations.

Each organisation should nominate:
- One organisational representative.
- One technical or operational contact where available.
- Public information sources.
- One desired use case.

### Step 3: Prepare organisational source packs

**Owner:** Participating organisations.

**Output:** A standard source pack for each organisation.

Each pack should contain:
- Short public description.
- Website.
- Public update feeds.
- GitHub or document links.
- Public contact.
- Key themes or activities.

### Step 4: Select the initial technical pattern

**Owner:** Agent architect and technical lead.

**Output:** Lightweight architecture and repository.

Choose:
- Agent runtime.
- Knowledge store.
- Source-ingestion mechanism.
- Telegram integration.
- Publishing destination.
- Model provider.

### Step 5: Define the demonstration

**Owner:** Product lead and organisational representatives.

**Output:** Acceptance criteria for the final demo.

The demo should test an end-to-end flow rather than a collection of unrelated features.

### Step 6: Prepare the hackathon environment

**Owner:** Technical team.

**Output:** Running development environment.

Prepare:
- Repository.
- Agent skeleton.
- Telegram bot.
- Sample source connectors.
- Knowledge database.
- Public publication structure.
- Cost tracking.

### Step 7: Run the hackathon

**Owner:** Hackathon facilitator.

**Output:** Working prototype and documented results.

Maintain strict scope around the central information loop.

### Step 8: Conduct a short pilot

**Owner:** ARC steward.

**Output:** Two- to four-week usage report.

Measure:
- Update usefulness.
- Member interaction.
- Accuracy.
- Cost.
- Organisation participation.
- Collaboration signals.

### Step 9: Make a continuation decision

**Owner:** Participating organisations.

**Output:** Pilot continuation, revision, or closure decision.

Possible outcomes:
- Continue and improve.
- Narrow the use case.
- Add organisations.
- Replace technical components.
- Pause after documenting learning.

## 12. Decision requested

Participating ARC organisations are invited to agree to:
1. Join the design of the ARC Agent hackathon.
1. Nominate one or more participants.
1. Provide a small set of public organisational information sources.
1. Allow those public sources to be summarised and republished under an agreed open licence.
1. Contribute to building and testing the prototype on a best-effort basis.
1. Help cover modest shared operating costs according to capacity and agreement.
1. Participate in a short pilot following the hackathon.
1. Review the evidence together and decide whether the ARC Agent should continue developing.

The immediate decision is not whether to build a permanent ARC platform.

It is whether to run a focused experiment demonstrating that a shared agent can make participating organisations more visible, connected, and useful to one another.

## 13. One-page hackathon brief

### Building the ARC Community Agent

ARC proposes a collaborative hackathon to create the first working version of a shared AI agent for the ARC community.

The ARC Agent would help onboard new members, keep active members informed, collect public updates from participating organisations, answer questions about their activities, and publish ARC’s development in public. Each organisation could provide updates through its preferred accessible public method. The agent would contact only registered and authorised users, tailoring updates to their stated interests and requested frequency. Its first-phase relationship function would connect onboarding, relevant updates, member responses, and useful follow-up so that membership feels like an ongoing relationship rather than a sequence of announcements.

Each participating organisation would provide a small number of public information sources, such as its website, GitHub repository, newsletter, YouTube channel, public social feeds, or selected documents.

The agent would regularly collect new material from these sources and create a shared synthesis of what ARC organisations are building, learning, publishing, and exploring.

Members could ask questions such as:
- What happened across ARC this week?
- Which organisations are working on a particular topic?
- What has one organisation published recently?
- Are several organisations exploring related ideas?
- How can I join or contribute?

The agent would also participate in ARC’s Telegram space. It would have a distinctive, publicly documented personality and publish a candid build-in-public feed explaining what it is doing and learning, how it is growing, where it is succeeding and failing, and what it plans to improve. Detailed updates would live in GitHub, with shorter versions published through approved social media feeds.

At a high level the agent has two functions: producing general and participant-specific updates from collected organisational information, and managing relationships through onboarding, engagement, follow-up, and connections among participating people and organisations.

In a second phase, the relationship function would use organisational updates and consented participant context to identify possible alignment among people and organisations. It would explain why a conversation may be useful, suggest a concrete purpose, and seek permission from every participant before making an introduction.

### Hackathon challenge

**How might we build an ARC Agent that regularly learns from the public activities of participating organisations, keeps members informed and engaged, and publishes ARC’s collective development in public?**

### What we will build

The hackathon will aim to produce:
- A working Telegram-based ARC Agent.
- Three to five connected organisations.
- Scheduled collection of public updates.
- A shared searchable knowledge base.
- Source-linked question answering.
- A daily or weekly ARC digest.
- Registered-member preferences and permission-controlled personalised updates.
- A Phase 1 member relationship loop and a safeguarded Phase 2 alignment-suggestion design.
- Token-use, operating-cost, available-funds, and contribution accounting.
- An approved low-funds contribution request to eligible members.
- A public GitHub build-in-public repository.
- A documented public personality and AI disclosure.
- A candid GitHub self-update and shorter approved social media post.
- A conversational onboarding flow.
- Documentation for adding another organisation.

### What participating organisations contribute

Each organisation will be invited to provide:
- A short public profile.
- One to three public update sources.
- One representative for the hackathon.
- Feedback on the accuracy and usefulness of the prototype.
- Best-effort contribution to development and operating costs.

### What participants leave with

Participants will leave with:
- A working prototype.
- A clearer model for inter-organisational agents.
- Shared technical and organisational learning.
- Reusable code and documentation.
- Greater visibility into participating organisations.
- Evidence about whether a longer pilot is worthwhile.

The hackathon is not intended to produce a complete platform. Its purpose is to test one practical proposition:

**Can a shared agent help ARC organisations remain aware of one another, activate their members, and discover opportunities that would otherwise remain hidden?**
