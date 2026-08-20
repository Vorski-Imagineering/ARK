---
name: ark-add-organisation
description: Add, approve, activate or admit an organisation in the ARK corpus. Run this instead of researching the site yourself.
version: 2.0.0
author: ARK hackathon
license: CC0-1.0
tags: [ark, onboarding, sources, organisations, operators]
platforms: [linux]
triggers:
  - add my organisation
  - add an org to ark
  - add us to ark
  - add this org
  - onboard my organisation
  - register our org
  - approve the org
  - activate the org
  - admit the org
  - who can add organisations
---

# Add an organisation to the ARK corpus

Anyone talking to you may add an organisation, and it becomes answerable
immediately. There is no approval step at present.

## Step 1 — collect this, do not guess it

1. **The organisation's public name**, as they want it written.
2. **One to three public URLs** that describe what they do. Not a login page.
3. **A short title for each URL** — "Home", "Manifesto", "About".
4. **Two or three themes** in plain words.

Only pages the organisation is content to have indexed, cited, and quoted in a
public demonstration. If the person is not from that organisation, ask whether
they have its agreement before adding it.

## Step 2 — add it

```
cd ~/ark && ./scripts/add-org \
  --organisation-id example-org \
  --display-name "Example Organisation" \
  --url https://example.org/ "Home" \
  --theme "first theme" --theme "second theme"
```

The id is lowercase kebab-case and permanent. Pages that render in the browser
are handled automatically; a site that returns little to a plain fetch needs no
special handling.

Then show it working:

```
cd ~/ark && ./scripts/query "What does Example Organisation do?"
```

## Say what has not happened

The organisation is answerable on this host. Nothing else is true yet, and each
of these is easy to skip past:

- **Not published.** The draft is on this host only. Publishing to the public
  repository is a human action.
- **Not approved.** The profile was extracted automatically from the page. It is
  a placeholder, not a description the organisation agreed to.
- **No representative named.** Someone from that organisation still has to take
  that role and confirm the material describes them accurately.

## If someone asks about approval or permissions

There is no approval gate right now: anything added goes live. The machinery for
a named-operator gate exists and is switched off. Point them at
`plan/ark-agent/permissions.md`, which explains how to turn it on.

## Check who is asking

```
cd ~/ark && ./scripts/ark-whoami
```

Use this when someone asks whether they can add or approve organisations.

## What remains true after a successful admit

Say these, because they are easy to skip past:

- **Not published.** The draft is on this host only. Publishing to the public
  repository is a human action.
- **Not approved.** The profile was extracted automatically from the page and is
  a placeholder, not a description the organisation agreed to.
- **No representative named.** Someone from that organisation still has to take
  that role and confirm the material describes them accurately.

## What you must not do

Do not add an organisation on someone's behalf without their agreement.

Do not edit `~/.ark-operators.json`, and do not tell anyone how to. If someone
asks to be made an operator, say that an existing operator has to do it on the
host directly.

Do not push to the repository.
