"""
rubber_band_report.py — Live per-strategy leaderboard for the equity bot.

Outputs:
  logs/rubber_band_report.md

Always exits 0 (non-fatal for GHA).

Usage:
  python scripts/rubber_band_report.py
"""
from __future__ import annotations

import csv
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median

REPO = Path(__file__).resolve().parent.parent
TX = REPO / "logs" / "transactions.csv"
RUNS = REPO / "logs" / "runs.csv"
OUT = REPO / "logs" / "rubber_band_report.md"

# Always show these on the board (n=0 → NEW / WATCH).
KNOWN_STRATEGIES = [
    "Pullback50", "MomReversal", "RSIRecovery", "52wkLow", "RubberBand",
    "MA_Squeeze", "GoldenPocket", "VWAP_Reclaim", "TrendResumption", "EarningsDrift",
]
DISABLED_STRATEGIES = ["GapDown", "VolumeSpike"]


def _f(v, d=0.0) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return d


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


def _exit_bucket(reason: str) -> str:
    r = (reason or "").lower()
    if r.startswith("stop_loss"):
        return "stop_loss"
    if r.startswith("max_hold"):
        return "max_hold"
    if r.startswith("midline"):
        return "midline"
    return "other"


def build() -> str:
    if not TX.exists():
        return "# Rubber Band Strategy Leaderboard\n\n_No transactions.csv yet._\n"

    rows = list(csv.DictReader(TX.open(encoding="utf-8")))
    sells = [r for r in rows if (r.get("action") or "").upper() == "SELL" and r.get("pnl_pct") not in ("", None)]

    by_strat: dict[str, list[dict]] = defaultdict(list)
    for r in sells:
        by_strat[(r.get("strategy") or "unknown").strip() or "unknown"].append(r)

    board = []
    for strat, grp in by_strat.items():
        if strat in DISABLED_STRATEGIES:
            continue
        pnls = [_f(r["pnl_pct"]) for r in grp]
        dollars = [_f(r.get("pnl_dollar")) for r in grp]
        holds = [_f(r.get("hold_days")) for r in grp if r.get("hold_days") not in ("", None)]
        wins = [p for p in pnls if p > 0]
        losses = [p for p in pnls if p <= 0]
        gw = sum(d for d in dollars if d > 0)
        gl = abs(sum(d for d in dollars if d < 0))
        pf = (gw / gl) if gl > 0 else (999.0 if gw > 0 else 0.0)
        board.append({
            "strategy": strat,
            "n": len(pnls),
            "wr": 100.0 * len(wins) / len(pnls) if pnls else 0.0,
            "avg": mean(pnls) if pnls else 0.0,
            "med": median(pnls) if pnls else 0.0,
            "p10": _percentile(pnls, 0.10),
            "pf": pf,
            "hold": mean(holds) if holds else 0.0,
            "total": sum(dollars),
        })
    board.sort(key=lambda x: (-x["pf"], -x["avg"], -x["n"]))

    seen = {b["strategy"] for b in board}
    for name in KNOWN_STRATEGIES:
        if name not in seen:
            board.append({
                "strategy": name,
                "n": 0,
                "wr": 0.0,
                "avg": 0.0,
                "med": 0.0,
                "p10": 0.0,
                "pf": 0.0,
                "hold": 0.0,
                "total": 0.0,
                "status": "NEW",
            })
    # Keep ranked filled strategies first, then NEW (n=0) alphabetically.
    board.sort(key=lambda x: (0 if x["n"] > 0 else 1, -x["pf"], -x["avg"], x["strategy"]))

    by_exit: dict[str, list[float]] = defaultdict(list)
    for r in sells:
        by_exit[_exit_bucket(r.get("exit_reason", ""))].append(_f(r["pnl_pct"]))

    # Monthly: last 3 calendar months with equity from runs.csv
    month_stats: dict[str, dict] = {}
    for r in sells:
        d = (r.get("date") or "")[:7]
        if not d:
            continue
        month_stats.setdefault(d, {"n": 0, "wins": 0, "pnls": [], "dollars": 0.0})
        p = _f(r["pnl_pct"])
        month_stats[d]["n"] += 1
        month_stats[d]["wins"] += 1 if p > 0 else 0
        month_stats[d]["pnls"].append(p)
        month_stats[d]["dollars"] += _f(r.get("pnl_dollar"))

    equity_by_day: dict[str, float] = {}
    if RUNS.exists():
        for r in csv.DictReader(RUNS.open(encoding="utf-8")):
            ts = r.get("timestamp") or ""
            if len(ts) >= 10:
                equity_by_day[ts[:10]] = _f(r.get("equity"))

    months = sorted(month_stats.keys())[-3:]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        "# Rubber Band Strategy Leaderboard",
        f"*Updated: {now}*",
        "*All strategies equal weight since 2026-07-18 schedule removal*",
        "",
        "| Rank | Strategy | n | WR% | Avg PnL% | Med PnL% | p10% | PF | Avg Hold | Total $ | Status |",
        "|------|----------|--:|----:|---------:|---------:|-----:|---:|---------:|--------:|--------|",
    ]
    for i, b in enumerate(board, 1):
        status = b.get("status") or ("WATCH" if b["n"] < 30 else "ACTIVE")
        if b["n"] == 0:
            status = "NEW"
        lines.append(
            f"| {i} | {b['strategy']} | {b['n']} | {b['wr']:.0f}% | "
            f"{b['avg']:+.2f}% | {b['med']:+.2f}% | {b['p10']:+.2f}% | "
            f"{b['pf']:.2f} | {b['hold']:.1f}d | ${b['total']:+.2f} | {status} |"
        )

    lines.extend([
        "",
        "## Disabled strategies (no new entries)",
        "",
        "| Strategy | Status |",
        "|----------|--------|",
    ])
    for name in DISABLED_STRATEGIES:
        lines.append(f"| {name} | Disabled 2026-07-20 |")

    lines.extend(["", "## Exit reason breakdown", "",
                  "| Exit Type | n | WR% | Avg PnL% |",
                  "|-----------|--:|----:|---------:|"])
    for et in ("stop_loss", "max_hold", "midline", "other"):
        vals = by_exit.get(et, [])
        if not vals:
            continue
        wr = 100.0 * sum(1 for v in vals if v > 0) / len(vals)
        lines.append(f"| {et} | {len(vals)} | {wr:.0f}% | {mean(vals):+.2f}% |")

    lines.extend(["", "## Monthly performance (last 3 months)", "",
                  "| Month | Trades | WR% | Avg PnL% | Equity Start | Equity End | Return |",
                  "|-------|-------:|----:|---------:|-------------:|-----------:|-------:|"])
    for m in months:
        st = month_stats[m]
        wr = 100.0 * st["wins"] / st["n"] if st["n"] else 0.0
        avg = mean(st["pnls"]) if st["pnls"] else 0.0
        days = sorted(d for d in equity_by_day if d.startswith(m))
        eq0 = equity_by_day[days[0]] if days else None
        eq1 = equity_by_day[days[-1]] if days else None
        ret = ((eq1 / eq0 - 1.0) * 100.0) if eq0 and eq1 and eq0 > 0 else None
        eq0s = f"${eq0:,.2f}" if eq0 else "—"
        eq1s = f"${eq1:,.2f}" if eq1 else "—"
        rets = f"{ret:+.2f}%" if ret is not None else "—"
        lines.append(
            f"| {m} | {st['n']} | {wr:.0f}% | {avg:+.2f}% | {eq0s} | {eq1s} | {rets} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    try:
        text = build()
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(text, encoding="utf-8")
        print(f"Wrote {OUT}")
        # Print leaderboard body for session logs
        for line in text.splitlines():
            if line.startswith("|") and "Strategy" not in line and "----" not in line:
                if line.count("|") >= 8:
                    print(line)
                    if line.strip().startswith("| 7 ") or "unknown" in line.lower():
                        break
        return 0
    except Exception as e:
        print(f"rubber_band_report failed: {e}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
