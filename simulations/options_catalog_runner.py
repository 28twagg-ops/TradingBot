"""
options_catalog_runner.py
================================================================================
Extensive strategy catalog testing — runs the full ~220 strategy registry through
the validated sim engine across parameter variants.

Modes:
  synthetic  — Black-Scholes dev data (fast, engine validation)
  historical — real stock paths from data/historical/stocks/

Run:
  python simulations/options_catalog_runner.py --quick
  python simulations/options_catalog_runner.py --extensive --n 500
  python simulations/options_catalog_runner.py --historical --symbols AAPL,MSFT,NVDA
  python simulations/options_catalog_runner.py --category equity_signal
"""

from __future__ import annotations

import argparse
import csv
import itertools
import math
import random
import sys
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_strategy_simulator import (
    SignalEvent, simulate_single_trade, aggregate, DEV_LABEL,
)

TRADING_MINUTES = 390
MINUTE_DT = 1.0 / (252 * TRADING_MINUTES)
from options_strategy_grid import (
    DTE_DAYS, ENTRY_WINDOWS, EXIT_HOLD_MIN, FILL_MODES,
    VT_MIN_EXP_PNL, VT_MIN_FILL_RATE, VT_MIN_SAMPLE, VT_MAX_SPREAD,
    VT_MAX_COST, VT_MIN_PROFIT_FACTOR,
)
from options_strategy_registry import (
    STRIKE_OFFSETS, StrategyDef, build_registry, load_registry, save_registry,
)

RESULTS_DIR = Path(__file__).resolve().parent / "results" / "catalog"


@dataclass
class CatalogResult:
    strategy_id: str
    strategy_name: str
    category: str
    signal: str
    structure: str
    side: str
    multi_leg: bool
    strike: str
    dte: int
    entry_window: str
    exit_type: str
    fill_mode: str
    signals: int
    filled: int
    fill_rate: float
    win_rate: float
    profit_factor: float
    exp_pnl_per_signal: float
    total_pnl: float
    survives: bool
    fail_reasons: str
    data_mode: str

    @property
    def variant_id(self) -> str:
        return (f"{self.strategy_id}|{self.strike}|{self.dte}DTE|"
                f"{self.entry_window}|{self.exit_type}|{self.fill_mode}")


def gen_strategy_signals(strat: StrategyDef, strike_key: str, dte: int,
                         win_key: str, exit_key: str, n: int,
                         seed: int) -> list[SignalEvent]:
    """Synthetic signals tuned to one registry strategy."""
    rng = random.Random(seed)
    off = STRIKE_OFFSETS.get(strike_key, STRIKE_OFFSETS.get(strat.strike_offset, 0.0))
    right = strat.right
    drift = strat.drift * ENTRY_WINDOWS[win_key]
    if right == "P" and strat.side == "long":
        drift = -abs(drift)
    elif right == "C" and strat.side == "long":
        drift = abs(drift)
    elif strat.side == "short":
        drift = abs(drift) * 0.75

    hold_min = EXIT_HOLD_MIN[exit_key]
    T = dte / 365.0
    sigs: list[SignalEvent] = []

    for i in range(n):
        S0 = rng.choice([10, 14, 18, 22, 28, 35, 45, 60, 90, 120, 180]) * rng.uniform(0.9, 1.1)
        iv = rng.choice([0.20, 0.24, 0.28, 0.35, 0.45, 0.55]) * rng.uniform(0.95, 1.05)
        oi = rng.choice([40, 120, 300, 800, 2000])
        if right == "C":
            K = round(S0 * (1 + off), 2)
        else:
            K = round(S0 * (1 - off), 2)

        S_signal = S0
        z1 = rng.gauss(0.0, 1.0)
        S_next = S_signal * math.exp(-0.5 * iv * iv * MINUTE_DT
                                     + iv * math.sqrt(MINUTE_DT) * z1)
        T_hold = hold_min * MINUTE_DT
        z2 = rng.gauss(0.0, 1.0)
        S_exit = S_signal * math.exp((drift - 0.5 * iv * iv) * T_hold
                                     + iv * math.sqrt(T_hold) * z2)
        T_exit = max(0.0, T - T_hold)

        sigs.append(SignalEvent(
            sig_id=i, sdate=str(date.today()), symbol=f"SYN{i % 100:03d}",
            mechanic=strat.mechanic_key, right=right, strike=K, T_years=T,
            iv=iv, open_interest=oi, period=("A" if i % 2 == 0 else "B"),
            S_signal=S_signal, S_next=S_next, S_exit=S_exit,
            T_exit_years=T_exit, side=strat.side,
        ))
    return sigs


def evaluate_catalog_variant(strat: StrategyDef, strike_key: str, dte: int,
                             win_key: str, exit_key: str, fill_mode: str,
                             n: int, seed: int,
                             data_mode: str = "synthetic") -> CatalogResult:
    sigs = gen_strategy_signals(strat, strike_key, dte, win_key, exit_key, n, seed)
    trades = [simulate_single_trade(s, fill_mode=fill_mode) for s in sigs]
    agg = aggregate(trades)

    filled = [t for t in trades if t.filled]
    pf = agg["profit_factor"]
    pf_val = pf if pf != float("inf") else 999.0
    n_fill = agg["filled"]

    fails = []
    if agg["exp_pnl_per_signal"] <= VT_MIN_EXP_PNL:
        fails.append("exp_pnl<=0")
    if agg["fill_rate"] < VT_MIN_FILL_RATE:
        fails.append("fill<40%")
    if n_fill < VT_MIN_SAMPLE:
        fails.append("sample<50")

    def _exp(period):
        sub = [t for s, t in zip(sigs, trades) if s.period == period]
        return aggregate(sub)["exp_pnl_per_signal"] if sub else float("-inf")
    exp_A, exp_B = _exp("A"), _exp("B")
    if not (exp_A > 0 and exp_B > 0):
        fails.append("not_both_periods")
    if pf_val < VT_MIN_PROFIT_FACTOR:
        fails.append("pf<1.2")

    return CatalogResult(
        strategy_id=strat.id, strategy_name=strat.name, category=strat.category,
        signal=strat.signal, structure=strat.structure, side=strat.side,
        multi_leg=strat.multi_leg, strike=strike_key, dte=dte,
        entry_window=win_key, exit_type=exit_key, fill_mode=fill_mode,
        signals=len(sigs), filled=n_fill, fill_rate=agg["fill_rate"],
        win_rate=agg["win_rate"], profit_factor=pf_val,
        exp_pnl_per_signal=agg["exp_pnl_per_signal"], total_pnl=agg["total_pnl"],
        survives=not fails, fail_reasons=",".join(fails) if fails else "",
        data_mode=data_mode,
    )


def _grid_axes(extensive: bool, quick: bool, focused: bool) -> tuple:
    if quick:
        return (["ATM"], [7], ["0930-1000"], ["EOD"], ["cancel"])
    if focused:
        return (["ATM"], [1, 3, 7], list(ENTRY_WINDOWS), ["intraday", "EOD"], FILL_MODES)
    if extensive:
        return (list(STRIKE_OFFSETS.keys()), DTE_DAYS, list(ENTRY_WINDOWS),
                list(EXIT_HOLD_MIN.keys()), FILL_MODES)
    return (["ATM", "OTM1"], [1, 3, 7, 14], list(ENTRY_WINDOWS),
            ["intraday", "EOD", "1day"], FILL_MODES)


def run_catalog(strategies: list[StrategyDef], n: int, extensive: bool = False,
                quick: bool = False, focused: bool = False,
                skip_multi_leg: bool = False) -> list[CatalogResult]:
    strikes, dtes, wins, exits, fills = _grid_axes(extensive, quick, focused)
    combos = list(itertools.product(strikes, dtes, wins, exits, fills))
    results: list[CatalogResult] = []
    total = len(strategies) * len(combos)
    print(f"[{DEV_LABEL}] Catalog run: {len(strategies)} strategies x "
          f"{len(combos)} variants = {total:,} evaluations ({n} signals each)")
    t0 = time.monotonic()
    idx = 0

    for si, strat in enumerate(strategies):
        if skip_multi_leg and strat.multi_leg:
            continue
        for ci, (sk, dte, win, ex, fill) in enumerate(combos):
            seed = 10000 + si * 1000 + ci
            results.append(evaluate_catalog_variant(
                strat, sk, dte, win, ex, fill, n, seed))
            idx += 1
            if idx % 500 == 0:
                el = time.monotonic() - t0
                print(f"  {idx}/{total} ({el:.0f}s)")

    print(f"  done {len(results)} in {time.monotonic()-t0:.1f}s")
    return results


def save_catalog_results(results: list[CatalogResult], tag: str) -> Path:
    out_dir = RESULTS_DIR / tag
    out_dir.mkdir(parents=True, exist_ok=True)
    ranked = sorted(results, key=lambda r: r.exp_pnl_per_signal, reverse=True)

    fields = [f.name for f in CatalogResult.__dataclass_fields__.values()] + ["variant_id"]
    csv_path = out_dir / "catalog_leaderboard.csv"
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in ranked:
            row = {k: getattr(r, k) for k in CatalogResult.__dataclass_fields__}
            row["variant_id"] = r.variant_id
            w.writerow(row)

    # Per-strategy best variant
    best_by_strat: dict[str, CatalogResult] = {}
    for r in ranked:
        if r.strategy_id not in best_by_strat:
            best_by_strat[r.strategy_id] = r

    summary_path = out_dir / "catalog_strategy_summary.csv"
    with open(summary_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=[
            "strategy_id", "strategy_name", "category", "best_variant",
            "exp_pnl_per_signal", "filled", "win_rate", "survives",
        ])
        w.writeheader()
        for sid in sorted(best_by_strat):
            r = best_by_strat[sid]
            w.writerow({
                "strategy_id": r.strategy_id,
                "strategy_name": r.strategy_name,
                "category": r.category,
                "best_variant": r.variant_id,
                "exp_pnl_per_signal": r.exp_pnl_per_signal,
                "filled": r.filled,
                "win_rate": r.win_rate,
                "survives": r.survives,
            })

    survivors = [r for r in ranked if r.survives and r.filled >= 50]
    report = out_dir / "catalog_report.md"
    lines = [
        f"# Options Catalog Run — {tag}",
        f"_{DEV_LABEL}_",
        "",
        f"Generated: {date.today().isoformat()}",
        f"Total variant evaluations: {len(results)}",
        f"Survivors (7 thresholds, >=50 fills): {len(survivors)}",
        "",
        "## Top 25 variants (all strategies)",
        "",
        "| Rank | Strategy | Variant | ExpP&L/sig | Fill | Win | Survives |",
        "|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(ranked[:25], 1):
        lines.append(
            f"| {i} | {r.strategy_id} {r.strategy_name[:30]} | "
            f"{r.strike}/{r.dte}DTE/{r.exit_type} | "
            f"${r.exp_pnl_per_signal:+.2f} | {r.fill_rate:.0%} | "
            f"{r.win_rate:.0%} | {'YES' if r.survives else 'no'} |"
        )
    lines += [
        "",
        "## Best variant per strategy (top 15 by Exp P&L/signal)",
        "",
    ]
    strat_best = sorted(best_by_strat.values(),
                        key=lambda x: x.exp_pnl_per_signal, reverse=True)[:15]
    for r in strat_best:
        lines.append(
            f"- **{r.strategy_id}** {r.strategy_name}: "
            f"${r.exp_pnl_per_signal:+.2f}/sig ({r.variant_id})"
        )
    report.write_text("\n".join(lines), encoding="utf-8")
    print(f"Saved: {csv_path}, {summary_path}, {report}")
    return out_dir


def run_historical_catalog(symbols: list[str], strategies: list[StrategyDef],
                           all_symbols: bool = False) -> None:
    from historical_backtest import run_catalog_historical, list_downloaded_symbols
    if all_symbols:
        symbols = list_downloaded_symbols()
        print(f"Historical: {len(symbols)} downloaded symbols")
    df = run_catalog_historical(symbols, strategies)
    print(f"Historical catalog: {len(df)} result rows")


def main() -> int:
    ap = argparse.ArgumentParser(description="Extensive options strategy catalog runner")
    ap.add_argument("--write-registry", action="store_true")
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--extensive", action="store_true")
    ap.add_argument("--focused", action="store_true")
    ap.add_argument("--n", type=int, default=200, help="signals per variant")
    ap.add_argument("--category", default=None, help="filter category e.g. equity_signal")
    ap.add_argument("--strategy", default=None, help="single strategy id e.g. S163")
    ap.add_argument("--historical", action="store_true")
    ap.add_argument("--symbols", default="AAPL,MSFT,NVDA,SPY,JPM,AMD,CRM")
    ap.add_argument("--all-symbols", action="store_true",
                    help="historical: all parquets in data/historical/stocks/")
    ap.add_argument("--skip-multi-leg", action="store_true", default=False,
                    help="exclude multi-leg structures (single-leg proxy only)")
    args = ap.parse_args()

    if args.write_registry:
        p = save_registry(build_registry())
        print(f"Registry written: {p} ({len(load_registry())} strategies)")
        return 0

    registry = load_registry()
    if not (Path(__file__).parent / "options_strategy_registry.json").exists():
        save_registry(registry)

    strategies = registry
    if args.category:
        strategies = [s for s in registry if s.category == args.category]
    if args.strategy:
        strategies = [s for s in registry if s.id == args.strategy]

    tag = date.today().isoformat()
    if args.quick:
        tag += "_quick"
    elif args.extensive:
        tag += "_extensive"
    elif args.focused:
        tag += "_focused"
    else:
        tag += "_standard"

    if args.historical:
        syms = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
        run_historical_catalog(syms, strategies, all_symbols=args.all_symbols)
        return 0

    results = run_catalog(
        strategies, args.n,
        extensive=args.extensive, quick=args.quick, focused=args.focused,
        skip_multi_leg=args.skip_multi_leg,
    )
    save_catalog_results(results, tag)
    survivors = sum(1 for r in results if r.survives and r.filled >= 50)
    print(f"Catalog complete: {len(results)} variants, {survivors} survivors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
