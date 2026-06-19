# -*- coding: utf-8 -*-
"""
Phase 3 PDT removal simulation suite — wraps pdt_schedule_engine.py

D3 modes: evening_only, morning_only, any_time, overnight_pdt, dual_window

  python pdt_removal_suite.py --mode dual_window --years 3 --slippage gap
  python pdt_removal_suite.py --mode all --years 7 --slippage empirical
"""
from __future__ import annotations

import argparse
import csv
import time
from datetime import date
from pathlib import Path

from pdt_schedule_engine import (
    D3_SCHEDULE_MODES,
    EMPIRICAL_OVERRIDE_THRESHOLD_PCT,
    STARTING_EQUITY,
    TICKER_LIMIT,
    MIN_HISTORY_DAYS,
    Trade,
    _build_signal_cache,
    _download_data,
    _fetch_sp500_tickers,
    _period_indices,
    run_simulation,
)

_HERE = Path(__file__).resolve().parent
OUT_BASE = _HERE / "results" / "pdt_removal"
SCHEDULE_DIR = OUT_BASE / "schedule_modes"
MASTER_CSV = OUT_BASE / "master_results_table.csv"

MASTER_FIELDS = [
    "test_name", "horizon_yr", "slippage_model", "total_return_pct", "ann_return_pct",
    "sharpe", "win_rate", "profit_factor", "stop_exit_count", "stop_avg_return",
    "max_drawdown_pct", "run_date", "days_both_windows", "days_one_window",
    "morning_entry_trades", "evening_entry_trades", "notes",
]


def _profit_factor(trades: list[Trade]) -> float:
    gw = sum(t.pnl_dollar for t in trades if t.pnl_dollar > 0)
    gl = abs(sum(t.pnl_dollar for t in trades if t.pnl_dollar <= 0)) or 1e-9
    return round(gw / gl, 2)


def _write_trades(path: Path, trades: list[Trade]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([
            "ticker", "strategy", "entry_date", "exit_date", "entry_price", "exit_price",
            "pnl_pct", "pnl_dollar", "hold_days", "exit_reason", "entry_scan_window", "seasonal",
        ])
        for t in trades:
            w.writerow([
                t.ticker, t.strategy, t.entry_date, t.exit_date,
                round(t.entry_price, 4), round(t.exit_price, 4),
                round(t.pnl_pct, 3), round(t.pnl_dollar, 2),
                t.hold_days, t.exit_reason, t.entry_scan_window, t.seasonal,
            ])


def _append_master(row: dict):
    MASTER_CSV.parent.mkdir(parents=True, exist_ok=True)
    write_header = not MASTER_CSV.exists()
    with open(MASTER_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=MASTER_FIELDS, extrasaction="ignore")
        if write_header:
            w.writeheader()
        w.writerow(row)


def _stop_override_stats(gap_trades: list[Trade]) -> dict:
    stops = [t for t in gap_trades if "stop" in t.exit_reason.lower()]
    eligible = [t for t in stops if t.pnl_pct > EMPIRICAL_OVERRIDE_THRESHOLD_PCT]
    return {
        "stop_count": len(stops),
        "eligible_count": len(eligible),
        "eligible_pct": round(len(eligible) / len(stops) * 100, 1) if stops else 0.0,
    }


def _count_overrides(gap_trades: list[Trade], emp_trades: list[Trade]) -> int:
    gap_stops = {
        (t.ticker, t.entry_date, t.exit_date): t.pnl_pct
        for t in gap_trades if "stop" in t.exit_reason.lower()
    }
    n = 0
    for t in emp_trades:
        if "stop" not in t.exit_reason.lower():
            continue
        key = (t.ticker, t.entry_date, t.exit_date)
        if key in gap_stops and abs(t.pnl_pct - gap_stops[key]) > 1e-6:
            n += 1
    return n


def _sim_metrics(r, trades: list[Trade]) -> dict:
    return {
        "total_return_pct": round(r.total_return_pct, 2),
        "win_rate": round(r.win_rate_pct, 1),
        "profit_factor": _profit_factor(trades),
        "stop_exit_count": r.stop_trades,
        "stop_avg_return": round(r.stop_avg_pnl_pct, 2),
        "max_drawdown_pct": round(r.max_drawdown_pct, 2),
        "sharpe": round(r.sharpe, 2),
        "ann_return_pct": round(r.cagr_pct, 2),
    }


def run_mode(mode_name: str, years: int, slippage: str):
    mode = next(m for m in D3_SCHEDULE_MODES if m.name == mode_name)
    end = date.today().isoformat()
    start = f"{date.today().year - years}-01-01"
    tickers = _fetch_sp500_tickers()[:TICKER_LIMIT]
    print(f"Data: {len(tickers)} tickers, {start} -> {end}")
    stock_data, spy_df = _download_data(tickers, start, end)
    dates = list(spy_df.index)
    i0, i1 = max(MIN_HISTORY_DAYS, _period_indices(dates, start, end)[0]), _period_indices(dates, start, end)[1]
    cache = _build_signal_cache(stock_data, spy_df, dates)
    slips = ["gap", "empirical"] if slippage == "both" else [slippage]

    t0 = time.time()
    r_gap = run_simulation(mode, stock_data, spy_df, dates, cache, i0, i1)
    gap_trades = list(r_gap.trades_list)
    override_stats = _stop_override_stats(gap_trades)
    print(
        f"  Stop override threshold: {EMPIRICAL_OVERRIDE_THRESHOLD_PCT}%  "
        f"({override_stats['eligible_count']}/{override_stats['stop_count']} stops = "
        f"{override_stats['eligible_pct']}% eligible for empirical overlay)"
    )
    dw = r_gap.daily_window_stats

    r_emp = None
    if "empirical" in slips:
        r_emp = run_simulation(mode, stock_data, spy_df, dates, cache, i0, i1, empirical_stops=True)

    for slip in slips:
        if slip == "gap":
            r, trades = r_gap, gap_trades
        else:
            r, trades = r_emp, list(r_emp.trades_list)
        metrics = _sim_metrics(r, trades)
        overrides = _count_overrides(gap_trades, trades) if slip == "empirical" else 0
        override_pct = round(overrides / override_stats["stop_count"] * 100, 1) if override_stats["stop_count"] else 0.0

        row = {
            "test_name": f"schedule_{mode_name}",
            "horizon_yr": years,
            "slippage_model": slip,
            "run_date": str(date.today()),
            "days_both_windows": dw.get("days_both_windows", 0),
            "days_one_window": dw.get("days_one_window", 0),
            "morning_entry_trades": dw.get("morning_entry_trades", 0),
            "evening_entry_trades": dw.get("evening_entry_trades", 0),
            "notes": (
                f"empirical=Option A in-engine; {overrides}/{override_stats['stop_count']} "
                f"stops overridden ({override_pct}%)"
                if slip == "empirical" else ""
            ),
            **metrics,
        }
        out = SCHEDULE_DIR / f"{mode_name}_{years}yr_{slip}.csv"
        _write_trades(out, trades)
        _append_master(row)
        print(f"{mode_name} {years}yr {slip}: return {metrics['total_return_pct']:+.1f}%  "
              f"stops {metrics['stop_exit_count']}  both-window-days {dw.get('days_both_windows', 0)}  "
              f"({time.time()-t0:.0f}s) -> {out}")
        if slip == "empirical":
            print(f"  empirical overlay applied to {overrides} stops ({override_pct}%)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="dual_window", help="mode name or 'all'")
    ap.add_argument("--years", type=int, default=3, choices=[3, 7])
    ap.add_argument("--slippage", default="both", choices=["gap", "empirical", "both"])
    args = ap.parse_args()
    modes = [m.name for m in D3_SCHEDULE_MODES] if args.mode == "all" else [args.mode]
    for m in modes:
        run_mode(m, args.years, args.slippage)


if __name__ == "__main__":
    main()
