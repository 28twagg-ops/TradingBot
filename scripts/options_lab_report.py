"""Summarize paper lab by bucket and strategy; write per-bucket summary.md."""
from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_lab import BUCKET_EXPERIMENTS, LEDGER_PATH, TRIAL_ROOT, bucket_dir, ensure_trial_layout

PAPER = ["S173", "S174", "S165", "S166", "S163"]


def _stats(vals: list[float]) -> str:
    if not vals:
        return "n=0"
    vals = sorted(vals)
    avg = sum(vals) / len(vals)
    med = vals[len(vals) // 2]
    return f"n={len(vals)} avg={avg:+.1f}% med={med:+.1f}%"


def main() -> int:
    ensure_trial_layout()
    if not LEDGER_PATH.exists():
        print(f"No ledger yet: {LEDGER_PATH}")
        print("Run options_morning_bot.py during market hours to populate.")
        return 0

    rows = list(csv.DictReader(LEDGER_PATH.open(encoding="utf-8")))
    exits = [r for r in rows if r.get("event") == "exit" and r.get("return_pct")]
    by_bucket: dict[str, list[float]] = defaultdict(list)
    by_strat: dict[str, list[float]] = defaultdict(list)

    for r in exits:
        try:
            v = float(r["return_pct"])
        except Exception:
            continue
        key = f"b{r.get('bucket_id','?')}|{r.get('profile','?')}"
        by_bucket[key].append(v)
        by_strat[r.get("strategy_id", "?")].append(v)

    print("=" * 60)
    print("OPTIONS TRIAL — exits by bucket")
    print("=" * 60)
    for b in BUCKET_EXPERIMENTS:
        key = f"b{b.bucket_id}|{b.name}"
        print(f"  {key:28s}  {_stats(by_bucket.get(key, []))}")
        summary = [
            f"# Bucket b{b.bucket_id} — {b.name}",
            "",
            f"Virtual equity: $500",
            "",
            "## Profile",
            "```json",
            json.dumps({
                "buy_limit_offset": b.buy_limit_offset,
                "buy_at_mid": b.buy_at_mid,
                "sell_limit_offset": b.sell_limit_offset,
                "max_premium": b.max_premium,
                "max_spread_frac": b.max_spread_frac,
                "account_cap": b.account_cap,
                "take_profit": b.take_profit,
                "stop_loss": b.stop_loss,
                "eod_only": b.eod_only,
            }, indent=2),
            "```",
            "",
            f"## Exits: {_stats(by_bucket.get(key, []))}",
            "",
            f"Ledger: `buckets/b{b.bucket_id}_{b.name}/ledger.csv`",
        ]
        (bucket_dir(b.bucket_id, b.name) / "summary.md").write_text(
            "\n".join(summary), encoding="utf-8"
        )

    print("\n" + "=" * 60)
    print("OPTIONS TRIAL — exits by strategy")
    print("=" * 60)
    for sid in PAPER:
        print(f"  {sid:6s}  {_stats(by_strat.get(sid, []))}")

    print(f"\nMaster ledger: {LEDGER_PATH}")
    print(f"Trial root:    {TRIAL_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
