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


def _prep_pattern_bars(sub: pd.DataFrame) -> pd.DataFrame | None:
    """Daily OHLCV + indicators for pattern scanners (need ~60+ bars)."""
    if sub is None or len(sub) < 60:
        return None
    df = sub.copy()
    df.columns = [c.lower() for c in df.columns]
    for col in ("open", "high", "low", "close", "volume"):
        if col not in df.columns:
            return None
    c = df["close"]
    v = df["volume"]
    o = df["open"]
    d = c.diff()
    gain = d.clip(lower=0).rolling(14).mean()
    loss = (-d.clip(upper=0)).rolling(14).mean()
    df["rsi"] = 100 - 100 / (1 + gain / (loss + 1e-10))
    df["ma20"] = c.rolling(20).mean()
    df["ma50"] = c.rolling(50).mean()
    df["ma200"] = c.rolling(200).mean()
    df["bbm"] = df["ma20"]
    df["bbu20"] = c.rolling(20).mean() + 2.0 * c.rolling(20).std()
    df["bbl20"] = c.rolling(20).mean() - 2.0 * c.rolling(20).std()
    df["bbw"] = (df["bbu20"] - df["bbl20"]) / (df["bbm"] + 1e-10)
    avg = v.rolling(20).mean()
    sv = v.rolling(20).std()
    df["vz"] = (v - avg) / (sv + 1e-10)
    df["prior_close"] = c.shift(1)
    df["gap_pct"] = (o - df["prior_close"]) / (df["prior_close"] + 1e-10)
    df["vwap5"] = ((df["high"] + df["low"] + c) / 3).rolling(5).mean()
    return df


def _pattern_today(sub: pd.DataFrame, today: date) -> pd.DataFrame | None:
    df = _prep_pattern_bars(sub)
    if df is None:
        return None
    if str(df.index[-1].date()) != str(today):
        return None
    return df


def scan_bb_squeeze(sub: pd.DataFrame, sym: str, today: date,
                    min_price: float = 3.0) -> SignalHit | None:
    """S169: BB squeeze near 20d min bandwidth + upside breakout on volume."""
    df = _pattern_today(sub, today)
    if df is None or len(df) < 45:
        return None
    last = df.iloc[-1]
    cn = float(last["close"])
    if cn < min_price:
        return None
    bbw = float(last["bbw"])
    bbu = float(last["bbu20"])
    vz = float(last["vz"])
    ma50 = float(last["ma50"])
    gap = float(last["gap_pct"])
    bbw_min = float(df["bbw"].rolling(20).min().shift(1).iloc[-1])
    if any(pd.isna(x) for x in [bbw, bbu, vz, ma50, gap, bbw_min]):
        return None
    if bbw < bbw_min * 1.05 and cn > bbu and vz >= 1.5 and cn > ma50 and gap >= -0.01:
        return SignalHit("S169", "BB Squeeze Breakout call 3 DTE", sym, cn,
                         f"BBW squeeze breakout VZ={vz:.1f}")
    return None


def scan_golden_pocket(sub: pd.DataFrame, sym: str, today: date,
                       min_price: float = 3.0) -> SignalHit | None:
    """S170: Fib 61.8–65% golden pocket bounce in MA200 uptrend."""
    df = _pattern_today(sub, today)
    if df is None or len(df) < 210:
        return None
    last = df.iloc[-1]
    cn = float(last["close"])
    opn = float(last["open"])
    if cn < min_price:
        return None
    ma200 = float(last["ma200"])
    vz = float(last["vz"])
    rsi = float(last["rsi"])
    swing_high = float(df["high"].rolling(60).max().iloc[-1])
    swing_low = float(df["low"].rolling(60).min().iloc[-1])
    if any(pd.isna(x) for x in [ma200, vz, rsi, swing_high, swing_low]):
        return None
    rng = swing_high - swing_low
    if rng <= 0:
        return None
    fib_618 = swing_high - 0.618 * rng
    fib_650 = swing_high - 0.650 * rng
    if (cn > ma200 and fib_650 <= cn <= fib_618 and cn > opn
            and vz >= 0.5 and 35 <= rsi <= 55):
        return SignalHit("S170", "Golden Pocket call 3 DTE", sym, cn,
                         "fib 61.8-65% bounce")
    return None


def scan_vwap_reclaim(sub: pd.DataFrame, sym: str, today: date,
                      min_price: float = 3.0) -> SignalHit | None:
    """S171: dipped below 5d VWAP proxy, closed back above on volume."""
    df = _pattern_today(sub, today)
    if df is None or len(df) < 55:
        return None
    last = df.iloc[-1]
    cn = float(last["close"])
    opn = float(last["open"])
    lo = float(last["low"])
    if cn < min_price:
        return None
    vwap5 = float(last["vwap5"])
    vz = float(last["vz"])
    ma50 = float(last["ma50"])
    gap = float(last["gap_pct"])
    if any(pd.isna(x) for x in [vwap5, vz, ma50, gap]):
        return None
    if (lo < vwap5 and cn > vwap5 and vz >= 1.0 and cn > ma50
            and cn > opn and gap >= -0.01):
        return SignalHit("S171", "VWAP Reclaim call 3 DTE", sym, cn,
                         f"VWAP reclaim VZ={vz:.1f}")
    return None


def scan_trend_resumption(sub: pd.DataFrame, sym: str, today: date,
                          min_price: float = 3.0) -> SignalHit | None:
    """S172: HH/HL structure, 2–4d pullback, break prior day high."""
    df = _pattern_today(sub, today)
    if df is None or len(df) < 210:
        return None
    last = df.iloc[-1]
    cn = float(last["close"])
    if cn < min_price:
        return None
    c = df["close"]
    ma50 = float(last["ma50"])
    ma200 = float(last["ma200"])
    vz = float(last["vz"])
    prior_high = float(df["high"].iloc[-2])
    if any(pd.isna(x) for x in [ma50, ma200, vz, prior_high]):
        return None
    recent_hi = float(df["high"].iloc[-5:].max())
    prior_hi = float(df["high"].iloc[-20:-5].max())
    hh_ok = recent_hi >= prior_hi * 0.99
    red_days = sum(float(c.iloc[-i]) < float(c.iloc[-i - 1]) for i in range(1, 5))
    if (hh_ok and 2 <= red_days <= 4 and cn > prior_high
            and cn > ma50 and cn > ma200 and vz >= 0.3):
        return SignalHit("S172", "Trend Resumption call 3 DTE", sym, cn,
                         f"HH/HL resumption after {red_days}d pullback")
    return None


def scan_earnings_drift(sub: pd.DataFrame, sym: str, today: date,
                        min_price: float = 3.0) -> SignalHit | None:
    """S175: PEAD continuation 1–5 days after +3% gap on high volume."""
    df = _pattern_today(sub, today)
    if df is None or len(df) < 30:
        return None
    last = df.iloc[-1]
    cn = float(last["close"])
    if cn < min_price:
        return None
    prev = float(df["close"].iloc[-2])
    ma20 = float(last["ma20"])
    rsi = float(last["rsi"])
    vz = float(last["vz"])
    if any(pd.isna(x) for x in [prev, ma20, rsi, vz]):
        return None
    recent = df.iloc[-6:-1]
    days_since = None
    for offset, (_, row) in enumerate(recent.iloc[::-1].iterrows(), start=1):
        gap = float(row["gap_pct"]) if not pd.isna(row["gap_pct"]) else None
        rvz = float(row["vz"]) if not pd.isna(row["vz"]) else None
        if gap is not None and rvz is not None and gap >= 0.03 and rvz >= 2.0:
            days_since = offset
            break
    if days_since is None:
        return None
    if (cn > prev and cn > ma20 and cn < ma20 * 1.15 and rsi < 70 and vz >= 0.5):
        return SignalHit("S175", "Earnings Drift call 3 DTE", sym, cn,
                         f"post-earnings continuation day {days_since}")
    return None


@dataclass
class StrategyConfig:
    id: str
    name: str
    dte_target: int
    dte_min: int
    dte_max: int
    scanner: object


# Live scan list — S174 ended (2026-07-16/20); S173 ended new entries (2026-07-20).
# Historical ledger still contains S173/S174 exits for audit; see DROPPED_STRATEGIES
# in options_lab for reflected P&L that excludes them.
# P2B (2026-07-18): S164=1-DTE, S168=5-DTE GapDown ATM; S165=3-DTE control; S163=7-DTE.
# P2C (2026-07-18): S167=1-strike OTM ~3-DTE (same gap signal as S165).
# Pattern arms (2026-07-22C): S169–S172, S175 — ATM ~3-DTE, independent of GapDown.
PAPER_STRATEGIES: list[StrategyConfig] = [
    StrategyConfig("S165", "GapDown long call 3 DTE", 3, 1, 7,
                   lambda sub, sym, today, mp: scan_gap_down(
                       sub, sym, today, GAP_DOWN_THRESH,
                       "S165", "GapDown long call 3 DTE", mp)),
    StrategyConfig(
        "S164", "GapDown ATM 1-DTE — P2B arm", 1, 0, 3,
        lambda sub, sym, today, mp: scan_gap_down(
            sub, sym, today, GAP_DOWN_THRESH,
            "S164", "GapDown ATM 1-DTE — P2B arm", mp)),
    StrategyConfig(
        "S168", "GapDown ATM 5-DTE — P2B arm", 5, 3, 8,
        lambda sub, sym, today, mp: scan_gap_down(
            sub, sym, today, GAP_DOWN_THRESH,
            "S168", "GapDown ATM 5-DTE — P2B arm", mp)),
    StrategyConfig(
        "S167", "GapDown long call 3 DTE 1-OTM — P2C", 3, 1, 7,
        lambda sub, sym, today, mp: scan_gap_down(
            sub, sym, today, GAP_DOWN_THRESH,
            "S167", "GapDown long call 3 DTE 1-OTM — P2C", mp)),
    StrategyConfig("S166", "GapDown strong call", 7, 2, 14, scan_gap_down_strong),
    StrategyConfig("S163", "A1 GapDown ATM call EOD", 7, 2, 10,
                   lambda sub, sym, today, mp: scan_gap_down(
                       sub, sym, today, GAP_DOWN_THRESH,
                       "S163", "A1 GapDown ATM call EOD", mp)),
    StrategyConfig("S169", "BB Squeeze Breakout call 3 DTE", 3, 1, 7, scan_bb_squeeze),
    StrategyConfig("S170", "Golden Pocket call 3 DTE", 3, 1, 7, scan_golden_pocket),
    StrategyConfig("S171", "VWAP Reclaim call 3 DTE", 3, 1, 7, scan_vwap_reclaim),
    StrategyConfig("S172", "Trend Resumption call 3 DTE", 3, 1, 7, scan_trend_resumption),
    StrategyConfig("S175", "Earnings Drift call 3 DTE", 3, 1, 7, scan_earnings_drift),
]

# Kept for reports / name lookup only — not scanned.
DROPPED_PAPER_STRATEGIES: list[StrategyConfig] = [
    StrategyConfig("S174", "RubberBand long call EOD", 7, 2, 14, scan_rubber_band),
    StrategyConfig("S173", "MomReversal long call", 1, 0, 7, scan_mom_reversal),
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
