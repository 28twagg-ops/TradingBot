#!/usr/bin/env python3
"""One-off sanity check: Option A at -0.8% threshold + stop fill distribution."""
from __future__ import annotations

import csv
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pdt_schedule_engine import (
    EMPIRICAL_OVERRIDE_THRESHOLD_PCT,
    STARTING_EQUITY,
    Trade,
    _load_empirical_stop_samples_pct,
    run_simulation,
    D3_SCHEDULE_MODES,
    TICKER_LIMIT,
    MIN_HISTORY_DAYS,
    _build_signal_cache,
    _download_data,
    _fetch_sp500_tickers,
    _period_indices,
)
from pdt_removal_suite import (
    _count_overrides,
    _stop_override_stats,
)


def _trade_notional(t: Trade) -> float:
    if abs(t.pnl_pct) > 1e-9:
        return abs(t.pnl_dollar / (t.pnl_pct / 100.0))
    return abs(t.pnl_dollar)

LIVE_MEAN = -1.68
TRIGGER = -0.5


def _stop_distribution(stops: list[Trade]) -> dict[str, float]:
    bands = {
        "better_than_-0.5%": 0,
        "-0.5%_to_-0.8%": 0,
        "-0.8%_to_-1.2%": 0,
        "-1.2%_to_-1.68%": 0,
        "worse_than_-1.68%": 0,
    }
    for t in stops:
        p = t.pnl_pct
        if p > TRIGGER:
            bands["better_than_-0.5%"] += 1
        elif p > -0.8:
            bands["-0.5%_to_-0.8%"] += 1
        elif p > -1.2:
            bands["-0.8%_to_-1.2%"] += 1
        elif p > LIVE_MEAN:
            bands["-1.2%_to_-1.68%"] += 1
        else:
            bands["worse_than_-1.68%"] += 1
    n = len(stops) or 1
    return {k: round(v / n * 100, 1) for k, v in bands.items()}


def _blind_equity_walk(gap_trades: list[Trade]) -> float:
    entries: dict[str, list[Trade]] = defaultdict(list)
    exits: dict[str, list[Trade]] = defaultdict(list)
    for t in gap_trades:
        entries[t.entry_date].append(t)
        exits[t.exit_date].append(t)
    cash = STARTING_EQUITY
    for day in sorted(set(entries) | set(exits)):
        for t in exits.get(day, []):
            n = _trade_notional(t)
            cash += n * (1 + t.pnl_pct / 100)
        for t in entries.get(day, []):
            cash -= _trade_notional(t)
    return round((cash / STARTING_EQUITY - 1) * 100, 2)


def run_mode(mode_name: str):
    mode = next(m for m in D3_SCHEDULE_MODES if m.name == mode_name)
    end = "2026-06-18"
    start = "2023-01-01"
    tickers = _fetch_sp500_tickers()[:TICKER_LIMIT]
    stock_data, spy_df = _download_data(tickers, start, end)
    dates = list(spy_df.index)
    i0 = max(MIN_HISTORY_DAYS, _period_indices(dates, start, end)[0])
    i1 = _period_indices(dates, start, end)[1]
    cache = _build_signal_cache(stock_data, spy_df, dates)

    r_gap = run_simulation(mode, stock_data, spy_df, dates, cache, i0, i1)
    r_emp = run_simulation(mode, stock_data, spy_df, dates, cache, i0, i1, empirical_stops=True)
    gap_trades = list(r_gap.trades_list)
    emp_trades = list(r_emp.trades_list)
    stats = _stop_override_stats(gap_trades)
    overrides = _count_overrides(gap_trades, emp_trades)
    walk_ret = _blind_equity_walk(gap_trades)
    stops = [t for t in gap_trades if "stop" in t.exit_reason.lower()]

    return {
        "mode": mode_name,
        "threshold": EMPIRICAL_OVERRIDE_THRESHOLD_PCT,
        "eligible_pct": stats["eligible_pct"],
        "eligible_count": stats["eligible_count"],
        "stop_count": stats["stop_count"],
        "gap_return": round(r_gap.total_return_pct, 2),
        "emp_return": round(r_emp.total_return_pct, 2),
        "overrides": overrides,
        "override_pct": round(overrides / stats["stop_count"] * 100, 1) if stats["stop_count"] else 0,
        "gap_walk": walk_ret,
        "walk_match": abs(walk_ret - r_gap.total_return_pct) < 0.5,
        "distribution": _stop_distribution(stops),
        "stop_mean": round(float(np.mean([t.pnl_pct for t in stops])), 2) if stops else 0,
    }


if __name__ == "__main__":
    for m in ["dual_window", "evening_only"]:
        r = run_mode(m)
        print(f"\n=== {r['mode']} ===")
        print(f"Threshold: {r['threshold']}%  Eligible: {r['eligible_count']}/{r['stop_count']} ({r['eligible_pct']}%)")
        print(f"Gap: {r['gap_return']:+.1f}%  Empirical: {r['emp_return']:+.1f}%  Overrides: {r['overrides']} ({r['override_pct']}%)")
        print(f"Gap engine vs blind walk: {r['gap_return']:+.2f}% vs {r['gap_walk']:+.2f}%  match={r['walk_match']}")
        print(f"Stop mean (gap): {r['stop_mean']}%")
        print("Stop fill distribution (% of all gap stops):")
        for band, pct in r["distribution"].items():
            print(f"  {band}: {pct}%")
