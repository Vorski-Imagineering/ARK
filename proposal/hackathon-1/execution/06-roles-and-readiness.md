# ARC Agent hackathon — roles and readiness

**Status:** Draft. Role ownership itself is not duplicated here — see `00-start-here.md`'s Mandatory owners table for who holds each role and the Decision and readiness gates for pass/fail status. This file covers coordination mechanics, contribution cadence, and mid-sprint onboarding that aren't specified elsewhere.
**Scope:** Coordination channels, push/PR cadence, and onboarding for contributors who join after Day 1.

## Coordination channels

- Which tool serves which function (video room, coordination chat, repository, shared working surface, delivery channel, starter-agent access) is set in `00-start-here.md`'s Minimal remote workspace table — fill that in, don't re-pick here.
- Telegram is already partially live: GitHub Actions post issue open/close/reopen, every push to `main`, and deploy-tag events to a Telegram dev chat (`.github/workflows/telegram-issues.yml`, `telegram-main-merge.yml`, `telegram-tag-deploy.yml`). That's repo-automation for the build team, separate from the participant-facing ARC Agent Telegram bot described as a conditional feature in `05-technical-specification.md` §7 — don't conflate the two when briefing participants.
- No side-channel decisions: anything the group should know goes in the coordination chat or the repo, not a DM.

## Push and PR cadence

`05-technical-specification.md` requires feature branches or small pull requests but doesn't set a cadence. Proposed defaults for the two build days:

- Push at least every 3 hours during active work sessions, including work-in-progress or broken states — visibility matters more than completeness.
- Open a draft PR when starting a new piece of work, even before code exists. Use the description as a live "here's what I'm doing" signal others can see, comment on, or offer to pair on.
- Prefer small PRs that merge over large ones that stall.
- One person holds convergence duty per shift — watching PRs, merging cleanly, keeping `main` runnable — rotating roughly every 4 hours.

## Onboarding mid-sprint

`05-technical-specification.md` §7A's access-lifecycle table already covers *removing* a participant ("Start of Day 1: confirm participant allow group and remove absent or replaced participants"). This covers *adding* one:

- An existing contributor vouches for the new person and spends ~30 minutes bringing them up to speed.
- The new contributor reads: this file, `00-start-here.md`, and the last 24 hours of the coordination channel.
- No expectation of full-cycle contribution — they contribute where they can for the time remaining.
