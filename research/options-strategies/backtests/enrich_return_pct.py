"""Add avg_return_pct columns — supports sharding for parallel runs."""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from historical_backtest import (
    HIST_DIR,
    backtest_strategy_on_prepared,
    load_daily_parquet,
)
from options_strategy_registry import load_registry

MERGED = ROOT / "results" / "historical_backtest" / "catalog_historical_2026-07-03_merged.csv"
OUT = MERGED.with_name(MERGED.stem + "_with_pct.csv")


def run_symbols(symbols: list[str], df: pd.DataFrame, strategies: dict,
                  shard: str = "") -> pd.DataFrame:
    tag = f"_{shard}" if shard else ""
    checkpoint = OUT.with_name(OUT.stem + f"{tag}_checkpoint.csv")
    pct_rows: list[dict] = []
    done: set[str] = set()

    if checkpoint.exists():
        cp = pd.read_csv(checkpoint)
        if len(cp):
            pct_rows = cp.to_dict("records")
            done = set(cp["symbol"].unique())
            print(f"  resume {shard}: {len(done)} symbols", flush=True)

    t0 = time.time()
    pending = [s for s in symbols if s not in done]
    print(f"  shard {shard or 'main'}: {len(pending)} symbols pending", flush=True)

    for i, sym in enumerate(pending):
        path = HIST_DIR / "stocks" / f"{sym}_daily.parquet"
        if not path.exists():
            continue
        try:
            sym_name, df_feat = load_daily_parquet(path)
        except Exception as exc:
            print(f"  skip {sym}: {exc}", flush=True)
            continue
        raw_cache: dict = {}
        for sid in df.loc[df.symbol == sym, "strategy_id"].unique():
            strat = strategies.get(sid)
            if not strat:
                continue
            try:
                agg = backtest_strategy_on_prepared(sym_name, df_feat, strat, raw_cache)
                pct_rows.append({
                    "strategy_id": sid,
                    "symbol": sym_name,
                    "avg_return_pct": agg.get("avg_return_pct", 0),
                    "med_return_pct": agg.get("med_return_pct", 0),
                    "exp_return_pct_per_signal": agg.get("exp_return_pct_per_signal", 0),
                })
            except Exception as exc:
                print(f"  {sym}/{sid}: {exc}", flush=True)
        if (i + 1) % 3 == 0 or i == 0:
            elapsed = time.time() - t0
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            left = (len(pending) - i - 1) / rate / 60 if rate > 0 else 0
            print(f"  [{shard}] {i + 1}/{len(pending)} {sym} "
                  f"({len(pct_rows)} rows, ~{left:.0f}m left)", flush=True)
        if (i + 1) % 5 == 0:
            pd.DataFrame(pct_rows).to_csv(checkpoint, index=False)

    pd.DataFrame(pct_rows).to_csv(checkpoint, index=False)
    print(f"  shard {shard or 'main'} done -> {checkpoint} ({len(pct_rows)} rows)", flush=True)
    return pd.DataFrame(pct_rows)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbols", default="", help="Comma-separated subset")
    ap.add_argument("--shard", default="", help="Shard tag")
    ap.add_argument("--merge-only", action="store_true")
    args = ap.parse_args()

    if args.merge_only:
        shards = sorted(OUT.parent.glob(OUT.stem + "_shard*_checkpoint.csv"))
        if not shards:
            print("No shard checkpoints found")
            return 1
        pct_df = pd.concat([pd.read_csv(p) for p in shards], ignore_index=True)
        df = pd.read_csv(MERGED)
        merged = df.merge(pct_df, on=["strategy_id", "symbol"], how="left")
        merged.to_csv(OUT, index=False)
        print(f"Merged {len(shards)} shards -> {OUT} ({len(merged)} rows)", flush=True)
        return 0

    if not MERGED.exists():
        print(f"Missing {MERGED}")
        return 1

    df = pd.read_csv(MERGED)
    strategies = {s.id: s for s in load_registry() if not s.multi_leg}
    if args.symbols:
        symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
    else:
        symbols = sorted(df["symbol"].unique())

    print(f"Enrich shard={args.shard or 'all'}: {len(symbols)} symbols", flush=True)
    run_symbols(symbols, df, strategies, args.shard)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
