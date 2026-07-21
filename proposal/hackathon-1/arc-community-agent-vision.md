# ARC Community Agent: Vision and Functionality

This document defines the enduring purpose, behaviour, boundaries, and operating model of the ARC Community Agent. The delivery experiment is defined separately in the [ARC Community Agent Hackathon Proposal](./arc-community-agent-hackathon-proposal.md).

## 1. Vision and purpose

The ARC Agent is a shared AI companion that helps activate, inform, connect, and grow the ARC community.

It serves three primary groups:

1. People considering joining ARC.
1. Registered and authorised ARC members.
1. Participating organisations within the ARC network.

At the highest level, the ARC Agent has two functions:

1. **Updates.** It collects attributable information from participating organisations, stores and synthesises it, and produces both general community updates and specific updates for each authorised participant based on their interests, permissions, and requested frequency.
1. **Relationship management.** It onboards and engages participants, maintains the relationship between each participant and ARC, and helps build relevant relationships among participating people and organisations. In Phase 2, it uses updates and consented participant context to suggest possible alignments and worthwhile conversations.

The public personality, build-in-public feed, source memory, consent controls, delivery channels, and operating-cost accounting support these two functions. They are not separate primary purposes.

The core operating loop is:

1. Each participating organisation chooses how it provides public updates, using any technically and legally accessible public mechanism that suits it.
1. The agent collects, stores, attributes, and synthesises those updates.
1. The agent communicates only with registered users it is authorised to contact and tailors proactive updates to their stated interests and requested frequency.
1. The agent maintains continuity between members and the community by remembering consented interests, following up at an agreed rhythm, inviting feedback and participation, and helping members see where they belong and how they can contribute.
1. In a second phase, the agent uses public updates and consented participant context to suggest possible alignments and worthwhile conversations among people and organisations.
1. The agent tracks token use, operating costs, available funds, and confirmed member or organisation contributions.
1. When funds cross an agreed low-funds threshold, the agent sends an approved contribution request to eligible registered recipients while leaving billing and payment authority with a human budget owner.

The agent is not a central authority, organisational spokesperson, autonomous financial actor, or organisational decision-maker. It is a shared community interface built from public information contributed by participating organisations.

## 2. The opportunity

ARC is a community of people who participate through organisations.

This creates an opportunity that is larger than a conventional member directory or community chat. Each organisation is continuously creating knowledge, running activities, building projects, publishing media, organising events, and learning from its work.

However, this activity is distributed across many channels:
- Websites.
- Social media.
- Newsletters.
- Videos.
- GitHub repositories.
- Telegram conversations.
- Public documents.
- Events and meeting recordings.
- Other agent or API interfaces.

As the number of organisations grows, it becomes increasingly difficult for members to understand what is happening across ARC.

Important updates are missed. Similar initiatives develop without discovering each other. New members face a wall of fragmented context. Active members must manually follow many feeds. The community may contain significant collective intelligence without having an interface through which that intelligence can be seen.

The ARC Agent would address this by creating a continuously updated shared intelligence layer.

Rather than requiring every participant to follow every organisation manually, the agent would:
- Collect organisational updates.
- Remember previous activity.
- Identify meaningful developments.
- Produce concise summaries.
- Answer questions.
- Personalise updates for members.
- Publish ARC’s collective story.

The opportunity is not merely information aggregation. It is the activation of relationships and collaboration through better visibility.

## 3. The problem

ARC currently lacks a persistent community intelligence function.

Without such a function:
- New members may not understand what ARC is or how to participate.
- Active members may lose touch with activity across the network.
- Participating organisations may not know what other organisations are building.
- Public updates remain fragmented across platforms.
- Relevant connections depend on individuals noticing them manually.
- Telegram discussions become difficult to search or revisit.
- Organisational knowledge is repeatedly explained rather than accumulated.
- ARC’s collective progress remains largely invisible to the wider world.
- The community lacks a consistent build-in-public practice.
- Coordinators must manually gather, interpret, and redistribute information.

A community can be active while still appearing dormant if its activity is not regularly gathered and reflected back to its members.

The ARC Agent is proposed as the mechanism for creating that feedback loop.

## 4. Functional model

The ARC Agent would be a shared AI companion for the ARC community.

Its purpose would be to activate participation, maintain community awareness, and make the activities of ARC organisations more visible.

It would not be a central authority, organisational spokesperson, or autonomous decision-maker. It would be a shared community interface built from public information contributed by participating organisations.

### 4.1 New-member onboarding

The agent would welcome new members and help them understand:
- What ARC is.
- Which organisations participate.
- What those organisations are doing.
- How members can participate.
- Which channels and activities are available.
- How to receive updates.
- How to contribute knowledge or public information.

The onboarding experience should be conversational rather than a static information dump.

The agent could ask questions such as:
- What brought you to ARC?
- Which themes or organisations interest you?
- What would you like to contribute?
- Which kinds of updates would be most useful to you?

This would allow the agent to begin building a relevant relationship with each person.

### 4.2 Ongoing member activation

The agent would maintain periodic contact with registered members whom it is authorised to contact. Registration should record explicit consent, the permitted delivery channel, the member's interests, the types of updates requested, and the requested update frequency.

This could include:
- Daily or weekly ARC summaries.
- Updates related to a person’s interests.
- Invitations to relevant events or conversations.
- Questions about what members are working on.
- On-request suggestions of organisations, topics, or public activities they may want to explore.
- Notifications about meaningful developments across the network.
- Prompts encouraging members to contribute or respond.

The goal is not to produce constant automated chatter. The goal is to create a useful rhythm that keeps members connected to the living activity of ARC.

The agent should send proactive updates only to registered and authorised recipients. Members should be able to change their interests, frequency, channel, or communication permission, including pausing or opting out of updates. The agent should apply those changes before the next scheduled delivery.

### 4.3 Organisational update streams

Every participating person belongs to a participating organisation.

Each organisation would instruct the ARC Agent on how to access a stream of its public updates. The organisation may choose whichever technically and legally accessible public mechanism suits it, including an automated feed, an organisation-specific agent, a shared public document, or a manual submission route. No organisation should be required to adopt a particular platform in order to participate.

Possible sources include:
- Organisation website.
- Public API.
- RSS or Atom feed.
- GitHub repositories.

- Instagram.
- YouTube.
- LinkedIn.
- Newsletter archive.
- Blog.
- Public calendar.
- Public document repository.
- Organisation-specific agent or agentic interface.

For the first version, the system should avoid attempting perfect integration with every platform.

A practical V1 could allow each organisation to provide:
- A small list of public URLs.
- One or more social or publishing feeds.
- A short organisational profile.
- Selected public documents.
- A manual update submission form or structured file.

The ARC Agent would poll these sources on a regular schedule, initially perhaps once per day.

It would detect new material, store it, summarise it, and incorporate it into its shared memory.

### 4.4 Community synthesis

The agent would collate updates from participating organisations into a shared synthesis.

A daily or periodic synthesis could include:
- New projects or releases.
- Events and gatherings.
- Articles, videos, or publications.
- Requests for help.
- New members or organisational participants.
- Emerging themes.
- Similar work appearing across organisations.
- Potential collaboration opportunities.
- Questions being explored by several organisations.
- Important changes in ARC itself.

The synthesis should not merely reproduce a list of links. Its value lies in helping members understand what the updates mean and how they relate.

### 4.5 Personalised updates

The ARC Agent would maintain an ongoing relationship with registered individual members whom it is allowed to contact.

Instead of sending identical information to everyone, it would tailor updates according to the preferences each member provides and may gradually improve relevance according to:
- Organisations the person follows.
- Themes they care about.
- Previous questions.
- Their role in ARC.
- Their preferred update frequency.
- Events or opportunities that may be relevant.

For example:

Three ARC organisations published updates related to community-owned AI infrastructure this week. Here is the common thread, along with the original sources.

Or:

You previously mentioned an interest in local food systems. One participating organisation has published a new pilot that may be relevant.

Personalisation should remain lightweight in V1. At minimum, each registered member should be able to select topics or organisations, choose an update frequency, and give or withdraw permission for the agent to contact them. The agent should not attempt deep behavioural profiling.

### 4.6 Question answering

Members would be able to ask the ARC Agent questions such as:
- What happened across ARC this week?
- Which organisations are working on AI agents?
- What has Organisation X been doing recently?
- Is anyone working on community governance?
- Which events are coming up?
- What has ARC learned about a particular topic?
- How can I join or contribute?
- What new organisations have joined?
- Where can I find the source for this claim?

Answers should be based on the accumulated public knowledge of ARC and should reference original sources.

Where the agent lacks sufficient information, it should say so rather than inventing an answer.

### 4.7 Telegram participation

The ARC Agent would participate in ARC’s Telegram space, similarly to the Region Tribe Agent mentioned in the voice note.

Within Telegram, it could:
- Answer questions when directly addressed.
- Share scheduled summaries.
- Welcome new participants.
- Provide links to relevant documents or organisational profiles.
- Summarise conversations when requested.
- Capture important public updates shared by members.
- Ask organisations for missing or outdated information.
- Surface relevant previous discussions.

The agent should not respond to every message or dominate the channel. It should behave as a useful participant with explicit triggers and a restrained publishing rhythm.

### 4.8 Public publishing

The ARC Agent would operate its own public channels as a recognisable public participant in the ARC community.

Possible channels include:
- A public GitHub repository.
- A public website or knowledge feed.
- X or another social platform.
- Telegram announcements.
- RSS.
- Email newsletter.
- Public API.

The GitHub repository could serve as the detailed, auditable record of:
- Organisational updates.
- Daily or weekly digests.
- ARC Agent development notes.
- Knowledge sources.
- Agent skills and prompts.
- Technical architecture.
- Implementation and pilot outputs.
- Lessons learned.

The public GitHub repository should be the canonical, detailed, auditable record. The agent should also publish shorter updates through one or more approved social media feeds, with those posts linking back to the fuller GitHub record wherever practical.

### 4.9 Building the agent in public

The ARC Agent would not only report on ARC organisations. It would maintain a candid, first-person build-in-public feed about its own activity and development.

Its build-in-public stream should explain:
- What the agent has been doing.
- What it is learning from public sources and community feedback.
- How its capabilities, skills, prompts, integrations, and working methods are changing.
- Where it is succeeding, with evidence or useful examples.
- Where it is failing, uncertain, blocked, or producing weak results.
- Mistakes, corrections, and lessons carried forward.
- Technical and governance decisions and why they were made.
- Token use, operating costs, funding position, and usage statistics at an appropriate aggregate level.
- New participating organisations.
- New members onboarded.
- What it plans to try or improve next.

Each substantive update should be published in full on GitHub and adapted into shorter posts for approved social media feeds. Social posts should link to the auditable record rather than becoming the only copy. During the early stages, externally published posts should follow an agreed review and correction process.

This creates transparency and turns the agent itself into a shared learning project. The feed should be candid rather than promotional: failures and uncertainty are part of the record, not material to hide.

### 4.10 Public personality

The ARC Agent should have a consistent, distinctive, and publicly documented personality. Its personality should make interaction approachable and recognisable while remaining appropriate for a multi-organisational community.

The public personality definition should include:
- Its public name and profile description.
- Its purpose, values, and role in ARC.
- Its tone, vocabulary, and interaction style.
- How it expresses curiosity, confidence, uncertainty, disagreement, success, and failure.
- What it will not claim or do.
- How community feedback can propose changes to its personality.

The agent should always identify itself as an AI agent. It should not pretend to be a person, impersonate an organisation, present its personality as evidence, or allow a memorable voice to obscure uncertainty and source attribution.

Changes to the personality, system instructions, or public voice should be versioned in GitHub and explained in the build-in-public feed. In this way the personality can grow with the agent while remaining inspectable and accountable.

### 4.11 Relationship stewardship and alignment

Relationship stewardship is a core function of the ARC Agent, not a secondary communication feature. It should support a network of relationships among participants:

1. **Member-to-community relationships.** It helps each registered member understand what is happening, remain connected at a rhythm they choose, find relevant ways to participate, contribute information or resources, give feedback, and see how their participation relates to the wider community.
1. **Member-to-member relationships.** It helps members become aware of relevant work, questions, needs, offers, and potential collaborators without turning the community into a directory, ranking system, or stream of unsolicited introductions.
1. **People-to-organisation and organisation-to-organisation relationships.** It helps participants discover relevant organisations, helps organisations understand member interests and offers where consent permits, and surfaces possible coordination or learning between organisations.

#### Phase 1: maintaining relationships

The first phase should establish a dependable relationship between the agent, each member, and the community. The agent should:
- Learn a member's stated interests, activities, offers, needs, contact permissions, and preferred communication rhythm.
- Deliver relevant updates and explain why they may matter to that member.
- Invite responses, corrections, questions, and contributions rather than treating communication as one-way broadcasting.
- Follow up on agreed actions or expressed interests without manufacturing urgency or excessive engagement.
- Help members navigate ARC, notice participation opportunities, and understand how their contributions fit into the collective activity.
- Remember only the minimum consented context needed to provide continuity, and allow members to inspect, correct, pause, or remove it.

The agent should support human relationships, not replace them. Community stewards and members remain responsible for trust, judgement, commitments, conflict, and care.

#### Phase 2: suggesting alignment and conversations

In the second phase, the agent should use new organisational updates, public participant activity, and consented participant context to identify possible alignment among people and organisations. Relevant signals may include:
- Members exploring the same question from different perspectives.
- A need expressed by one member that matches an offer or capability from another.
- A member's interest, capability, or offer that aligns with an organisation's public activity or request.
- Organisations pursuing complementary work or encountering a shared challenge.
- Complementary projects, skills, resources, locations, events, or timelines.
- Several members responding to the same organisational update or emerging theme.
- Work that may benefit from comparison, coordination, mutual learning, or collaboration.

For each proposed alignment, the agent should explain:
- Which public or consented signals led to the suggestion.
- Why a conversation may be useful to each person or organisation.
- The uncertainty or limitations in the inference.
- A concrete purpose, question, or lightweight agenda for the conversation.

The agent should approach each person or authorised organisational representative separately and seek permission before making an introduction or sharing non-public context. A conversation should proceed only when all proposed participants opt in. Declining or ignoring a suggestion should not reduce a participant's standing or cause repeated pressure.

The agent may record whether a suggestion was accepted, declined, or useful when participants consent, so the service can improve. It should not create hidden social scores, infer relationships as facts, publish private member information, or optimise for the number of introductions rather than their relevance and value.

## 5. Priority user journeys

### Journey 1: Onboarding a new member

**User:** A person who has recently discovered ARC.

**Need:** Understand ARC, its organisations, and how to participate.

**Agent behaviour:**
- Welcomes the person.
- Explains ARC briefly.
- Presents participating organisations.
- Asks about interests.
- Suggests relevant organisations, updates, or channels.
- Offers a preferred update rhythm.

**Information used:**
- ARC overview.
- Organisation profiles.
- Recent updates.
- Public participation information.

**Expected outcome:**

The person understands ARC and knows what action to take next.

### Journey 2: Receiving a community update

**User:** An active ARC member.

**Need:** Understand what happened across ARC without monitoring every organisational channel.

**Agent behaviour:**
- Collects new organisational updates.
- Groups them into useful themes.
- Produces a concise synthesis.
- Includes links to original sources.
- Sends or publishes the synthesis.

**Expected outcome:**

The member remains informed while spending less time following fragmented feeds.

### Journey 3: Learning about an organisation

**User:** A member interested in another ARC organisation.

**Need:** Understand what that organisation does and what it has been doing recently.

**Agent behaviour:**
- Retrieves the organisation’s profile.
- Summarises recent activity.
- Links to public documents and feeds.
- Identifies relevant current projects.
- Suggests how to learn more.

**Expected outcome:**

The member can understand the organisation without searching across several platforms.

### Journey 4: Discovering an overlap

**User:** A participant exploring a particular topic.

**Need:** Find other organisations working on related ideas.

**Agent behaviour:**
- Searches organisational profiles and updates.
- Identifies related activity.
- Explains why the activities may connect.
- Provides the original sources.
- Suggests people or organisations to approach.

**Expected outcome:**

The agent reveals at least one relevant relationship or collaboration opportunity.

### Journey 5: Updating organisational knowledge

**User:** An authorised participant from an ARC organisation.

**Need:** Help the agent understand the organisation more accurately.

**Agent behaviour:**
- Identifies missing or outdated information.
- Requests a public profile, document, link, or update stream.
- Processes the submitted information.
- Confirms how the organisation is now represented.
- Adds the source to its future update process.

**Expected outcome:**

Organisations can improve the agent’s understanding without requiring a developer.

### Journey 6: Following the agent's development

**User:** A member of the public, an ARC member, or a participating organisation.

**Need:** Understand what the agent is doing, learning, improving, and struggling with.

**Agent behaviour:**
- Publishes through a consistent and clearly disclosed AI personality.
- Records a detailed build-in-public update in GitHub.
- Explains recent activity, learning, capability changes, successes, failures, corrections, and next steps.
- Publishes a shorter social media version linking to the detailed record.
- Distinguishes verified facts from the agent's own interpretation and reflection.

**Expected outcome:**

The public can follow the agent's development, evaluate its claims, understand its limitations, and contribute informed feedback.

### Journey 7: Maintaining a relationship with the community

**User:** A registered member who wants an ongoing but manageable connection to ARC.

**Need:** Remain informed, recognised, and able to participate without monitoring every channel.

**Agent behaviour:**
- Remembers the member's consented interests, activities, offers, needs, permissions, and preferred rhythm.
- Sends relevant updates with an explanation of why they matter.
- Invites feedback, corrections, questions, and contributions.
- Follows up on an expressed interest or agreed action.
- Lets the member inspect, change, pause, or delete the relationship context.

**Expected outcome:**

The member experiences ARC as a continuing relationship rather than a stream of disconnected announcements.

### Journey 8: Suggesting an alignment conversation in Phase 2

**User:** Two or more participating people or organisations whose public updates or consented context indicate a potentially useful alignment.

**Need:** Discover a relevant conversation that the participants would not necessarily have identified themselves.

**Agent behaviour:**
- Detects a possible alignment from attributable public or consented signals.
- Explains separately to each person or authorised organisational representative why the conversation may be useful and where the inference is uncertain.
- Suggests a concrete purpose or lightweight agenda.
- Requests consent from every proposed participant before sharing non-public context or making an introduction.
- Records the outcome only with participant consent and uses it to improve future suggestions.

**Expected outcome:**

Participating people or organisations enter a mutually agreed, purposeful conversation with clear context and no unwanted disclosure or pressure.

## 6. High-level technical and operating approach

A simple initial architecture could be:

Public organisation sources  
Websites | RSS | GitHub | YouTube | Social feeds | Documents  
                         ↓  
               Update collection service  
                         ↓  
              Normalisation and summarisation  
                         ↓  
             ARC shared knowledge and memory  
                         ↓  
                    ARC Agent runtime  
                  ↙        ↓         ↘  
             Telegram   GitHub     Public feed  
                  ↓  
              ARC members

### 6.1 Source collection

The system needs a lightweight connector layer capable of:
- Polling configured URLs.
- Reading RSS feeds.
- Reading public GitHub repositories.
- Processing public web pages.
- Accepting submitted documents.
- Receiving manual organisational updates.
- Connecting to APIs where practical.

Each organisation should have a simple configuration record:

organisation:  
  name: Example Organisation  
  description: Short public description  
  website: https://example.org  
  update\_sources:  
    - type: rss  
      url: https://example.org/feed.xml  
    - type: github  
      url: https://github.com/example  
    - type: youtube  
      url: https://youtube.com/@example  
  contact:  
    name: Public ARC representative

### 6.2 Shared knowledge and memory

The knowledge layer should store:
- Organisation profiles.
- Source URLs.
- Individual updates.
- Publication dates.
- Source references.
- Generated summaries.
- ARC digests.
- Agent development updates.
- The versioned public personality definition and change history.
- Build-in-public entries, publication status, corrections, and links to GitHub and social versions.
- Telegram summaries where included.

The first version does not require an elaborate knowledge graph.

A separate access-controlled relationship layer should store only the minimum member context needed for the service: registration status, contact permission, stated interests, activities, offers, needs, requested update rhythm, agreed follow-ups, and introduction consent. Public organisational knowledge and private member relationship state should not be mixed. Members should be able to inspect, correct, export, pause, or remove their relationship data.

In Phase 2, alignment suggestions should retain the public or consented evidence used, the agent's explanation and uncertainty, each participant's consent state, and any voluntarily supplied outcome. This record should support accountability without becoming a hidden reputation or social-scoring system.

A conventional database, document store, or simple vector-enabled knowledge system may be sufficient. The important requirement is that every generated claim can be traced back to its public source.

### 6.3 Agent runtime

The agent runtime should:
- Retrieve relevant information.
- Answer questions.
- Run onboarding workflows.
- Generate summaries.
- Participate in Telegram.
- Apply its versioned public personality consistently across channels.
- Generate evidence-based self-updates from public activity, run logs, test results, corrections, cost records, and versioned changes.
- Publish canonical build-in-public updates to GitHub and approved shorter versions to social media feeds.
- Maintain consented member-to-community relationship state and agreed follow-ups.
- Generate evidence-based Phase 2 alignment suggestions and request consent before introductions.
- Ask organisations for additional information.
- Track scheduled tasks.

The system should be designed so that the underlying agent framework can be replaced later without rebuilding the knowledge layer.

### 6.4 Publishing

The simplest publication path is:
- Detailed updates committed to a public GitHub repository.
- Short summaries posted to Telegram.
- Short social media posts linked to the GitHub record and generated for human review during the early stages.

GitHub is particularly useful because it provides:
- Public access.
- Version history.
- Searchability.
- Open collaboration.
- A natural build-in-public record.
- A place to store agent prompts, skills, and documentation.

### 6.5 Cost management

Different tasks should use different model levels.

For example:
- Cheap model: feed classification and metadata extraction.
- Cheap or mid-tier model: routine summaries.
- Mid-tier model: member question answering.
- Stronger model: cross-organisational synthesis or major public reports.

The system should record:
- Model used.
- Token use.
- Cost per task.
- Daily and monthly cost.
- Non-model operating costs supplied by the budget owner.
- Number of updates processed.
- Number of member interactions.

The system should produce a realistic estimate of ongoing operating costs. The agent should aggregate these records itself so it can report current spend, forecast operating runway, and explain the basis of its calculations.

### 6.6 Operating funds and contribution accounting

The agent should maintain an operational funding ledger from human-approved inputs. The ledger should record:
- Available operating funds.
- Contributions committed and contributions received from members or participating organisations.
- Operating costs incurred, including model, hosting, storage, and other approved services.
- Current net balance.
- Average spend over an agreed period.
- Forecast runway at the current rate of use.
- The source and time of each accounting input or adjustment.

The agent should calculate its current balance and forecast runway from this ledger. A human budget owner should reconcile received contributions and non-model invoices; the agent should not infer that a promised contribution has been received.

The community should agree a low-funds threshold and a stop-spend threshold. When the forecast balance or runway crosses the low-funds threshold, the agent should:
1. Explain the current balance, recent operating costs, and forecast runway.
1. Calculate the contribution required to return to the agreed operating reserve.
1. Send an approved contribution request to registered members or participating organisations that have agreed to receive such requests.
1. Record that the request was sent and report subsequent confirmed contributions without exposing private contributor information.

If the stop-spend threshold is reached, the agent should suspend non-essential paid activity and alert the human budget owner.

The agent may perform accounting, forecasting, and approved communication, but it should not access payment instruments, change provider billing limits, confirm receipt of funds without a trusted accounting input, or make financial commitments. Public reporting should use aggregate figures and should not reveal private member identities or individual financial contributions.

## 7. Governance and operating principles

### 7.1 Public information by design

The system assumes that all contributed information is public and openly shareable.

Participants should not submit:
- Private personal information.
- Confidential organisational information.
- Internal commercial information.
- Unpublished sensitive documents.
- Credentials or access tokens.
- Information they do not have the right to share.

A simple working principle should apply:

If it should not appear in ARC’s public build-in-public feed, do not give it to the ARC Agent.

### 7.2 Open licensing

Participating organisations should agree that submitted content may be:
- Stored.
- Summarised.
- Quoted.
- Remixed.
- Indexed.
- Republished with attribution.
- Used to improve the shared ARC knowledge system.

The project should select one simple open licence for shared content and one for code.

### 7.3 Source attribution

Every important claim or summary should retain a link to its source.

The agent should distinguish between:
- Information published directly by an organisation.
- A summary produced by the ARC Agent.
- A pattern inferred across several sources.

### 7.4 Accuracy

The ARC Agent should avoid presenting uncertain interpretations as established organisational positions.

Organisations should be able to correct inaccurate profiles or summaries through a simple public process.

### 7.5 Publishing rhythm

The agent should not publish merely because a schedule exists.

Daily collection may be appropriate, while public synthesis may work better weekly unless there is sufficient activity.

The project should test both the frequency and usefulness of updates.

### 7.6 Platform limitations

Some social platforms restrict automated access or frequently change their APIs.

The system should not depend entirely on scraping proprietary feeds. RSS, public websites, GitHub, newsletters, and organisation-submitted updates may provide a more stable foundation.

### 7.7 Community activation

Information delivery alone will not necessarily energise a community.

The agent should occasionally invite action:
- Who wants to explore this?
- Does this connect to work elsewhere in ARC?
- Can anyone contribute to this request?
- Would these two organisations benefit from a conversation?

However, the agent should avoid turning every update into forced engagement bait.

### 7.8 Ongoing stewardship

Someone must remain responsible for:
- Infrastructure.
- Source configurations.
- Prompt and skill updates.
- Quality review.
- Operating costs.
- Responding when integrations fail.
- Adding new organisations.

A prototype without stewardship is a brief light show with a repository attached.

### 7.9 Relationship consent and member agency

Relationship management requires a private, access-controlled boundary even though the agent's organisational knowledge and public feed are open by design.

Members should control what relationship context is held, why it is used, how often the agent contacts them, and whether it may suggest or facilitate introductions. The agent should disclose the evidence and reasoning behind an alignment suggestion, obtain consent from every participant, minimise retained data, and provide correction and deletion routes.

The agent should not rank members, infer trust or compatibility as fact, expose private activity, make commitments for participants, or use repeated prompts to pressure people into engagement.

## 8. Longer-term vision

The longer-term vision is an inter-organisational intelligence network.

In this future model:
- Each participating organisation maintains its own public update stream.
- Some organisations may operate their own agents.
- The ARC Agent connects to those organisational agents or feeds.
- The ARC Agent maintains a network-level view.
- Members can discover activity across organisations through conversation.
- The system continuously identifies common themes and potential collaborations.
- The agent helps maintain relationships among members, organisations, and the wider ARC community.
- Public knowledge is accumulated rather than repeatedly rediscovered.
- ARC’s development is documented in public.
- New organisations can join through a standard onboarding process.

The network could eventually support:
- Agent-to-agent updates.
- Structured organisational profiles.
- Event and opportunity matching.
- Topic subscriptions.
- Cross-organisational project discovery.
- Public dashboards.
- Audio or video summaries.
- Local or regional ARC agents.
- Automated newsletters.
- Community research.
- Collaborative proposals.
- Shared skills and technical infrastructure.

Initial implementations should establish the smallest working loop from organisational updates to member value before attempting the entire vision.

## 9. Open product questions

1. Should each organisation eventually have its own agent?
1. Should organisational agents communicate directly with the ARC Agent?
1. Should ARC maintain a public knowledge graph?
1. Which public channels should receive automated posts?
1. Should audio or video summaries be introduced?
1. How should individual member interests, contact permissions, and update preferences be stored securely?
1. What level of operating contribution should members and participating organisations make?
1. How should the system scale to dozens or hundreds of organisations?
1. Which activities should remain human-led?
1. Which member context may be used for Phase 2 alignment suggestions, and how will consent, correction, deletion, and access control work?
1. What evidence makes an alignment suggestion useful enough to send, and how should accepted, declined, and useful conversations be evaluated without social scoring?
1. What evidence would justify building a production platform?
