# ChatGPT Project Export

This repo now includes a dependency-free exporter at
[`scripts/chatgpt_project_to_markdown.py`](/Users/vvorski/dev/ark/scripts/chatgpt_project_to_markdown.py)
that turns a ChatGPT data export into repository-friendly Markdown.

## What It Does

- Accepts a ChatGPT export `.zip`, an extracted export folder, or a direct `conversations.json` path
- Writes one `.md` file per conversation
- Copies any exported files it can resolve from message metadata into a sibling `assets/` folder
- Produces an `inventory.json` so you can audit what was exported and what could not be resolved
- Supports a best-effort `--project` filter for exports that include project metadata

## Usage

From the repo root:

```bash
python3 scripts/chatgpt_project_to_markdown.py \
  ~/Downloads/chatgpt-export.zip \
  --output-dir imports/my-chatgpt-project \
  --project "My ChatGPT Project" \
  --overwrite
```

If you want to export everything in the archive, omit `--project`.

## Output Layout

```text
imports/my-chatgpt-project/
├── README.md
├── inventory.json
├── assets/
│   └── <conversation-slug>/
└── threads/
    └── <conversation-slug>.md
```

## Notes

- File capture is best-effort. If the export contains only an internal pointer and not the actual file bytes, the exporter will list that reference under `Unresolved file references`.
- The script preserves the raw conversational record instead of trying to summarize or reshape it.
- Project filtering depends on metadata actually being present in your export; if nothing matches, run once without `--project` and inspect `inventory.json`.
