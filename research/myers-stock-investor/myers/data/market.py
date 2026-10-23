from __future__ import annotations

from datetime import date, datetime, timedelta
from functools import lru_cache

import pandas as pd
import yfinance as yf


def _normalize_index(df: pd.DataFrame) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame()
    out = df.copy()
    out.index = pd.to_datetime(out.index).tz_localize(None).normalize()
    out = out[~out.index.duplicated(keep="last")].sort_index()
    out.columns = [str(c).lower() for c in out.columns]
    return out


@lru_cache(maxsize=64)
def fetch_price_history(ticker: str, start: str = "2005-01-01") -> pd.DataFrame:
    """Daily OHLCV adjusted via yfinance. Cached per process."""
    t = yf.Ticker(ticker)
    df = t.history(start=start, auto_adjust=True)
    return _normalize_index(df)


def latest_price_as_of(ticker: str, as_of: date, start: str = "2005-01-01") -> float | None:
    df = fetch_price_history(ticker, start=start)
    if df.empty or "close" not in df.columns:
        return None
    cutoff = pd.Timestamp(as_of)
    sub = df.loc[df.index <= cutoff]
    if sub.empty:
        return None
    px = float(sub["close"].iloc[-1])
    return px if px > 0 else None


def avg_dollar_volume(ticker: str, as_of: date, window: int = 60) -> float | None:
    df = fetch_price_history(ticker)
    if df.empty or "close" not in df.columns or "volume" not in df.columns:
        return None
    cutoff = pd.Timestamp(as_of)
    sub = df.loc[df.index <= cutoff].tail(window)
    if len(sub) < max(10, window // 3):
        return None
    return float((sub["close"] * sub["volume"]).mean())


def quarter_ends(start: date, end: date) -> list[date]:
    """Month-end dates for Mar/Jun/Sep/Dec within [start, end]."""
    idx = pd.date_range(start, end, freq="QE")
    return [d.date() for d in idx if start <= d.date() <= end]


def trading_days_between(ticker: str, start: date, end: date) -> pd.DatetimeIndex:
    df = fetch_price_history(ticker)
    if df.empty:
        return pd.DatetimeIndex([])
    mask = (df.index >= pd.Timestamp(start)) & (df.index <= pd.Timestamp(end))
    return df.index[mask]
