# 07. Knowledge Graph And Compiled Knowledge Design

## Purpose

Define the external memory schema and any compiled knowledge artefacts built on top of it.

## Topics to answer

- Whether the current `document/chunk/concept/community` model is enough.
- What new entities and edges are required.
- Whether explicit `claim`, `evidence`, `decision`, `person`, `project`, `question`, `procedure`, `affinity`, or `trend_shift` records are needed.
- What temporal semantics are needed.
- What graph queries the system must support in v1.
- Whether generated entity pages or wiki pages compiled from the graph are needed.
- How graph memory and markdown or wiki memory stay in sync.
- What indexing strategy is needed for hybrid retrieval and graph traversal at expected scale.

## Included answers from current materials

- The current planning materials assume an external memory plane centered on SurrealDB unless later research shows a mismatch.
- Transcript-native institutional memory will require richer primitives than the current base model alone.

## Still to answer

- The target v1 schema.
- Whether compiled wiki artefacts are required in v1.
- The query patterns and indexing strategy needed for the guide-agent model.
