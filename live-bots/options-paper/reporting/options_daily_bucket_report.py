"""
Generate a per-bucket daily performance report from master_ledger.csv.

Writes to logs/options_trial/reports/YYYY-MM-DD_buckets.md and .csv
(committed by GitHub Actions with other bot logs).

Usage:
    python scripts/options_daily_bucket_report.py
    python scripts/options_daily_bucket_report.py --date 2026-07-06
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path
from statistics import mean, median

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_lab import (
    BUCKET_EXPERIMENTS,
    LEDGER_PATH,
    TRIAL_ROOT,
    ensure_trial_layout,
    load_state,
)

STALE_ENTRY_DAYS = 5  # open lots + last_entry older than this => warning


def _f(val, default=0.0) -> float:
    try:
        return float(val)
    except (TypeError, ValueError):
        return default


def _day_rows(rows: list[dict], day: str) -> list[dict]:
    out = []
    for r in rows:
        ts = str(r.get("ts", ""))
        if ts.startswith(day) or str(r.get("date", "")) == day:
            out.append(r)
    return out


def _pnl_for_exit(r: dict, lots: dict[str, dict]) -> float:
    if r.get("pnl_usd"):
        return _f(r["pnl_usd"])
    lot_id = r.get("lot_id") or ""
    ret = _f(r.get("return_pct"))
    if not lot_id or not ret:
        return 0.0
    lot = lots.get(lot_id)
    if not lot:
        return _f(r.get("cost")) * ret / 100.0
    qty = max(1, int(_f(r.get("qty"), 1)))
    entry_qty = max(1, lot.get("qty", 1))
    cost = lot.get("cost", 0)
    return cost * (qty / entry_qty) * ret / 100.0


def _row_day(r: dict) -> str:
    ts = str(r.get("ts", ""))
    if len(ts) >= 10:
        return ts[:10]
    return str(r.get("date", "") or "")


def _parse_day(day: str) -> date | None:
    try:
        return date.fromisoformat(day[:10])
    except ValueError:
        return None


def build_bucket_report(day: str) -> tuple[list[dict], dict]:
    ensure_trial_layout()
    if not LEDGER_PATH.exists():
        return [], {"day": day, "error": "no ledger"}

    all_rows = list(csv.DictReader(LEDGER_PATH.open(encoding="utf-8")))
    day_rows = _day_rows(all_rows, day)
    as_of = _parse_day(day) or date.today()

    lots: dict[str, dict] = {}
    last_entry_by_bucket: dict[int, str] = {}
    for r in all_rows:
        if r.get("event") == "entry" and r.get("lot_id"):
            lots[r["lot_id"]] = {
                "cost": _f(r.get("cost")),
                "qty": max(1, int(_f(r.get("qty"), 1))),
            }
            try:
                bid = int(r.get("bucket_id", -1))
            except (TypeError, ValueError):
                continue
            d = _row_day(r)
            if d and (bid not in last_entry_by_bucket or d > last_entry_by_bucket[bid]):
                last_entry_by_bucket[bid] = d

    open_lots_by_bucket: dict[int, list] = defaultdict(list)
    try:
        state = load_state()
        for lot in state.lots:
            if lot.qty > 0:
                open_lots_by_bucket[int(lot.bucket_id)].append(lot)
    except Exception:
        state = None

    entries_by_bucket: dict[int, list[dict]] = defaultdict(list)
    exits_by_bucket: dict[int, list[dict]] = defaultdict(list)
    for r in day_rows:
        try:
            bid = int(r.get("bucket_id", -1))
        except (TypeError, ValueError):
            continue
        if r.get("event") == "entry":
            entries_by_bucket[bid].append(r)
        elif r.get("event") == "exit":
            exits_by_bucket[bid].append(r)

    report_rows: list[dict] = []
    stale_buckets: list[dict] = []
    total_realized = 0.0
    total_exits = 0

    for b in BUCKET_EXPERIMENTS:
        ents = entries_by_bucket.get(b.bucket_id, [])
        exs = exits_by_bucket.get(b.bucket_id, [])
        rets = [_f(x.get("return_pct")) for x in exs if x.get("return_pct")]
        pnls = [_pnl_for_exit(x, lots) for x in exs]
        realized = sum(pnls)
        total_realized += realized
        total_exits += len(exs)

        symbols = sorted({x.get("symbol", "") for x in ents + exs if x.get("symbol")})
        strats = sorted({x.get("strategy_id", "") for x in ents + exs if x.get("strategy_id")})

        open_lots = open_lots_by_bucket.get(b.bucket_id, [])
        last_entry = last_entry_by_bucket.get(b.bucket_id, "")
        if not last_entry and open_lots:
            # Fall back to newest open-lot entry_date from lab state.
            dates = [str(getattr(l, "entry_date", "") or "")[:10] for l in open_lots]
            dates = [d for d in dates if len(d) == 10]
            if dates:
                last_entry = max(dates)
        stale = False
        stale_days = ""
        if open_lots and last_entry:
            last_d = _parse_day(last_entry)
            if last_d is not None:
                age = (as_of - last_d).days
                if age > STALE_ENTRY_DAYS:
                    stale = True
                    stale_days = age
                    stale_buckets.append(
                        {
                            "bucket_id": b.bucket_id,
                            "profile": b.name,
                            "open_lots": len(open_lots),
                            "last_entry": last_entry,
                            "days_since_entry": age,
                            "symbols": ",".join(sorted({l.underlying for l in open_lots if l.underlying})),
                        }
                    )

        if exs:
            status = "closed"
        elif ents:
            status = "entered_no_exit"
        elif open_lots and stale:
            status = "stale_open"
        elif open_lots:
            status = "open"
        else:
            status = "idle"

        reasons = [x.get("reason", "") for x in exs if x.get("reason")]
        row = {
            "bucket_id": b.bucket_id,
            "profile": b.name,
            "buy_rule": "mid" if b.buy_at_mid else f"ask{b.buy_limit_offset:+.2f}",
            "sell_rule": f"bid{b.sell_limit_offset:+.2f}",
            "take_profit_pct": round(b.take_profit * 100, 1),
            "stop_loss_pct": round(b.stop_loss * 100, 1),
            "entries": len(ents),
            "exits": len(exs),
            "open_lots": len(open_lots),
            "last_entry": last_entry,
            "stale": stale,
            "stale_days": stale_days,
            "win_rate_pct": round(100 * sum(1 for x in rets if x > 0) / len(rets), 1) if rets else "",
            "avg_return_pct": round(mean(rets), 2) if rets else "",
            "med_return_pct": round(median(rets), 2) if rets else "",
            "best_return_pct": round(max(rets), 2) if rets else "",
            "worst_return_pct": round(min(rets), 2) if rets else "",
            "realized_usd": round(realized, 2),
            "symbols": ",".join(symbols),
            "strategies": ",".join(strats),
            "exit_reasons": "; ".join(reasons[:3]) + ("…" if len(reasons) > 3 else ""),
            "status": status,
        }
        report_rows.append(row)

    summary = {
        "day": day,
        "buckets": len(BUCKET_EXPERIMENTS),
        "buckets_with_entries": sum(1 for r in report_rows if r["entries"] > 0),
        "buckets_with_exits": sum(1 for r in report_rows if r["exits"] > 0),
        "total_entries": sum(r["entries"] for r in report_rows),
        "total_exits": total_exits,
        "total_realized_usd": round(total_realized, 2),
        "stale_bucket_count": len(stale_buckets),
        "stale_buckets": stale_buckets,
        "stale_entry_days": STALE_ENTRY_DAYS,
        "generated_at": datetime.now().isoformat(),
    }
    return report_rows, summary


def write_report(day: str, report_rows: list[dict], summary: dict) -> tuple[Path, Path]:
    out_dir = TRIAL_ROOT / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / f"{day}_buckets.md"
    csv_path = out_dir / f"{day}_buckets.csv"

    lines = [
        f"# Options bucket report — {day}",
        "",
        f"_Generated {summary.get('generated_at', '')}_",
        "",
        "## Day summary",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Buckets defined | {summary.get('buckets', 0)} |",
        f"| Buckets with entries | {summary.get('buckets_with_entries', 0)} |",
        f"| Buckets with exits | {summary.get('buckets_with_exits', 0)} |",
        f"| Total entry events | {summary.get('total_entries', 0)} |",
        f"| Total exit events | {summary.get('total_exits', 0)} |",
        f"| Total realized (tracked) | ${summary.get('total_realized_usd', 0):+,.2f} |",
        f"| Stale buckets (open lots, last_entry >{summary.get('stale_entry_days', STALE_ENTRY_DAYS)}d) | "
        f"{summary.get('stale_bucket_count', 0)} |",
        "",
    ]

    stale = summary.get("stale_buckets") or []
    if stale:
        lines.extend(
            [
                "## Stale bucket warning",
                "",
                f"Buckets with open lots whose last ledger entry is older than "
                f"**{summary.get('stale_entry_days', STALE_ENTRY_DAYS)}** days — "
                "possible orphaned / stuck positions.",
                "",
                "| b | profile | open lots | last_entry | days | symbols |",
                "|---|---------|----------:|------------|-----:|---------|",
            ]
        )
        for s in stale:
            lines.append(
                f"| {s['bucket_id']} | {s['profile']} | {s['open_lots']} | "
                f"{s['last_entry']} | {s['days_since_entry']} | {s['symbols'] or '—'} |"
            )
        lines.append("")
    else:
        lines.extend(
            [
                "## Stale bucket warning",
                "",
                f"_None — no open-lot buckets with last_entry older than "
                f"{summary.get('stale_entry_days', STALE_ENTRY_DAYS)} days._",
                "",
            ]
        )

    lines.extend(
        [
            "## All buckets (b0–b99)",
            "",
            "| b | profile | entries | exits | open | last_entry | realized $ | avg ret% | symbols | strategies | status |",
            "|---|---------|--------:|------:|-----:|------------|-----------:|---------:|---------|------------|--------|",
        ]
    )
    for r in report_rows:
        avg = r["avg_return_pct"]
        avg_s = f"{avg:+.1f}" if avg != "" else "—"
        last = r.get("last_entry") or "—"
        lines.append(
            f"| {r['bucket_id']} | {r['profile']} | {r['entries']} | {r['exits']} | "
            f"{r.get('open_lots', 0)} | {last} | ${r['realized_usd']:+,.2f} | {avg_s} | "
            f"{r['symbols'] or '—'} | {r['strategies'] or '—'} | {r['status']} |"
        )

    lines.extend([
        "",
        "## Bucket parameters reference",
        "",
        "Full buy/sell/tp/sl grid: see `docs/options_trial/INDEX.md` or each bucket's `profile.json`.",
        "",
        "## Notes",
        "",
        "- **Pre-2026-07-07 runs** used optimistic entry logging (ledger entry on submit). "
        "P&L attribution may include `orphan_reconcile` (b0) when virtual lots drifted from broker.",
        "- **Post bf50fee8** registers entries on fill only; one entry attempt per bucket×strategy per day.",
        f"- **Stale flag:** open lots + last_entry older than {STALE_ENTRY_DAYS} days "
        "(possible stuck / orphaned bucket).",
        "",
    ])
    md_path.write_text("\n".join(lines), encoding="utf-8")

    # CSV: omit nested stale_buckets list; rows already have flat stale fields
    csv_rows = [{k: v for k, v in r.items()} for r in report_rows]
    if csv_rows:
        fields = list(csv_rows[0].keys())
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(csv_rows)

    return md_path, csv_path


def main() -> int:
    ap = argparse.ArgumentParser(description="Per-bucket daily options report")
    ap.add_argument("--date", default=date.today().isoformat(), help="YYYY-MM-DD")
    args = ap.parse_args()

    rows, summary = build_bucket_report(args.date)
    if summary.get("error"):
        print(f"No ledger at {LEDGER_PATH}")
        return 1

    md_path, csv_path = write_report(args.date, rows, summary)
    print(f"Wrote {md_path}")
    print(f"Wrote {csv_path}")
    print(
        f"Summary: {summary['buckets_with_exits']} buckets closed trades, "
        f"${summary['total_realized_usd']:+,.2f} realized"
    )
    stale_n = summary.get("stale_bucket_count", 0)
    if stale_n:
        print(f"STALE WARNING: {stale_n} bucket(s) with open lots and last_entry >{STALE_ENTRY_DAYS}d")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
