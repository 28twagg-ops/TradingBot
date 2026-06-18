#!/usr/bin/env python3
"""Daily June execution audit for live bot logs.

This script builds a deterministic audit report from repo logs and (optionally)
an Alpaca fills export CSV.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Iterable


@dataclass
class SellRow:
    date: str
    ticker: str
    strategy: str
    pnl_pct: float
    pnl_dollar: float
    exit_reason: str
    timestamp: str


def _safe_float(v: str | None) -> float:
    try:
        return float((v or "").strip() or 0.0)
    except Exception:
        return 0.0


def _read_tx_sells(tx_file: Path) -> list[SellRow]:
    rows: list[SellRow] = []
    with tx_file.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("action") or "").strip().upper() != "SELL":
                continue
            rows.append(
                SellRow(
                    date=(r.get("date") or "").strip(),
                    ticker=(r.get("ticker") or "").strip(),
                    strategy=(r.get("strategy") or "").strip() or "?",
                    pnl_pct=_safe_float(r.get("pnl_pct")),
                    pnl_dollar=_safe_float(r.get("pnl_dollar")),
                    exit_reason=(r.get("exit_reason") or "").strip(),
                    timestamp=(r.get("timestamp") or "").strip(),
                )
            )
    return rows


def _read_runs(runs_file: Path) -> list[dict[str, str]]:
    with runs_file.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _month_key(date_str: str) -> str:
    return date_str[:7]


def _is_june(date_str: str) -> bool:
    return _month_key(date_str) == "2026-06"


def _is_may(date_str: str) -> bool:
    return _month_key(date_str) == "2026-05"


def _iter_daily_files(daily_dir: Path) -> Iterable[Path]:
    if not daily_dir.exists():
        return []
    return sorted(daily_dir.glob("*.md"))


def _daily_trade_mismatch(daily_dir: Path, tx_by_date: dict[str, int], month_prefix: str = "2026-06") -> list[str]:
    mismatches: list[str] = []
    for p in _iter_daily_files(daily_dir):
        date_key = p.stem
        if not date_key.startswith(month_prefix):
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        says_no_trades = "No trades today." in text
        tx_count = tx_by_date.get(date_key, 0)
        if says_no_trades and tx_count > 0:
            mismatches.append(f"{date_key}: daily log says no trades but tx has {tx_count}")
    return mismatches


def _load_broker_sell_keys(broker_csv: Path) -> set[tuple[str, str]]:
    keys: set[tuple[str, str]] = set()
    with broker_csv.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    # Flexible column mapping for common Alpaca export fields.
    date_cols = ("filled_at", "submitted_at", "created_at", "date", "timestamp")
    ticker_cols = ("symbol", "ticker")
    side_cols = ("side", "order_side", "action")
    status_cols = ("status", "order_status")
    for r in rows:
        side = ""
        for c in side_cols:
            if c in r and r[c]:
                side = r[c].strip().lower()
                break
        if side and "sell" not in side:
            continue
        status = ""
        for c in status_cols:
            if c in r and r[c]:
                status = r[c].strip().lower()
                break
        if status and "fill" not in status:
            continue
        ticker = ""
        for c in ticker_cols:
            if c in r and r[c]:
                ticker = r[c].strip().upper()
                break
        if not ticker:
            continue
        raw_dt = ""
        for c in date_cols:
            if c in r and r[c]:
                raw_dt = r[c].strip()
                break
        if not raw_dt:
            continue
        dt = raw_dt[:10]
        keys.add((dt, ticker))
    return keys


def _format_pct(num: float) -> str:
    return f"{num:+.2f}%"


def main() -> int:
    ap = argparse.ArgumentParser(description="Build June daily execution audit report.")
    ap.add_argument("--tx", default="logs/transactions.csv", help="Path to transactions.csv")
    ap.add_argument("--runs", default="logs/runs.csv", help="Path to runs.csv")
    ap.add_argument("--daily-dir", default="logs/daily", help="Path to logs/daily directory")
    ap.add_argument(
        "--broker-csv",
        default="",
        help="Optional Alpaca fills export CSV for phantom-sell reconciliation",
    )
    ap.add_argument(
        "--out",
        default="logs/analysis/june_audit_latest.md",
        help="Output markdown report path",
    )
    ap.add_argument(
        "--min-june-sells",
        type=int,
        default=20,
        help="Minimum June sells before strategy gate is evaluated",
    )
    ap.add_argument(
        "--min-june-winrate",
        type=float,
        default=45.0,
        help="Minimum June sell win rate (percent) for strategy PASS",
    )
    ap.add_argument(
        "--min-june-avg-pct",
        type=float,
        default=-0.10,
        help="Minimum June average pnl_pct per sell for strategy PASS",
    )
    args = ap.parse_args()

    tx_file = Path(args.tx)
    runs_file = Path(args.runs)
    daily_dir = Path(args.daily_dir)
    out_file = Path(args.out)

    sells = _read_tx_sells(tx_file)
    runs = _read_runs(runs_file)

    june_sells = [s for s in sells if _is_june(s.date)]
    may_sells = [s for s in sells if _is_may(s.date)]

    def summarize(rows: list[SellRow]) -> dict[str, float]:
        n = len(rows)
        wins = sum(1 for r in rows if r.pnl_pct > 0)
        pnl = sum(r.pnl_dollar for r in rows)
        wr = (wins / n * 100.0) if n else 0.0
        avg_pct = (sum(r.pnl_pct for r in rows) / n) if n else 0.0
        return {"n": n, "wins": wins, "pnl": pnl, "wr": wr, "avg_pct": avg_pct}

    june = summarize(june_sells)
    may = summarize(may_sells)

    overshoot_june = [s for s in june_sells if "stop_loss" in s.exit_reason and s.pnl_pct <= -3.0]
    overshoot_may = [s for s in may_sells if "stop_loss" in s.exit_reason and s.pnl_pct <= -3.0]

    dup_counter = Counter((s.date, s.ticker) for s in june_sells)
    dupes = [(d, t, c) for (d, t), c in dup_counter.items() if c > 1]

    tx_by_date = Counter(s.date for s in sells)
    daily_mismatch = _daily_trade_mismatch(daily_dir, dict(tx_by_date), month_prefix="2026-06")

    exits_by_date = defaultdict(int)
    for r in runs:
        d = (r.get("timestamp") or "")[:10]
        exits_by_date[d] += int(_safe_float(r.get("exits")))
    june_dates = sorted({s.date for s in june_sells})
    run_vs_tx = []
    for d in june_dates:
        tx_n = sum(1 for s in june_sells if s.date == d)
        run_n = exits_by_date.get(d, 0)
        if tx_n != run_n:
            run_vs_tx.append((d, tx_n, run_n))

    phantom_lines: list[str] = []
    if args.broker_csv:
        broker_file = Path(args.broker_csv)
        if broker_file.exists():
            broker_keys = _load_broker_sell_keys(broker_file)
            missing = [(s.date, s.ticker) for s in june_sells if (s.date, s.ticker) not in broker_keys]
            for d, t in sorted(set(missing)):
                phantom_lines.append(f"{d} {t}")
        else:
            phantom_lines.append(f"Broker CSV not found: {broker_file}")
    else:
        phantom_lines.append("Broker CSV not provided (phantom-sell check skipped).")

    june_stop_losses = [s for s in june_sells if "stop_loss" in s.exit_reason]
    may_stop_losses = [s for s in may_sells if "stop_loss" in s.exit_reason]
    june_overshoot_rate = (len(overshoot_june) / len(june_stop_losses) * 100.0) if june_stop_losses else 0.0
    may_overshoot_rate = (len(overshoot_may) / len(may_stop_losses) * 100.0) if may_stop_losses else 0.0

    exec_checks = [
        ("duplicate_sells", len(dupes) == 0, f"{len(dupes)}"),
        ("daily_log_mismatch", len(daily_mismatch) == 0, f"{len(daily_mismatch)}"),
        ("run_tx_mismatch", len(run_vs_tx) == 0, f"{len(run_vs_tx)}"),
        (
            "overshoot_rate_not_worse_than_may",
            june_overshoot_rate <= may_overshoot_rate if may_stop_losses else True,
            f"June {june_overshoot_rate:.2f}% vs May {may_overshoot_rate:.2f}%",
        ),
    ]
    exec_pass = all(ok for _, ok, _ in exec_checks)

    broker_gate = "PENDING"
    if args.broker_csv:
        broker_gate = "PASS" if len(phantom_lines) == 0 else "FAIL"

    strategy_gate = "PENDING"
    if int(june["n"]) >= args.min_june_sells:
        strategy_pass = june["wr"] >= args.min_june_winrate and june["avg_pct"] >= args.min_june_avg_pct
        strategy_gate = "PASS" if strategy_pass else "FAIL"

    out: list[str] = []
    out.append("# June Daily Audit")
    out.append("")
    out.append(f"Generated: {datetime.now(UTC).strftime('%Y-%m-%d %H:%M UTC')}")
    out.append("")
    out.append("## Performance Snapshot")
    out.append("")
    out.append("| Window | Sells | Win Rate | P&L$ | Avg P&L% |")
    out.append("|---|---:|---:|---:|---:|")
    out.append(f"| 2026-06 (to date) | {int(june['n'])} | {june['wr']:.2f}% | ${june['pnl']:+.2f} | {_format_pct(june['avg_pct'])} |")
    out.append(f"| 2026-05 baseline | {int(may['n'])} | {may['wr']:.2f}% | ${may['pnl']:+.2f} | {_format_pct(may['avg_pct'])} |")
    out.append("")
    out.append("## Execution Quality Checks")
    out.append("")
    out.append(f"- Stop-loss overshoots (<= -3.0%) in June: **{len(overshoot_june)}** ({june_overshoot_rate:.2f}% of June stop-loss sells)")
    out.append(f"- Stop-loss overshoots (<= -3.0%) in May baseline: **{len(overshoot_may)}** ({may_overshoot_rate:.2f}% of May stop-loss sells)")
    out.append(f"- Duplicate same-day sells in June: **{len(dupes)}**")
    out.append(f"- Daily markdown mismatches (\"No trades today\" but tx rows exist): **{len(daily_mismatch)}**")
    out.append(f"- Run/tx exit-count mismatches in June dates: **{len(run_vs_tx)}**")
    out.append("")
    if dupes:
        out.append("### Duplicate Sell Rows")
        out.append("")
        for d, t, c in dupes:
            out.append(f"- {d} {t}: {c} sell rows")
        out.append("")
    if daily_mismatch:
        out.append("### Daily Log Mismatches")
        out.append("")
        for line in daily_mismatch:
            out.append(f"- {line}")
        out.append("")
    if run_vs_tx:
        out.append("### runs.csv vs transactions.csv Exit Mismatches (June)")
        out.append("")
        for d, tx_n, run_n in run_vs_tx:
            out.append(f"- {d}: tx sells={tx_n}, runs exits sum={run_n}")
        out.append("")
    out.append("## Broker Fill Reconciliation")
    out.append("")
    if args.broker_csv and broker_gate == "PASS":
        out.append("- PASS: every June tx sell matched a broker sell key (date+ticker).")
    else:
        for line in phantom_lines:
            out.append(f"- {line}")
    out.append("")
    out.append("## Go/No-Go Snapshot")
    out.append("")
    out.append(f"- Execution gate: **{'PASS' if exec_pass else 'FAIL'}**")
    out.append(f"- Broker reconciliation gate: **{broker_gate}**")
    out.append(f"- Strategy gate: **{strategy_gate}**")
    out.append("")
    out.append("### Gate Rules")
    out.append("")
    out.append("- Execution gate PASS requires: duplicate sells=0, daily-log mismatch=0, run-vs-tx mismatch=0, and June overshoot rate <= May rate.")
    out.append("- Broker gate PASS requires broker CSV provided and no unmatched June sell rows.")
    out.append(
        f"- Strategy gate PASS requires June sells >= {args.min_june_sells}, win rate >= {args.min_june_winrate:.1f}%, "
        f"and avg pnl per sell >= {args.min_june_avg_pct:+.2f}%."
    )
    out.append("")
    out.append("### Execution Gate Check Detail")
    out.append("")
    for name, ok, detail in exec_checks:
        out.append(f"- {name}: {'PASS' if ok else 'FAIL'} ({detail})")
    out.append("")

    out_file.write_text("\n".join(out), encoding="utf-8")
    print(f"Wrote {out_file}")
    print(f"June sells={int(june['n'])} pnl={june['pnl']:+.2f} wr={june['wr']:.2f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
