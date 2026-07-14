"""
options_signals.py — Morning signal scanners for multi-strategy options paper bot.

Logic mirrors historical_backtest._match_signal() so paper entries align with
research rankings (return % per trade).
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

import pandas as pd

GAP_DOWN_THRESH = -0.02
GAP_STRONG_THRESH = -0.03
MOM_RB_GAP = -0.015


@dataclass
class SignalHit:
    strategy_id: str
    strategy_name: str
    symbol: str
    price: float
    detail: str


def prepare_bars(sub: pd.DataFrame) -> pd.DataFrame | None:
    if len(sub) < 2:
        return None
    df = sub.copy()
    df.columns = [c.lower() for c in df.columns]
    df["prior_close"] = df["close"].shift(1)
    df["gap_pct"] = (df["open"] - df["prior_close"]) / df["prior_close"]
    return df


def _today_row(sub: pd.DataFrame, today: date) -> pd.Series | None:
    df = prepare_bars(sub)
    if df is None:
        return None
    if str(df.index[-1].date()) != str(today):
        return None
    return df.iloc[-1]


def scan_gap_down(sub: pd.DataFrame, sym: str, today: date,
                  threshold: float, strategy_id: str, strategy_name: str,
                  min_price: float = 3.0, use_open: bool = True) -> SignalHit | None:
    last = _today_row(sub, today)
    if last is None:
        return None
    gap = float(last["gap_pct"])
    px = float(last["open"] if use_open else last["close"])
    if pd.isna(gap) or px < min_price:
        return None
    if gap <= threshold:
        return SignalHit(strategy_id, strategy_name, sym, px, f"gap {gap:+.1%}")
    return None


def scan_rubber_band(sub: pd.DataFrame, sym: str, today: date,
                     min_price: float = 3.0) -> SignalHit | None:
    """historical: gap <= -1.5% and close above bar midpoint."""
    last = _today_row(sub, today)
    if last is None:
        return None
    gap = float(last["gap_pct"])
    lo, hi, cn = float(last["low"]), float(last["high"]), float(last["close"])
    if pd.isna(gap) or cn < min_price:
        return None
    mid = lo + (hi - lo) * 0.5
    if gap <= MOM_RB_GAP and cn > mid:
        return SignalHit("S174", "RubberBand long call EOD", sym, cn,
                         f"RB gap {gap:+.1%} reclaim")
    return None


def scan_mom_reversal(sub: pd.DataFrame, sym: str, today: date,
                      min_price: float = 3.0) -> SignalHit | None:
    """historical: gap <= -1.5% and green day (close > open)."""
    last = _today_row(sub, today)
    if last is None:
        return None
    gap = float(last["gap_pct"])
    opn, cn = float(last["open"]), float(last["close"])
    if pd.isna(gap) or cn < min_price:
        return None
    if gap <= MOM_RB_GAP and cn > opn:
        return SignalHit("S173", "MomReversal long call", sym, cn,
                         f"MR gap {gap:+.1%} green")
    return None


def scan_gap_down_strong(sub: pd.DataFrame, sym: str, today: date,
                         min_price: float = 3.0) -> SignalHit | None:
    """historical gap_down_strong: gap <= -3%."""
    return scan_gap_down(sub, sym, today, GAP_STRONG_THRESH,
                         "S166", "GapDown strong call", min_price, use_open=True)


@dataclass
class StrategyConfig:
    id: str
    name: str
    dte_target: int
    dte_min: int
    dte_max: int
    scanner: object


# Live scan list — S174 paused (2026-07-13): negative median / drop recommendation.
# Historical ledger still contains S174 exits for audit; see DROPPED_STRATEGIES
# in options_lab for reflected P&L that excludes them.
PAPER_STRATEGIES: list[StrategyConfig] = [
    StrategyConfig("S173", "MomReversal long call", 1, 0, 7, scan_mom_reversal),
    StrategyConfig("S165", "GapDown long call 3 DTE", 3, 1, 7,
                   lambda sub, sym, today, mp: scan_gap_down(
                       sub, sym, today, GAP_DOWN_THRESH,
                       "S165", "GapDown long call 3 DTE", mp)),
    StrategyConfig("S166", "GapDown strong call", 7, 2, 14, scan_gap_down_strong),
    StrategyConfig("S163", "A1 GapDown ATM call EOD", 7, 2, 10,
                   lambda sub, sym, today, mp: scan_gap_down(
                       sub, sym, today, GAP_DOWN_THRESH,
                       "S163", "A1 GapDown ATM call EOD", mp)),
]

# Kept for reports / name lookup only — not scanned.
DROPPED_PAPER_STRATEGIES: list[StrategyConfig] = [
    StrategyConfig("S174", "RubberBand long call EOD", 7, 2, 14, scan_rubber_band),
]

ALL_KNOWN_STRATEGIES: list[StrategyConfig] = PAPER_STRATEGIES + DROPPED_PAPER_STRATEGIES


def scan_symbol(sub: pd.DataFrame, sym: str, today: date,
                min_price: float = 3.0) -> list[SignalHit]:
    hits: list[SignalHit] = []
    for strat in PAPER_STRATEGIES:
        try:
            hit = strat.scanner(sub, sym, today, min_price)
            if hit:
                hits.append(hit)
        except Exception:
            continue
    return hits
