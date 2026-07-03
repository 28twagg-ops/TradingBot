"""
run_historical_parallel.py — Split historical backtest across N parallel workers.

Usage:
  python scripts/run_historical_parallel.py --workers 4
  python scripts/run_historical_parallel.py --workers 4 --merge-only
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SIM = REPO / "simulations"
PY = sys.executable


def _pending_symbols() -> list[str]:
    sys.path.insert(0, str(SIM))
    from historical_backtest import list_downloaded_symbols
    import pandas as pd
    from datetime import date

    all_syms = list_downloaded_symbols()
    done: set[str] = set()
    cp = REPO / "simulations/results/historical_backtest" / (
        f"catalog_historical_{date.today().isoformat()}_checkpoint.csv"
    )
    if cp.exists():
        df = pd.read_csv(cp)
        if "symbol" in df.columns:
            done = set(df["symbol"].unique())
    return [s for s in all_syms if s not in done]


def _chunks(items: list[str], n: int) -> list[list[str]]:
    n = max(1, min(n, len(items)))
    size = (len(items) + n - 1) // n
    return [items[i:i + size] for i in range(0, len(items), size)]


def launch_workers(workers: int, dry_run: bool = False) -> list[subprocess.Popen]:
    pending = _pending_symbols()
    if not pending:
        print("No pending symbols — run --merge-only or check checkpoint.")
        return []

    chunks = _chunks(pending, workers)
    print(f"Launching {len(chunks)} workers for {len(pending)} pending symbols")

    procs: list[subprocess.Popen] = []
    log_dir = REPO / "data" / "historical" / "parallel"
    log_dir.mkdir(parents=True, exist_ok=True)

    for i, chunk in enumerate(chunks):
        sym_arg = ",".join(chunk)
        cmd = [
            PY, "-u", str(SIM / "historical_backtest.py"),
            "--symbols", sym_arg,
            "--output-tag", f"shard{i}",
            "--no-resume",
        ]
        log_path = log_dir / f"shard{i}.log"
        print(f"  worker {i}: {len(chunk)} symbols -> {log_path.name}")
        if dry_run:
            print("   ", " ".join(cmd[:6]), "...")
            continue
        log_f = open(log_path, "w", encoding="utf-8")
        procs.append(subprocess.Popen(
            cmd, cwd=str(REPO), stdout=log_f, stderr=subprocess.STDOUT,
            env={**os.environ, "PYTHONUNBUFFERED": "1"},
        ))
    return procs


def merge() -> int:
    sys.path.insert(0, str(SIM))
    from historical_backtest import merge_historical_shards
    merge_historical_shards()
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Parallel historical backtest")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--merge-only", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--wait", action="store_true", default=False,
                    help="wait for all workers then merge")
    args = ap.parse_args()

    if args.merge_only:
        return merge()

    procs = launch_workers(args.workers, dry_run=args.dry_run)
    if args.dry_run or not procs:
        return 0

    print(f"\n{len(procs)} workers running. Logs: data/historical/parallel/")
    if args.wait:
        codes = [p.wait() for p in procs]
        print(f"Workers finished: {codes}")
        if all(c == 0 for c in codes):
            return merge()
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
