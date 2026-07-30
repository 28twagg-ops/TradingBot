"""
options_universe.py — shared universe helper for Phase 1 data infrastructure.

Provides get_universe() returning the ~900-ticker S&P 500 + S&P 400 MidCap
combined list, with today-scoped disk cache in logs/cache/.

This module intentionally has NO Alpaca import so it can be imported without
credentials. It replicates the Wikipedia-scrape + caching logic from
rubber_band_bot.get_live_tickers() but is standalone.

Used by: api_probe_options.py, first_hour_collector.py, options_data_collector.py
"""

from __future__ import annotations

import json
import logging
from datetime import date
from pathlib import Path

import pandas as pd

log = logging.getLogger(__name__)

_REPO_ROOT = Path(__file__).resolve().parent.parent
_CACHE_DIR = _REPO_ROOT / "logs" / "cache"
_SP500_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
_SP400_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies"
_R1000_URL = "https://en.wikipedia.org/wiki/Russell_1000_Index"
_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def _cache_path() -> Path:
    _CACHE_DIR.mkdir(parents=True, exist_ok=True)
    return _CACHE_DIR / f"tickers_{date.today()}.json"

def to_alpaca_symbol(ticker: str) -> str:
    """Map universe ticker to Alpaca API symbol (class shares: BRK-B -> BRK.B)."""
    return ticker.replace("-", ".")

def get_universe(force_refresh: bool = False) -> list[str]:
    """Return a curated 'Top 100' universe of highly liquid stocks, ensuring AAPL is included."""
    # Fast / High-volatility tech and momentum names
    fast = [
        "NVDA", "TSLA", "AMD", "SMCI", "COIN", "PLTR", "CRWD", "META", "AMZN", "NFLX",
        "UBER", "SNOW", "AVGO", "MARA", "MSTR", "ARM", "PANW", "RST", "SHOP", "SQ",
        "HOOD", "DDOG", "ROKU", "AFRM", "TTD", "DKNG", "CVNA", "UPST", "ZS", "NET",
        "MDB", "CELH", "RBLX", "PATH", "DOCN", "GTLB", "FSLY", "BILL", "CFLT", "TWLO"
    ]
    # Neutral / Standard liquid names
    neutral = [
        "AAPL", "MSFT", "GOOGL", "SPY", "QQQ", "IWM", "DIS", "HD", "MCD", "NKE",
        "V", "MA", "JPM", "BAC", "BAC", "WFC", "C", "GS", "MS", "AXP", "BLK",
        "XOM", "CVX", "CVX", "COP", "SLB", "EOG", "PXD", "MPC", "OXY",
        "BA", "UNP", "CAT", "LMT", "GE", "MMM", "HON", "RTX", "DE", "UNH",
        "PFE", "LLY", "ABBV", "MRK", "TMO", "MDT", "DHR", "ISRG", "SYK", "ZTS"
    ]
    # Slow / Stable low-volatility names
    slow = [
        "KO", "PG", "JNJ", "WMT", "PEP", "COST", "T", "VZ", "MRK", "BMY",
        "CL", "KMB", "K", "GIS", "CPB", "SJM", "HRL", "CAG", "MKC", "MDLZ",
        "DUK", "SO", "D", "AEP", "EXC", "SRE", "XEL", "WEC", "ES", "ED"
    ]
    
    combined = list(dict.fromkeys(fast + neutral + slow))
    return combined

def get_stock_tier(ticker: str) -> str:
    """Return 'fast', 'slow', or 'neutral' based on the stock's volatility profile."""
    # Fast / High-volatility tech and momentum names
    fast = {
        "NVDA", "TSLA", "AMD", "SMCI", "COIN", "PLTR", "CRWD", "META", "AMZN", "NFLX",
        "UBER", "SNOW", "AVGO", "MARA", "MSTR", "ARM", "PANW", "RST", "SHOP", "SQ",
        "HOOD", "DDOG", "ROKU", "AFRM", "TTD", "DKNG", "CVNA", "UPST", "ZS", "NET",
        "MDB", "CELH", "RBLX", "PATH", "DOCN", "GTLB", "FSLY", "BILL", "CFLT", "TWLO"
    }
    # Slow / Stable low-volatility names
    slow = {
        "KO", "PG", "JNJ", "WMT", "PEP", "COST", "T", "VZ", "MRK", "BMY",
        "CL", "KMB", "K", "GIS", "CPB", "SJM", "HRL", "CAG", "MKC", "MDLZ",
        "DUK", "SO", "D", "AEP", "EXC", "SRE", "XEL", "WEC", "ES", "ED"
    }
    
    if ticker in fast:
        return "fast"
    if ticker in slow:
        return "slow"
    return "neutral"



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    universe = get_universe()
    print(f"Universe size: {len(universe)}")
    print(f"Sample: {universe[:10]}")
