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
    """Return the combined S&P 500 + S&P 400 MidCap + Russell 1000 list (~1400 symbols).

    Reads from today's cache file if present (avoids redundant Wikipedia hits).
    Cache is written to logs/cache/tickers_YYYY-MM-DD.json in the same format
    as rubber_band_bot.get_live_tickers() so both share the same daily file.

    Args:
        force_refresh: If True, bypass cache and re-scrape Wikipedia.

    Returns:
        List of ticker strings, deduplicated, dots replaced with hyphens.

    Raises:
        SystemExit(1) if Wikipedia scrapes fail (same behaviour as the equity bot).
    """
    cache = _cache_path()
    if not force_refresh and cache.exists():
        try:
            cached = json.loads(cache.read_text(encoding="utf-8"))
            tickers = cached.get("tickers", [])
            if tickers:
                log.debug("Universe cache hit: %d tickers (%s)", len(tickers), cache.name)
                return tickers
        except Exception as exc:
            log.warning("Ticker cache read failed: %s", exc)

    log.info("Fetching universe from Wikipedia (S&P 500 + S&P 400 + Russell 1000) …")
    sp500: list[str] = []
    mid400: list[str] = []
    r1000: list[str] = []

    try:
        sp500 = (
            pd.read_html(_SP500_URL, storage_options=_HEADERS)[0]["Symbol"].tolist()
        )
        log.info("  S&P 500: %d tickers", len(sp500))
    except Exception as exc:
        log.error("FATAL: could not fetch S&P 500 list: %s", exc)
        raise SystemExit(1) from exc

    try:
        mid400 = (
            pd.read_html(_SP400_URL, storage_options=_HEADERS)[0]["Symbol"].tolist()
        )
        log.info("  S&P 400 MidCap: %d tickers", len(mid400))
    except Exception as exc:
        log.error("FATAL: could not fetch S&P 400 list: %s", exc)
        raise SystemExit(1) from exc

    try:
        # Table 3 is typically the components table
        r1000_table = pd.read_html(_R1000_URL, storage_options=_HEADERS)[3]
        col = "Symbol" if "Symbol" in r1000_table.columns else "Ticker"
        r1000 = r1000_table[col].tolist()
        log.info("  Russell 1000: %d tickers", len(r1000))
    except Exception as exc:
        log.warning("Could not fetch Russell 1000 list: %s", exc)
        # Not fatal, we still have S&P 500/400

    combined = list(dict.fromkeys(sp500 + mid400 + r1000))
    cleaned = [str(t).replace(".", "-") for t in combined if pd.notna(t)]
    log.info("  Universe total: %d tickers", len(cleaned))

    try:
        cache.write_text(
            json.dumps({"date": str(date.today()), "tickers": cleaned}, indent=2),
            encoding="utf-8",
        )
    except Exception as exc:
        log.warning("Ticker cache write failed: %s", exc)

    return cleaned


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    universe = get_universe()
    print(f"Universe size: {len(universe)}")
    print(f"Sample: {universe[:10]}")
