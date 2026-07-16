"""
Generate a strategy-level selection report for options trial.

Outputs:
  logs/options_trial/reports/YYYY-MM-DD_strategy_selection.md
  logs/options_trial/reports/YYYY-MM-DD_strategy_selection.csv

Usage:
  python scripts/options_strategy_selection_report.py
  python scripts/options_strategy_selection_report.py --date 2026-07-09
"""
from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_lab import (
    DROPPED_STRATEGIES,
    LEDGER_PATH,
    ORPHAN_BUCKET_ID,
    ORPHAN_PROFILE,
    ORPHAN_STRATEGY,
    TRIAL_ROOT,
    ensure_trial_layout,
)
from options_signals import ALL_KNOWN_STRATEGIES, PAPER_STRATEGIES

ORPHAN_RATE_WARN = 0.10  # >10% orphan exits => attribution likely broken


@dataclass
class StratStats:
    strategy_id: str
    strategy_name: str
    entries: int = 0
    exits: int = 0
    wins: int = 0
    losses: int = 0
    avg_return_pct: float = 0.0
    med_return_pct: float = 0.0
    p10_return_pct: float = 0.0
    p90_return_pct: float = 0.0
    realized_usd: float = 0.0
    active_days: int = 0
    unique_symbols: int = 0
    top_symbol_share_pct: float = 0.0
    recommendation: str = "watch"
    rationale: str = ""


def _f(v, d=0.0) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return d


def _median(vals: list[float]) -> float:
    if not vals:
        return 0.0
    s = sorted(vals)
    n = len(s)
    m = n // 2
    return s[m] if n % 2 else (s[m - 1] + s[m]) / 2


def _percentile(vals: list[float], p: float) -> float:
    if not vals:
        return 0.0
    s = sorted(vals)
    if len(s) == 1:
        return s[0]
    k = (len(s) - 1) * p
    lo = int(k)
    hi = min(lo + 1, len(s) - 1)
    frac = k - lo
    return s[lo] * (1.0 - frac) + s[hi] * frac


def _recommend(exits: int, med_ret: float, p10: float, top_symbol_share_pct: float) -> tuple[str, str]:
    if exits < 8:
        return "watch", "insufficient sample (<8 exits)"
    if exits < 20:
        if med_ret <= 0:
            return "watch", "early sample with non-positive median"
        return "watch", "building sample (8-19 exits)"
    if med_ret <= 0:
        return "drop", "non-positive median return"
    if p10 < -45:
        return "watch", "fat left tail (p10 < -45%)"
    if top_symbol_share_pct >= 60:
        return "watch", "too concentrated in one symbol"
    if exits >= 30 and med_ret > 0 and p10 >= -35 and top_symbol_share_pct < 50:
        return "keep", "enough sample + positive median + acceptable tail/concentration"
    if exits >= 20 and med_ret > 5 and p10 >= -40:
        return "watch", "promising mid-sample — need more exits"
    return "watch", "promising but needs larger sample"


def build_report(as_of_day: str) -> tuple[list[StratStats], dict]:
    ensure_trial_layout()
    if not LEDGER_PATH.exists():
        return [], {"error": f"no ledger at {LEDGER_PATH}"}

    rows = list(csv.DictReader(LEDGER_PATH.open(encoding="utf-8")))
    # Use all data up to as_of_day inclusive.
    filt = []
    for r in rows:
        ts = str(r.get("ts", ""))
        d = ts[:10] if len(ts) >= 10 else str(r.get("date", ""))
        if d and d <= as_of_day:
            filt.append(r)

    exits_by_sid: dict[str, list[dict]] = defaultdict(list)
    entries_by_sid: dict[str, list[dict]] = defaultdict(list)
    for r in filt:
        sid = r.get("strategy_id") or "?"
        ev = r.get("event")
        if ev == "entry":
            entries_by_sid[sid].append(r)
        elif ev == "exit":
            exits_by_sid[sid].append(r)

    sid_to_name = {s.id: s.name for s in ALL_KNOWN_STRATEGIES}
    all_sids = sorted(set(list(sid_to_name.keys()) + list(entries_by_sid.keys()) + list(exits_by_sid.keys())))
    all_sids = [sid for sid in all_sids if sid in sid_to_name]
    out: list[StratStats] = []

    for sid in all_sids:
        exits = exits_by_sid.get(sid, [])
        entries = entries_by_sid.get(sid, [])
        rets: list[float] = []
        realized = 0.0
        symbol_counts: dict[str, int] = defaultdict(int)
        days: set[str] = set()
        for r in exits:
            ret = _f(r.get("return_pct"), None)
            if ret is not None:
                rets.append(ret)
            realized += _f(r.get("pnl_usd"), 0.0)
            sym = r.get("symbol") or "?"
            symbol_counts[sym] += 1
            ts = str(r.get("ts", ""))
            if len(ts) >= 10:
                days.add(ts[:10])
            elif r.get("date"):
                days.add(str(r.get("date")))

        n = len(rets)
        wins = sum(1 for x in rets if x > 0)
        losses = sum(1 for x in rets if x <= 0)
        top_share = 0.0
        if symbol_counts:
            top_share = 100.0 * max(symbol_counts.values()) / max(1, sum(symbol_counts.values()))
        avg = sum(rets) / n if n else 0.0
        med = _median(rets)
        p10 = _percentile(rets, 0.10)
        p90 = _percentile(rets, 0.90)
        rec, why = _recommend(n, med, p10, top_share)
        if sid in DROPPED_STRATEGIES:
            rec, why = "drop", "manually paused — excluded from new entries & reflected P&L"

        out.append(
            StratStats(
                strategy_id=sid,
                strategy_name=sid_to_name.get(sid, sid),
                entries=len(entries),
                exits=n,
                wins=wins,
                losses=losses,
                avg_return_pct=round(avg, 2),
                med_return_pct=round(med, 2),
                p10_return_pct=round(p10, 2),
                p90_return_pct=round(p90, 2),
                realized_usd=round(realized, 2),
                active_days=len(days),
                unique_symbols=len(symbol_counts),
                top_symbol_share_pct=round(top_share, 1),
                recommendation=rec,
                rationale=why,
            )
        )

    out.sort(key=lambda s: ({"keep": 0, "watch": 1, "drop": 2}.get(s.recommendation, 3), -s.med_return_pct, -s.exits))

    # Attribution health: orphan exits are not strategy edge — high rate means broken tagging.
    total_exit_events = 0
    orphan_exit_events = 0
    for r in filt:
        if r.get("event") != "exit":
            continue
        total_exit_events += 1
        sid = str(r.get("strategy_id") or "")
        profile = str(r.get("profile") or "")
        # b0 is also a real controlled-layout bucket — do NOT key off bucket_id alone.
        if sid == ORPHAN_STRATEGY or profile == ORPHAN_PROFILE:
            orphan_exit_events += 1
    orphan_rate = (orphan_exit_events / total_exit_events) if total_exit_events else 0.0

    summary = {
        "as_of": as_of_day,
        "generated_at": datetime.now().isoformat(),
        "strategies": len(out),
        "keep": sum(1 for x in out if x.recommendation == "keep"),
        "watch": sum(1 for x in out if x.recommendation == "watch"),
        "drop": sum(1 for x in out if x.recommendation == "drop"),
        "total_exits": total_exit_events,
        "orphan_exits": orphan_exit_events,
        "orphan_rate": round(orphan_rate, 4),
        "orphan_alert": orphan_rate > ORPHAN_RATE_WARN and total_exit_events > 0,
    }
    return out, summary


def write_report(as_of_day: str, rows: list[StratStats], summary: dict) -> tuple[Path, Path]:
    out_dir = TRIAL_ROOT / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / f"{as_of_day}_strategy_selection.md"
    csv_path = out_dir / f"{as_of_day}_strategy_selection.csv"

    lines = [
        f"# Options strategy selection report — {as_of_day}",
        "",
        f"_Generated {summary.get('generated_at', '')}_",
        "",
        "## Summary",
        "",
        f"- Strategies analyzed: **{summary.get('strategies', 0)}**",
        f"- Keep: **{summary.get('keep', 0)}**",
        f"- Watch: **{summary.get('watch', 0)}**",
        f"- Drop: **{summary.get('drop', 0)}**",
        "",
        "## Attribution health",
        "",
        f"- Total exits: **{summary.get('total_exits', 0)}**",
        f"- Orphan exits (b{ORPHAN_BUCKET_ID}/{ORPHAN_PROFILE}): **{summary.get('orphan_exits', 0)}**",
        f"- Orphan rate: **{100.0 * float(summary.get('orphan_rate', 0)):.1f}%** "
        f"(warn if >{100 * ORPHAN_RATE_WARN:.0f}%)",
    ]
    if summary.get("orphan_alert"):
        lines.append(
            f"- **ALERT:** orphan_rate > {100 * ORPHAN_RATE_WARN:.0f}% — "
            "check client_order_id tagging / fill attribution before trusting strategy P&L."
        )
    else:
        lines.append("- Orphan rate OK (attribution looks healthy).")
    lines.extend(
        [
            "",
            "## Strategy scoreboard",
            "",
            "| strategy | recommendation | exits | win% | med ret% | avg ret% | p10% | p90% | realized $ | symbols | top symbol share | rationale |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for r in rows:
        win_pct = (100.0 * r.wins / r.exits) if r.exits else 0.0
        lines.append(
            f"| {r.strategy_id} ({r.strategy_name}) | {r.recommendation} | {r.exits} | "
            f"{win_pct:.1f} | {r.med_return_pct:+.2f} | {r.avg_return_pct:+.2f} | "
            f"{r.p10_return_pct:+.2f} | {r.p90_return_pct:+.2f} | ${r.realized_usd:+,.2f} | "
            f"{r.unique_symbols} | {r.top_symbol_share_pct:.1f}% | {r.rationale} |"
        )
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.",
            "- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.",
            "- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.",
            "- `watch` means potentially viable but still sample-limited or risk-concentrated.",
            "- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).",
            f"- Orphan rate = orphan_exits / total_exits; alert if >{100 * ORPHAN_RATE_WARN:.0f}% (attribution failure, not edge).",
            "",
        ]
    )
    md_path.write_text("\n".join(lines), encoding="utf-8")

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "strategy_id",
                "strategy_name",
                "recommendation",
                "rationale",
                "entries",
                "exits",
                "wins",
                "losses",
                "avg_return_pct",
                "med_return_pct",
                "p10_return_pct",
                "p90_return_pct",
                "realized_usd",
                "active_days",
                "unique_symbols",
                "top_symbol_share_pct",
            ],
        )
        w.writeheader()
        for r in rows:
            w.writerow(r.__dict__)

    return md_path, csv_path


def main() -> int:
    ap = argparse.ArgumentParser(description="Options strategy selection report")
    ap.add_argument("--date", default=date.today().isoformat(), help="As-of date YYYY-MM-DD")
    args = ap.parse_args()

    rows, summary = build_report(args.date)
    if summary.get("error"):
        print(summary["error"])
        return 1
    md, csvp = write_report(args.date, rows, summary)
    print(f"Wrote {md}")
    print(f"Wrote {csvp}")
    print(f"Summary: keep={summary['keep']} watch={summary['watch']} drop={summary['drop']}")
    orphan_pct = 100.0 * float(summary.get("orphan_rate", 0))
    alert = " ALERT" if summary.get("orphan_alert") else ""
    print(
        f"Orphan rate: {orphan_pct:.1f}% "
        f"({summary.get('orphan_exits', 0)}/{summary.get('total_exits', 0)}){alert}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

