# 11. Deployment, Scaling, And Operations

## Purpose

Define how the framework is deployed and operated as a multi-agent platform.

## Topics to answer

- The first deployment shape.
- How many concurrent project agents and conversation agents the first architecture should support.
- How secrets, credentials, and per-agent identities are managed.
- What background jobs, queues, and schedulers are required.
- What observability is required for runs, memory writes, failures, and dream sweeps.
- What the backup and disaster-recovery requirements are.
- What operational limits should exist on token budgets, sweep frequency, and background job concurrency.
- What scale assumptions should shape the v1 design.

## Included answers from current materials

- METIS is being framed as a shared framework that must support many agents, not just one project-specific install.

## Still to answer

- The initial deployment architecture.
- The concurrency and scale assumptions.
- The operational controls and observability model.
