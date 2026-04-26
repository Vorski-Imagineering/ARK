# 05. Memory Model And Retrieval Policy

## Purpose

Define what memory layers exist and how agents retrieve from them.

## Topics to answer

- Which memory layers are required in v1.
- What data belongs in each layer.
- What HERMES may read directly from built-in memory versus the external memory plane.
- What retrieval modes are required.
- What should be retrieved at interaction time versus only during offline consolidation.
- How memory freshness, contradiction, and confidence are surfaced to agents and humans.
- Whether per-agent local memory plus shared group memory is needed from day one.

## Included answers from current materials

- The design direction assumes a separate queryable memory or knowledge layer outside the runtime.
- One open question is how much shared memory is safe in v1 before trust and privacy boundaries are mature enough.

## Still to answer

- The layered memory model for v1.
- The online versus offline retrieval contract.
- The boundary between local, shared, and group memory.
