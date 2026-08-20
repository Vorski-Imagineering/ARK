"""Run the Phase 1 acceptance set against the real model and write a review sheet.

Not part of the test suite. Calls a real model, so it is slow, costs whatever
the provider charges, and is not reproducible. It never gates a build unit.

Its output is a document for humans: each question, the answer, the sources
cited with their public URLs, and empty fields for a representative to mark
whether the answer is accurate.
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import yaml  # noqa: E402

from app.answer import answer  # noqa: E402
from app.digest import digest  # noqa: E402
from app.index import Index  # noqa: E402
from app.llm import HermesLLM  # noqa: E402
from app.source_pack import load_source_pack  # noqa: E402
from app.usage import Usage, estimate_cost, log_run  # noqa: E402

QUESTIONS = Path(__file__).resolve().parent / "questions.yaml"
OUT_DIR = Path(__file__).resolve().parent / "outputs"
PACK_DIR = Path("proposal/hackathon-1/execution/source-packs")


def _source_urls() -> dict[str, str]:
    """Map every source id to its public URL, so citations are checkable."""
    urls: dict[str, str] = {}
    for path in sorted(PACK_DIR.glob("*.md")):
        pack = load_source_pack(path)
        for source in pack.sources:
            urls[source.source_id] = source.canonical_url
    return urls


def _display_names() -> dict[str, str]:
    names: dict[str, str] = {}
    for path in sorted(PACK_DIR.glob("*.md")):
        pack = load_source_pack(path)
        names[pack.organisation.organisation_id] = pack.organisation.display_name
    return names


def _render(record, urls: dict[str, str], heading: str) -> str:
    lines = [f"### {heading}", ""]
    lines.append(f"**Question or scope:** {record.question_or_digest_scope}")
    lines.append("")
    lines.append("**Answer**")
    lines.append("")
    lines.append("> " + record.output.replace("\n", "\n> "))
    lines.append("")
    lines.append("**Cited sources**")
    lines.append("")
    if record.cited_source_ids:
        for source_id in record.cited_source_ids:
            lines.append(f"- `{source_id}` — {urls.get(source_id, 'URL NOT FOUND')}")
    else:
        lines.append("- (none)")
    lines.append("")
    if record.limitations:
        lines.append("**Limitations recorded by the system**")
        lines.append("")
        for limitation in record.limitations:
            lines.append(f"- {limitation}")
        lines.append("")
    lines.append(f"**Refused as insufficient evidence:** {record.insufficient_evidence}")
    lines.append("")
    lines.append(
        f"**Usage:** in={record.usage.input_tokens} out={record.usage.output_tokens} "
        f"est_usd={record.usage.estimated_cost_usd:.6f}  ·  model `{record.model}`"
    )
    lines.append("")
    lines.append("| Reviewer field | |")
    lines.append("|---|---|")
    lines.append("| Accurate? (yes / no) | |")
    lines.append("| Material misrepresentation? | |")
    lines.append("| Notes | |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the Phase 1 acceptance set")
    parser.add_argument("--index", default="index/active.sqlite3")
    parser.add_argument("--k", type=int, default=8)
    parser.add_argument("--limit-organisations", type=int, default=None)
    parser.add_argument(
        "--skip-per-organisation",
        action="store_true",
        help="run only the cross-organisation and negative questions",
    )
    args = parser.parse_args()

    config = yaml.safe_load(QUESTIONS.read_text(encoding="utf-8"))
    index = Index.open(Path(args.index))
    llm = HermesLLM()
    urls = _source_urls()
    names = _display_names()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = OUT_DIR / f"{stamp}.md"
    run_log = OUT_DIR / "runs.jsonl"

    parts = [
        f"# Phase 1 evaluation — {stamp}",
        "",
        f"Index: `{args.index}`  ·  chunks: {index.count()}  ·  k={args.k}",
        "",
        "A representative reviews only their own organisation's section. Mark "
        "Accurate as yes or no and note any material misrepresentation.",
        "",
        "---",
        "",
    ]

    records: list = []

    if not args.skip_per_organisation:
        organisations = config["organisations"]
        if args.limit_organisations:
            organisations = organisations[: args.limit_organisations]
        for organisation_id in organisations:
            display = names.get(organisation_id, organisation_id)
            parts.append(f"## {display}")
            parts.append("")
            for question in config["per_organisation"]:
                text = question["text"].replace("this organisation", display)
                print(f"  [{organisation_id}/{question['id']}] {text}", flush=True)
                record = answer(text, index, llm, k=args.k)
                records.append(("answer", record))
                parts.append(_render(record, urls, f"{question['id']}"))
            parts.append("---")
            parts.append("")

    parts.append("## Cross-organisation question")
    parts.append("")
    parts.append(
        "_This is the question that proves the phase. It cannot be answered "
        "from a single-organisation index._"
    )
    parts.append("")
    for question in config["cross_organisation"]:
        print(f"  [cross/{question['id']}]", flush=True)
        record = answer(question["text"].strip(), index, llm, k=args.k * 2)
        records.append(("answer", record))
        parts.append(_render(record, urls, question["id"]))

    parts.append("---")
    parts.append("")
    parts.append("## Negative question")
    parts.append("")
    for question in config["negative"]:
        parts.append(f"_Expectation: {question['expectation'].strip()}_")
        parts.append("")
        print(f"  [negative/{question['id']}]", flush=True)
        record = answer(question["text"], index, llm, k=args.k)
        records.append(("answer", record))
        parts.append(_render(record, urls, question["id"]))

    parts.append("---")
    parts.append("")
    parts.append("## Cross-organisation digest")
    parts.append("")
    print("  [digest]", flush=True)
    digest_record = digest(config["digest_scope"], index, llm, k=args.k * 3)
    records.append(("digest", digest_record))
    parts.append(_render(digest_record, urls, "digest"))

    for kind, record in records:
        cost = estimate_cost(record.model, record.usage.input_tokens,
                             record.usage.output_tokens)
        log_run(
            run_log,
            run_id=record.run_id,
            model=record.model,
            usage=Usage(record.usage.input_tokens, record.usage.output_tokens, cost),
            kind=kind,
        )

    total_in = sum(r.usage.input_tokens for _, r in records)
    total_out = sum(r.usage.output_tokens for _, r in records)
    parts.append("---")
    parts.append("")
    parts.append("## Run totals")
    parts.append("")
    parts.append(f"- calls: {len(records)}")
    parts.append(f"- input tokens: {total_in}")
    parts.append(f"- output tokens: {total_out}")
    parts.append(f"- refusals: {sum(1 for _, r in records if r.insufficient_evidence)}")
    parts.append(
        f"- answers with no resolvable citation: "
        f"{sum(1 for _, r in records if not r.cited_source_ids)}"
    )
    parts.append("")

    out_path.write_text("\n".join(parts), encoding="utf-8")
    print(f"\nreview sheet: {out_path}")
    print(f"run log:      {run_log}")
    print(json.dumps({"calls": len(records), "input_tokens": total_in,
                      "output_tokens": total_out}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
