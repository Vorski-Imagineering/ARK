"""Resolve who is asking, and whether they may admit an organisation.

The identity used here comes from the messaging platform, recorded by the
runtime when the session opened. It is not taken from the message text, so
someone typing "I am an operator" does not become one.

Enforcement lives in this script rather than in the agent's instructions. An
instruction is a request the model may or may not honour; a check the model
cannot bypass is a boundary. The agent is free to attempt an activation — it
simply fails unless the person who asked is on the operator list.

The operator list is a host file, deliberately not in the repository: it holds
platform user identifiers, which are personal data and do not belong in a
public CC0 repository.
"""

import json
import os
import sqlite3
import sys
from pathlib import Path

STATE_DB = Path.home() / ".hermes/state.db"
OPERATORS_FILE = Path(
    os.environ.get("ARK_OPERATORS_FILE", Path.home() / ".ark-operators.json")
)
RECENT_FALLBACK_SECONDS = 900


class Identity:
    def __init__(self, user_id, user_name, platform, source, chat_type="unknown"):
        self.user_id = user_id
        self.user_name = user_name
        self.platform = platform
        self.source = source
        self.chat_type = chat_type

    def __str__(self):
        who = self.user_name or "unknown"
        return f"{who} ({self.platform}:{self.user_id}) via {self.source}"


def _origin_for_session(session_id: str) -> dict | None:
    if not STATE_DB.exists():
        return None
    connection = sqlite3.connect(f"file:{STATE_DB}?mode=ro", uri=True)
    try:
        row = connection.execute(
            "SELECT origin_json, chat_type FROM sessions WHERE id = ?", (session_id,)
        ).fetchone()
    finally:
        connection.close()
    if not row or not row[0]:
        return None
    try:
        origin = json.loads(row[0])
    except json.JSONDecodeError:
        return None
    origin["_chat_type"] = row[1] or origin.get("chat_type") or "unknown"
    return origin


def _latest_platform_origin() -> tuple[dict | None, str]:
    """Most recent non-CLI session. Used only when the runtime gave us no id."""
    if not STATE_DB.exists():
        return None, "no-state-db"
    connection = sqlite3.connect(f"file:{STATE_DB}?mode=ro", uri=True)
    try:
        row = connection.execute(
            "SELECT origin_json, started_at FROM sessions "
            "WHERE source != 'cli' AND origin_json IS NOT NULL "
            "ORDER BY started_at DESC LIMIT 1"
        ).fetchone()
    finally:
        connection.close()
    if not row or not row[0]:
        return None, "no-platform-session"
    try:
        return json.loads(row[0]), "latest-session-fallback"
    except json.JSONDecodeError:
        return None, "unparseable-origin"


def resolve_identity() -> Identity | None:
    """Determine who is asking, preferring the runtime-supplied session id."""
    session_id = os.environ.get("HERMES_SESSION_ID", "").strip()
    if session_id:
        origin = _origin_for_session(session_id)
        if origin:
            return Identity(
                str(origin.get("user_id") or ""),
                origin.get("user_name"),
                origin.get("platform", "unknown"),
                "session-id",
                origin.get("_chat_type", "unknown"),
            )

    origin, why = _latest_platform_origin()
    if origin:
        return Identity(
            str(origin.get("user_id") or ""),
            origin.get("user_name"),
            origin.get("platform", "unknown"),
            why,
        )
    return None


def load_operators() -> dict:
    if not OPERATORS_FILE.exists():
        return {"operators": []}
    try:
        return json.loads(OPERATORS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"operators": []}


def is_operator(identity: Identity | None) -> tuple[bool, str]:
    if identity is None or not identity.user_id:
        return False, "could not determine who is asking"

    # A group thread is a shared session. Its recorded identity is whoever
    # opened the thread, not whoever sent the current message, so anyone
    # posting in an operator's thread would inherit that operator's rights.
    # Identity is only unambiguous in a one-to-one chat.
    if identity.chat_type in {"group", "forum", "channel", "supergroup"}:
        return False, (
            "this is a shared group thread, where the session identity belongs to "
            "whoever opened the thread rather than to whoever sent this message. "
            "Send me a direct message to approve an organisation."
        )

    data = load_operators()
    for entry in data.get("operators", []):
        if str(entry.get("user_id")) == identity.user_id and entry.get(
            "platform", "telegram"
        ) == identity.platform:
            return True, f"{entry.get('label', 'operator')}"
    return False, f"{identity} is not on the operator list"


def main() -> int:
    command = sys.argv[1] if len(sys.argv) > 1 else "whoami"
    identity = resolve_identity()

    if command == "whoami":
        if identity is None:
            print("caller: unknown (no platform session found)")
            return 1
        allowed, reason = is_operator(identity)
        print(f"caller:   {identity}")
        print(f"operator: {'yes' if allowed else 'no'} — {reason}")
        return 0

    if command == "check":
        allowed, reason = is_operator(identity)
        if allowed:
            print(f"operator confirmed: {identity}")
            return 0
        print(f"REFUSED: {reason}", file=sys.stderr)
        print(
            "Only a named operator may admit an organisation into the query pool.",
            file=sys.stderr,
        )
        return 1

    print(f"usage: {sys.argv[0]} [whoami|check]", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
