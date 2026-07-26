"""
options_strategy_lab.py - Systematic 100+ strategy testing framework.

Manages StrategySpec definitions, generates bucket assignments, runs daily
auto-kill evaluation, and writes the strategy_registry.json used by GHA.

Designed to run as a library (imported by options_morning_bot, options_lab)
and as a standalone CLI:
  python3 scripts/options_strategy_lab.py --evaluate
  python3 scripts/options_strategy_lab.py --list
  python3 scripts/options_strategy_lab.py --dump-registry

2026-07-25B: Initial framework. Phase 1 = S200-S219 (20 signals).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass, field, asdict
from datetime import date
from pathlib import Path
from typing import Optional

import pandas as pd

# --------------------------------------------------------------------------- #
# Paths
# --------------------------------------------------------------------------- #
_SCRIPTS_DIR = Path(__file__).parent
_ROOT = _SCRIPTS_DIR.parent
_REGISTRY_PATH = _SCRIPTS_DIR / "strategy_registry.json"
_LEDGER_PATH = _ROOT / "logs" / "options_trial" / "_ledger" / "master_ledger.csv"
_EVAL_REPORT_PATH = _ROOT / "logs" / "options_trial" / "reports" / "strategy_eval.md"

# --------------------------------------------------------------------------- #
# Kill / promote thresholds (conservative - avoid false kills)
# --------------------------------------------------------------------------- #
KILL_MIN_N = 15
KILL_MEDIAN_THRESH = -25.0        # median P&L% < -25 at n>=15 ? KILL
KILL_P10_THRESH = -85.0           # p10 < -85 at n>=15 ? KILL (catastrophic tail)
KILL_WR_MIN_N = 25
KILL_WR_THRESH = 15.0             # WR < 15% at n>=25 ? KILL
WATCH_MEDIAN_UPPER = -10.0        # median -10 to -25 ? WATCH
KEEP_MEDIAN_THRESH = -10.0        # median > -10 at n>=30 ? KEEP
PROMOTE_MIN_N = 30
PROMOTE_MEDIAN_THRESH = 0.0       # median > 0 at n>=30 ? PROMOTE


# --------------------------------------------------------------------------- #
# StrategySpec - one testable configuration
# --------------------------------------------------------------------------- #
@dataclass
class StrategySpec:
    strategy_id: str           # "S200"
    signal_name: str           # "GapDown_Aggressive"
    signal_params: dict        # signal-specific thresholds

    dte_target: int = 3
    dte_min: int = 1
    dte_max: int = 7

    strike_offset: int = 0     # 0=ATM, 1=1-OTM, -1=1-ITM, 2=2-OTM
    option_type: str = "call"  # "call" or "put"

    tp_pct: float = 50.0       # take-profit %
    sl_pct: float = -50.0      # stop-loss %

    windows: list = field(default_factory=lambda: ["w1", "w2", "w3", "w4"])
    reps: int = 2

    status: str = "active"     # "active" | "watch" | "dropped"
    launched_date: str = ""
    drop_reason: str = ""

    def to_dict(self) -> dict:
        d = asdict(self)
        d["launched_date"] = self.launched_date or date.today().isoformat()
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "StrategySpec":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})


# --------------------------------------------------------------------------- #
# StrategyLab - manages all specs + bucket generation
# --------------------------------------------------------------------------- #
class StrategyLab:
    WINDOWS = [
        ("w1_0928_1005", "09:28", "10:05"),
        ("w2_1005_1045", "10:05", "10:45"),
        ("w3_1045_1120", "10:45", "11:20"),
        ("w4_1120_1135", "11:20", "11:35"),
    ]

    def __init__(self) -> None:
        self.strategies: list[StrategySpec] = []
        self._next_id: int = 200

    # ---- registry management -------------------------------------------- #

    def add(self, spec: StrategySpec) -> None:
        existing_ids = {s.strategy_id for s in self.strategies}
        if spec.strategy_id in existing_ids:
            return
        if not spec.launched_date:
            spec.launched_date = date.today().isoformat()
        self.strategies.append(spec)

    def drop(self, strategy_id: str, reason: str) -> None:
        for s in self.strategies:
            if s.strategy_id == strategy_id:
                s.status = "dropped"
                s.drop_reason = reason
                return

    def active_strategies(self) -> list[StrategySpec]:
        return [s for s in self.strategies if s.status != "dropped"]

    # ---- bucket generation ---------------------------------------------- #

    def generate_buckets(self, start_idx: int = 88) -> list[dict]:
        """
        Returns list of bucket-definition dicts for all active strategies.
        Each dict mirrors the kwargs for BucketProfile in options_lab.py.
        start_idx: first bucket_id to assign (default 88, after existing 0-87).
        """
        buckets: list[dict] = []
        idx = start_idx
        for spec in self.active_strategies():
            for win_tag, start_hm, end_hm in self.WINDOWS:
                for rep in range(spec.reps):
                    name = (f"lab{idx:04d}_{spec.strategy_id.lower()}"
                            f"_{win_tag}_r{rep + 1}")
                    buckets.append({
                        "bucket_id": idx,
                        "name": name,
                        "strategy_scope": spec.strategy_id,
                        "buy_start_hm": start_hm,
                        "buy_end_hm": end_hm,
                        "take_profit": spec.tp_pct / 100.0,
                        "stop_loss": spec.sl_pct / 100.0,
                        "option_type": spec.option_type,
                        "strike_offset": spec.strike_offset,
                        "dte_target": spec.dte_target,
                        "dte_min": spec.dte_min,
                        "dte_max": spec.dte_max,
                    })
                    idx += 1
        return buckets

    # ---- serialization -------------------------------------------------- #

    def to_json(self) -> str:
        return json.dumps(
            {
                "generated": date.today().isoformat(),
                "next_id": self._next_id,
                "strategies": [s.to_dict() for s in self.strategies],
            },
            indent=2,
        )

    def save(self, path: Path | str | None = None) -> None:
        p = Path(path) if path else _REGISTRY_PATH
        p.write_text(self.to_json(), encoding="utf-8")

    @classmethod
    def from_json(cls, path: Path | str | None = None) -> "StrategyLab":
        p = Path(path) if path else _REGISTRY_PATH
        lab = cls()
        if not p.exists():
            return lab
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            lab._next_id = data.get("next_id", 200)
            for d in data.get("strategies", []):
                try:
                    lab.strategies.append(StrategySpec.from_dict(d))
                except Exception:
                    pass
        except Exception:
            pass
        return lab


# --------------------------------------------------------------------------- #
# Auto-kill evaluator
# --------------------------------------------------------------------------- #

def _load_ledger(ledger_path: Path | str | None = None) -> pd.DataFrame | None:
    p = Path(ledger_path) if ledger_path else _LEDGER_PATH
    if not p.exists():
        return None
    try:
        df = pd.read_csv(p, low_memory=False)
        df.columns = [c.strip().lower() for c in df.columns]
        return df
    except Exception:
        return None


def evaluate_for_kill(
    strategy_id: str,
    ledger_df: pd.DataFrame,
    min_n: int = KILL_MIN_N,
    kill_threshold: float = KILL_MEDIAN_THRESH,
) -> str:
    """
    Evaluate a single strategy's performance from closed ledger rows.

    Returns: "KILL" | "WATCH" | "KEEP" | "PROMOTE" | "INSUFFICIENT"
    """
    try:
        # filter to this strategy's closed exits
        col_sid = "strategy_id" if "strategy_id" in ledger_df.columns else None
        col_pl = next(
            (c for c in ledger_df.columns if "pl_pct" in c or "pnl_pct" in c), None
        )
        if col_sid is None or col_pl is None:
            return "INSUFFICIENT"

        sub = ledger_df[
            (ledger_df[col_sid] == strategy_id)
            & (ledger_df[col_pl].notna())
        ][col_pl].astype(float)

        n = len(sub)
        if n < min_n:
            return "INSUFFICIENT"

        median_pl = float(sub.median())
        p10 = float(sub.quantile(0.10))
        wr = float((sub > 0).mean() * 100)

        # Hard kills
        if n >= min_n and median_pl < KILL_MEDIAN_THRESH:
            return "KILL"
        if n >= min_n and p10 < KILL_P10_THRESH:
            return "KILL"
        if n >= KILL_WR_MIN_N and wr < KILL_WR_THRESH:
            return "KILL"

        # Promote
        if n >= PROMOTE_MIN_N and median_pl > PROMOTE_MEDIAN_THRESH:
            return "PROMOTE"

        # Keep
        if n >= PROMOTE_MIN_N and median_pl > KEEP_MEDIAN_THRESH:
            return "KEEP"

        # Watch (borderline - keep collecting data)
        if KILL_MEDIAN_THRESH <= median_pl <= WATCH_MEDIAN_UPPER:
            return "WATCH"

        return "WATCH"

    except Exception:
        return "INSUFFICIENT"


def run_daily_evaluation(
    ledger_path: Path | str | None = None,
    registry_path: Path | str | None = None,
) -> int:
    """
    Run after market close: evaluate all active strategies, auto-kill losers,
    write report to logs/options_trial/reports/strategy_eval.md,
    update strategy_registry.json.

    Returns exit code 0 always (non-fatal - logged errors are sufficient).
    """
    today = date.today().isoformat()
    ledger_df = _load_ledger(ledger_path)
    lab = StrategyLab.from_json(registry_path)

    lines: list[str] = [
        f"# Strategy Pipeline Evaluation - {today}",
        "",
    ]

    if ledger_df is None:
        lines.append("_Ledger not found - no evaluation possible._")
        _write_eval_report("\n".join(lines))
        return 0

    killed_today: list[tuple[str, str, int, float]] = []
    promote_candidates: list[tuple[str, int, float, float]] = []
    pipeline_rows: list[dict] = []

    all_specs = lab.strategies if lab.strategies else []

    # Also cover existing S163-S175 that aren't in registry yet
    all_known_ids: set[str] = {s.strategy_id for s in all_specs}
    col_sid = "strategy_id" if "strategy_id" in ledger_df.columns else None
    if col_sid:
        for sid in ledger_df[col_sid].dropna().unique():
            if sid not in all_known_ids:
                # synthesize a lightweight spec for evaluation
                all_specs.append(
                    StrategySpec(strategy_id=str(sid), signal_name=str(sid),
                                 signal_params={}, status="active")
                )

    for spec in all_specs:
        if spec.status == "dropped":
            continue
        verdict = evaluate_for_kill(spec.strategy_id, ledger_df)

        col_pl = next(
            (c for c in ledger_df.columns if "pl_pct" in c or "pnl_pct" in c), None
        )
        col_sid2 = "strategy_id" if "strategy_id" in ledger_df.columns else None
        n, median_pl, wr = 0, float("nan"), float("nan")
        if col_pl and col_sid2:
            sub = ledger_df[
                (ledger_df[col_sid2] == spec.strategy_id)
                & (ledger_df[col_pl].notna())
            ][col_pl].astype(float)
            n = len(sub)
            if n > 0:
                median_pl = float(sub.median())
                wr = float((sub > 0).mean() * 100)

        launched = spec.launched_date or "-"
        try:
            days_live = (date.today() - date.fromisoformat(launched)).days
        except Exception:
            days_live = 0

        pipeline_rows.append({
            "id": spec.strategy_id,
            "signal": spec.signal_name,
            "n": n,
            "median": median_pl,
            "wr": wr,
            "verdict": verdict,
            "days": days_live,
            "status": spec.status,
        })

        if verdict == "KILL" and spec.status == "active":
            reason = (f"auto-kill {today}: "
                      f"n={n} median={median_pl:.1f}% wr={wr:.0f}%")
            lab.drop(spec.strategy_id, reason)
            killed_today.append((spec.strategy_id, spec.signal_name, n, median_pl))

        if verdict == "PROMOTE":
            promote_candidates.append((spec.strategy_id, n, median_pl, wr))

    # Build report
    active_count = sum(1 for r in pipeline_rows if r["status"] == "active")
    watching_count = sum(1 for r in pipeline_rows
                         if r["verdict"] in ("WATCH", "INSUFFICIENT")
                         and r["status"] == "active")

    best_row = max(
        [r for r in pipeline_rows if r["n"] >= 10 and r["status"] == "active"],
        key=lambda r: r["median"] if not _isnan(r["median"]) else -999,
        default=None,
    )
    worst_row = min(
        [r for r in pipeline_rows if r["n"] >= 10 and r["status"] == "active"],
        key=lambda r: r["median"] if not _isnan(r["median"]) else 999,
        default=None,
    )

    lines += [
        f"**DAILY PIPELINE SUMMARY - {today}**",
        "",
        (f"Active: {active_count} | "
         f"Watching: {watching_count} | "
         f"Killed today: {len(killed_today)} | "
         f"Promote candidates: {len(promote_candidates)}"),
    ]
    if best_row:
        lines.append(
            f"Best median (n?10): {best_row['id']} "
            f"{best_row['median']:+.1f}% (n={best_row['n']})"
        )
    if worst_row:
        lines.append(
            f"Worst active (n?10): {worst_row['id']} "
            f"{worst_row['median']:+.1f}% (n={worst_row['n']})"
            + (" ? AUTO-KILLED" if worst_row['id'] in
               {k[0] for k in killed_today} else "")
        )
    lines += [""]

    # Pipeline table
    lines += [
        "## Strategy Pipeline Status",
        "",
        "| Strategy | Signal | DTE | n | Median% | WR% | Status | Days |",
        "|----------|--------|-----|---|---------|-----|--------|------|",
    ]
    for r in sorted(pipeline_rows, key=lambda x: x["id"]):
        med_s = f"{r['median']:+.1f}%" if not _isnan(r["median"]) else "-"
        wr_s = f"{r['wr']:.0f}%" if not _isnan(r["wr"]) else "-"
        status_label = r["verdict"] if r["status"] == "active" else r["status"].upper()

        # Attempt to find DTE from spec
        dte = "3"
        for spec in all_specs:
            if spec.strategy_id == r["id"]:
                dte = str(spec.dte_target)
                break

        lines.append(
            f"| {r['id']} | {r['signal'][:18]} | {dte} "
            f"| {r['n']} | {med_s} | {wr_s} | {status_label} | {r['days']} |"
        )

    # Kill log
    lines += [
        "",
        "## Auto-Kill Log",
        "",
        "| Date | Strategy | Reason | n | Median% |",
        "|------|----------|--------|---|---------|",
    ]
    # Load historical kills from existing dropped strategies
    for spec in lab.strategies:
        if spec.status == "dropped" and spec.drop_reason.startswith("auto-kill"):
            parts = spec.drop_reason.split()
            kill_date = parts[1] if len(parts) > 1 else "-"
            lines.append(
                f"| {kill_date} | {spec.strategy_id} | {spec.drop_reason[:40]} | - | - |"
            )
    if not any(s.status == "dropped" and s.drop_reason.startswith("auto-kill")
               for s in lab.strategies):
        lines.append("| - | - | (no kills yet) | - | - |")

    # Promote candidates
    lines += [
        "",
        "## Promote Candidates (n?30, median>0%)",
        "",
        "| Strategy | n | Median% | WR% | Recommendation |",
        "|----------|---|---------|-----|----------------|",
    ]
    if promote_candidates:
        for sid, n, med, wr in sorted(promote_candidates, key=lambda x: -x[2]):
            wr_s = f"{wr:.0f}%" if not _isnan(wr) else "-"
            lines.append(
                f"| {sid} | {n} | {med:+.1f}% | {wr_s} | Tyler review |"
            )
    else:
        lines.append("| - | - | - | - | (none yet - collecting data) |")

    _write_eval_report("\n".join(lines))

    # Save updated registry (only if lab has strategies - don't clobber empty registry)
    if lab.strategies:
        lab.save(registry_path)

    # Summary to stdout
    print(f"Evaluation complete: {len(pipeline_rows)} strategies evaluated, "
          f"{len(killed_today)} killed, {len(promote_candidates)} promote candidates.")
    if killed_today:
        for sid, name, n, med in killed_today:
            print(f"  KILLED: {sid} ({name}) n={n} median={med:.1f}%")
    if promote_candidates:
        for sid, n, med, wr in promote_candidates:
            print(f"  PROMOTE: {sid} n={n} median={med:.1f}% wr={wr:.0f}%")

    return 0


def _isnan(v) -> bool:
    try:
        import math
        return math.isnan(v)
    except Exception:
        return True


def _write_eval_report(text: str) -> None:
    try:
        _EVAL_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        _EVAL_REPORT_PATH.write_text(text, encoding="utf-8")
    except Exception as exc:
        print(f"  WARN: could not write eval report: {exc}", file=sys.stderr)


# --------------------------------------------------------------------------- #
# Phase-1 strategy registry (S200-S219)
# --------------------------------------------------------------------------- #
# Populated below; also loaded from strategy_registry.json if it exists.

_PHASE1_SPECS: list[StrategySpec] = [
    # ---- FAMILY 1: GAP SIGNALS -------------------------------------------
    StrategySpec("S200", "GapDown_Aggressive",
                 {"gap_thresh": -0.03, "vz_min": 2.0, "rsi_max": 50},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S201", "GapDown_Mild",
                 {"gap_lo": -0.03, "gap_hi": -0.015, "vz_min": 1.0},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S202", "GapDown_Monster",
                 {"gap_thresh": -0.05},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S203", "GapUp_Fade",
                 {"gap_thresh": 0.03},
                 dte_target=3, dte_min=1, dte_max=7, option_type="put",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S204", "GapUp_Continuation",
                 {"gap_thresh": 0.02, "vz_min": 2.0},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S205", "GapDown_HighVol",
                 {"gap_thresh": -0.02, "vz_min": 3.0},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S206", "GapDown_WithTrend",
                 {"gap_thresh": -0.02, "vz_min": 1.5},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S207", "GapDown_AtSupport",
                 {"gap_thresh": -0.02, "ma50_pct": 0.05},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S208", "GapDown_AboveMA200",
                 {"gap_thresh": -0.02},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S209", "GapDown_Recovery",
                 {"gap_thresh": -0.02},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    # ---- FAMILY 2: MOVING AVERAGE SIGNALS --------------------------------
    StrategySpec("S210", "MA_Cross_8_21",
                 {"fast": 8, "slow": 21},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S211", "MA_Cross_21_50",
                 {"fast": 21, "slow": 50},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S212", "MA_Bounce_50",
                 {"ma": 50, "pct_band": 0.03},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S213", "MA_Bounce_200",
                 {"ma": 200, "pct_band": 0.03},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S214", "MA_Death_Cross",
                 {"fast": 50, "slow": 200},
                 dte_target=3, dte_min=1, dte_max=7, option_type="put",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S215", "MA_Reclaim_200",
                 {"ma": 200, "lookback": 10},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    # ---- EARLY RSI / BB / VOL ENTRIES (S216-S219) -----------------------
    StrategySpec("S216", "RSI_Oversold_Cross",
                 {"rsi_thresh": 30},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S217", "RSI_25_Bounce",
                 {"rsi_thresh": 25},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S218", "BB_Lower_Touch",
                 {"std": 2.0, "window": 20},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
    StrategySpec("S219", "Volume_Climax_Up",
                 {"vz_min": 3.0},
                 dte_target=3, dte_min=1, dte_max=7, option_type="call",
                 tp_pct=50.0, sl_pct=-50.0, launched_date="2026-07-26"),
]


def get_phase1_lab() -> StrategyLab:
    """Return a StrategyLab pre-loaded with Phase-1 specs (S200-S219)."""
    lab = StrategyLab()
    for spec in _PHASE1_SPECS:
        lab.add(spec)
    return lab


def load_or_init_lab() -> StrategyLab:
    """Load from registry JSON if it exists; otherwise seed from Phase-1 specs."""
    if _REGISTRY_PATH.exists():
        lab = StrategyLab.from_json()
        # Merge any Phase-1 specs not yet in file
        existing_ids = {s.strategy_id for s in lab.strategies}
        for spec in _PHASE1_SPECS:
            if spec.strategy_id not in existing_ids:
                lab.add(spec)
        return lab
    lab = get_phase1_lab()
    lab.save()
    return lab


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def _cmd_evaluate(args) -> int:
    return run_daily_evaluation()


def _cmd_list(args) -> int:
    lab = load_or_init_lab()
    print(f"{'ID':<8} {'Signal':<25} {'DTE':>3} {'Type':<5} {'Status'}")
    print("-" * 60)
    for s in sorted(lab.strategies, key=lambda x: x.strategy_id):
        print(f"{s.strategy_id:<8} {s.signal_name:<25} {s.dte_target:>3} "
              f"{s.option_type:<5} {s.status}")
    return 0


def _cmd_dump_registry(args) -> int:
    lab = load_or_init_lab()
    lab.save()
    print(f"Registry written to {_REGISTRY_PATH}")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Options strategy lab - framework manager")
    sub = parser.add_subparsers()

    p_eval = sub.add_parser("--evaluate", help="Run daily kill/promote evaluation")
    p_eval.set_defaults(func=_cmd_evaluate)

    p_list = sub.add_parser("--list", help="List all registered strategies")
    p_list.set_defaults(func=_cmd_list)

    p_dump = sub.add_parser("--dump-registry", help="Write strategy_registry.json")
    p_dump.set_defaults(func=_cmd_dump_registry)

    # Also allow bare --evaluate/--list/--dump-registry as top-level flags
    if argv is None:
        argv = sys.argv[1:]

    if argv and argv[0] in ("--evaluate", "-e"):
        return _cmd_evaluate(None)
    if argv and argv[0] in ("--list", "-l"):
        return _cmd_list(None)
    if argv and argv[0] in ("--dump-registry", "-d"):
        return _cmd_dump_registry(None)

    # Default: print help
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
