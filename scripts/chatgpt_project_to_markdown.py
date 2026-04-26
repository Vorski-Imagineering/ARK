#!/usr/bin/env python3
"""
Convert a ChatGPT data export into repository-friendly Markdown files.

The script accepts either:
- an extracted ChatGPT export directory
- a ChatGPT export zip file
- a direct path to conversations.json

It emits one Markdown file per conversation plus any resolvable exported files
referenced by messages.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import tempfile
import zipfile
from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse


FILE_LIKE_KEYS = {
    "asset_pointer",
    "download_url",
    "file",
    "file_id",
    "file_ids",
    "file_name",
    "filename",
    "files",
    "image",
    "image_url",
    "local_path",
    "path",
    "sandbox_path",
    "url",
}

TEXT_EXTENSIONS = {
    ".c",
    ".cc",
    ".cpp",
    ".css",
    ".csv",
    ".doc",
    ".docx",
    ".gif",
    ".heic",
    ".html",
    ".ipynb",
    ".jpeg",
    ".jpg",
    ".json",
    ".md",
    ".mov",
    ".mp3",
    ".mp4",
    ".pdf",
    ".png",
    ".ppt",
    ".pptx",
    ".py",
    ".rtf",
    ".svg",
    ".tar",
    ".tex",
    ".txt",
    ".wav",
    ".webm",
    ".webp",
    ".xls",
    ".xlsx",
    ".xml",
    ".yaml",
    ".yml",
    ".zip",
}

SKIP_EXPORT_FILES = {
    "chat.html",
    "conversations.json",
    "message_feedback.json",
    "model_comparisons.json",
    "user.json",
}


@dataclass(frozen=True)
class AssetRef:
    label: str
    raw: str
    source_path: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export ChatGPT conversations into Markdown files."
    )
    parser.add_argument(
        "source",
        help="Path to a ChatGPT export zip, extracted export directory, or conversations.json",
    )
    parser.add_argument(
        "--output-dir",
        default="imports/chatgpt-project",
        help="Directory inside the repo where Markdown files should be written",
    )
    parser.add_argument(
        "--project",
        help="Best-effort project name or project id filter",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Delete the output directory before exporting",
    )
    return parser.parse_args()


def slugify(value: str, fallback: str = "untitled") -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return cleaned or fallback


def to_iso8601(value: Any) -> str | None:
    if value in (None, ""):
        return None
    try:
        timestamp = float(value)
    except (TypeError, ValueError):
        return str(value)
    if timestamp > 10_000_000_000:
        timestamp /= 1000
    return datetime.fromtimestamp(timestamp, tz=UTC).isoformat()


def yaml_string(value: Any) -> str:
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text.strip("\n")


def load_export_root(source: Path) -> tuple[Path, Path, tempfile.TemporaryDirectory[str] | None]:
    if source.is_file() and source.suffix.lower() == ".zip":
        tempdir = tempfile.TemporaryDirectory(prefix="chatgpt-export-")
        with zipfile.ZipFile(source) as archive:
            archive.extractall(tempdir.name)
        root = Path(tempdir.name)
        conversations_path = find_conversations_json(root)
        return root, conversations_path, tempdir

    if source.is_file() and source.name == "conversations.json":
        return source.parent, source, None

    if source.is_dir():
        conversations_path = find_conversations_json(source)
        return source, conversations_path, None

    raise FileNotFoundError(f"Could not use source path: {source}")


def find_conversations_json(root: Path) -> Path:
    direct = root / "conversations.json"
    if direct.exists():
        return direct

    matches = list(root.rglob("conversations.json"))
    if not matches:
        raise FileNotFoundError(f"Could not find conversations.json under {root}")
    return matches[0]


def load_conversations(conversations_path: Path) -> list[dict[str, Any]]:
    with conversations_path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError("Expected conversations.json to contain a top-level list")
    return [item for item in data if isinstance(item, dict)]


def should_skip_export_file(path: Path) -> bool:
    if path.name in SKIP_EXPORT_FILES:
        return True
    return False


def build_export_file_index(root: Path) -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = defaultdict(list)
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if should_skip_export_file(path):
            continue
        index[path.name.lower()].append(path)
        index[path.stem.lower()].append(path)
    return index


def collect_project_metadata(obj: Any, trail: tuple[str, ...] = ()) -> list[dict[str, Any]]:
    collected: list[dict[str, Any]] = []
    if isinstance(obj, dict):
        matched = {
            key: value
            for key, value in obj.items()
            if "project" in key.lower() or "workspace" in key.lower()
        }
        if matched:
            collected.append(
                {
                    "path": ".".join(trail) or "<root>",
                    "values": matched,
                }
            )
        for key, value in obj.items():
            collected.extend(collect_project_metadata(value, trail + (str(key),)))
    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            collected.extend(collect_project_metadata(value, trail + (str(index),)))
    return collected


def project_strings(conversation: dict[str, Any]) -> list[str]:
    values: list[str] = []
    for metadata in collect_project_metadata(conversation):
        for value in metadata["values"].values():
            if isinstance(value, (str, int, float)):
                values.append(str(value))
    return values


def matches_project_filter(conversation: dict[str, Any], project_filter: str | None) -> bool:
    if not project_filter:
        return True
    needle = project_filter.strip().lower()
    if not needle:
        return True
    for candidate in project_strings(conversation):
        if needle in candidate.lower():
            return True
    return False


def path_depth(path: Path) -> int:
    return len(path.parts)


def basename_from_reference(value: str) -> str:
    parsed = urlparse(value)
    candidate = parsed.path or value
    if candidate.startswith("file-service://"):
        candidate = candidate.removeprefix("file-service://")
    if candidate.startswith("sandbox:/"):
        candidate = candidate.split("/")[-1]
    candidate = candidate.split("?")[0].split("#")[0]
    return Path(candidate).name


def looks_file_like(value: str) -> bool:
    lower = value.lower()
    if lower.startswith(("http://", "https://", "sandbox:/", "file-service://")):
        return True
    suffix = Path(basename_from_reference(value)).suffix.lower()
    return suffix in TEXT_EXTENSIONS


def collect_asset_refs(obj: Any, trail: tuple[str, ...] = ()) -> list[AssetRef]:
    refs: list[AssetRef] = []
    if isinstance(obj, dict):
        label = first_non_empty(
            obj.get("filename"),
            obj.get("file_name"),
            obj.get("title"),
            obj.get("name"),
        )

        for key, value in obj.items():
            key_lower = key.lower()
            next_trail = trail + (key,)

            if isinstance(value, str) and (
                key_lower in FILE_LIKE_KEYS
                or "attachment" in key_lower
                or "asset" in key_lower
                or key_lower.endswith("_url")
                or key_lower.endswith("_path")
                or key_lower.endswith("_pointer")
                or key_lower.endswith("_file")
            ):
                if looks_file_like(value):
                    refs.append(
                        AssetRef(
                            label=label or basename_from_reference(value) or key,
                            raw=value,
                            source_path=".".join(next_trail),
                        )
                    )

            if isinstance(value, list) and key_lower in FILE_LIKE_KEYS:
                for item in value:
                    if isinstance(item, str) and looks_file_like(item):
                        refs.append(
                            AssetRef(
                                label=label or basename_from_reference(item) or key,
                                raw=item,
                                source_path=".".join(next_trail),
                            )
                        )

            refs.extend(collect_asset_refs(value, next_trail))

    elif isinstance(obj, list):
        for index, value in enumerate(obj):
            refs.extend(collect_asset_refs(value, trail + (str(index),)))

    return dedupe_asset_refs(refs)


def dedupe_asset_refs(refs: Iterable[AssetRef]) -> list[AssetRef]:
    deduped: list[AssetRef] = []
    seen: set[tuple[str, str]] = set()
    for ref in refs:
        basename = basename_from_reference(ref.raw).lower()
        key = (ref.label.lower(), basename or ref.raw)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(ref)
    return deduped


def first_non_empty(*values: Any) -> str | None:
    for value in values:
        if isinstance(value, str) and value.strip():
            return value.strip()
    return None


def find_best_file_match(ref: AssetRef, file_index: dict[str, list[Path]]) -> Path | None:
    candidates: list[Path] = []
    possible_keys = {
        basename_from_reference(ref.raw).lower(),
        ref.label.lower(),
        Path(ref.label).stem.lower(),
    }
    for key in possible_keys:
        if not key:
            continue
        candidates.extend(file_index.get(key, []))

    if not candidates:
        return None

    ranked = sorted(
        set(candidates),
        key=lambda path: (
            path_depth(path),
            len(path.name),
            path.as_posix(),
        ),
    )
    return ranked[0]


def safe_copy_asset(src: Path, dest_dir: Path, used_names: set[str]) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    target_name = src.name
    stem = src.stem
    suffix = src.suffix
    counter = 2
    while target_name.lower() in used_names:
        target_name = f"{stem}-{counter}{suffix}"
        counter += 1
    used_names.add(target_name.lower())
    target = dest_dir / target_name
    shutil.copy2(src, target)
    return target


def render_content(content: Any) -> str:
    if not isinstance(content, dict):
        return ""

    content_type = content.get("content_type")
    parts = content.get("parts")

    if isinstance(parts, list):
        rendered_parts = [render_part(part) for part in parts]
        body = "\n\n".join(part for part in rendered_parts if part)
        if body:
            return body

    if content_type == "text" and isinstance(content.get("text"), str):
        return normalize_text(content["text"])

    if "result" in content and isinstance(content["result"], str):
        return normalize_text(content["result"])

    fallback = content.get("text") or content.get("caption")
    if isinstance(fallback, str):
        return normalize_text(fallback)

    return ""


def render_part(part: Any) -> str:
    if isinstance(part, str):
        return normalize_text(part)

    if isinstance(part, dict):
        text = first_non_empty(
            part.get("text"),
            part.get("caption"),
            part.get("title"),
            part.get("alt_text"),
            part.get("prompt"),
        )
        if text:
            return normalize_text(text)
        if looks_like_image_part(part):
            label = first_non_empty(part.get("title"), part.get("name")) or "Image"
            return f"[{label} omitted from text export]"
        return normalize_text(json.dumps(part, ensure_ascii=False, indent=2))

    return normalize_text(str(part))


def looks_like_image_part(part: dict[str, Any]) -> bool:
    joined_keys = " ".join(part.keys()).lower()
    return "image" in joined_keys or "asset" in joined_keys


def extract_model_slug(message: dict[str, Any]) -> str | None:
    metadata = message.get("metadata")
    if not isinstance(metadata, dict):
        return None
    return first_non_empty(
        metadata.get("model_slug"),
        metadata.get("default_model_slug"),
        metadata.get("requested_model_slug"),
    )


def collect_messages(conversation: dict[str, Any]) -> list[dict[str, Any]]:
    mapping = conversation.get("mapping")
    if not isinstance(mapping, dict):
        return []

    messages: list[dict[str, Any]] = []
    for node_id, node in mapping.items():
        if not isinstance(node, dict):
            continue
        message = node.get("message")
        if not isinstance(message, dict):
            continue
        role = ((message.get("author") or {}).get("role")) or "unknown"
        created = message.get("create_time")
        if created is None:
            created = node.get("create_time")
        messages.append(
            {
                "node_id": node_id,
                "parent_id": node.get("parent"),
                "role": role,
                "author_name": ((message.get("author") or {}).get("name")) or "",
                "created_at": created,
                "created_at_iso": to_iso8601(created),
                "model_slug": extract_model_slug(message),
                "recipient": message.get("recipient"),
                "status": message.get("status"),
                "content": render_content(message.get("content")),
                "asset_refs": collect_asset_refs(message),
            }
        )

    messages.sort(
        key=lambda item: (
            item["created_at"] is None,
            item["created_at"] if item["created_at"] is not None else float("inf"),
            str(item["node_id"]),
        )
    )
    return messages


def markdown_for_conversation(
    conversation: dict[str, Any],
    messages: list[dict[str, Any]],
    asset_links: dict[str, list[str]],
    unresolved_assets: dict[str, list[AssetRef]],
) -> str:
    title = first_non_empty(conversation.get("title")) or "Untitled Chat"
    conversation_id = conversation.get("id")
    created_at = to_iso8601(conversation.get("create_time"))
    updated_at = to_iso8601(conversation.get("update_time"))
    project_meta = collect_project_metadata(conversation)

    lines = [
        "---",
        f"title: {yaml_string(title)}",
        f"conversation_id: {yaml_string(conversation_id)}",
        f"created_at: {yaml_string(created_at)}",
        f"updated_at: {yaml_string(updated_at)}",
        f"message_count: {len(messages)}",
        "---",
        "",
        f"# {title}",
        "",
        f"- Conversation ID: `{conversation_id}`" if conversation_id else "- Conversation ID: unknown",
        f"- Created: `{created_at}`" if created_at else "- Created: unknown",
        f"- Updated: `{updated_at}`" if updated_at else "- Updated: unknown",
    ]

    if project_meta:
        lines.append("- Project metadata:")
        for entry in project_meta:
            compact = json.dumps(entry["values"], ensure_ascii=False, sort_keys=True)
            lines.append(f"  - `{entry['path']}`: `{compact}`")

    lines.extend(["", "## Messages", ""])

    for index, message in enumerate(messages, start=1):
        role = str(message["role"]).title()
        lines.append(f"### {index:03d}. {role}")
        lines.append("")
        lines.append(f"- Node ID: `{message['node_id']}`")
        if message["parent_id"]:
            lines.append(f"- Parent ID: `{message['parent_id']}`")
        if message["created_at_iso"]:
            lines.append(f"- Timestamp: `{message['created_at_iso']}`")
        if message["author_name"]:
            lines.append(f"- Author Name: `{message['author_name']}`")
        if message["model_slug"]:
            lines.append(f"- Model: `{message['model_slug']}`")
        if message["recipient"]:
            lines.append(f"- Recipient: `{message['recipient']}`")
        if message["status"]:
            lines.append(f"- Status: `{message['status']}`")
        lines.append("")

        body = message["content"] or "_[No text content exported]_"
        lines.append(body)
        lines.append("")

        if asset_links.get(message["node_id"]):
            lines.append("Files:")
            for relative_path in asset_links[message["node_id"]]:
                lines.append(f"- [{Path(relative_path).name}]({relative_path})")
            lines.append("")

        if unresolved_assets.get(message["node_id"]):
            lines.append("Unresolved file references:")
            for ref in unresolved_assets[message["node_id"]]:
                lines.append(f"- `{ref.label}` from `{ref.source_path}`: `{ref.raw}`")
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def export_conversations(
    conversations: list[dict[str, Any]],
    output_dir: Path,
    file_index: dict[str, list[Path]],
    project_filter: str | None,
) -> dict[str, Any]:
    threads_dir = output_dir / "threads"
    assets_dir = output_dir / "assets"
    threads_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(parents=True, exist_ok=True)

    summary: list[dict[str, Any]] = []
    used_slugs: set[str] = set()

    filtered = [conv for conv in conversations if matches_project_filter(conv, project_filter)]

    for conversation in filtered:
        title = first_non_empty(conversation.get("title")) or "Untitled Chat"
        conversation_id = str(conversation.get("id") or "no-id")
        base_slug = slugify(title)
        short_id = slugify(conversation_id)[:8] or "chat"
        slug = base_slug
        if slug in used_slugs:
            slug = f"{base_slug}-{short_id}"
        used_slugs.add(slug)

        messages = collect_messages(conversation)
        message_asset_links: dict[str, list[str]] = defaultdict(list)
        unresolved_assets: dict[str, list[AssetRef]] = defaultdict(list)
        used_asset_names: set[str] = set()

        for message in messages:
            for ref in message["asset_refs"]:
                match = find_best_file_match(ref, file_index)
                if match is None:
                    unresolved_assets[message["node_id"]].append(ref)
                    continue
                copied = safe_copy_asset(match, assets_dir / slug, used_asset_names)
                relative = os.path.relpath(copied, threads_dir)
                message_asset_links[message["node_id"]].append(relative)

        markdown = markdown_for_conversation(
            conversation=conversation,
            messages=messages,
            asset_links=message_asset_links,
            unresolved_assets=unresolved_assets,
        )

        target = threads_dir / f"{slug}.md"
        target.write_text(markdown, encoding="utf-8")

        summary.append(
            {
                "conversation_id": conversation_id,
                "title": title,
                "slug": slug,
                "project_strings": project_strings(conversation),
                "markdown_path": str(target),
                "message_count": len(messages),
                "copied_files": sum(len(items) for items in message_asset_links.values()),
                "unresolved_files": sum(len(items) for items in unresolved_assets.values()),
            }
        )

    write_index(output_dir, summary, project_filter)
    return {
        "conversation_count": len(summary),
        "summary": summary,
    }


def write_index(output_dir: Path, summary: list[dict[str, Any]], project_filter: str | None) -> None:
    readme_path = output_dir / "README.md"
    inventory_path = output_dir / "inventory.json"

    inventory_path.write_text(
        json.dumps(
            {
                "project_filter": project_filter,
                "conversations": summary,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    lines = [
        "# ChatGPT Project Export",
        "",
        "This folder was generated by `scripts/chatgpt_project_to_markdown.py`.",
        "",
        f"- Project filter: `{project_filter or 'none'}`",
        f"- Conversations exported: `{len(summary)}`",
        f"- Inventory: [inventory.json](inventory.json)",
        "",
        "## Threads",
        "",
    ]

    for item in summary:
        relative = os.path.relpath(item["markdown_path"], output_dir)
        lines.append(
            f"- [{item['title']}]({relative}) "
            f"({item['message_count']} messages, {item['copied_files']} files, {item['unresolved_files']} unresolved)"
        )

    if not summary:
        lines.append("- No conversations matched the current filter.")

    readme_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    source = Path(args.source).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve()

    if args.overwrite and output_dir.exists():
        shutil.rmtree(output_dir)

    export_root, conversations_path, tempdir = load_export_root(source)
    try:
        conversations = load_conversations(conversations_path)
        file_index = build_export_file_index(export_root)
        result = export_conversations(
            conversations=conversations,
            output_dir=output_dir,
            file_index=file_index,
            project_filter=args.project,
        )
    finally:
        if tempdir is not None:
            tempdir.cleanup()

    print(
        json.dumps(
            {
                "output_dir": str(output_dir),
                "conversation_count": result["conversation_count"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
