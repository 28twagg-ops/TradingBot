"""Signal frequency + yearly return estimates for paper top 5."""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from historical_backtest import HIST_DIR, load_daily_parquet

PAPER = ["S173", "S174", "S165", "S166", "S163"]
TRADING_DAYS = 252

pct = pd.read_csv(
    ROOT / "results/historical_backtest/catalog_historical_2026-07-03_merged_with_pct.csv",
    low_memory=False,
)
_, df = load_daily_parquet(HIST_DIR / "stocks" / "AAPL_daily.parquet")
years = (df.index.max() - df.index.min()).days / 365.25

sub = pct[pct.strategy_id.isin(PAPER)]
g = sub.groupby(["strategy_id", "strategy_name"]).agg(
    symbols=("symbol", "nunique"),
    total_signals=("signals", "sum"),
    total_filled=("filled", "sum"),
    fill_rate=("fill_rate", "mean"),
    avg_ret=("avg_return_pct", "mean"),
    med_ret=("med_return_pct", "median"),
    exp_ret_sig=("exp_return_pct_per_signal", "mean"),
    win_rate=("win_rate", "mean"),
).reset_index()

g["signals_per_sym_yr"] = g.total_signals / years / g.symbols
g["fills_per_sym_yr"] = g.total_filled / years / g.symbols
g["signals_all_yr"] = g.total_signals / years
g["fills_all_yr"] = g.total_filled / years
g["_o"] = g.strategy_id.map({s: i for i, s in enumerate(PAPER)})
g = g.sort_values("_o")

print(f"History span: ~{years:.1f} years | 904 symbols | 252 trading days/yr\n")

print("PER STRATEGY (avg per symbol per year):")
print("-" * 90)
for _, r in g.iterrows():
    print(f"  {r.strategy_id} {r.strategy_name}")
    print(f"    Signals: {r.signals_per_sym_yr:.2f}/sym/yr  |  Fills: {r.fills_per_sym_yr:.2f}/sym/yr  "
          f"|  Fill rate: {r.fill_rate:.0%}")
    print(f"    Avg return/fill: {r.avg_ret:.1%}  |  Median: {r.med_ret:.1%}  |  Win rate: {r.win_rate:.0%}")
    print(f"    Expected return per signal: {r.exp_ret_sig:.1%}")
    print()

tot_sig_day = g.signals_all_yr.sum() / TRADING_DAYS
tot_fill_day = g.fills_all_yr.sum() / TRADING_DAYS
print("UNIVERSE TOTALS (all 904 symbols):")
print(f"  Signal activations: ~{g.signals_all_yr.sum():,.0f}/yr  (~{tot_sig_day:.0f}/trading day)")
print(f"  Filled trades:      ~{g.fills_all_yr.sum():,.0f}/yr  (~{tot_fill_day:.0f}/trading day)")

w_avg = (g.avg_ret * g.total_filled).sum() / g.total_filled.sum()
print(f"\n  Fill-weighted avg return per trade: {w_avg:.1%}")

# $500 paper bot realistic
print("\n$500 PAPER BOT — REALISTIC YEARLY RANGE (NOT a promise):")
print("-" * 90)
print("Assumptions: 1 contract, ~$60 premium, 5 strategy slots, capital limits trades")
prem = 60
capital = 500
for n_trades, label in [(30, "low (30 fills/yr)"), (60, "mid (60 fills/yr)"), (120, "high (120 fills/yr)")]:
    acct_r = w_avg * (prem / capital)
    simple = n_trades * prem * w_avg
    simple_pct = simple / capital * 100
    compound = ((1 + acct_r) ** n_trades - 1) * 100
    print(f"  {label}: simple ~${simple:,.0f} ({simple_pct:.0f}% on $500) | "
          f"compounded ~{compound:.0f}%")

print("\nCAVEAT: Historical = daily bars + Black-Scholes, not live fills/slippage.")
print("Paper lab will measure real slippage; expect lower than backtest.")
