"""Launch 4 parallel workers for paper top-5 return-% ranking."""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SIM = REPO / "simulations"
PY = sys.executable


def _symbols() -> list[str]:
    sys.path.insert(0, str(SIM))
    from historical_backtest import list_downloaded_symbols
    return list_downloaded_symbols()


def _chunks(items: list[str], n: int) -> list[list[str]]:
    size = (len(items) + n - 1) // n
    return [items[i:i + size] for i in range(0, len(items), size)]


def main() -> int:
    workers = 4
    syms = _symbols()
    chunks = _chunks(syms, workers)
    print(f"Launching {workers} rank workers for {len(syms)} symbols")
    procs = []
    for i, chunk in enumerate(chunks):
        cmd = [
            PY, "-u", str(SIM / "rank_paper_top5_pct.py"),
            "--symbols", ",".join(chunk),
            "--shard", f"shard{i}",
        ]
        print(f"  shard{i}: {len(chunk)} symbols")
        procs.append(subprocess.Popen(
            cmd, cwd=str(REPO),
            env={**os.environ, "PYTHONUNBUFFERED": "1"},
        ))
    rc = 0
    for p in procs:
        rc = max(rc, p.wait())
    if rc:
        return rc
    return subprocess.call([PY, str(SIM / "rank_paper_top5_pct.py"), "--merge-only"], cwd=str(REPO))


if __name__ == "__main__":
    raise SystemExit(main())
