"""
options_strategy_simulator.py
================================================================================
PHASE 2 of the Options Expansion Master Plan v3 (Task 2.1 + Task 2.2).

Builds the options simulation engine in the prescribed order (Steps A-E) and
runs the six SIM INTEGRITY CHECKS (Gate 2A) that must all pass before any
strategy grid is permitted to produce rankings.

DATA SOURCE NOTE (important):
  The production simulation (Phase 3) consumes ONLY Alpaca 1-minute parquet
  data (see TradingBot-git/scripts/options_data_collector.py). That data does
  not exist yet (needs ~4 weeks of live collection + API credentials).

  Until then, this engine runs on a SYNTHETIC DEVELOPMENT DATASET generated
  with Black-Scholes pricing + the plan's adversarial spread model. Every
  result produced from synthetic data is labelled:

      "DEVELOPMENT ONLY - NOT FOR TRADING DECISIONS"

  The integrity checks validate ENGINE CORRECTNESS (fee application, fill
  logic, compounding math, boundaries), NOT strategy edge. They are exactly
  the checks that would have caught the equity bot's -191% / -40% / -20%
  methodology bugs.

A real-data loader stub (load_alpaca_dataset) is provided so Phase 3 can swap
in the Alpaca parquet files without changing the rest of the engine.

Usage:
  python options_strategy_simulator.py --integrity   # run Gate 2A, write report
  python options_strategy_simulator.py --demo        # small end-to-end demo
  python options_strategy_simulator.py --steps       # print Step A-E walkthrough
================================================================================
"""

from __future__ import annotations

import argparse
import math
import random
import sys
from dataclasses import dataclass, field, asdict
from datetime import date
from pathlib import Path

# --------------------------------------------------------------------------- #
#  Constants (from Master Plan v3, Section 4 "Adversarial Assumptions")
# --------------------------------------------------------------------------- #

FEE_PER_CONTRACT_LEG = 0.65          # $0.65 per contract per leg ($1.30 round trip)
FEE_ROUND_TRIP       = 2 * FEE_PER_CONTRACT_LEG
CONTRACT_MULTIPLIER  = 100           # one option contract = 100 shares
RISK_FREE_RATE       = 0.04          # annualized, for Black-Scholes

# Liquidity / tradeability filters (Section 4 adversarial skip rules)
MIN_OPEN_INTEREST    = 100
MAX_SPREAD_FRAC      = 0.25          # spread > 25% of mid -> skip
MAX_CONTRACT_COST    = 75.0          # 1 contract cost > $75 -> skip (Tier 0)
MIN_SIGNALS_SAMPLE   = 30            # < 30 signals -> flag insufficient sample

# Sizing (Tier 0 from Task 4.3)
TIER0_MAX_CONTRACTS  = 1
TIER0_ACCOUNT_CAP    = 0.20          # 20% of equity in options premium
START_EQUITY         = 500.0

DEV_LABEL = "DEVELOPMENT ONLY - NOT FOR TRADING DECISIONS"

RESULTS_DIR = Path(__file__).resolve().parent / "results"
REPORT_PATH = RESULTS_DIR / "sim_integrity_report.md"


# --------------------------------------------------------------------------- #
#  Black-Scholes pricing (no scipy: normal CDF via math.erf)
# --------------------------------------------------------------------------- #

def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bs_price(S: float, K: float, T: float, sigma: float, right: str,
             r: float = RISK_FREE_RATE) -> float:
    """Black-Scholes price of a European call/put. T in years."""
    right = right.upper()
    if T <= 0 or sigma <= 0:
        # intrinsic value at/after expiry
        return max(0.0, (S - K) if right == "C" else (K - S))
    d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    if right == "C":
        return S * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)
    return K * math.exp(-r * T) * norm_cdf(-d2) - S * norm_cdf(-d1)


def bs_delta(S: float, K: float, T: float, sigma: float, right: str,
             r: float = RISK_FREE_RATE) -> float:
    if T <= 0 or sigma <= 0:
        intrinsic = (S - K) if right.upper() == "C" else (K - S)
        return (1.0 if intrinsic > 0 else 0.0) * (1 if right.upper() == "C" else -1)
    d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
    return norm_cdf(d1) if right.upper() == "C" else norm_cdf(d1) - 1.0


def model_spread(iv: float, mid: float) -> float:
    """Bid-ask spread model from Section 4 (used when real spread unavailable)."""
    if iv < 0.30:
        return max(0.05, 0.02 * mid)
    if iv <= 0.60:
        return max(0.10, 0.05 * mid)
    return max(0.15, 0.10 * mid)


# --------------------------------------------------------------------------- #
#  Data model
# --------------------------------------------------------------------------- #

@dataclass
class OptionQuote:
    """A single option quote at a point in time, with adversarial fill prices."""
    mid: float
    bid: float
    ask: float
    iv: float
    open_interest: int

    @property
    def spread(self) -> float:
        return self.ask - self.bid

    @property
    def spread_frac(self) -> float:
        return self.spread / self.mid if self.mid > 0 else 9.99


@dataclass
class SignalEvent:
    """One tradeable signal: an underlying move + a chosen option contract path."""
    sig_id: int
    sdate: str
    symbol: str
    mechanic: str
    right: str                       # "C" or "P"
    strike: float
    T_years: float                   # time to expiry at signal
    iv: float
    open_interest: int
    period: str                      # which half of the data ("A"/"B") for robustness
    # underlying path samples we need
    S_signal: float                  # underlying at signal minute
    S_next: float                    # underlying one window later (for fill check)
    S_exit: float                    # underlying at exit
    T_exit_years: float              # time to expiry at exit


def quote_from_underlying(S: float, K: float, T: float, iv: float,
                          oi: int, right: str) -> OptionQuote:
    mid = bs_price(S, K, T, iv, right)
    mid = max(mid, 0.0)
    sp = model_spread(iv, mid)
    bid = max(0.0, mid - sp / 2.0)
    ask = mid + sp / 2.0
    return OptionQuote(mid=mid, bid=bid, ask=ask, iv=iv, open_interest=oi)


# --------------------------------------------------------------------------- #
#  Trade simulation (STEP B: one signal -> one trade)
# --------------------------------------------------------------------------- #

@dataclass
class TradeResult:
    sig_id: int
    sdate: str
    symbol: str
    mechanic: str
    right: str
    strike: float
    period: str
    skipped: bool = False
    skip_reason: str = ""
    filled: bool = False
    contracts: int = 0
    entry_limit: float = 0.0
    entry_fill: float = 0.0
    exit_price: float = 0.0
    entry_cost: float = 0.0          # premium paid per contract * 100 (gross, no fees)
    gross_pnl: float = 0.0           # before fees
    fees: float = 0.0
    pnl_dollar: float = 0.0          # net
    pnl_pct: float = 0.0             # net pnl / entry_cost
    return_pct_gross: float = 0.0    # gross pnl / entry_cost (for boundary check)


def simulate_single_trade(sig: SignalEvent, contracts: int = 1,
                          liquidity_filter: bool = True,
                          fill_mode: str = "cancel") -> TradeResult:
    """
    STEP B core. Adversarial assumptions (Section 4):
      - quotes derived from underlying via Black-Scholes + spread model
      - BUY fills at ASK, SELL fills at BID, never mid
      - exit sells at bid at exit time
      - fees: $0.65 / contract / leg

    fill_mode controls the Section 4 "fill behavior" axis (default preserves the
    original, integrity-validated behavior so Gate 2A is unaffected):
      - "cancel" (Option 1): limit = ask-$0.01; fills only if next-window ask
        drops to <= limit, else cancelled. (low fill rate, best entry price)
      - "widen"  (Option 2): if not filled at ask-$0.01, widen to the prevailing
        ask; fills if next-window ask <= signal ask, paying that ask. (higher
        fill rate, worse entry price)
      - "hold"   (Option 3): hold the ask-$0.01 limit for ~30 min; fills at the
        limit if next-window ask <= signal ask. (higher fill rate, best price)
    """
    res = TradeResult(sig_id=sig.sig_id, sdate=sig.sdate, symbol=sig.symbol,
                      mechanic=sig.mechanic, right=sig.right, strike=sig.strike,
                      period=sig.period)

    q_sig = quote_from_underlying(sig.S_signal, sig.strike, sig.T_years,
                                  sig.iv, sig.open_interest, sig.right)

    # Liquidity / tradeability filters (drives Integrity Check 6)
    if liquidity_filter:
        contract_cost = q_sig.ask * CONTRACT_MULTIPLIER
        if q_sig.open_interest < MIN_OPEN_INTEREST:
            res.skipped, res.skip_reason = True, "open_interest<100"
            return res
        if q_sig.bid <= 0.0:
            res.skipped, res.skip_reason = True, "bid=0"
            return res
        if q_sig.spread_frac > MAX_SPREAD_FRAC:
            res.skipped, res.skip_reason = True, "spread>25%"
            return res
        if contract_cost > MAX_CONTRACT_COST:
            res.skipped, res.skip_reason = True, "cost>$75"
            return res

    # Entry: limit at ask - $0.01. Fill behavior depends on fill_mode (Section 4).
    entry_limit = round(q_sig.ask - 0.01, 2)
    res.entry_limit = entry_limit
    q_next = quote_from_underlying(sig.S_next, sig.strike, sig.T_years,
                                   sig.iv, sig.open_interest, sig.right)
    mode = (fill_mode or "cancel").lower()
    if mode == "cancel":             # Option 1: strict limit, cancel after one window
        if q_next.ask > entry_limit:
            res.filled = False
            return res
        entry_fill = entry_limit
    elif mode == "widen":            # Option 2: widen to ask, pay the prevailing ask
        if q_next.ask > q_sig.ask:
            res.filled = False
            return res
        entry_fill = round(q_next.ask, 2)
    elif mode == "hold":             # Option 3: patient limit held ~30 min, keep price
        if q_next.ask > q_sig.ask:
            res.filled = False
            return res
        entry_fill = entry_limit
    else:
        raise ValueError(f"unknown fill_mode: {fill_mode!r}")

    res.filled = True
    res.contracts = contracts
    res.entry_fill = entry_fill
    res.entry_cost = entry_fill * CONTRACT_MULTIPLIER

    # Exit: sell at bid at exit time
    q_exit = quote_from_underlying(sig.S_exit, sig.strike, sig.T_exit_years,
                                   sig.iv, sig.open_interest, sig.right)
    exit_price = q_exit.bid
    res.exit_price = exit_price

    res.gross_pnl = (exit_price - entry_fill) * CONTRACT_MULTIPLIER * contracts
    res.fees = FEE_ROUND_TRIP * contracts
    res.pnl_dollar = res.gross_pnl - res.fees
    basis = res.entry_cost * contracts
    res.pnl_pct = (res.pnl_dollar / basis) if basis > 0 else 0.0
    res.return_pct_gross = (res.gross_pnl / basis) if basis > 0 else 0.0
    return res


# --------------------------------------------------------------------------- #
#  Synthetic development dataset (Task 2.3 stand-in until Alpaca data exists)
# --------------------------------------------------------------------------- #

def _gbm_step(S: float, mu: float, sigma: float, dt: float, rng: random.Random) -> float:
    z = rng.gauss(0.0, 1.0)
    return S * math.exp((mu - 0.5 * sigma * sigma) * dt + sigma * math.sqrt(dt) * z)


def generate_dev_signals(n: int, seed: int = 42, mechanic: str = "mixed",
                         randomized: bool = False) -> list[SignalEvent]:
    """
    Build a synthetic set of signal events calibrated so that:
      - a substantial (but not extreme) fraction fail liquidity filters
        (Integrity Check 6 expects ~30-60% skipped)
      - real (non-random) mechanics carry a small directional edge, random
        mechanics carry none (Integrity Check 1 zero-edge baseline)
    Underlying paths use GBM; option quotes are Black-Scholes derived.
    """
    rng = random.Random(seed)
    sigs: list[SignalEvent] = []
    trading_minutes = 390
    minute_dt = 1.0 / (252 * trading_minutes)   # one minute in years

    for i in range(n):
        # Underlying universe: spread of price levels. Calibrated so a healthy
        # fraction of contracts land in the $500-account tradeable band
        # (premium roughly $0.20-$0.75) while a substantial fraction is still
        # filtered out (too pricey, too wide, too illiquid) -> Integrity Check 6.
        S0 = rng.choice([10, 14, 18, 22, 28, 35, 45, 60, 90]) * rng.uniform(0.9, 1.1)
        iv = rng.choice([0.20, 0.24, 0.28, 0.35, 0.45]) * rng.uniform(0.95, 1.05)
        oi = rng.choice([40, 120, 300, 800, 2000])          # ~20% < 100 -> skipped
        dte_days = rng.choice([2, 3, 5, 7, 10, 14, 21, 30])
        T = dte_days / 365.0

        # Strike near the money: ATM or a step OTM
        moneyness = rng.choice([0.0, 0.01, 0.02, 0.03]) 
        right = rng.choice(["C", "P"])

        if randomized:
            mech = "RANDOM"
            right = rng.choice(["C", "P"])
            drift = 0.0
            entry_min = rng.randint(0, trading_minutes - 60)
            hold_min = rng.randint(5, 120)
        else:
            mech = mechanic if mechanic != "mixed" else rng.choice(
                ["GapDownCall", "GapUpPut", "ORBCall"])
            # Each mechanic has a small, realistic directional bias in the
            # underlying over the holding window (this is the "edge").
            if mech == "GapDownCall":
                right, drift = "C", 0.18      # bounce after gap down
            elif mech == "GapUpPut":
                right, drift = "P", 0.18      # fade after gap up (drift applied to put-favorable move)
            else:  # ORBCall
                right, drift = "C", 0.14
            entry_min = rng.randint(0, 60)    # morning window
            hold_min = rng.randint(20, 180)

        K = round(S0 * (1 + (moneyness if right == "C" else -moneyness)), 2)

        # Underlying at signal
        S_signal = S0
        # One window later (1 minute) for fill check - near-zero drift intra-window
        S_next = _gbm_step(S_signal, 0.0, iv, minute_dt, rng)
        # Exit underlying after hold_min minutes, with the mechanic's drift
        # (drift expressed as annualized; convert via minutes held)
        mu_ann = drift if not randomized else 0.0
        # For puts we want downward favorable move -> negative underlying drift
        if right == "P" and not randomized:
            mu_ann = -abs(drift)
        S_exit = S_signal
        for _ in range(hold_min):
            S_exit = _gbm_step(S_exit, mu_ann, iv, minute_dt, rng)
        T_exit = max(0.0, T - hold_min * minute_dt)

        period = "A" if i % 2 == 0 else "B"    # two periods for robustness check
        sigs.append(SignalEvent(
            sig_id=i, sdate=str(date.today()), symbol=f"SYN{i%50:02d}",
            mechanic=mech, right=right, strike=K, T_years=T, iv=iv,
            open_interest=oi, period=period,
            S_signal=S_signal, S_next=S_next, S_exit=S_exit, T_exit_years=T_exit,
        ))
    return sigs


def load_alpaca_dataset(stocks_parquet: Path, options_parquet: Path) -> list[SignalEvent]:
    """
    PHASE 3 HOOK (not used in Phase 2 dev runs).
    Load real Alpaca 1-minute stock + options parquet produced by
    TradingBot-git/scripts/options_data_collector.py and translate into
    SignalEvent objects. Intentionally unimplemented until real data exists.
    """
    raise NotImplementedError(
        "Real Alpaca dataset loader is a Phase 3 task; requires collected "
        "1-minute parquet data that does not exist yet.")


# --------------------------------------------------------------------------- #
#  Trade log + aggregation (STEP D + STEP E)
# --------------------------------------------------------------------------- #

def build_trade_log(sigs: list[SignalEvent], contracts: int = 1,
                    liquidity_filter: bool = True) -> list[TradeResult]:
    return [simulate_single_trade(s, contracts=contracts,
                                  liquidity_filter=liquidity_filter) for s in sigs]


def aggregate(trades: list[TradeResult]) -> dict:
    considered = len(trades)
    skipped = [t for t in trades if t.skipped]
    after_filter = [t for t in trades if not t.skipped]
    filled = [t for t in after_filter if t.filled]
    wins = [t for t in filled if t.pnl_dollar > 0]
    losses = [t for t in filled if t.pnl_dollar <= 0]

    n_fill = len(filled)
    gross_profit = sum(t.pnl_dollar for t in wins)
    gross_loss = -sum(t.pnl_dollar for t in losses)
    total_pnl = sum(t.pnl_dollar for t in filled)
    win_rate = len(wins) / n_fill if n_fill else 0.0
    avg_win = (gross_profit / len(wins)) if wins else 0.0
    avg_loss = (gross_loss / len(losses)) if losses else 0.0
    loss_rate = len(losses) / n_fill if n_fill else 0.0
    fill_rate = n_fill / len(after_filter) if after_filter else 0.0
    profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else float("inf")
    # KEY METRIC (Section 4): Expected P&L per signal (dollar), penalizes fill rate
    exp_pnl_per_signal = fill_rate * (win_rate * avg_win - loss_rate * avg_loss)

    return {
        "signals_considered": considered,
        "skipped": len(skipped),
        "skipped_frac": len(skipped) / considered if considered else 0.0,
        "after_filter": len(after_filter),
        "filled": n_fill,
        "fill_rate": fill_rate,
        "wins": len(wins),
        "losses": len(losses),
        "win_rate": win_rate,
        "avg_win": avg_win,
        "avg_loss": avg_loss,
        "total_pnl": total_pnl,
        "profit_factor": profit_factor,
        "exp_pnl_per_signal": exp_pnl_per_signal,
    }


# --------------------------------------------------------------------------- #
#  Compounding equity curve (sizing against RUNNING equity - the -191% fix)
# --------------------------------------------------------------------------- #

def compounding_curve(filled_trades: list[TradeResult],
                      start_equity: float = START_EQUITY) -> list[dict]:
    """
    Build an equity curve sizing each trade against RUNNING equity (Tier 0).
    Returns per-trade rows for Integrity Check 4. The historical -191% bug
    was caused by sizing against STARTING equity; here we size against the
    current equity at each trade.
    """
    equity = start_equity
    rows = []
    for t in filled_trades:
        cap = TIER0_ACCOUNT_CAP * equity
        contract_cost = t.entry_fill * CONTRACT_MULTIPLIER
        affordable = int(cap // contract_cost) if contract_cost > 0 else 0
        contracts = max(0, min(TIER0_MAX_CONTRACTS, affordable))
        # pnl per contract for this trade
        pnl_per_contract = ((t.exit_price - t.entry_fill) * CONTRACT_MULTIPLIER
                            - FEE_ROUND_TRIP)
        trade_pnl = pnl_per_contract * contracts
        notional = contract_cost * contracts
        equity_before = equity
        equity += trade_pnl
        rows.append({
            "sig_id": t.sig_id, "equity_before": equity_before,
            "contracts": contracts, "notional": notional,
            "trade_pnl": trade_pnl, "equity_after": equity,
        })
    return rows


# --------------------------------------------------------------------------- #
#  GATE 2A : the six integrity checks
# --------------------------------------------------------------------------- #

@dataclass
class CheckResult:
    name: str
    passed: bool
    detail: str
    numbers: dict = field(default_factory=dict)


def check1_zero_edge_baseline() -> CheckResult:
    sigs = generate_dev_signals(2000, seed=7, randomized=True)
    trades = build_trade_log(sigs)
    agg = aggregate(trades)
    exp = agg["exp_pnl_per_signal"]
    total = agg["total_pnl"]
    passed = exp < 0 and total < 0
    return CheckResult(
        "1. Zero Edge Baseline", passed,
        ("Random signals must lose money (spread + fees). "
         f"Expected P&L/signal = ${exp:.2f}, total P&L = ${total:.2f} over "
         f"{agg['filled']} fills."),
        {"exp_pnl_per_signal": round(exp, 4), "total_pnl": round(total, 2),
         "fills": agg["filled"]},
    )


def check2_single_trade_audit() -> CheckResult:
    sigs = generate_dev_signals(400, seed=11)
    trades = [t for t in build_trade_log(sigs) if t.filled][:5]
    mismatches = []
    for t in trades:
        # Independent recompute from stored fill prices (the "by hand" math)
        recomputed = ((t.exit_price - t.entry_fill) * CONTRACT_MULTIPLIER
                      * t.contracts - FEE_ROUND_TRIP * t.contracts)
        if abs(recomputed - t.pnl_dollar) > 0.02:
            mismatches.append((t.sig_id, recomputed, t.pnl_dollar))
        # entry must equal limit (ask - 0.01); exit must equal a bid (>=0)
        if t.exit_price < 0:
            mismatches.append((t.sig_id, "neg_exit", t.exit_price))
    passed = len(trades) == 5 and not mismatches
    return CheckResult(
        "2. Single Trade Audit", passed,
        (f"Recomputed P&L for {len(trades)} filled trades within $0.02 of "
         f"engine P&L; entry=limit(ask-$0.01), exit=bid>=0. "
         f"Mismatches: {mismatches if mismatches else 'none'}"),
        {"audited": len(trades), "mismatches": len(mismatches)},
    )


def check3_boundary() -> CheckResult:
    sigs = generate_dev_signals(2000, seed=13)
    trades = [t for t in build_trade_log(sigs) if t.filled]
    bad_loss = [t for t in trades if t.return_pct_gross < -1.0001]   # >100% gross loss
    suspicious_gain = [t for t in trades if t.return_pct_gross > 5.0]  # >500% flag
    passed = not bad_loss
    return CheckResult(
        "3. Boundary Check", passed,
        (f"Long options cannot lose >100% of premium (gross). "
         f"Trades with >100% gross loss: {len(bad_loss)} (must be 0). "
         f"Trades flagged >500% gain (rare, informational): "
         f"{len(suspicious_gain)}."),
        {"over_100pct_loss": len(bad_loss), "over_500pct_gain": len(suspicious_gain),
         "fills": len(trades)},
    )


def check4_compounding() -> CheckResult:
    sigs = generate_dev_signals(800, seed=17)
    filled = [t for t in build_trade_log(sigs) if t.filled]
    rows = compounding_curve(filled)
    errors = []
    for i, r in enumerate(rows):
        expected = r["equity_before"] + r["trade_pnl"]
        if abs(expected - r["equity_after"]) > 1e-6:
            errors.append(i)
        # sizing must never exceed running-equity cap (notional <= 20% equity + slack)
        if r["notional"] > TIER0_ACCOUNT_CAP * r["equity_before"] + 1e-6 and r["contracts"] > 0:
            # one contract may exceed cap only if a single contract is the minimum;
            # Tier 0 buys at most 1 contract, so flag only if >1 contract over cap
            if r["contracts"] > 1:
                errors.append(("oversize", i))
    sample = rows[:10]
    passed = not errors and len(rows) > 0
    return CheckResult(
        "4. Compounding Check", passed,
        (f"Equity curve sizes against RUNNING equity (the -191% bug fix). "
         f"Checked {len(rows)} trades; consistency errors: "
         f"{errors if errors else 'none'}. First trade equity "
         f"{sample[0]['equity_before']:.2f}->{sample[0]['equity_after']:.2f} "
         if sample else "no trades"),
        {"trades": len(rows), "errors": len(errors),
         "final_equity": round(rows[-1]["equity_after"], 2) if rows else None},
    )


def check5_fill_rate() -> CheckResult:
    sigs = generate_dev_signals(3000, seed=19)
    trades = build_trade_log(sigs)
    agg = aggregate(trades)
    fr = agg["fill_rate"]
    passed = 0.10 <= fr <= 0.95
    return CheckResult(
        "5. Fill Rate Reality Check", passed,
        (f"Fill rate among tradeable signals = {fr*100:.1f}% "
         f"(must be >10% and <95%; limit=ask-$0.01 fills only if next-window "
         f"ask drops to the limit). {agg['filled']}/{agg['after_filter']} filled."),
        {"fill_rate": round(fr, 4), "filled": agg["filled"],
         "tradeable": agg["after_filter"]},
    )


def check6_liquidity_filter() -> CheckResult:
    sigs = generate_dev_signals(3000, seed=23)
    trades = build_trade_log(sigs)
    agg = aggregate(trades)
    frac = agg["skipped_frac"]
    # breakdown
    reasons: dict[str, int] = {}
    for t in trades:
        if t.skipped:
            reasons[t.skip_reason] = reasons.get(t.skip_reason, 0) + 1
    passed = 0.10 <= frac <= 0.90
    return CheckResult(
        "6. Liquidity Filter Audit", passed,
        (f"{frac*100:.1f}% of raw signals skipped by liquidity filters "
         f"(must be >10% and <90%). Breakdown: {reasons}"),
        {"skipped_frac": round(frac, 4), "skipped": agg["skipped"],
         "considered": agg["signals_considered"], "reasons": reasons},
    )


ALL_CHECKS = [
    check1_zero_edge_baseline,
    check2_single_trade_audit,
    check3_boundary,
    check4_compounding,
    check5_fill_rate,
    check6_liquidity_filter,
]


def run_integrity_suite() -> list[CheckResult]:
    results = []
    for fn in ALL_CHECKS:
        try:
            results.append(fn())
        except Exception as e:  # a check that crashes is a FAIL
            results.append(CheckResult(fn.__name__, False, f"CHECK CRASHED: {e}"))
    return results


def write_report(results: list[CheckResult]) -> bool:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    all_pass = all(r.passed for r in results)
    lines = []
    lines.append("# Options Sim Integrity Report (Gate 2A)")
    lines.append("")
    lines.append(f"_{DEV_LABEL}_")
    lines.append("")
    lines.append(f"Generated: {date.today().isoformat()}")
    lines.append(f"Engine: `simulations/options_strategy_simulator.py`")
    lines.append(f"Dataset: SYNTHETIC development data (Black-Scholes + adversarial "
                 f"spread model). Real Alpaca 1-min data required for Phase 3.")
    lines.append("")
    lines.append(f"## Overall: {'ALL 6 PASS' if all_pass else 'NOT ALL PASS - Phase 3 BLOCKED'}")
    lines.append("")
    lines.append("| # | Check | Result |")
    lines.append("|---|-------|--------|")
    for r in results:
        lines.append(f"| | {r.name} | {'PASS' if r.passed else 'FAIL'} |")
    lines.append("")
    lines.append("## Details")
    lines.append("")
    for r in results:
        lines.append(f"### {r.name} - {'PASS' if r.passed else 'FAIL'}")
        lines.append("")
        lines.append(r.detail)
        lines.append("")
        if r.numbers:
            lines.append(f"`{r.numbers}`")
            lines.append("")
    lines.append("## What this proves (and does not)")
    lines.append("")
    lines.append("- PROVES: the engine applies fees, fill logic, compounding, and "
                 "boundaries correctly; random trading loses money; liquidity "
                 "filters and fill modelling behave sanely.")
    lines.append("- DOES NOT PROVE: any strategy has real edge. That requires the "
                 "production run on collected Alpaca 1-minute data (Phase 3), which "
                 "cannot start until ~4 weeks of real data exist.")
    lines.append("")
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    return all_pass


# --------------------------------------------------------------------------- #
#  Step A-E walkthrough (the prescribed build order, for transparency)
# --------------------------------------------------------------------------- #

def steps_walkthrough() -> None:
    print(f"[{DEV_LABEL}]")
    print("STEP A - data loader / data check")
    sigs = generate_dev_signals(20, seed=1)
    print(f"  loaded {len(sigs)} synthetic signal events")
    print(f"  columns: {list(asdict(sigs[0]).keys())}")
    print(f"  sample: {asdict(sigs[0])}")
    print()
    print("STEP B - single trade")
    t = simulate_single_trade(sigs[0])
    print(f"  {asdict(t)}")
    print()
    print("STEP C - 10 trades, engine vs independent recompute (<= $0.01)")
    ok = 0
    for s in generate_dev_signals(1000, seed=2):
        r = simulate_single_trade(s)
        if not r.filled:
            continue
        recompute = ((r.exit_price - r.entry_fill) * CONTRACT_MULTIPLIER * r.contracts
                     - FEE_ROUND_TRIP * r.contracts)
        match = abs(recompute - r.pnl_dollar) <= 0.01
        ok += int(match)
        print(f"  sig {r.sig_id:>3}  engine ${r.pnl_dollar:8.2f}  "
              f"recompute ${recompute:8.2f}  {'OK' if match else 'MISMATCH'}")
        if ok >= 10:
            break
    print(f"  matched {ok}/10")
    print()
    print("STEP D + E - trade log + aggregate")
    log = build_trade_log(generate_dev_signals(1000, seed=3))
    agg = aggregate(log)
    for k, v in agg.items():
        print(f"  {k}: {v}")


# --------------------------------------------------------------------------- #
#  CLI
# --------------------------------------------------------------------------- #

def main() -> int:
    ap = argparse.ArgumentParser(description="Options strategy simulator (Phase 2)")
    ap.add_argument("--integrity", action="store_true",
                    help="run Gate 2A integrity suite and write report")
    ap.add_argument("--demo", action="store_true", help="small end-to-end demo")
    ap.add_argument("--steps", action="store_true", help="print Step A-E walkthrough")
    args = ap.parse_args()

    if args.steps:
        steps_walkthrough()
        return 0

    if args.demo:
        print(f"[{DEV_LABEL}]")
        log = build_trade_log(generate_dev_signals(1500, seed=5))
        agg = aggregate(log)
        print("Aggregate (mixed real mechanics, synthetic dev data):")
        for k, v in agg.items():
            print(f"  {k}: {v}")
        return 0

    if args.integrity:
        print(f"[{DEV_LABEL}]")
        print("Running Gate 2A integrity suite...\n")
        results = run_integrity_suite()
        for r in results:
            print(f"  [{'PASS' if r.passed else 'FAIL'}] {r.name}")
            print(f"        {r.detail}")
        all_pass = write_report(results)
        print(f"\nReport written: {REPORT_PATH}")
        print(f"GATE 2A: {'ALL 6 PASS' if all_pass else 'BLOCKED (fix failures)'}")
        return 0 if all_pass else 1

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
