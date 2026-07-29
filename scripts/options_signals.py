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
    option_type: str = "call"   # "call" or "put" — bearish signals set "put"


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


# =========================================================================== #
#  PHASE-1 SCANNERS: S200-S219  (added 2026-07-25B)
#  All follow: scan_SXXX(sub, sym, today, min_px) -> SignalHit | None
#  Indicators computed inline from _prep_pattern_bars().
# =========================================================================== #

# --------------------------------------------------------------------------- #
#  FAMILY 1: GAP SIGNALS — S200-S209
# --------------------------------------------------------------------------- #

def scan_s200(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S200 GapDown_Aggressive: gap <= -3%, green close, VZ >= 2.0, RSI < 50."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        gap = float(row.get("gap_pct", float("nan")))
        vz = float(row.get("vz", float("nan")))
        rsi = float(row.get("rsi", float("nan")))
        cn, opn = float(row["close"]), float(row["open"])
        if any(pd.isna(v) for v in (gap, vz, rsi)) or cn < min_px:
            return None
        if gap <= -0.03 and cn > opn and vz >= 2.0 and rsi < 50:
            return SignalHit("S200", "GapDown_Aggressive", sym, cn,
                             f"gap {gap:+.1%} vz={vz:.1f} rsi={rsi:.0f}")
    except Exception:
        pass
    return None


def scan_s201(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S201 GapDown_Mild: gap -1.5% to -3%, green close, VZ >= 1.0."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        gap = float(row.get("gap_pct", float("nan")))
        vz = float(row.get("vz", float("nan")))
        cn, opn = float(row["close"]), float(row["open"])
        if any(pd.isna(v) for v in (gap, vz)) or cn < min_px:
            return None
        if -0.03 < gap <= -0.015 and cn > opn and vz >= 1.0:
            return SignalHit("S201", "GapDown_Mild", sym, cn,
                             f"gap {gap:+.1%} vz={vz:.1f}")
    except Exception:
        pass
    return None


def scan_s202(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S202 GapDown_Monster: gap <= -5% (capitulation, any close)."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        gap = float(row.get("gap_pct", float("nan")))
        cn = float(row["close"])
        if pd.isna(gap) or cn < min_px:
            return None
        if gap <= -0.05:
            return SignalHit("S202", "GapDown_Monster", sym, cn, f"gap {gap:+.1%}")
    except Exception:
        pass
    return None


def scan_s203(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S203 GapUp_Fade: gap >= +3%, RED close (gap fill reversal -- PUT)."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        gap = float(row.get("gap_pct", float("nan")))
        cn, opn = float(row["close"]), float(row["open"])
        if pd.isna(gap) or cn < min_px:
            return None
        if gap >= 0.03 and cn < opn:
            return SignalHit("S203", "GapUp_Fade", sym, cn,
                             f"gap {gap:+.1%} red close",
                             option_type="put")
    except Exception:
        pass
    return None


def scan_s204(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S204 GapUp_Continuation: gap >= +2%, green close, VZ >= 2.0 (call)."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        gap = float(row.get("gap_pct", float("nan")))
        vz = float(row.get("vz", float("nan")))
        cn, opn = float(row["close"]), float(row["open"])
        if any(pd.isna(v) for v in (gap, vz)) or cn < min_px:
            return None
        if gap >= 0.02 and cn > opn and vz >= 2.0:
            return SignalHit("S204", "GapUp_Continuation", sym, cn,
                             f"gap {gap:+.1%} vz={vz:.1f}")
    except Exception:
        pass
    return None


def scan_s205(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S205 GapDown_HighVol: gap <= -2%, VZ >= 3.0 (institutional panic)."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        gap = float(row.get("gap_pct", float("nan")))
        vz = float(row.get("vz", float("nan")))
        cn = float(row["close"])
        if any(pd.isna(v) for v in (gap, vz)) or cn < min_px:
            return None
        if gap <= -0.02 and vz >= 3.0:
            return SignalHit("S205", "GapDown_HighVol", sym, cn,
                             f"gap {gap:+.1%} vz={vz:.1f}")
    except Exception:
        pass
    return None


def scan_s206(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S206 GapDown_WithTrend: gap <= -2%, above MA50, green, VZ >= 1.5."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        gap = float(row.get("gap_pct", float("nan")))
        vz = float(row.get("vz", float("nan")))
        ma50 = float(row.get("ma50", float("nan")))
        cn, opn = float(row["close"]), float(row["open"])
        if any(pd.isna(v) for v in (gap, vz, ma50)) or cn < min_px:
            return None
        if gap <= -0.02 and cn > opn and vz >= 1.5 and cn > ma50:
            return SignalHit("S206", "GapDown_WithTrend", sym, cn,
                             f"gap {gap:+.1%} vz={vz:.1f} above MA50")
    except Exception:
        pass
    return None


def scan_s207(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S207 GapDown_AtSupport: gap <= -2%, close within 5% above MA50 (support zone)."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        gap = float(row.get("gap_pct", float("nan")))
        ma50 = float(row.get("ma50", float("nan")))
        cn, opn = float(row["close"]), float(row["open"])
        if any(pd.isna(v) for v in (gap, ma50)) or cn < min_px or ma50 <= 0:
            return None
        dist = (cn - ma50) / ma50
        if gap <= -0.02 and cn > opn and 0 <= dist <= 0.05:
            return SignalHit("S207", "GapDown_AtSupport", sym, cn,
                             f"gap {gap:+.1%} MA50 dist={dist:.1%}")
    except Exception:
        pass
    return None


def scan_s208(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S208 GapDown_AboveMA200: gap <= -2%, green, price > MA200 (quality name)."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        gap = float(row.get("gap_pct", float("nan")))
        ma200 = float(row.get("ma200", float("nan")))
        cn, opn = float(row["close"]), float(row["open"])
        if any(pd.isna(v) for v in (gap, ma200)) or cn < min_px:
            return None
        if gap <= -0.02 and cn > opn and cn > ma200:
            return SignalHit("S208", "GapDown_AboveMA200", sym, cn,
                             f"gap {gap:+.1%} above MA200")
    except Exception:
        pass
    return None


def scan_s209(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S209 GapDown_Recovery: gap <= -2%, close > prior close (immediate recovery)."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        gap = float(row.get("gap_pct", float("nan")))
        prior_close = float(row.get("prior_close", float("nan")))
        cn = float(row["close"])
        if any(pd.isna(v) for v in (gap, prior_close)) or cn < min_px:
            return None
        if gap <= -0.02 and cn > prior_close:
            return SignalHit("S209", "GapDown_Recovery", sym, cn,
                             f"gap {gap:+.1%} recovery above prev close")
    except Exception:
        pass
    return None


# --------------------------------------------------------------------------- #
#  FAMILY 2: MOVING AVERAGE SIGNALS — S210-S215
# --------------------------------------------------------------------------- #

def _ma_cross(df: pd.DataFrame, fast_n: int, slow_n: int) -> tuple[bool, bool]:
    """Return (crossed_above_today, was_below_yesterday)."""
    c = df["close"]
    fast = c.rolling(fast_n).mean()
    slow = c.rolling(slow_n).mean()
    if len(fast) < 2 or pd.isna(fast.iloc[-1]) or pd.isna(slow.iloc[-1]):
        return False, False
    cross_today = fast.iloc[-1] > slow.iloc[-1]
    was_below = fast.iloc[-2] <= slow.iloc[-2]
    return cross_today and was_below, True


def scan_s210(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S210 MA_Cross_8_21: 8-day MA crosses above 21-day MA."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        if str(df.index[-1].date()) != str(today):
            return None
        cn = float(df.iloc[-1]["close"])
        if cn < min_px:
            return None
        crossed, _ = _ma_cross(df, 8, 21)
        if crossed:
            ma8 = float(df["close"].rolling(8).mean().iloc[-1])
            return SignalHit("S210", "MA_Cross_8_21", sym, cn,
                             f"MA8 {ma8:.2f} crossed above MA21")
    except Exception:
        pass
    return None


def scan_s211(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S211 MA_Cross_21_50: 21-day crosses above 50-day."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        if str(df.index[-1].date()) != str(today):
            return None
        cn = float(df.iloc[-1]["close"])
        if cn < min_px:
            return None
        crossed, _ = _ma_cross(df, 21, 50)
        if crossed:
            return SignalHit("S211", "MA_Cross_21_50", sym, cn,
                             "MA21 crossed above MA50")
    except Exception:
        pass
    return None


def scan_s212(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S212 MA_Bounce_50: touch 50MA from above + green candle."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        ma50 = float(row.get("ma50", float("nan")))
        lo = float(row["low"])
        cn, opn = float(row["close"]), float(row["open"])
        if pd.isna(ma50) or cn < min_px:
            return None
        pct_from_ma = abs(lo - ma50) / ma50
        if pct_from_ma <= 0.015 and cn > opn:
            return SignalHit("S212", "MA_Bounce_50", sym, cn,
                             f"low={lo:.2f} MA50={ma50:.2f} touch+green")
    except Exception:
        pass
    return None


def scan_s213(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S213 MA_Bounce_200: touch 200MA from above + green candle."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        ma200 = float(row.get("ma200", float("nan")))
        lo = float(row["low"])
        cn, opn = float(row["close"]), float(row["open"])
        if pd.isna(ma200) or cn < min_px:
            return None
        pct_from_ma = abs(lo - ma200) / ma200
        if pct_from_ma <= 0.02 and cn > opn:
            return SignalHit("S213", "MA_Bounce_200", sym, cn,
                             f"low={lo:.2f} MA200={ma200:.2f} touch+green")
    except Exception:
        pass
    return None


def scan_s214(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S214 MA_Death_Cross: 50MA crosses below 200MA -- PUT signal."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        if str(df.index[-1].date()) != str(today):
            return None
        cn = float(df.iloc[-1]["close"])
        if cn < min_px:
            return None
        c = df["close"]
        ma50 = c.rolling(50).mean()
        ma200 = c.rolling(200).mean()
        if pd.isna(ma50.iloc[-1]) or pd.isna(ma200.iloc[-1]):
            return None
        below_today = ma50.iloc[-1] < ma200.iloc[-1]
        was_above = ma50.iloc[-2] >= ma200.iloc[-2] if len(ma50) >= 2 else False
        if below_today and was_above:
            return SignalHit("S214", "MA_Death_Cross", sym, cn,
                             f"MA50 {ma50.iloc[-1]:.2f} crossed below MA200 {ma200.iloc[-1]:.2f}",
                             option_type="put")
    except Exception:
        pass
    return None


def scan_s215(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S215 MA_Reclaim_200: price reclaims 200MA after being below it (within 10d)."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None or len(df) < 12:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        ma200 = float(row.get("ma200", float("nan")))
        cn = float(row["close"])
        if pd.isna(ma200) or cn < min_px:
            return None
        above_today = cn > ma200
        prev_closes = df["close"].iloc[-11:-1]
        prev_ma200 = df["close"].rolling(200).mean().iloc[-11:-1]
        was_below_recently = any(
            float(pc) < float(pm)
            for pc, pm in zip(prev_closes, prev_ma200)
            if not pd.isna(pm)
        )
        if above_today and was_below_recently:
            return SignalHit("S215", "MA_Reclaim_200", sym, cn,
                             f"price {cn:.2f} reclaimed MA200 {ma200:.2f}")
    except Exception:
        pass
    return None


# --------------------------------------------------------------------------- #
#  EARLY RSI / BB / VOLUME ENTRIES — S216-S219
# --------------------------------------------------------------------------- #

def scan_s216(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S216 RSI_Oversold_Cross: RSI crosses above 30 (oversold recovery)."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None or len(df) < 2:
            return None
        if str(df.index[-1].date()) != str(today):
            return None
        rsi_today = float(df.iloc[-1].get("rsi", float("nan")))
        rsi_prev = float(df.iloc[-2].get("rsi", float("nan")))
        cn = float(df.iloc[-1]["close"])
        if any(pd.isna(v) for v in (rsi_today, rsi_prev)) or cn < min_px:
            return None
        if rsi_today > 30 and rsi_prev <= 30:
            return SignalHit("S216", "RSI_Oversold_Cross", sym, cn,
                             f"RSI crossed 30: {rsi_prev:.1f} -> {rsi_today:.1f}")
    except Exception:
        pass
    return None


def scan_s217(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S217 RSI_25_Bounce: RSI < 25 + green candle (deeper oversold entry)."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        rsi = float(row.get("rsi", float("nan")))
        cn, opn = float(row["close"]), float(row["open"])
        if pd.isna(rsi) or cn < min_px:
            return None
        if rsi < 25 and cn > opn:
            return SignalHit("S217", "RSI_25_Bounce", sym, cn,
                             f"RSI={rsi:.1f} green")
    except Exception:
        pass
    return None


def scan_s218(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S218 BB_Lower_Touch: price touches lower 2.0-std band + green candle."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        bbl = float(row.get("bbl20", float("nan")))
        lo = float(row["low"])
        cn, opn = float(row["close"]), float(row["open"])
        if pd.isna(bbl) or cn < min_px:
            return None
        if lo <= bbl * 1.005 and cn > opn:
            return SignalHit("S218", "BB_Lower_Touch", sym, cn,
                             f"low={lo:.2f} BB_lower={bbl:.2f} touch+green")
    except Exception:
        pass
    return None


def scan_s219(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S219 Volume_Climax_Up: VZ >= 3.0 + green candle (institutional accumulation)."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None:
            return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today):
            return None
        vz = float(row.get("vz", float("nan")))
        cn, opn = float(row["close"]), float(row["open"])
        if pd.isna(vz) or cn < min_px:
            return None
        if vz >= 3.0 and cn > opn:
            return SignalHit("S219", "Volume_Climax_Up", sym, cn,
                             f"VZ={vz:.1f} green close")
    except Exception:
        pass
    return None


# --------------------------------------------------------------------------- #
#  SIMPLE FREQUENCY BOOSTERS (added 2026-07-28A) — S400-S403
# --------------------------------------------------------------------------- #

def scan_s400(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S400 Any_Green_Close: stock is green today + VZ >= 0.5 + above MA50."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None: return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today): return None
        vz = float(row.get("vz", float("nan")))
        ma50 = float(row.get("ma50", float("nan")))
        cn, opn = float(row["close"]), float(row["open"])
        if pd.isna(vz) or pd.isna(ma50) or cn < min_px: return None
        if cn > opn and vz >= 0.5 and cn > ma50:
            return SignalHit("S400", "Any_Green_Close", sym, cn, f"green VZ={vz:.1f} >MA50")
    except Exception: pass
    return None

def scan_s401(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S401 Any_Gap_Down_Small: gap -0.5% to -2%, green close."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None: return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today): return None
        gap = float(row.get("gap_pct", float("nan")))
        cn, opn = float(row["close"]), float(row["open"])
        if pd.isna(gap) or cn < min_px: return None
        if -0.02 <= gap <= -0.005 and cn > opn:
            return SignalHit("S401", "Any_Gap_Down_Small", sym, cn, f"gap {gap:+.2%} green")
    except Exception: pass
    return None

def scan_s402(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S402 Any_High_Volume: VZ >= 2.0 + close > open."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None: return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today): return None
        vz = float(row.get("vz", float("nan")))
        cn, opn = float(row["close"]), float(row["open"])
        if pd.isna(vz) or cn < min_px: return None
        if vz >= 2.0 and cn > opn:
            return SignalHit("S402", "Any_High_Volume", sym, cn, f"VZ={vz:.1f} green")
    except Exception: pass
    return None

def scan_s403(sub: pd.DataFrame, sym: str, today: date, min_px: float = 3.0) -> SignalHit | None:
    """S403 Any_MA50_Touch: within 0.5% of MA50 + green."""
    try:
        df = _prep_pattern_bars(sub)
        if df is None: return None
        row = df.iloc[-1]
        if str(df.index[-1].date()) != str(today): return None
        ma50 = float(row.get("ma50", float("nan")))
        lo, cn, opn = float(row["low"]), float(row["close"]), float(row["open"])
        if pd.isna(ma50) or cn < min_px: return None
        pct_from_ma = abs(lo - ma50) / ma50
        if pct_from_ma <= 0.005 and cn > opn:
            return SignalHit("S403", "Any_MA50_Touch", sym, cn, f"touch MA50 green")
    except Exception: pass
    return None

def _get_base_scanner(base_id: str):
    if base_id == "S165": return lambda s, sym, t, mp: scan_gap_down(s, sym, t, GAP_DOWN_THRESH, base_id, "base", mp)
    if base_id == "S174": return scan_rubber_band
    if base_id == "S169": return scan_bb_squeeze
    if base_id == "S200": return scan_s200
    if base_id == "S219": return scan_s219
    return None

def scan_variant(sub: pd.DataFrame, sym: str, today: date, min_px: float, strat_id: str, base_id: str, name: str) -> SignalHit | None:
    scanner = _get_base_scanner(base_id)
    if not scanner: return None
    hit = scanner(sub, sym, today, min_px)
    if hit:
        hit.strategy_id = strat_id
        hit.strategy_name = name
    return hit

@dataclass
class StrategyConfig:
    id: str
    name: str
    dte_target: int
    dte_min: int
    dte_max: int
    scanner: object
    strike_offset: int = 0
    option_type: str = "call"


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

# Phase-1 strategies (2026-07-25B): S200-S219 -- 20 signals, 8 buckets each = 160 new buckets
# Signals with option_type="put": S203 (GapUp_Fade), S214 (MA_Death_Cross)
PHASE1_STRATEGIES: list[StrategyConfig] = [
    StrategyConfig("S200", "GapDown_Aggressive", 3, 1, 7, scan_s200),
    StrategyConfig("S201", "GapDown_Mild",        3, 1, 7, scan_s201),
    StrategyConfig("S202", "GapDown_Monster",     3, 1, 7, scan_s202),
    StrategyConfig("S203", "GapUp_Fade",          3, 1, 7, scan_s203),
    StrategyConfig("S204", "GapUp_Continuation",  3, 1, 7, scan_s204),
    StrategyConfig("S205", "GapDown_HighVol",     3, 1, 7, scan_s205),
    StrategyConfig("S206", "GapDown_WithTrend",   3, 1, 7, scan_s206),
    StrategyConfig("S207", "GapDown_AtSupport",   3, 1, 7, scan_s207),
    StrategyConfig("S208", "GapDown_AboveMA200",  3, 1, 7, scan_s208),
    StrategyConfig("S209", "GapDown_Recovery",    3, 1, 7, scan_s209),
    StrategyConfig("S210", "MA_Cross_8_21",       3, 1, 7, scan_s210),
    StrategyConfig("S211", "MA_Cross_21_50",      3, 1, 7, scan_s211),
    StrategyConfig("S212", "MA_Bounce_50",        3, 1, 7, scan_s212),
    StrategyConfig("S213", "MA_Bounce_200",       3, 1, 7, scan_s213),
    StrategyConfig("S214", "MA_Death_Cross",      3, 1, 7, scan_s214),
    StrategyConfig("S215", "MA_Reclaim_200",      3, 1, 7, scan_s215),
    StrategyConfig("S216", "RSI_Oversold_Cross",  3, 1, 7, scan_s216),
    StrategyConfig("S217", "RSI_25_Bounce",       3, 1, 7, scan_s217),
    StrategyConfig("S218", "BB_Lower_Touch",      3, 1, 7, scan_s218),
    StrategyConfig("S219", "Volume_Climax_Up",    3, 1, 7, scan_s219),
    StrategyConfig("S400", "Any_Green_Close",     3, 1, 7, scan_s400),
    StrategyConfig("S401", "Any_Gap_Down_Small",  3, 1, 7, scan_s401),
    StrategyConfig("S402", "Any_High_Volume",     3, 1, 7, scan_s402),
    StrategyConfig("S403", "Any_MA50_Touch",      3, 1, 7, scan_s403),
]

PAPER_STRATEGIES.extend(PHASE1_STRATEGIES)

# Dynamically add S350-S415 (Variants)
_VARIANT_CONFIGS = [
    # DTE Matrix (offset = 0)
    ("S350", "GapDown_0DTE", "S165", 0, 0, 1, 0), ("S351", "GapDown_1DTE", "S165", 1, 0, 2, 0), ("S352", "GapDown_2DTE", "S165", 2, 1, 3, 0), ("S353", "GapDown_3DTE", "S165", 3, 2, 4, 0), ("S354", "GapDown_5DTE", "S165", 5, 4, 6, 0), ("S355", "GapDown_7DTE", "S165", 7, 6, 8, 0), ("S356", "GapDown_14DTE", "S165", 14, 13, 17, 0), ("S357", "GapDown_21DTE", "S165", 21, 20, 24, 0), ("S358", "GapDown_30DTE", "S165", 30, 29, 33, 0),
    ("S359", "RubberBand_0DTE", "S174", 0, 0, 1, 0), ("S360", "RubberBand_1DTE", "S174", 1, 0, 2, 0), ("S361", "RubberBand_2DTE", "S174", 2, 1, 3, 0), ("S362", "RubberBand_3DTE", "S174", 3, 2, 4, 0), ("S363", "RubberBand_5DTE", "S174", 5, 4, 6, 0), ("S364", "RubberBand_7DTE", "S174", 7, 6, 8, 0), ("S365", "RubberBand_14DTE", "S174", 14, 13, 17, 0), ("S366", "RubberBand_21DTE", "S174", 21, 20, 24, 0), ("S367", "RubberBand_30DTE", "S174", 30, 29, 33, 0),
    ("S368", "BBSqueeze_0DTE", "S169", 0, 0, 1, 0), ("S369", "BBSqueeze_1DTE", "S169", 1, 0, 2, 0), ("S370", "BBSqueeze_2DTE", "S169", 2, 1, 3, 0), ("S371", "BBSqueeze_3DTE", "S169", 3, 2, 4, 0), ("S372", "BBSqueeze_5DTE", "S169", 5, 4, 6, 0), ("S373", "BBSqueeze_7DTE", "S169", 7, 6, 8, 0), ("S374", "BBSqueeze_14DTE", "S169", 14, 13, 17, 0), ("S375", "BBSqueeze_21DTE", "S169", 21, 20, 24, 0), ("S376", "BBSqueeze_30DTE", "S169", 30, 29, 33, 0),
    ("S377", "GapDownAggr_0DTE", "S200", 0, 0, 1, 0), ("S378", "GapDownAggr_1DTE", "S200", 1, 0, 2, 0), ("S379", "GapDownAggr_2DTE", "S200", 2, 1, 3, 0), ("S380", "GapDownAggr_3DTE", "S200", 3, 2, 4, 0), ("S381", "GapDownAggr_5DTE", "S200", 5, 4, 6, 0), ("S382", "GapDownAggr_7DTE", "S200", 7, 6, 8, 0), ("S383", "GapDownAggr_14DTE", "S200", 14, 13, 17, 0), ("S384", "GapDownAggr_21DTE", "S200", 21, 20, 24, 0), ("S385", "GapDownAggr_30DTE", "S200", 30, 29, 33, 0),
    ("S386", "VolClimax_0DTE", "S219", 0, 0, 1, 0), ("S387", "VolClimax_1DTE", "S219", 1, 0, 2, 0), ("S388", "VolClimax_2DTE", "S219", 2, 1, 3, 0), ("S389", "VolClimax_3DTE", "S219", 3, 2, 4, 0), ("S390", "VolClimax_5DTE", "S219", 5, 4, 6, 0), ("S391", "VolClimax_7DTE", "S219", 7, 6, 8, 0), ("S392", "VolClimax_14DTE", "S219", 14, 13, 17, 0), ("S393", "VolClimax_21DTE", "S219", 21, 20, 24, 0), ("S394", "VolClimax_30DTE", "S219", 30, 29, 33, 0),
    # Strike Matrix (defaults to 3DTE)
    ("S395", "GapDown_ITM3", "S165", 3, 1, 7, -3), ("S396", "GapDown_ITM2", "S165", 3, 1, 7, -2), ("S397", "GapDown_ITM1", "S165", 3, 1, 7, -1), ("S398", "GapDown_ATM", "S165", 3, 1, 7, 0), ("S399", "GapDown_OTM1", "S165", 3, 1, 7, 1), ("S404", "GapDown_OTM2", "S165", 3, 1, 7, 2), ("S405", "GapDown_OTM3", "S165", 3, 1, 7, 3),
    ("S406", "RubberBand_ITM3", "S174", 3, 1, 7, -3), ("S407", "RubberBand_ITM2", "S174", 3, 1, 7, -2), ("S408", "RubberBand_ITM1", "S174", 3, 1, 7, -1), ("S409", "RubberBand_ATM", "S174", 3, 1, 7, 0), ("S410", "RubberBand_OTM1", "S174", 3, 1, 7, 1), ("S411", "RubberBand_OTM2", "S174", 3, 1, 7, 2), ("S412", "RubberBand_OTM3", "S174", 3, 1, 7, 3),
    ("S413", "BBSqueeze_ITM3", "S169", 3, 1, 7, -3), ("S414", "BBSqueeze_ITM2", "S169", 3, 1, 7, -2), ("S415", "BBSqueeze_ITM1", "S169", 3, 1, 7, -1), ("S416", "BBSqueeze_ATM", "S169", 3, 1, 7, 0), ("S417", "BBSqueeze_OTM1", "S169", 3, 1, 7, 1), ("S418", "BBSqueeze_OTM2", "S169", 3, 1, 7, 2), ("S419", "BBSqueeze_OTM3", "S169", 3, 1, 7, 3),
]

for sid, name, base, dtarg, dmin, dmax, strike_offset in _VARIANT_CONFIGS:
    PAPER_STRATEGIES.append(
        StrategyConfig(sid, name, dtarg, dmin, dmax, 
                       lambda sub, sym, t, mp, s=sid, b=base, n=name: scan_variant(sub, sym, t, mp, s, b, n),
                       strike_offset=strike_offset)
    )

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
