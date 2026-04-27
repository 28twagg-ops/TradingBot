#!/usr/bin/env python3
"""
generate_dashboard.py
---------------------
Reads rubber_band_bot log files and writes a single dashboard.md
with a full performance summary — no need to dig through multiple logs.

Usage:
    python generate_dashboard.py              # reads live logs/ folder
    python generate_dashboard.py paper        # reads paper_logs/ folder
    python generate_dashboard.py logs         # explicit live logs
"""

import sys
import csv
import json
from pathlib import Path
from datetime import datetime, date
from collections import defaultdict

# ── Config ────────────────────────────────────────────────────────────────────
STARTING_EQUITY = 500.0   # adjust if you funded with a different amount

# Pick log folder: live = logs/, paper = paper_logs/
arg = sys.argv[1].lower() if len(sys.argv) > 1 else "auto"
if arg == "paper":
    LOG_DIR = Path("paper_logs")
elif arg in ("logs", "live"):
    LOG_DIR = Path("logs")
else:
    # auto: prefer live logs if they have data, else paper_logs
    live_tx = Path("logs/transactions.csv")
    paper_tx = Path("paper_logs/transactions.csv")
    if live_tx.exists() and live_tx.stat().st_size > 100:
        LOG_DIR = Path("logs")
    elif paper_tx.exists() and paper_tx.stat().st_size > 100:
        LOG_DIR = Path("paper_logs")
    else:
        LOG_DIR = Path("logs")

TX_FILE   = LOG_DIR / "transactions.csv"
RUNS_FILE = LOG_DIR / "runs.csv"
OUT_FILE  = LOG_DIR / "dashboard.md"

print(f"Reading from: {LOG_DIR}/")

# ── Load transactions ──────────────────────────────────────────────────────────
trades = []
if TX_FILE.exists():
    with open(TX_FILE) as f:
        for row in csv.DictReader(f):
            row["pnl_pct"]    = float(row.get("pnl_pct", 0) or 0)
            row["pnl_dollar"] = float(row.get("pnl_dollar", 0) or 0)
            row["dollar_amount"] = float(row.get("dollar_amount", 0) or 0)
            row["hold_days"]  = int(row.get("hold_days", 0) or 0)
            trades.append(row)

buys  = [t for t in trades if t["action"] == "BUY"]
sells = [t for t in trades if t["action"] == "SELL"]

# ── Load runs ─────────────────────────────────────────────────────────────────
runs = []
if RUNS_FILE.exists():
    with open(RUNS_FILE) as f:
        for row in csv.DictReader(f):
            row["equity"] = float(row.get("equity", 0) or 0)
            row["cash"]   = float(row.get("cash", 0) or 0)
            runs.append(row)

# ── Equity stats from runs ─────────────────────────────────────────────────────
equity_series = [r["equity"] for r in runs if r["equity"] > 0]
current_equity = equity_series[-1] if equity_series else STARTING_EQUITY
peak_equity    = max(equity_series) if equity_series else STARTING_EQUITY
trough_equity  = min(equity_series) if equity_series else STARTING_EQUITY

total_return_pct  = (current_equity - STARTING_EQUITY) / STARTING_EQUITY * 100
max_drawdown_pct  = (trough_equity - peak_equity) / peak_equity * 100 if peak_equity > 0 else 0

# Current cash / positions from last run
last_run = runs[-1] if runs else {}
current_cash = last_run.get("cash", 0)
open_positions = last_run.get("open_positions", "0")
open_tickers   = last_run.get("tickers", "")
last_run_time  = last_run.get("timestamp", "N/A")

# ── Closed trade stats ─────────────────────────────────────────────────────────
wins   = [s for s in sells if s["pnl_pct"] > 0]
losses = [s for s in sells if s["pnl_pct"] <= 0]
total_closed = len(sells)

win_rate   = len(wins) / total_closed * 100 if total_closed > 0 else 0
avg_win    = sum(s["pnl_pct"] for s in wins)   / len(wins)   if wins   else 0
avg_loss   = sum(s["pnl_pct"] for s in losses) / len(losses) if losses else 0
avg_hold   = sum(s["hold_days"] for s in sells) / total_closed if total_closed > 0 else 0
total_pnl  = sum(s["pnl_dollar"] for s in sells)

gross_win  = sum(s["pnl_dollar"] for s in wins)   if wins   else 0
gross_loss = abs(sum(s["pnl_dollar"] for s in losses)) if losses else 1e-9
profit_factor = gross_win / gross_loss if gross_loss > 0 else float("inf")

# ── Breakdown by exit reason ───────────────────────────────────────────────────
by_exit = defaultdict(list)
for s in sells:
    reason = s.get("exit_reason", "unknown") or "unknown"
    # normalize: strip trailing detail in parens for grouping
    key = reason.split("(")[0].strip().split(" ")[0]
    by_exit[key].append(s)

# ── Breakdown by strategy (from buys) ─────────────────────────────────────────
# Match buys to sells by ticker and approximate date
strategy_map = {}  # ticker -> strategy (from most recent buy)
for b in buys:
    strategy_map[b["ticker"]] = b.get("strategy", "unknown")

by_strategy = defaultdict(list)
for s in sells:
    strat = strategy_map.get(s["ticker"], s.get("strategy", "unknown")) or "unknown"
    by_strategy[strat].append(s)

# ── Recent trades (last 20) ────────────────────────────────────────────────────
recent_sells = sells[-20:][::-1]  # newest first

# ── Equity curve (weekly snapshots) ───────────────────────────────────────────
# Sample equity at end of each day from runs
daily_equity = {}
for r in runs:
    ts = r.get("timestamp", "")[:10]
    if ts:
        daily_equity[ts] = r["equity"]

equity_dates = sorted(daily_equity.keys())

# ── Build dashboard ────────────────────────────────────────────────────────────
now_str = datetime.now().strftime("%Y-%m-%d %H:%M")

lines = []
lines.append(f"# 📊 Rubber Band Bot — Performance Dashboard")
lines.append(f"*Generated: {now_str}  |  Log source: `{LOG_DIR}/`*\n")

# ── Account Snapshot ──
lines.append("## Account Snapshot")
lines.append(f"| | |")
lines.append(f"|---|---|")
lines.append(f"| **Current Equity** | ${current_equity:.2f} |")
lines.append(f"| **Starting Equity** | ${STARTING_EQUITY:.2f} |")
lines.append(f"| **Total Return** | {total_return_pct:+.2f}% (${current_equity - STARTING_EQUITY:+.2f}) |")
lines.append(f"| **Peak Equity** | ${peak_equity:.2f} |")
lines.append(f"| **Max Drawdown** | {max_drawdown_pct:.2f}% |")
lines.append(f"| **Current Cash** | ${current_cash:.2f} |")
lines.append(f"| **Open Positions** | {open_positions} ({open_tickers}) |")
lines.append(f"| **Last Bot Run** | {last_run_time} |")
lines.append("")

# ── Trade Performance ──
lines.append("## Trade Performance (Closed Trades)")
lines.append(f"| Metric | Value |")
lines.append(f"|---|---|")
lines.append(f"| **Total Closed Trades** | {total_closed} |")
lines.append(f"| **Wins / Losses** | {len(wins)} / {len(losses)} |")
lines.append(f"| **Win Rate** | {win_rate:.1f}% |")
lines.append(f"| **Avg Win** | +{avg_win:.2f}% |")
lines.append(f"| **Avg Loss** | {avg_loss:.2f}% |")
lines.append(f"| **Profit Factor** | {profit_factor:.2f}x |")
lines.append(f"| **Avg Hold Days** | {avg_hold:.1f}d |")
lines.append(f"| **Total P&L** | ${total_pnl:+.2f} |")
lines.append("")

# ── Exit reason breakdown ──
if by_exit:
    lines.append("## Exit Reasons")
    lines.append(f"| Exit Type | Trades | Win Rate | Avg P&L% |")
    lines.append(f"|---|---|---|---|")
    for reason, group in sorted(by_exit.items(), key=lambda x: -len(x[1])):
        g_wins = [s for s in group if s["pnl_pct"] > 0]
        g_wr   = len(g_wins) / len(group) * 100 if group else 0
        g_avg  = sum(s["pnl_pct"] for s in group) / len(group) if group else 0
        lines.append(f"| `{reason}` | {len(group)} | {g_wr:.0f}% | {g_avg:+.2f}% |")
    lines.append("")

# ── Strategy breakdown ──
if total_closed > 0 and by_strategy:
    lines.append("## Strategy Breakdown")
    lines.append(f"| Strategy | Trades | Win Rate | Avg P&L% |")
    lines.append(f"|---|---|---|---|")
    for strat, group in sorted(by_strategy.items(), key=lambda x: -len(x[1])):
        g_wins = [s for s in group if s["pnl_pct"] > 0]
        g_wr   = len(g_wins) / len(group) * 100 if group else 0
        g_avg  = sum(s["pnl_pct"] for s in group) / len(group) if group else 0
        lines.append(f"| `{strat}` | {len(group)} | {g_wr:.0f}% | {g_avg:+.2f}% |")
    lines.append("")

# ── Equity timeline (simple text) ──
if len(equity_dates) > 1:
    lines.append("## Equity Timeline")
    lines.append(f"| Date | Equity | Change |")
    lines.append(f"|---|---|---|")
    prev = STARTING_EQUITY
    for d in equity_dates[::max(1, len(equity_dates)//30)]:  # max ~30 rows
        eq  = daily_equity[d]
        chg = eq - prev
        lines.append(f"| {d} | ${eq:.2f} | {chg:+.2f} |")
        prev = eq
    # Always include last date
    last_d = equity_dates[-1]
    if last_d not in equity_dates[::max(1, len(equity_dates)//30)]:
        eq  = daily_equity[last_d]
        chg = eq - prev
        lines.append(f"| {last_d} | ${eq:.2f} | {chg:+.2f} |")
    lines.append("")

# ── Recent trade history ──
if recent_sells:
    lines.append("## Recent Closed Trades (newest first)")
    lines.append(f"| Date | Ticker | Strategy | P&L% | P&L$ | Hold | Exit Reason |")
    lines.append(f"|---|---|---|---|---|---|---|")
    for s in recent_sells:
        pnl_pct  = s["pnl_pct"]
        pnl_str  = f"{pnl_pct:+.2f}%"
        dollar   = f"${s['pnl_dollar']:+.2f}"
        strat    = strategy_map.get(s["ticker"], s.get("strategy", "?")) or "?"
        reason   = s.get("exit_reason", "") or ""
        lines.append(
            f"| {s['date']} | **{s['ticker']}** | `{strat}` | {pnl_str} | {dollar} | {s['hold_days']}d | {reason} |"
        )
    lines.append("")

# ── All-time trade log ──
if len(sells) > 20:
    lines.append("<details>")
    lines.append("<summary>Full trade history (all closed trades)</summary>\n")
    lines.append(f"| Date | Ticker | P&L% | P&L$ | Hold | Exit Reason |")
    lines.append(f"|---|---|---|---|---|---|")
    for s in sells[::-1]:
        pnl_pct = s["pnl_pct"]
        lines.append(
            f"| {s['date']} | {s['ticker']} | {pnl_pct:+.2f}% | ${s['pnl_dollar']:+.2f} | {s['hold_days']}d | {s.get('exit_reason','')} |"
        )
    lines.append("</details>\n")

# ── Footer ──
lines.append("---")
lines.append(f"*Auto-generated by `generate_dashboard.py` — run after `git pull` to refresh.*")

# ── Write file ────────────────────────────────────────────────────────────────
OUT_FILE.write_text("\n".join(lines))
print(f"✅ Dashboard written to: {OUT_FILE}")
print(f"   Closed trades: {total_closed}  |  Win rate: {win_rate:.1f}%  |  Equity: ${current_equity:.2f}")
