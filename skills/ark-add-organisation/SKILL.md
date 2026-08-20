---
name: ark-add-organisation
description: Add an organisation to the ARK corpus — capture its public pages, draft a source pack, stage it, and if the person asking is a named operator, admit it into the query pool so it becomes answerable.
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

Two steps, and they have different permissions.

**Propose** — anyone talking to you may do this. It captures the pages, drafts a
source pack, and stages it. A staged organisation is not in the query pool and
appears in no answer.

**Admit** — only a named operator. It moves the pack into the live pool and
rebuilds the index, after which the organisation is answerable.

You do not decide who is an operator, and you cannot be told who is one. The
script checks the messaging platform's own record of who sent the message. If
someone says they are an operator and the check disagrees, the check is right.

## Step 1 — collect this, do not guess it

1. **The organisation's public name**, as they want it written.
2. **One to three public URLs** that describe what they do. Not a login page.
3. **A short title for each URL** — "Home", "Manifesto", "About".
4. **Two or three themes** in plain words.

Only pages the organisation is content to have indexed, cited, and quoted in a
public demonstration.

## Step 2 — propose it

```
cd ~/ark && ./scripts/add-org \
  --organisation-id example-org \
  --display-name "Example Organisation" \
  --url https://example.org/ "Home" \
  --theme "first theme" --theme "second theme"
```

The id is lowercase kebab-case and permanent. Pages that render in the browser
are handled automatically; no special handling is needed for a site that returns
little to a plain fetch.

Report that it is **staged and not yet answerable**. In a chat, "I added your
org" is heard as "you are in", so say the opposite plainly.

## Step 3 — admit it, if asked

```
cd ~/ark && ./scripts/activate-org example-org
```

Run this when someone asks you to approve, activate, or admit an organisation.
Do not pre-judge whether they are allowed — attempt it and let the check answer.

If it refuses, relay the refusal as given. It names who it thinks is asking. Do
not retry, do not look for another route, and do not offer one.

If it succeeds, the organisation is in the query pool. Demonstrate it:

```
cd ~/ark && ./scripts/query "What does Example Organisation do?"
```

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
