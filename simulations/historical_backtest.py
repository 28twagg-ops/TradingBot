"""
historical_backtest.py
================================================================================
Historical options backtest engine — uses real stock paths (yfinance daily or
Alpaca 1-min parquet) + Black-Scholes option reconstruction when chain data
is unavailable.

Run standalone:
  python simulations/historical_backtest.py --symbols AAPL,MSFT,NVDA --years 2
  python simulations/historical_backtest.py --from-parquet data/stocks_1min/2026-07-02.parquet
"""

from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_strategy_registry import STRIKE_OFFSETS, StrategyDef, load_registry
from options_strategy_simulator import (
    SignalEvent, aggregate, bs_price, build_trade_log, model_spread,
    CONTRACT_MULTIPLIER, DEV_LABEL,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
HIST_DIR = REPO_ROOT / "data" / "historical"
RESULTS_DIR = Path(__file__).resolve().parent / "results" / "historical_backtest"

TRADING_DAYS = 252
GAP_DOWN_THRESH = -0.02
GAP_UP_THRESH = 0.02
GAP_STRONG_THRESH = -0.03
VOL_SPIKE_MULT = 2.0


@dataclass
class RawSignal:
    sdate: str
    symbol: str
    signal: str
    S_open: float
    S_prev_close: float
    S_close: float
    S_high: float
    S_low: float
    volume: float
    vol_avg: float
    gap_pct: float
    rsi: float | None = None


# --------------------------------------------------------------------------- #
#  Signal detectors (daily bar basis; intraday when 1-min parquet available)
# --------------------------------------------------------------------------- #

def _rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0).rolling(period).mean()
    loss = (-delta.clip(upper=0)).rolling(period).mean()
    rs = gain / loss.replace(0, np.nan)
    return 100 - (100 / (1 + rs))


def prepare_daily_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add gap, volume ratio, RSI to OHLCV dataframe indexed by date."""
    df = df.sort_index().copy()
    df["prev_close"] = df["Close"].shift(1)
    df["gap_pct"] = (df["Open"] - df["prev_close"]) / df["prev_close"]
    df["vol_avg20"] = df["Volume"].rolling(20).mean()
    df["vol_ratio"] = df["Volume"] / df["vol_avg20"]
    df["rsi14"] = _rsi(df["Close"])
    df["ret"] = df["Close"].pct_change()
    df["ma20"] = df["Close"].rolling(20).mean()
    df["high_52w"] = df["High"].rolling(252, min_periods=60).max()
    df["low_52w"] = df["Low"].rolling(252, min_periods=60).min()
    return df


def _match_signal(row: pd.Series, signal_type: str) -> bool:
    g = row.get("gap_pct", 0) or 0
    vr = row.get("vol_ratio", 1) or 1
    rsi = row.get("rsi14", 50) or 50
    c, o, ma = row.get("Close"), row.get("Open"), row.get("ma20")

    checks = {
        "gap_down": g <= GAP_DOWN_THRESH,
        "gap_down_strong": g <= GAP_STRONG_THRESH,
        "gap_down_weak": GAP_DOWN_THRESH < g <= -0.01,
        "gap_up": g >= GAP_UP_THRESH,
        "gap_down_vol": g <= GAP_DOWN_THRESH and vr >= VOL_SPIKE_MULT,
        "gap_up_low_vol": g >= GAP_UP_THRESH and vr < 1.0,
        "volume_spike": vr >= VOL_SPIKE_MULT,
        "pullback50": bool(ma and c and o and c > o and c > ma * 0.98),
        "pullback_ma": bool(ma and c and abs(c - ma) / ma < 0.01),
        "rsi_oversold": rsi < 30,
        "rsi_overbought": rsi > 70,
        "rsi_recovery": 30 <= rsi <= 45 and g <= -0.005,
        "high_52w_break": bool(row.get("high_52w") and c >= row["high_52w"] * 0.995),
        "low_52w_break": bool(row.get("low_52w") and c <= row["low_52w"] * 1.005),
        "low_52w": bool(row.get("low_52w") and c <= row["low_52w"] * 1.02),
        "mom_reversal": g <= -0.015 and c > o,
        "rubber_band": g <= -0.015 and c > (row.get("Low", c) + (row.get("High", c) - row.get("Low", c)) * 0.5),
        "orb_breakout": c > o * 1.008,
        "orb_breakdown": c < o * 0.992,
        "vwap_reclaim": c > o and g < 0,
        "vwap_reject": c < o and g > 0,
        "power_hour": abs(g) > 0.01,
        "power_hour_fade": g > 0.02 and c < o,
        "ten_am_reversal": g <= -0.01 and c > o,
        "breakdown": c < ma if ma else False,
        "momentum": c > ma if ma else False,
        "uptrend": c > ma if ma else False,
        "downtrend": c < ma if ma else False,
        "neutral": abs(g) < 0.005,
        "iv_rank_low": vr < 0.8,
        "iv_rank_high": vr > 1.5,
        "pre_earnings": False,  # needs calendar overlay
        "post_earnings_iv": vr > 1.8,
        "pre_event": vr > 1.3,
        "regime_bull": c > ma if ma else False,
        "regime_bear": c < ma if ma else False,
        "regime_corr": abs(g) > 0.03,
        "regime_low_vol": vr < 0.9,
        "seasonal": True,
        "macro_orb": abs(g) > 0.015,
        "opex_pin": False,
        "fomc": False,
        "month_end": False,
        "seasonal_jan": False,
        "seasonal_dec": False,
        "ex_div": False,
        "support_retest": c > ma if ma else False,
        "resistance_retest": c < ma if ma else False,
        "failed_breakout": g > 0.02 and c < o,
        "failed_breakdown": g < -0.02 and c > o,
        "gap_down_cont": g <= GAP_DOWN_THRESH and c < o,
        "earnings_positive": g > 0 and vr > 1.2,
        "earnings_negative": g < -0.03,
        "sector_leader": vr > 1.5 and c > o,
        "sector_laggard": vr > 1.5 and c < o,
        "macd_bull": c > ma if ma else False,
        "macd_bear": c < ma if ma else False,
        "iv_vs_hv_low": vr < 1.0,
        "iv_vs_hv_high": vr > 1.5,
        "term_contango": True,
        "term_backwardation": vr > 1.2,
        "term_inverted": vr > 1.3,
        "skew_steep": abs(g) > 0.02,
        "crash_hedge": g < -0.03,
        "vix_high": False,
        "uoa_call": vr > 2.5,
        "uoa_put": vr > 2.5 and g < 0,
        "pcr_high": g < -0.01,
        "pcr_low": g > 0.01,
        "max_pain": False,
        "gex_positive": abs(g) < 0.01,
        "gex_negative": abs(g) > 0.02,
        "dealer_flow": vr > 1.8,
        "oi_breakout": vr > 2.0,
        "pcr_skew": abs(g) > 0.015,
        "dark_pool": vr > 2.2,
        "fundamental_lag": True,
        "tape_imbalance": vr > 1.6,
        "open_imbalance": abs(g) > 0.015,
        "open_print": vr > 2.0 and abs(g) > 0.01,
        "midday_breakout": c > o * 1.005,
        "lunch_lull": vr < 0.7,
    }
    if signal_type in checks:
        val = checks[signal_type]
        return bool(val) if not isinstance(val, bool) else val
    # Default: gap_down family for unknown equity signals
    return g <= GAP_DOWN_THRESH


def detect_signals_from_daily(df: pd.DataFrame, symbol: str,
                              signal_type: str) -> list[RawSignal]:
    df = prepare_daily_features(df)
    return detect_signals_from_prepared(df, symbol, signal_type)


def detect_signals_from_prepared(df: pd.DataFrame, symbol: str,
                                 signal_type: str) -> list[RawSignal]:
    """Detect signals from an already feature-engineered daily dataframe."""
    out: list[RawSignal] = []
    for idx, row in df.iterrows():
        if pd.isna(row.get("prev_close")) or pd.isna(row.get("gap_pct")):
            continue
        if not _match_signal(row, signal_type):
            continue
        out.append(RawSignal(
            sdate=str(idx.date()) if hasattr(idx, "date") else str(idx)[:10],
            symbol=symbol,
            signal=signal_type,
            S_open=float(row["Open"]),
            S_prev_close=float(row["prev_close"]),
            S_close=float(row["Close"]),
            S_high=float(row["High"]),
            S_low=float(row["Low"]),
            volume=float(row["Volume"]),
            vol_avg=float(row.get("vol_avg20") or row["Volume"]),
            gap_pct=float(row["gap_pct"]),
            rsi=float(row["rsi14"]) if not pd.isna(row.get("rsi14")) else None,
        ))
    return out


def load_daily_parquet(stock_path: Path) -> tuple[str, pd.DataFrame]:
    df = pd.read_parquet(stock_path)
    if "Close" not in df.columns and "close" in df.columns:
        df = df.rename(columns={"close": "Close", "open": "Open",
                                "high": "High", "low": "Low", "volume": "Volume"})
    if "timestamp" in df.columns:
        df = df.set_index(pd.to_datetime(df["timestamp"]))
    else:
        df.index = pd.to_datetime(df.index)
    sym = stock_path.stem.upper().replace("_DAILY", "")
    return sym, prepare_daily_features(df)


def detect_signals_from_stocks(stocks_df: pd.DataFrame,
                               signal_type: str = "gap_down") -> list[RawSignal]:
    """Detect signals from Alpaca 1-min stock parquet (aggregated to daily)."""
    df = stocks_df.copy()
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
        df["date"] = df["timestamp"].dt.date
    elif "date" not in df.columns:
        raise ValueError("stocks parquet needs timestamp or date column")

    out: list[RawSignal] = []
    for sym, grp in df.groupby("symbol"):
        daily = grp.groupby("date").agg(
            Open=("open", "first"),
            High=("high", "max"),
            Low=("low", "min"),
            Close=("close", "last"),
            Volume=("volume", "sum"),
        )
        daily.index = pd.to_datetime(daily.index)
        out.extend(detect_signals_from_daily(daily, sym, signal_type))
    return out


def _realized_vol(close: pd.Series, window: int = 20) -> float:
    rets = close.pct_change().dropna()
    if len(rets) < 5:
        return 0.30
    return float(rets.tail(window).std() * math.sqrt(TRADING_DAYS))


def signals_to_events(raw: list[RawSignal], strategy: StrategyDef | None = None,
                      options_df: pd.DataFrame | None = None,
                      use_bs_fallback: bool = True,
                      hold_days: int = 1) -> list[SignalEvent]:
    """Convert raw equity signals to SignalEvent for the sim engine."""
    strategy = strategy or load_registry()[0]
    off = STRIKE_OFFSETS.get(strategy.strike_offset, 0.0)
    right = strategy.right
    dte = strategy.dte_default
    T = dte / 365.0
    side = strategy.side
    events: list[SignalEvent] = []

    for i, r in enumerate(raw):
        S0 = r.S_open
        if right == "C":
            K = round(S0 * (1 + off), 2)
        else:
            K = round(S0 * (1 - off), 2)

        iv = 0.28
        oi = 500

        if options_df is not None and len(options_df) > 0:
            day_opts = options_df[
                (options_df.get("underlying", options_df.get("symbol")) == r.symbol)
            ]
            if len(day_opts) > 0 and "implied_volatility" in day_opts.columns:
                ivs = day_opts["implied_volatility"].dropna()
                if len(ivs):
                    iv = float(ivs.median())
            if "open_interest" in day_opts.columns:
                ois = day_opts["open_interest"].dropna()
                if len(ois):
                    oi = int(ois.median())

        S_signal = S0
        S_next = S0 * (1 + r.gap_pct * 0.05)
        S_exit = r.S_close
        T_exit = max(0.0, T - hold_days / 365.0)

        events.append(SignalEvent(
            sig_id=i, sdate=r.sdate, symbol=r.symbol,
            mechanic=strategy.mechanic_key, right=right, strike=K,
            T_years=T, iv=iv, open_interest=oi,
            period="A" if i % 2 == 0 else "B",
            S_signal=S_signal, S_next=S_next, S_exit=S_exit,
            T_exit_years=T_exit, side=side,
        ))
    return events


def backtest_strategy_on_prepared(sym: str, df_feat: pd.DataFrame,
                                  strategy: StrategyDef,
                                  raw_cache: dict[str, list[RawSignal]],
                                  research_mode: bool = True) -> dict:
    sig_type = strategy.signal
    if sig_type not in raw_cache:
        raw_cache[sig_type] = detect_signals_from_prepared(df_feat, sym, sig_type)
    raw = raw_cache[sig_type]
    if not raw:
        return {"strategy_id": strategy.id, "symbol": sym, "signals_considered": 0}

    events = signals_to_events(raw, strategy=strategy)
    cost_cap = 2000.0 if research_mode else None
    trades = build_trade_log(events, max_contract_cost=cost_cap)
    agg = aggregate(trades)
    agg["strategy_id"] = strategy.id
    agg["strategy_name"] = strategy.name
    agg["symbol"] = sym
    agg["signal"] = sig_type
    agg["data_source"] = "historical_daily"
    return agg


def backtest_strategy_on_daily(stock_path: Path, strategy: StrategyDef,
                               signal_type: str | None = None,
                               research_mode: bool = True) -> dict:
    """Run one strategy on one symbol's daily CSV/parquet."""
    sym, df_feat = load_daily_parquet(stock_path)
    cache: dict[str, list[RawSignal]] = {}
    return backtest_strategy_on_prepared(sym, df_feat, strategy, cache, research_mode)


def list_downloaded_symbols() -> list[str]:
    stocks_dir = HIST_DIR / "stocks"
    if not stocks_dir.exists():
        return []
    out = []
    for p in sorted(stocks_dir.glob("*_daily.parquet")):
        sym = p.stem.replace("_daily", "").upper()
        out.append(sym)
    return out


def run_catalog_historical(symbols: list[str], strategies: list[StrategyDef] | None = None,
                           years: int = 2, resume: bool = True,
                           output_tag: str = "") -> pd.DataFrame:
    """Backtest all registry strategies on downloaded historical daily data."""
    strategies = strategies or load_registry()
    single_leg = [s for s in strategies if not s.multi_leg]
    HIST_DIR.mkdir(parents=True, exist_ok=True)
    tag = f"_{output_tag}" if output_tag else ""
    rows: list[dict] = []
    done_syms: set[str] = set()
    cp_path = RESULTS_DIR / f"catalog_historical_{date.today().isoformat()}{tag}_checkpoint.csv"
    if resume and cp_path.exists():
        cp = pd.read_csv(cp_path)
        if len(cp) and "symbol" in cp.columns:
            rows = cp.to_dict("records")
            done_syms = set(cp["symbol"].unique())
            print(f"Resuming: {len(done_syms)} symbols, {len(rows)} rows from checkpoint",
                  flush=True)

    pending = [s for s in symbols if s not in done_syms]
    print(f"Historical backtest{tag}: {len(pending)} pending + {len(done_syms)} done "
          f"of {len(symbols)} symbols x {len(single_leg)} strategies", flush=True)

    for si, sym in enumerate(pending):
        path = HIST_DIR / "stocks" / f"{sym}_daily.parquet"
        if not path.exists():
            continue
        try:
            sym_name, df_feat = load_daily_parquet(path)
        except Exception as exc:
            print(f"  skip {sym}: load error {exc}", flush=True)
            continue
        raw_cache: dict[str, list[RawSignal]] = {}
        for strat in single_leg:
            try:
                agg = backtest_strategy_on_prepared(
                    sym_name, df_feat, strat, raw_cache)
                if agg.get("signals_considered", 0) == 0:
                    continue
                rows.append({
                    "strategy_id": strat.id,
                    "strategy_name": strat.name,
                    "category": strat.category,
                    "symbol": sym_name,
                    "signal": strat.signal,
                    "signals": agg.get("signals_considered", 0),
                    "filled": agg.get("filled", 0),
                    "fill_rate": agg.get("fill_rate", 0),
                    "win_rate": agg.get("win_rate", 0),
                    "exp_pnl_per_signal": agg.get("exp_pnl_per_signal", 0),
                    "avg_return_pct": agg.get("avg_return_pct", 0),
                    "med_return_pct": agg.get("med_return_pct", 0),
                    "exp_return_pct_per_signal": agg.get("exp_return_pct_per_signal", 0),
                    "total_pnl": agg.get("total_pnl", 0),
                    "profit_factor": agg.get("profit_factor", 0),
                })
            except Exception as exc:
                rows.append({"strategy_id": strat.id, "symbol": sym_name,
                             "error": str(exc)})
        if (si + 1) % 10 == 0:
            total_done = len(done_syms) + si + 1
            print(f"  [{total_done}/{len(symbols)}] symbols, {len(rows)} result rows …",
                  flush=True)
            _checkpoint_historical(rows, output_tag)

    df = pd.DataFrame(rows)
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out = RESULTS_DIR / f"catalog_historical_{date.today().isoformat()}{tag}.csv"
    df.to_csv(out, index=False)
    print(f"Saved {len(df)} rows -> {out}", flush=True)
    return df


def _checkpoint_historical(rows: list[dict], output_tag: str = "") -> None:
    if not rows:
        return
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    tag = f"_{output_tag}" if output_tag else ""
    cp = RESULTS_DIR / f"catalog_historical_{date.today().isoformat()}{tag}_checkpoint.csv"
    pd.DataFrame(rows).to_csv(cp, index=False)


def merge_historical_shards(output_tag_prefix: str = "shard") -> Path:
    """Merge main checkpoint + parallel shard outputs into one CSV."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    day = date.today().isoformat()
    parts: list[pd.DataFrame] = []
    main_cp = RESULTS_DIR / f"catalog_historical_{day}_checkpoint.csv"
    if main_cp.exists():
        parts.append(pd.read_csv(main_cp))
    for p in sorted(RESULTS_DIR.glob(f"catalog_historical_{day}_{output_tag_prefix}*.csv")):
        if "_checkpoint" in p.name:
            continue
        parts.append(pd.read_csv(p))
    if not parts:
        raise FileNotFoundError("No historical shard files to merge")
    df = pd.concat(parts, ignore_index=True)
    if "symbol" in df.columns and "strategy_id" in df.columns:
        df = df.drop_duplicates(subset=["symbol", "strategy_id"], keep="last")
    out = RESULTS_DIR / f"catalog_historical_{day}_merged.csv"
    df.to_csv(out, index=False)
    print(f"Merged {len(df)} rows, {df['symbol'].nunique()} symbols -> {out}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Historical options backtest")
    ap.add_argument("--symbols", default="AAPL,MSFT,NVDA,SPY,JPM",
                    help="comma-separated tickers")
    ap.add_argument("--years", type=int, default=2)
    ap.add_argument("--strategy", default=None, help="strategy id e.g. S163")
    ap.add_argument("--from-parquet", default=None, help="Alpaca stocks parquet path")
    ap.add_argument("--all-symbols", action="store_true")
    ap.add_argument("--output-tag", default="", help="shard tag for parallel workers")
    ap.add_argument("--no-resume", action="store_true")
    args = ap.parse_args()

    print(f"[{DEV_LABEL}] historical backtest")
    registry = load_registry()

    if args.from_parquet:
        stocks = pd.read_parquet(args.from_parquet)
        strat = next((s for s in registry if s.id == (args.strategy or "S163")), registry[0])
        raw = detect_signals_from_stocks(stocks, strat.signal)
        events = signals_to_events(raw, strategy=strat)
        trades = build_trade_log(events)
        agg = aggregate(trades)
        print(f"Strategy {strat.id} {strat.name}: {agg}")
        return 0

    if args.all_symbols:
        symbols = list_downloaded_symbols()
    else:
        symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
    strats = registry
    if args.strategy:
        strats = [s for s in registry if s.id == args.strategy]
    df = run_catalog_historical(
        symbols, strats, years=args.years,
        resume=not args.no_resume, output_tag=args.output_tag,
    )
    print(f"Results: {len(df)} rows -> {RESULTS_DIR}")
    if len(df):
        top = df.sort_values("exp_pnl_per_signal", ascending=False).head(10)
        print(top[["strategy_id", "strategy_name", "symbol", "exp_pnl_per_signal", "filled"]].to_string())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
