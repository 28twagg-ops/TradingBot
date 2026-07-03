"""
historical_data_fetcher.py — Download historical stock data locally for options research.

Sources:
  1. yfinance daily OHLCV (free, no API key) — default, period=max for longest history
  2. Alpaca historical bars (if ALPACA_API_KEY set) — optional upgrade

Outputs:
  data/historical/stocks/{SYMBOL}_daily.parquet
  data/historical/manifest.json

Run:
  python scripts/historical_data_fetcher.py
  python scripts/historical_data_fetcher.py --universe-full --max-history
  python scripts/historical_data_fetcher.py --universe-top 50 --years 5
  python scripts/historical_data_fetcher.py --probe-alpaca
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import yfinance as yf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_universe import get_universe

REPO_ROOT = Path(__file__).resolve().parent.parent
HIST_STOCKS = REPO_ROOT / "data" / "historical" / "stocks"
MANIFEST = REPO_ROOT / "data" / "historical" / "manifest.json"
PROGRESS_LOG = REPO_ROOT / "data" / "historical" / "fetch_progress.log"

DEFAULT_SYMBOLS = [
    "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "JPM", "V", "UNH",
    "SPY", "QQQ", "IWM", "AMD", "CRM", "NFLX", "BA", "DIS", "GS", "XOM",
]


def _log(msg: str) -> None:
    PROGRESS_LOG.parent.mkdir(parents=True, exist_ok=True)
    line = f"{date.today().isoformat()} {msg}"
    print(line, flush=True)
    with open(PROGRESS_LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def _load_manifest() -> dict:
    if MANIFEST.exists():
        try:
            return json.loads(MANIFEST.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"symbols": {}}


def fetch_yfinance_daily(symbol: str, years: int = 2,
                         max_history: bool = False) -> pd.DataFrame | None:
    try:
        t = yf.Ticker(symbol)
        if max_history or years <= 0:
            df = t.history(period="max", auto_adjust=True)
        else:
            end = date.today()
            start = end - timedelta(days=years * 365 + 30)
            df = t.history(start=start.isoformat(), end=end.isoformat(), auto_adjust=True)
        if df is None or df.empty:
            return None
        df = df.rename(columns={
            "Open": "Open", "High": "High", "Low": "Low",
            "Close": "Close", "Volume": "Volume",
        })
        df.index = pd.to_datetime(df.index)
        df["symbol"] = symbol
        return df
    except Exception as exc:
        _log(f"  yfinance error {symbol}: {exc}")
        return None


def fetch_alpaca_daily(symbol: str, years: int = 2) -> pd.DataFrame | None:
    api_key = os.getenv("ALPACA_API_KEY")
    api_secret = os.getenv("ALPACA_SECRET_KEY")
    if not api_key or not api_secret:
        return None
    try:
        from alpaca.data.historical import StockHistoricalDataClient
        from alpaca.data.requests import StockBarsRequest
        from alpaca.data.timeframe import TimeFrame

        client = StockHistoricalDataClient(api_key, api_secret)
        end = date.today()
        start = end - timedelta(days=max(years, 1) * 365)
        req = StockBarsRequest(
            symbol_or_symbols=symbol,
            timeframe=TimeFrame.Day,
            start=start,
            end=end,
        )
        bars = client.get_stock_bars(req)
        if symbol not in bars.data or not bars.data[symbol]:
            return None
        rows = [{
            "Open": b.open, "High": b.high, "Low": b.low,
            "Close": b.close, "Volume": b.volume,
        } for b in bars.data[symbol]]
        df = pd.DataFrame(rows, index=pd.to_datetime([b.timestamp for b in bars.data[symbol]]))
        df["symbol"] = symbol
        return df
    except Exception as exc:
        _log(f"  Alpaca error {symbol}: {exc}")
        return None


def save_symbol(symbol: str, df: pd.DataFrame) -> Path:
    HIST_STOCKS.mkdir(parents=True, exist_ok=True)
    out = HIST_STOCKS / f"{symbol}_daily.parquet"
    df.to_parquet(out, compression="snappy")
    return out


def symbol_already_fetched(symbol: str, skip_existing: bool) -> bool:
    if not skip_existing:
        return False
    path = HIST_STOCKS / f"{symbol}_daily.parquet"
    return path.exists() and path.stat().st_size > 500


def fetch_all(symbols: list[str], years: int = 2,
              prefer_alpaca: bool = False,
              max_history: bool = False,
              skip_existing: bool = True) -> dict:
    manifest = _load_manifest()
    manifest.setdefault("symbols", {})
    manifest["fetched"] = date.today().isoformat()
    manifest["years"] = "max" if max_history else years
    manifest["max_history"] = max_history

    ok, fail, skipped = 0, 0, 0
    _log(f"Starting fetch: {len(symbols)} symbols, max_history={max_history}, skip_existing={skip_existing}")

    for i, sym in enumerate(symbols):
        if symbol_already_fetched(sym, skip_existing):
            skipped += 1
            if (i + 1) % 100 == 0:
                _log(f"[{i+1}/{len(symbols)}] progress ok={ok} fail={fail} skipped={skipped}")
            continue

        _log(f"[{i+1}/{len(symbols)}] {sym} …")
        df = None
        if prefer_alpaca:
            df = fetch_alpaca_daily(sym, years if years > 0 else 10)
        if df is None:
            df = fetch_yfinance_daily(sym, years, max_history=max_history)
        if df is None or df.empty:
            fail += 1
            manifest["symbols"][sym] = {"status": "failed"}
            continue
        path = save_symbol(sym, df)
        ok += 1
        manifest["symbols"][sym] = {
            "status": "ok",
            "rows": len(df),
            "start": str(df.index.min().date()),
            "end": str(df.index.max().date()),
            "path": str(path.relative_to(REPO_ROOT)),
        }
        if (i + 1) % 50 == 0:
            MANIFEST.parent.mkdir(parents=True, exist_ok=True)
            manifest["summary"] = {"ok": ok, "failed": fail, "skipped": skipped,
                                   "total": len(symbols)}
            MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            _log(f"  checkpoint [{i+1}/{len(symbols)}] ok={ok} fail={fail} skipped={skipped}")
        time.sleep(0.12)

    manifest["summary"] = {"ok": ok, "failed": fail, "skipped": skipped, "total": len(symbols)}
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    _log(f"Done: {ok} OK, {fail} failed, {skipped} skipped / {len(symbols)} total. Manifest -> {MANIFEST}")
    return manifest


def probe_alpaca_options() -> int:
    api_key = os.getenv("ALPACA_API_KEY")
    if not api_key:
        print("Set ALPACA_API_KEY and ALPACA_SECRET_KEY to run api probe.")
        return 1
    probe = Path(__file__).resolve().parent / "api_probe_options.py"
    if not probe.exists():
        print("api_probe_options.py not found")
        return 1
    import subprocess
    return subprocess.call([sys.executable, str(probe)])


def main() -> int:
    ap = argparse.ArgumentParser(description="Fetch historical stock data locally")
    ap.add_argument("--symbols", default=None, help="comma-separated tickers")
    ap.add_argument("--years", type=int, default=0,
                    help="years of history (0 = use --max-history)")
    ap.add_argument("--max-history", action="store_true",
                    help="fetch maximum available daily history (yfinance period=max)")
    ap.add_argument("--universe-top", type=int, default=0,
                    help="fetch top N from options universe")
    ap.add_argument("--universe-full", action="store_true",
                    help="fetch entire ~900 ticker universe")
    ap.add_argument("--prefer-alpaca", action="store_true")
    ap.add_argument("--force", action="store_true", help="re-fetch even if parquet exists")
    ap.add_argument("--probe-alpaca", action="store_true", help="run Gate 1A probe")
    ap.add_argument("--then-historical", action="store_true",
                    help="after fetch, run historical backtest on all symbols")
    args = ap.parse_args()

    if args.probe_alpaca:
        return probe_alpaca_options()

    if args.universe_full:
        symbols = get_universe()
    elif args.universe_top > 0:
        symbols = get_universe()[:args.universe_top]
    elif args.symbols:
        symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
    else:
        symbols = DEFAULT_SYMBOLS

    max_hist = args.max_history or args.years <= 0
    years = args.years if args.years > 0 else 10

    fetch_all(symbols, years=years, prefer_alpaca=args.prefer_alpaca,
              max_history=max_hist, skip_existing=not args.force)

    if args.then_historical:
        import subprocess
        _log("Starting historical backtest on all downloaded symbols …")
        catalog = REPO_ROOT / "simulations" / "options_catalog_runner.py"
        subprocess.call([sys.executable, str(catalog), "--historical", "--all-symbols"],
                        cwd=str(REPO_ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
