#!/usr/bin/env python3
"""Build records/MANIFEST.csv with SHA-256 for migrated/copied record trees."""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "records" / "MANIFEST.csv"

# Only trees we intentionally place/copy under records/ (+ key indexes)
SCAN_DIRS = [
    ROOT / "records" / "research",
    ROOT / "records" / "archive",
    ROOT / "records" / "current",
]
# Also checksum originals that remain active but are inventoried for preservation
ALSO = [
    ROOT / "logs" / "research",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for base in SCAN_DIRS + ALSO:
        if not base.exists():
            continue
        files = [base] if base.is_file() else sorted(base.rglob("*"))
        for p in files:
            if not p.is_file():
                continue
            if p.name == "MANIFEST.csv":
                continue
            rel = p.relative_to(ROOT).as_posix()
            if rel in seen:
                continue
            seen.add(rel)
            rows.append(
                {
                    "path": rel,
                    "sha256": sha256(p),
                    "bytes": str(p.stat().st_size),
                    "role": "records" if rel.startswith("records/") else "active_research_logs",
                }
            )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["path", "sha256", "bytes", "role"])
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {OUT.relative_to(ROOT)} ({len(rows)} files)")


if __name__ == "__main__":
    main()
