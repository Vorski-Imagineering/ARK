# Phase 1 evaluation harness

This measures answer quality. It is **not** part of the test suite and must
never gate a build unit.

## Why it is separate

Model output is not reproducible, so no automated assertion can check whether
an answer is *good*. What the test suite checks is structure: that citations
resolve to real sources, that empty retrieval refuses rather than guesses, that
retrieved text is quarantined as untrusted data.

Whether an answer is *accurate* is a judgement, and the people qualified to make
it are the representatives of the organisations being described. This harness
exists to put answers in front of them in a reviewable form.

## Running it

```
./.venv/bin/python evals/run_eval.py --index index/active.sqlite3
```

Calls the real model. Writes a review sheet to `evals/outputs/<timestamp>.md`,
which is gitignored. Only a reviewed summary is committed.

## What a reviewer does

For each answer: read it, check the cited sources, mark Accurate as yes or no,
and note any material misrepresentation. A representative reviews only their own
organisation.

The phase gate is not "the harness ran". It is "representatives found no
unresolved material misrepresentation".
