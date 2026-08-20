# Notice — what CC0 covers here, and what it cannot

This repository is dedicated to the public domain under CC0 1.0. That dedication
is ours to make **only for the material we authored**.

## CC0 applies to

- the application code, scripts, and tests
- the proposal, plan, execution, and research writing
- the source-pack metadata: organisation identifiers, selected URLs, titles,
  permission basis, themes, representative questions
- the capture configuration and snapshot manifests

## CC0 does not — and cannot — apply to

**Captured content from participating organisations' websites.** Those are other
people's words, published by them under their own rights. We have no standing to
dedicate them to the public domain, and stamping CC0 on them would assert a
relicensing power nobody here holds.

Each organisation's material remains under whatever terms that organisation
publishes it. The permission recorded in a source pack
(`open-reuse`, `experiment-use`, `link-and-summarise`) describes what that
organisation has agreed we may do with it — it is not a licence we grant onward.

## What changed on 2026-08-20

Rendered snapshots of four organisations' pages were briefly committed here.
That was a mistake: it placed third-party content inside a CC0 repository and
implied a dedication we cannot make.

The snapshots have been removed from the working tree and are no longer tracked.
They are held on the project server instead.

**The Git history still contains them.** Removing a file from the current commit
does not remove it from earlier commits. If the group wants that history
rewritten, it needs a coordinated force-push that everyone with a clone must
respond to, so it is a decision for the repository owner rather than something to
do unilaterally. Either way, this notice records that no CC0 dedication was ever
validly made over that content.

## How the corpus stays reproducible

The repository holds the **instructions to fetch**, not the fetched content:

- `proposal/hackathon-1/execution/snapshots/sources.json` — which URLs, which
  titles, and the redaction list
- `scripts/capture-snapshots.mjs` — the capture tool
- `proposal/hackathon-1/execution/source-packs/*.md` — permission basis per source

Anyone can rebuild the corpus by running the capture against those instructions.
This is the pattern the technical specification already anticipated: *"Git-tracked
text/markdown where rights permit; otherwise reproducible fetch instructions."*
[see: proposal/hackathon-1/execution/05-technical-specification.md#canonical-and-derived-layers]

## Attribution

Generated answers cite the source they came from and resolve it to a public URL.
A citation that does not resolve to a real source is dropped rather than shown.
Provenance is enforced by the code, not promised by a policy.
