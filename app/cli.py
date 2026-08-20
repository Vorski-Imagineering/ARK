"""One-step commands for every operation.

A new builder should never have to remember a sequence of internal module
calls. The required command set is ratified in the technical specification:
setup, ingest, query, digest, test, run.
"""

import argparse
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from app.chunk import chunk_document
from app.index import build_index, promote
from app.normalise import LINK_AND_SUMMARISE, normalise
from app.source_loader import load_raw
from app.source_pack import SourcePackError, load_source_pack

DEFAULT_SOURCE_PACK_DIR = "proposal/hackathon-1/execution/source-packs"
DEFAULT_INDEX_ROOT = "index"
DEFAULT_MAX_CHARS = 1200
DEFAULT_OVERLAP = 120
DEFAULT_K = 8


@dataclass(frozen=True)
class IngestResult:
    packs_loaded: int
    sources_loaded: int
    sources_skipped_for_permission: int
    chunks_indexed: int
    index_path: Path | None
    errors: list[str]


def _embedder(prefer_local: bool):
    """Local model in production; the deterministic fake when it is unavailable."""
    if prefer_local:
        try:
            from app.embed import LocalEmbedder

            return LocalEmbedder()
        except Exception:  # noqa: BLE001 - fall back rather than fail ingestion
            pass
    from app.embed import FakeEmbedder

    return FakeEmbedder(dim=16)


def ingest_command(
    source_pack_dir: str = DEFAULT_SOURCE_PACK_DIR,
    index_root: Path | str = DEFAULT_INDEX_ROOT,
    only: list[str] | None = None,
    max_chars: int = DEFAULT_MAX_CHARS,
    overlap: int = DEFAULT_OVERLAP,
    prefer_local_embedder: bool = False,
) -> IngestResult:
    """Rebuild the index from approved source packs."""
    pack_dir = Path(source_pack_dir)
    index_root = Path(index_root)
    retrieved_at = datetime.now(timezone.utc).isoformat()

    names = sorted(only) if only else sorted(p.name for p in pack_dir.glob("*.md"))

    packs_loaded = 0
    sources_loaded = 0
    skipped_for_permission = 0
    chunks = []
    errors: list[str] = []

    for name in names:
        try:
            pack = load_source_pack(pack_dir / name)
        except SourcePackError as exc:
            errors.append(f"{name}: {exc}")
            continue

        packs_loaded += 1

        for source in pack.sources:
            sources_loaded += 1

            if source.permission_mode == LINK_AND_SUMMARISE:
                # Permitted to link and summarise only, so no body text is
                # stored and the source contributes no retrievable chunks.
                skipped_for_permission += 1
                continue

            if not source.snapshot_path:
                errors.append(f"{source.source_id}: no snapshot_path")
                continue

            try:
                raw = load_raw(Path(source.snapshot_path), source.source_type)
            except Exception as exc:  # noqa: BLE001 - report and continue
                errors.append(f"{source.source_id}: {exc}")
                continue

            document = normalise(raw, source, retrieved_at)
            chunks.extend(chunk_document(document, max_chars, overlap))

    index_path = None
    if chunks:
        staging = build_index(chunks, _embedder(prefer_local_embedder), index_root)
        promote(staging, index_root)
        index_path = index_root / "active.sqlite3"

    return IngestResult(
        packs_loaded=packs_loaded,
        sources_loaded=sources_loaded,
        sources_skipped_for_permission=skipped_for_permission,
        chunks_indexed=len(chunks),
        index_path=index_path,
        errors=errors,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ark", description="ARK Agent commands")
    subparsers = parser.add_subparsers(dest="command", required=False)

    ingest = subparsers.add_parser("ingest", help="rebuild the index from source packs")
    ingest.add_argument("--source-pack-dir", default=DEFAULT_SOURCE_PACK_DIR)
    ingest.add_argument("--index-root", default=None)
    ingest.add_argument("--local-embedder", action="store_true")

    query = subparsers.add_parser("query", help="answer a question with sources")
    query.add_argument("question", help="the question to answer")
    query.add_argument("-k", type=int, default=DEFAULT_K)
    query.add_argument("--index-root", default=None)

    dig = subparsers.add_parser("digest", help="generate the cross-organisation digest")
    dig.add_argument("--scope", default="weekly cross-organisation digest")
    dig.add_argument("-k", type=int, default=DEFAULT_K * 2)
    dig.add_argument("--index-root", default=None)

    run = subparsers.add_parser("run", help="start the local interface")
    run.add_argument("--index-root", default=None)

    return parser


def _resolve_index_root(explicit: str | None) -> Path:
    return Path(explicit or os.environ.get("ARK_INDEX_PATH") or DEFAULT_INDEX_ROOT)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 0

    index_root = _resolve_index_root(getattr(args, "index_root", None))

    if args.command == "ingest":
        result = ingest_command(
            source_pack_dir=args.source_pack_dir,
            index_root=index_root,
            prefer_local_embedder=args.local_embedder,
        )
        print(
            f"packs={result.packs_loaded} sources={result.sources_loaded} "
            f"skipped_for_permission={result.sources_skipped_for_permission} "
            f"chunks={result.chunks_indexed}"
        )
        for error in result.errors:
            print(f"  error: {error}")
        return 1 if result.errors and not result.chunks_indexed else 0

    from app.index import Index
    from app.llm import HermesLLM

    index = Index.open(index_root / "active.sqlite3")

    if args.command == "query":
        from app.answer import answer

        record = answer(args.question, index, HermesLLM(), k=args.k)
        _print_record(record)
        return 0

    if args.command == "digest":
        from app.digest import digest

        record = digest(args.scope, index, HermesLLM(), k=args.k)
        _print_record(record)
        return 0

    if args.command == "run":
        print(f"index: {index_root / 'active.sqlite3'}  chunks: {index.count()}")
        print("interactive mode. blank line to exit.")
        from app.answer import answer

        while True:
            try:
                question = input("\n> ").strip()
            except EOFError:
                break
            if not question:
                break
            _print_record(answer(question, index, HermesLLM(), k=DEFAULT_K))
        return 0

    parser.print_help()
    return 0


def _print_record(record) -> None:
    print(record.output)
    print("\nsources:")
    for source_id in record.cited_source_ids:
        print(f"  - {source_id}")
    if not record.cited_source_ids:
        print("  (none)")
    if record.limitations:
        print("\nlimitations:")
        for limitation in record.limitations:
            print(f"  - {limitation}")
    print(
        f"\nusage: in={record.usage.input_tokens} out={record.usage.output_tokens} "
        f"est_usd={record.usage.estimated_cost_usd:.6f}"
    )


if __name__ == "__main__":
    raise SystemExit(main())
