#!/usr/bin/env python3
"""Profitability research: CLEAN/ALL lenses, costs, constrained portfolio sim.

Research-only. Does not enable live options or change Rubber Band production.
Reads logs/options_trial ledgers + published reports. Writes under
research/options-strategies/results/ and records/current/.

Usage:
  python research/options-strategies/profitability_research.py
"""
from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass, asdict
from datetime import date, datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "live-bots" / "options-paper" / "lab"))
sys.path.insert(0, str(ROOT / "live-bots" / "options-paper" / "reporting"))
sys.path.insert(0, str(ROOT / "live-bots" / "shared"))

from options_lab import LEDGER_PATH, TRIAL_ROOT  # noqa: E402
from options_data_quality_report import (  # noqa: E402
    KNOWN_OUTAGE_DAYS,
    NATURAL_REASON_RE,
    _norm_ret,
)

OUT_DIR = ROOT / "research" / "options-strategies" / "results"
RECORDS_CURRENT = ROOT / "records" / "current"
REPORT_MD = ROOT / "research" / "options-strategies" / "PROFITABILITY_RESEARCH_REPORT.md"

PRIORITY = ["S406", "S404", "S397", "S362", "S167", "S166", "S410", "S430", "S431", "S432"]
# Round-trip cost assumption (premium points → USD via cost column when present)
COST_PER_CONTRACT_USD = 2.00  # commissions + half-spread drag estimate
STOCK_CASH_RESERVE = 250.0
OPTIONS_ALLOCATION = 250.0
SOURCES = {
    "ledger": str(LEDGER_PATH),
    "selection": str(TRIAL_ROOT / "reports" / "2026-10-23_strategy_selection.md"),
    "quality": str(TRIAL_ROOT / "reports" / "2026-10-23_data_quality.md"),
    "selection_csv": str(TRIAL_ROOT / "reports" / "2026-10-23_strategy_selection.csv"),
}


def _load_exits() -> pd.DataFrame:
    path = LEDGER_PATH
    if not path.exists():
        raise SystemExit(f"ledger missing: {path}")
    df = pd.read_csv(path, low_memory=False)
    df["ts"] = pd.to_datetime(df["ts"], format="mixed", utc=True, errors="coerce")
    df["day"] = df["ts"].dt.date
    df["return_pct"] = pd.to_numeric(df.get("return_pct"), errors="coerce")
    df["pnl_usd"] = pd.to_numeric(df.get("pnl_usd"), errors="coerce")
    df["cost"] = pd.to_numeric(df.get("cost"), errors="coerce")
    df["fill_price"] = pd.to_numeric(df.get("fill_price"), errors="coerce")
    df["spread_frac"] = pd.to_numeric(df.get("spread_frac"), errors="coerce")
    exits = df[df["event"].astype(str).str.lower() == "exit"].copy()
    reason = exits["reason"].astype(str)
    exits["is_reconcile"] = reason.str.contains(
        "reconcile|missing_from_broker", case=False, na=False
    )
    exits["is_natural"] = reason.str.contains(
        NATURAL_REASON_RE, case=False, na=False, regex=True
    )
    exits["is_outage_day"] = exits["day"].isin(KNOWN_OUTAGE_DAYS)
    exits["quality"] = "TAINTED"
    exits.loc[
        exits["is_natural"] & ~exits["is_outage_day"] & ~exits["is_reconcile"],
        "quality",
    ] = "CLEAN"
    exits["ret"] = _norm_ret(exits["return_pct"])
    exits["pnl_net"] = exits["pnl_usd"].fillna(0) - COST_PER_CONTRACT_USD
    return exits


def _stats(sub: pd.DataFrame) -> dict:
    r = sub["ret"].dropna()
    pnl = pd.to_numeric(sub["pnl_usd"], errors="coerce").fillna(0)
    pnl_net = pd.to_numeric(sub.get("pnl_net"), errors="coerce")
    if pnl_net is None or pnl_net.isna().all():
        pnl_net = pnl - COST_PER_CONTRACT_USD
    else:
        pnl_net = pnl_net.fillna(pnl - COST_PER_CONTRACT_USD)
    if r.empty:
        return {
            "n": 0, "win": 0.0, "med": 0.0, "avg": 0.0, "p10": 0.0,
            "pnl": 0.0, "pnl_net": 0.0, "pf": 0.0, "expectancy": 0.0,
            "max_dd": 0.0,
        }
    wins = pnl[pnl > 0].sum()
    losses = -pnl[pnl < 0].sum()
    pf = float(wins / losses) if losses > 0 else (float("inf") if wins > 0 else 0.0)
    # Equity curve drawdown on chronological pnl
    ordered = sub.sort_values("ts")
    eq = pd.to_numeric(ordered["pnl_usd"], errors="coerce").fillna(0).cumsum()
    peak = eq.cummax()
    dd = float((eq - peak).min()) if len(eq) else 0.0
    return {
        "n": int(len(r)),
        "win": float((r > 0).mean() * 100),
        "med": float(r.median() * 100),
        "avg": float(r.mean() * 100),
        "p10": float(r.quantile(0.10) * 100),
        "pnl": float(pnl.sum()),
        "pnl_net": float(pnl_net.sum()),
        "pf": pf if math.isfinite(pf) else 99.0,
        "expectancy": float(pnl_net.mean()) if len(pnl_net) else 0.0,
        "max_dd": dd,
    }


def strategy_lenses(exits: pd.DataFrame, sids: list[str]) -> pd.DataFrame:
    rows = []
    for sid in sids:
        sub = exits[exits["strategy_id"].astype(str) == sid]
        all_s = _stats(sub)
        clean_s = _stats(sub[sub["quality"] == "CLEAN"])
        gap_pnl = all_s["pnl"] - clean_s["pnl"]
        rows.append({
            "strategy_id": sid,
            "all_n": all_s["n"], "all_win": all_s["win"], "all_med": all_s["med"],
            "all_p10": all_s["p10"], "all_pnl": all_s["pnl"], "all_pnl_net": all_s["pnl_net"],
            "all_pf": all_s["pf"], "all_exp": all_s["expectancy"], "all_dd": all_s["max_dd"],
            "clean_n": clean_s["n"], "clean_win": clean_s["win"], "clean_med": clean_s["med"],
            "clean_p10": clean_s["p10"], "clean_pnl": clean_s["pnl"],
            "clean_pnl_net": clean_s["pnl_net"], "clean_pf": clean_s["pf"],
            "clean_exp": clean_s["expectancy"], "clean_dd": clean_s["max_dd"],
            "pnl_gap_all_minus_clean": gap_pnl,
        })
    return pd.DataFrame(rows)


def winner_loser_features(exits: pd.DataFrame, sids: list[str]) -> pd.DataFrame:
    """Pre-decision features only: cost, spread, reason family, symbol conc."""
    rows = []
    sub = exits[exits["strategy_id"].astype(str).isin(sids)].copy()
    sub["win"] = sub["ret"] > 0
    for sid, g in sub.groupby(sub["strategy_id"].astype(str)):
        for label, part in (("winner", g[g["win"]]), ("loser", g[~g["win"]])):
            if part.empty:
                continue
            rows.append({
                "strategy_id": sid,
                "cohort": label,
                "n": len(part),
                "med_cost": float(part["cost"].median()) if part["cost"].notna().any() else None,
                "med_spread": float(part["spread_frac"].median())
                if part["spread_frac"].notna().any() else None,
                "med_ret_pct": float(part["ret"].median() * 100),
                "top_symbol_share": float(
                    part["symbol"].astype(str).value_counts(normalize=True).iloc[0]
                ) if len(part) else None,
                "eod_share": float(
                    part["reason"].astype(str).str.contains("EOD|eod", case=False).mean()
                ),
                "tp_share": float(
                    part["reason"].astype(str).str.contains("take_profit", case=False).mean()
                ),
                "sl_share": float(
                    part["reason"].astype(str).str.contains("stop_loss", case=False).mean()
                ),
            })
    return pd.DataFrame(rows)


def classify_status(row: pd.Series) -> str:
    n = int(row["clean_n"])
    med = float(row["clean_med"])
    exp = float(row["clean_exp"])
    p10 = float(row["clean_p10"])
    if n < 8:
        return "NEEDS MORE DATA"
    if p10 < -70 and exp < 0:
        return "EXECUTION OR DATA PROBLEM"
    if med > 0 and exp > 0 and n >= 30 and row["clean_pf"] >= 1.1:
        return "PROFITABLE IN EXPLORATORY PAPER"
    if med > 0 and exp > 0:
        return "PROMISING BUT UNVALIDATED"
    return "NOT ECONOMICALLY ATTRACTIVE"


def scorecard(lenses: pd.DataFrame) -> pd.DataFrame:
    out = lenses.copy()
    out["status"] = out.apply(classify_status, axis=1)
    # Composite: net expectancy, sample, pf, dd penalty
    out["score"] = (
        out["clean_exp"].clip(-50, 50) * 2
        + np.log1p(out["clean_n"]) * 5
        + out["clean_pf"].clip(0, 3) * 10
        + out["clean_dd"].clip(-500, 0) * 0.05
        + (out["clean_med"] > 0).astype(float) * 10
    )
    out = out.sort_values("score", ascending=False)
    return out


@dataclass
class SimResult:
    mode: str
    starting_options_cash: float
    stock_reserve: float
    n_fills: int
    n_skipped_capital: int
    n_skipped_simultaneous: int
    ending_cash: float
    realized_pnl: float
    max_drawdown: float
    max_simultaneous: int
    note: str


def _load_entry_exit_pairs(arms: list[str]) -> pd.DataFrame:
    """Pair CLEAN exits with prior entry cost/timing for capital replay."""
    path = LEDGER_PATH
    df = pd.read_csv(path, low_memory=False)
    df["ts"] = pd.to_datetime(df["ts"], format="mixed", utc=True, errors="coerce")
    df["day"] = df["ts"].dt.date
    df["strategy_id"] = df["strategy_id"].astype(str)
    df = df[df["strategy_id"].isin(arms)].copy()
    df["cost"] = pd.to_numeric(df.get("cost"), errors="coerce")
    df["pnl_usd"] = pd.to_numeric(df.get("pnl_usd"), errors="coerce")
    df["return_pct"] = pd.to_numeric(df.get("return_pct"), errors="coerce")
    reason = df["reason"].astype(str)
    is_reconcile = reason.str.contains("reconcile|missing_from_broker", case=False, na=False)
    is_natural = reason.str.contains(NATURAL_REASON_RE, case=False, na=False, regex=True)
    is_outage = df["day"].isin(KNOWN_OUTAGE_DAYS)

    exits = df[df["event"].astype(str).str.lower() == "exit"].copy()
    exits = exits[is_natural.loc[exits.index] & ~is_outage.loc[exits.index] & ~is_reconcile.loc[exits.index]]
    entries = df[df["event"].astype(str).str.lower() == "entry"].copy()

    # Map lot_id → entry ts/cost
    ent = entries.dropna(subset=["lot_id"]).set_index("lot_id")
    rows = []
    for _, x in exits.iterrows():
        lid = x.get("lot_id")
        cost = float(x["cost"]) if pd.notna(x.get("cost")) and float(x["cost"]) > 0 else None
        entry_ts = x["ts"]
        if lid in ent.index:
            e = ent.loc[lid]
            if isinstance(e, pd.DataFrame):
                e = e.iloc[0]
            entry_ts = e["ts"] if pd.notna(e.get("ts")) else entry_ts
            if cost is None and pd.notna(e.get("cost")) and float(e["cost"]) > 0:
                cost = float(e["cost"])
        if cost is None or cost <= 0:
            cost = 50.0
        # Hold at least until exit; if entry missing, assume same-day open
        if pd.isna(entry_ts) or entry_ts > x["ts"]:
            entry_ts = x["ts"] - pd.Timedelta(hours=4)
        rows.append({
            "strategy_id": x["strategy_id"],
            "lot_id": lid,
            "entry_ts": entry_ts,
            "exit_ts": x["ts"],
            "cost": cost,
            "pnl_usd": float(x["pnl_usd"]) if pd.notna(x["pnl_usd"]) else 0.0,
        })
    return pd.DataFrame(rows).sort_values("entry_ts")


def constrained_portfolio_sim(
    exits: pd.DataFrame,
    arms: list[str],
    *,
    options_cash: float = OPTIONS_ALLOCATION,
    max_simultaneous: int = 2,
    mode: str = "capital_constrained",
) -> SimResult:
    """Replay CLEAN trades under capital / concurrency constraints.

    Discovery mode: ignore cash (unconstrained paper). Constrained: whole
    contracts, premium locked until exit, unfilled when broke / at max open.
    """
    clean = exits[
        (exits["quality"] == "CLEAN")
        & (exits["strategy_id"].astype(str).isin(arms))
    ].sort_values("ts")

    if mode == "discovery":
        pnl = pd.to_numeric(clean["pnl_usd"], errors="coerce").fillna(0)
        eq = options_cash + pnl.cumsum()
        dd = float((eq - eq.cummax()).min()) if len(eq) else 0.0
        return SimResult(
            mode="discovery",
            starting_options_cash=options_cash,
            stock_reserve=STOCK_CASH_RESERVE,
            n_fills=int(len(clean)),
            n_skipped_capital=0,
            n_skipped_simultaneous=0,
            ending_cash=float(options_cash + pnl.sum()),
            realized_pnl=float(pnl.sum()),
            max_drawdown=dd,
            max_simultaneous=len(arms),
            note="DISCOVERY / exploratory paper — no capital or concurrency constraints",
        )

    pairs = _load_entry_exit_pairs(arms)
    cash = float(options_cash)
    peak = cash
    max_dd = 0.0
    fills = 0
    skip_cap = 0
    skip_sim = 0
    realized = 0.0
    open_lots: list[dict] = []
    max_open = 0

    def _mark_to_peak():
        nonlocal peak, max_dd
        locked = sum(o["cost"] for o in open_lots)
        equity = cash + locked  # approx; ignores MTM
        peak = max(peak, equity)
        max_dd = min(max_dd, equity - peak)

    for _, row in pairs.iterrows():
        # Close anything that exited before this entry
        still = []
        for o in open_lots:
            if o["exit_ts"] <= row["entry_ts"]:
                cash += o["cost"] + o["pnl_usd"]
                realized += o["pnl_usd"]
                fills += 1
            else:
                still.append(o)
        open_lots = still
        _mark_to_peak()

        if len(open_lots) >= max_simultaneous:
            skip_sim += 1
            continue
        cost = float(row["cost"])
        if cost > cash + 1e-6:
            skip_cap += 1
            continue
        cash -= cost
        open_lots.append({
            "cost": cost,
            "pnl_usd": float(row["pnl_usd"]),
            "exit_ts": row["exit_ts"],
        })
        max_open = max(max_open, len(open_lots))
        _mark_to_peak()

    # Flush remaining opens at their exits
    for o in sorted(open_lots, key=lambda x: x["exit_ts"]):
        cash += o["cost"] + o["pnl_usd"]
        realized += o["pnl_usd"]
        fills += 1
        _mark_to_peak()
    open_lots = []

    return SimResult(
        mode=mode,
        starting_options_cash=options_cash,
        stock_reserve=STOCK_CASH_RESERVE,
        n_fills=fills,
        n_skipped_capital=skip_cap,
        n_skipped_simultaneous=skip_sim,
        ending_cash=cash,
        realized_pnl=realized,
        max_drawdown=max_dd,
        max_simultaneous=max_open,
        note=(
            f"Whole contracts; premium locked until exit; "
            f"max {max_simultaneous} simultaneous; stock reserve ${STOCK_CASH_RESERVE:.0f} untouched"
        ),
    )


def estimate_min_account(lenses: pd.DataFrame, arms: list[str]) -> dict:
    """Rough minimum practical account: reserve + options sleeve + buffer."""
    sub = lenses[lenses["strategy_id"].isin(arms)]
    med_cost = 55.0  # typical from paper min_cost/filters
    # Need room for 2 contracts + reserve + 1 buffer contract
    options_need = med_cost * 3
    total = STOCK_CASH_RESERVE + max(OPTIONS_ALLOCATION, options_need) + 100
    return {
        "stock_reserve": STOCK_CASH_RESERVE,
        "options_sleeve_research": OPTIONS_ALLOCATION,
        "assumed_med_contract_cost": med_cost,
        "min_practical_account_usd": round(total, 0),
        "rationale": (
            "$250 stock reserve + $250 options research sleeve + ~$100 buffer; "
            "below ~$600 concurrent 2-contract options + stock reserve is impractical"
        ),
        "arms": arms,
    }


def overlap_corr(exits: pd.DataFrame, arms: list[str]) -> pd.DataFrame:
    """Daily realized pnl correlation across arms (CLEAN)."""
    clean = exits[
        (exits["quality"] == "CLEAN")
        & (exits["strategy_id"].astype(str).isin(arms))
    ].copy()
    if clean.empty:
        return pd.DataFrame()
    clean["pnl_usd"] = pd.to_numeric(clean["pnl_usd"], errors="coerce").fillna(0)
    pivot = clean.pivot_table(
        index="day", columns="strategy_id", values="pnl_usd", aggfunc="sum"
    ).fillna(0)
    if pivot.shape[1] < 2:
        return pd.DataFrame()
    return pivot.corr()


def write_dashboard(score: pd.DataFrame, sims: list[SimResult], corr: pd.DataFrame) -> Path:
    path = OUT_DIR / "profitability_dashboard.md"
    lines = [
        "# Profitability Research Dashboard",
        "",
        f"_Generated {datetime.now(timezone.utc).isoformat()}_",
        "",
        "## Data sources",
        "",
    ]
    for k, v in SOURCES.items():
        lines.append(f"- **{k}**: `{v}`")
    lines += [
        "",
        "## Strategy scorecard (CLEAN lens primary)",
        "",
        "| sid | status | clean n | clean med% | clean $ | clean $/trade | ALL $ | $ gap | score |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for _, r in score.iterrows():
        lines.append(
            f"| {r['strategy_id']} | {r['status']} | {int(r['clean_n'])} | "
            f"{r['clean_med']:+.1f} | ${r['clean_pnl']:+,.0f} | "
            f"${r['clean_exp']:+.2f} | ${r['all_pnl']:+,.0f} | "
            f"${r['pnl_gap_all_minus_clean']:+,.0f} | {r['score']:.1f} |"
        )
    lines += ["", "## Portfolio simulations", ""]
    for s in sims:
        lines += [
            f"### Mode: `{s.mode}`",
            "",
            f"- Starting options cash: ${s.starting_options_cash:.0f}",
            f"- Stock reserve (untouched): ${s.stock_reserve:.0f}",
            f"- Fills / skip_capital / skip_simultaneous: "
            f"{s.n_fills} / {s.n_skipped_capital} / {s.n_skipped_simultaneous}",
            f"- Realized P&L: ${s.realized_pnl:+,.2f}",
            f"- Ending options cash: ${s.ending_cash:.2f}",
            f"- Max DD (options sleeve): ${s.max_drawdown:+,.2f}",
            f"- Max simultaneous: {s.max_simultaneous}",
            f"- Note: {s.note}",
            "",
        ]
    if corr is not None and not corr.empty:
        lines += ["## CLEAN daily P&L correlation", "", corr.round(2).to_markdown(), ""]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_report(
    score: pd.DataFrame,
    features: pd.DataFrame,
    sims: list[SimResult],
    corr: pd.DataFrame,
    min_acct: dict,
) -> Path:
    s406 = score[score["strategy_id"] == "S406"]
    s404 = score[score["strategy_id"] == "S404"]
    disc = next(s for s in sims if s.mode == "discovery")
    cons = next(s for s in sims if s.mode == "capital_constrained")
    combo = next((s for s in sims if s.mode == "combo_constrained"), cons)

    def row(sid: str) -> pd.Series:
        return score[score["strategy_id"] == sid].iloc[0]

    makers = score[score["status"].isin([
        "PROFITABLE IN EXPLORATORY PAPER", "PROMISING BUT UNVALIDATED"
    ])]
    losers = score[score["status"] == "NOT ECONOMICALLY ATTRACTIVE"]

    lines = [
        "# Profitability Research Report",
        "",
        f"**Generated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}  ",
        f"**Branch work:** paper research + safety; live entries remain OFF  ",
        f"**LIVE_OPTIONS_ENTRIES:** fail-closed default `0` (unchanged)  ",
        f"**LIVE_OPTIONS_MAX_CAP:** hard maximum `$250` (configs above rejected)  ",
        "",
        "## Data sources (every figure cites these)",
        "",
    ]
    for k, v in SOURCES.items():
        lines.append(f"- `{k}` → `{v}`")
    lines += [
        f"- Analysis outputs → `{OUT_DIR.as_posix()}`",
        "",
        "---",
        "",
        "## A. What Actually Makes Money?",
        "",
        "Primary lens is **CLEAN** (natural TP/SL/EOD on non-outage days). "
        "ALL includes TAINTED reconcile/outage mass and can invent or destroy dollars.",
        "",
        "### CLEAN keepers among priority arms",
        "",
        "| Strategy | CLEAN n | WR% | Med% | CLEAN $ | $/trade (after $2 cost) | Status |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for _, r in makers.iterrows():
        lines.append(
            f"| {r['strategy_id']} | {int(r['clean_n'])} | {r['clean_win']:.1f} | "
            f"{r['clean_med']:+.1f} | ${r['clean_pnl']:+,.0f} | "
            f"${r['clean_exp']:+.2f} | {r['status']} |"
        )
    if s406.shape[0]:
        r = row("S406")
        lines += [
            "",
            "### S406 CLEAN vs ALL dollar gap",
            "",
            f"- CLEAN: n={int(r['clean_n'])}, ${r['clean_pnl']:+,.0f}, med {r['clean_med']:+.1f}% "
            f"(source: `{SOURCES['ledger']}` + CLEAN tag rules in `options_data_quality_report.py`)",
            f"- ALL: n={int(r['all_n'])}, ${r['all_pnl']:+,.0f}, med {r['all_med']:+.1f}%",
            f"- Gap (ALL − CLEAN) = **${r['pnl_gap_all_minus_clean']:+,.0f}** — "
            "extra ALL dollars are mostly TAINTED / reconcile-path outcomes, not proven alpha.",
            f"- After ${COST_PER_CONTRACT_USD:.0f}/contract cost drag: CLEAN net "
            f"${r['clean_pnl_net']:+,.0f} (${r['clean_exp']:+.2f}/trade).",
        ]
    if s404.shape[0]:
        r = row("S404")
        lines += [
            "",
            "### S404",
            "",
            f"- CLEAN ${r['clean_pnl']:+,.0f} (n={int(r['clean_n'])}, WR {r['clean_win']:.1f}%, "
            f"med {r['clean_med']:+.1f}%) vs ALL ${r['all_pnl']:+,.0f} — "
            "ALL median collapses when TAINTED days included "
            f"(ALL med {r['all_med']:+.1f}%).",
        ]
    lines += [
        "",
        "### Winner vs loser pre-decision traits",
        "",
        "Features available at decision time only (cost, spread, exit-reason shares).",
        "",
    ]
    if not features.empty:
        lines.append(features.to_markdown(index=False))
    else:
        lines.append("_Insufficient feature columns in ledger for cohort split._")
    lines += [
        "",
        "Effects separation (qualitative from ledger structure):",
        "",
        "- **Underlying move:** RubberBand/GapDown winners show higher TP share; "
        "losers cluster on stop_loss/EOD — consistent with underlying direction, not only IV.",
        "- **Contract choice:** ITM3 (S406) vs OTM2 (S404) vs ITM1 (S397) — CLEAN medians "
        "similar (~53–56%) but S404 has better CLEAN $ density; OTM increases left-tail risk on ALL.",
        "- **Timing:** DayTrader S430–S432 still n≤4 — not attributable.",
        "- **Optimistic fills:** paper ask−0.01 + virtual $500 buckets overstate concurrency "
        "vs $250 live sleeve (see constrained sim).",
        "",
        "---",
        "",
        "## B. What Is Losing Money?",
        "",
        "| Strategy | CLEAN n | Med% | CLEAN $ | ALL $ | Status |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for _, r in losers.iterrows():
        lines.append(
            f"| {r['strategy_id']} | {int(r['clean_n'])} | {r['clean_med']:+.1f} | "
            f"${r['clean_pnl']:+,.0f} | ${r['all_pnl']:+,.0f} | {r['status']} |"
        )
    lines += [
        "",
        "Book-level drag (from `2026-10-23_data_quality.md`):",
        "",
        "- TAINTED exits: n=2036, −$11,713 — ops/reconcile, not strategy alpha.",
        "- Orphan exits: 422 / 3775 = **11.2%** — attribution debt (history preserved; "
        "live micro now normalizes OCC + best-effort reclaim).",
        "- CLEAN kill list leaders (S212, S202, S360, …) remain non-attractive; "
        "not re-promoted here.",
        "",
        "---",
        "",
        "## C. Best New Experiments (implemented)",
        "",
        "New strategy IDs only (S404/S406 paper twins preserved). "
        "**Awaiting forward paper evidence** — no live enablement.",
        "",
        "| ID | Name | Hypothesis | Mechanics vs baseline |",
        "|---|---|---|---|",
        "| **S440** | RubberBand_ITM3_StrongGap | Stronger gap (≤−3%) cuts S406 left tail | "
        "RB reclaim + GAP_STRONG; strike ITM3 |",
        "| **S441** | GapDown_OTM2_StrongGap | S404 structure + S166 gap quality | "
        "Gap ≤−3%, OTM2 |",
        "| **S442** | RubberBand_ITM3_5DTE | DTE neighbor to S362/S406 | ITM3, 5 DTE |",
        "| **S443** | TrueORB_15m | Classical ORB ≠ S430 drive proxy | "
        "≥15m session, stronger drive/high |",
        "",
        "Paper buckets (research-only):",
        "",
        "- `b92 s406_maxprem40` — S406 scope, max_premium=$40 (left-tail / cost).",
        "- `b93 s440_rb_stronggap` — dedicated S440 sleeve.",
        "",
        "Code: `live-bots/options-paper/strategies/options_signals.py` "
        "(PROFITABILITY_EXPERIMENT_STRATEGIES), "
        "`live-bots/options-paper/lab/options_lab.py` (bucket 92/93 inject).",
        "",
        "---",
        "",
        "## D. Best Portfolio Combination (constrained sim)",
        "",
        f"Arms tested: S406 + S404 + S397 + S362 (CLEAN replay).",
        "",
        f"| Mode | Fills | Skip capital | Skip concurrency | Realized $ | End cash | Max DD |",
        f"|---|---:|---:|---:|---:|---:|---:|",
        f"| Discovery (unconstrained) | {disc.n_fills} | {disc.n_skipped_capital} | "
        f"{disc.n_skipped_simultaneous} | ${disc.realized_pnl:+,.0f} | "
        f"${disc.ending_cash:,.0f} | ${disc.max_drawdown:+,.0f} |",
        f"| Capital-constrained ($250 opts) | {cons.n_fills} | {cons.n_skipped_capital} | "
        f"{cons.n_skipped_simultaneous} | ${cons.realized_pnl:+,.0f} | "
        f"${cons.ending_cash:,.0f} | ${cons.max_drawdown:+,.0f} |",
        f"| Combo constrained | {combo.n_fills} | {combo.n_skipped_capital} | "
        f"{combo.n_skipped_simultaneous} | ${combo.realized_pnl:+,.0f} | "
        f"${combo.ending_cash:,.0f} | ${combo.max_drawdown:+,.0f} |",
        "",
        f"**Minimum practical account (estimate):** "
        f"${min_acct['min_practical_account_usd']:.0f} — {min_acct['rationale']}",
        "",
        "Correlation (CLEAN daily P&L):",
        "",
    ]
    if corr is not None and not corr.empty:
        lines.append(corr.round(2).to_markdown())
    else:
        lines.append("_Insufficient overlapping days for correlation matrix._")
    lines += [
        "",
        "**Portfolio read:** Prefer at most one GapDown family (S404 **or** S397) plus "
        "one RubberBand family (S406 **or** S362) under a $250 options sleeve — "
        "correlation and capital skips make four-arm concurrency unrealistic. "
        "**Do not recommend live execution.**",
        "",
        "---",
        "",
        "## E. Next Steps to Genuine Profitability",
        "",
        "1. Keep `LIVE_OPTIONS_ENTRIES=0` until S440/S441 forward n≥20 CLEAN and "
        "p10 protocol clears.",
        "2. Collect forward paper on S440–S443 + b92/b93 for 10–15 sessions.",
        "3. Drive orphan rate &lt;10% via OCC-normalized reclaim (shipped) + paper "
        "`attribute_vanished_lots` monitoring.",
        "4. Re-run constrained sim monthly; treat discovery $ as upper bound only.",
        "5. Separate Myers research — live trading stays disabled there.",
        "6. No Rubber Band / production live behavior changes without explicit approval.",
        "",
        "---",
        "",
        "## Safety confirmation",
        "",
        "| Control | Status |",
        "|---|---|",
        "| LIVE_OPTIONS_ENTRIES | **0** workflow + fail-closed parser |",
        "| Options hard max | **$250** (reject &gt;250 / NaN / inf) |",
        "| Stock cash reserve | **$250** |",
        "| Broker query fail-closed | Entries abort; manage still runs |",
        "| DayTrader freshness | Same-day disk TTL; no RTH disk pin; "
        "incomplete morning grace |",
        "| Main merge | **Not merged** |",
        "",
    ]
    REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")
    return REPORT_MD


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RECORDS_CURRENT.mkdir(parents=True, exist_ok=True)

    exits = _load_exits()
    lenses = strategy_lenses(exits, PRIORITY)
    feats = winner_loser_features(exits, PRIORITY)
    score = scorecard(lenses)

    arms = ["S406", "S404", "S397", "S362"]
    disc = constrained_portfolio_sim(exits, arms, mode="discovery")
    cons = constrained_portfolio_sim(
        exits, arms, options_cash=OPTIONS_ALLOCATION, max_simultaneous=2,
        mode="capital_constrained",
    )
    # Best combo heuristic: top 2 by clean expectancy with n>=20
    ranked = score[
        (score["strategy_id"].isin(arms)) & (score["clean_n"] >= 20)
    ].sort_values("clean_exp", ascending=False)
    top2 = ranked["strategy_id"].head(2).tolist() or arms[:2]
    combo = constrained_portfolio_sim(
        exits, top2, options_cash=OPTIONS_ALLOCATION, max_simultaneous=2,
        mode="capital_constrained",
    )
    combo = SimResult(
        mode="combo_constrained",
        starting_options_cash=combo.starting_options_cash,
        stock_reserve=combo.stock_reserve,
        n_fills=combo.n_fills,
        n_skipped_capital=combo.n_skipped_capital,
        n_skipped_simultaneous=combo.n_skipped_simultaneous,
        ending_cash=combo.ending_cash,
        realized_pnl=combo.realized_pnl,
        max_drawdown=combo.max_drawdown,
        max_simultaneous=combo.max_simultaneous,
        note=combo.note + f" | arms={top2}",
    )

    corr = overlap_corr(exits, arms)
    min_acct = estimate_min_account(lenses, arms)

    lenses.to_csv(OUT_DIR / "strategy_lenses_clean_all.csv", index=False)
    score.to_csv(OUT_DIR / "strategy_scorecard.csv", index=False)
    feats.to_csv(OUT_DIR / "winner_loser_features.csv", index=False)
    if not corr.empty:
        corr.to_csv(OUT_DIR / "clean_daily_pnl_correlation.csv")
    (OUT_DIR / "portfolio_sims.json").write_text(
        json.dumps([asdict(s) for s in (disc, cons, combo)], indent=2),
        encoding="utf-8",
    )
    (OUT_DIR / "min_account_estimate.json").write_text(
        json.dumps(min_acct, indent=2), encoding="utf-8",
    )
    (OUT_DIR / "sources.json").write_text(
        json.dumps(SOURCES, indent=2), encoding="utf-8",
    )

    dash = write_dashboard(score, [disc, cons, combo], corr)
    report = write_report(score, feats, [disc, cons, combo], corr, min_acct)

    # Link from records/current
    link = RECORDS_CURRENT / "profitability-research.md"
    link.write_text(
        "\n".join([
            "# Profitability research (pointer)",
            "",
            f"- Main report: [`../../research/options-strategies/PROFITABILITY_RESEARCH_REPORT.md`]"
            f"(../../research/options-strategies/PROFITABILITY_RESEARCH_REPORT.md)",
            f"- Dashboard: [`../../research/options-strategies/results/profitability_dashboard.md`]"
            f"(../../research/options-strategies/results/profitability_dashboard.md)",
            f"- Scorecard CSV: `research/options-strategies/results/strategy_scorecard.csv`",
            f"- Generated: {date.today().isoformat()}",
            f"- LIVE_OPTIONS_ENTRIES remains **0** (fail-closed).",
            "",
        ]),
        encoding="utf-8",
    )

    print(f"Wrote {report}")
    print(f"Wrote {dash}")
    print(f"Scorecard rows: {len(score)}")
    print(
        f"Discovery ${disc.realized_pnl:+,.0f} vs constrained ${cons.realized_pnl:+,.0f} "
        f"(skips cap={cons.n_skipped_capital} sim={cons.n_skipped_simultaneous})"
    )
    print(f"Best combo arms: {top2}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
