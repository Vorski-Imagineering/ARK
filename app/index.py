"""Build, promote, and read the derived retrieval index.

The index is a disposable cache, never a system of record. It is always
rebuildable from the canonical corpus in git.

Three operational properties are ratified requirements rather than niceties:
a build writes to a staging file and only an explicit promotion makes it live;
a failed build leaves the running index untouched; and previous indexes remain
selectable so a bad ingestion can be rolled back without a rebuild.
"""

import hashlib
import json
import re
import sqlite3
import struct
from dataclasses import dataclass, field
from pathlib import Path

from app.chunk import Chunk
from app.embed import Embedder

ACTIVE_NAME = "active.sqlite3"
_ARCHIVE = re.compile(r"\Aindex-(\d{4})\.sqlite3\Z")
_STAGING = re.compile(r"\Astaging-(\d{4})\.sqlite3\Z")

# One live index plus three retained predecessors.
MAX_RETAINED = 4

_SCHEMA = """
CREATE TABLE IF NOT EXISTS chunks (
    chunk_id        TEXT PRIMARY KEY,
    source_id       TEXT NOT NULL,
    organisation_id TEXT NOT NULL,
    heading_path    TEXT NOT NULL,
    text            TEXT NOT NULL,
    start_offset    INTEGER,
    end_offset      INTEGER,
    embedding       BLOB NOT NULL,
    embedding_model TEXT NOT NULL
);
"""


class IndexBuildError(Exception):
    """An index could not be built."""


@dataclass(frozen=True)
class StoredChunk:
    chunk_id: str
    source_id: str
    organisation_id: str
    heading_path: list[str]
    text: str
    start_offset: int
    end_offset: int
    embedding: list[float] = field(default_factory=list)


def _pack(vector: list[float]) -> bytes:
    return struct.pack(f"<{len(vector)}d", *vector)


def _unpack(blob: bytes) -> list[float]:
    return list(struct.unpack(f"<{len(blob) // 8}d", blob))


def _next_number(root: Path, pattern: re.Pattern) -> int:
    highest = 0
    if root.exists():
        for entry in root.iterdir():
            match = pattern.match(entry.name)
            if match:
                highest = max(highest, int(match.group(1)))
    return highest + 1


def build_index(chunks: list[Chunk], embedder: Embedder, root: Path) -> Path:
    """Embed every chunk and write a new staging index. Never touches the active one."""
    if not chunks:
        raise IndexBuildError(
            "refusing to build an index from zero chunks; the active index is unchanged"
        )

    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)

    vectors = embedder.embed([chunk.text for chunk in chunks])
    if len(vectors) != len(chunks):
        raise IndexBuildError(
            f"embedder returned {len(vectors)} vectors for {len(chunks)} chunks"
        )

    # A monotonic counter rather than a timestamp: two builds inside the same
    # second must not collide.
    staging = root / f"staging-{_next_number(root, _STAGING):04d}.sqlite3"

    connection = sqlite3.connect(staging)
    try:
        connection.executescript(_SCHEMA)
        connection.executemany(
            "INSERT INTO chunks (chunk_id, source_id, organisation_id, heading_path,"
            " text, start_offset, end_offset, embedding, embedding_model)"
            " VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                (
                    chunk.chunk_id,
                    chunk.source_id,
                    chunk.organisation_id,
                    json.dumps(chunk.heading_path),
                    chunk.text,
                    chunk.start_offset,
                    chunk.end_offset,
                    _pack(vector),
                    getattr(embedder, "model_id", "unknown"),
                )
                for chunk, vector in zip(chunks, vectors)
            ],
        )
        connection.commit()
    except sqlite3.Error as exc:
        connection.close()
        staging.unlink(missing_ok=True)
        raise IndexBuildError(f"could not write staging index: {exc}") from exc
    finally:
        connection.close()

    return staging


def list_indexes(root: Path) -> list[Path]:
    """Every selectable index: the active one plus retained predecessors."""
    root = Path(root)
    if not root.exists():
        return []
    found = [entry for entry in root.iterdir() if _ARCHIVE.match(entry.name)]
    found.sort(key=lambda p: p.name)
    active = root / ACTIVE_NAME
    if active.exists():
        found.append(active)
    return found


def promote(staging_path: Path, root: Path) -> None:
    """Make a staging index live, retaining the previous one for rollback."""
    root = Path(root)
    staging_path = Path(staging_path)
    if not staging_path.exists():
        raise IndexBuildError(f"cannot promote missing staging index {staging_path}")

    active = root / ACTIVE_NAME
    if active.exists():
        archive = root / f"index-{_next_number(root, _ARCHIVE):04d}.sqlite3"
        active.rename(archive)

    staging_path.rename(active)

    # Retain at most MAX_RETAINED selectable indexes, oldest discarded first.
    archives = sorted(
        (entry for entry in root.iterdir() if _ARCHIVE.match(entry.name)),
        key=lambda p: p.name,
    )
    while len(archives) + 1 > MAX_RETAINED:
        archives.pop(0).unlink(missing_ok=True)


class Index:
    """Read-only view over a built index."""

    def __init__(self, connection: sqlite3.Connection, path: Path) -> None:
        self._connection = connection
        self.path = path

    @classmethod
    def open(cls, path: Path) -> "Index":
        path = Path(path)
        if not path.exists():
            raise IndexBuildError(f"no index at {path}")
        # Opened read-only: the query path must never mutate the live index.
        connection = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        return cls(connection, path)

    @classmethod
    def create_empty(cls, path: Path) -> "Index":
        """A valid index holding no chunks.

        Deliberately bypasses the non-empty guard in build_index so that the
        insufficient-evidence path has something to query.
        """
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(path)
        connection.executescript(_SCHEMA)
        connection.commit()
        connection.close()
        return cls.open(path)

    def count(self) -> int:
        return self._connection.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]

    def _row_to_chunk(self, row) -> StoredChunk:
        return StoredChunk(
            chunk_id=row[0],
            source_id=row[1],
            organisation_id=row[2],
            heading_path=json.loads(row[3]),
            text=row[4],
            start_offset=row[5],
            end_offset=row[6],
            embedding=_unpack(row[7]),
        )

    def get(self, chunk_id: str) -> StoredChunk:
        row = self._connection.execute(
            "SELECT chunk_id, source_id, organisation_id, heading_path, text,"
            " start_offset, end_offset, embedding FROM chunks WHERE chunk_id = ?",
            (chunk_id,),
        ).fetchone()
        if row is None:
            raise KeyError(chunk_id)
        return self._row_to_chunk(row)

    def all(self) -> list[StoredChunk]:
        rows = self._connection.execute(
            "SELECT chunk_id, source_id, organisation_id, heading_path, text,"
            " start_offset, end_offset, embedding FROM chunks ORDER BY chunk_id"
        ).fetchall()
        return [self._row_to_chunk(row) for row in rows]

    def embedding_signature(self) -> tuple[str, int] | None:
        """The model identifier and vector dimension stored in this index.

        A query has to be embedded the same way its corpus was, so the reader
        needs to know which model produced these vectors.
        """
        row = self._connection.execute(
            "SELECT embedding_model, LENGTH(embedding) FROM chunks LIMIT 1"
        ).fetchone()
        if row is None:
            return None
        return str(row[0]), int(row[1]) // 8

    def fingerprint(self) -> str:
        """Content identity of the index.

        Covers chunk identifiers and vectors only. Timestamps and file paths are
        excluded so that two builds of the same corpus compare equal.
        """
        digest = hashlib.sha256()
        for row in self._connection.execute(
            "SELECT chunk_id, embedding FROM chunks ORDER BY chunk_id"
        ):
            digest.update(row[0].encode("utf-8"))
            digest.update(row[1])
        return digest.hexdigest()
