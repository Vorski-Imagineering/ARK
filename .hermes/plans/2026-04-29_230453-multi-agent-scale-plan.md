# Genesis Brain Light — Multi-Agent Scale Implementation Plan

**Version:** 1.0  
**Date:** 2026-04-29  
**Status:** Planning  
**Context:** ARK repository, The Gathering deployment

---

## Goal

Deploy Genesis Brain Light knowledge system scaled to **hundreds of agents (one per person)**, where each person has their own agent with access to shared community knowledge while maintaining privacy boundaries.

---

## Current Context

**Existing Design:**
- Genesis Brain Light uses GitHub → webhook → SurrealDB pipeline
- MCP server provides AI assistant access to knowledge graph
- Designed for single community namespace

**Scalability Questions for Multi-Agent:**
1. **Data separation:** How to partition knowledge between personal and shared
2. **Agent identity:** How agents authenticate and are identified
3. **Resource limits:** CPU/memory for hundreds of potential concurrent agents
4. **Privacy:** What stays private vs shared across the community
5. **Coordination:** How agents collaborate on shared knowledge

---

## Assumptions

1. Each person has their own Hermes agent instance
2. All agents connect to the same SurrealDB instance
3. Some knowledge is personal (private), some is shared (community)
4. Agents may collaborate on joint projects/documents
5. The Gathering has ~100-200 members who could become agents

---

## Proposed Architecture: Hybrid Multi-Tenant

### Data Partitioning Strategy

| Data Type | Storage | Access |
|-----------|---------|--------|
| Personal memories | Per-agent SQLite | Agent-private |
| Community knowledge | Shared SurrealDB | Read: all agents, Write: authorized |
| Personal notes | Agent-local SurrealDB namespace | Agent-private |
| Project collaboration | Shared SurrealDB with ACLs | Project members |

### SurrealDB Namespace Structure

```
Namespaces:
├── tcc/                     # The Coherence Company shared knowledge
│   ├── knowledge_base/      # Public community docs
│   └── projects/            # Collaborative spaces
├── <agent_id>/              # Personal knowledge for each agent
│   ├── memory/              # Episodic/personal memory
│   └── private_kb/          # Private documents/scratchpad
└── groups/                  # Special group workspaces
```

---

## Step-by-Step Implementation Plan

### Phase 0: Foundation (Prep) — 1 day

**Tasks:**
1. ✅ Verify SurrealDB setup is stable (currently not running)
2. Set up proper namespace and authentication in SurrealDB
3. Create agent identity system (UUID per agent, stored in SurrealDB)
4. Document data separation policy (what's shared vs private)

**Files to create:**
- `.hermes/plans/2026-04-29_surrealdb-multi-agent-plan.md` (this file)
- `skills/knowledge-base/auth/agent_identity.py` - Identity management
- `skills/knowledge-base/auth/scopes.py` - Permission scopes

---

### Phase 1: Multi-Tenant Database — 2-3 days

**Tasks:**
1. Configure SurrealDB with proper namespaces and authentication
2. Implement namespace routing based on agent_id
3. Create schema for agent registry and permissions
4. Set up read-only vs read-write access patterns

**SurrealDB Changes:**
```sql
-- Agent registry table
DEFINE TABLE agent SCHEMALESS;
DEFINE FIELD id ON agent TYPE string;
DEFINE FIELD name ON agent TYPE string;
DEFINE FIELD telegram_handle ON agent TYPE string;
DEFINE FIELD created_at ON agent TYPE datetime;

-- Permission system
DEFINE TABLE kb_permission SCHEMALESS;
DEFINE FIELD agent_id ON kb_permission TYPE string;
DEFINE FIELD ns ON kb_permission TYPE string;
DEFINE FIELD can_read ON kb_permission TYPE bool;
DEFINE FIELD can_write ON kb_permission TYPE bool;
```

**Files to modify:**
- `skills/knowledge-base/pipeline/db.py` - Add namespace parameter
- `skills/knowledge-base/pipeline/ingest.py` - Support multi-tenant ingestion

---

### Phase 2: Agent Identity System — 1-2 days

**Tasks:**
1. Create agent identity verification (Telegram handle → agent_id mapping)
2. Generate JWT tokens or API keys per agent for SurrealDB access
3. Implement identity-aware pipeline operations
4. Store agent metadata in shared SurrealDB

**Components:**
- `skills/knowledge-base/auth/authenticate.py` - Verify agent identity
- `skills/knowledge-base/auth/token.py` - Generate access tokens
- Update pipeline to include agent context in all operations

---

### Phase 3: Privacy Boundaries — 2 days

**Tasks:**
1. Implement query filtering by namespace
2. Create personal KB ingestion path (writes to agent's namespace)
3. Set up shared KB modification workflow (review/approval or git-based)
4. Define "share request" mechanism for personal → community

**Key Decisions:**
- **Shared knowledge:** Modified only via PR-style process (git push to community repo)
- **Personal knowledge:** Direct ingestion, no review
- **Collaboration:** Shared namespace with member list

---

### Phase 4: Agent Configuration — 1 day

**Tasks:**
1. Create agent template with knowledge base configuration
2. Document agent_id setup (from Telegram handle)
3. Create per-agent SurrealDB credentials
4. Test with 2-3 test agents

**Files:**
- `skills/knowledge-base/config/agent_template.yaml`
- `skills/knowledge-base/scripts/setup_agent.sh <telegram_handle>`

---

### Phase 5: Scaling Tests — 1-2 days

**Tasks:**
1. Simulate 5-10 concurrent agents
2. Measure resource usage under load
3. Test query performance with multi-tenant data
4. Verify isolation between namespaces

**Metrics to track:**
- Memory per active agent connection
- Query latency on shared namespace
- Concurrent connection limits

---

### Phase 6: Documentation & Rollout — Ongoing

**Tasks:**
1. Write agent setup guide for The Gathering members
2. Create privacy policy documentation
3. Document collaboration workflows
4. Gradual rollout (start with core team, then wider)

---

## Files Likely to Change

```
skills/knowledge-base/
├── pipeline/
│   ├── db.py           # Add namespace routing
│   ├── ingest.py       # Multi-tenant support
│   └── auth/           # New directory
│       ├── authenticate.py
│       └── token.py
├── scripts/
│   ├── setup_agent.sh
│   └── query.sh        # Update for multi-tenant
├── config/
│   └── agent_template.yaml
└── SKILL.md            # Update usage patterns
```

---

## Tests / Validation

| Test | Method | Success Criteria |
|------|--------|------------------|
| Identity system | Create test agent, verify token | Can authenticate queries |
| Namespace isolation | Query across namespaces | Only sees authorized data |
| Concurrent agents | 5 simultaneous queries | <100ms latency |
| Privacy boundary | Attempt cross-namespace write | Rejected |
| Shared ingestion | Simulate PR workflow | Community KB updated |

---

## Risks, Tradeoffs, Open Questions

### Key Risks
1. **SurrealDB resource scaling** - How many concurrent connections can it handle?
2. **Authorization complexity** - Permissions system could become unwieldy
3. **Privacy violations** - Risk of agents accessing wrong namespace

### Tradeoffs
- **Simplicity vs Security:** Single namespace is easier but less private
- **Consistency vs Speed:** Shared KB needs review process, slower updates
- **Cost vs Features:** More namespaces = more storage, better isolation

### Open Questions
1. Should each agent get their own SurrealDB instance or shared DB with namespaces?
2. How to handle agent identity when people change Telegram handles?
3. What's the approval workflow for community KB contributions?
4. Should agents automatically ingest their conversations into personal KB?
5. How to handle offline agents (do they fall behind on community knowledge)?

---

## Next Actions

1. **Immediate:** Get SurrealDB running (Phase 0, Task 1)
2. **Short term:** Implement basic multi-tenant namespace routing (Phase 1)
3. **Validation:** Test with 2 agents before scaling

---

## References

- [Genesis Brain Light Design](../../research/regentribe/GENESIS-BRAIN-LIGHT-DESIGN.md)
- [TCC MVP Specification](../plan/The Coherence Company/metis-hermes-01/mvp.md)
- [SurrealDB Multi-Tenancy Docs](https://surrealdb.com/docs/surrealql/namespaces-and-databases)
