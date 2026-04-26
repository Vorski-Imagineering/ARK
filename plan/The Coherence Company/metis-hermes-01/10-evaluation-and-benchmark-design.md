# 10. Evaluation And Benchmark Design

## Purpose

Define how to judge whether the METIS guide-agent framework is working.

## Topics to answer

- What task-level benchmarks matter most.
- How to measure factual recall, update handling, contradiction detection, matchmaking usefulness, and summary fidelity.
- What safety tests are required for memory poisoning, cross-domain leakage, sycophancy, and unauthorized retention.
- What multi-agent quality metrics matter.
- What cost and latency budgets are acceptable for online interaction and offline consolidation.
- What offline benchmark suite should run before rollout.
- What live acceptance tests should gate deployment.

## Included answers from current materials

- The first production slice must be evaluated before it is considered ready.
- The design spec should include evaluation thresholds for go or no-go.

## Still to answer

- The actual benchmark set.
- The acceptance thresholds.
- The relationship between guide quality, memory quality, and operational cost.
