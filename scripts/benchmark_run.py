"""Lightweight timing harness for fetch_batch and mode detection (no broker calls)."""
import time
from pathlib import Path

# Run from repo root
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from rubber_band_bot import fetch_batch, detect_mode, get_live_tickers, FETCH_WORKERS


def bench_fetch_sample():
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "JPM", "V"]
    t0 = time.time()
    data = fetch_batch(tickers, label="bench")
    elapsed = time.time() - t0
    print(f"fetch_batch({len(tickers)} tickers, workers={FETCH_WORKERS}): {elapsed:.1f}s -> {len(data)} valid")


def bench_ticker_cache():
    t0 = time.time()
    tickers = get_live_tickers()
    elapsed = time.time() - t0
    print(f"get_live_tickers: {elapsed:.1f}s -> {len(tickers)} tickers")


def main():
    print("Mode detection:", detect_mode())
    bench_ticker_cache()
    bench_fetch_sample()


if __name__ == "__main__":
    main()
