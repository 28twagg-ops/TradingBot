#!/usr/bin/env python3
"""
generate_paper_summary.py
=========================
Reads paper bot logs and writes a rich Markdown summary to stdout
(pipe to $GITHUB_STEP_SUMMARY in GitHub Actions).

Usage:
    python generate_paper_summary.py >> $GITHUB_STEP_SUMMARY
"""

import csv, json, sys, os
from pathlib import Path
from datetime import datetime, date, timedelta
from collections import defaultdict

LOG_DIR   = Path("logs/paper")
TX_FILE   = LOG_DIR / "transactions.csv"
RUNS_FILE = LOG_DIR / "runs.csv"

STARTING_EQUITY = 100_000.0

def read_csv(path):
    if not path.exists(): return []
    with open(path, newline="") as f:
        return list(csv.DictReader(f))

def fmt_pct(v, digits=2):
    sign = "+" if v >= 0 else ""
    return f"{sign}{v:.{digits}f}%"

def fmt_dollar(v):
    sign = "+" if v >= 0 else ""
    return f"${sign}{v:,.2f}"

def pct_badge(v):
    if v > 5:   return f"🟢 **{fmt_pct(v)}**"
    if v > 0:   return f"🟡 **{fmt_pct(v)}**"
    return            f"🔴 **{fmt_pct(v)}**"

def trend_arrow(series):
    if len(series) < 2: return "→"
    delta = series[-1] - series[-2]
    if delta > 50: return "⬆️"
    if delta > 0:  return "↗️"
    if delta < -50:return "⬇️"
    return "↘️"

# ─── Load data ────────────────────────────────────────────────────────────────
trades = read_csv(TX_FILE)
runs   = read_csv(RUNS_FILE)

for t in trades:
    t["pnl_pct"]    = float(t.get("pnl_pct", 0) or 0)
    t["pnl_dollar"] = float(t.get("pnl_dollar", 0) or 0)
    t["hold_days"]  = int(t.get("hold_days", 0) or 0)
for r in runs:
    r["equity"] = float(r.get("equity", 0) or 0)
    r["cash"]   = float(r.get("cash", 0) or 0)

buys_tx  = [t for t in trades if t["action"] == "BUY"]
sells_tx = [t for t in trades if t["action"] == "SELL"]

eq_series      = [r["equity"] for r in runs if r["equity"] > 0]
current_equity = eq_series[-1] if eq_series else STARTING_EQUITY
peak_equity    = max(eq_series) if eq_series else STARTING_EQUITY
total_ret_pct  = (current_equity - STARTING_EQUITY) / STARTING_EQUITY * 100
total_ret_dol  = current_equity - STARTING_EQUITY
max_dd_pct     = 0.0
running_peak   = STARTING_EQUITY
for eq in eq_series:
    if eq > running_peak: running_peak = eq
    dd = (running_peak - eq) / running_peak * 100
    if dd > max_dd_pct: max_dd_pct = dd

last_run      = runs[-1] if runs else {}
current_cash  = float(last_run.get("cash", 0) or 0)
open_pos_cnt  = last_run.get("open_positions", "0")
open_tickers  = (last_run.get("tickers", "") or "").replace("|", ", ")
last_run_time = last_run.get("timestamp", "N/A")
last_mode     = last_run.get("mode", "?")
last_regime   = (last_run.get("regime", "?") or "?").upper()

wins   = [s for s in sells_tx if s["pnl_pct"] > 0]
losses = [s for s in sells_tx if s["pnl_pct"] <= 0]
total_closed = len(sells_tx)
win_rate     = len(wins) / total_closed * 100 if total_closed else 0
avg_win      = sum(s["pnl_pct"] for s in wins)   / len(wins)   if wins   else 0
avg_loss     = sum(s["pnl_pct"] for s in losses) / len(losses) if losses else 0
avg_hold     = sum(s["hold_days"] for s in sells_tx) / total_closed if total_closed else 0
total_pnl    = sum(s["pnl_dollar"] for s in sells_tx)
gross_win    = sum(s["pnl_dollar"] for s in wins)
gross_loss   = abs(sum(s["pnl_dollar"] for s in losses)) or 1e-9
profit_factor = gross_win / gross_loss

# strat lookup
strat_map = {b["ticker"]: b.get("strategy","?") for b in buys_tx}

# by strategy
by_strat = defaultdict(list)
for s in sells_tx:
    st = strat_map.get(s["ticker"], s.get("strategy","?")) or "?"
    by_strat[st].append(s)

# equity sparkline (last 20 data points → ASCII)
def sparkline(data, width=20):
    if not data: return ""
    data = data[-width:]
    lo, hi = min(data), max(data)
    rng = hi - lo or 1
    chars = "▁▂▃▄▅▆▇█"
    return "".join(chars[min(7, int((v - lo) / rng * 7.999))] for v in data)

spark = sparkline(eq_series)

# Today's trades
today_str = str(date.today())
today_buys  = [t for t in buys_tx  if t.get("date","") == today_str]
today_sells = [t for t in sells_tx if t.get("date","") == today_str]

# This week's trades
week_start = (date.today() - timedelta(days=date.today().weekday())).isoformat()
week_sells = [s for s in sells_tx if s.get("date","") >= week_start]

# ─── Build summary ────────────────────────────────────────────────────────────
run_time_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
mode_label   = "📋 EXITS CHECK" if last_mode == "exits" else "🔍 DAILY SCAN" if last_mode == "scan" else "📊 SUMMARY"
regime_icon  = {"BULL": "🐂", "BEAR": "🐻", "CORRECTION": "⚠️"}.get(last_regime, "❓")

L = []
L.append(f"# 🤖 Paper Bot Run — {run_time_utc}")
L.append(f"> **Mode:** {mode_label} &nbsp;·&nbsp; **Regime:** {regime_icon} {last_regime} &nbsp;·&nbsp; **Last Run:** {last_run_time}")
L.append("")

# ── Account snapshot ──────────────────────────────────────────────────────────
arrow = trend_arrow(eq_series)
ret_badge = pct_badge(total_ret_pct)

L.append("## 💰 Account Snapshot")
L.append("")
L.append(f"| Metric | Value | |")
L.append(f"|--------|-------|---|")
L.append(f"| **Current Equity** | **${current_equity:,.2f}** | {arrow} |")
L.append(f"| **Total Return** | {ret_badge} ({fmt_dollar(total_ret_dol)}) | vs ${STARTING_EQUITY:,.0f} start |")
L.append(f"| **Max Drawdown** | {'🔴' if max_dd_pct > 5 else '🟡' if max_dd_pct > 2 else '🟢'} {max_dd_pct:.2f}% | all-time |")
L.append(f"| **Cash Available** | ${current_cash:,.2f} | |")
L.append(f"| **Open Positions** | {open_pos_cnt} | {open_tickers or '—'} |")
L.append("")

if spark:
    L.append(f"**Equity trend (recent):** `{spark}`")
    L.append("")

# ── Trade stats ───────────────────────────────────────────────────────────────
L.append("## 📈 Trade Performance")
L.append("")
if total_closed > 0:
    wr_icon   = "🟢" if win_rate >= 50 else "🟡" if win_rate >= 40 else "🔴"
    pf_icon   = "🟢" if profit_factor >= 1.5 else "🟡" if profit_factor >= 1.0 else "🔴"
    ev        = (win_rate/100 * avg_win + (1-win_rate/100) * avg_loss)
    ev_icon   = "🟢" if ev > 0 else "🔴"
    L.append(f"| Metric | Value | Signal |")
    L.append(f"|--------|-------|--------|")
    L.append(f"| **Closed Trades** | {total_closed} | — |")
    L.append(f"| **Win Rate** | {win_rate:.1f}% | {wr_icon} |")
    L.append(f"| **Avg Win** | +{avg_win:.2f}% | — |")
    L.append(f"| **Avg Loss** | {avg_loss:.2f}% | — |")
    L.append(f"| **Profit Factor** | {profit_factor:.2f}× | {pf_icon} |")
    L.append(f"| **EV / Trade** | {fmt_pct(ev)} | {ev_icon} |")
    L.append(f"| **Avg Hold Days** | {avg_hold:.1f}d | — |")
    L.append(f"| **Total Realised P&L** | {fmt_dollar(total_pnl)} | — |")
else:
    L.append("*No closed trades yet.*")
L.append("")

# ── Today's activity ──────────────────────────────────────────────────────────
L.append("## 📅 Today's Activity")
L.append("")
if today_buys or today_sells:
    if today_buys:
        L.append(f"**Entries ({len(today_buys)}):**")
        L.append("")
        L.append("| # | Ticker | Strategy | Size |")
        L.append("|---|--------|----------|------|")
        for i, b in enumerate(today_buys, 1):
            L.append(f"| {i} | **{b['ticker']}** | `{b.get('strategy','?')}` | ${float(b.get('dollar_amount',0)):,.2f} |")
        L.append("")
    if today_sells:
        L.append(f"**Exits ({len(today_sells)}):**")
        L.append("")
        L.append("| # | Ticker | Strategy | P&L% | P&L$ | Reason |")
        L.append("|---|--------|----------|------|------|--------|")
        for i, s in enumerate(today_sells, 1):
            icon = "✅" if s["pnl_pct"] > 0 else "🛑"
            st = strat_map.get(s["ticker"], s.get("strategy","?")) or "?"
            L.append(f"| {i} {icon} | **{s['ticker']}** | `{st}` "
                     f"| {fmt_pct(s['pnl_pct'])} | {fmt_dollar(s['pnl_dollar'])} "
                     f"| {s.get('exit_reason','').split('(')[0].strip()[:22]} |")
        L.append("")
else:
    L.append("*No trades today.*")
    L.append("")

# ── This week ─────────────────────────────────────────────────────────────────
if week_sells:
    week_pnl = sum(s["pnl_dollar"] for s in week_sells)
    week_wr  = sum(1 for s in week_sells if s["pnl_pct"] > 0) / len(week_sells) * 100
    L.append(f"**This week:** {len(week_sells)} closed  ·  WR {week_wr:.0f}%  ·  P&L {fmt_dollar(week_pnl)}")
    L.append("")

# ── By strategy ───────────────────────────────────────────────────────────────
if by_strat:
    L.append("## 🎯 Strategy Breakdown (All Time)")
    L.append("")
    L.append("| Strategy | Trades | Win Rate | Avg P&L% | Total P&L$ |")
    L.append("|----------|--------|----------|----------|------------|")
    rows = []
    for st, grp in by_strat.items():
        g_wins = [s for s in grp if s["pnl_pct"] > 0]
        g_wr   = len(g_wins) / len(grp) * 100 if grp else 0
        g_avg  = sum(s["pnl_pct"] for s in grp) / len(grp)
        g_pnl  = sum(s["pnl_dollar"] for s in grp)
        rows.append((st, len(grp), g_wr, g_avg, g_pnl))
    rows.sort(key=lambda x: x[4], reverse=True)
    for st, n, wr, avg, pnl in rows:
        wr_icon = "🟢" if wr >= 50 else "🟡" if wr >= 40 else "🔴"
        L.append(f"| `{st}` | {n} | {wr_icon} {wr:.0f}% | {fmt_pct(avg)} | {fmt_dollar(pnl)} |")
    L.append("")

# ── Recent closed trades ──────────────────────────────────────────────────────
recent = sells_tx[-15:][::-1]
if recent:
    L.append("## 🔄 Recent Closed Trades (last 15)")
    L.append("")
    L.append("| Date | Ticker | P&L% | P&L$ | Hold | Exit |")
    L.append("|------|--------|------|------|------|------|")
    for s in recent:
        icon = "✅" if s["pnl_pct"] > 0 else "🛑"
        reason = (s.get("exit_reason","") or "").split("(")[0].strip()[:18]
        L.append(f"| {s['date']} | {icon} **{s['ticker']}** "
                 f"| {fmt_pct(s['pnl_pct'])} | {fmt_dollar(s['pnl_dollar'])} "
                 f"| {s['hold_days']}d | {reason} |")
    L.append("")

# ── Configuration ─────────────────────────────────────────────────────────────
L.append("## ⚙️ Bot Configuration")
L.append("")
L.append("| Setting | Value |")
L.append("|---------|-------|")
L.append("| Mode | 📋 PAPER TRADING (no real money) |")
L.append("| Universe | SP500 + MidCap (~900 stocks) |")
L.append("| Stop Loss | -0.5% (GTC stop-market) |")
L.append("| Max Hold | 3 days |")
L.append("| Seasonal Size | 20% of equity |")
L.append("| Off-Schedule Size | 12% of equity |")
L.append("| Extended-Hours Sells | ✅ Enabled (4pm DAY limit) |")
L.append("| Entry Time | 3:50pm close price |")
L.append("")

L.append("---")
L.append(f"*Auto-generated at {run_time_utc}. Paper account — no real money at risk.*")

print("\n".join(L))
