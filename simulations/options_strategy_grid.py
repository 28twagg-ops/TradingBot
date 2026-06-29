"""
options_strategy_grid.py
================================================================================
PHASE 3 machinery (Task 2.3 build) — the mass strategy-testing parameter grid.

DEVELOPMENT ONLY - NOT FOR TRADING DECISIONS.

This builds and exercises the full Phase 3 parameter grid on top of the
validated Phase 2 engine (options_strategy_simulator.py). It runs on the
SYNTHETIC development dataset because real Alpaca 1-minute data does not exist
yet (needs ~4 weeks of live collection). When that data arrives, swap the
signal source for `load_alpaca_dataset(...)` (already stubbed in the engine) and
the grid / aggregation / thresholds / leaderboard code below is unchanged.

What it produces (Master Plan v3, Section 4 + Section 7):
  - A ranked leaderboard of variants by Expected P&L per signal ($)
  - MAIN (>=50 filled) / SECONDARY (30-49) / EXCLUDED (<30) split
  - The 7 minimum-viability threshold checks per variant (Section 7)
  - Hold-period recommendation table per mechanic
  - Fill-behavior recommendation table per mechanic

The grid axes (Section 4 "PARAMETER GRID"):
  mechanic x strike(ATM/1OTM/2OTM) x expiry(1/3/7/14/30 DTE)
    x entry window(9:30-10 / 10-11 / 11-12) x exit(intraday/EOD/1day/3day)
    x fill behavior(cancel/widen/hold)

Run:
  python simulations/options_strategy_grid.py            # full grid (dev data)
  python simulations/options_strategy_grid.py --n 80     # fewer signals/variant
  python simulations/options_strategy_grid.py --quick    # tiny smoke run
"""

from __future__ import annotations

import argparse
import csv
import itertools
import math
import random
import sys
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_strategy_simulator import (  # noqa: E402
    SignalEvent, simulate_single_trade, aggregate, quote_from_underlying,
    MAX_CONTRACT_COST, DEV_LABEL,
)

# --------------------------------------------------------------------------- #
#  Grid axes
# --------------------------------------------------------------------------- #

# Representative mechanic archetypes. On SYNTHETIC data a "mechanic" only encodes
# a directional bias (right + drift); the real per-mechanic differentiation comes
# from real data in Phase 3. The library expands trivially (A1..E6) by adding
# entries here; the grid machinery is identical.
MECHANICS = {
    "A1_GapDownCall":    {"right": "C", "drift": 0.22},
    "A4_MorningRevCall": {"right": "C", "drift": 0.16},
    "A8_ORBCall":        {"right": "C", "drift": 0.13},
    "A3_GapUpPut":       {"right": "P", "drift": 0.22},
    "A7_VWAPRejPut":     {"right": "P", "drift": 0.14},
}

STRIKE_OFFSETS = {"ATM": 0.0, "OTM1": 0.015, "OTM2": 0.030}
DTE_DAYS = [1, 3, 7, 14, 30]
ENTRY_WINDOWS = {"0930-1000": 1.00, "1000-1100": 0.65, "1100-1200": 0.45}
EXIT_HOLD_MIN = {"intraday": 90, "EOD": 200, "1day": 390, "3day": 1170}
FILL_MODES = ["cancel", "widen", "hold"]

TRADING_MINUTES = 390
MINUTE_DT = 1.0 / (252 * TRADING_MINUTES)

# Section 7 — minimum viability thresholds
VT_MIN_EXP_PNL = 0.0
VT_MIN_FILL_RATE = 0.40
VT_MIN_SAMPLE = 50
VT_MAX_SPREAD = 0.20
VT_MAX_COST = MAX_CONTRACT_COST     # $75
VT_MIN_PROFIT_FACTOR = 1.2

RESULTS_DIR = Path(__file__).resolve().parent / "results" / "strategy_grid_dev"


# --------------------------------------------------------------------------- #
#  Synthetic signal generation for one variant
# --------------------------------------------------------------------------- #

def gen_variant_signals(mech: str, strike_key: str, dte: int, win_key: str,
                        exit_key: str, n: int, seed: int) -> list[SignalEvent]:
    rng = random.Random(seed)
    spec = MECHANICS[mech]
    right = spec["right"]
    drift = spec["drift"] * ENTRY_WINDOWS[win_key]     # edge decays later in morning
    if right == "P":
        drift = -abs(drift)                            # puts want downward move
    off = STRIKE_OFFSETS[strike_key]
    hold_min = EXIT_HOLD_MIN[exit_key]
    T = dte / 365.0

    sigs: list[SignalEvent] = []
    for i in range(n):
        # Underlying universe spread so liquidity filters bite for some contracts.
        S0 = rng.choice([10, 14, 18, 22, 28, 35, 45, 60, 90]) * rng.uniform(0.9, 1.1)
        iv = rng.choice([0.20, 0.24, 0.28, 0.35, 0.45]) * rng.uniform(0.95, 1.05)
        oi = rng.choice([40, 120, 300, 800, 2000])
        # OTM strike in the unfavorable direction for the option holder
        K = round(S0 * (1 + (off if right == "C" else -off)), 2)

        # GBM closed-form terminal draws (equivalent to stepping minute-by-minute
        # but O(1) instead of O(hold_min) — essential for the long-hold variants).
        S_signal = S0
        z1 = rng.gauss(0.0, 1.0)
        S_next = S_signal * math.exp(-0.5 * iv * iv * MINUTE_DT
                                     + iv * math.sqrt(MINUTE_DT) * z1)   # 1 window, mu=0
        T_hold = hold_min * MINUTE_DT
        z2 = rng.gauss(0.0, 1.0)
        S_exit = S_signal * math.exp((drift - 0.5 * iv * iv) * T_hold
                                     + iv * math.sqrt(T_hold) * z2)
        T_exit = max(0.0, T - T_hold)                          # may expire (clamped)

        sigs.append(SignalEvent(
            sig_id=i, sdate=str(date.today()), symbol=f"SYN{i % 50:02d}",
            mechanic=mech, right=right, strike=K, T_years=T, iv=iv,
            open_interest=oi, period=("A" if i % 2 == 0 else "B"),
            S_signal=S_signal, S_next=S_next, S_exit=S_exit, T_exit_years=T_exit,
        ))
    return sigs


# --------------------------------------------------------------------------- #
#  One variant -> metrics
# --------------------------------------------------------------------------- #

@dataclass
class VariantResult:
    mechanic: str
    strike: str
    dte: int
    entry_window: str
    exit_type: str
    fill_mode: str
    signals: int
    filled: int
    fill_rate: float
    win_rate: float
    profit_factor: float
    avg_spread_frac: float
    avg_entry_cost: float
    exp_pnl_per_signal: float
    total_pnl: float
    exp_pnl_A: float
    exp_pnl_B: float
    survives: bool
    fail_reasons: str

    @property
    def variant_id(self) -> str:
        return (f"{self.mechanic}|{self.strike}|{self.dte}DTE|{self.entry_window}"
                f"|{self.exit_type}|{self.fill_mode}")


def evaluate_variant(mech, strike_key, dte, win_key, exit_key, fill_mode,
                     n, seed) -> VariantResult:
    sigs = gen_variant_signals(mech, strike_key, dte, win_key, exit_key, n, seed)
    trades = [simulate_single_trade(s, fill_mode=fill_mode) for s in sigs]
    agg = aggregate(trades)

    filled = [t for t in trades if t.filled]
    # avg spread at signal + avg entry cost (filled only)
    sf, costs = [], []
    for s, t in zip(sigs, trades):
        if t.filled:
            q = quote_from_underlying(s.S_signal, s.strike, s.T_years,
                                      s.iv, s.open_interest, s.right)
            sf.append(q.spread_frac)
            costs.append(t.entry_cost)
    avg_spread = sum(sf) / len(sf) if sf else 9.99
    avg_cost = sum(costs) / len(costs) if costs else 0.0

    # period robustness (Section 7 #6): exp P&L per signal in BOTH halves
    def _exp(period):
        sub = [t for s, t in zip(sigs, trades) if s.period == period]
        return aggregate(sub)["exp_pnl_per_signal"] if sub else float("-inf")
    exp_A, exp_B = _exp("A"), _exp("B")

    pf = agg["profit_factor"]
    pf_val = pf if pf != float("inf") else 999.0
    n_fill = agg["filled"]

    # 7 viability thresholds
    fails = []
    if agg["exp_pnl_per_signal"] <= VT_MIN_EXP_PNL:
        fails.append("exp_pnl<=0")
    if agg["fill_rate"] < VT_MIN_FILL_RATE:
        fails.append("fill<40%")
    if n_fill < VT_MIN_SAMPLE:
        fails.append("sample<50")
    if avg_spread > VT_MAX_SPREAD:
        fails.append("spread>20%")
    if avg_cost > VT_MAX_COST:
        fails.append("cost>$75")
    if not (exp_A > 0 and exp_B > 0):
        fails.append("not_both_periods")
    if pf_val < VT_MIN_PROFIT_FACTOR:
        fails.append("pf<1.2")

    return VariantResult(
        mechanic=mech, strike=strike_key, dte=dte, entry_window=win_key,
        exit_type=exit_key, fill_mode=fill_mode, signals=len(sigs), filled=n_fill,
        fill_rate=agg["fill_rate"], win_rate=agg["win_rate"], profit_factor=pf_val,
        avg_spread_frac=avg_spread, avg_entry_cost=avg_cost,
        exp_pnl_per_signal=agg["exp_pnl_per_signal"], total_pnl=agg["total_pnl"],
        exp_pnl_A=exp_A, exp_pnl_B=exp_B,
        survives=not fails, fail_reasons=",".join(fails) if fails else "",
    )


# --------------------------------------------------------------------------- #
#  Run the grid
# --------------------------------------------------------------------------- #

def run_grid(n: int, quick: bool = False, focused: bool = False) -> list[VariantResult]:
    if focused:
        # VERDICT B preset (Task 2.0 preliminary): the edge is INTRADAY/EOD only and
        # strongest on strong signals. So prioritise same-day exits, ATM strikes, and
        # short DTE (morning scalps / Mechanic E style); DROP the 3/5-day holds that
        # the preliminary study showed do not beat control.
        # NOTE: the strong-signal filter (gap_pct < -2%, high vol_ratio) is a property
        # of REAL data and is applied in the Phase 3 real-data loader, not on synthetic.
        mechanics = list(MECHANICS)
        strikes = ["ATM"]
        dtes = [1, 3, 7]
        wins = list(ENTRY_WINDOWS)
        exits = ["intraday", "EOD"]
        fills = FILL_MODES
    elif quick:
        mechanics = list(MECHANICS)[:2]
        strikes = ["ATM"]
        dtes = [7]
        wins = ["0930-1000"]
        exits = ["intraday", "1day"]
        fills = ["cancel", "hold"]
    else:
        mechanics = list(MECHANICS)
        strikes = list(STRIKE_OFFSETS)
        dtes = DTE_DAYS
        wins = list(ENTRY_WINDOWS)
        exits = list(EXIT_HOLD_MIN)
        fills = FILL_MODES

    combos = list(itertools.product(mechanics, strikes, dtes, wins, exits, fills))
    total = len(combos)
    print(f"[{DEV_LABEL}]")
    print(f"Grid: {total} variants x {n} signals = {total*n:,} single-trade sims")
    results: list[VariantResult] = []
    t0 = time.monotonic()
    for idx, (mech, sk, dte, win, ex, fill) in enumerate(combos):
        seed = 1000 + idx                       # deterministic per variant
        results.append(evaluate_variant(mech, sk, dte, win, ex, fill, n, seed))
        if (idx + 1) % 250 == 0:
            el = time.monotonic() - t0
            print(f"  {idx+1}/{total} variants ({el:.1f}s)")
        if time.monotonic() - t0 > 55 * 60:     # RH-4 safety
            print("  RUNTIME GUARD hit (55 min) - stopping early")
            break
    print(f"  done {len(results)} variants in {time.monotonic()-t0:.1f}s")
    return results


# --------------------------------------------------------------------------- #
#  Recommendation tables (per mechanic)
# --------------------------------------------------------------------------- #

def best_by(results, group_field) -> dict:
    """For each (mechanic, group_field value), mean exp_pnl_per_signal; pick best."""
    buckets: dict = {}
    for r in results:
        key = (r.mechanic, getattr(r, group_field))
        buckets.setdefault(key, []).append(r.exp_pnl_per_signal)
    table: dict = {}
    for (mech, val), xs in buckets.items():
        table.setdefault(mech, {})[val] = sum(xs) / len(xs)
    reco = {mech: max(d, key=d.get) for mech, d in table.items()}
    return {"table": table, "best": reco}


# --------------------------------------------------------------------------- #
#  Output
# --------------------------------------------------------------------------- #

def save_outputs(results: list[VariantResult], n: int,
                 focused: bool = False) -> tuple[int, int, int, int]:
    out_dir = (RESULTS_DIR / "focused") if focused else RESULTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    # full leaderboard csv (ranked by exp pnl per signal)
    ranked = sorted(results, key=lambda r: r.exp_pnl_per_signal, reverse=True)
    fields = ["variant_id", "mechanic", "strike", "dte", "entry_window",
              "exit_type", "fill_mode", "signals", "filled", "fill_rate",
              "win_rate", "profit_factor", "avg_spread_frac", "avg_entry_cost",
              "exp_pnl_per_signal", "total_pnl", "exp_pnl_A", "exp_pnl_B",
              "survives", "fail_reasons"]
    with open(out_dir / "options_leaderboard_dev.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in ranked:
            row = {k: getattr(r, k) for k in fields if k != "variant_id"}
            row["variant_id"] = r.variant_id
            w.writerow(row)

    main = [r for r in ranked if r.filled >= 50]
    secondary = [r for r in ranked if 30 <= r.filled < 50]
    excluded = [r for r in ranked if r.filled < 30]
    survivors = [r for r in main if r.survives]

    hold = best_by(results, "exit_type")
    fillb = best_by(results, "fill_mode")

    with open(out_dir / "hold_period_reco_dev.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["mechanic"] + list(EXIT_HOLD_MIN) + ["best"])
        for mech, d in hold["table"].items():
            w.writerow([mech] + [f"{d.get(k, float('nan')):.4f}" for k in EXIT_HOLD_MIN]
                       + [hold["best"][mech]])
    with open(out_dir / "fill_behavior_reco_dev.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["mechanic"] + FILL_MODES + ["best"])
        for mech, d in fillb["table"].items():
            w.writerow([mech] + [f"{d.get(k, float('nan')):.4f}" for k in FILL_MODES]
                       + [fillb["best"][mech]])

    _write_report(ranked, main, secondary, excluded, survivors, hold, fillb, n, out_dir)
    return len(main), len(secondary), len(excluded), len(survivors)


def _write_report(ranked, main, secondary, excluded, survivors, hold, fillb, n, out_dir):
    L = ["# Options Strategy Grid — Leaderboard (Phase 3 dry-run)", "",
         f"_{DEV_LABEL}_", "",
         f"Generated: {date.today().isoformat()}",
         "Engine: `simulations/options_strategy_simulator.py` (Gate 2A validated).",
         "Data: SYNTHETIC development dataset (Black-Scholes + adversarial spread "
         "model). NOT real edge — swap in Alpaca 1-min data for the production run.",
         f"Signals per variant: {n}.", "",
         "## Grid summary", "",
         f"- Total variants: {len(ranked)}",
         f"- MAIN (>=50 filled): {len(main)}",
         f"- SECONDARY (30-49 filled): {len(secondary)}",
         f"- EXCLUDED (<30 filled): {len(excluded)}",
         f"- **Survived all 7 viability thresholds: {len(survivors)}**", "",
         "## Section 7 viability thresholds applied", "",
         f"1. Expected P&L/signal > $0  2. Fill rate >= {VT_MIN_FILL_RATE:.0%}  "
         f"3. Sample >= {VT_MIN_SAMPLE}  4. Avg spread <= {VT_MAX_SPREAD:.0%}  "
         f"5. Cost <= ${VT_MAX_COST:.0f}  6. Holds in BOTH periods  "
         f"7. Profit factor >= {VT_MIN_PROFIT_FACTOR}", "",
         "## MAIN leaderboard — top 15 (>=50 filled, ranked by Exp P&L/signal)", "",
         "| Rank | Variant | ExpP&L/sig | Fill | Win | PF | Spread | Survives |",
         "|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(main[:15], 1):
        L.append(f"| {i} | {r.variant_id} | ${r.exp_pnl_per_signal:+.2f} | "
                 f"{r.fill_rate:.0%} | {r.win_rate:.0%} | {r.profit_factor:.2f} | "
                 f"{r.avg_spread_frac:.0%} | {'YES' if r.survives else 'no'} |")
    L += ["", f"## Survivors (all 7 thresholds): {len(survivors)}", ""]
    if survivors:
        L += ["| Variant | ExpP&L/sig | Fill | PF | A | B |",
              "|---|---|---|---|---|---|"]
        for r in survivors[:25]:
            L.append(f"| {r.variant_id} | ${r.exp_pnl_per_signal:+.2f} | "
                     f"{r.fill_rate:.0%} | {r.profit_factor:.2f} | "
                     f"${r.exp_pnl_A:+.2f} | ${r.exp_pnl_B:+.2f} |")
    else:
        L.append("_No variant survived all 7 thresholds on synthetic data. This is "
                 "EXPECTED and fine — synthetic edges are deliberately small and the "
                 "purpose here is to exercise the machinery, not find real winners._")
    L += ["", "## Hold-period recommendation per mechanic (mean Exp P&L/signal)", "",
          "| Mechanic | " + " | ".join(EXIT_HOLD_MIN) + " | BEST |",
          "|---|" + "---|" * (len(EXIT_HOLD_MIN) + 1)]
    for mech, d in hold["table"].items():
        L.append(f"| {mech} | " + " | ".join(f"${d.get(k, float('nan')):+.2f}"
                 for k in EXIT_HOLD_MIN) + f" | {hold['best'][mech]} |")
    L += ["", "## Fill-behavior recommendation per mechanic (mean Exp P&L/signal)", "",
          "| Mechanic | " + " | ".join(FILL_MODES) + " | BEST |",
          "|---|" + "---|" * (len(FILL_MODES) + 1)]
    for mech, d in fillb["table"].items():
        L.append(f"| {mech} | " + " | ".join(f"${d.get(k, float('nan')):+.2f}"
                 for k in FILL_MODES) + f" | {fillb['best'][mech]} |")
    L += ["", "_Note: these two tables average Exp P&L/signal across ALL parameter "
          "combinations for each mechanic, so they are dominated by the many "
          "negative-edge (short-hold) combos — that is why `cancel` (trade less) "
          "tends to win the MEAN. Among the positive-edge variants on the "
          "leaderboard the opposite holds: higher-fill modes (`widen`/`hold`) "
          "compound a real edge and rank at the top. On real data, read the "
          "per-variant leaderboard, not just these marginal means._",
          "", "## What this proves (and does not)", "",
          "- PROVES: the Phase 3 grid machinery works end-to-end — it sweeps every "
          "axis, applies the adversarial engine, computes the Section 4 key metric, "
          "enforces the Section 7 thresholds, and produces ranked leaderboards + "
          "hold-period / fill-behavior recommendations.",
          "- DOES NOT PROVE: any real strategy edge. Synthetic drifts are arbitrary. "
          "The production leaderboard requires ~4 weeks of Alpaca 1-min data via "
          "`load_alpaca_dataset(...)`; only then are rankings meaningful.",
          f"- {DEV_LABEL}"]
    (out_dir / "strategy_grid_report_dev.md").write_text("\n".join(L), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Phase 3 strategy grid (dev data)")
    ap.add_argument("--n", type=int, default=1000, help="signals per variant")
    ap.add_argument("--quick", action="store_true", help="tiny smoke grid")
    ap.add_argument("--focused", action="store_true",
                    help="Verdict B preset: intraday/EOD exits, ATM, short DTE only")
    args = ap.parse_args()

    results = run_grid(args.n, quick=args.quick, focused=args.focused)
    nmain, nsec, nexc, nsurv = save_outputs(results, args.n, focused=args.focused)
    print(f"\nLeaderboard: MAIN={nmain} SECONDARY={nsec} EXCLUDED={nexc} "
          f"SURVIVORS={nsurv}")
    print(f"Outputs: {RESULTS_DIR}")
    print(f"STATUS: grid machinery OK (DEV data). {len(results)} variants ranked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
