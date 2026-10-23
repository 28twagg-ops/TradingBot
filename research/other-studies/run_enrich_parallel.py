"""Run enrich_return_pct across 4 parallel symbol shards."""
from __future__ import annotations

try:
    from repo_root import find_repo_root
except ImportError:
    import sys as _sys
    from pathlib import Path as _Path
    _sys.path.insert(0, str(_Path(__file__).resolve().parents[2] / "live-bots" / "shared"))
    from repo_root import find_repo_root


import os
import subprocess
import sys
from pathlib import Path

REPO = find_repo_root(Path(__file__))
SIM = REPO / "research/options-strategies/backtests"
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
