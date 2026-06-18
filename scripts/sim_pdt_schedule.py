"""
Extensive simulation: intraday exits vs PDT overnight schedule (afternoon buy / morning sell).

Uses the live bot's signal + exit rules (imported from rubber_band_bot.py).
Data: yfinance daily OHLC (no Alpaca keys required for the sim itself).

Modes compared:
  intraday_full      — morning+afternoon entries, intraday stops, same-day stops OK (ideal cron)
  strict_pdt         — entries both windows, NO same-day sells (old live guard)
  overnight_pdt      — afternoon entries only, morning exits only (user proposal)
  overnight_cap3     — overnight + max 3 entries/day ($500 realism)
  intraday_cap3      — intraday_full + max 3 entries/day
  overnight_broker_stop — overnight + GTC stop at -0.5% (whole-share positions only)

Outputs: logs/analysis/pdt_schedule_sim_report.md + CSV tables
"""
from __future__ import annotations

import json
import math
import os
import sys
import time
import warnings
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import yfinance as yf

warnings.filterwarnings("ignore", category=FutureWarning)

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "logs" / "analysis"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Dummy keys so rubber_band_bot imports without exiting
os.environ.setdefault("ALPACA_API_KEY", "sim")
os.environ.setdefault("ALPACA_SECRET_KEY", "sim")
sys.path.insert(0, str(ROOT))

from rubber_band_bot import (  # noqa: E402
    add_ind,
    BULL_P,
    BEAR_P,
    CORR_P,
    CASH_RESERVE_PCT,
    EXIT_DAYS_MAX,
    EXIT_STOP_LOSS,
    MIN_TRADE_SIZE,
    MIN_HISTORY_DAYS,
    MIN_STOCK_PRICE,
    OFFSCHEDULE_SIZE_PCT,
    SCHEDULE,
    SEASONAL_SIZE_PCT,
    check_exit,
    consec_down,
    get_signals,
    regime,
)

# ---------------------------------------------------------------------------
# Simulation config
# ---------------------------------------------------------------------------

STARTING_EQUITY = 500.0
DATA_START = "2018-01-01"
DATA_END = "2025-12-31"
TICKER_LIMIT = 120  # subset for runtime; stratified across SP500 list

# Sub-periods for stress / OOS slices
PERIODS = {
    "full_8yr": ("2018-01-01", "2025-12-31"),
    "recent_3yr": ("2023-01-01", "2025-12-31"),
    "covid_stress": ("2020-02-01", "2020-06-30"),
    "bear_2022": ("2022-01-01", "2022-12-31"),
    "bull_2024": ("2024-01-01", "2024-12-31"),
}

ROLLING_OOS_YEARS = 3
ROLLING_STEP_MONTHS = 6


@dataclass
class SimMode:
    name: str
    label: str
    buy_morning: bool
    buy_afternoon: bool
    sell_morning: bool
    sell_intraday: bool
    sell_afternoon_eod: bool
    same_day_sell: bool
    max_entries_per_day: Optional[int] = None
    broker_stop_whole_share: bool = False  # GTC stop fills at stop_px if Low breaches


MODES: List[SimMode] = [
    SimMode(
        "intraday_full",
        "Current ideal (2 scans + intraday stops, same-day OK)",
        buy_morning=True, buy_afternoon=True,
        sell_morning=True, sell_intraday=True, sell_afternoon_eod=True,
        same_day_sell=True,
    ),
    SimMode(
        "strict_pdt",
        "Old live guard (no same-day sells, intraday after overnight)",
        buy_morning=True, buy_afternoon=True,
        sell_morning=True, sell_intraday=True, sell_afternoon_eod=True,
        same_day_sell=False,
    ),
    SimMode(
        "overnight_pdt",
        "Afternoon buy / morning sell only (PDT-safe)",
        buy_morning=False, buy_afternoon=True,
        sell_morning=True, sell_intraday=False, sell_afternoon_eod=False,
        same_day_sell=False,
    ),
    SimMode(
        "overnight_cap3",
        "Overnight schedule + max 3 entries/day",
        buy_morning=False, buy_afternoon=True,
        sell_morning=True, sell_intraday=False, sell_afternoon_eod=False,
        same_day_sell=False,
        max_entries_per_day=3,
    ),
    SimMode(
        "intraday_cap3",
        "Intraday full + max 3 entries/day",
        buy_morning=True, buy_afternoon=True,
        sell_morning=True, sell_intraday=True, sell_afternoon_eod=True,
        same_day_sell=True,
        max_entries_per_day=3,
    ),
    SimMode(
        "overnight_broker_stop",
        "Overnight + broker GTC stop on whole-share lots",
        buy_morning=False, buy_afternoon=True,
        sell_morning=True, sell_intraday=False, sell_afternoon_eod=False,
        same_day_sell=False,
        broker_stop_whole_share=True,
    ),
]


@dataclass
class Position:
    ticker: str
    strategy: str
    seasonal: bool
    entry_idx: int
    entry_date: str
    entry_price: float
    dollars: float
    shares: float
    broker_stop_active: bool = False


@dataclass
class Trade:
    ticker: str
    strategy: str
    entry_date: str
    exit_date: str
    entry_price: float
    exit_price: float
    pnl_pct: float
    pnl_dollar: float
    hold_days: int
    exit_reason: str
    overshoot_pct: float  # vs EXIT_STOP_LOSS when stop exit


@dataclass
class SimResult:
    mode: str
    period: str
    start_equity: float
    end_equity: float
    total_return_pct: float
    cagr_pct: float
    max_drawdown_pct: float
    sharpe: float
    trades: int
    wins: int
    win_rate_pct: float
    avg_hold_days: float
    avg_trade_pnl_pct: float
    stop_trades: int
    stop_avg_pnl_pct: float
    stop_overshoot_avg_pct: float
    day_trades_used: int
    entries_blocked_pdt: int = 0
    trades_list: List[Trade] = field(default_factory=list)


def _fetch_sp500_tickers() -> List[str]:
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        sp = pd.read_html(
            "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
            storage_options=headers,
        )[0]["Symbol"].tolist()
        return [t.replace(".", "-") for t in sp]
    except Exception:
        # Fallback liquid sample if Wikipedia fails
        return [
            "AAPL", "MSFT", "AMZN", "GOOGL", "META", "NVDA", "JPM", "V", "UNH", "XOM",
            "JNJ", "WMT", "PG", "MA", "HD", "CVX", "MRK", "ABBV", "KO", "PEP",
            "COST", "AVGO", "TMO", "MCD", "CSCO", "ACN", "ABT", "DHR", "TXN", "NEE",
            "LIN", "PM", "UNP", "RTX", "HON", "LOW", "UPS", "AMGN", "IBM", "CAT",
            "GE", "SPGI", "BA", "DE", "GS", "MS", "BLK", "AMD", "INTC", "QCOM",
        ]


def _download_data(tickers: List[str], start: str, end: str) -> Tuple[Dict[str, pd.DataFrame], pd.DataFrame]:
    print(f"Downloading {len(tickers)} tickers + SPY ({start} to {end})...")
    all_syms = list(dict.fromkeys(tickers + ["SPY"]))
    raw = pd.DataFrame()
    chunk = 80
    for i in range(0, len(all_syms), chunk):
        part = all_syms[i:i + chunk]
        try:
            d = yf.download(
                part, start=start, end=end, progress=False,
                auto_adjust=True, group_by="ticker", threads=True,
            )
            if d.empty:
                continue
            if raw.empty:
                raw = d
            else:
                raw = pd.concat([raw, d], axis=1)
        except Exception as e:
            print(f"  chunk {i} failed: {e}")
        print(f"  downloaded {min(i + chunk, len(all_syms))}/{len(all_syms)}")

    stock_data: Dict[str, pd.DataFrame] = {}
    if isinstance(raw.columns, pd.MultiIndex):
        for t in all_syms:
            try:
                sub = raw[t].dropna(how="all")
                if sub.empty or len(sub) < MIN_HISTORY_DAYS:
                    continue
                sub = sub.rename(columns=str.capitalize)
                if float(sub["Close"].iloc[-1]) < MIN_STOCK_PRICE:
                    continue
                stock_data[t] = add_ind(sub)
            except Exception:
                pass
    spy_df = stock_data.get("SPY")
    return stock_data, spy_df


def _regime_on_day(spy_df: pd.DataFrame, idx: int) -> str:
    sub = spy_df.iloc[:idx + 1]
    return regime(sub)


def _build_signal_cache(
    stock_data: Dict[str, pd.DataFrame],
    spy_df: pd.DataFrame,
    dates: List[pd.Timestamp],
) -> Dict[int, List[dict]]:
    """Precompute all entry signals once (major speedup)."""
    date_to_idx = {d: i for i, d in enumerate(dates)}
    regimes = [_regime_on_day(spy_df, i) for i in range(len(dates))]
    cache: Dict[int, List[dict]] = {i: [] for i in range(len(dates))}
    tickers = [t for t in stock_data if t != "SPY"]
    print(f"Precomputing signals for {len(tickers)} tickers...")
    for n, ticker in enumerate(tickers):
        df = stock_data[ticker]
        for loc in range(MIN_HISTORY_DAYS, len(df)):
            dt = df.index[loc]
            if dt not in date_to_idx:
                continue
            i = date_to_idx[dt]
            month = dt.month
            rgm = regimes[i]
            sub = df.iloc[:loc + 1]
            for s in get_signals(ticker, sub, month, rgm):
                cache[i].append(s)
        if n % 25 == 0:
            print(f"  signal cache {n}/{len(tickers)}")
    total = sum(len(v) for v in cache.values())
    print(f"  total signal slots: {total}")
    return cache


def _bar_on_date(df: pd.DataFrame, dt: pd.Timestamp) -> Optional[pd.Series]:
    if dt not in df.index:
        return None
    return df.loc[dt]


def _position_pnl_pct(pos: Position, price: float) -> float:
    if pos.entry_price <= 0:
        return 0.0
    return (price / pos.entry_price - 1.0) * 100.0


def _stop_price(entry: float) -> float:
    return entry * (1.0 + EXIT_STOP_LOSS)


def _can_sell_today(pos: Position, day_idx: int, mode: SimMode) -> bool:
    if mode.same_day_sell:
        return True
    return pos.entry_idx < day_idx


def _size_entries(
    equity: float,
    cash: float,
    n_signals: int,
    mode: SimMode,
) -> Tuple[float, float, int]:
    reserve = equity * CASH_RESERVE_PCT
    avail = max(0.0, cash - reserve)
    max_trades = max(1, int(avail // max(MIN_TRADE_SIZE, 0.01)))
    n_viable = max(1, n_signals)
    n_slots = min(n_viable, max_trades)
    if mode.max_entries_per_day is not None:
        n_slots = min(n_slots, mode.max_entries_per_day)
    equal_share = avail / n_slots if n_slots else 0.0
    sea_da = max(MIN_TRADE_SIZE, min(equity * SEASONAL_SIZE_PCT, equal_share))
    ratio = OFFSCHEDULE_SIZE_PCT / SEASONAL_SIZE_PCT
    off_da = max(MIN_TRADE_SIZE, min(equity * OFFSCHEDULE_SIZE_PCT, equal_share * ratio))
    return sea_da, off_da, n_slots


def _try_exit(
    pos: Position,
    day_idx: int,
    dates: List[pd.Timestamp],
    df: pd.DataFrame,
    price: float,
    reason: str,
    cash: float,
    trades: List[Trade],
    mode: SimMode,
) -> float:
    pnl_pct = _position_pnl_pct(pos, price)
    pnl_dollar = pos.dollars * (pnl_pct / 100.0)
    overshoot = 0.0
    if "stop" in reason.lower():
        overshoot = pnl_pct - (EXIT_STOP_LOSS * 100.0)
    trades.append(Trade(
        ticker=pos.ticker,
        strategy=pos.strategy,
        entry_date=pos.entry_date,
        exit_date=str(dates[day_idx].date()),
        entry_price=pos.entry_price,
        exit_price=price,
        pnl_pct=pnl_pct,
        pnl_dollar=pnl_dollar,
        hold_days=day_idx - pos.entry_idx,
        exit_reason=reason,
        overshoot_pct=overshoot,
    ))
    return cash + pos.dollars + pnl_dollar


def _evaluate_exits(
    positions: Dict[str, Position],
    day_idx: int,
    dates: List[pd.Timestamp],
    stock_data: Dict[str, pd.DataFrame],
    mode: SimMode,
    phase: str,
    cash: float,
    trades: List[Trade],
    day_trades: int,
) -> Tuple[Dict[str, Position], float, int]:
    """phase: 'morning_open' | 'intraday' | 'afternoon_close'"""
    to_remove = []
    for ticker, pos in list(positions.items()):
        if ticker not in stock_data:
            continue
        df = stock_data[ticker]
        if not _can_sell_today(pos, day_idx, mode):
            continue

        row = _bar_on_date(df, dates[day_idx])
        if row is None:
            continue
        open_px = float(row["Open"])
        low_px = float(row["Low"])
        close_px = float(row["Close"])
        stop_px = _stop_price(pos.entry_price)

        exit_price = None
        reason = ""

        # Broker GTC stop (whole shares): triggers on Low breach, fill at stop_px
        if mode.broker_stop_whole_share and pos.broker_stop_active and pos.shares >= 1.0:
            if low_px <= stop_px:
                exit_price = stop_px
                reason = f"broker_stop ({_position_pnl_pct(pos, exit_price):.1f}%)"

        if exit_price is None and phase == "morning_open" and mode.sell_morning:
            px = open_px
            pnl_frac = _position_pnl_pct(pos, px) / 100.0
            pos_stub = {"pnl_pct": _position_pnl_pct(pos, px), "entry_date": pos.entry_date}
            sub = df.loc[:dates[day_idx]]
            # Stop at open / gap
            if open_px <= stop_px or pnl_frac <= EXIT_STOP_LOSS:
                exit_price = open_px
                reason = f"stop_loss ({_position_pnl_pct(pos, exit_price):.1f}%)"
            elif (day_idx - pos.entry_idx) >= EXIT_DAYS_MAX:
                exit_price = px
                reason = f"max_hold ({_position_pnl_pct(pos, exit_price):+.1f}%)"
            else:
                ex, why = check_exit(sub, pos_stub, eod_only=False)
                if ex and "stop" in why or "max_hold" in why:
                    exit_price = px
                    reason = why

        if exit_price is None and phase == "intraday" and mode.sell_intraday:
            if low_px <= stop_px:
                exit_price = stop_px
                reason = f"stop_loss ({_position_pnl_pct(pos, exit_price):.1f}%)"

        if exit_price is None and phase == "afternoon_close" and mode.sell_afternoon_eod:
            px = close_px
            pnl_frac = _position_pnl_pct(pos, px) / 100.0
            pos_stub = {"pnl_pct": _position_pnl_pct(pos, px), "entry_date": pos.entry_date}
            sub = df.loc[:dates[day_idx]]
            if pnl_frac <= EXIT_STOP_LOSS:
                exit_price = px
                reason = f"stop_loss ({_position_pnl_pct(pos, exit_price):.1f}%)"
            elif (day_idx - pos.entry_idx) >= EXIT_DAYS_MAX:
                exit_price = px
                reason = f"max_hold ({_position_pnl_pct(pos, exit_price):+.1f}%)"
            else:
                ex, why = check_exit(sub, pos_stub, eod_only=True)
                if ex:
                    exit_price = px
                    reason = why

        if exit_price is not None:
            cash = _try_exit(pos, day_idx, dates, df, exit_price, reason, cash, trades, mode)
            to_remove.append(ticker)
            if pos.entry_idx == day_idx:
                day_trades += 1

    for t in to_remove:
        del positions[t]
    return positions, cash, day_trades


def run_simulation(
    mode: SimMode,
    stock_data: Dict[str, pd.DataFrame],
    spy_df: pd.DataFrame,
    dates: List[pd.Timestamp],
    signal_cache: Dict[int, List[dict]],
    start_idx: int,
    end_idx: int,
    starting_equity: float = STARTING_EQUITY,
) -> SimResult:
    cash = starting_equity
    positions: Dict[str, Position] = {}
    trades: List[Trade] = []
    day_trades = 0
    equity_curve: List[float] = []

    for day_idx in range(start_idx, end_idx + 1):
        dt = dates[day_idx]

        # Mark-to-market equity
        mtm = cash
        for t, pos in positions.items():
            df = stock_data.get(t)
            if df is None:
                continue
            row = _bar_on_date(df, dt)
            if row is not None:
                mtm += pos.dollars * (1 + _position_pnl_pct(pos, float(row["Close"])) / 100.0)
        equity_curve.append(mtm)
        equity = mtm

        positions, cash, day_trades = _evaluate_exits(
            positions, day_idx, dates, stock_data, mode, "morning_open", cash, trades, day_trades,
        )
        positions, cash, day_trades = _evaluate_exits(
            positions, day_idx, dates, stock_data, mode, "intraday", cash, trades, day_trades,
        )

        # Morning entries: signals from prior trading day close
        if mode.buy_morning and day_idx > start_idx:
            signals = [
                s for s in signal_cache.get(day_idx - 1, [])
                if s["ticker"] not in positions
            ]
            signals.sort(key=lambda s: (not s.get("seasonal"), s["strategy"]))
            sea_da, off_da, n_slots = _size_entries(equity, cash, len(signals), mode)
            entries_today = 0
            for sig in signals:
                if entries_today >= n_slots:
                    break
                ticker = sig["ticker"]
                if ticker in positions:
                    continue
                da = sea_da if sig.get("seasonal") else off_da
                if da > cash - equity * CASH_RESERVE_PCT:
                    continue
                df = stock_data[ticker]
                row = _bar_on_date(df, dt)
                if row is None:
                    continue
                px = float(row["Open"])
                if px <= 0:
                    continue
                shares = da / px
                whole = math.floor(shares)
                broker_stop = mode.broker_stop_whole_share and whole >= 1.0
                positions[ticker] = Position(
                    ticker=ticker,
                    strategy=sig["strategy"],
                    seasonal=sig.get("seasonal", False),
                    entry_idx=day_idx,
                    entry_date=str(dt.date()),
                    entry_price=px,
                    dollars=da,
                    shares=shares,
                    broker_stop_active=broker_stop,
                )
                cash -= da
                entries_today += 1

        positions, cash, day_trades = _evaluate_exits(
            positions, day_idx, dates, stock_data, mode, "afternoon_close", cash, trades, day_trades,
        )

        if mode.buy_afternoon:
            signals = [
                s for s in signal_cache.get(day_idx, [])
                if s["ticker"] not in positions
            ]
            signals.sort(key=lambda s: (not s.get("seasonal"), s["strategy"]))
            sea_da, off_da, n_slots = _size_entries(equity, cash, len(signals), mode)
            entries_today = 0
            for sig in signals:
                if entries_today >= n_slots:
                    break
                ticker = sig["ticker"]
                if ticker in positions:
                    continue
                da = sea_da if sig.get("seasonal") else off_da
                if da > cash - equity * CASH_RESERVE_PCT:
                    continue
                df = stock_data[ticker]
                row = _bar_on_date(df, dt)
                if row is None:
                    continue
                px = float(row["Close"])
                if px <= 0:
                    continue
                shares = da / px
                whole = math.floor(shares)
                broker_stop = mode.broker_stop_whole_share and whole >= 1.0
                positions[ticker] = Position(
                    ticker=ticker,
                    strategy=sig["strategy"],
                    seasonal=sig.get("seasonal", False),
                    entry_idx=day_idx,
                    entry_date=str(dt.date()),
                    entry_price=px,
                    dollars=da,
                    shares=shares,
                    broker_stop_active=broker_stop,
                )
                cash -= da
                entries_today += 1

    # Liquidate remaining at last close
    for ticker, pos in list(positions.items()):
        df = stock_data.get(ticker)
        if df is None:
            continue
        row = _bar_on_date(df, dates[end_idx])
        if row is None:
            continue
        px = float(row["Close"])
        cash = _try_exit(pos, end_idx, dates, df, px, "sim_end", cash, trades, mode)

    end_equity = cash
    ret_pct = (end_equity / starting_equity - 1.0) * 100.0

    n_days = max(1, end_idx - start_idx)
    years = n_days / 252.0
    cagr = ((end_equity / starting_equity) ** (1.0 / years) - 1.0) * 100.0 if years > 0 else 0.0

    eq = np.array(equity_curve) if equity_curve else np.array([starting_equity])
    peak = np.maximum.accumulate(eq)
    dd = (eq - peak) / peak
    max_dd = float(dd.min()) * 100.0

    daily_rets = np.diff(eq) / eq[:-1]
    sharpe = 0.0
    if len(daily_rets) > 1 and np.std(daily_rets) > 0:
        sharpe = float(np.mean(daily_rets) / np.std(daily_rets) * math.sqrt(252))

    wins = sum(1 for t in trades if t.pnl_dollar > 0)
    win_rate = (wins / len(trades) * 100.0) if trades else 0.0
    avg_hold = float(np.mean([t.hold_days for t in trades])) if trades else 0.0
    avg_pnl = float(np.mean([t.pnl_pct for t in trades])) if trades else 0.0
    stop_trades = [t for t in trades if "stop" in t.exit_reason.lower()]
    stop_avg = float(np.mean([t.pnl_pct for t in stop_trades])) if stop_trades else 0.0
    stop_overshoot = float(np.mean([t.overshoot_pct for t in stop_trades])) if stop_trades else 0.0

    return SimResult(
        mode=mode.name,
        period="",
        start_equity=starting_equity,
        end_equity=end_equity,
        total_return_pct=ret_pct,
        cagr_pct=cagr,
        max_drawdown_pct=max_dd,
        sharpe=sharpe,
        trades=len(trades),
        wins=wins,
        win_rate_pct=win_rate,
        avg_hold_days=avg_hold,
        avg_trade_pnl_pct=avg_pnl,
        stop_trades=len(stop_trades),
        stop_avg_pnl_pct=stop_avg,
        stop_overshoot_avg_pct=stop_overshoot,
        day_trades_used=day_trades,
        trades_list=trades,
    )


def _period_indices(dates: List[pd.Timestamp], start: str, end: str) -> Tuple[int, int]:
    s, e = pd.Timestamp(start), pd.Timestamp(end)
    idx_start = next((i for i, d in enumerate(dates) if d >= s), 0)
    idx_end = next((i for i in range(len(dates) - 1, -1, -1) if dates[i] <= e), len(dates) - 1)
    return idx_start, idx_end


def rolling_oos_windows(dates: List[pd.Timestamp]) -> List[Tuple[str, int, int]]:
    windows = []
    start_year = dates[0].year
    end_year = dates[-1].year
    y = start_year
    while y + ROLLING_OOS_YEARS <= end_year:
        for m in [1, 7]:
            start = pd.Timestamp(year=y, month=m, day=1)
            end = start + pd.DateOffset(years=ROLLING_OOS_YEARS) - pd.DateOffset(days=1)
            if end > dates[-1]:
                break
            i0, i1 = _period_indices(dates, str(start.date()), str(end.date()))
            if i1 - i0 > 252:
                label = f"{start.date()}_{end.date()}"
                windows.append((label, i0, i1))
        y += 1
    return windows


def main():
    t0 = time.time()
    tickers = _fetch_sp500_tickers()[:TICKER_LIMIT]
    stock_data, spy_df = _download_data(tickers, DATA_START, DATA_END)
    if spy_df is None or len(stock_data) < 30:
        print("ERROR: insufficient data")
        sys.exit(1)

    dates = list(spy_df.index)
    print(f"Loaded {len(stock_data)} tickers (cap {TICKER_LIMIT}), {len(dates)} trading days")
    signal_cache = _build_signal_cache(stock_data, spy_df, dates)

    all_results: List[SimResult] = []
    rolling_rows: List[dict] = []

    for period_name, (ps, pe) in PERIODS.items():
        i0, i1 = _period_indices(dates, ps, pe)
        if i1 <= i0 + MIN_HISTORY_DAYS:
            continue
        print(f"\n=== Period {period_name} ({ps} to {pe}) days {i0}-{i1} ===")
        for mode in MODES:
            r = run_simulation(mode, stock_data, spy_df, dates, signal_cache, i0, i1)
            r.period = period_name
            all_results.append(r)
            print(
                f"  {mode.name:22s}  ret {r.total_return_pct:+7.1f}%  "
                f"CAGR {r.cagr_pct:+6.1f}%  DD {r.max_drawdown_pct:6.1f}%  "
                f"trades {r.trades:4d}  stop_avg {r.stop_avg_pnl_pct:+.2f}%  "
                f"overshoot {r.stop_overshoot_avg_pct:+.2f}%"
            )

    # Rolling OOS
    print("\n=== Rolling 3yr OOS windows ===")
    oos_by_mode: Dict[str, List[float]] = {m.name: [] for m in MODES}
    for label, i0, i1 in rolling_oos_windows(dates):
        for mode in MODES:
            r = run_simulation(mode, stock_data, spy_df, dates, signal_cache, i0, i1)
            r.period = f"oos_{label}"
            all_results.append(r)
            oos_by_mode[mode.name].append(r.total_return_pct)
            rolling_rows.append({
                "window": label,
                "mode": mode.name,
                "return_pct": r.total_return_pct,
                "cagr_pct": r.cagr_pct,
                "max_dd_pct": r.max_drawdown_pct,
                "trades": r.trades,
                "stop_overshoot_avg_pct": r.stop_overshoot_avg_pct,
            })

    # Summary table for full period
    full_rows = []
    for mode in MODES:
        rs = [r for r in all_results if r.period == "full_8yr" and r.mode == mode.name]
        if not rs:
            continue
        r = rs[0]
        oos = oos_by_mode[mode.name]
        full_rows.append({
            "mode": mode.name,
            "label": next(m.label for m in MODES if m.name == mode.name),
            "total_return_pct": r.total_return_pct,
            "cagr_pct": r.cagr_pct,
            "max_dd_pct": r.max_drawdown_pct,
            "sharpe": r.sharpe,
            "trades": r.trades,
            "win_rate_pct": r.win_rate_pct,
            "avg_hold_days": r.avg_hold_days,
            "stop_trades": r.stop_trades,
            "stop_avg_pnl_pct": r.stop_avg_pnl_pct,
            "stop_overshoot_avg_pct": r.stop_overshoot_avg_pct,
            "day_trades": r.day_trades_used,
            "oos_windows": len(oos),
            "oos_avg_return_pct": float(np.mean(oos)) if oos else 0.0,
            "oos_median_return_pct": float(np.median(oos)) if oos else 0.0,
            "oos_positive_windows": sum(1 for x in oos if x > 0),
        })

    summary_df = pd.DataFrame(full_rows)
    period_df = pd.DataFrame([
        {
            "period": r.period,
            "mode": r.mode,
            "total_return_pct": r.total_return_pct,
            "cagr_pct": r.cagr_pct,
            "max_dd_pct": r.max_drawdown_pct,
            "sharpe": r.sharpe,
            "trades": r.trades,
            "win_rate_pct": r.win_rate_pct,
            "stop_overshoot_avg_pct": r.stop_overshoot_avg_pct,
        }
        for r in all_results
        if not r.period.startswith("oos_")
    ])
    rolling_df = pd.DataFrame(rolling_rows)

    summary_df.to_csv(OUT_DIR / "pdt_schedule_sim_summary.csv", index=False)
    period_df.to_csv(OUT_DIR / "pdt_schedule_sim_by_period.csv", index=False)
    rolling_df.to_csv(OUT_DIR / "pdt_schedule_sim_rolling_oos.csv", index=False)

    # Head-to-head: overnight vs intraday on full period
    intraday = summary_df[summary_df["mode"] == "intraday_full"].iloc[0]
    overnight = summary_df[summary_df["mode"] == "overnight_pdt"].iloc[0]
    overnight_c3 = summary_df[summary_df["mode"] == "overnight_cap3"].iloc[0]
    intraday_c3 = summary_df[summary_df["mode"] == "intraday_cap3"].iloc[0]
    strict = summary_df[summary_df["mode"] == "strict_pdt"].iloc[0]
    broker = summary_df[summary_df["mode"] == "overnight_broker_stop"].iloc[0]

    verdict_lines = []
    if overnight["total_return_pct"] > intraday["total_return_pct"]:
        verdict_lines.append(
            f"Overnight schedule **beats** intraday full on total return "
            f"({overnight['total_return_pct']:+.1f}% vs {intraday['total_return_pct']:+.1f}%)."
        )
    else:
        verdict_lines.append(
            f"Intraday full **beats** overnight schedule on total return "
            f"({intraday['total_return_pct']:+.1f}% vs {overnight['total_return_pct']:+.1f}%)."
        )

    if overnight_c3["stop_overshoot_avg_pct"] < strict["stop_overshoot_avg_pct"]:
        verdict_lines.append(
            f"Overnight+cap3 reduces stop overshoot vs strict PDT hold "
            f"({overnight_c3['stop_overshoot_avg_pct']:+.2f}% vs {strict['stop_overshoot_avg_pct']:+.2f}%)."
        )

    report = [
        "# PDT Schedule Simulation Report",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Universe: S&P 500 sample ({len(stock_data)} tickers, limit {TICKER_LIMIT})",
        f"Starting equity: ${STARTING_EQUITY:.0f}",
        f"Stop: {EXIT_STOP_LOSS*100:.1f}% | Max hold: {EXIT_DAYS_MAX}d | Reserve: {CASH_RESERVE_PCT*100:.0f}%",
        "",
        "## Executive summary",
        "",
    ] + [f"- {line}" for line in verdict_lines] + [
        "",
        "## Full 8-year comparison (2018–2025)",
        "",
        "| Mode | Return | CAGR | Max DD | Sharpe | Trades | Win% | Stop avg | Overshoot | Day trades | OOS avg |",
        "|------|--------|------|--------|--------|--------|------|----------|-----------|------------|---------|",
    ]

    for _, row in summary_df.sort_values("total_return_pct", ascending=False).iterrows():
        report.append(
            f"| {row['mode']} | {row['total_return_pct']:+.1f}% | {row['cagr_pct']:+.1f}% | "
            f"{row['max_dd_pct']:.1f}% | {row['sharpe']:.2f} | {int(row['trades'])} | "
            f"{row['win_rate_pct']:.1f}% | {row['stop_avg_pnl_pct']:+.2f}% | "
            f"{row['stop_overshoot_avg_pct']:+.2f}% | {int(row['day_trades'])} | "
            f"{row['oos_avg_return_pct']:+.1f}% |"
        )

    def _pivot_md(df, valcol):
        pt = df.pivot_table(index="period", columns="mode", values=valcol)
        lines = ["| period | " + " | ".join(pt.columns) + " |", "|---|" + "|".join(["---"] * len(pt.columns)) + "|"]
        for idx, row in pt.iterrows():
            cells = " | ".join(f"{v:+.1f}" if not pd.isna(v) else "n/a" for v in row)
            lines.append(f"| {idx} | {cells} |")
        return "\n".join(lines)

    report.extend([
        "",
        "## By stress period (return %)",
        "",
        _pivot_md(period_df, "total_return_pct"),
        "",
        "## Stop overshoot by period (avg % worse than -0.5%)",
        "",
        _pivot_md(period_df, "stop_overshoot_avg_pct"),
        "",
        "## Mode definitions",
        "",
        "- **intraday_full**: Morning + afternoon entries; intraday stop checks; same-day stops allowed; EOD midline.",
        "- **strict_pdt**: Same entries; no same-day sells (old live guard); intraday stops after overnight only.",
        "- **overnight_pdt**: Afternoon entries only; morning exits only (your proposal).",
        "- **overnight_cap3**: Overnight schedule + max 3 new positions per day.",
        "- **intraday_cap3**: Intraday full + max 3 entries/day.",
        "- **overnight_broker_stop**: Overnight schedule + GTC stop on whole-share lots.",
        "",
        "## Interpretation for $500 account",
        "",
        "1. **PDT constraint**: overnight modes use **0 same-day round trips** for exits; intraday modes generate day trades.",
        "2. **Stop overshoot**: strict PDT (hold losers overnight) usually worsens stop fills; overnight morning exit is a middle ground.",
        "3. **Cap 3 entries**: concentrates capital (~$100+/position) — compare overnight_cap3 vs intraday_cap3.",
        "4. Daily-bar sim approximates 15-min cron; real slippage may differ.",
        "",
        f"Runtime: {time.time() - t0:.1f}s",
        "",
        "## Files",
        "",
        "- `pdt_schedule_sim_summary.csv`",
        "- `pdt_schedule_sim_by_period.csv`",
        "- `pdt_schedule_sim_rolling_oos.csv`",
    ])

    report_path = OUT_DIR / "pdt_schedule_sim_report.md"
    report_path.write_text("\n".join(report), encoding="utf-8")
    print(f"\nReport written: {report_path}")
    print(f"Total runtime: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
