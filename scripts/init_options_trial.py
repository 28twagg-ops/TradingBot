"""Initialize options_trial folder layout + sync docs to local docs/options_trial/."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_lab import (
    BUCKET_EXPERIMENTS, STRATEGY_TWEAKS, PAPER_UNLIMITED_BUCKETS, VIRTUAL_BUCKET_USD,
    bucket_dir, ensure_trial_layout, experiment_layout_id, load_state, save_state,
    sync_state_layout, trial_root,
)

GIT = Path(__file__).resolve().parent.parent

try:
    from local_docs import local_docs, local_docs_available
    DOCS = local_docs("options_trial") if local_docs_available() else None
except Exception:
    DOCS = None


def main() -> int:
    ensure_trial_layout()
    state = load_state()
    note = sync_state_layout(state)
    if note:
        save_state(state)
        print(f"Layout: {experiment_layout_id()} ({note})")
    else:
        print(f"Layout: {experiment_layout_id()}")

    if DOCS is None:
        print(f"Trial layout: {trial_root()}")
        print("Docs:         skipped (local docs unavailable on this runner)")
        print(f"Buckets:      {len(BUCKET_EXPERIMENTS)}")
        return 0

    DOCS.mkdir(parents=True, exist_ok=True)

    index = [
        "# Options Trial — Documentation Index",
        "",
        "Separate from **rubber_band_bot** (`logs/daily/`, `logs/ab_test/`).",
        "",
        "## Runtime files (git repo)",
        f"Root: `{trial_root()}`",
        "",
        "| Path | Purpose |",
        "|------|---------|",
        "| `_state/lab_state.json` | Open virtual lots, pending orders |",
        "| `_state/lab_buckets.json` | Live premium per bucket |",
        "| `_state/strategies.json` | Top-5 IDs + per-strategy tweaks |",
        "| `_ledger/master_ledger.csv` | All entries/exits |",
        "| `runs/YYYY-MM-DD.md` | Bot run log per day |",
        "| `buckets/b{N}_{name}/profile.json` | Frozen bucket parameters |",
        "| `buckets/b{N}_{name}/ledger.csv` | Trades for this bucket only |",
        "| `buckets/b{N}_{name}/summary.md` | Auto stats (lab_report) |",
        "| `simulations/` | Offline test outputs |",
        "",
        "## Buckets ($500 virtual each)",
        f"Profiles defined: **{len(BUCKET_EXPERIMENTS)}** | "
        f"Paper unlimited: **{PAPER_UNLIMITED_BUCKETS}**",
        "",
    ]

    for b in BUCKET_EXPERIMENTS:
        slug = f"b{b.bucket_id}_{b.name}"
        doc_path = DOCS / "buckets" / f"{slug}.md"
        doc_path.parent.mkdir(parents=True, exist_ok=True)
        body = f"""# Bucket {b.bucket_id}: {b.name}

Virtual equity: **${VIRTUAL_BUCKET_USD:.0f}** per bucket (fixed; not split from broker balance)

## Buy parameters
| Parameter | Value |
|-----------|-------|
| buy_limit_offset | {b.buy_limit_offset} (from ask) |
| buy_at_mid | {b.buy_at_mid} |
| max_premium | ${b.max_premium:.0f}/contract |
| max_spread_frac | {b.max_spread_frac:.0%} |
| min_open_interest | {b.min_open_interest} |
| account_cap | {b.account_cap:.0%} of $500 |
| max_contracts | {b.max_contracts} |

## Sell parameters
| Parameter | Value |
|-----------|-------|
| sell_limit_offset | {b.sell_limit_offset} (from bid) |
| sell_at_mid | {b.sell_at_mid} |
| take_profit | {b.take_profit:+.0%} on premium |
| stop_loss | {b.stop_loss:+.0%} on premium |
| eod_only | {b.eod_only} |
| market_exit_eod | {b.market_exit_eod} |

## Order tags
- Entry: `LB{b.bucket_id}|<strategy>|YYYYMMDD`
- Exit: `LX{b.bucket_id}|<strategy>|<lot_id>`

## Files
- Repo: `logs/options_trial/buckets/{slug}/`
- profile.json, ledger.csv, summary.md, README.txt

## Strategy tweaks (layered on this bucket)
```json
{json.dumps(STRATEGY_TWEAKS, indent=2)}
```
"""
        doc_path.write_text(body, encoding="utf-8")
        index.append(f"- [{slug}](buckets/{slug}.md) — buy={b.buy_limit_offset}, tp={b.take_profit:+.0%}, sl={b.stop_loss:+.0%}")

    (DOCS / "INDEX.md").write_text("\n".join(index), encoding="utf-8")
    readme = trial_root() / "README.txt"
    readme.write_text(
        "OPTIONS TRIAL — separate from rubber_band_bot logs/daily/\n"
        "Docs: ../TradingBot/docs/options_trial/INDEX.md (local)\n"
        "Init: python scripts/init_options_trial.py\n"
        "Report: python scripts/options_lab_report.py\n",
        encoding="utf-8",
    )
    print(f"Trial layout: {trial_root()}")
    print(f"Docs:         {DOCS}")
    print(f"Buckets:      {len(BUCKET_EXPERIMENTS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
