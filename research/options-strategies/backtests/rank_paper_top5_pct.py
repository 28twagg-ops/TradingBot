"""Fast return-% ranking for the 5 paper-bot strategies across all symbols."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from historical_backtest import HIST_DIR, backtest_strategy_on_prepared, load_daily_parquet
from options_strategy_registry import load_registry

PAPER_TOP5 = ["S173", "S174", "S165", "S166", "S163"]
OUT = ROOT / "results" / "historical_backtest" / "paper_top5_return_pct.csv"


def run_shard(symbols: list[str], out_path: Path) -> pd.DataFrame:
    strategies = {s.id: s for s in load_registry() if s.id in PAPER_TOP5}
    rows: list[dict] = []
    for si, sym in enumerate(symbols):
        path = HIST_DIR / "stocks" / f"{sym}_daily.parquet"
        if not path.exists():
            continue
        try:
            sym_name, df_feat = load_daily_parquet(path)
        except Exception as exc:
            print(f"  skip {sym}: {exc}", flush=True)
            continue
        raw_cache: dict = {}
        for sid in PAPER_TOP5:
            strat = strategies[sid]
            try:
                agg = backtest_strategy_on_prepared(sym_name, df_feat, strat, raw_cache)
            except Exception as exc:
                print(f"  {sym}/{sid}: {exc}", flush=True)
                continue
            if agg.get("signals_considered", 0) == 0:
                continue
            rows.append({
                "strategy_id": sid,
                "strategy_name": strat.name,
                "symbol": sym_name,
                "signals": agg.get("signals_considered", 0),
                "filled": agg.get("filled", 0),
                "win_rate": agg.get("win_rate", 0),
                "avg_return_pct": agg.get("avg_return_pct", 0),
                "med_return_pct": agg.get("med_return_pct", 0),
                "exp_return_pct_per_signal": agg.get("exp_return_pct_per_signal", 0),
                "exp_pnl_per_signal": agg.get("exp_pnl_per_signal", 0),
                "total_pnl": agg.get("total_pnl", 0),
            })
        if (si + 1) % 50 == 0:
            print(f"  [{si + 1}/{len(symbols)}] symbols …", flush=True)
    df = pd.DataFrame(rows)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Shard saved -> {out_path} ({len(df)} rows)", flush=True)
    return df


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    g = df.groupby(["strategy_id", "strategy_name"]).agg(
        symbols=("symbol", "nunique"),
        total_signals=("signals", "sum"),
        total_filled=("filled", "sum"),
        avg_return_pct=("avg_return_pct", "mean"),
        med_return_pct=("med_return_pct", "median"),
        exp_return_pct=("exp_return_pct_per_signal", "mean"),
        avg_win=("win_rate", "mean"),
        total_pnl=("total_pnl", "sum"),
    ).reset_index()
    g["_order"] = g.strategy_id.map({s: i for i, s in enumerate(PAPER_TOP5)})
    return g.sort_values("_order")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbols", default="", help="Comma-separated symbol subset")
    ap.add_argument("--shard", default="", help="Shard tag for output file")
    ap.add_argument("--merge-only", action="store_true")
    args = ap.parse_args()

    if args.merge_only:
        shards = sorted(OUT.parent.glob("paper_top5_return_pct_shard*.csv"))
        if not shards:
            print("No shard files to merge")
            return 1
        df = pd.concat([pd.read_csv(p) for p in shards], ignore_index=True)
        df.to_csv(OUT, index=False)
        g = summarize(df)
        print(f"Merged {len(shards)} shards -> {OUT} ({len(df)} rows)")
        _print_summary(g)
        return 0

    if args.symbols:
        symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
    else:
        symbols = sorted({p.stem.replace("_daily", "").upper()
                          for p in (HIST_DIR / "stocks").glob("*_daily.parquet")})

    out_path = OUT if not args.shard else OUT.with_name(
        f"paper_top5_return_pct_{args.shard}.csv")
    print(f"Ranking {len(PAPER_TOP5)} strategies x {len(symbols)} symbols -> {out_path.name}",
          flush=True)
    df = run_shard(symbols, out_path)
    if not args.shard:
        _print_summary(summarize(df))
    return 0


def _print_summary(g: pd.DataFrame) -> None:
    print("\nPAPER TOP 5 — avg return % per filled trade (mean across symbols):")
    cols = ["strategy_id", "strategy_name", "symbols", "total_filled",
            "avg_return_pct", "med_return_pct", "exp_return_pct", "avg_win"]
    print(g[cols].to_string(index=False, float_format="%.4f"))


if __name__ == "__main__":
    raise SystemExit(main())
