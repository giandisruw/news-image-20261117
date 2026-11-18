#!/usr/bin/env python3
"""Deliver the finished newspaper front page to the harness output slot.

The artwork itself is baked into the bundle as ``entry.png`` sitting right
next to this file. Nothing here is generated, fetched, or tweaked at run
time: the job is simply to place that exact image where the evaluator
expects it, and to do so the same way on every single run.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path


ARTWORK_NAME = "entry.png"
FALLBACK_SLOT = Path("/output/entry.png")


def _here() -> Path:
    """Folder holding this script (and therefore the bundled artwork)."""
    return Path(__file__).resolve().parent


def _destination() -> Path:
    """Where the finished image must land.

    ``MAKEFUN_OUTPUT_DIR`` points at the harness output folder when the
    entry runs under evaluation; without it we fall back to ``/output``.
    """
    slot = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if slot:
        return Path(slot) / ARTWORK_NAME
    return FALLBACK_SLOT


def _fingerprint(path: Path) -> str:
    """SHA-256 digest of a file, read in modest chunks."""
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def _validate_png(path: Path) -> bool:
    """Reject anything that is not a real PNG before it is copied.

    Reads the first 8 bytes and compares them against the PNG magic
    signature (89 50 4E 47 0D 0A 1A 0A); anything else is not our artwork.
    """
    with path.open("rb") as stream:
        magic = stream.read(len(PNG_SIGNATURE))
    return magic == PNG_SIGNATURE


def place_front_page() -> int:
    """Copy the bundled front page into the output slot, byte for byte."""
    source = _here() / ARTWORK_NAME
    target = _destination()

    if not source.is_file():
        print(f"missing bundled artwork: {source}", file=sys.stderr)
        return 1

    if not _validate_png(source):
        print(
            f"bundled artwork is not a valid PNG: {source} "
            "(bad magic bytes, expected 89 50 4E 47 0D 0A 1A 0A)",
            file=sys.stderr,
        )
        return 1

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)

    before = _fingerprint(source)
    after = _fingerprint(target)
    if before != after:
        print("output does not match the bundled artwork", file=sys.stderr)
        return 1

    print(f"wrote {target} (sha256 {after})")
    return 0


if __name__ == "__main__":
    raise SystemExit(place_front_page())
