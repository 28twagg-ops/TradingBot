"""
generate_dashboard.py — Build a self-contained HTML ops dashboard.

Reads committed logs and embeds data as JS constants into logs/dashboard.html.
Always exits 0 (non-fatal for GHA).

Usage:
  python scripts/generate_dashboard.py
"""
from __future__ import annotations

import csv
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

REPO = Path(__file__).resolve().parent.parent
TRIAL = REPO / "logs" / "options_trial"
OUT = REPO / "logs" / "dashboard.html"
ET = ZoneInfo("America/New_York")
START_EQUITY = 480.0
STRATS = [
    "S163", "S164", "S165", "S166", "S167", "S168",
    "S169", "S170", "S171", "S172", "S175",
    "S173", "S174",
]
KNOWN_RB_STRATEGIES = [
    "Pullback50", "MomReversal", "RSIRecovery", "52wkLow", "RubberBand",
    "MA_Squeeze", "GoldenPocket", "VWAP_Reclaim", "TrendResumption", "EarningsDrift",
]


def _f(v, d=0.0) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return d


def _read_runs_equity(days: int = 30) -> dict:
    path = REPO / "logs" / "runs.csv"
    points = []
    last_run = None
    open_pos = 0
    if path.exists():
        with path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                ts = row.get("timestamp") or ""
                eq = _f(row.get("equity"))
                if not ts or eq <= 0:
                    continue
                points.append({"t": ts[:16], "e": round(eq, 2)})
                last_run = ts
                open_pos = int(_f(row.get("open_positions"), 0))
    # Dedup to last point per calendar day, then last N days
    by_day: dict[str, dict] = {}
    for p in points:
        by_day[p["t"][:10]] = p
    days_sorted = sorted(by_day.keys())[-days:]
    series = [by_day[d] for d in days_sorted]
    equity = series[-1]["e"] if series else START_EQUITY
    return {
        "series": series,
        "equity": equity,
        "start_equity": START_EQUITY,
        "return_pct": round(100.0 * (equity / START_EQUITY - 1.0), 2) if START_EQUITY else 0,
        "open_positions": open_pos,
        "last_run": last_run,
    }


def _rb_today_pnl() -> dict:
    path = REPO / "logs" / "transactions.csv"
    today = datetime.now(ET).date().isoformat()
    realized = 0.0
    n = 0
    if path.exists():
        with path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                if (row.get("date") or "")[:10] != today:
                    continue
                if (row.get("action") or "").upper() != "SELL":
                    continue
                realized += _f(row.get("pnl_dollar"))
                n += 1
    return {"realized": round(realized, 2), "sells": n, "date": today}


def _latest_selection() -> dict:
    reports = sorted((TRIAL / "reports").glob("*_strategy_selection.csv"))
    if not reports:
        return {"rows": [], "path": None, "keep": 0, "watch": 0, "drop": 0}
    path = reports[-1]
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    keep = sum(1 for r in rows if r.get("recommendation") == "keep")
    watch = sum(1 for r in rows if r.get("recommendation") == "watch")
    drop = sum(1 for r in rows if r.get("recommendation") == "drop")
    return {"rows": rows, "path": path.name, "keep": keep, "watch": watch, "drop": drop}


def _parse_freq_md() -> dict:
    path = TRIAL / "reports" / "signal_frequency.md"
    matrix: dict[str, dict[str, int]] = {}
    if not path.exists():
        return {"matrix": {}, "strategies": STRATS}
    text = path.read_text(encoding="utf-8")
    # Find first markdown table after "Unique underlying"
    in_table = False
    headers: list[str] = []
    for line in text.splitlines():
        if "Unique underlying symbols per day" in line:
            in_table = True
            continue
        if not in_table:
            continue
        if line.startswith("| Date"):
            headers = [c.strip() for c in line.strip("|").split("|")]
            continue
        if line.startswith("|---") or line.startswith("| --"):
            continue
        if not line.startswith("|"):
            if headers:
                break
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2 or cells[0].startswith("_"):
            continue
        day = cells[0]
        matrix[day] = {}
        for i, h in enumerate(headers[1:], start=1):
            if h == "Total" or i >= len(cells):
                continue
            try:
                matrix[day][h] = int(cells[i])
            except ValueError:
                matrix[day][h] = 0
    # Prefer strategies present in headers, else STRATS
    strats = [h for h in headers[1:] if h != "Total"] if headers else STRATS
    # last 14 days
    days = sorted(matrix.keys())[-14:]
    return {"matrix": {d: matrix[d] for d in days}, "strategies": strats or STRATS}


def _ledger_health() -> dict:
    path = TRIAL / "reports" / "ledger_health.md"
    status = "OK"
    warns = 0
    open_lots = 0
    if path.exists():
        text = path.read_text(encoding="utf-8")
        for line in text.splitlines():
            if "| Current stuck" in line or "| Orphaned lots" in line or "| Missing exit" in line:
                if "WARN" in line:
                    warns += 1
                    status = "WARN"
            m = re.search(r"Total open lots\s*\|\s*(\d+)", line)
            if m:
                open_lots = int(m.group(1))
    return {"status": status, "warns": warns, "open_lots": open_lots}


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


def _median(vals: list[float]) -> float:
    if not vals:
        return 0.0
    s = sorted(vals)
    n = len(s)
    m = n // 2
    return s[m] if n % 2 else (s[m - 1] + s[m]) / 2


def _ledger_arm_stats() -> dict[str, dict]:
    """Per-strategy exit stats from master_ledger.csv."""
    path = TRIAL / "_ledger" / "master_ledger.csv"
    out: dict[str, dict] = {}
    if not path.exists():
        return out
    by: dict[str, list[float]] = {}
    first_entry: dict[str, str] = {}
    with path.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            sid = r.get("strategy_id") or ""
            if not sid:
                continue
            ts = str(r.get("ts") or "")[:10]
            if r.get("event") == "entry" and ts:
                if sid not in first_entry or ts < first_entry[sid]:
                    first_entry[sid] = ts
            if r.get("event") != "exit":
                continue
            ret = _f(r.get("return_pct"), None)
            if ret is None:
                continue
            by.setdefault(sid, []).append(ret)
    for sid, rets in by.items():
        n = len(rets)
        rec = "INSUFFICIENT" if n < 5 else ("keep" if _median(rets) > 0 and n >= 30 else "watch")
        if n >= 20 and _median(rets) <= 0:
            rec = "drop"
        out[sid] = {
            "exits": n,
            "med": round(_median(rets), 2) if n >= 5 else None,
            "p10": round(_percentile(rets, 0.10), 2) if n >= 5 else None,
            "status": rec,
            "first_entry": first_entry.get(sid),
        }
    for sid, day in first_entry.items():
        out.setdefault(sid, {"exits": 0, "med": None, "p10": None, "status": "INSUFFICIENT"})
        out[sid]["first_entry"] = day
    return out


def _router_detail() -> dict:
    """CONFIRMED if any S163/S164/S166/S167/S168 ENTRY ever logged."""
    runs = TRIAL / "runs"
    pat = re.compile(
        r"ENTRY\s*\[[^\]]*\|(S163|S164|S166|S167|S168)\]",
        re.I,
    )
    first_date = None
    confirmed = False
    if runs.exists():
        for p in sorted(runs.glob("*.log")):
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            m = pat.search(text)
            if m:
                confirmed = True
                # Prefer date from filename YYYY-MM-DD.log
                day = p.stem if re.match(r"\d{4}-\d{2}-\d{2}$", p.stem) else None
                if day and (first_date is None or day < first_date):
                    first_date = day
    return {
        "status": "CONFIRMED" if confirmed else "PENDING",
        "first_entry_date": first_date or "PENDING",
        "confirmed": confirmed,
    }


def _experiment_progress(selection_rows: list[dict], ledger: dict[str, dict]) -> dict:
    by_sel = {r.get("strategy_id"): r for r in selection_rows}

    def arm(sid: str, label: str, extra: str = "") -> dict:
        L = ledger.get(sid) or {}
        S = by_sel.get(sid) or {}
        exits = int(L.get("exits") or _f(S.get("exits"), 0))
        med = L.get("med")
        p10 = L.get("p10")
        if med is None and exits >= 5:
            med = _f(S.get("med_return_pct"), None)
        if p10 is None and exits >= 5:
            p10 = _f(S.get("p10_return_pct"), None)
        status = L.get("status") or S.get("recommendation") or "INSUFFICIENT"
        if exits < 5:
            status = "INSUFFICIENT"
            med = None
            p10 = None
        return {
            "id": sid,
            "label": label,
            "extra": extra,
            "exits": exits,
            "target": 30,
            "pct": min(100, round(100.0 * exits / 30.0, 1)),
            "med": med,
            "p10": p10,
            "status": status,
        }

    p2b_arms = [
        arm("S164", "1-DTE", "1 day"),
        arm("S165", "3-DTE", "3 days"),
        arm("S168", "5-DTE", "5 days"),
        arm("S163", "7-DTE", "7 days"),
    ]
    p2c_arms = [
        arm("S165", "ATM ctrl", "ATM"),
        arm("S167", "1-OTM", "+1 strike"),
    ]

    def best_note(arms: list[dict]) -> str:
        ready = [a for a in arms if a["exits"] >= 30 and a["med"] is not None]
        if not ready:
            return "Insufficient data (need n≥30 per arm)"
        best = max(ready, key=lambda a: a["med"])
        return f"Best arm after n≥30: {best['id']} at {best['med']:+.1f}%"

    return {
        "p2b": {
            "title": "Experiment P2B — DTE Sensitivity (GapDown signal)",
            "subtitle": "Does holding period matter for gap-recovery options?",
            "arms": p2b_arms,
            "progress": best_note(p2b_arms),
            "note": "Decision threshold: n≥30 per arm. Early kill: p10<-80% at n≥15.",
        },
        "p2c": {
            "title": "Experiment P2C — Strike Sensitivity (GapDown signal)",
            "subtitle": "Does buying OTM vs ATM improve risk-adjusted returns?",
            "arms": p2c_arms,
            "progress": best_note(p2c_arms),
            "note": "Decision threshold: n≥30 per arm. Early kill: p10<-80% at n≥15.",
        },
    }


def _rb_leaderboard() -> list[dict]:
    path = REPO / "logs" / "transactions.csv"
    disabled = {"GapDown", "VolumeSpike"}
    by: dict[str, list[float]] = {}
    by_d: dict[str, list[float]] = {}
    if path.exists():
        with path.open(encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                if (r.get("action") or "").upper() != "SELL":
                    continue
                strat = (r.get("strategy") or "unknown").strip() or "unknown"
                by.setdefault(strat, []).append(_f(r.get("pnl_pct")))
                by_d.setdefault(strat, []).append(_f(r.get("pnl_dollar")))
    active_rows = []
    disabled_rows = []
    for strat, pnls in by.items():
        dollars = by_d.get(strat, [])
        gw = sum(d for d in dollars if d > 0)
        gl = abs(sum(d for d in dollars if d < 0))
        pf = (gw / gl) if gl > 0 else (999.0 if gw > 0 else 0.0)
        row = {
            "strategy": strat,
            "n": len(pnls),
            "wr": round(100.0 * sum(1 for p in pnls if p > 0) / len(pnls), 1),
            "avg": round(sum(pnls) / len(pnls), 2),
            "med": round(_median(pnls), 2),
            "p10": round(_percentile(pnls, 0.10), 2),
            "pf": round(pf, 2),
            "total": round(sum(dollars), 2),
            "status": "WATCH" if len(pnls) < 30 else "ACTIVE",
        }
        if strat in disabled:
            row["note"] = "Disabled 2026-07-20"
            row["status"] = "DISABLED"
            disabled_rows.append(row)
        else:
            active_rows.append(row)
    # Ensure known active strategies appear even at n=0
    have = {r["strategy"] for r in active_rows}
    for name in KNOWN_RB_STRATEGIES:
        if name not in have and name not in disabled:
            active_rows.append({
                "strategy": name, "n": 0, "wr": 0.0, "avg": 0.0, "med": 0.0,
                "p10": 0.0, "pf": 0.0, "total": 0.0, "status": "NEW",
            })
    # Ensure disabled names appear even with no sells in window
    have_d = {r["strategy"] for r in disabled_rows}
    for name in sorted(disabled):
        if name not in have_d:
            disabled_rows.append({
                "strategy": name, "n": 0, "wr": 0.0, "avg": 0.0, "med": 0.0,
                "p10": 0.0, "pf": 0.0, "total": 0.0, "note": "Disabled 2026-07-20",
                "status": "DISABLED",
            })
    active_rows.sort(key=lambda x: (0 if x["n"] > 0 else 1, -x["pf"], -x["avg"], x["strategy"]))
    disabled_rows.sort(key=lambda x: x["strategy"])
    return active_rows, disabled_rows


def _stale(last_run: str | None, minutes: int = 20) -> bool:
    if not last_run:
        return True
    try:
        dt = datetime.strptime(last_run[:19], "%Y-%m-%d %H:%M:%S")
        # runs.csv timestamps are typically ET naive; treat as ET
        dt = dt.replace(tzinfo=ET)
        return (datetime.now(ET) - dt) > timedelta(minutes=minutes)
    except Exception:
        return True


def build_data() -> dict:
    rb = _read_runs_equity()
    today = _rb_today_pnl()
    sel = _latest_selection()
    freq = _parse_freq_md()
    health = _ledger_health()
    ledger = _ledger_arm_stats()
    router = _router_detail()
    rb_active, rb_disabled = _rb_leaderboard()
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    return {
        "generated_at": generated,
        "rubber_band": {
            **rb,
            "today_realized": today["realized"],
            "today_sells": today["sells"],
            "status": "STALE" if _stale(rb.get("last_run")) else "RUNNING",
            "leaderboard": rb_active,
            "disabled": rb_disabled,
        },
        "options": {
            "active_strategies": 11,
            "keep": sel["keep"],
            "watch": sel["watch"],
            "drop": sel["drop"],
            "orphan_rate": None,
            "open_lots": health["open_lots"],
            "selection_file": sel["path"],
            "leaderboard": sel["rows"],
        },
        "system": {
            "ledger_health": health["status"],
            "ledger_warns": health["warns"],
            "router": router["status"],
            "router_first_entry": router["first_entry_date"],
            "cron": "OK" if not _stale(rb.get("last_run"), 20) else "STALE",
            "last_run": rb.get("last_run"),
        },
        "frequency": freq,
        "experiments": _experiment_progress(sel["rows"], ledger),
        "router_card": router,
    }


def _orphan_from_selection_md() -> float | None:
    reports = sorted((TRIAL / "reports").glob("*_strategy_selection.md"))
    if not reports:
        return None
    text = reports[-1].read_text(encoding="utf-8")
    m = re.search(r"Orphan rate:\s*\*\*([0-9.]+)%", text)
    if m:
        return float(m.group(1))
    return None


def render_html(data: dict) -> str:
    payload = json.dumps(data, separators=(",", ":"))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>TradingBot Dashboard</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet"/>
<style>
:root {{
  --bg:#0d1117; --panel:#161b22; --border:#30363d; --text:#e6edf3; --muted:#8b949e;
  --green:#2ea043; --yellow:#d29922; --red:#da3633; --blue:#388bfd;
}}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--text); font-family:Inter,system-ui,sans-serif; }}
.wrap {{ max-width:1200px; margin:0 auto; padding:24px 16px 48px; }}
h1 {{ font-size:1.4rem; margin:0 0 4px; }}
.sub {{ color:var(--muted); font-size:0.85rem; margin-bottom:20px; }}
.grid3 {{ display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-bottom:20px; }}
@media (max-width:900px) {{ .grid3 {{ grid-template-columns:1fr; }} }}
.card {{ background:var(--panel); border:1px solid var(--border); border-radius:10px; padding:16px; }}
.card h2 {{ margin:0 0 10px; font-size:0.95rem; color:var(--muted); text-transform:uppercase; letter-spacing:.04em; }}
.metric {{ font-family:"JetBrains Mono",monospace; font-size:1.6rem; font-weight:600; }}
.row {{ display:flex; justify-content:space-between; gap:8px; margin:6px 0; font-size:0.9rem; }}
.muted {{ color:var(--muted); }}
.pill {{ display:inline-block; padding:2px 8px; border-radius:999px; font-size:0.75rem; font-weight:600; }}
.pill.ok {{ background:rgba(46,160,67,.2); color:var(--green); }}
.pill.warn {{ background:rgba(210,153,34,.2); color:var(--yellow); }}
.pill.bad {{ background:rgba(218,54,51,.2); color:var(--red); }}
.pill.info {{ background:rgba(56,139,253,.2); color:var(--blue); }}
section {{ margin-bottom:24px; }}
section > h3 {{ margin:0 0 10px; font-size:1.05rem; }}
table {{ width:100%; border-collapse:collapse; font-size:0.85rem; }}
th,td {{ padding:8px 10px; border-bottom:1px solid var(--border); text-align:left; }}
th {{ color:var(--muted); font-weight:600; }}
td.mono {{ font-family:"JetBrains Mono",monospace; }}
tr.keep td:first-child {{ box-shadow:inset 3px 0 0 var(--green); }}
tr.watch td:first-child {{ box-shadow:inset 3px 0 0 var(--yellow); }}
tr.drop td:first-child {{ box-shadow:inset 3px 0 0 var(--red); }}
tr.disabled {{ opacity:0.55; color:var(--muted); }}
tr.disabled td:first-child {{ box-shadow:inset 3px 0 0 var(--muted); }}
.heat {{ display:grid; gap:4px; overflow-x:auto; }}
.heat-row {{ display:grid; grid-template-columns:90px repeat(auto-fit,minmax(36px,1fr)); gap:4px; align-items:center; }}
.heat-cell {{ height:28px; border-radius:4px; background:#21262d; font-family:"JetBrains Mono",monospace; font-size:0.7rem;
  display:flex; align-items:center; justify-content:center; color:var(--text); }}
.bar {{ height:8px; background:#21262d; border-radius:4px; overflow:hidden; margin-top:4px; }}
.bar > i {{ display:block; height:100%; background:var(--blue); }}
.exp {{ display:grid; grid-template-columns:1fr 1fr; gap:12px; }}
@media (max-width:800px) {{ .exp {{ grid-template-columns:1fr; }} }}
svg.spark {{ width:100%; height:120px; background:var(--panel); border:1px solid var(--border); border-radius:10px; }}
</style>
</head>
<body>
<div class="wrap">
  <h1>TradingBot Ops Dashboard</h1>
  <div class="sub">Generated <span id="gen"></span> · data embedded from committed logs</div>
  <div class="grid3" id="statusCards"></div>
  <section>
    <h3>Rubber Band equity (last 30 days)</h3>
    <svg class="spark" id="spark" viewBox="0 0 1000 120" preserveAspectRatio="none"></svg>
    <div class="row muted" id="sparkLegend"></div>
  </section>
  <section>
    <h3>Options strategy leaderboard</h3>
    <div class="card" style="padding:0; overflow:auto"><table id="board"></table></div>
  </section>
  <section>
    <h3>Signal frequency (unique underlyings / day)</h3>
    <div class="card" id="heat"></div>
  </section>
  <section>
    <h3>Experiments</h3>
    <div class="exp" id="exps"></div>
    <div class="card" id="routerCard" style="margin-top:12px"></div>
  </section>
  <section>
    <h3>Rubber Band Strategy Leaderboard</h3>
    <div class="card" style="padding:0; overflow:auto"><table id="rbBoard"></table></div>
    <div class="muted" style="margin-top:8px;font-size:0.85rem">Equal weight since 2026-07-18 — schedule not enforced · GapDown + VolumeSpike disabled 2026-07-20</div>
    <div class="card" style="padding:0; overflow:auto; margin-top:12px"><table id="rbDisabled"></table></div>
  </section>
</div>
<script>
const DATA = {payload};
function pill(text, cls) {{ return `<span class="pill ${{cls}}">${{text}}</span>`; }}
function fmtMoney(x) {{
  const n = Number(x||0);
  const s = (n<0?'-':'') + '$' + Math.abs(n).toFixed(2);
  return s;
}}
function fmtPct(x) {{
  if (x==null || x===undefined) return '—';
  const n = Number(x);
  return (n>=0?'+':'') + n.toFixed(1) + '%';
}}
function statusCls(s) {{
  const t = (s||'').toLowerCase();
  if (t==='keep' || t==='confirmed') return 'ok';
  if (t==='drop' || t==='bad') return 'bad';
  return 'warn';
}}
function renderCards() {{
  const rb = DATA.rubber_band, op = DATA.options, sy = DATA.system;
  const rbPill = rb.status==='RUNNING' ? pill('RUNNING','ok') : pill('STALE','warn');
  const orphan = op.orphan_rate==null ? '—' : op.orphan_rate.toFixed(1)+'%';
  const orphanCls = (op.orphan_rate!=null && op.orphan_rate>10) ? 'bad' : 'ok';
  const ledgerCls = sy.ledger_health==='OK' ? 'ok' : 'warn';
  const routerCls = sy.router==='CONFIRMED' ? 'ok' : 'warn';
  document.getElementById('statusCards').innerHTML = `
    <div class="card"><h2>Rubber Band</h2>
      <div class="metric">${{fmtMoney(rb.equity)}}</div>
      <div class="row"><span class="muted">Today realized</span><span class="mono">${{fmtMoney(rb.today_realized)}}</span></div>
      <div class="row"><span class="muted">Open positions</span><span class="mono">${{rb.open_positions}}</span></div>
      <div class="row"><span class="muted">Last run</span><span class="mono">${{rb.last_run||'—'}}</span></div>
      <div class="row"><span class="muted">Status</span>${{rbPill}}</div>
    </div>
    <div class="card"><h2>Options Lab</h2>
      <div class="metric">${{op.active_strategies}} active</div>
      <div class="row"><span class="muted">Keep / Watch / Drop</span><span class="mono">${{op.keep}}/${{op.watch}}/${{op.drop}}</span></div>
      <div class="row"><span class="muted">Orphan rate</span>${{pill(orphan, orphanCls)}}</div>
      <div class="row"><span class="muted">Open lots</span><span class="mono">${{op.open_lots}}</span></div>
      <div class="row"><span class="muted">Report</span><span class="mono">${{op.selection_file||'—'}}</span></div>
    </div>
    <div class="card"><h2>System Health</h2>
      <div class="row"><span class="muted">Cron / last run</span>${{pill(sy.cron, sy.cron==='OK'?'ok':'warn')}}</div>
      <div class="row"><span class="muted">Ledger health</span>${{pill(sy.ledger_health, ledgerCls)}}</div>
      <div class="row"><span class="muted">Router</span>${{pill(sy.router, routerCls)}}</div>
      <div class="row"><span class="muted">First router ENTRY</span><span class="mono">${{sy.router_first_entry||'PENDING'}}</span></div>
      <div class="row"><span class="muted">Last run</span><span class="mono">${{sy.last_run||'—'}}</span></div>
    </div>`;
}}
function renderSpark() {{
  const s = DATA.rubber_band.series||[];
  const svg = document.getElementById('spark');
  if (s.length < 2) {{ svg.innerHTML = ''; return; }}
  const vals = s.map(p=>p.e);
  const min = Math.min(...vals), max = Math.max(...vals);
  const span = Math.max(0.01, max-min);
  const pts = s.map((p,i) => {{
    const x = i/(s.length-1)*1000;
    const y = 110 - ((p.e-min)/span)*100;
    return `${{x.toFixed(1)}},${{y.toFixed(1)}}`;
  }}).join(' ');
  const color = DATA.rubber_band.equity >= DATA.rubber_band.start_equity ? '#2ea043' : '#da3633';
  svg.innerHTML = `<polyline fill="none" stroke="${{color}}" stroke-width="2.5" points="${{pts}}"/>`;
  document.getElementById('sparkLegend').textContent =
    `Start $${{DATA.rubber_band.start_equity.toFixed(0)}} → $${{DATA.rubber_band.equity.toFixed(2)}} (${{DATA.rubber_band.return_pct>=0?'+':''}}${{DATA.rubber_band.return_pct}}%)`;
}}
function renderBoard() {{
  const rows = DATA.options.leaderboard||[];
  let html = `<thead><tr><th>Strategy</th><th>DTE</th><th>n</th><th>Win%</th><th>Median%</th><th>p10%</th><th>Status</th></tr></thead><tbody>`;
  for (const r of rows) {{
    const exits = Number(r.exits||0);
    const wins = Number(r.wins||0);
    const wr = exits ? (100*wins/exits).toFixed(1) : '0.0';
    const rec = r.recommendation||'watch';
    html += `<tr class="${{rec}}"><td>${{r.strategy_id}}</td><td class="mono">${{r.dte_profile||'—'}}</td>
      <td class="mono">${{exits}}</td><td class="mono">${{wr}}</td>
      <td class="mono">${{Number(r.med_return_pct||0).toFixed(2)}}</td>
      <td class="mono">${{Number(r.p10_return_pct||0).toFixed(2)}}</td>
      <td>${{pill(rec, rec==='keep'?'ok':rec==='drop'?'bad':'warn')}}</td></tr>`;
  }}
  html += '</tbody>';
  document.getElementById('board').innerHTML = html;
}}
function heatColor(n) {{
  if (!n) return '#21262d';
  if (n===1) return 'rgba(56,139,253,.35)';
  if (n===2) return 'rgba(56,139,253,.55)';
  return 'rgba(46,160,67,.65)';
}}
function renderHeat() {{
  const m = DATA.frequency.matrix||{{}};
  const strats = DATA.frequency.strategies||[];
  const days = Object.keys(m);
  let html = `<div class="heat-row"><div class="muted">Day</div>` +
    strats.map(s=>`<div class="muted" style="text-align:center;font-size:0.7rem">${{s}}</div>`).join('') + `</div>`;
  for (const d of days) {{
    html += `<div class="heat-row"><div class="mono" style="font-size:0.75rem">${{d.slice(5)}}</div>`;
    for (const s of strats) {{
      const n = (m[d]&&m[d][s])||0;
      html += `<div class="heat-cell" style="background:${{heatColor(n)}}">${{n||''}}</div>`;
    }}
    html += `</div>`;
  }}
  document.getElementById('heat').innerHTML = `<div class="heat">${{html||'<div class="muted">No frequency data</div>'}}</div>`;
}}
function renderExps() {{
  const ex = DATA.experiments||{{}};
  function card(e, kind) {{
    const head = kind==='p2b'
      ? '<tr><th>Arm</th><th>Strategy</th><th>DTE</th><th>n</th><th>Med%</th><th>p10%</th><th>Status</th></tr>'
      : '<tr><th>Arm</th><th>Strategy</th><th>Strike</th><th>n</th><th>Med%</th><th>p10%</th><th>Status</th></tr>';
    let rows = (e.arms||[]).map(a => {{
      return `<tr><td>${{a.label}}</td><td class="mono">${{a.id}}</td><td class="mono">${{a.extra||'—'}}</td>
        <td class="mono">${{a.exits}}</td><td class="mono">${{fmtPct(a.med)}}</td>
        <td class="mono">${{fmtPct(a.p10)}}</td>
        <td>${{pill(a.status||'INSUFFICIENT', statusCls(a.status))}}</td></tr>`;
    }}).join('');
    return `<div class="card"><h2>${{e.title||''}}</h2>
      <div class="muted" style="margin-bottom:8px">${{e.subtitle||''}}</div>
      <table><thead>${{head}}</thead><tbody>${{rows}}</tbody></table>
      <div class="row" style="margin-top:10px"><span class="muted">Progress</span><span>${{e.progress||'—'}}</span></div>
      <div class="muted" style="font-size:0.8rem;margin-top:6px">${{e.note||''}}</div></div>`;
  }}
  document.getElementById('exps').innerHTML = card(ex.p2b||{{}}, 'p2b') + card(ex.p2c||{{}}, 'p2c');
  const rc = DATA.router_card||{{}};
  document.getElementById('routerCard').innerHTML = `
    <h2>Router Status — Controlled Layout</h2>
    <div class="row"><span class="muted">S163/S164/S166/S167/S168 confirmed</span>
      ${{pill(rc.status||'PENDING', statusCls(rc.status))}}</div>
    <div class="row"><span class="muted">First confirmed entry date</span>
      <span class="mono">${{rc.first_entry_date||'PENDING'}}</span></div>`;
}}
function renderRbBoard() {{
  const rows = (DATA.rubber_band&&DATA.rubber_band.leaderboard)||[];
  let html = `<thead><tr><th>Rank</th><th>Strategy</th><th>n</th><th>WR%</th><th>Avg%</th><th>Med%</th><th>p10%</th><th>PF</th><th>Total $</th></tr></thead><tbody>`;
  rows.forEach((r,i) => {{
    const pf = Number(r.pf||0);
    const status = r.status || (r.n===0 ? 'NEW' : (r.n<30 ? 'WATCH' : 'ACTIVE'));
    const cls = status==='NEW' ? 'watch' : (pf>=1.1 ? 'keep' : (pf>=0.9 ? 'watch' : 'drop'));
    const badge = status==='NEW' ? ' <span class="pill watch">NEW</span>' : '';
    html += `<tr class="${{cls}}"><td class="mono">${{i+1}}</td><td>${{r.strategy}}${{badge}}</td>
      <td class="mono">${{r.n}}</td><td class="mono">${{r.wr}}</td>
      <td class="mono">${{fmtPct(r.avg)}}</td><td class="mono">${{fmtPct(r.med)}}</td>
      <td class="mono">${{fmtPct(r.p10)}}</td><td class="mono">${{pf.toFixed(2)}}</td>
      <td class="mono">${{fmtMoney(r.total)}}</td></tr>`;
  }});
  html += '</tbody>';
  document.getElementById('rbBoard').innerHTML = html;
  const dis = (DATA.rubber_band&&DATA.rubber_band.disabled)||[];
  let dhtml = `<thead><tr><th colspan="9" style="color:var(--muted)">Disabled strategies (historical stats)</th></tr>
    <tr><th></th><th>Strategy</th><th>n</th><th>WR%</th><th>Avg%</th><th>Med%</th><th>p10%</th><th>PF</th><th>Note</th></tr></thead><tbody>`;
  dis.forEach(r => {{
    dhtml += `<tr class="disabled"><td></td><td>${{r.strategy}}</td>
      <td class="mono">${{r.n}}</td><td class="mono">${{r.wr}}</td>
      <td class="mono">${{fmtPct(r.avg)}}</td><td class="mono">${{fmtPct(r.med)}}</td>
      <td class="mono">${{fmtPct(r.p10)}}</td><td class="mono">${{Number(r.pf||0).toFixed(2)}}</td>
      <td class="muted">${{r.note||'Disabled 2026-07-20'}}</td></tr>`;
  }});
  dhtml += '</tbody>';
  document.getElementById('rbDisabled').innerHTML = dhtml;
}}
document.getElementById('gen').textContent = DATA.generated_at;
renderCards(); renderSpark(); renderBoard(); renderHeat(); renderExps(); renderRbBoard();
</script>
</body>
</html>
"""


def main() -> int:
    try:
        data = build_data()
        orphan = _orphan_from_selection_md()
        data["options"]["orphan_rate"] = orphan
        OUT.parent.mkdir(parents=True, exist_ok=True)
        html = render_html(data)
        OUT.write_text(html, encoding="utf-8")
        print(f"Wrote {OUT}")
        print(f"equity={data['rubber_band']['equity']} router={data['system']['router']} "
              f"leaderboard_rows={len(data['options']['leaderboard'])}")
        return 0
    except Exception as e:
        print(f"dashboard failed: {e}")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
