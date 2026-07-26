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
from datetime import date, datetime, timedelta
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

# Display DTE / family labels for experiment grouping.
DTE_PROFILE: dict[str, str] = {
    "S163": "7d ATM",
    "S164": "1d ATM",
    "S165": "3d ATM",
    "S166": "3d ATM strong",
    "S167": "3d 1-OTM",
    "S168": "5d ATM",
    "S169": "3d ATM BB squeeze",
    "S170": "3d ATM golden pocket",
    "S171": "3d ATM VWAP reclaim",
    "S172": "3d ATM trend resume",
    "S175": "3d ATM earnings drift",
    "S173": "MomRev",
    "S174": "RubberBand (dropped)",
    # Phase-1 (2026-07-25B)
    "S200": "3d ATM gap-aggr", "S201": "3d ATM gap-mild",
    "S202": "3d ATM gap-monster", "S203": "3d ATM gap-up fade (put)",
    "S204": "3d ATM gap-up cont", "S205": "3d ATM gap-highvol",
    "S206": "3d ATM gap-trend", "S207": "3d ATM gap-support",
    "S208": "3d ATM gap-ma200", "S209": "3d ATM gap-recovery",
    "S210": "3d ATM MA cross 8/21", "S211": "3d ATM MA cross 21/50",
    "S212": "3d ATM MA bounce 50", "S213": "3d ATM MA bounce 200",
    "S214": "3d ATM death cross (put)", "S215": "3d ATM MA reclaim 200",
    "S216": "3d ATM RSI x30", "S217": "3d ATM RSI<25 bounce",
    "S218": "3d ATM BB lower touch", "S219": "3d ATM vol climax up",
}

COMPARISON_GROUPS: list[tuple[str, list[str]]] = [
    ("GapDown DTE comparison", ["S163", "S164", "S165", "S168"]),
    ("GapDown Strike comparison", ["S165", "S167"]),
    ("New Pattern Strategies — GapDown signal independent",
     ["S169", "S170", "S171", "S172", "S175"]),
    ("Phase-1 Gap family", ["S200", "S201", "S202", "S204", "S205", "S206", "S207", "S208", "S209"]),
    ("Phase-1 Bearish Gap & MA", ["S203", "S214"]),
    ("Phase-1 MA family", ["S210", "S211", "S212", "S213", "S215"]),
    ("Phase-1 RSI/BB/Vol", ["S216", "S217", "S218", "S219"]),
    ("Other", ["S173"]),
]


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
    p25_return_pct: float = 0.0
    p90_return_pct: float = 0.0
    realized_usd: float = 0.0
    active_days: int = 0
    days_since_first_entry: int | None = None
    entries_last_5d: int = 0
    exits_last_5d: int = 0
    dte_profile: str = ""
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


def _row_day(r: dict) -> str:
    ts = str(r.get("ts", ""))
    if len(ts) >= 10:
        return ts[:10]
    return str(r.get("date", "") or "")


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


def _dte_profile_for(sid: str) -> str:
    if sid in DTE_PROFILE:
        return DTE_PROFILE[sid]
    for s in ALL_KNOWN_STRATEGIES:
        if s.id == sid:
            return f"{s.dte_target}d"
    return "?"


def build_report(as_of_day: str) -> tuple[list[StratStats], dict]:
    ensure_trial_layout()
    if not LEDGER_PATH.exists():
        return [], {"error": f"no ledger at {LEDGER_PATH}"}

    rows = list(csv.DictReader(LEDGER_PATH.open(encoding="utf-8")))
    # Use all data up to as_of_day inclusive.
    filt = []
    for r in rows:
        d = _row_day(r)
        if d and d <= as_of_day:
            filt.append(r)

    try:
        as_of = date.fromisoformat(as_of_day)
    except ValueError:
        as_of = date.today()
    last5_start = (as_of - timedelta(days=4)).isoformat()

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
            d = _row_day(r)
            if d:
                days.add(d)

        entry_days = [_row_day(r) for r in entries if _row_day(r)]
        first_entry = min(entry_days) if entry_days else None
        days_since = None
        if first_entry:
            try:
                days_since = (as_of - date.fromisoformat(first_entry)).days
            except ValueError:
                days_since = None

        entries_last_5 = sum(1 for r in entries if last5_start <= _row_day(r) <= as_of_day)
        exits_last_5 = sum(1 for r in exits if last5_start <= _row_day(r) <= as_of_day)

        n = len(rets)
        wins = sum(1 for x in rets if x > 0)
        losses = sum(1 for x in rets if x <= 0)
        top_share = 0.0
        if symbol_counts:
            top_share = 100.0 * max(symbol_counts.values()) / max(1, sum(symbol_counts.values()))
        avg = sum(rets) / n if n else 0.0
        med = _median(rets)
        p10 = _percentile(rets, 0.10)
        p25 = _percentile(rets, 0.25)
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
                p25_return_pct=round(p25, 2),
                p90_return_pct=round(p90, 2),
                realized_usd=round(realized, 2),
                active_days=len(days),
                days_since_first_entry=days_since,
                entries_last_5d=entries_last_5,
                exits_last_5d=exits_last_5,
                dte_profile=_dte_profile_for(sid),
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
        "by_id": {s.strategy_id: s for s in out},
    }
    return out, summary


def _comparison_section(rows: list[StratStats]) -> list[str]:
    by_id = {r.strategy_id: r for r in rows}
    lines = [
        "## Comparison groups",
        "",
        "Experiment arms grouped for side-by-side decisions. "
        "INSUFFICIENT if any arm has n<10 exits.",
        "",
    ]
    for title, sids in COMPARISON_GROUPS:
        lines.append(f"### {title}")
        lines.append("")
        arms = [by_id[s] for s in sids if s in by_id]
        if not arms:
            lines.append("_No data yet for this group._")
            lines.append("")
            continue
        insuff = any(a.exits < 10 for a in arms)
        best_med = max(arms, key=lambda a: a.med_return_pct)
        best_p10 = max(arms, key=lambda a: a.p10_return_pct)
        status = "INSUFFICIENT" if insuff else "OK"
        lines.append(
            f"- Status: **{status}** | Best median: **{best_med.strategy_id}** "
            f"({best_med.med_return_pct:+.2f}%) | Best p10: **{best_p10.strategy_id}** "
            f"({best_p10.p10_return_pct:+.2f}%)"
        )
        lines.append("")
        lines.append(
            "| strategy | DTE profile | exits | med% | p10% | p25% | entries 5d | exits 5d |"
        )
        lines.append("|---|---|---:|---:|---:|---:|---:|---:|")
        for a in arms:
            lines.append(
                f"| {a.strategy_id} | {a.dte_profile} | {a.exits} | "
                f"{a.med_return_pct:+.2f} | {a.p10_return_pct:+.2f} | "
                f"{a.p25_return_pct:+.2f} | {a.entries_last_5d} | {a.exits_last_5d} |"
            )
        lines.append("")
    return lines


def _pipeline_section(rows: list[StratStats]) -> list[str]:
    """
    Strategy Pipeline Status section -- added 2026-07-25B.
    Reads from strategy_eval.md if available, else builds from StratStats.
    """
    from pathlib import Path as _Path
    from options_strategy_lab import (
        evaluate_for_kill, _load_ledger, _LEDGER_PATH,
        KILL_MIN_N, PROMOTE_MIN_N, PROMOTE_MEDIAN_THRESH,
    )

    eval_report = TRIAL_ROOT / "reports" / "strategy_eval.md"
    ledger_df = _load_ledger(_LEDGER_PATH)

    today = date.today().isoformat()
    lines: list[str] = [
        "## Strategy Pipeline Status",
        "",
        f"_Pipeline evaluation as of {today}. "
        "Auto-kill thresholds: median<-25% at n>=15, p10<-85%, WR<15% at n>=25. "
        "Promote: n>=30 median>0%._",
        "",
        "| Strategy | Signal | n | Median% | WR% | Status | Days |",
        "|----------|--------|---|---------|-----|--------|------|",
    ]

    by_id = {r.strategy_id: r for r in rows}

    # Include all rows (existing S163-S175) plus phase-1 (S200+)
    all_ids: list[str] = sorted(
        {r.strategy_id for r in rows}
        | {s.id for s in PAPER_STRATEGIES if s.id >= "S200"},
        key=lambda x: x,
    )

    for sid in all_ids:
        r = by_id.get(sid)
        n = r.exits if r else 0
        med = f"{r.med_return_pct:+.2f}%" if (r and r.exits >= 1) else "—"
        wr_pct = (100.0 * r.wins / r.exits) if (r and r.exits) else 0.0
        wr_s = f"{wr_pct:.0f}%" if (r and r.exits) else "—"
        days = r.days_since_first_entry if r and r.days_since_first_entry else 0
        signal_name = r.strategy_name if r else sid

        verdict = "NEW"
        if ledger_df is not None and n >= KILL_MIN_N:
            verdict = evaluate_for_kill(sid, ledger_df)
        elif n > 0:
            verdict = "WATCH"

        lines.append(
            f"| {sid} | {signal_name[:22]} | {n} | {med} | {wr_s} "
            f"| {verdict} | {days} |"
        )

    # Auto-kill log
    lines += [
        "",
        "## Auto-Kill Log",
        "",
        "| Date | Strategy | Reason | n | Median% |",
        "|------|----------|--------|---|---------|",
    ]
    # Pull from eval report if present
    killed_rows = []
    if eval_report.exists():
        try:
            text = eval_report.read_text(encoding="utf-8")
            in_kill = False
            for ln in text.splitlines():
                if "## Auto-Kill Log" in ln:
                    in_kill = True
                    continue
                if in_kill and ln.startswith("| 20"):
                    killed_rows.append(ln)
                elif in_kill and ln.startswith("##"):
                    break
        except Exception:
            pass
    if killed_rows:
        lines.extend(killed_rows)
    else:
        lines.append("| — | — | (no kills yet) | — | — |")

    # Promote candidates
    promote = [
        r for r in rows
        if r.exits >= PROMOTE_MIN_N and r.med_return_pct > PROMOTE_MEDIAN_THRESH
    ]
    lines += [
        "",
        "## Promote Candidates (n>=30, median>0%)",
        "",
        "| Strategy | n | Median% | WR% | Recommendation |",
        "|----------|---|---------|-----|----------------|",
    ]
    if promote:
        for r in sorted(promote, key=lambda x: -x.med_return_pct):
            wr_pct = (100.0 * r.wins / r.exits) if r.exits else 0.0
            lines.append(
                f"| {r.strategy_id} | {r.exits} | {r.med_return_pct:+.2f}% "
                f"| {wr_pct:.0f}% | Tyler review |"
            )
    else:
        lines.append("| — | — | — | — | (none yet — collecting data) |")

    lines.append("")
    return lines


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
            "| strategy | DTE | rec | exits | win% | med% | p10% | p25% | p90% | "
            "days live | ent 5d | exit 5d | realized $ | top share | rationale |",
            "|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for r in rows:
        win_pct = (100.0 * r.wins / r.exits) if r.exits else 0.0
        days_live = r.days_since_first_entry if r.days_since_first_entry is not None else "—"
        lines.append(
            f"| {r.strategy_id} ({r.strategy_name}) | {r.dte_profile} | {r.recommendation} | "
            f"{r.exits} | {win_pct:.1f} | {r.med_return_pct:+.2f} | {r.p10_return_pct:+.2f} | "
            f"{r.p25_return_pct:+.2f} | {r.p90_return_pct:+.2f} | {days_live} | "
            f"{r.entries_last_5d} | {r.exits_last_5d} | ${r.realized_usd:+,.2f} | "
            f"{r.top_symbol_share_pct:.1f}% | {r.rationale} |"
        )
    lines.append("")
    lines.extend(_comparison_section(rows))
    lines.extend(_pipeline_section(rows))
    lines.extend(
        [
            "## Notes",
            "",
            "- Selection emphasizes robustness first: median > 0, acceptable left tail (**p10**), and symbol diversification.",
            "- **p10 (10th percentile return %)** is the primary options risk metric — fat left tails hide behind a flat median.",
            "- **p25** sits between p10 and median for mid-tail visibility.",
            "- `keep` requires >=30 exits with positive median and no extreme concentration/tail risk.",
            "- `watch` means potentially viable but still sample-limited or risk-concentrated.",
            "- `drop` means current evidence is not supportive (e.g., non-positive median with enough exits).",
            f"- Orphan rate = orphan_exits / total_exits; alert if >{100 * ORPHAN_RATE_WARN:.0f}% (attribution failure, not edge).",
            "- Active paper strategies: " + ", ".join(s.id for s in PAPER_STRATEGIES) + ".",
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
                "dte_profile",
                "recommendation",
                "rationale",
                "entries",
                "exits",
                "wins",
                "losses",
                "avg_return_pct",
                "med_return_pct",
                "p10_return_pct",
                "p25_return_pct",
                "p90_return_pct",
                "realized_usd",
                "active_days",
                "days_since_first_entry",
                "entries_last_5d",
                "exits_last_5d",
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
