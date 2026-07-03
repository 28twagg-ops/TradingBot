"""Analysis of historical + synthetic research — ranked by return % per trade."""
import pandas as pd
from pathlib import Path

RESULTS = Path(__file__).resolve().parent / "results"
hist_path = RESULTS / "historical_backtest" / "catalog_historical_2026-07-03_merged_with_pct.csv"
if not hist_path.exists():
    hist_path = RESULTS / "historical_backtest" / "catalog_historical_2026-07-03_merged.csv"
paper_path = RESULTS / "historical_backtest" / "paper_top5_return_pct.csv"
syn_path = RESULTS / "catalog" / "2026-07-02_extensive" / "catalog_leaderboard.csv"

hist = pd.read_csv(hist_path)
syn_lb = pd.read_csv(syn_path)

has_pct = "avg_return_pct" in hist.columns

if not has_pct:
    print("NOTE: merged historical CSV lacks avg_return_pct — run enrich_return_pct.py")
    print("      Falling back to dollar exp_pnl_per_signal for this report.\n")
    rank_col, med_col = "avg_exp_pnl", "med_exp_pnl"
    hist = hist.rename(columns={"exp_pnl_per_signal": "avg_exp_pnl"})
    g = hist.groupby(["strategy_id", "strategy_name", "category", "signal"]).agg(
        symbols=("symbol", "nunique"),
        total_signals=("signals", "sum"),
        total_filled=("filled", "sum"),
        avg_exp_pnl=("avg_exp_pnl", "mean"),
        med_exp_pnl=("avg_exp_pnl", "median"),
        total_pnl=("total_pnl", "sum"),
        avg_win=("win_rate", "mean"),
    ).reset_index().sort_values("avg_exp_pnl", ascending=False)
else:
    rank_col, med_col = "avg_return_pct", "med_return_pct"
    g = hist.groupby(["strategy_id", "strategy_name", "category", "signal"]).agg(
        symbols=("symbol", "nunique"),
        total_signals=("signals", "sum"),
        total_filled=("filled", "sum"),
        avg_return_pct=("avg_return_pct", "mean"),
        med_return_pct=("med_return_pct", "median"),
        exp_return_pct=("exp_return_pct_per_signal", "mean"),
        total_pnl=("total_pnl", "sum"),
        avg_win=("win_rate", "mean"),
    ).reset_index().sort_values("avg_return_pct", ascending=False)

cols = ["strategy_id", "strategy_name", "category", "symbols",
        "total_filled", rank_col, med_col, "avg_win", "total_pnl"]

PAPER_TOP5 = ["S173", "S174", "S165", "S166", "S163"]

if paper_path.exists():
    pdf = pd.read_csv(paper_path)
    pg = pdf.groupby(["strategy_id", "strategy_name"]).agg(
        symbols=("symbol", "nunique"),
        total_filled=("filled", "sum"),
        avg_return_pct=("avg_return_pct", "mean"),
        med_return_pct=("med_return_pct", "median"),
        exp_return_pct=("exp_return_pct_per_signal", "mean"),
        avg_win=("win_rate", "mean"),
    ).reset_index()
    pg["_order"] = pg.strategy_id.map({s: i for i, s in enumerate(PAPER_TOP5)})
    pg = pg.sort_values("_order")
    print("=" * 70)
    print("PAPER TOP 5 — return % per filled trade (904 symbols)")
    print("  ratio 0.50 = +50% on premium per trade")
    print("=" * 70)
    pcols = ["strategy_id", "strategy_name", "symbols", "total_filled",
             "avg_return_pct", "med_return_pct", "exp_return_pct", "avg_win"]
    print(pg[pcols].to_string(index=False, float_format="%.4f"))
    print()

print("=" * 70)
print(f"HISTORICAL: TOP 20 STRATEGIES (by {rank_col} per filled trade, 904 symbols)")
print("=" * 70)
print(g.head(20)[cols].to_string(index=False, float_format="%.3f"))

print("\n" + "=" * 70)
print("PAPER BOT TOP 5 (implemented in options_morning_bot.py)")
print("=" * 70)
paper = g[g.strategy_id.isin(PAPER_TOP5)].copy()
paper["_order"] = paper.strategy_id.map({s: i for i, s in enumerate(PAPER_TOP5)})
paper = paper.sort_values("_order")
print(paper[cols].to_string(index=False, float_format="%.3f"))

print("\n" + "=" * 70)
print("ROBUST picks (positive avg+median return %, symbols>=100, fills>=500)")
print("=" * 70)
if has_pct:
    robust = g[(g.avg_return_pct > 0) & (g.med_return_pct > 0)
               & (g.symbols >= 100) & (g.total_filled >= 500)]
    print(robust.sort_values("med_return_pct", ascending=False).head(15)[cols]
          .to_string(index=False, float_format="%.3f"))
else:
    robust = g[(g.avg_exp_pnl > 0) & (g.med_exp_pnl > 0)
               & (g.symbols >= 100) & (g.total_filled >= 500)]
    print(robust.sort_values("med_exp_pnl", ascending=False).head(15)[cols]
          .to_string(index=False, float_format="%.2f"))
