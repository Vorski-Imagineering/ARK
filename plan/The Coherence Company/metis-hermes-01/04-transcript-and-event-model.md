# 04. Transcript And Event Model

## Purpose

Define the canonical representation for conversations and related evidence.

## Topics to answer

- The canonical schema for conversations, turns, participants, channels, attachments, replies, timestamps, and sessions.
- The derived objects needed in v1, such as claims, questions, decisions, commitments, interests, summaries, contradictions, affinities, and tasks.
- How provenance is represented from each derived object back to source turns or documents.
- How edits, redactions, deletions, and reversals are represented over time.
- What access-control or sensitivity labels must exist at the event level.
- The ingestion path for chat transcripts versus markdown docs versus uploaded files.

## Included answers from current materials

- Transcript-native institutional memory will require richer primitives than `document`, `chunk`, and `concept` alone.

## Still to answer

- The full event schema.
- The minimum set of derived objects for v1.
- The provenance model and temporal mutation model.
