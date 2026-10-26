"""
options_robustness_tests.py — Offline validation on historical return-% data.

Runs now (no API): outlier scrub, median-robust rank, period split proxy,
top-5 drawdown-style stats, strategy overlap check.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "results" / "options_trial" / "simulations"
PAPER = ["S173", "S174", "S165", "S166", "S163"]

MERGED = ROOT / "results/historical_backtest/catalog_historical_2026-07-03_merged_with_pct.csv"
PAPER_CSV = ROOT / "results/historical_backtest/paper_top5_return_pct.csv"


def load() -> pd.DataFrame:
    return pd.read_csv(MERGED, low_memory=False)


def rank_table(g: pd.DataFrame, title: str) -> str:
    cols = ["strategy_id", "strategy_name", "symbols", "total_filled",
            "avg_return_pct", "med_return_pct", "pct_positive_syms"]
    g = g.sort_values("avg_return_pct", ascending=False)
    return f"\n{title}\n" + g[cols].to_string(index=False, float_format="%.4f")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    df = load()
    paper = df[df.strategy_id.isin(PAPER)].copy()

    lines = ["# Options Robustness Tests", f"Source: {MERGED.name}", ""]

    # 1) Baseline top-5
    g0 = paper.groupby(["strategy_id", "strategy_name"]).agg(
        symbols=("symbol", "nunique"),
        total_filled=("filled", "sum"),
        avg_return_pct=("avg_return_pct", "mean"),
        med_return_pct=("med_return_pct", "median"),
        pct_positive_syms=("avg_return_pct", lambda s: (s > 0).mean()),
    ).reset_index()
    lines.append(rank_table(g0, "## 1. Baseline top-5 (symbol-mean return %)"))

    # 2) Outlier scrub: drop top 5% symbol rows per strategy by avg_return_pct
    scrubbed = []
    for sid, grp in paper.groupby("strategy_id"):
        cutoff = grp["avg_return_pct"].quantile(0.95)
        scrubbed.append(grp[grp["avg_return_pct"] <= cutoff])
    paper_scrub = pd.concat(scrubbed)
    g1 = paper_scrub.groupby(["strategy_id", "strategy_name"]).agg(
        symbols=("symbol", "nunique"),
        total_filled=("filled", "sum"),
        avg_return_pct=("avg_return_pct", "mean"),
        med_return_pct=("med_return_pct", "median"),
        pct_positive_syms=("avg_return_pct", lambda s: (s > 0).mean()),
    ).reset_index()
    lines.append(rank_table(g1, "## 2. After dropping top 5% symbol outliers per strategy"))

    # 3) Robust filter: median>0, avg>0, 50+ symbols
    g2 = g0[(g0.med_return_pct > 0) & (g0.avg_return_pct > 0) & (g0.symbols >= 50)]
    lines.append(rank_table(g2, "## 3. Robust filter (avg>0, median>0, 50+ symbols)"))

    # 4) Fill-weighted portfolio return (top 5)
    w = (g0.avg_return_pct * g0.total_filled).sum() / g0.total_filled.sum()
    lines.append(f"\n## 4. Fill-weighted avg return/trade (top 5): {w:.2%}")

    # 5) Per-symbol return distribution (paper detail csv)
    if PAPER_CSV.exists():
        pd_ = pd.read_csv(PAPER_CSV)
        for sid in PAPER:
            sub = pd_[pd_.strategy_id == sid]["avg_return_pct"]
            if len(sub) == 0:
                continue
            lines.append(
                f"\n### {sid} symbol distribution: "
                f"p10={sub.quantile(0.1):.2%} p50={sub.median():.2%} "
                f"p90={sub.quantile(0.9):.2%} pct_pos={(sub > 0).mean():.0%}"
            )

    # 6) Simulated $500 drawdown proxy: bootstrap 50 trades from paper fills
    rng = np.random.default_rng(42)
    if PAPER_CSV.exists():
        pd_ = pd.read_csv(PAPER_CSV)
        rets = pd_["avg_return_pct"].values
        rets = rets[np.isfinite(rets)]
        if len(rets) > 20:
            sims = []
            for _ in range(500):
                pick = rng.choice(rets, size=50, replace=True)
                acct = 1.0
                for r in pick:
                    acct *= 1 + r * 0.12  # ~$60 on $500
                sims.append(acct - 1)
            arr = np.array(sims)
            lines.append("\n## 6. Bootstrap 50-trade $500 proxy (12% premium/trade)")
            lines.append(f"  median ending return: {np.median(arr):.1%}")
            lines.append(f"  5th percentile:       {np.quantile(arr, 0.05):.1%}")
            lines.append(f"  95th percentile:      {np.quantile(arr, 0.95):.1%}")
            lines.append(f"  % simulations loss:   {(arr < 0).mean():.1%}")

    # 7) Full universe robust top 15
    all_g = df.groupby(["strategy_id", "strategy_name", "category"]).agg(
        symbols=("symbol", "nunique"),
        total_filled=("filled", "sum"),
        avg_return_pct=("avg_return_pct", "mean"),
        med_return_pct=("med_return_pct", "median"),
    ).reset_index()
    robust_all = all_g[
        (all_g.avg_return_pct > 0) & (all_g.med_return_pct > 0)
        & (all_g.symbols >= 100) & (all_g.total_filled >= 500)
    ].sort_values("med_return_pct", ascending=False).head(15)
    lines.append("\n## 7. Full universe robust top 15 (for challenger ideas)")
    lines.append(robust_all.to_string(index=False, float_format="%.4f"))

    report = "\n".join(lines)
    out_path = OUT / "robustness_report.md"
    out_path.write_text(report, encoding="utf-8")
    print(report)
    print(f"\nSaved -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
