"""Run enrich_return_pct across 4 parallel symbol shards."""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SIM = REPO / "simulations"
PY = sys.executable


def _symbols() -> list[str]:
    import pandas as pd
    p = SIM / "results/historical_backtest/catalog_historical_2026-07-03_merged.csv"
    return sorted(pd.read_csv(p)["symbol"].unique())


def _chunks(items: list[str], n: int) -> list[list[str]]:
    size = (len(items) + n - 1) // n
    return [items[i:i + size] for i in range(0, len(items), size)]


def main() -> int:
    workers = 4
    syms = _symbols()
    chunks = _chunks(syms, workers)
    print(f"Launching {workers} enrich workers ({len(syms)} symbols total)")
    procs = []
    for i, chunk in enumerate(chunks):
        cmd = [PY, "-u", str(SIM / "enrich_return_pct.py"),
               "--symbols", ",".join(chunk), "--shard", f"shard{i}"]
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
    return subprocess.call([PY, "-u", str(SIM / "enrich_return_pct.py"), "--merge-only"])


if __name__ == "__main__":
    raise SystemExit(main())
