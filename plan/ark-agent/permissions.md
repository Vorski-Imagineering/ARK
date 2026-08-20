# Who may add an organisation

**Current setting: `auto`. Anyone talking to the agent can add an organisation
and it becomes answerable immediately.**

That is deliberate for now. While the group is experimenting, the cost of a
wrong organisation appearing is a one-line fix, and the cost of friction is that
nobody tries it. The machinery for a stricter mode is built and tested; it is
switched off, not absent.

This document is how to switch it on.

---

## The two modes

| Mode | Proposing | Admitting into the query pool |
|---|---|---|
| `auto` *(current)* | Anyone | Automatic, immediate |
| `operator` | Anyone | A named operator, from a direct message |

Set with the `ARK_APPROVAL_MODE` environment variable. Unset means `auto`.

```
./scripts/ark-whoami mode      # prints the current mode
```

## Turning approval on

**1. Create the operator list on the host.** Never in this repository — it holds
platform user identifiers, which are personal data, and this repository is
public and CC0.

```
~/.ark-operators.json          # chmod 600
```

```json
{
  "operators": [
    { "platform": "telegram", "user_id": "<numeric id>", "label": "event lead" }
  ]
}
```

**2. Find someone's platform id.** It is recorded automatically the first time
they message the agent. On the host:

```
python3 - <<'EOF'
import sqlite3, json
c = sqlite3.connect('file:$HOME/.hermes/state.db?mode=ro', uri=True)
for r in c.execute("SELECT origin_json FROM sessions WHERE source!='cli' ORDER BY started_at DESC LIMIT 20"):
    o = json.loads(r[0]); print(o.get('user_name'), o.get('user_id'), o.get('chat_type'))
EOF
```

Do not paste that output anywhere public.

**3. Set the mode** where the agent runs, so it applies to every invocation:

```
ARK_APPROVAL_MODE=operator
```

**4. Restart the gateway** and confirm:

```
./scripts/ark-whoami mode      # expect: operator
./scripts/ark-whoami           # expect: your name, operator yes/no
```

## How the check works, and its one real constraint

Identity comes from the messaging platform's own record of who opened the
session. It is never taken from the message text, so someone typing "I am an
operator" does not become one. The check runs inside the script rather than in
the agent's instructions — an instruction is a request a model may ignore, a
check it cannot bypass is a boundary.

**Approval requires a direct message, and this is not a preference.** A group
thread is a long-lived shared session, and the identity recorded on it belongs
to whoever *opened the thread*, not to whoever sent the current message. This
was verified on the live server: one group thread carried 125 messages across
two days under a single recorded user.

So in a group, anyone posting in an operator's thread would inherit that
operator's rights, and an operator posting in someone else's thread would be
refused. Identity is only unambiguous in a one-to-one chat, so `operator` mode
refuses to admit anything from a group thread and says why.

`[OPEN QUESTION: If per-message sender identity is later exposed to a skill, group-thread approval becomes safe and this constraint can be lifted. Owner: technical lead.]`

## What approval does not cover

Admitting an organisation makes it answerable on that host. It does not publish
anything to this repository, and it does not mean the organisation approved how
it is described. Those are separate, and both require a person:

- the auto-extracted profile is a placeholder until someone rewrites it
- a representative must be named and must sign off
- a person commits and pushes

See the sign-off blocks in each source pack, and the approval question in
`open-questions.md`.

## Turning it back off

Unset `ARK_APPROVAL_MODE`, or set it to `auto`, and restart. The operator list
can stay in place; it is simply not consulted.
