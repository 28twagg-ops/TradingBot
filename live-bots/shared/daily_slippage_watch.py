"""
Daily stop-slippage monitor — writes logs/analysis/daily_slippage_watch.md
Run after each bot session (CI) or on demand.
"""
from __future__ import annotations

import csv
import statistics
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

STOP_TRIGGER = -0.5
ALERT_OVERSHOOT_PP = 0.8  # mean overshoot worse than this vs -0.5%
ALERT_STOP_MEAN = -1.2
GOOD_OVERSHOOT_PP = 0.5
GOOD_STOP_MEAN = -0.9


def _read_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _stops_for_day(tx_rows: list[dict], day: str) -> list[dict]:
    out = []
    for r in tx_rows:
        if r.get("date") != day or r.get("action") != "SELL":
            continue
        if "stop_loss" not in (r.get("exit_reason") or ""):
            continue
        try:
            pnl = float(r.get("pnl_pct") or 0)
        except (TypeError, ValueError):
            continue
        out.append({"ticker": r.get("ticker", ""), "pnl_pct": pnl})
    return out


def _audit_stops_for_day(audit_rows: list[dict], day: str) -> list[dict]:
    out = []
    for r in audit_rows:
        if r.get("date") != day or r.get("action") != "SELL":
            continue
        if "stop_loss" not in (r.get("exit_reason") or r.get("note") or ""):
            continue
        try:
            slip = float(r.get("slippage_pct") or 0)
        except (TypeError, ValueError):
            slip = 0.0
        out.append({
            "ticker": r.get("ticker", ""),
            "method": r.get("execution_method") or "?",
            "slippage_pct": slip,
        })
    return out


def _summarize_stops(stops: list[dict]) -> dict:
    if not stops:
        return {}
    pnls = [s["pnl_pct"] for s in stops]
    overshoots = [p - STOP_TRIGGER for p in pnls]
    n = len(pnls)
    within_1 = sum(1 for p in pnls if p >= -1.0)
    return {
        "count": n,
        "mean_pnl": statistics.mean(pnls),
        "min_pnl": min(pnls),
        "max_pnl": max(pnls),
        "overshoot_pp": statistics.mean(overshoots),
        "within_1pct": within_1,
        "worst": sorted(stops, key=lambda x: x["pnl_pct"])[:5],
    }


def _verdict(mean_pnl: float, overshoot_pp: float) -> str:
    if overshoot_pp <= -ALERT_OVERSHOOT_PP or mean_pnl <= ALERT_STOP_MEAN:
        return "ALERT"
    if overshoot_pp <= -GOOD_OVERSHOOT_PP or mean_pnl <= GOOD_STOP_MEAN:
        return "WATCH"
    return "OK"


def build_report(logs_dir: Path, lookback_days: int = 14) -> str:
    tx_rows = _read_csv(logs_dir / "transactions.csv")
    audit_rows = _read_csv(logs_dir / "execution_audit.csv")
    today = date.today()

    lines = [
        "# Daily Slippage Watch",
        f"*Updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}*",
        "",
        "Tracks **stop P&L** (position loss vs entry) vs **execution slippage** "
        "(fill vs limit). Target: stops near -0.5% trigger when no overnight gap.",
        "",
        "| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |",
        "|-----|-------|-----------|---------------------|------------|-----------|--------|",
    ]

    for i in range(lookback_days):
        d = (today - timedelta(days=i)).isoformat()
        stops = _stops_for_day(tx_rows, d)
        audit_stops = _audit_stops_for_day(audit_rows, d)
        if not stops:
            continue
        s = _summarize_stops(stops)
        sell_slips = []
        for r in audit_rows:
            if r.get("date") != d and r.get("action") != "SELL":
                continue
            try:
                sell_slips.append(float(r.get("slippage_pct") or 0))
            except (TypeError, ValueError):
                pass
        slip_mean = statistics.mean(sell_slips) if sell_slips else 0.0
        verdict = _verdict(s["mean_pnl"], s["overshoot_pp"])
        lines.append(
            f"| {d} | {s['count']} | {s['mean_pnl']:+.2f}% | "
            f"{s['overshoot_pp']:+.2f}pp | {s['within_1pct']}/{s['count']} | "
            f"{slip_mean:+.4f}% | **{verdict}** |"
        )

    # Today detail
    day = today.isoformat()
    stops_t = _stops_for_day(tx_rows, day)
    audit_t = _audit_stops_for_day(audit_rows, day)
    lines += ["", f"## Today ({day}) detail", ""]
    if stops_t:
        s = _summarize_stops(stops_t)
        lines.append(f"- Stop count: **{s['count']}**")
        lines.append(f"- Mean stop P&L: **{s['mean_pnl']:+.2f}%** (overshoot {s['overshoot_pp']:+.2f}pp)")
        lines.append(f"- Within -1.0%: {s['within_1pct']}/{s['count']}")
        lines.append(f"- Worst: " + ", ".join(
            f"{w['ticker']} {w['pnl_pct']:+.1f}%" for w in s["worst"]))
        methods = Counter(a["method"] for a in audit_t)
        if methods:
            lines.append("- Stop execution methods:")
            for m, c in methods.most_common():
                lines.append(f"  - `{m}`: {c}")
    else:
        lines.append("_No stop losses recorded today._")

    # Rolling baseline
    all_stops = []
    for r in tx_rows:
        if r.get("action") == "SELL" and "stop_loss" in (r.get("exit_reason") or ""):
            try:
                all_stops.append(float(r.get("pnl_pct") or 0))
            except (TypeError, ValueError):
                pass
    if all_stops:
        hist_os = statistics.mean([p - STOP_TRIGGER for p in all_stops])
        lines += [
            "",
            "## Historical baseline (all logs)",
            f"- Stop samples: {len(all_stops)}",
            f"- Mean stop P&L: {statistics.mean(all_stops):+.2f}%",
            f"- Mean overshoot: {hist_os:+.2f}pp",
            "",
            "**Alert** if overshoot < -0.8pp or mean stop < -1.2%. "
            "**OK** if overshoot > -0.5pp and mean stop > -0.9%.",
        ]

    return "\n".join(lines) + "\n"


def main():
    logs_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("logs")
    out = logs_dir / "analysis" / "daily_slippage_watch.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_report(logs_dir), encoding="utf-8")
    print(f"Written {out}")


if __name__ == "__main__":
    main()
