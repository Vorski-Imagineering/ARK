# 02. System Boundary And Source Of Truth

## Purpose

Decide which parts of the system own truth and what data belongs in each layer.

## Topics to answer

- The system of record for raw transcripts, editable notes, derived knowledge, and agent procedures.
- Which data is immutable raw evidence and which is derived or promotable.
- Which parts live in GitHub, SurrealDB, object storage, and HERMES-local state.
- What must never be stored only in HERMES memory files or profile state.
- Whether a compiled wiki layer is needed in addition to graph memory.
- The durability and deletion requirements for each data class.

## Included answers from current materials

- Genesis Brain Light should keep an editable document layer and a separate queryable memory or knowledge layer.
- The agent runtime should not become the system of record.
- SurrealDB remains the default canonical memory candidate unless research shows a blocking mismatch.

## Still to answer

- The exact source-of-truth map for each major data type.
- Whether compiled wiki artefacts are required in v1.
- The deletion, retention, and rollback rules for each class of data.
