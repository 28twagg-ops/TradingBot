"""
run_options_research.py — Local orchestrator for the full options research pipeline.

Steps:
  1. Write strategy registry (220 strategies)
  2. Fetch historical stock data (yfinance)
  3. Run Gate 1A API probe (optional, needs Alpaca creds)
  4. Run synthetic catalog grid (extensive)
  5. Run historical backtest on downloaded data

Usage:
  python scripts/run_options_research.py --all
  python scripts/run_options_research.py --fetch --symbols AAPL,MSFT,NVDA
  python scripts/run_options_research.py --synthetic-quick
  python scripts/run_options_research.py --synthetic-extensive
  python scripts/run_options_research.py --historical
  python scripts/run_options_research.py --probe
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SIM = REPO / "simulations"
SCRIPTS = REPO / "scripts"


def _run(cmd: list[str], desc: str) -> int:
    print(f"\n{'='*60}\n{desc}\n{'='*60}")
    print(">", " ".join(cmd))
    return subprocess.call(cmd, cwd=str(REPO))


def main() -> int:
    ap = argparse.ArgumentParser(description="Options research pipeline orchestrator")
    ap.add_argument("--all", action="store_true", help="full pipeline (fetch + synthetic + historical)")
    ap.add_argument("--write-registry", action="store_true")
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--symbols", default="AAPL,MSFT,NVDA,AMZN,GOOGL,META,TSLA,JPM,SPY,QQQ,AMD,CRM")
    ap.add_argument("--years", type=int, default=2)
    ap.add_argument("--universe-top", type=int, default=0)
    ap.add_argument("--probe", action="store_true", help="Gate 1A api probe")
    ap.add_argument("--synthetic-quick", action="store_true")
    ap.add_argument("--synthetic-extensive", action="store_true")
    ap.add_argument("--synthetic-focused", action="store_true")
    ap.add_argument("--historical", action="store_true")
    ap.add_argument("--integrity", action="store_true", help="Gate 2A integrity checks")
    args = ap.parse_args()

    py = sys.executable
    rc = 0

    if args.all or args.write_registry:
        rc = _run([py, str(SIM / "options_strategy_registry.py"), "--write"], "Write registry")
        if rc and not args.all:
            return rc

    if args.all or args.integrity:
        rc = _run([py, str(SIM / "options_strategy_simulator.py"), "--integrity"],
                  "Gate 2A integrity checks")
        if rc and not args.all:
            return rc

    if args.all or args.probe:
        rc = _run([py, str(SCRIPTS / "historical_data_fetcher.py"), "--probe-alpaca"],
                  "Gate 1A API probe")
        # non-fatal if no creds

    if args.all or args.fetch:
        cmd = [py, str(SCRIPTS / "historical_data_fetcher.py"), "--years", str(args.years)]
        if args.universe_top:
            cmd += ["--universe-top", str(args.universe_top)]
        else:
            cmd += ["--symbols", args.symbols]
        rc = _run(cmd, "Fetch historical stock data")
        if rc and not args.all:
            return rc

    if args.all or args.synthetic_quick:
        rc = _run([py, str(SIM / "options_catalog_runner.py"), "--write-registry", "--quick", "--n", "100"],
                  "Synthetic catalog (quick smoke)")
        if rc and not args.all:
            return rc

    if args.all or args.synthetic_focused:
        rc = _run([py, str(SIM / "options_catalog_runner.py"), "--focused", "--n", "300"],
                  "Synthetic catalog (focused / Verdict-B preset)")
        if rc and not args.all:
            return rc

    if args.all or args.synthetic_extensive:
        rc = _run(
            [py, str(SIM / "options_catalog_runner.py"), "--extensive", "--n", "500"],
            "Synthetic catalog (EXTENSIVE — all 220 strategies x full grid)",
        )
        if rc and not args.all:
            return rc

    if args.all or args.historical:
        rc = _run(
            [py, str(SIM / "options_catalog_runner.py"), "--historical",
             "--symbols", args.symbols],
            "Historical backtest catalog",
        )
        if rc and not args.all:
            return rc

    if not any([args.all, args.write_registry, args.fetch, args.probe,
                args.synthetic_quick, args.synthetic_extensive, args.synthetic_focused,
                args.historical, args.integrity]):
        ap.print_help()
        print("\nTip: start with  python scripts/run_options_research.py --all")
        return 0

    print("\nPipeline complete. Results in simulations/results/catalog/ and data/historical/")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
