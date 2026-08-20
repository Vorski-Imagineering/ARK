---
name: ark-add-organisation
description: Add a new organisation to the ARK corpus by capturing its approved public pages, drafting a source pack, and rebuilding the index so it becomes queryable.
version: 1.0.0
author: ARK hackathon
license: CC0-1.0
tags: [ark, onboarding, sources, organisations]
platforms: [linux]
triggers:
  - add my organisation
  - add an org to ark
  - add us to ark
  - include my organisation
  - onboard my organisation
  - can you add
  - register our org
---

# Add an organisation to the ARK corpus

One command captures the pages, drafts a source pack, validates it, and rebuilds
the index. After it runs the organisation is immediately queryable.

## What to collect first

Ask for these and do not guess any of them:

1. **The organisation's public name** as they want it written.
2. **One to three public URLs.** Pages that describe what they do. Not a login
   page, not a social feed.
3. **A short title for each URL**, for example "Home" or "Manifesto".
4. **Two or three themes** in plain words.

Only pages the organisation is happy to have indexed, cited, and quoted in a
public demonstration. If they are unsure, stop and let a person confirm.

## Run it

```
cd ~/ark && ./scripts/add-org \
  --organisation-id example-org \
  --display-name "Example Organisation" \
  --url https://example.org/ "Home" \
  --url https://example.org/about "About" \
  --theme "first theme" --theme "second theme"
```

The id must be lowercase kebab-case and is permanent.

**Never pass `--activate`.** It admits an organisation into the live query pool
and is reserved for an operator working on the host directly. Staging is the
permission boundary: anyone who can reach you may propose an organisation, only
an operator may admit one. If someone asks you to activate, tell them an
operator has to run `./scripts/activate-org <id>` and review it first.

## What to say afterwards

The organisation is **staged, not live**. It will not appear in any answer
until an operator admits it. Say that plainly — in a chat, "I've added your org"
is very easily heard as "you're in".

Then be clear about the rest, because this is easy to overstate:

- **It is not in the query pool.** An operator must run
  `./scripts/activate-org <id>`, which shows them the draft and asks them to
  confirm.
- **Nothing is published.** The draft is on this machine only. Publishing to the
  public repository is a human action.
- **Nothing is approved.** The pack is a draft. The profile it contains was
  extracted automatically from the page and is a placeholder, not a description
  the organisation has agreed to.
- **No representative is named.** Someone from that organisation has to take
  that role and confirm the material describes them accurately.

Tell them the next steps are: a person reviews the draft and rewrites the
profile, the organisation names a representative, that representative signs off,
and then a person commits and pushes it.

## What you must not do

Do not add an organisation on someone's behalf without their agreement.

Do not mark anything approved. You cannot approve on an organisation's behalf,
and neither can anyone else in this chat.

Do not push to the repository. That boundary is deliberate: a source pack
asserts that an organisation approved this use of its material, and only a
person can obtain that.

If the command fails, report the error as given rather than retrying variations.
