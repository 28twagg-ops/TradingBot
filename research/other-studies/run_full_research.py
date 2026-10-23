"""
run_full_research.py — Long-running research: extensive synthetic + full universe historical.

Runs in sequence:
  1. Extensive synthetic catalog (220 strategies x full grid)
  2. Fetch full ~900 universe with max yfinance history
  3. Historical backtest on all downloaded symbols

Usage:
  python scripts/run_full_research.py
  python scripts/run_full_research.py --fetch-only
  python scripts/run_full_research.py --historical-only
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PY = sys.executable


def run(cmd: list[str], desc: str) -> int:
    print(f"\n{'='*60}\n{desc}\n{'='*60}")
    print(">", " ".join(cmd))
    return subprocess.call(cmd, cwd=str(REPO))


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch-only", action="store_true")
    ap.add_argument("--historical-only", action="store_true")
    ap.add_argument("--synthetic-only", action="store_true")
    ap.add_argument("--n", type=int, default=500, help="signals per synthetic variant")
    args = ap.parse_args()

    rc = 0

    if not args.fetch_only and not args.historical_only:
        rc = run(
            [PY, str(REPO / "simulations" / "options_catalog_runner.py"),
             "--extensive", "--n", str(args.n)],
            f"EXTENSIVE synthetic: 220 strategies x full grid x {args.n} signals",
        )
        if rc and args.synthetic_only:
            return rc

    if not args.synthetic_only and not args.historical_only:
        rc = run(
            [PY, str(REPO / "scripts" / "historical_data_fetcher.py"),
             "--universe-full", "--max-history"],
            "Fetch full universe (~900 stocks) max daily history",
        )
        if rc and args.fetch_only:
            return rc

    if not args.synthetic_only and not args.fetch_only:
        rc = run(
            [PY, str(REPO / "simulations" / "options_catalog_runner.py"),
             "--historical", "--all-symbols"],
            "Historical backtest all downloaded symbols x all strategies",
        )

    print("\nFull research pipeline finished.")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
