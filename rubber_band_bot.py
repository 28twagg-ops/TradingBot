# -*- coding: utf-8 -*-
"""
RUBBER BAND BOT v8  *** UPDATED 2026-05-05 ***
========================================================================
FIXES IN THIS VERSION (v8):
  1. ensure_stop()    — switched from stop-LIMIT to stop-MARKET (GTC)
                        stop-limit at -1% won't fill on a -6% overnight gap;
                        stop-market fills at the open price no matter how big the gap.
  2. place_all_stops()— NEW: called after every buy loop AND at the start of exits.
                        Ensures every position always has a GTC stop, even if
                        placement failed on a prior run or bot missed a morning run.
  3. cancel_stop_orders() — called before every software-triggered sell to avoid
                        double-sell conflicts with the GTC stop.
  4. log_tx()         — explicit file flush + stderr fallback so no transaction
                        is ever silently lost even if disk write fails.
  5. run_exits()      — calls place_all_stops() at start to catch gaps from missed runs.
  6. run_scan()       — calls place_all_stops() after buy loop (5s wait for fills).
========================================================================
FIXES IN v7:
  1. enrich()      — entry date now uses NEWEST BUY order (not oldest order of any side)
  2. detect_mode() — scan window is 3:45-4:10pm ET using real Eastern time (zoneinfo)
  3. run_bot.yml   — uses explicit pip install (no requirements.txt needed)
========================================================================
Calendar-aware, regime-switching, multi-strategy trading bot.
Runs on GitHub Actions triggered by cron-job.org.

CHANGES FROM v6 (sim-validated across 2yr/3yr/5yr/7yr, 900 stocks):
  - Exit simplified: midline only (price > 20-day MA)
    Removed momentum decay layer + RSI requirement
    Midline alone was the most consistent exit across every timeframe
  - Max hold: 14d -> 3d (rolling 16-window OOS avg +153.9% vs 5d +127.7%, 2026-05-03)
  - Stop loss tightened: -3% -> -2% (deep sweep: tighter = better OOS)
    Reasoning: 2x slippage floor means -5% stop = -10% worst-case loss.
    Cutting to -2% (floor -4%) caps losses and recycles cash faster.
  - Position sizing: 20% seasonal / 12% off-schedule (tiered by strategy)
  - Removed MAX_OPEN_POSITIONS cap: cash availability is the real constraint

  ENTRY STRATEGIES (bake-off validated, 5yr/20yr 900 stocks):
    ACTIVE:  RSIRecovery (10/16 OOS wins as scheduled primary -- Apr/May/Nov, 2026-05-03)
             RubberBand  (51.7% win, 0.84 Sharpe -- off-schedule + Oct)
             52wkLow     (53.4% win, 0.60 Sharpe)
             MomReversal (54.4% win, 0.47 Sharpe, lowest drawdown)
             GapDown     (53.9% win, 0.51 Sharpe -- panic-to-recovery)
             VolumeSpike (58.5% win, consistent all regimes -- institutional)
             Pullback50  (58.2% win -- uptrend dip-buy)
    REMOVED: GoldenCross (negative Sharpe, lost money)

WHAT RUNS WHEN (auto-detected by US Eastern time, DST-aware via zoneinfo):
  9:30–9:43am ET  -> morning_prep (cache signals/exits for morning scan)
  9:44–9:59am ET  -> morning_scan (exits + entries)
  10:00am–3:29pm  -> exits-only
  3:30–3:43pm ET  -> evening_prep (cache for evening scan)
  3:44–3:59pm ET  -> scan / scan_evening (exits + entries + daily log)
  4:00pm–8:00pm ET -> post-market exits-only (extended hours)
  Weekend         -> weekly summary, no trading
  Other           -> status summary, no trading

LOGS committed back to repo after every run:
  logs/daily/YYYY-MM-DD.md
  logs/weekly/YYYY-WNN.md
  logs/transactions.csv
  logs/runs.csv

GITHUB SECRETS required:
  ALPACA_API_KEY
  ALPACA_SECRET_KEY
"""

import os, json, time, logging, csv, math, random
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, date
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

from alpaca.trading.client   import TradingClient
from alpaca.trading.requests import (MarketOrderRequest, GetOrdersRequest,
                                      StopOrderRequest, StopLimitOrderRequest,
                                      LimitOrderRequest)
from alpaca.trading.enums    import (OrderSide, TimeInForce, QueryOrderStatus,
                                     OrderType, OrderStatus)
from alpaca.data.historical  import StockHistoricalDataClient
from alpaca.data.requests    import StockBarsRequest, StockLatestQuoteRequest
from alpaca.data.timeframe   import TimeFrame

# Cap hung network calls (Alpaca / yfinance / Wikipedia). Without this, a stalled
# socket can block the entire GHA job indefinitely (see May 27 timeout crash).
socket.setdefaulttimeout(45)

# alpaca-py 0.43.2 TradingClient.__init__ still has no timeout= (params: api_key,
# secret_key, oauth_token, paper, raw_data, url_override). RESTClient has retry_*
# but no request timeout either. Closed 2026-07-25A: keep socket.setdefaulttimeout(45)
# as the best available cap; recheck when alpaca-py adds a real timeout kwarg.
# GHA installs with: pip install --upgrade alpaca-py ...


# =============================================================================
#  KEYS
# =============================================================================

API_KEY    = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")

if not API_KEY or not API_SECRET:
    print("ERROR: Set ALPACA_API_KEY and ALPACA_SECRET_KEY as environment variables.")
    raise SystemExit(1)


# =============================================================================
#  CONFIGURATION
# =============================================================================

PAPER_TRADING = False  # LIVE -- real money

# ---- Universe ----------------------------------------------------------------
# "sp500"   -- S&P 500 only (~500 stocks, faster)
# "midcap"  -- S&P MidCap 400 only (~400 stocks)
# "both"    -- S&P 500 + MidCap 400 (~900 stocks, more signals)
UNIVERSE = "both"

# ---- Position sizing ---------------------------------------------------------
# Sim-validated (7yr, 900 stocks, multiple runs):
#   Seasonal signals  (primary + secondary from monthly schedule): 20%
#   Off-schedule signals (other 4 strategies firing off-schedule): 20%
#
#   Sweep result (7yr, 900 stocks):
#     20%/20% beats 20%/12% by +121pp total return (Test 18, 2026-05-10)
#     while keeping sizing simple and symmetric.
#
#   Weak-month reduction (Feb/Mar/Sep → 5%) was tested and rejected:
#     Reduces total return by ~52pp and OOS by ~18pp vs no reduction.
#     Even underperforming months generate enough profitable trades at
#     full sizing to outweigh the savings from cutting size.
# Schedule removal 2026-07-18: SEASONAL_SIZE_PCT no longer used.
# All strategies use OFFSCHEDULE_SIZE_PCT = 0.20 regardless of month.
# SCHEDULE dict retained for reference and display only.
SEASONAL_SIZE_PCT    = 0.20   # RETAINED (unused for sizing since 2026-07-18 schedule removal)
OFFSCHEDULE_SIZE_PCT = 0.20   # all strategies equal weight (schedule removed 2026-07-18)
CASH_RESERVE_PCT     = 0.05   # sim-validated at 5% (Test 18)
MIN_TRADE_SIZE       = 0.01   # effectively no floor while keeping sizing math safe

# ---- Exit rules (v7 -- deep param sweep validated, 7yr 899 stocks) ----------
# Midline only: price crosses above 20-day moving average
# Deep sweep (15 combos: 5 stops x 3 holds) winner by OOS return:
#   -2% stop / 5d hold  →  OOS +113.6%,  OOS DD 11.6%,  OOS win 55.0%
# Tighter stop (-2% floor -4%) cuts losses fast, recycles cash sooner.
# Every step wider (-2.5 → -3 → -4 → -5%) reduced OOS return despite
# higher win rate, because the 2x slippage floor magnifies wide-stop losses.
EXIT_DAYS_MAX      = 3       # OOS-validated: 3d beats 5d (Test 10 rolling 16-window avg: +153.9% vs +127.7%)
EXIT_STOP_LOSS     = -0.005  # OOS-validated: -0.5% beats -2.0% (16/16 rolling windows, 20yr)

# Strategies disabled after live performance analysis (2026-07-20).
# Signal functions (_gd, _vs) are retained for potential re-enable.
# Disable evidence:
#   GapDown:    n=102, PF=0.49, avg=-0.99%, total=-$12.63, t***
#               77/102 exits were stop_loss averaging -2.14%
#               June primary month drag confirmed consistent underperf
#   VolumeSpike: n=44, PF=0.41, avg=-0.56%, total=-$1.05, t***
#               39/44 exits were stop_loss, avg hold 0.3d, WR 11%
DISABLED_STRATEGIES = {
    "GapDown",
    "VolumeSpike",
}

# ---- Extended-hours selling --------------------------------------------------
# Post-market limit sells (4pm–8pm ET) using DAY orders (DAY allowed on
# fractional shares; GTC is not). Limit = cur × 0.9985 (wider spread than
# regular hours, ~3×). If unfilled by market open, 9:35am run re-evaluates.
# No overnight GTC stop issue — these are DAY orders that expire the same day.
# Scan runs at 3:44-3:59pm ET — regular market hours — so exits during the
# scan always use regular market sells (limit → market fallback).
# Extended-hours sells (limit only, no fallback) are only used in
# run_exits(extended_hours=True) which covers 4pm-8pm ET.
USE_EXTENDED_HOURS_SELL = False
WEEKLY_MAX_HOLDINGS_PRINT = 8

# ---- Daily entry cap ---------------------------------------------------------
# MAX_OPEN_POSITIONS caps concurrent holdings so ~$500 accounts get ~$90/slot
# (whole-share broker GTC stops) instead of 30+ fractional fragments.
MAX_OPEN_POSITIONS = 5
# Max entries per scan also bounded by floor(avail / MIN_TRADE_SIZE).

# ---- Earnings filter ---------------------------------------------------------
# Skip buy signals if the stock has earnings within this many calendar days.
# Sim-validated 2026-05-13: filtering down-gap >3% events adds +16.4pp CAGR
# (196.6% → 213.0%) with only 2% of signals filtered out.
# yfinance calendar is ~70-80% reliable so this catches most but not all.
EARNINGS_SKIP_DAYS = 2

# ---- Data quality ------------------------------------------------------------
MIN_STOCK_PRICE  = 5.0
MIN_HISTORY_DAYS = 220

# ---- Paths -------------------------------------------------------------------
LOG_DIR    = Path("logs")
DAILY_DIR  = LOG_DIR / "daily"
WEEKLY_DIR = LOG_DIR / "weekly"
PLAN_DIR   = LOG_DIR / "plans"
CACHE_DIR  = LOG_DIR / "cache"
TX_FILE    = LOG_DIR / "transactions.csv"
EXEC_AUDIT_FILE = LOG_DIR / "execution_audit.csv"
RUNS_FILE  = LOG_DIR / "runs.csv"
STOP_LOSS_LOOK_FILE = LOG_DIR / "stop_losses_to_look_into.txt"
FRACTIONAL_WATCH_FILE = LOG_DIR / "fractional_watch.json"
AB_TEST_DIR           = LOG_DIR / "ab_test"
AB_TEST_REGISTRY_FILE = AB_TEST_DIR / "registry.json"
AB_TEST_DASHBOARD     = AB_TEST_DIR / "dashboard.md"
AB_TEST_WEEK_REVIEW   = AB_TEST_DIR / "week_review.md"
AB_TEST_TRADES_CSV    = AB_TEST_DIR / "trades_sorted.csv"
MORNING_PLAN_FILE = PLAN_DIR / "morning_plan.json"
EVENING_PLAN_FILE = PLAN_DIR / "evening_plan.json"
PLAN_MAX_AGE_MIN = 120
USE_TWO_PHASE_PLAN = True
# Strategy timing: entries at evening scan only (Phase 3 sim will confirm vs any-time).
# TODO(phase3): rename PREFER_EVENING_ENTRIES after schedule mode sims (D3).
# PDT-safe schedule was evening-only (Jun 2026); dual window re-enabled when day trading allowed.
EVENING_ONLY_ENTRIES = False

# ---- A/B concentration test (1 week) -----------------------------------------
# Virtual 50/50 equity split; no fixed position cap — only group budget + ratio.
#   Group A (wide):        ~AB_RATIO_A_TO_B names per 1 B name, smaller size
#   Group B (concentrated): 1 per ratio block, larger size
# Each scan: shuffle all viable signals, split by ratio, size = half_budget / count.
AB_TEST_ENABLED      = True
AB_TEST_DAYS         = 7
AB_TEST_START        = ""     # auto-set on first run if empty (YYYY-MM-DD)
AB_TEST_EQUITY_SPLIT = 0.50
AB_RATIO_A_TO_B      = 5     # target ~5 wide (A) for every 1 concentrated (B)

# Alpaca account: read only .equity / .cash via get_account_safe().
# Deprecated Jul 6 2026: pattern_day_trader, daytrade_count, daytrading_buying_power — never used here.
FETCH_WORKERS = 16
FETCH_CHUNK_PAUSE_S = 0.25

_run_started_at = None
_last_cache_hit = False

for d in [LOG_DIR, DAILY_DIR, WEEKLY_DIR, PLAN_DIR, CACHE_DIR, AB_TEST_DIR]:
    d.mkdir(parents=True, exist_ok=True)

W = 72   # display box inner width


# =============================================================================
#  CALENDAR STRATEGY SCHEDULE  (v7 bake-off validated)
#  DISPLAY / REFERENCE ONLY since 2026-07-18 — does NOT affect entry priority
#  or sizing. Live data (May–Jul 2026): off-schedule WR 34% vs scheduled 21%.
#  All 7 strategies run every day at OFFSCHEDULE_SIZE_PCT.
#
#  Changes from v6:
#    - GoldenCross REMOVED (negative Sharpe, lost money)
#    - GapDown ADDED (53.9% win, 0.51 Sharpe) -- replaces GoldenCross in Sep
#    - VolumeSpike ADDED (58.5% win, all-regime consistent) -- secondary
#    - Pullback50 ADDED (58.2% win, uptrend dip-buy) -- secondary in bull months
# =============================================================================

SCHEDULE = {
    1:  {"p": "MomReversal", "s": "52wkLow",     "note": "Jan: MomReversal primary, 52wkLow secondary"},
    2:  {"p": "52wkLow",     "s": "VolumeSpike",  "note": "Feb: 52wkLow + VolumeSpike (58.5% win)"},
    3:  {"p": "GapDown",     "s": "52wkLow",      "note": "Mar: GapDown primary (20yr IS+OOS confirmed)"},
    4:  {"p": "RubberBand",  "s": "Pullback50",   "note": "Apr: RubberBand reverted (Test 14: RB wins 3/3 OOS windows; RSIRecovery Apr negative EV -0.548%, Test 27 2026-05-10)"},
    5:  {"p": "RubberBand",  "s": "52wkLow",      "note": "May: RubberBand reverted (Test 14: RB wins 3/3 OOS windows vs RSIRecovery schedule, 2026-05-10)"},
    6:  {"p": "GapDown",     "s": "VolumeSpike",  "note": "Jun: GapDown primary (20yr IS+OOS confirmed)"},
    7:  {"p": "52wkLow",     "s": "Pullback50",   "note": "Jul: 52wkLow + Pullback50 (bull dip-buy)"},
    8:  {"p": "VolumeSpike", "s": "52wkLow",      "note": "Aug: VolumeSpike primary (20yr IS+OOS confirmed 2026-05-02)"},
    9:  {"p": "GapDown",     "s": "VolumeSpike",  "note": "Sep: GapDown replaces GoldenCross + VolSpike"},
    10: {"p": "RubberBand",  "s": "GapDown",      "note": "Oct: RubberBand + GapDown (53.9% win)"},
    11: {"p": "RubberBand",  "s": "MomReversal",  "note": "Nov: RubberBand reverted (Test 14: RB wins 3/3 OOS windows vs RSIRecovery schedule, 2026-05-10)"},
    12: {"p": "MomReversal", "s": "VolumeSpike",  "note": "Dec: MomReversal + VolumeSpike year-end"},
}

MN = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",
      7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}

BULL_P = {"consec_down":5, "rsi_thresh":25, "bb_std":2.5, "vol_z_min":1.5, "require_ma200":True}
CORR_P = {"consec_down":3, "rsi_thresh":30, "bb_std":2.0, "vol_z_min":0.5, "require_ma200":False}
BEAR_P = {"consec_down":5, "rsi_thresh":20, "bb_std":2.5, "vol_z_min":1.0, "require_ma200":False}


# =============================================================================
#  LOGGING
# =============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger("RBv8")


# =============================================================================
#  DISPLAY
# =============================================================================

def _trunc(s, n):
    s = str(s)
    return s if len(s) <= n else s[:n-1] + "~"

def hdr(title=""):
    bar = "=" * W
    print(f"\n+{bar}+")
    if title:
        t  = f"  {title}  "
        if len(t) > W: t = t[:W]
        lp = (W - len(t)) // 2
        rp = W - len(t) - lp
        print(f"|{' '*lp}{t}{' '*rp}|")
        print(f"+{bar}+")

def ftr():  print(f"+{'='*W}+")
def div():  print(f"+{'-'*W}+")
def blank():print(f"|{' '*W}|")

def row(label="", value=""):
    label = str(label); value = str(value)
    if value:
        val_max = min(len(value), W - 6)
        val_str = _trunc(value, val_max)
        lbl_max = W - 4 - len(val_str)
        lbl_str = _trunc(label, max(1, lbl_max))
        content = f"  {lbl_str:<{max(1,lbl_max)}}  {val_str}"
    else:
        content = f"  {_trunc(label, W-2)}"
    if len(content) > W: content = content[:W]
    print(f"|{content}{' '*(W-len(content))}|")

def trow(*cols, widths=None):
    if widths is None:
        w_each = W // max(len(cols), 1)
        widths = [w_each] * len(cols)
    parts   = [_trunc(str(c), w) for c, w in zip(cols, widths)]
    padded  = [f"{p:<{w}}" for p, w in zip(parts, widths)]
    content = ("  " + "  ".join(padded))[:W]
    print(f"|{content}{' '*(W-len(content))}|")


def _append_stoploss_look_items(items, mode):
    """Append non-duplicate stop-loss investigations to one persistent text file."""
    if not items:
        return 0

    existing_ids = set()
    if STOP_LOSS_LOOK_FILE.exists():
        try:
            with open(STOP_LOSS_LOOK_FILE, encoding="utf-8") as f:
                for line in f:
                    if line.startswith("ID: "):
                        existing_ids.add(line[4:].strip())
        except Exception:
            pass

    lines = []
    if not STOP_LOSS_LOOK_FILE.exists():
        lines.extend([
            "STOP LOSSES TO LOOK INTO",
            "=" * 72,
            "This file records stop-loss breaches where expected exit did not complete.",
            "Duplicates are prevented by (ticker + entry_date).",
            "",
        ])

    added = 0
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for item in items:
        item_id = item["id"]
        if item_id in existing_ids:
            continue
        lines.extend([
            "-" * 72,
            f"Timestamp: {ts}",
            f"ID: {item_id}",
            f"Mode: {mode}",
            f"Ticker: {item['ticker']}",
            f"Strategy: {item.get('strategy', '?')}",
            f"Entry date: {item.get('entry_date', 'unknown')}",
            f"P&L at breach: {item['pnl_frac']*100:+.2f}%",
            f"Stop threshold: {EXIT_STOP_LOSS*100:+.2f}%",
            f"Root cause: {item['root_cause']}",
            f"Explanation: {item['explanation']}",
            "",
        ])
        existing_ids.add(item_id)
        added += 1

    if lines:
        with open(STOP_LOSS_LOOK_FILE, "a", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines))
            if not lines[-1].endswith("\n"):
                f.write("\n")
    return added


# =============================================================================
#  UNIVERSE
# =============================================================================

def _ticker_cache_path():
    return CACHE_DIR / f"tickers_{date.today().isoformat()}.json"


def get_live_tickers():
    cache_path = _ticker_cache_path()
    if cache_path.exists():
        try:
            cached = json.loads(cache_path.read_text(encoding="utf-8"))
            tickers = cached.get("tickers", [])
            if tickers:
                log.info(f"  Universe cache hit: {len(tickers)} tickers ({cache_path.name})")
                return tickers
        except Exception as e:
            log.warning(f"  Ticker cache read failed: {e}")

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    log.info(f"Fetching tickers (universe={UNIVERSE})...")
    sp500, mid400 = [], []

    if UNIVERSE in ("sp500", "both"):
        try:
            sp500 = pd.read_html(
                "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
                storage_options=headers)[0]["Symbol"].tolist()
            log.info(f"  S&P 500: {len(sp500)}")
        except Exception as e:
            # Do not kill the whole run — GHA evenings still need exits/summary.
            log.error(f"S&P 500 fetch failed (non-fatal if cache exists): {e}")
            sp500 = []

    if UNIVERSE in ("midcap", "both"):
        try:
            mid400 = pd.read_html(
                "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies",
                storage_options=headers)[0]["Symbol"].tolist()
            log.info(f"  MidCap 400: {len(mid400)}")
        except Exception as e:
            log.error(f"MidCap 400 fetch failed (non-fatal if cache exists): {e}")
            mid400 = []

    if not sp500 and not mid400:
        # Last resort: any older cache file in the ticker cache dir.
        try:
            cache_dir = cache_path.parent
            cands = sorted(cache_dir.glob("tickers_*.json"), reverse=True)
            for p in cands:
                raw = json.loads(p.read_text(encoding="utf-8"))
                tickers = raw.get("tickers") or []
                if tickers:
                    log.warning(f"  Using stale ticker cache {p.name} ({len(tickers)} symbols)")
                    return tickers
        except Exception as e:
            log.error(f"  Stale ticker cache fallback failed: {e}")
        log.error("FATAL: no tickers available (Wikipedia + cache failed)")
        raise SystemExit(1)

    combined = list(dict.fromkeys(sp500 + mid400))
    cleaned  = [t.replace(".", "-") for t in combined]
    log.info(f"  Total: {len(cleaned)} tickers")
    try:
        cache_path.write_text(
            json.dumps({"date": str(date.today()), "tickers": cleaned}, indent=2),
            encoding="utf-8",
        )
    except Exception as e:
        log.warning(f"  Ticker cache write failed: {e}")
    return cleaned


# =============================================================================
#  DATA
# =============================================================================

_dc = None
def _get_dc():
    global _dc
    if _dc is None: _dc = StockHistoricalDataClient(API_KEY, API_SECRET)
    return _dc

def _alpaca(ticker, days=300):
    try:
        req  = StockBarsRequest(symbol_or_symbols=ticker, timeframe=TimeFrame.Day,
                                start=datetime.today()-timedelta(days=days+30))
        bars = _get_dc().get_stock_bars(req).df
        if bars.empty: return None
        if isinstance(bars.index, pd.MultiIndex):
            lvl0 = bars.index.get_level_values(0)
            if ticker not in lvl0: return None
            bars = bars.xs(ticker, level="symbol")
        bars.index = pd.to_datetime(bars.index)
        bars = bars.rename(columns={"open":"Open","high":"High","low":"Low",
                                     "close":"Close","volume":"Volume"})
        df = bars[["Open","High","Low","Close","Volume"]].dropna()
        return df if len(df) >= MIN_HISTORY_DAYS else None
    except Exception: return None

def _yf(ticker, days=300):
    try:
        df = yf.download(ticker,
                         start=datetime.today()-timedelta(days=days+60),
                         end=datetime.today(), progress=False, auto_adjust=True)
        if df.empty or len(df) < MIN_HISTORY_DAYS: return None
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        return df[["Open","High","Low","Close","Volume"]].dropna()
    except Exception: return None

def fetch_stock(ticker):
    df = _alpaca(ticker)
    if df is None or df.empty: df = _yf(ticker)
    if df is None or df.empty: return None
    if float(df["Close"].iloc[-1]) < MIN_STOCK_PRICE: return None
    return df

def add_ind(df):
    c, v = df["Close"], df["Volume"]
    o    = df["Open"]
    df   = df.copy()
    d = c.diff()
    g = d.clip(lower=0).rolling(14).mean()
    l = (-d.clip(upper=0)).rolling(14).mean()
    df["RSI"]   = 100 - 100 / (1 + g / (l + 1e-10))
    df["BBL25"] = c.rolling(20).mean() - 2.5 * c.rolling(20).std()
    df["BBL20"] = c.rolling(20).mean() - 2.0 * c.rolling(20).std()
    df["BBM"]   = c.rolling(20).mean()
    avg = v.rolling(20).mean(); sv = v.rolling(20).std()
    df["VZ"]    = (v - avg) / (sv + 1e-10)
    df["MA50"]  = c.rolling(50).mean()
    df["MA200"] = c.rolling(200).mean()
    df["L252"]  = c.rolling(252).min()
    df["R60"]   = c.pct_change(60)
    df["Ret1"]  = c.pct_change(1)
    # -- New strategy indicators (v7 bake-off validated) ----------------------
    df["GapPct"] = (o - c.shift(1)) / (c.shift(1) + 1e-10)  # gap from prev close
    df["Green"]  = (c > o).astype(int)                        # green candle
    # -- Pattern strategies (2026-07-22B) --------------------------------------
    df["BBU20"] = c.rolling(20).mean() + 2.0 * c.rolling(20).std()
    df["BBW"] = (df["BBU20"] - df["BBL20"]) / (df["BBM"] + 1e-10)
    df["VWAP5"] = ((df["High"] + df["Low"] + df["Close"]) / 3).rolling(5).mean()
    return df

def fetch_batch(tickers, label=""):
    if not tickers:
        return {}
    data = {}
    chunk_size = 40
    # Alpaca HTTP pool is effectively ~10 connections per host by default.
    # Keep worker count below that to avoid noisy "Connection pool is full"
    # warnings during prep/scans while preserving parallel fetch speed.
    workers = min(FETCH_WORKERS, 8, max(1, len(tickers)))

    def _fetch_one(t):
        df = fetch_stock(t)
        if df is not None:
            return t, add_ind(df)
        return t, None

    for i in range(0, len(tickers), chunk_size):
        chunk = tickers[i:i + chunk_size]
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(_fetch_one, t): t for t in chunk}
            for fut in as_completed(futures):
                try:
                    t, df = fut.result()
                    if df is not None:
                        data[t] = df
                except Exception as e:
                    log.debug(f"  fetch_batch {futures[fut]}: {e}")
        log.info(f"  [{label}] {min(i + chunk_size, len(tickers))}/{len(tickers)} ({len(data)} valid)")
        if i + chunk_size < len(tickers):
            time.sleep(FETCH_CHUNK_PAUSE_S)
    return data


# =============================================================================
#  REGIME
# =============================================================================

def regime(spy_df):
    if spy_df is None or len(spy_df) < 210: return "bull"
    r = float(spy_df["Close"].iloc[-1]) / (float(spy_df["MA200"].iloc[-1]) + 1e-10)
    return "bull" if r >= 1.0 else "correction" if r >= 0.93 else "bear"

def consec_down(close):
    vals = close.values; n = 0
    for i in range(len(vals)-1, 0, -1):
        if vals[i] < vals[i-1]: n += 1
        else: break
    return n


# =============================================================================
#  ENTRY SIGNALS  (v7 -- bake-off validated, updated 2026-05-03)
#
#  ACTIVE:
#    RSIRecovery  -- RSI crosses back above 30 after oversold (Test 14: 10/16 OOS wins)
#                    Replaces RubberBand as primary in Apr, May, Nov
#    RubberBand   -- 51.7% win, 0.84 Sharpe (best Sharpe of all)
#    52wkLow      -- 53.4% win, 0.60 Sharpe, 83.6% return
#    MomReversal  -- 54.4% win, 0.47 Sharpe, 129% return, lowest DD
#    GapDown      -- 53.9% win, 0.51 Sharpe, 93.5% return
#    VolumeSpike  -- 58.5% win (highest!), consistent across all regimes
#    Pullback50   -- 58.2% win, uptrend dip-buy, low risk
#
#  REMOVED:
#    GoldenCross  -- negative Sharpe, lost money over 5 years
# =============================================================================

def _rb(ticker, df, p):
    try:
        c = df["Close"]; cn = float(c.iloc[-1]); rsi = float(df["RSI"].iloc[-1])
        bb = float(df["BBL25" if p["bb_std"] >= 2.4 else "BBL20"].iloc[-1])
        vz = float(df["VZ"].iloc[-1]); ma200 = float(df["MA200"].iloc[-1])
        cd = consec_down(c)
        if any(pd.isna(x) for x in [rsi, bb, vz, ma200]): return None
        c1 = (cd >= p["consec_down"]) or (rsi < p["rsi_thresh"])
        c2 = cn <= bb; c3 = vz >= p["vol_z_min"]
        c4 = (cn > ma200) if p["require_ma200"] else True
        if c1 and c2 and c3 and c4:
            return {"ticker": ticker, "strategy": "RubberBand",
                    "close": round(cn, 2), "rsi": round(rsi, 1), "vol_z": round(vz, 2),
                    "trigger": "RSI" if rsi < p["rsi_thresh"] else f"{cd}d-down"}
    except Exception: pass
    return None

def _52(ticker, df):
    try:
        cn = float(df["Close"].iloc[-1]); low = float(df["L252"].iloc[-1])
        rsi = float(df["RSI"].iloc[-1]); vz = float(df["VZ"].iloc[-1])
        if any(pd.isna(x) for x in [low, rsi]): return None
        if (cn <= low * 1.05) and (vz >= 0.5) and (rsi > 10):
            return {"ticker": ticker, "strategy": "52wkLow",
                    "close": round(cn, 2), "rsi": round(rsi, 1), "vol_z": round(vz, 2),
                    "trigger": f"{((cn/low)-1)*100:.1f}% above 52wk low"}
    except Exception: pass
    return None

def _mr(ticker, df):
    try:
        c = df["Close"]; cn = float(c.iloc[-1]); r60 = float(df["R60"].iloc[-1])
        r5 = float(c.pct_change(5).iloc[-1])
        rsi = float(df["RSI"].iloc[-1]); vz = float(df["VZ"].iloc[-1])
        if any(pd.isna(x) for x in [r60, r5, rsi]): return None
        if (r60 < -0.12) and (r5 > -0.02) and (rsi < 40) and (vz >= 0.3):
            return {"ticker": ticker, "strategy": "MomReversal",
                    "close": round(cn, 2), "rsi": round(rsi, 1), "vol_z": round(vz, 2),
                    "trigger": f"{r60*100:.1f}% drop/60d stabilising"}
    except Exception: pass
    return None

def _gd(ticker, df):
    """GapDown reversal: open gaps down >=3% but close is green."""
    try:
        cn  = float(df["Close"].iloc[-1])
        gap = float(df["GapPct"].iloc[-1])
        grn = int(df["Green"].iloc[-1])
        rsi = float(df["RSI"].iloc[-1])
        vz  = float(df["VZ"].iloc[-1])
        if pd.isna(gap): return None
        if gap <= -0.03 and grn == 1:
            return {"ticker": ticker, "strategy": "GapDown",
                    "close": round(cn, 2), "rsi": round(rsi, 1), "vol_z": round(vz, 2),
                    "trigger": f"gap {gap*100:.1f}% recovered"}
    except Exception: pass
    return None

def _vs(ticker, df):
    """VolumeSpike: very high volume while price holds flat/up."""
    try:
        c = df["Close"]; cn = float(c.iloc[-1])
        vz  = float(df["VZ"].iloc[-1])
        rsi = float(df["RSI"].iloc[-1])
        r5  = float(c.pct_change(5).iloc[-1])
        if any(pd.isna(x) for x in [vz, r5]): return None
        if vz >= 2.5 and r5 >= -0.01 and r5 <= 0.05:
            return {"ticker": ticker, "strategy": "VolumeSpike",
                    "close": round(cn, 2), "rsi": round(rsi, 1), "vol_z": round(vz, 2),
                    "trigger": f"vol z={vz:.1f} 5d={r5*100:+.1f}%"}
    except Exception: pass
    return None

def _pb(ticker, df):
    """Pullback50: uptrend stock pulls back to touch 50MA, closes green."""
    try:
        cn   = float(df["Close"].iloc[-1])
        ma50 = float(df["MA50"].iloc[-1])
        ma200= float(df["MA200"].iloc[-1])
        grn  = int(df["Green"].iloc[-1])
        rsi  = float(df["RSI"].iloc[-1])
        vz   = float(df["VZ"].iloc[-1])
        if any(pd.isna(x) for x in [ma50, ma200]): return None
        in_uptrend = cn > ma200
        near_50ma  = abs(cn - ma50) / ma50 <= 0.01
        if in_uptrend and near_50ma and grn == 1:
            return {"ticker": ticker, "strategy": "Pullback50",
                    "close": round(cn, 2), "rsi": round(rsi, 1), "vol_z": round(vz, 2),
                    "trigger": f"50MA bounce ({((cn/ma50)-1)*100:+.1f}%)"}
    except Exception: pass
    return None

def _rsi(ticker, df):
    """RSIRecovery: RSI crosses back above 30 after being oversold.
    More precise than RubberBand's raw RSI threshold — requires the actual
    recovery cross rather than just being in oversold territory.
    Test 14 (20yr, 16 rolling OOS windows): RSI schedule wins 10/16 vs baseline 6/16.
    Replaces RubberBand as primary in Apr, May, Nov.
    """
    try:
        c = df["Close"]; cn = float(c.iloc[-1])
        rsi      = float(df["RSI"].iloc[-1])
        rsi_prev = float(df["RSI"].iloc[-2])
        vz       = float(df["VZ"].iloc[-1])
        grn      = int(df["Green"].iloc[-1])
        if any(pd.isna(x) for x in [rsi, rsi_prev, vz]): return None
        if (rsi_prev < 30              # was oversold yesterday
                and rsi >= 30          # crossed back above 30 today
                and vz >= 0.3          # some volume confirmation
                and grn == 1):         # price confirms recovery
            return {"ticker": ticker, "strategy": "RSIRecovery",
                    "close": round(cn, 2), "rsi": round(rsi, 1), "vol_z": round(vz, 2),
                    "trigger": f"RSI {rsi_prev:.1f}→{rsi:.1f} cross above 30"}
    except Exception: pass
    return None


def _maq(ticker, df):
    """MA_Squeeze: Bollinger bandwidth near 20d min, then upside breakout on volume."""
    try:
        if len(df) < 45:
            return None
        cn = float(df["Close"].iloc[-1])
        bbw = float(df["BBW"].iloc[-1])
        bbu = float(df["BBU20"].iloc[-1])
        vz = float(df["VZ"].iloc[-1])
        ma50 = float(df["MA50"].iloc[-1])
        rsi = float(df["RSI"].iloc[-1])
        bbw_min = float(df["BBW"].rolling(20).min().shift(1).iloc[-1])
        if any(pd.isna(x) for x in [bbw, bbu, vz, ma50, bbw_min]):
            return None
        if (bbw < bbw_min * 1.05 and cn > bbu and vz >= 1.5 and cn > ma50):
            return {"ticker": ticker, "strategy": "MA_Squeeze",
                    "close": round(cn, 2), "rsi": round(rsi, 1), "vol_z": round(vz, 2),
                    "trigger": f"BBW squeeze breakout VZ={vz:.1f}"}
    except Exception:
        pass
    return None


def _gp(ticker, df):
    """GoldenPocket: Fib 61.8–65% retracement bounce in MA200 uptrend."""
    try:
        if len(df) < 210:
            return None
        cn = float(df["Close"].iloc[-1])
        ma200 = float(df["MA200"].iloc[-1])
        grn = int(df["Green"].iloc[-1])
        vz = float(df["VZ"].iloc[-1])
        rsi = float(df["RSI"].iloc[-1])
        swing_high = float(df["High"].rolling(20).max().iloc[-1])
        swing_low = float(df["Low"].rolling(20).min().iloc[-1])
        if any(pd.isna(x) for x in [ma200, swing_high, swing_low, vz]):
            return None
        rng = swing_high - swing_low
        if rng <= 0:
            return None
        fib_618 = swing_high - 0.618 * rng
        fib_650 = swing_high - 0.650 * rng
        if cn > ma200 and fib_650 <= cn <= fib_618 and grn == 1 and vz >= 0.5:
            return {"ticker": ticker, "strategy": "GoldenPocket",
                    "close": round(cn, 2), "rsi": round(rsi, 1), "vol_z": round(vz, 2),
                    "trigger": "fib 61.8-65% bounce"}
    except Exception:
        pass
    return None


def _vr(ticker, df):
    """VWAP_Reclaim: dipped below 5d VWAP proxy, closed back above on volume."""
    try:
        if len(df) < 55:
            return None
        cn = float(df["Close"].iloc[-1])
        lo = float(df["Low"].iloc[-1])
        vwap5 = float(df["VWAP5"].iloc[-1])
        vz = float(df["VZ"].iloc[-1])
        ma50 = float(df["MA50"].iloc[-1])
        grn = int(df["Green"].iloc[-1])
        rsi = float(df["RSI"].iloc[-1])
        if any(pd.isna(x) for x in [vwap5, vz, ma50]):
            return None
        if lo < vwap5 and cn > vwap5 and vz >= 1.0 and cn > ma50 and grn == 1:
            return {"ticker": ticker, "strategy": "VWAP_Reclaim",
                    "close": round(cn, 2), "rsi": round(rsi, 1), "vol_z": round(vz, 2),
                    "trigger": f"VWAP reclaim VZ={vz:.1f}"}
    except Exception:
        pass
    return None


def _tr(ticker, df):
    """TrendResumption: HH/HL structure, 2–4d pullback, then break prior high."""
    try:
        if len(df) < 210:
            return None
        c = df["Close"]
        cn = float(c.iloc[-1])
        ma50 = float(df["MA50"].iloc[-1])
        ma200 = float(df["MA200"].iloc[-1])
        vz = float(df["VZ"].iloc[-1])
        rsi = float(df["RSI"].iloc[-1])
        prior_high = float(df["High"].iloc[-2])
        if any(pd.isna(x) for x in [ma50, ma200, vz, prior_high]):
            return None
        hh_struct = float(df["High"].iloc[-10]) < float(df["High"].iloc[-5])
        pullback_days = sum(
            float(c.iloc[-i]) < float(c.iloc[-i - 1]) for i in range(1, 4)
        )
        if (hh_struct and pullback_days >= 2 and cn > prior_high
                and cn > ma50 and cn > ma200 and vz >= 0.3):
            return {"ticker": ticker, "strategy": "TrendResumption",
                    "close": round(cn, 2), "rsi": round(rsi, 1), "vol_z": round(vz, 2),
                    "trigger": f"HH/HL resumption after {pullback_days}d pullback"}
    except Exception:
        pass
    return None


def _ed(ticker, df):
    """EarningsDrift: post +3% gap/volume spike continuation within 5 days."""
    try:
        if len(df) < 30:
            return None
        cn = float(df["Close"].iloc[-1])
        prev = float(df["Close"].iloc[-2])
        ma20 = float(df["BBM"].iloc[-1])  # MA20
        rsi = float(df["RSI"].iloc[-1])
        vz = float(df["VZ"].iloc[-1])
        if any(pd.isna(x) for x in [prev, ma20, rsi, vz]):
            return None
        recent = df.iloc[-6:-1]
        days_since = None
        for offset, (_, row) in enumerate(recent.iloc[::-1].iterrows(), start=1):
            gap = float(row["GapPct"]) if not pd.isna(row["GapPct"]) else None
            rvz = float(row["VZ"]) if not pd.isna(row["VZ"]) else None
            if gap is not None and rvz is not None and gap >= 0.03 and rvz >= 2.0:
                days_since = offset
                break
        if days_since is None:
            return None
        if (cn > prev and cn > ma20 and cn < ma20 * 1.10
                and rsi < 70 and vz >= 0.5):
            return {"ticker": ticker, "strategy": "EarningsDrift",
                    "close": round(cn, 2), "rsi": round(rsi, 1), "vol_z": round(vz, 2),
                    "trigger": f"post-earnings continuation day {days_since}"}
    except Exception:
        pass
    return None


def get_signals(ticker, df, month, rgm):
    """Check all active strategies every day.

    Schedule removal 2026-07-18: every hit is tagged seasonal=False so all
    strategies share equal entry priority and OFFSCHEDULE_SIZE_PCT sizing.
    The SCHEDULE dict is display/reference only.
    """
    # Bear override REMOVED 2026-05-10: Test 16 shows following monthly schedule
    # in bear regime outperforms the 52wkLow+MomReversal override (2/3 OOS windows).
    # The override was never validated before; now tested, it loses OOS.
    prm = BULL_P if rgm == "bull" else CORR_P if rgm == "correction" else BEAR_P

    checks = {
        "RubberBand": lambda: _rb(ticker, df, prm),
        "RSIRecovery": lambda: _rsi(ticker, df),
        "52wkLow": lambda: _52(ticker, df),
        "MomReversal": lambda: _mr(ticker, df),
        "GapDown": lambda: _gd(ticker, df),      # disabled
        "VolumeSpike": lambda: _vs(ticker, df),  # disabled
        "Pullback50": lambda: _pb(ticker, df),
        "MA_Squeeze": lambda: _maq(ticker, df),
        "GoldenPocket": lambda: _gp(ticker, df),
        "VWAP_Reclaim": lambda: _vr(ticker, df),
        "TrendResumption": lambda: _tr(ticker, df),
        "EarningsDrift": lambda: _ed(ticker, df),
    }
    sigs = []
    for name, fn in checks.items():
        if name in DISABLED_STRATEGIES:
            continue
        s = fn()
        if s:
            s["seasonal"] = False  # schedule removed 2026-07-18: all strategies equal
            sigs.append(s)
    # Deterministic order only — no seasonal priority tier
    sigs.sort(key=lambda x: x["strategy"])
    return sigs


def has_earnings_soon(ticker: str) -> bool:
    """Return True if this ticker has earnings within EARNINGS_SKIP_DAYS.

    Uses yfinance .calendar (forward-looking only). Reliability ~70-80%.
    Sim-validated 2026-05-13: skipping earnings-window buys adds +16.4pp CAGR.
    Only called for tickers that already fired a buy signal (~10-30 per scan),
    not for the full 900-stock universe — API overhead is minimal.
    """
    try:
        cal = yf.Ticker(ticker).calendar
        if cal is None or (hasattr(cal, "empty") and cal.empty):
            return False
        # yfinance returns a DataFrame; 'Earnings Date' is in the index
        if "Earnings Date" in cal.index:
            earn_dt = cal.loc["Earnings Date"].iloc[0]
            if hasattr(earn_dt, "date"):
                earn_dt = earn_dt.date()
            days_away = (earn_dt - date.today()).days
            if 0 <= days_away <= EARNINGS_SKIP_DAYS:
                return True
    except Exception:
        pass
    return False


# =============================================================================
#  EXIT LOGIC  (v7 -- midline only, sim-validated)
#
#  Sim tested 7 exit strategies across 2/3/7yr windows with 900 stocks.
#  Midline (price > 20-day MA) was the most consistent winner:
#    - 48.5% win rate, 0.078% avg return per trade
#    - Beat RSI+midline combo (v6), momentum decay, 2nd derivative
#    - 7-day hold recycles capital faster than 14-day at $500 accounts
#
#  Exit triggers (in priority order):
#    1. Stop loss: P&L <= -3%
#    2. Max hold:  held >= 7 days
#    3. Midline:   price > 20-day moving average
# =============================================================================

def check_exit(df, pos, eod_only=False):
    """Check exit conditions.
    eod_only=False  (intraday 15-min runs): stop-loss + max-hold only.
                    Midline skipped — sim shows intraday midline checks hurt
                    win rate by 7.9pp due to premature exits on brief MA touches.
    eod_only=True   (3:50pm EOD scan): all exits including midline.
                    Midline is validated against closing prices, matching the
                    sim that produced our 53.9% win rate."""
    try:
        c_now  = float(df["Close"].iloc[-1])
        mid    = float(df["BBM"].iloc[-1])
        pnl    = pos.get("pnl_pct", 0) / 100

        if pd.isna(mid):
            return False, ""

        # Hard stops first -- override everything (always checked)
        if pnl <= EXIT_STOP_LOSS:
            return True, f"stop_loss ({pnl*100:.1f}%)"

        if pos.get("entry_date"):
            try:
                days = (datetime.today() -
                        datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days
                if days >= EXIT_DAYS_MAX:
                    return True, f"max_hold {days}d ({pnl*100:+.1f}%)"
            except Exception: pass

        # Midline exit: only at EOD (3:50pm scan) — not intraday
        if eod_only and c_now > mid:
            return True, f"midline ({pnl*100:+.1f}%)"

    except Exception: pass
    return False, ""


# =============================================================================
#  POSITIONS
# =============================================================================

def get_account_safe(client, retries=3, wait=10):
    """Retry wrapper for Alpaca account fetch — mid-run timeouts lost entire
    entry sessions (e.g. 2026-05-27). Prefer this over bare client calls."""
    for i in range(retries):
        try:
            return client.get_account()
        except Exception as e:
            if i < retries - 1:
                log.warning(
                    f"get_account failed attempt {i + 1}/{retries}: {e} "
                    f"retrying in {wait}s"
                )
                time.sleep(wait)
            else:
                log.error(f"get_account failed after {retries} attempts: {e}")
                raise


def get_positions(client):
    try:
        out = {}
        for p in client.get_all_positions():
            out[p.symbol] = {
                "ticker": p.symbol, "qty": float(p.qty),
                "market_value": float(p.market_value),
                "entry_price": float(p.avg_entry_price),
                "current_price": float(p.current_price),
                "pnl_pct": float(p.unrealized_plpc) * 100,
                "pnl_dollar": float(p.unrealized_pl),
                "dollar_amt": float(p.market_value),
                "entry_date": "", "strategy": "unknown",
            }
        return out
    except Exception as e:
        log.error(f"get_positions failed: {e}"); return {}

def enrich(client, positions):
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.CLOSED, limit=200)
        orders = client.get_orders(req); seen = set()
        # Sort NEWEST first — so the most recent buy for each ticker wins.
        # Old code sorted oldest-first: if a ticker was ever held before, the stale
        # old order's fill date was used as entry_date, making the position appear
        # much older than it is and triggering premature max_hold exits.
        # Filter to BUY orders only — sell fills are never a position's entry date.
        for o in sorted(orders, key=lambda x: x.submitted_at or datetime.min, reverse=True):
            sym = o.symbol
            if sym not in positions or sym in seen: continue
            if o.side != OrderSide.BUY: continue        # buys only for entry date
            seen.add(sym)
            if o.filled_at: positions[sym]["entry_date"] = str(o.filled_at.date())
            if o.client_order_id and "|" in o.client_order_id:
                positions[sym]["strategy"] = o.client_order_id.split("|")[0]
    except Exception as e: log.debug(f"enrich failed: {e}")
    if ab_test_active() or ab_load_registry().get("entries"):
        ab_attach_groups(positions)
    return positions


# =============================================================================
#  DAILY ENTRY COUNT (replaces pdt.json — 2026-06-18)
# =============================================================================

def _count_buys_today():
    today = str(date.today())
    if not TX_FILE.exists():
        return 0
    with open(TX_FILE, newline="") as f:
        return sum(1 for r in csv.DictReader(f)
                   if r.get("action") == "BUY" and r.get("date") == today)


def entry_slot_ok(buys_today, max_trades):
    """True if another entry is allowed under cash / position caps."""
    if max_trades <= 0:
        return False
    if buys_today >= max_trades:
        log.warning(f"Entry cap reached {buys_today}/{max_trades}")
        return False
    return True


# =============================================================================
#  A/B CONCENTRATION TEST  (virtual 50/50 groups, tracked separately)
# =============================================================================

def _ab_default_registry():
    start = AB_TEST_START or str(date.today())
    return {"started": start, "days": AB_TEST_DAYS, "entries": {}, "scans": []}


def ab_load_registry():
    if not AB_TEST_REGISTRY_FILE.exists():
        reg = _ab_default_registry()
        ab_save_registry(reg)
        return reg
    try:
        return json.loads(AB_TEST_REGISTRY_FILE.read_text(encoding="utf-8"))
    except Exception as e:
        log.warning(f"ab_load_registry failed: {e}")
        return _ab_default_registry()


def ab_save_registry(reg):
    try:
        AB_TEST_REGISTRY_FILE.write_text(
            json.dumps(reg, indent=2, sort_keys=True), encoding="utf-8")
    except Exception as e:
        log.warning(f"ab_save_registry failed: {e}")


def ab_test_end(start_str=None):
    reg = ab_load_registry()
    start = start_str or reg.get("started") or str(date.today())
    try:
        s = datetime.strptime(start, "%Y-%m-%d").date()
    except Exception:
        s = date.today()
    days = int(reg.get("days") or AB_TEST_DAYS)
    return s + timedelta(days=days - 1)


def ab_test_active():
    if not AB_TEST_ENABLED:
        return False
    reg = ab_load_registry()
    start = reg.get("started") or str(date.today())
    try:
        s = datetime.strptime(start, "%Y-%m-%d").date()
    except Exception:
        return False
    return s <= date.today() <= ab_test_end(start)


def ab_position_key(ticker, entry_date):
    return f"{ticker}|{entry_date or ''}"


def ab_register_entry(ticker, entry_date, group, strategy, dollars):
    reg = ab_load_registry()
    reg.setdefault("entries", {})
    reg["entries"][ab_position_key(ticker, entry_date)] = {
        "group": group,
        "strategy": strategy,
        "dollars": round(float(dollars), 2),
        "entry_date": entry_date,
    }
    ab_save_registry(reg)


def ab_unregister_entry(ticker, entry_date):
    reg = ab_load_registry()
    key = ab_position_key(ticker, entry_date)
    if reg.get("entries", {}).pop(key, None) is not None:
        ab_save_registry(reg)


def ab_group_for(ticker, entry_date=""):
    reg = ab_load_registry()
    entries = reg.get("entries", {})
    if entry_date:
        ent = entries.get(ab_position_key(ticker, entry_date))
        if ent:
            return ent.get("group", "")
    for k, ent in entries.items():
        if k.startswith(f"{ticker}|"):
            return ent.get("group", "")
    return ""


def ab_attach_groups(positions):
    for ticker, pos in positions.items():
        pos["ab_group"] = ab_group_for(ticker, pos.get("entry_date", ""))


def ab_open_counts(positions):
    a = b = 0
    for ticker, p in positions.items():
        g = p.get("ab_group") or ab_group_for(ticker, p.get("entry_date", ""))
        if g == "A":
            a += 1
        elif g == "B":
            b += 1
    return a, b


def ab_deployed(positions, group):
    total = 0.0
    for ticker, p in positions.items():
        g = p.get("ab_group") or ab_group_for(ticker, p.get("entry_date", ""))
        if g == group:
            total += float(p.get("dollar_amt", 0) or p.get("market_value", 0) or 0)
    return total


def ab_size_for_group(group, equity, batch_count, deployed=0.0):
    """Dynamic size: remaining half-budget divided by signals in this group today."""
    half = equity * AB_TEST_EQUITY_SPLIT
    avail_g = max(0.0, half - float(deployed))
    n = max(1, int(batch_count))
    return max(MIN_TRADE_SIZE, min(avail_g / n, avail_g))


def ab_assign_groups(viable):
    """Shuffle all viable signals; split ~ratio:1 into A (wide) vs B (conc). No cap."""
    sigs = [dict(s) for s in viable]
    if not sigs:
        return []
    rng = random.Random(int(date.today().strftime("%Y%m%d")))
    rng.shuffle(sigs)
    n = len(sigs)
    ratio = max(1, AB_RATIO_A_TO_B)
    n_b = max(1, round(n / (ratio + 1)))
    n_b = min(n_b, n)
    n_a = n - n_b
    for i, s in enumerate(sigs):
        s["ab_group"] = "B" if i < n_b else "A"
    for s in sigs:
        s["_ab_batch_n"] = n_b if s["ab_group"] == "B" else n_a
    sigs.sort(key=lambda s: (0 if s["ab_group"] == "B" else 1, s["ticker"]))
    return sigs


def ab_log_scan(assigned, viable_count):
    reg = ab_load_registry()
    reg.setdefault("scans", []).append({
        "date": str(date.today()),
        "time": datetime.now().strftime("%H:%M:%S"),
        "viable": viable_count,
        "assigned_a": sum(1 for s in assigned if s.get("ab_group") == "A"),
        "assigned_b": sum(1 for s in assigned if s.get("ab_group") == "B"),
        "tickers_a": sorted(s["ticker"] for s in assigned if s.get("ab_group") == "A"),
        "tickers_b": sorted(s["ticker"] for s in assigned if s.get("ab_group") == "B"),
    })
    ab_save_registry(reg)


def ab_fetch_test_rows():
    """All BUY/SELL rows with ab_group since test start, sorted for review."""
    reg = ab_load_registry()
    start = reg.get("started", "")
    if not TX_FILE.exists():
        return []
    rows = []
    with open(TX_FILE, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            g = (r.get("ab_group") or "").strip()
            if not g:
                continue
            if start and (r.get("date") or "") < start:
                continue
            rows.append(r)
    rows.sort(key=lambda r: (r.get("date", ""), r.get("ab_group", ""), r.get("action", ""),
                             r.get("timestamp", ""), r.get("ticker", "")))
    return rows


def ab_group_stats(rows, group, action="SELL"):
    sub = [r for r in rows if r.get("ab_group") == group and r.get("action") == action]
    if action == "SELL":
        pnls = []
        for r in sub:
            try:
                pnls.append(float(r.get("pnl_dollar") or 0))
            except Exception:
                pass
        wins = sum(1 for p in pnls if p > 0)
        n = len(pnls)
        return {
            "n": n,
            "wins": wins,
            "win_rate": round(wins / n * 100, 1) if n else 0.0,
            "total_pnl": round(sum(pnls), 2),
            "avg_pnl": round(sum(pnls) / n, 2) if n else 0.0,
        }
    return {"n": len(sub), "wins": 0, "win_rate": 0.0, "total_pnl": 0.0, "avg_pnl": 0.0}


def ab_strategy_breakdown(rows, group):
    out = {}
    for r in rows:
        if r.get("ab_group") != group or r.get("action") != "SELL":
            continue
        st = r.get("strategy") or "?"
        out.setdefault(st, {"n": 0, "pnl": 0.0, "wins": 0})
        out[st]["n"] += 1
        try:
            p = float(r.get("pnl_dollar") or 0)
        except Exception:
            p = 0.0
        out[st]["pnl"] += p
        if p > 0:
            out[st]["wins"] += 1
    return dict(sorted(out.items(), key=lambda kv: kv[1]["pnl"], reverse=True))


def ab_realized_pnl(group=None):
    if not TX_FILE.exists():
        return 0.0, 0
    reg = ab_load_registry()
    start = reg.get("started", "")
    total = 0.0
    n = 0
    with open(TX_FILE, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("action") != "SELL":
                continue
            if start and (r.get("date") or "") < start:
                continue
            g = (r.get("ab_group") or "").strip()
            if group and g != group:
                continue
            if not group and not g:
                continue
            try:
                total += float(r.get("pnl_dollar") or 0)
                n += 1
            except Exception:
                pass
    return total, n


def ab_write_dashboard(equity, cash, positions):
    """Write dashboard.md, week_review.md, and trades_sorted.csv for end-of-week review."""
    if not ab_test_active() and not ab_load_registry().get("entries"):
        return
    reg = ab_load_registry()
    start = reg.get("started", "?")
    end = ab_test_end(start)
    ab_attach_groups(positions)
    a_open, b_open = ab_open_counts(positions)
    a_dep = ab_deployed(positions, "A")
    b_dep = ab_deployed(positions, "B")
    a_open_pnl = sum(p.get("pnl_dollar", 0) for p in positions.values()
                     if (p.get("ab_group") or "") == "A")
    b_open_pnl = sum(p.get("pnl_dollar", 0) for p in positions.values()
                     if (p.get("ab_group") or "") == "B")
    a_real, a_n = ab_realized_pnl("A")
    b_real, b_n = ab_realized_pnl("B")
    half = equity * AB_TEST_EQUITY_SPLIT
    active = ab_test_active()
    rows = ab_fetch_test_rows()
    a_st = ab_group_stats(rows, "A")
    b_st = ab_group_stats(rows, "B")
    a_buys = ab_group_stats(rows, "A", action="BUY")["n"]
    b_buys = ab_group_stats(rows, "B", action="BUY")["n"]
    ratio_live = round(a_open / b_open, 1) if b_open else (a_open if a_open else 0)

    # ── trades_sorted.csv ─────────────────────────────────────────────────
    try:
        fields = ["date", "timestamp", "ab_group", "action", "ticker", "strategy",
                  "price", "dollar_amount", "pnl_pct", "pnl_dollar", "hold_days",
                  "exit_reason", "sell_method"]
        with open(AB_TEST_TRADES_CSV, "w", newline="", encoding="utf-8") as cf:
            w = csv.DictWriter(cf, fieldnames=fields, extrasaction="ignore")
            w.writeheader()
            for r in rows:
                w.writerow({k: r.get(k, "") for k in fields})
    except Exception as e:
        log.warning(f"ab trades csv failed: {e}")

    # ── dashboard.md (quick snapshot) ─────────────────────────────────────
    dash = [
        "# A/B Test — Quick Dashboard",
        "",
        "| | |",
        "|---|---|",
        f"| Status | {'**ACTIVE**' if active else 'ENDED — review week_review.md'} |",
        f"| Period | {start} → {end} |",
        f"| Equity | ${equity:,.2f} |",
        f"| Split | {AB_TEST_EQUITY_SPLIT:.0%} virtual budget per group |",
        f"| Target ratio | ~{AB_RATIO_A_TO_B}:1 (A wide : B conc) |",
        f"| Live open ratio | {a_open}:{b_open} ({ratio_live}:1) |",
        "",
        "## Scoreboard (realized since test start)",
        "",
        "| Group | Buys | Closed | Win% | Realized P&L | Open | Open P&L | Deployed |",
        "|-------|------|--------|------|--------------|------|----------|----------|",
        f"| **A** wide | {a_buys} | {a_st['n']} | {a_st['win_rate']:.1f}% | "
        f"${a_real:+,.2f} | {a_open} | ${a_open_pnl:+,.2f} | ${a_dep:,.2f} |",
        f"| **B** conc | {b_buys} | {b_st['n']} | {b_st['win_rate']:.1f}% | "
        f"${b_real:+,.2f} | {b_open} | ${b_open_pnl:+,.2f} | ${b_dep:,.2f} |",
        f"| **Combined** | {a_buys + b_buys} | {a_st['n'] + b_st['n']} | — | "
        f"${a_real + b_real:+,.2f} | {a_open + b_open} | ${a_open_pnl + b_open_pnl:+,.2f} | — |",
        "",
        "## Open positions (sorted by group → ticker)",
    ]
    for grp in ("A", "B"):
        dash.append(f"### Group {grp}")
        pos_rows = sorted(
            [(t, p) for t, p in positions.items() if (p.get("ab_group") or "") == grp],
            key=lambda x: x[0],
        )
        if not pos_rows:
            dash.append("_None_")
            continue
        dash += ["| Ticker | Strategy | Invested | P&L% | P&L$ | Entry |",
                   "|--------|----------|----------|------|------|-------|"]
        for t, p in pos_rows:
            dash.append(
                f"| {t} | {p.get('strategy','?')} | ${p.get('dollar_amt',0):,.2f} "
                f"| {p.get('pnl_pct',0):+.1f}% | ${p.get('pnl_dollar',0):+.2f} "
                f"| {p.get('entry_date','')} |")
        dash.append("")
    dash.append(f"_Updated {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}_")
    dash.append(f"_Full detail: `week_review.md` · All trades: `trades_sorted.csv`_")

    # ── week_review.md (full sorted review) ───────────────────────────────
    review = [
        "# A/B Concentration Test — Week Review",
        "",
        f"**Period:** {start} → {end}  ",
        f"**Status:** {'ACTIVE' if active else 'ENDED'}  ",
        f"**Design:** ~{AB_RATIO_A_TO_B}:1 signal ratio (A wide / B conc), no fixed position cap — "
        f"limited only by each group's 50% virtual budget and account cash.",
        "",
        "---",
        "",
        "## 1. Headline comparison",
        "",
        "| Metric | Group A (wide) | Group B (conc) |",
        "|--------|----------------|----------------|",
        f"| Buys (test period) | {a_buys} | {b_buys} |",
        f"| Closed trades | {a_st['n']} | {b_st['n']} |",
        f"| Win rate | {a_st['win_rate']:.1f}% | {b_st['win_rate']:.1f}% |",
        f"| Avg $ / closed trade | ${a_st['avg_pnl']:+.2f} | ${b_st['avg_pnl']:+.2f} |",
        f"| Realized P&L | ${a_real:+,.2f} | ${b_real:+,.2f} |",
        f"| Open positions now | {a_open} | {b_open} |",
        f"| Open P&L (unrealized) | ${a_open_pnl:+,.2f} | ${b_open_pnl:+,.2f} |",
        f"| Capital deployed now | ${a_dep:,.2f} / ${half:,.0f} | ${b_dep:,.2f} / ${half:,.0f} |",
        f"| **Total P&L (realized + open)** | "
        f"${a_real + a_open_pnl:+,.2f} | ${b_real + b_open_pnl:+,.2f} |",
        "",
        "## 2. Closed trades by group (newest first)",
        "",
    ]
    sells = [r for r in rows if r.get("action") == "SELL"]
    sells.sort(key=lambda r: (r.get("date", ""), r.get("timestamp", "")), reverse=True)
    if sells:
        review += ["| Date | Grp | Ticker | Strategy | P&L$ | P&L% | Hold | Exit |",
                   "|------|-----|--------|----------|------|------|------|------|"]
        for r in sells:
            review.append(
                f"| {r.get('date','')} | {r.get('ab_group','')} | {r.get('ticker','')} "
                f"| {r.get('strategy','?')} | ${float(r.get('pnl_dollar') or 0):+.2f} "
                f"| {float(r.get('pnl_pct') or 0):+.1f}% | {r.get('hold_days','')} "
                f"| {r.get('exit_reason','')} |")
    else:
        review.append("_No closed A/B trades yet._")
    review += ["", "## 3. Closed trades by strategy", ""]
    for grp, label in [("A", "Wide"), ("B", "Concentrated")]:
        review.append(f"### Group {grp} — {label}")
        br = ab_strategy_breakdown(rows, grp)
        if not br:
            review.append("_None_")
        else:
            review += ["| Strategy | Trades | Wins | Win% | Total P&L |",
                       "|----------|--------|------|------|-----------|"]
            for st, v in br.items():
                wr = round(v["wins"] / v["n"] * 100, 1) if v["n"] else 0
                review.append(
                    f"| {st} | {v['n']} | {v['wins']} | {wr:.1f}% | ${v['pnl']:+.2f} |")
        review.append("")
    review += ["## 4. Daily scan log (signal assignment)", ""]
    scans = reg.get("scans") or []
    if scans:
        review += ["| Date | Time | Viable | → A | → B | B tickers |",
                   "|------|------|--------|-----|-----|-----------|"]
        for sc in scans:
            review.append(
                f"| {sc.get('date','')} | {sc.get('time','')} | {sc.get('viable',0)} "
                f"| {sc.get('assigned_a',0)} | {sc.get('assigned_b',0)} "
                f"| {', '.join(sc.get('tickers_b') or [])} |")
    else:
        review.append("_No scans logged yet._")
    review += [
        "",
        "## 5. All ledger rows (sorted: date → group → action → ticker)",
        "",
        "See **`trades_sorted.csv`** for spreadsheet import.",
        "",
    ]
    if rows:
        review += ["| Date | Time | Grp | Act | Ticker | Strategy | $ | P&L$ | Note |",
                   "|------|------|-----|-----|--------|----------|---|------|------|"]
        for r in rows:
            tm = (r.get("timestamp") or "")[11:19]
            note = r.get("exit_reason", "") if r.get("action") == "SELL" else ""
            review.append(
                f"| {r.get('date','')} | {tm} | {r.get('ab_group','')} | {r.get('action','')} "
                f"| {r.get('ticker','')} | {r.get('strategy','?')} "
                f"| ${float(r.get('dollar_amount') or 0):.2f} "
                f"| ${float(r.get('pnl_dollar') or 0):+.2f} | {_trunc(note, 30)} |")
    review.append("")
    review.append(f"_Generated {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}_")

    try:
        AB_TEST_DASHBOARD.write_text("\n".join(dash), encoding="utf-8")
        AB_TEST_WEEK_REVIEW.write_text("\n".join(review), encoding="utf-8")
        log.info(f"  AB reports -> {AB_TEST_DASHBOARD.name}, {AB_TEST_WEEK_REVIEW.name}, "
                 f"{AB_TEST_TRADES_CSV.name}")
    except Exception as e:
        log.warning(f"ab_write_dashboard failed: {e}")


# =============================================================================
#  ORDERS
# =============================================================================

def _order_fill_summary(order):
    """Return normalized fill info from an Alpaca order object."""
    try:
        avg = float(getattr(order, "filled_avg_price", 0) or 0)
        qty = float(getattr(order, "filled_qty", 0) or 0)
        if avg > 0 and qty > 0:
            return {"price": avg, "qty": qty, "dollars": avg * qty}
    except Exception:
        pass
    return {"price": None, "qty": None, "dollars": None}


def _recent_filled_order(client, ticker, side, limit=20):
    """Best-effort lookup of the most recent filled order for ticker+side."""
    try:
        req = GetOrdersRequest(
            status=QueryOrderStatus.CLOSED,
            symbols=[ticker],
            limit=limit,
        )
        for o in client.get_orders(req):
            if o.side != side:
                continue
            if getattr(o, "status", None) not in (OrderStatus.filled, OrderStatus.partially_filled):
                continue
            fill = _order_fill_summary(o)
            if fill["price"] is not None:
                return fill
    except Exception:
        pass
    return {"price": None, "qty": None, "dollars": None}


def do_buy(client, ticker, dollars, strategy, expected_price=None, fast_submit=False):
    try:
        cid = f"{strategy}|{ticker}|{date.today()}"[:48]
        o = client.submit_order(MarketOrderRequest(
            symbol=ticker, notional=round(dollars, 2),
            side=OrderSide.BUY, time_in_force=TimeInForce.DAY,
            client_order_id=cid))
        log.info(f"  BUY  {ticker}  ${dollars:.2f}  [{strategy}]  id={o.id}")
        order_id = str(o.id)

        if fast_submit:
            return {
                "ok": True,
                "filled": False,
                "order_id": order_id,
                "expected_price": expected_price,
                "order_price": expected_price,
                "execution_method": "market_submit_pending",
                "price": None,
                "qty": None,
                "dollars": None,
            }

        # Best-effort fill capture for accurate transaction logs.
        for _ in range(3):
            time.sleep(2)
            try:
                oo = client.get_order_by_id(order_id)
                if oo.status in (OrderStatus.filled, OrderStatus.partially_filled):
                    fill = _order_fill_summary(oo)
                    return {
                        "ok": True,
                        "filled": True,
                        "order_id": order_id,
                        "expected_price": expected_price,
                        "order_price": expected_price,
                        "execution_method": "market_fill_confirmed",
                        **fill,
                    }
            except Exception:
                pass

        fill = _recent_filled_order(client, ticker, OrderSide.BUY, limit=10)
        fill_confirmed = (fill["price"] is not None and fill["qty"] is not None and fill["qty"] > 0)
        return {
            "ok": True,
            "filled": fill_confirmed,
            "order_id": order_id,
            "expected_price": expected_price,
            "order_price": expected_price,
            "execution_method": "market_fill_delayed" if fill_confirmed else "market_submit_unconfirmed",
            **fill,
        }
    except Exception as e:
        log.error(f"  BUY FAILED {ticker}: {e}")
        return {
            "ok": False,
            "filled": False,
            "order_id": None,
            "price": None,
            "qty": None,
            "dollars": None,
            "expected_price": expected_price,
            "order_price": expected_price,
            "execution_method": "buy_failed",
        }


def poll_pending_buys(client, pending_buys, rgm):
    """Poll submitted buys; log confirmed fills. Returns count of newly confirmed fills."""
    if not pending_buys:
        return 0
    confirmed = 0
    hdr("BUY FILL CONFIRMATION")
    row("Pending submits", str(len(pending_buys)))
    div()
    for item in pending_buys:
        ticker = item["ticker"]
        strategy = item["strategy"]
        da = item["dollars"]
        sig_close = item.get("expected_price")
        order_id = item.get("order_id")
        fill = {"price": None, "qty": None, "dollars": None}
        filled = False
        if order_id:
            for _ in range(4):
                try:
                    oo = client.get_order_by_id(order_id)
                    if oo.status in (OrderStatus.filled, OrderStatus.partially_filled):
                        fill = _order_fill_summary(oo)
                        filled = True
                        break
                except Exception:
                    pass
                time.sleep(2)
        if not filled:
            fill = _recent_filled_order(client, ticker, OrderSide.BUY, limit=10)
            filled = fill["price"] is not None and fill.get("qty") and fill["qty"] > 0
        if filled:
            confirmed += 1
            buy_price = fill.get("price") if fill.get("price") is not None else sig_close
            buy_dollars = fill.get("dollars") if fill.get("dollars") is not None else da
            log_tx("BUY", ticker, strategy, buy_price, buy_dollars, rgm,
                   float(get_account_safe(client).equity),
                   expected_price=sig_close,
                   order_price=sig_close,
                   execution_method="market_fill_batched",
                   ab_group=item.get("ab_group", ""))
            row(ticker, f"confirmed @ ${float(buy_price):.2f}")
        else:
            row(ticker, "still unconfirmed")
    ftr()
    return confirmed

def cancel_stop_orders(client, ticker):
    """Cancel ALL open sell orders for a ticker (stop, stop-limit, and stuck
    limit sells from previous do_sell() calls).  Called before a
    software-triggered exit so we never have two conflicting sell orders."""
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, symbols=[ticker])
        for o in client.get_orders(req):
            if o.side == OrderSide.SELL:          # cancel ANY open sell
                try:
                    client.cancel_order_by_id(str(o.id))
                    log.info(f"  SELL order cancelled {ticker}  "
                             f"type={getattr(o,'order_type','?')}  id={o.id}")
                except Exception as ce:
                    log.warning(f"  cancel failed {ticker} id={o.id}: {ce}")
    except Exception as e:
        log.warning(f"  cancel_stop_orders failed {ticker}: {e}")


def ensure_stop(client, ticker, entry_price, qty):
    """Place a GTC stop-MARKET sell order.
    Trigger = entry × (1 + EXIT_STOP_LOSS)   e.g. -0.5%

    Why stop-MARKET (not stop-LIMIT):
      A stop-LIMIT at -1% will NOT fill if the stock gaps down -6% overnight —
      the order triggers but the price is already below the limit, so it sits
      unfilled until the software exit catches it at 9:35am (or never if the
      morning run misses like May 1st). A stop-MARKET converts to a market order
      the instant the trigger is breached, filling at whatever the open price is.
      You still lose the gap amount, but you're OUT at the open instead of
      riding further intraday decline.

    Skipped silently if a GTC stop already exists for this ticker."""
    stop_price = round(entry_price * (1.0 + EXIT_STOP_LOSS), 2)
    # Alpaca rejects GTC orders on fractional quantities — floor to whole shares.
    # At small account sizes some positions will be < 1 share; skip the stop for
    # those (the software exit at 9:35am will still catch them).
    stop_qty = math.floor(qty)
    if stop_qty < 1:
        log.info(f"  STOP skipped {ticker}: fractional ({qty:.4f} shares) — software exit will handle it")
        _register_fractional_watch(ticker, qty, entry_price)
        return False
    try:
        # Check if a stop-sell already exists for this ticker
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, symbols=[ticker])
        for o in client.get_orders(req):
            if (getattr(o, "order_type", None) in (OrderType.STOP,
                                                    OrderType.STOP_LIMIT)
                    and o.side == OrderSide.SELL):
                log.info(f"  STOP already live {ticker} @ ${o.stop_price}")
                return True
        # Place new GTC stop-MARKET order (whole shares only)
        o = client.submit_order(StopOrderRequest(
            symbol=ticker,
            qty=str(stop_qty),
            side=OrderSide.SELL,
            time_in_force=TimeInForce.GTC,
            stop_price=stop_price,
        ))
        log.info(f"  STOP-MARKET placed {ticker}  qty={stop_qty} (pos={qty:.4f})  "
                 f"stop=${stop_price:.2f}  id={o.id}")
        return True
    except Exception as e:
        log.warning(f"  STOP placement failed {ticker}: {e}")
        return False


def place_all_stops(client):
    """Ensure every open Alpaca position has a GTC stop-market order.

    Called:
      • After the buy loop in run_scan() — places stops on newly bought positions.
        Waits 5s first so market orders have time to fill and appear in positions.
      • At the start of run_exits() — catches any position that lost its stop
        (e.g. stop was triggered on a small dip but re-entered, or morning run
        missed entirely like May 1st leaving positions unprotected all day).

    safe to call repeatedly — ensure_stop() skips tickers that already have a stop."""
    try:
        positions = client.get_all_positions()
        if not positions:
            return
        log.info(f"  place_all_stops: checking {len(positions)} positions...")
        for p in positions:
            ensure_stop(client, p.symbol,
                        float(p.avg_entry_price), float(p.qty))
    except Exception as e:
        log.warning(f"  place_all_stops failed: {e}")


def _load_fractional_watch():
    if not FRACTIONAL_WATCH_FILE.exists():
        return {}
    try:
        return json.loads(FRACTIONAL_WATCH_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_fractional_watch(data):
    try:
        FRACTIONAL_WATCH_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except Exception as e:
        log.warning(f"  fractional_watch save failed: {e}")


def _register_fractional_watch(ticker, qty, entry_price):
    data = _load_fractional_watch()
    data[ticker] = {
        "qty": float(qty),
        "entry_price": float(entry_price),
        "registered": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    _save_fractional_watch(data)


def _clear_fractional_watch(ticker):
    data = _load_fractional_watch()
    if ticker in data:
        del data[ticker]
        _save_fractional_watch(data)


def place_eod_stops(client):
    """Replace all GTC stops with current-price-based stops right before close.

    Called once at the end of run_scan() (~3:49pm ET).

    Why this matters:
      place_all_stops() sets the stop at entry_price * 0.995 and never moves it.
      If a position drops from $132 to $127, the entry-based stop at $131.34 is
      already blown through — useless overnight. This function cancels the old
      stop and places a fresh one at current_price * 0.995, so the stop always
      reflects where the stock IS right now, not where it was bought.

      Effect:
        • Losing positions: stop moves to current level — caps further overnight bleed.
        • Winning positions: stop ratchets up — locks in some of the gain.

    Fractional positions (<1 whole share) can't have GTC stops — logged and skipped.
    Those are protected by ext_exits (4pm–8pm) and the morning exits run.
    """
    try:
        positions = client.get_all_positions()
        if not positions:
            return
        log.info(f"  place_eod_stops: updating {len(positions)} stops to current price...")
        for p in positions:
            qty       = float(p.qty)
            stop_qty  = math.floor(qty)
            cur_price = float(p.current_price)
            stop_price = round(cur_price * (1.0 + EXIT_STOP_LOSS), 2)

            if stop_qty < 1:
                log.info(f"  EOD stop skip {p.symbol}: {qty:.4f} shares (fractional) "
                         f"— ext_exits will cover")
                continue

            # Cancel any existing stop for this ticker first
            try:
                req = GetOrdersRequest(status=QueryOrderStatus.OPEN,
                                       symbols=[p.symbol])
                for o in client.get_orders(req):
                    if (getattr(o, "order_type", None) in
                            (OrderType.STOP, OrderType.STOP_LIMIT)
                            and o.side == OrderSide.SELL):
                        client.cancel_order_by_id(str(o.id))
                        log.info(f"  EOD stop: cancelled old stop {p.symbol}")
            except Exception as e:
                log.warning(f"  EOD stop: cancel failed {p.symbol}: {e}")

            # Place fresh stop at current price
            try:
                o = client.submit_order(StopOrderRequest(
                    symbol=p.symbol,
                    qty=str(stop_qty),
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC,
                    stop_price=stop_price,
                ))
                log.info(f"  EOD stop placed {p.symbol} @ ${stop_price:.2f}  "
                         f"(cur ${cur_price:.2f}  qty={stop_qty})")
            except Exception as e:
                log.warning(f"  EOD stop failed {p.symbol}: {e}")
    except Exception as e:
        log.warning(f"  place_eod_stops failed: {e}")


def _latest_bid(ticker):
    """Best-effort latest bid from Alpaca market data."""
    try:
        req = StockLatestQuoteRequest(symbol_or_symbols=[ticker])
        q = _get_dc().get_stock_latest_quote(req)
        qv = q.get(ticker) if isinstance(q, dict) else None
        if qv is None and hasattr(q, "__getitem__"):
            qv = q[ticker]
        bid = float(getattr(qv, "bid_price", 0) or 0)
        return bid if bid > 0 else None
    except Exception:
        return None


def do_sell(client, ticker, extended_hours=False, urgency="normal"):
    """Exit a position.
    In regular hours (extended_hours=False):
      - urgency="urgent" (stop breach): market sell immediately.
      - otherwise: limit 0.2% below, then market fallback after polls.

    In extended hours (extended_hours=True):
      - DAY limit sell at 0.15% below current (DAY orders work on fractional shares).
      - No market-order fallback (Alpaca only allows limit in extended hours).
      - If unfilled by market open, 9:35am run re-evaluates.

    Returns dict with:
      ok: command path succeeded
      filled: position was actually filled/closed this run
      price/dollars/qty: best-effort Alpaca fill details for logging
    """
    cancel_stop_orders(client, ticker)
    t0 = time.time()

    def _position_state():
        """Return (is_open, remaining_qty) for ticker right now."""
        try:
            p = client.get_open_position(ticker)
            return True, abs(float(p.qty))
        except Exception:
            return False, 0.0

    def _mk(ok, filled, fill=None, method="", pending=False, exit_complete=None, remaining_qty=None):
        fill = fill or {"price": None, "qty": None, "dollars": None}
        price = fill.get("price")
        slp = None
        if cur_submit is not None and price is not None and cur_submit > 0:
            try:
                slp = (float(cur_submit) - float(price)) / float(cur_submit) * 10000.0
            except Exception:
                slp = None
        if exit_complete is None:
            if filled:
                is_open, rem = _position_state()
                exit_complete = (not is_open) or rem <= 1e-6
                remaining_qty = 0.0 if exit_complete else rem
            else:
                exit_complete = False
        partial = bool(filled and not exit_complete)
        if filled and method and not method.endswith("_full") and not method.endswith("_partial"):
            method = f"{method}_{'full' if exit_complete else 'partial'}"
        return {
            "ok": ok,
            "filled": filled,
            "pending": pending,
            "exit_complete": exit_complete,
            "partial": partial,
            "remaining_qty": remaining_qty,
            "price": fill.get("price"),
            "qty": fill.get("qty"),
            "dollars": fill.get("dollars"),
            "sell_method": method,
            "cur_at_submit": cur_submit,
            "bid_at_submit": bid_submit,
            "limit_price_used": lim_submit,
            "sell_latency_s": time.time() - t0,
            "fill_slippage_bps": slp,
        }

    cur_submit = None
    bid_submit = None
    lim_submit = None

    # ── Urgent regular hours: market immediately (stop breach) ────────────
    if urgency == "urgent" and not extended_hours:
        try:
            pos = client.get_open_position(ticker)
            cur_submit = float(pos.current_price)
            client.close_position(ticker)
            log.info(f"  SELL MARKET [urgent] {ticker} closed")
            time.sleep(2)
            fill = _recent_filled_order(client, ticker, OrderSide.SELL, limit=10)
            return _mk(True, True, fill=fill, method="market_urgent")
        except Exception as e:
            msg = str(e)
            if "not found" in msg or "position" in msg.lower():
                log.info(f"  SELL [urgent] {ticker}: position already closed")
                fill = _recent_filled_order(client, ticker, OrderSide.SELL, limit=10)
                return _mk(True, True, fill=fill, method="position_already_closed")
            log.warning(f"  SELL MARKET [urgent] failed {ticker}: {e}")
            # fall through to limit + market path

    # ── Step 1: try a limit sell ──────────────────────────────────────────
    try:
        pos = client.get_open_position(ticker)
        qty = abs(float(pos.qty))
        cur = float(pos.current_price)
        cur_submit = cur
        _polls = {"urgent": 1, "normal": 4, "low": 6}.get(urgency, 4)
        # Extended hours: wider spread (~3×), use tighter limit to get filled
        spread_adj = 0.9985 if extended_hours else 0.998
        bid = None if extended_hours else _latest_bid(ticker)
        bid_submit = bid
        lim = max(cur * spread_adj, bid) if bid is not None else (cur * spread_adj)
        lim = round(lim, 2)
        lim_submit = lim
        order_kwargs = dict(
            symbol=ticker, qty=str(qty),
            side=OrderSide.SELL,
            time_in_force=TimeInForce.DAY,
            limit_price=lim,
        )
        if extended_hours:
            order_kwargs["extended_hours"] = True
        o = client.submit_order(LimitOrderRequest(**order_kwargs))
        eh_tag = " [EXT HRS]" if extended_hours else ""
        log.info(f"  SELL LIMIT{eh_tag} {ticker}  qty={qty}  limit=${lim:.2f}  id={o.id}")

        # In extended hours we don't wait for fill — 9:35am run will catch it
        if extended_hours:
            # Brief check (1 × 5s) in case it fills immediately
            time.sleep(5)
            try:
                o = client.get_order_by_id(str(o.id))
                if o.status in (OrderStatus.filled, OrderStatus.partially_filled):
                    log.info(f"  SELL LIMIT[EXT] filled {ticker} @ ${o.filled_avg_price}")
                    fill = _order_fill_summary(o)
                    return _mk(True, True, fill=fill, method="ext_limit_fill")
            except Exception:
                pass
            # Still pending — leave it; 9:35am will re-check
            log.info(f"  SELL LIMIT[EXT] pending for {ticker} — 9:35am will follow up")
            return _mk(True, False, method="ext_limit_pending", pending=True)

        # Regular hours: urgency-adjusted wait for fill.
        for _ in range(_polls):
            time.sleep(5)
            try:
                o = client.get_order_by_id(str(o.id))
                if o.status in (OrderStatus.filled, OrderStatus.partially_filled):
                    log.info(f"  SELL LIMIT filled {ticker} @ ${o.filled_avg_price}")
                    fill = _order_fill_summary(o)
                    return _mk(True, True, fill=fill, method="limit_fill")
            except Exception:
                pass  # order may already be filled/gone — check position below

        # Check if position is already gone (limit may have filled silently)
        try:
            client.get_open_position(ticker)
        except Exception:
            log.info(f"  SELL LIMIT filled {ticker} (confirmed by position check)")
            fill = _order_fill_summary(o)
            if fill["price"] is None:
                fill = _recent_filled_order(client, ticker, OrderSide.SELL, limit=10)
            return _mk(True, True, fill=fill, method="limit_fill_position_check")

        # Still open — cancel limit and fall through to market sell
        try:
            client.cancel_order_by_id(str(o.id))
        except Exception:
            pass
        log.info(f"  SELL LIMIT not filled for {ticker}, falling back to market")

    except Exception as e:
        log.warning(f"  SELL LIMIT setup failed {ticker}: {e}")

    # ── Step 2: market sell fallback (regular hours only) ─────────────────
    if extended_hours:
        # Market orders not allowed in extended hours — leave for 9:35am
        log.info(f"  SELL[EXT] {ticker}: limit not placed, 9:35am will retry")
        return _mk(True, False, method="ext_retry")
    try:
        # Check position still exists before attempting market sell
        client.get_open_position(ticker)
        client.close_position(ticker)
        log.info(f"  SELL MARKET {ticker} closed")
        time.sleep(2)
        fill = _recent_filled_order(client, ticker, OrderSide.SELL, limit=10)
        return _mk(True, True, fill=fill, method="market_fallback")
    except Exception as e:
        msg = str(e)
        if "not found" in msg or "position" in msg.lower():
            # Position already gone — treat as success
            log.info(f"  SELL {ticker}: position already closed")
            fill = _recent_filled_order(client, ticker, OrderSide.SELL, limit=10)
            return _mk(True, True, fill=fill, method="position_already_closed")
        log.warning(f"  SELL {ticker}: {e}")
        return _mk(False, False, method="sell_failed")


# =============================================================================
#  TRANSACTION LOG
# =============================================================================

TX_F = ["timestamp","date","action","ticker","strategy","price","dollar_amount",
        "pnl_pct","pnl_dollar","hold_days","exit_reason","regime","equity_after",
        "sell_method","cur_at_submit","bid_at_submit","limit_price_used",
        "sell_latency_s","fill_slippage_bps","ab_group"]
EXEC_AUDIT_F = [
    "timestamp", "date", "action", "ticker", "strategy",
    "expected_price", "order_price", "actual_price", "filled_dollars",
    "slippage_pct", "slippage_dollar", "execution_method",
    "exit_reason", "regime",
]

def log_tx(action, ticker, strategy, price, dollars, rgm, equity,
           pnl_pct=0, pnl_dollar=0, hold_days=0, exit_reason="",
           sell_method="", cur_at_submit=None, bid_at_submit=None,
           limit_price_used=None, sell_latency_s=None, fill_slippage_bps=None,
           expected_price=None, order_price=None, execution_method="",
           ab_group=""):
    def _fmt(v, nd=2):
        if v is None:
            return ""
        try:
            return round(float(v), nd)
        except Exception:
            return ""

    def _to_f(v):
        try:
            if v is None or v == "":
                return None
            return float(v)
        except Exception:
            return None

    def _log_exec_audit():
        exp = _to_f(expected_price)
        if exp is None:
            exp = _to_f(cur_at_submit) if action == "SELL" else _to_f(price)
        ord_px = _to_f(order_price)
        if ord_px is None:
            ord_px = _to_f(limit_price_used) if action == "SELL" else exp
        act = _to_f(price)
        filled = _to_f(dollars)

        slip_pct = None
        slip_dol = None
        qty_est = None
        if exp and exp > 0 and filled is not None:
            qty_est = filled / exp
        if exp and exp > 0 and act is not None:
            slip_pct = ((act - exp) / exp) * 100.0
            if qty_est is not None:
                slip_dol = (act - exp) * qty_est

        row = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "date": str(date.today()),
            "action": action,
            "ticker": ticker,
            "strategy": strategy,
            "expected_price": _fmt(exp, 4),
            "order_price": _fmt(ord_px, 4),
            "actual_price": _fmt(act, 4),
            "filled_dollars": _fmt(filled, 2),
            "slippage_pct": _fmt(slip_pct, 4),
            "slippage_dollar": _fmt(slip_dol, 4),
            "execution_method": execution_method or sell_method or ("manual_" + action.lower()),
            "exit_reason": exit_reason,
            "regime": rgm,
        }
        init = not EXEC_AUDIT_FILE.exists()
        with open(EXEC_AUDIT_FILE, "a", newline="") as af:
            aw = csv.DictWriter(af, fieldnames=EXEC_AUDIT_F)
            if init:
                aw.writeheader()
            aw.writerow(row)
            af.flush()
            os.fsync(af.fileno())

    row_data = {
        "timestamp":    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "date":         str(date.today()),
        "action":       action,
        "ticker":       ticker,
        "strategy":     strategy,
        "price":        round(price, 2),
        "dollar_amount":round(dollars, 2),
        "pnl_pct":      round(pnl_pct, 2),
        "pnl_dollar":   round(pnl_dollar, 2),
        "hold_days":    hold_days,
        "exit_reason":  exit_reason,
        "regime":       rgm,
        "equity_after": round(equity, 2),
        "sell_method":  sell_method,
        "cur_at_submit": _fmt(cur_at_submit, 4),
        "bid_at_submit": _fmt(bid_at_submit, 4),
        "limit_price_used": _fmt(limit_price_used, 4),
        "sell_latency_s": _fmt(sell_latency_s, 2),
        "fill_slippage_bps": _fmt(fill_slippage_bps, 2),
        "ab_group": ab_group or "",
    }
    if action == "SELL" and not row_data["ab_group"]:
        row_data["ab_group"] = ab_group_for(ticker)
    if action == "BUY" and row_data["ab_group"]:
        ab_register_entry(ticker, str(date.today()), row_data["ab_group"], strategy, dollars)
    if action == "SELL":
        reg = ab_load_registry()
        for k in list(reg.get("entries", {})):
            if k.startswith(f"{ticker}|"):
                reg["entries"].pop(k, None)
                ab_save_registry(reg)
                break
    try:
        init = not TX_FILE.exists()
        with open(TX_FILE, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=TX_F)
            if init: w.writeheader()
            w.writerow(row_data)
            f.flush()          # force write to disk — prevents silent data loss
            os.fsync(f.fileno())
        try:
            _log_exec_audit()
        except Exception as audit_e:
            log.warning(f"  EXEC audit log failed {action} {ticker}: {audit_e}")
        log.info(f"  TX logged: {action} {ticker}  "
                 f"{'P&L '+str(round(pnl_pct,2))+'%' if action=='SELL' else '$'+str(round(dollars,2))}")
    except Exception as e:
        log.error(f"  TX LOG FAILED {action} {ticker}: {e}")
        # Fallback: print to stdout so GitHub Actions always captures it in run logs
        print(f"TX_FALLBACK|{row_data}", flush=True)

RUN_F = ["timestamp","mode","regime","equity","cash","signals","entries",
         "exits","open_positions","tickers","universe","duration_s","cache_hit"]

def log_run(mode, rgm, equity, cash, signals, entries, exits, positions,
            cache_hit=None):
    global _last_cache_hit
    if cache_hit is not None:
        _last_cache_hit = cache_hit
    duration_s = ""
    if _run_started_at is not None:
        duration_s = round(time.time() - _run_started_at, 1)
    init = not RUNS_FILE.exists()
    with open(RUNS_FILE, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=RUN_F, extrasaction="ignore")
        if init: w.writeheader()
        w.writerow({"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "mode": mode, "regime": rgm, "equity": round(equity, 2),
                    "cash": round(cash, 2), "signals": signals, "entries": entries,
                    "exits": exits, "open_positions": len(positions),
                    "tickers": "|".join(positions.keys()), "universe": UNIVERSE,
                    "duration_s": duration_s, "cache_hit": _last_cache_hit})


def _max_drawdown_pct_pathwise(eq_series):
    """Path-wise max drawdown from running peaks (negative percentage)."""
    if not eq_series:
        return 0.0
    peak = eq_series[0]
    max_dd = 0.0
    for eq in eq_series:
        if eq > peak:
            peak = eq
        if peak > 0:
            dd = (eq - peak) / peak * 100.0
            if dd < max_dd:
                max_dd = dd
    return max_dd


# =============================================================================
#  PERFORMANCE DASHBOARD
# =============================================================================

def write_dashboard():
    """Generate logs/dashboard.md — single-file performance summary."""
    try:
        STARTING_EQUITY = 500.0
        DASH_FILE = LOG_DIR / "dashboard.md"

        # Load transactions
        trades, buys_tx, sells_tx = [], [], []
        if TX_FILE.exists():
            with open(TX_FILE, newline="") as f:
                for r in csv.DictReader(f):
                    r["pnl_pct"]    = float(r.get("pnl_pct", 0) or 0)
                    r["pnl_dollar"] = float(r.get("pnl_dollar", 0) or 0)
                    r["hold_days"]  = int(r.get("hold_days", 0) or 0)
                    trades.append(r)
            buys_tx  = [t for t in trades if t["action"] == "BUY"]
            sells_tx = [t for t in trades if t["action"] == "SELL"]

        # Load runs for equity curve
        runs = []
        if RUNS_FILE.exists():
            with open(RUNS_FILE, newline="") as f:
                for r in csv.DictReader(f):
                    r["equity"] = float(r.get("equity", 0) or 0)
                    r["cash"]   = float(r.get("cash", 0) or 0)
                    runs.append(r)

        eq_series      = [r["equity"] for r in runs if r["equity"] > 0]
        current_equity = eq_series[-1] if eq_series else STARTING_EQUITY
        peak_equity    = max(eq_series) if eq_series else STARTING_EQUITY
        total_ret_pct  = (current_equity - STARTING_EQUITY) / STARTING_EQUITY * 100
        max_dd_pct     = _max_drawdown_pct_pathwise(eq_series)

        last_run      = runs[-1] if runs else {}
        current_cash  = last_run.get("cash", 0)
        open_pos_cnt  = last_run.get("open_positions", "0")
        open_tickers  = last_run.get("tickers", "")
        last_run_time = last_run.get("timestamp", "N/A")

        # Trade stats
        wins   = [s for s in sells_tx if s["pnl_pct"] > 0]
        losses = [s for s in sells_tx if s["pnl_pct"] <= 0]
        total_closed = len(sells_tx)
        win_rate     = len(wins) / total_closed * 100 if total_closed else 0
        avg_win      = sum(s["pnl_pct"] for s in wins)   / len(wins)   if wins   else 0
        avg_loss     = sum(s["pnl_pct"] for s in losses) / len(losses) if losses else 0
        avg_hold     = sum(s["hold_days"] for s in sells_tx) / total_closed if total_closed else 0
        total_pnl    = sum(s["pnl_dollar"] for s in sells_tx)
        gross_win    = sum(s["pnl_dollar"] for s in wins)
        gross_loss   = abs(sum(s["pnl_dollar"] for s in losses)) or 1e-9
        pf           = gross_win / gross_loss

        # Strategy map (most recent buy per ticker)
        strat_map = {b["ticker"]: b.get("strategy", "?") for b in buys_tx}

        # Exit reason breakdown
        from collections import defaultdict
        by_exit = defaultdict(list)
        for s in sells_tx:
            key = (s.get("exit_reason") or "unknown").split("(")[0].strip().split(" ")[0]
            by_exit[key].append(s)

        by_strat = defaultdict(list)
        for s in sells_tx:
            strat = strat_map.get(s["ticker"], s.get("strategy", "?")) or "?"
            by_strat[strat].append(s)

        # Daily equity (last reading per day)
        daily_eq = {}
        for r in runs:
            d = r.get("timestamp", "")[:10]
            if d:
                daily_eq[d] = r["equity"]
        eq_dates = sorted(daily_eq.keys())

        now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        L = []
        L.append("# 📊 Rubber Band Bot — Performance Dashboard")
        L.append(f"*Updated: {now_str}*\n")

        L.append("## Account Snapshot")
        L.append("| | |"); L.append("|---|---|")
        L.append(f"| **Current Equity** | ${current_equity:.2f} |")
        L.append(f"| **Starting Equity** | ${STARTING_EQUITY:.2f} |")
        L.append(f"| **Total Return** | {total_ret_pct:+.2f}% (${current_equity - STARTING_EQUITY:+.2f}) |")
        L.append(f"| **Peak Equity** | ${peak_equity:.2f} |")
        L.append(f"| **Max Drawdown** | {max_dd_pct:.2f}% |")
        L.append(f"| **Current Cash** | ${current_cash:.2f} |")
        L.append(f"| **Open Positions** | {open_pos_cnt} ({open_tickers}) |")
        L.append(f"| **Last Bot Run** | {last_run_time} |")
        L.append("")

        L.append("## Trade Performance (Closed Trades)")
        L.append("| Metric | Value |"); L.append("|---|---|")
        L.append(f"| **Total Closed Trades** | {total_closed} |")
        L.append(f"| **Wins / Losses** | {len(wins)} / {len(losses)} |")
        L.append(f"| **Win Rate** | {win_rate:.1f}% |")
        L.append(f"| **Avg Win** | +{avg_win:.2f}% |")
        L.append(f"| **Avg Loss** | {avg_loss:.2f}% |")
        L.append(f"| **Profit Factor** | {pf:.2f}x |")
        L.append(f"| **Avg Hold Days** | {avg_hold:.1f}d |")
        L.append(f"| **Total Realised P&L** | ${total_pnl:+.2f} |")
        L.append("")

        if by_exit:
            L.append("## Exit Reasons")
            L.append("| Exit Type | Trades | Win Rate | Avg P&L% |")
            L.append("|---|---|---|---|")
            for reason, grp in sorted(by_exit.items(), key=lambda x: -len(x[1])):
                gw = [s for s in grp if s["pnl_pct"] > 0]
                L.append(f"| `{reason}` | {len(grp)} | {len(gw)/len(grp)*100:.0f}% "
                         f"| {sum(s['pnl_pct'] for s in grp)/len(grp):+.2f}% |")
            L.append("")

        if total_closed > 0 and by_strat:
            L.append("## Strategy Breakdown")
            L.append("| Strategy | Trades | Win Rate | Avg P&L% |")
            L.append("|---|---|---|---|")
            for strat, grp in sorted(by_strat.items(), key=lambda x: -len(x[1])):
                gw = [s for s in grp if s["pnl_pct"] > 0]
                L.append(f"| `{strat}` | {len(grp)} | {len(gw)/len(grp)*100:.0f}% "
                         f"| {sum(s['pnl_pct'] for s in grp)/len(grp):+.2f}% |")
            L.append("")

        if len(eq_dates) > 1:
            L.append("## Equity Timeline")
            L.append("| Date | Equity | Change |"); L.append("|---|---|---|")
            prev = STARTING_EQUITY
            step = max(1, len(eq_dates) // 30)
            shown = set()
            for d in eq_dates[::step]:
                eq = daily_eq[d]; chg = eq - prev
                L.append(f"| {d} | ${eq:.2f} | {chg:+.2f} |")
                prev = eq; shown.add(d)
            if eq_dates[-1] not in shown:
                eq = daily_eq[eq_dates[-1]]; chg = eq - prev
                L.append(f"| {eq_dates[-1]} | ${eq:.2f} | {chg:+.2f} |")
            L.append("")

        recent = sells_tx[-20:][::-1]
        if recent:
            L.append("## Recent Closed Trades")
            L.append("| Date | Ticker | Strategy | P&L% | P&L$ | Hold | Exit Reason |")
            L.append("|---|---|---|---|---|---|---|")
            for s in recent:
                strat = strat_map.get(s["ticker"], s.get("strategy", "?")) or "?"
                L.append(f"| {s['date']} | **{s['ticker']}** | `{strat}` "
                         f"| {s['pnl_pct']:+.2f}% | ${s['pnl_dollar']:+.2f} "
                         f"| {s['hold_days']}d | {s.get('exit_reason','')} |")
            L.append("")

        L.append("---")
        L.append("*Auto-generated after every EOD scan. View on GitHub: `logs/dashboard.md`*")

        DASH_FILE.write_text("\n".join(L))
        log.info("  Dashboard written → logs/dashboard.md")
    except Exception as e:
        log.warning(f"  write_dashboard failed: {e}")


# =============================================================================
#  DAILY LOG
# =============================================================================

def _read_existing_signals_section(path):
    """Return existing daily-log signal section body lines (without heading)."""
    try:
        if not path.exists():
            return None
        lines = path.read_text(encoding="utf-8").splitlines()
        start = None
        for i, line in enumerate(lines):
            if line.strip() == "## Signals":
                start = i + 1
                break
        if start is None:
            return None
        end = len(lines)
        for i in range(start, len(lines)):
            if lines[i].startswith("## ") or lines[i].strip() == "---":
                end = i
                break
        return lines[start:end]
    except Exception:
        return None


def write_daily(today, equity, cash, rgm, month, positions, signals, buys, sells,
                preserve_existing_signals=False):
    sc = SCHEDULE[month]
    op_pnl = sum(p.get("pnl_dollar", 0) for p in positions.values())
    fname  = DAILY_DIR / f"{today}.md"
    L = [f"# Daily Log -- {today}", "",
         "## Account", "| | |", "|---|---|",
         f"| Equity | **${equity:,.2f}** |",
         f"| Cash | ${cash:,.2f} |",
         f"| Reserve | ${equity*CASH_RESERVE_PCT:,.2f} |",
         f"| Open P&L | ${op_pnl:+,.2f} |",
         f"| Regime | {rgm.upper()} |",
         f"| Universe | {UNIVERSE} |",
        f"| Exit mode | midline / stop{EXIT_STOP_LOSS*100:.1f}% / {EXIT_DAYS_MAX}d max |",
         f"| Strategies | {sc['p']} + {sc['s']} (display only — schedule not enforced) |", "",
         "## Holdings"]
    if positions:
        L += ["| Ticker | Strategy | Invested | Entry | Now | P&L% | P&L$ | Days |",
              "|--------|----------|----------|-------|-----|------|------|------|"]
        for t, p in positions.items():
            dh = ""
            if p.get("entry_date"):
                try: dh = str((datetime.today() - datetime.strptime(p["entry_date"], "%Y-%m-%d")).days) + "d"
                except Exception: pass
            L.append(f"| {t} | {p.get('strategy','?')} | ${p.get('dollar_amt',0):,.2f} "
                     f"| ${p['entry_price']:.2f} | ${p['current_price']:.2f} "
                     f"| {p['pnl_pct']:+.2f}% | ${p['pnl_dollar']:+.2f} | {dh} |")
    else:
        L.append("_No open positions._")
    L += ["", "## Trades today"]
    # Source of truth: ledger entries from transactions.csv for this date.
    # This captures exits placed outside the current in-memory scan run too.
    ledger_today = []
    if TX_FILE.exists():
        try:
            with open(TX_FILE, newline="") as f:
                for r in csv.DictReader(f):
                    if r.get("date") == str(today):
                        ledger_today.append(r)
        except Exception as e:
            log.warning(f"write_daily ledger read failed: {e}")
    if ledger_today:
        ledger_today.sort(key=lambda r: r.get("timestamp", ""))
        has_grp = any(r.get("ab_group") for r in ledger_today)
        if has_grp:
            L += ["| Time | Grp | Action | Ticker | Strategy | Price | Amount | Note |",
                  "|------|-----|--------|--------|----------|-------|--------|------|"]
        else:
            L += ["| Time | Action | Ticker | Strategy | Price | Amount | Note |",
                  "|------|--------|--------|----------|-------|--------|------|"]
        for t in ledger_today:
            ts = t.get("timestamp", "")
            tm = ts[11:16] if len(ts) >= 16 else "--:--"
            action = (t.get("action") or "").upper()
            try:
                px = float(t.get("price", 0) or 0)
            except Exception:
                px = 0.0
            try:
                amt = float(t.get("dollar_amount", 0) or 0)
            except Exception:
                amt = 0.0
            note = t.get("exit_reason", "") if action == "SELL" else "--"
            note = note or "--"
            if has_grp:
                L.append(f"| {tm} | {t.get('ab_group','')} | {action:<4} | {t.get('ticker','')} | "
                         f"{t.get('strategy','?')} | ${px:.2f} | ${amt:.2f} | {note} |")
            else:
                L.append(f"| {tm} | {action:<4} | {t.get('ticker','')} | {t.get('strategy','?')} | "
                         f"${px:.2f} | ${amt:.2f} | {note} |")
    elif buys or sells:
        # Fallback for first run before ledger write is available.
        L += ["| Time | Action | Ticker | Strategy | Price | Amount | Note |",
              "|------|--------|--------|----------|-------|--------|------|"]
        for b in buys:
            L.append(f"| {b['t']} | BUY  | {b['tk']} | {b['st']} | ${b['px']:.2f} | ${b['$']:.2f} | -- |")
        for s in sells:
            L.append(f"| {s['t']} | SELL | {s['tk']} | {s['st']} | ${s['px']:.2f} | -- | {s['why']} |")
    else:
        L.append("_No trades today._")
    existing_signals = None
    if preserve_existing_signals and not signals:
        existing_signals = _read_existing_signals_section(fname)
    L += ["", "## Signals"]
    if signals:
        L += ["| Ticker | Strategy | Price | RSI | Vol Z | Trigger |",
              "|--------|----------|-------|-----|-------|---------|"]
        for s in signals:
            L.append(f"| {s['ticker']} | {s['strategy']} | ${s['close']:.2f} "
                     f"| {s.get('rsi',0):.1f} | {s.get('vol_z',0):.2f} | {s.get('trigger','')} |")
    elif existing_signals is not None:
        if existing_signals:
            L += existing_signals
        else:
            L.append("_No signals recorded yet._")
    else:
        L.append("_No signals today._")
    L += ["", "---", f"_RBv8{datetime.now().strftime('%H:%M UTC')}_"]
    fname.write_text("\n".join(L), encoding="utf-8")
    log.info(f"  Daily log -> {fname}")


# =============================================================================
#  WEEKLY SUMMARY
# =============================================================================

def year_by_year_from_log():
    """Read transactions.csv and return a list of year rows sorted oldest-first.
    Each row: {year, start_eq, end_eq, ret_pct, n_trades, win_rate, profitable}
    Uses equity_after column to track account value over time."""
    if not TX_FILE.exists():
        return []
    try:
        with open(TX_FILE, newline="") as f:
            txs = [t for t in csv.DictReader(f)
                   if t.get("equity_after") and t.get("date")]
        if not txs:
            return []

        # Group equity snapshots by year (use last equity_after per year)
        by_year = {}
        for tx in txs:
            yr  = tx["date"][:4]
            eq  = float(tx["equity_after"])
            by_year.setdefault(yr, {"first": eq, "last": eq,
                                    "trades": 0, "wins": 0})
            by_year[yr]["last"]   = eq
            by_year[yr]["trades"] += 1
            if tx["action"] == "SELL":
                pnl = float(tx.get("pnl_pct", 0))
                if pnl > 0:
                    by_year[yr]["wins"] += 1

        years = sorted(by_year.keys())
        rows  = []
        for i, yr in enumerate(years):
            d = by_year[yr]
            # start equity = previous year's end, or first tx equity for first year
            if i == 0:
                # Estimate start: first tx equity minus that trade's size
                start_eq = d["first"]
            else:
                start_eq = by_year[years[i-1]]["last"]
            end_eq   = d["last"]
            ret_pct  = (end_eq - start_eq) / start_eq * 100 if start_eq > 0 else 0
            sells    = [tx for tx in txs
                        if tx["date"][:4] == yr and tx["action"] == "SELL"]
            n_sells  = len(sells)
            wins     = sum(1 for t in sells if float(t.get("pnl_pct", 0)) > 0)
            win_rate = wins / n_sells * 100 if n_sells > 0 else 0
            rows.append({"year": yr, "start_eq": start_eq, "end_eq": end_eq,
                         "ret_pct": ret_pct, "n_trades": d["trades"],
                         "win_rate": win_rate,
                         "profitable": ret_pct > 0})
        return rows
    except Exception as e:
        log.debug(f"year_by_year_from_log: {e}")
        return []


def write_weekly(client, equity, cash):
    today = date.today(); wk = today.isocalendar()[1]
    fname = WEEKLY_DIR / f"{today.year}-W{wk:02d}.md"
    positions = enrich(client, get_positions(client))
    week_tx = []
    all_tx  = []
    if TX_FILE.exists():
        with open(TX_FILE, newline="") as f:
            all_tx = list(csv.DictReader(f))
        for tx in all_tx:
            try:
                if datetime.strptime(tx["date"], "%Y-%m-%d").date() >= today - timedelta(days=7):
                    week_tx.append(tx)
            except Exception: pass
    buys     = [t for t in week_tx if t["action"] == "BUY"]
    sells    = [t for t in week_tx if t["action"] == "SELL"]
    real_pnl = sum(float(t.get("pnl_dollar", 0)) for t in sells)
    open_pnl = sum(p.get("pnl_dollar", 0) for p in positions.values())
    invested = sum(p.get("dollar_amt", 0) for p in positions.values())

    # ── Compute extra stats ───────────────────────────────────────────────────
    week_sells   = [t for t in sells]
    week_wins    = sum(1 for t in week_sells if float(t.get("pnl_pct", 0)) > 0)
    week_wr      = week_wins / len(week_sells) * 100 if week_sells else 0
    all_sells    = [t for t in all_tx if t["action"] == "SELL"]
    all_real_pnl = sum(float(t.get("pnl_dollar", 0)) for t in all_sells)
    hold_days    = []
    for t in all_sells:
        try:
            hd = int(t.get("hold_days", 0))
            if hd > 0: hold_days.append(hd)
        except Exception: pass
    avg_hold = sum(hold_days) / len(hold_days) if hold_days else 0
    pdt_used  = _count_buys_today()
    reserve   = equity * CASH_RESERVE_PCT
    wk_avail  = max(0.0, cash - reserve)
    wk_max_t  = max(1, int(wk_avail // MIN_TRADE_SIZE))
    sc       = SCHEDULE[today.month]
    nm       = today.month % 12 + 1; ns = SCHEDULE[nm]
    all_eq_start = float(all_tx[0]["equity_after"]) if all_tx else equity
    all_ret      = (equity - all_eq_start) / all_eq_start * 100 if all_eq_start else 0

    # ── Terminal display ──────────────────────────────────────────────────────
    hdr(f"RUBBER BAND BOT  |  Week {wk} / {today.year}  |  {'PAPER' if PAPER_TRADING else 'LIVE'}")
    div()
    row("Date",            f"{today}  ({MN[today.month]})")
    row("Regime",          rgm.upper())
    row("Strategy",        f"{sc['p']}  +  {sc['s']} (display only — schedule not enforced)")
    row("Execution",       "Summary mode only (no orders submitted)")
    row("Buys today",    f"{pdt_used}")
    row("Cash-based cap",  f"{wk_max_t} max trades with current available cash")
    div()
    # Two-column account layout
    def _col2(l1, v1, l2, v2):
        left  = f"  {l1:<16} {v1:<12}"
        right = f"  {l2:<16} {v2}"
        line  = f"{left}{right}"
        if len(line) > W: line = line[:W]
        print(f"|{line}{' '*(W-len(line))}|")

    _col2("Equity",    f"${equity:,.2f}",   "Cash",        f"${cash:,.2f}")
    _col2("Invested",  f"${invested:,.2f}",  "Available",   f"${max(0,cash - equity*CASH_RESERVE_PCT):,.2f}")
    _col2("Open P&L",  f"${open_pnl:+,.2f}", "Realized P&L",f"${all_real_pnl:+,.2f}")
    div()
    row("This week",       f"{len(buys)} buys  |  {len(sells)} sells  |  "
                           f"Win rate {week_wr:.0f}%  |  P&L ${real_pnl:+,.2f}")
    row("All time",        f"{len(all_tx)} trades  |  Avg hold {avg_hold:.1f}d  |  "
                           f"Return {all_ret:+.1f}%  |  P&L ${all_real_pnl:+,.2f}")
    div()
    if positions:
        shown = 0
        trow("TICKER","STRATEGY","INVESTED","ENTRY","NOW","P&L%","P&L$",
             widths=[6,13,9,8,8,8,10])
        div()
        for t, p in positions.items():
            if shown >= WEEKLY_MAX_HOLDINGS_PRINT:
                break
            pnl_flag = " !" if p["pnl_pct"] <= EXIT_STOP_LOSS * 100 else ""
            trow(t, p.get("strategy","?"),
                 f"${p.get('dollar_amt',0):.2f}",
                 f"${p['entry_price']:.2f}",
                 f"${p['current_price']:.2f}",
                 f"{p['pnl_pct']:+.1f}%{pnl_flag}",
                 f"${p['pnl_dollar']:+.2f}",
                 widths=[6,13,9,8,8,8,10])
            shown += 1
        if len(positions) > shown:
            blank()
            row("More holdings",
                f"Showing {shown}/{len(positions)} in terminal; full list in weekly markdown file")
    else:
        blank(); row("  No open positions."); blank()
    div()
    row("Next month",      f"{MN[nm]}:  {ns['p']}  +  {ns['s']}")
    ftr()

    # ── Year-by-year performance ──────────────────────────────────────────────
    yr_rows = year_by_year_from_log()
    if yr_rows:
        hdr("YEAR-BY-YEAR PERFORMANCE")
        trow("YEAR","START","END","RETURN","P&L $","TRADES","WIN%",
             widths=[5,8,8,8,10,7,10])
        div()
        for r in yr_rows:
            flag = " ✓" if r["profitable"] else " ✗"
            dollar_pnl = r["end_eq"] - r["start_eq"]
            trow(r["year"],
                 f"${r['start_eq']:,.0f}",
                 f"${r['end_eq']:,.0f}",
                 f"{r['ret_pct']:+.1f}%",
                 f"${dollar_pnl:+,.2f}",
                 str(r["n_trades"]),
                 f"{r['win_rate']:.1f}%{flag}",
                 widths=[5,8,8,8,10,7,10])
        div()
        profitable_n = sum(1 for r in yr_rows if r["profitable"])
        best  = max(yr_rows, key=lambda r: r["ret_pct"])
        worst = min(yr_rows, key=lambda r: r["ret_pct"])
        row("Profitable years", f"{profitable_n}/{len(yr_rows)}  ({profitable_n/len(yr_rows)*100:.0f}%)")
        row("Best  year",       f"{best['year']}   {best['ret_pct']:+.1f}%   ${best['end_eq']-best['start_eq']:+,.2f}")
        row("Worst year",       f"{worst['year']}   {worst['ret_pct']:+.1f}%   ${worst['end_eq']-worst['start_eq']:+,.2f}")
        ftr()

    L = [f"# Weekly Summary -- Week {wk}, {today.year}", f"_{today}_", "",
         "## Account", "| | |", "|---|---|",
         f"| Equity | **${equity:,.2f}** |",
         f"| Cash | ${cash:,.2f} |",
         f"| Invested | ${invested:,.2f} |",
         f"| Open P&L | ${open_pnl:+,.2f} |",
         f"| Realised P&L | ${real_pnl:+,.2f} |", ""]

    # Year-by-year section in markdown
    if yr_rows:
        L += ["## Year-by-Year Performance",
              "| Year | Start | End | Return | Trades | Win% | Profitable |",
              "|------|-------|-----|--------|--------|------|------------|"]
        for r in yr_rows:
            flag = "✅" if r["profitable"] else "❌"
            L.append(f"| {r['year']} | ${r['start_eq']:,.0f} | ${r['end_eq']:,.0f} "
                     f"| **{r['ret_pct']:+.1f}%** | {r['n_trades']:,} "
                     f"| {r['win_rate']:.1f}% | {flag} |")
        profitable_n = sum(1 for r in yr_rows if r["profitable"])
        L += [f"",
              f"_{profitable_n}/{len(yr_rows)} years profitable_", ""]

    L += ["## Holdings"]
    if positions:
        L += ["| Ticker | Strategy | Invested | Entry | Now | P&L% | P&L$ |",
              "|--------|----------|----------|-------|-----|------|------|"]
        for t, p in positions.items():
            L.append(f"| {t} | {p.get('strategy','?')} | ${p.get('dollar_amt',0):,.2f} "
                     f"| ${p['entry_price']:.2f} | ${p['current_price']:.2f} "
                     f"| {p['pnl_pct']:+.2f}% | ${p['pnl_dollar']:+.2f} |")
    else:
        L.append("_No open positions._")
    L += ["", "## Trades this week"]
    if week_tx:
        L += ["| Date | Action | Ticker | Strategy | Amount | P&L |",
              "|------|--------|--------|----------|--------|-----|"]
        for t in week_tx:
            pstr = f"${float(t.get('pnl_dollar',0)):+.2f}" if t["action"] == "SELL" else "--"
            L.append(f"| {t['date']} | {t['action']} | {t['ticker']} "
                     f"| {t['strategy']} | ${float(t['dollar_amount']):.2f} | {pstr} |")
    else:
        L.append("_No trades this week._")
    nm = today.month % 12 + 1; ns = SCHEDULE[nm]
    L += ["", "## Next session",
          f"- Month: **{MN[nm]}**",
          f"- Primary: **{ns['p']}**   Secondary: **{ns['s']}**",
          f"- Note: {ns['note']}", "", "---",
          f"_RBv8{datetime.now().strftime('%Y-%m-%d %H:%M UTC')}_"]
    fname.write_text("\n".join(L), encoding="utf-8")
    log.info(f"  Weekly summary -> {fname}")


# =============================================================================
#  PREP PLAN CACHE (two-phase runs)
# =============================================================================

def _plan_file_for_mode(mode_name):
    if mode_name == "morning":
        return MORNING_PLAN_FILE
    return EVENING_PLAN_FILE


def _save_plan(path, payload):
    try:
        payload["saved_at_utc"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        return True
    except Exception as e:
        log.warning(f"  plan save failed {path}: {e}")
        return False


def _load_plan(path):
    try:
        if not path.exists():
            return None
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        log.warning(f"  plan load failed {path}: {e}")
        return None


def _plan_fresh_minutes(plan):
    try:
        ts = plan.get("saved_at_utc", "")
        if not ts:
            return None
        saved = datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ")
        return (datetime.utcnow() - saved).total_seconds() / 60.0
    except Exception:
        return None


def _snapshot_open_sell_orders(client):
    rows = []
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN)
        for o in client.get_orders(req):
            if getattr(o, "side", None) == OrderSide.SELL:
                rows.append({
                    "ticker": getattr(o, "symbol", "?"),
                    "type": str(getattr(o, "order_type", "?")),
                    "qty": str(getattr(o, "qty", "")),
                    "limit": str(getattr(o, "limit_price", "")),
                    "stop": str(getattr(o, "stop_price", "")),
                })
    except Exception:
        pass
    return rows


def _plan_usable(plan, mode_name, rgm, month, positions=None, open_sell_orders=None):
    if not plan:
        return False, "missing"
    age_min = _plan_fresh_minutes(plan)
    if age_min is None:
        return False, "no timestamp"
    if age_min > PLAN_MAX_AGE_MIN:
        return False, f"stale ({age_min:.1f}m)"
    if plan.get("mode_name") != mode_name:
        return False, "mode mismatch"
    if plan.get("regime") != rgm:
        return False, "regime changed"
    if int(plan.get("month", -1)) != int(month):
        return False, "month changed"
    if positions is not None:
        try:
            cached_count = int(plan.get("positions_count", -1))
        except Exception:
            cached_count = -1
        if cached_count >= 0 and cached_count != len(positions):
            return False, "positions changed"
        cached_tickers = sorted(
            str(p.get("ticker", "")).upper()
            for p in plan.get("positions_snapshot", [])
            if p.get("ticker")
        )
        live_tickers = sorted(str(t).upper() for t in positions.keys())
        if cached_tickers != live_tickers:
            return False, "positions changed"
    if open_sell_orders is not None:
        def _ord_key(o):
            return (
                str(o.get("ticker", "")).upper(),
                str(o.get("type", "")).lower(),
                str(o.get("qty", "")).strip(),
                str(o.get("limit", "")).strip(),
                str(o.get("stop", "")).strip(),
            )
        cached_orders = sorted(_ord_key(o) for o in plan.get("open_sell_orders", []))
        live_orders = sorted(_ord_key(o) for o in open_sell_orders)
        if cached_orders != live_orders:
            return False, "open sell orders changed"
    return True, f"fresh ({age_min:.1f}m)"


def _plan_signals_cacheable(plan, mode_name, rgm, month):
    """Signals-only cache: ignore position changes (exits still evaluated live)."""
    if not plan:
        return False, "missing"
    age_min = _plan_fresh_minutes(plan)
    if age_min is None:
        return False, "no timestamp"
    if age_min > PLAN_MAX_AGE_MIN:
        return False, f"stale ({age_min:.1f}m)"
    if plan.get("mode_name") != mode_name:
        return False, "mode mismatch"
    if plan.get("regime") != rgm:
        return False, "regime changed"
    if int(plan.get("month", -1)) != int(month):
        return False, "month changed"
    return True, f"signals fresh ({age_min:.1f}m)"


def build_plan(client, equity, cash, rgm, mode_name):
    """
    Build a cached plan with:
      - exit candidates (sell if needed) from current positions
      - entry candidates (signals) from full universe scan
    mode_name: "morning" or "evening"
    """
    month = date.today().month
    positions = enrich(client, get_positions(client))
    positions_snapshot = []
    for ticker, p in positions.items():
        positions_snapshot.append({
            "ticker": ticker,
            "strategy": p.get("strategy", "?"),
            "dollar_amt": float(p.get("dollar_amt", 0) or 0),
            "entry_price": float(p.get("entry_price", 0) or 0),
            "current_price": float(p.get("current_price", 0) or 0),
            "pnl_pct": float(p.get("pnl_pct", 0) or 0),
            "pnl_dollar": float(p.get("pnl_dollar", 0) or 0),
        })
    pos_data = fetch_batch(list(positions.keys()), "prep_positions") if positions else {}

    exit_plan = []
    for ticker, pos in positions.items():
        pnl_frac = pos.get("pnl_pct", 0) / 100

        if pnl_frac <= EXIT_STOP_LOSS:
            exit_plan.append({"ticker": ticker, "why": f"stop_loss ({pnl_frac*100:.1f}%)"})
            continue
        if pos.get("entry_date"):
            try:
                days = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days
                if days >= EXIT_DAYS_MAX:
                    exit_plan.append({"ticker": ticker, "why": f"max_hold {days}d ({pnl_frac*100:+.1f}%)"})
                    continue
            except Exception:
                pass
        if ticker in pos_data:
            # Keep existing behavior: scan path uses eod_only=True for midline checks.
            ex, why = check_exit(pos_data[ticker], pos, eod_only=True)
            if ex:
                exit_plan.append({"ticker": ticker, "why": why})

    tickers = get_live_tickers()
    scan = [t for t in tickers if t not in positions]
    all_data = fetch_batch(scan, "prep_universe")
    signals = []
    for ticker, df in all_data.items():
        for s in get_signals(ticker, df, month, rgm):
            s["month"] = month
            s["regime"] = rgm
            signals.append(s)

    open_sell_orders = _snapshot_open_sell_orders(client)

    payload = {
        "mode_name": mode_name,
        "date": str(date.today()),
        "month": month,
        "regime": rgm,
        "positions_count": len(positions),
        "positions_snapshot": positions_snapshot,
        "open_sell_orders": open_sell_orders,
        "scan_universe_count": len(scan),
        "exit_plan": exit_plan,
        "signals": signals,
    }
    return payload


def run_prep(client, equity, cash, rgm, mode_name):
    """Pre-compute exits + signals and save cache for the next execution run."""
    plan_file = _plan_file_for_mode(mode_name)
    hdr(f"{mode_name.upper()} PREP")
    row("Goal", "Precompute exits/signals for next execution run")
    row("Plan file", str(plan_file))
    row("Regime", rgm.upper())
    ftr()

    # Reuse a fresh prep plan when positions/open sell orders/regime/month are unchanged.
    # This avoids repeatedly downloading/scanning the full universe across adjacent prep runs.
    cached = _load_plan(plan_file)
    positions_now = enrich(client, get_positions(client))
    open_sell_orders_now = _snapshot_open_sell_orders(client)
    month_now = date.today().month
    cache_ok, cache_note = _plan_usable(
        cached,
        mode_name,
        rgm,
        month_now,
        positions=positions_now,
        open_sell_orders=open_sell_orders_now,
    )
    if USE_TWO_PHASE_PLAN and cache_ok:
        hdr("PREP CACHE")
        row("Using cached plan", f"yes ({cache_note})")
        row("Exit candidates", str(len(cached.get("exit_plan", []))))
        row("Signal candidates", str(len(cached.get("signals", []))))
        row("Universe scanned", str(cached.get("scan_universe_count", 0)))
        ftr()
        log.info("  Prep cache reused; skipped full universe scan")
        return

    plan = build_plan(client, equity, cash, rgm, mode_name)
    ok = _save_plan(plan_file, plan)
    pos_rows = plan.get("positions_snapshot", [])
    open_pnl = sum(float(p.get("pnl_dollar", 0) or 0) for p in pos_rows)
    invested = sum(float(p.get("dollar_amt", 0) or 0) for p in pos_rows)

    hdr("OPEN POSITION P&L SNAPSHOT")
    row("Open positions", str(len(pos_rows)))
    row("Invested", f"${invested:,.2f}")
    row("Open P&L", f"${open_pnl:+,.2f}")
    if pos_rows:
        trow("TICKER", "STRATEGY", "INVESTED", "ENTRY", "NOW", "P&L%", "P&L$",
             widths=[7, 14, 9, 7, 7, 6, 7])
        div()
        for p in pos_rows:
            trow(
                p.get("ticker", "?"),
                p.get("strategy", "?"),
                f"${float(p.get('dollar_amt', 0) or 0):.2f}",
                f"${float(p.get('entry_price', 0) or 0):.2f}",
                f"${float(p.get('current_price', 0) or 0):.2f}",
                f"{float(p.get('pnl_pct', 0) or 0):+.1f}%",
                f"${float(p.get('pnl_dollar', 0) or 0):+.2f}",
                widths=[7, 14, 9, 7, 7, 6, 7],
            )
    else:
        blank(); row("No open positions."); blank()
    ftr()

    hdr("OPEN SELL ORDERS")
    sell_orders = plan.get("open_sell_orders", [])
    row("Count", str(len(sell_orders)))
    if sell_orders:
        trow("TICKER", "TYPE", "QTY", "LIMIT", "STOP", widths=[8, 16, 8, 10, 10])
        div()
        for o in sell_orders:
            trow(
                o.get("ticker", "?"),
                _trunc(o.get("type", "?"), 16),
                _trunc(o.get("qty", ""), 8),
                _trunc(o.get("limit", ""), 10),
                _trunc(o.get("stop", ""), 10),
                widths=[8, 16, 8, 10, 10],
            )
    else:
        blank(); row("No open sell orders."); blank()
    ftr()

    hdr("PREP SUMMARY")
    row("Saved", "yes" if ok else "no")
    row("Exit candidates", str(len(plan.get("exit_plan", []))))
    row("Signal candidates", str(len(plan.get("signals", []))))
    row("Universe scanned", str(plan.get("scan_universe_count", 0)))
    ftr()


# =============================================================================
#  TIME AUTO-DETECTION
# =============================================================================

def detect_mode():
    # Use real US Eastern time (handles EDT/EST automatically via zoneinfo).
    from zoneinfo import ZoneInfo
    now = datetime.now(ZoneInfo("America/New_York"))
    h = now.hour; m = now.minute; dow = now.weekday()
    if dow >= 5: return "weekly"
    # Friday: keep running extended-hours exits through 7:59pm ET.
    # Switch to weekly summary only after extended-hours window closes.
    if dow == 4 and h >= 20: return "weekly"
    # Morning prep: 9:30–9:43am ET (compute plan only, no orders).
    if h == 9 and 30 <= m <= 43: return "morning_prep"
    # Morning scan: 9:44–9:59am ET (exits + entries).
    if h == 9 and m >= 44: return "morning_scan"
    # Evening scan: 3:44–3:59pm ET
    if h == 15 and m >= 44: return "scan"
    # Evening prep: 3:30–3:43pm ET (Chicago 2:30 cron)
    if h == 15 and 30 <= m <= 43: return "evening_prep"
    # Post-market extended-hours exits: 4:00pm–8:00pm ET
    # Alpaca allows DAY limit sells in extended hours. No new buys.
    if h == 16 or (17 <= h <= 19): return "ext_exits"
    # Exits only: 10:00am–3:29pm ET (between scan windows)
    if (10 <= h <= 14) or (h == 15 and m < 30): return "exits"
    return "summary"


# =============================================================================
#  STATUS SUMMARY
# =============================================================================

def run_summary(client, equity, cash, rgm):
    # Safety net: create today's daily log if scan lost its git push
    reconcile_daily_log(client, equity, cash, rgm)

    positions = enrich(client, get_positions(client))
    invested  = sum(p.get("dollar_amt", 0) for p in positions.values())
    open_pnl  = sum(p.get("pnl_dollar", 0) for p in positions.values())

    hdr("ACCOUNT STATUS")
    row("Equity",         f"${equity:,.2f}")
    row("Cash",           f"${cash:,.2f}")
    row("Regime",         rgm.upper())
    row("Universe",       UNIVERSE)
    row("Total invested", f"${invested:,.2f}")
    row("Open P&L",       f"${open_pnl:+,.2f}")
    ftr()

    hdr(f"HOLDINGS  ({len(positions)} positions)")
    if positions:
        trow("TICKER","STRATEGY","INVESTED","ENTRY","NOW","P&L%","P&L$",
             widths=[7,14,9,7,7,6,7])
        div()
        for t, p in positions.items():
            trow(t, p.get("strategy","?"),
                 f"${p.get('dollar_amt',0):.2f}", f"${p['entry_price']:.2f}",
                 f"${p['current_price']:.2f}", f"{p['pnl_pct']:+.1f}%",
                 f"${p['pnl_dollar']:+.2f}", widths=[7,14,9,7,7,6,7])
        blank()
        row("Total invested", f"${invested:,.2f}")
        row("Total open P&L", f"${open_pnl:+,.2f}")
    else:
        blank(); row("No open positions."); blank()
    ftr()

    hdr("EXIT LOGIC ACTIVE  (v8)")
    row("Profit target",  "price > 20-day MA (midline)")
    row("Stop loss",      f"{EXIT_STOP_LOSS*100:.1f}% from entry")
    row("Time stop",      f"max {EXIT_DAYS_MAX} calendar days")
    ftr()

    hdr("RECENT TRANSACTIONS")
    if TX_FILE.exists():
        with open(TX_FILE, newline="") as f: txs = list(csv.DictReader(f))
        for tx in (txs[-6:] if len(txs) >= 6 else txs)[::-1]:
            pnl = f"  P&L ${float(tx.get('pnl_dollar',0)):+.2f}" if tx["action"] == "SELL" else ""
            row(f"{tx['date']}  {tx['action']}  {tx['ticker']}  "
                f"{tx['strategy']}  ${float(tx['dollar_amount']):.2f}{pnl}")
    else:
        row("No transactions yet.")
    ftr()
    log_run("summary", rgm, equity, cash, 0, 0, 0, positions)


# =============================================================================
#  DAILY LOG SAFETY NET
# =============================================================================

def reconcile_daily_log(client, equity, cash, rgm):
    """Refresh today's daily markdown from transactions.csv when needed."""
    today = date.today()
    fname = DAILY_DIR / f"{today}.md"
    ledger = []
    if TX_FILE.exists():
        with open(TX_FILE, newline="") as f:
            for r in csv.DictReader(f):
                if r.get("date") == str(today):
                    ledger.append(r)

    if fname.exists():
        text = fname.read_text(encoding="utf-8")
        if "Fallback log" not in text and "_No trades today._" not in text:
            if not ledger:
                return
        # stale fallback or missing trades — rebuild below
    elif not ledger and not _past_evening_scan_window():
        return

    try:
        positions = enrich(client, get_positions(client))
        write_daily(today, equity, cash, rgm, today.month, positions,
                    signals=[], buys=[], sells=[],
                    preserve_existing_signals=fname.exists())
        log.info(f"  Daily log reconciled -> {fname} ({len(ledger)} ledger rows)")
    except Exception as e:
        log.warning(f"  reconcile_daily_log failed: {e}")


def _past_evening_scan_window():
    from zoneinfo import ZoneInfo
    now = datetime.now(ZoneInfo("America/New_York"))
    return now.hour >= 16 or (now.hour == 15 and now.minute >= 44)


# =============================================================================
#  EXITS RUN
# =============================================================================

def run_exits(client, equity, cash, rgm, extended_hours=False):
    """Exit check for open positions.

    extended_hours=False  (9:35am run): regular hours; market-order fallback
                          allowed; GTC stops re-placed on any position missing one.
    extended_hours=True   (4:15pm run): Alpaca extended hours (4pm–8pm ET);
                          limit orders only — no market orders, no GTC placement.
                          Checks stop-loss and max-hold exits only (no midline —
                          midline uses today's close which is already final).
    """
    # Safety net: if today's daily log is missing (scan lost its git push),
    # write a fallback log now so we always have a record for every trading day.
    reconcile_daily_log(client, equity, cash, rgm)

    eh_tag = " [EXTENDED HRS]" if extended_hours else ""

    # Regular hours only: place GTC stops at start of morning exits.
    # Extended hours: GTC stops don't trigger after 4pm, limit sells are
    # the only mechanism available — handled below in the exit loop.
    if not extended_hours:
        place_all_stops(client)

    positions = enrich(client, get_positions(client))
    mode_label = "EXTENDED HOURS EXIT" if extended_hours else "MORNING CHECK"
    run_mode_name = "ext_exits" if extended_hours else "exits"
    if not positions:
        hdr(mode_label); blank(); row("No open positions."); blank(); ftr()
        log_run(run_mode_name, rgm, equity, cash, 0, 0, 0, {}); return

    pos_data = fetch_batch(list(positions.keys()), "positions") if not extended_hours else {}
    exits = 0
    exited = set()

    # Load today's sells to prevent duplicate logging
    already_sold_today = set()
    today_str = str(date.today())
    if TX_FILE.exists():
        with open(TX_FILE, newline="") as _f:
            for _r in csv.DictReader(_f):
                if _r.get("action") == "SELL" and _r.get("date") == today_str:
                    sm = (_r.get("sell_method") or "").lower()
                    if "partial" in sm:
                        continue
                    already_sold_today.add(_r["ticker"])

    hdr(f"EXIT CHECK{eh_tag}")
    exit_desc = f"stop{EXIT_STOP_LOSS*100:.1f}% / {EXIT_DAYS_MAX}d max"
    if not extended_hours:
        exit_desc += "  (midline at EOD only)"
    else:
        exit_desc += "  (midline skipped — close already final)"
    row("Exit logic", exit_desc)
    div()

    eh_sells = []   # collect ext-hours sells for summary section
    stats = {
        "already_logged": 0,
        "no_data_skip": 0,
        "attempted": 0,
        "filled": 0,
        "partial": 0,
        "pending": 0,
        "failed": 0,
        "holds": 0,
    }
    stop_breaches = {}
    stoploss_look_items = {}

    sorted_positions = sorted(
        positions.items(),
        key=lambda kv: float(kv[1].get("pnl_pct", 0) or 0),
    )
    for ticker, pos in sorted_positions:
        if ticker in already_sold_today and abs(float(pos.get("qty", 0) or 0)) <= 1e-6:
            stats["already_logged"] += 1
            continue

        pnl_frac = pos.get("pnl_pct", 0) / 100
        if pnl_frac <= EXIT_STOP_LOSS:
            stop_breaches[ticker] = pnl_frac

        entry_date = pos.get("entry_date", "")
        entered_today = (entry_date == str(date.today()))

        # ── Stop-loss: Alpaca unrealized P&L — no yfinance needed ─────────
        if pnl_frac <= EXIT_STOP_LOSS:
            why = f"stop_loss ({pnl_frac*100:.1f}%)"
            row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%  ${pos['pnl_dollar']:+.2f}",
                f"EXIT{eh_tag}: {_trunc(why,22)}")
            stats["attempted"] += 1
            sell_res = do_sell(client, ticker, extended_hours=extended_hours, urgency="urgent")
            if sell_res.get("ok") and sell_res.get("filled"):
                if sell_res.get("exit_complete", True):
                    stats["filled"] += 1
                    exits += 1; exited.add(ticker); already_sold_today.add(ticker)
                    cur = sell_res.get("price") if sell_res.get("price") is not None else pos["current_price"]
                    sold_dollars = sell_res.get("dollars") if sell_res.get("dollars") is not None else pos["market_value"]
                    dh  = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days \
                          if pos.get("entry_date") else 0
                    log_tx("SELL", ticker, pos.get("strategy","?"), cur, sold_dollars,
                           rgm, float(get_account_safe(client).equity),
                           pos["pnl_pct"], pos["pnl_dollar"], dh, why,
                           sell_method=sell_res.get("sell_method",""),
                           cur_at_submit=sell_res.get("cur_at_submit"),
                           bid_at_submit=sell_res.get("bid_at_submit"),
                           limit_price_used=sell_res.get("limit_price_used"),
                           sell_latency_s=sell_res.get("sell_latency_s"),
                           fill_slippage_bps=sell_res.get("fill_slippage_bps"))
                    _clear_fractional_watch(ticker)
                    if extended_hours:
                        eh_sells.append((ticker, pos.get("strategy","?"), pos["pnl_pct"],
                                         pos["pnl_dollar"], why))
                else:
                    stats["partial"] += 1
                    rem = sell_res.get("remaining_qty")
                    rem_txt = f"{float(rem):.4f} sh remain" if rem is not None else "residual shares remain"
                    row(ticker, f"PARTIAL SELL ({rem_txt}) — will retry this session")
            elif sell_res.get("pending"):
                stats["pending"] += 1
                uid = f"{ticker}|{entry_date or 'unknown'}"
                stoploss_look_items[uid] = {
                    "id": uid,
                    "ticker": ticker,
                    "strategy": pos.get("strategy", "?"),
                    "entry_date": entry_date or "unknown",
                    "pnl_frac": pnl_frac,
                    "root_cause": "After-hours limit still pending",
                    "explanation": "Stop breached but extended-hours order is limit-only and did not fill immediately; follow-up occurs next regular-hours run.",
                }
                row(ticker, "SELL pending (after-hours limit open)")
            else:
                stats["failed"] += 1
                uid = f"{ticker}|{entry_date or 'unknown'}"
                stoploss_look_items[uid] = {
                    "id": uid,
                    "ticker": ticker,
                    "strategy": pos.get("strategy", "?"),
                    "entry_date": entry_date or "unknown",
                    "pnl_frac": pnl_frac,
                    "root_cause": "Sell attempt failed",
                    "explanation": "Stop breached and an exit was attempted, but the broker/order flow returned a failure state.",
                }
                row(ticker, "SELL attempt failed (will retry next run)")
            continue

        # ── Max-hold: position data only — no yfinance needed ─────────────
        if pos.get("entry_date"):
            try:
                days = (datetime.today() -
                        datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days
                if days >= EXIT_DAYS_MAX:
                    why = f"max_hold {days}d ({pnl_frac*100:+.1f}%)"
                    row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%  ${pos['pnl_dollar']:+.2f}",
                        f"EXIT{eh_tag}: {_trunc(why,22)}")
                    stats["attempted"] += 1
                    sell_res = do_sell(client, ticker, extended_hours=extended_hours, urgency="normal")
                    if sell_res.get("ok") and sell_res.get("filled"):
                        if sell_res.get("exit_complete", True):
                            stats["filled"] += 1
                            exits += 1; exited.add(ticker); already_sold_today.add(ticker)
                            cur = sell_res.get("price") if sell_res.get("price") is not None else pos["current_price"]
                            sold_dollars = sell_res.get("dollars") if sell_res.get("dollars") is not None else pos["market_value"]
                            log_tx("SELL", ticker, pos.get("strategy","?"), cur, sold_dollars,
                                   rgm, float(get_account_safe(client).equity),
                                   pos["pnl_pct"], pos["pnl_dollar"], days, why,
                                   sell_method=sell_res.get("sell_method",""),
                                   cur_at_submit=sell_res.get("cur_at_submit"),
                                   bid_at_submit=sell_res.get("bid_at_submit"),
                                   limit_price_used=sell_res.get("limit_price_used"),
                                   sell_latency_s=sell_res.get("sell_latency_s"),
                                   fill_slippage_bps=sell_res.get("fill_slippage_bps"))
                            if extended_hours:
                                eh_sells.append((ticker, pos.get("strategy","?"), pos["pnl_pct"],
                                                 pos["pnl_dollar"], why))
                        else:
                            stats["partial"] += 1
                            rem = sell_res.get("remaining_qty")
                            rem_txt = f"{float(rem):.4f} sh remain" if rem is not None else "residual shares remain"
                            row(ticker, f"PARTIAL SELL ({rem_txt}) — will retry this session")
                    elif sell_res.get("pending"):
                        stats["pending"] += 1
                        uid = f"{ticker}|{entry_date or 'unknown'}"
                        stoploss_look_items[uid] = {
                            "id": uid,
                            "ticker": ticker,
                            "strategy": pos.get("strategy", "?"),
                            "entry_date": entry_date or "unknown",
                            "pnl_frac": pnl_frac,
                            "root_cause": "After-hours limit still pending",
                            "explanation": "Stop breached but extended-hours order is limit-only and did not fill immediately; follow-up occurs next regular-hours run.",
                        }
                        row(ticker, "SELL pending (after-hours limit open)")
                    else:
                        stats["failed"] += 1
                        uid = f"{ticker}|{entry_date or 'unknown'}"
                        stoploss_look_items[uid] = {
                            "id": uid,
                            "ticker": ticker,
                            "strategy": pos.get("strategy", "?"),
                            "entry_date": entry_date or "unknown",
                            "pnl_frac": pnl_frac,
                            "root_cause": "Sell attempt failed",
                            "explanation": "Stop breached and an exit was attempted, but the broker/order flow returned a failure state.",
                        }
                        row(ticker, "SELL attempt failed (will retry next run)")
                    continue
            except Exception: pass

        # ── Midline: needs price/MA data from yfinance ─────────────────────
        # Skip midline check in extended hours — today's close is already baked
        # into signals; midline exits are better handled by the 9:35am run.
        if extended_hours:
            strat = pos.get("strategy", "midline")
            stats["holds"] += 1
            row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%  ${pos['pnl_dollar']:+.2f}",
                f"HOLDING until 9:35am scan ({strat})")
            continue
        if ticker not in pos_data:
            stats["no_data_skip"] += 1
            row(ticker, "no price data (stop/max-hold already checked)"); continue
        ex, why = check_exit(pos_data[ticker], pos, eod_only=False)
        row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%  ${pos['pnl_dollar']:+.2f}",
            f"EXIT: {_trunc(why,22)}" if ex else "HOLD")
        sell_res = do_sell(client, ticker, urgency="low") if ex else {"ok": False, "filled": False}
        if ex and sell_res.get("ok") and sell_res.get("filled"):
            stats["attempted"] += 1
            if sell_res.get("exit_complete", True):
                stats["filled"] += 1
                exits += 1; exited.add(ticker); already_sold_today.add(ticker)
                cur = sell_res.get("price") if sell_res.get("price") is not None else pos["current_price"]
                sold_dollars = sell_res.get("dollars") if sell_res.get("dollars") is not None else pos["market_value"]
                dh  = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days \
                      if pos.get("entry_date") else 0
                log_tx("SELL", ticker, pos.get("strategy","?"), cur, sold_dollars,
                       rgm, float(get_account_safe(client).equity),
                       pos["pnl_pct"], pos["pnl_dollar"], dh, why,
                       sell_method=sell_res.get("sell_method",""),
                       cur_at_submit=sell_res.get("cur_at_submit"),
                       bid_at_submit=sell_res.get("bid_at_submit"),
                       limit_price_used=sell_res.get("limit_price_used"),
                       sell_latency_s=sell_res.get("sell_latency_s"),
                       fill_slippage_bps=sell_res.get("fill_slippage_bps"))
            else:
                stats["partial"] += 1
                rem = sell_res.get("remaining_qty")
                rem_txt = f"{float(rem):.4f} sh remain" if rem is not None else "residual shares remain"
                row(ticker, f"PARTIAL SELL ({rem_txt}) — will retry this session")
        elif ex and sell_res.get("pending"):
            stats["attempted"] += 1
            stats["pending"] += 1
            uid = f"{ticker}|{entry_date or 'unknown'}"
            stoploss_look_items[uid] = {
                "id": uid,
                "ticker": ticker,
                "strategy": pos.get("strategy", "?"),
                "entry_date": entry_date or "unknown",
                "pnl_frac": pnl_frac,
                "root_cause": "After-hours limit still pending",
                "explanation": "Stop breached but extended-hours order is limit-only and did not fill immediately; follow-up occurs next regular-hours run.",
            }
            row(ticker, "SELL pending (after-hours limit open)")
        elif ex:
            stats["attempted"] += 1
            stats["failed"] += 1
            uid = f"{ticker}|{entry_date or 'unknown'}"
            stoploss_look_items[uid] = {
                "id": uid,
                "ticker": ticker,
                "strategy": pos.get("strategy", "?"),
                "entry_date": entry_date or "unknown",
                "pnl_frac": pnl_frac,
                "root_cause": "Sell attempt failed",
                "explanation": "Stop breached and an exit was attempted, but the broker/order flow returned a failure state.",
            }
            row(ticker, "SELL attempt failed (will retry next run)")
        else:
            stats["holds"] += 1
    ftr()

    # ── Extended-hours sells summary ──────────────────────────────────────
    if extended_hours and eh_sells:
        hdr("EXTENDED HOURS SELLS")
        trow("TICKER", "STRATEGY", "P&L%", "P&L$", "REASON",
             widths=[8, 14, 7, 8, 28])
        div()
        total_pnl = 0.0
        for ticker, strat, pnl_pct, pnl_dollar, why in eh_sells:
            trow(ticker, strat, f"{pnl_pct:+.2f}%", f"${pnl_dollar:+.2f}", why,
                 widths=[8, 14, 7, 8, 28])
            total_pnl += pnl_dollar
        blank()
        row(f"{len(eh_sells)} sold after hours", f"total P&L  ${total_pnl:+.2f}")
        ftr()
    elif extended_hours:
        hdr("EXTENDED HOURS SELLS")
        blank(); row("No extended-hours sells this run."); blank()
        ftr()

    hdr("EXIT RUN SUMMARY")
    total_candidates = len(positions)
    row("Mode", run_mode_name)
    row("Candidates", str(total_candidates))
    row("Deferred/Skipped", f"already logged {stats['already_logged']}")
    row("Data skips", f"no price data {stats['no_data_skip']}")
    row("Sell attempts", f"{stats['attempted']} attempted  |  {stats['filled']} filled  |  "
                         f"{stats['partial']} partial  |  {stats['pending']} pending  |  {stats['failed']} failed")
    row("Holds", str(stats["holds"]))
    row("Logged exits", str(exits))
    ftr()

    hdr("STOP-LOSS BREACHES THIS RUN")
    if stop_breaches:
        for tk, frac in sorted(stop_breaches.items(), key=lambda kv: kv[1]):
            row(tk, f"{frac*100:+.2f}%  (threshold {EXIT_STOP_LOSS*100:+.2f}%)")
        row("Count", str(len(stop_breaches)))
    else:
        row("None")
    ftr()

    added_look = _append_stoploss_look_items(list(stoploss_look_items.values()), run_mode_name)
    row("Stop-loss look file", str(STOP_LOSS_LOOK_FILE))
    row("New investigations added", str(added_look))
    ftr()

    positions_after = enrich(client, get_positions(client))
    acct2 = get_account_safe(client)
    eq2 = float(acct2.equity)
    ca2 = float(acct2.cash)
    log_run(run_mode_name, rgm, eq2, ca2, 0, 0, exits, positions_after)
    # Keep daily markdown in sync for non-scan exit runs too.
    write_daily(date.today(), eq2, ca2, rgm, date.today().month, positions_after, [], [], [],
                preserve_existing_signals=True)
    if ab_test_active() or ab_load_registry().get("entries"):
        ab_write_dashboard(eq2, ca2, positions_after)


# =============================================================================
#  FULL SCAN
# =============================================================================

def run_scan(client, equity, cash, rgm, mode_name="scan"):
    today = date.today(); month = today.month; sc = SCHEDULE[month]
    reserve = equity * CASH_RESERVE_PCT; avail = max(0.0, cash - reserve)

    hdr("RUBBER BAND BOT v8  --  DAILY SCAN")
    row("Mode",     "PAPER" if PAPER_TRADING else "*** LIVE ***")
    row("Date",     str(today))
    row("Universe", UNIVERSE)
    row("Month",    f"{MN[month]}: {sc['p']} + {sc['s']} (display only — schedule not enforced)")
    row("Disabled", f"{', '.join(sorted(DISABLED_STRATEGIES))} (see DISABLED_STRATEGIES)")
    row("Regime",   rgm.upper())
    row("Exit",     f"midline / stop{EXIT_STOP_LOSS*100:.1f}% / {EXIT_DAYS_MAX}d max")
    ftr()

    hdr("ACCOUNT")
    row("Equity",    f"${equity:,.2f}")
    row("Cash",      f"${cash:,.2f}")
    row("Reserve",   f"${reserve:,.2f}  (always kept)")
    row("Available",     f"${avail:,.2f}  (for new trades)")
    row("Trade size", f"${equity*OFFSCHEDULE_SIZE_PCT:,.2f}  ({OFFSCHEDULE_SIZE_PCT*100:.0f}% per signal — all strategies equal)")
    ftr()

    positions = enrich(client, get_positions(client))
    entries_today = _count_buys_today()
    # Dynamic entry cap: cash slots + MAX_OPEN_POSITIONS concurrent holdings.
    max_trades = max(1, int(avail // MIN_TRADE_SIZE))
    if not ab_test_active() and MAX_OPEN_POSITIONS:
        max_trades = min(max_trades, max(0, MAX_OPEN_POSITIONS - len(positions)))

    if ab_test_active():
        reg = ab_load_registry()
        hdr("A/B CONCENTRATION TEST  (ACTIVE)")
        row("Period", f"{reg.get('started')} → {ab_test_end(reg.get('started'))}")
        row("Group A", f"wide — ~{AB_RATIO_A_TO_B}× B count, no fixed cap")
        row("Group B", f"conc — 1 per ~{AB_RATIO_A_TO_B}+1 signals, no fixed cap")
        row("Sizing", f"each group's 50% budget ÷ signals assigned that day")
        row("Review files", f"logs/ab_test/week_review.md · trades_sorted.csv")
        ftr()
    plan_mode_name = "morning" if mode_name == "morning_scan" else "evening"
    plan_file = _plan_file_for_mode(plan_mode_name)
    cached_plan = _load_plan(plan_file)
    live_open_sell_orders = _snapshot_open_sell_orders(client)
    plan_ok, plan_note = _plan_usable(
        cached_plan,
        plan_mode_name,
        rgm,
        month,
        positions=positions,
        open_sell_orders=live_open_sell_orders,
    )
    signals_cache_ok, signals_note = _plan_signals_cacheable(
        cached_plan, plan_mode_name, rgm, month)
    if not USE_TWO_PHASE_PLAN:
        plan_ok = False
        signals_cache_ok = False
        plan_note = "disabled (parity mode)"

    hdr(f"HOLDINGS  ({len(positions)} open)")
    if positions:
        if ab_test_active():
            trow("GRP","TICKER","STRATEGY","INVESTED","ENTRY","NOW","P&L%","P&L$",
                 widths=[4,7,14,9,7,7,6,7])
        else:
            trow("TICKER","STRATEGY","INVESTED","ENTRY","NOW","P&L%","P&L$",
                 widths=[7,14,9,7,7,6,7])
        div()
        for t, p in positions.items():
            if ab_test_active():
                trow(p.get("ab_group","?"), t, p.get("strategy","?"),
                     f"${p.get('dollar_amt',0):.2f}", f"${p['entry_price']:.2f}",
                     f"${p['current_price']:.2f}", f"{p['pnl_pct']:+.1f}%",
                     f"${p['pnl_dollar']:+.2f}", widths=[4,7,14,9,7,7,6,7])
            else:
                trow(t, p.get("strategy","?"),
                     f"${p.get('dollar_amt',0):.2f}", f"${p['entry_price']:.2f}",
                     f"${p['current_price']:.2f}", f"{p['pnl_pct']:+.1f}%",
                     f"${p['pnl_dollar']:+.2f}", widths=[7,14,9,7,7,6,7])
        blank()
        inv = sum(p.get("dollar_amt",0) for p in positions.values())
        pnl = sum(p.get("pnl_dollar",0) for p in positions.values())
        row("Total invested", f"${inv:,.2f}")
        row("Total open P&L", f"${pnl:+,.2f}")
        if ab_test_active():
            a_o, b_o = ab_open_counts(positions)
            row("By group", f"A: {a_o} open ${ab_deployed(positions,'A'):,.0f}  |  "
                f"B: {b_o} open ${ab_deployed(positions,'B'):,.0f}")
    else:
        blank(); row("No open positions."); blank()
    cap_note = "A/B test (no global cap)" if ab_test_active() else str(MAX_OPEN_POSITIONS)
    row(f"Buys today: {entries_today}  |  entry cap: {max_trades}"
        f"  |  max open: {cap_note}")
    ftr()

    hdr("PLAN CACHE")
    row("Mode", plan_mode_name)
    row("File", str(plan_file))
    row("Use cached plan", f"{'yes' if plan_ok else 'no'} ({plan_note})")
    if plan_ok:
        row("Cached exits", str(len(cached_plan.get("exit_plan", []))))
        row("Cached signals", str(len(cached_plan.get("signals", []))))
    if not plan_ok and signals_cache_ok:
        row("Use cached signals", f"yes ({signals_note}; positions refreshed live)")
        row("Cached signals", str(len(cached_plan.get("signals", []))))
    ftr()

    # Exit check on held positions
    exits = 0; sells_log = []
    scan_exit_stats = {
        "already_logged": 0,
        "no_data_skip": 0,
        "attempted": 0,
        "filled": 0,
        "partial": 0,
        "pending": 0,
        "failed": 0,
        "holds": 0,
    }
    scan_stop_breaches = {}
    scan_stoploss_look_items = {}

    # Load today's sells to prevent duplicate logging across multiple scan runs
    already_sold_today = set()
    if TX_FILE.exists():
        with open(TX_FILE, newline="") as _f:
            for _r in csv.DictReader(_f):
                if _r.get("action") == "SELL" and _r.get("date") == str(today):
                    sm = (_r.get("sell_method") or "").lower()
                    if "partial" in sm:
                        continue
                    already_sold_today.add(_r["ticker"])

    if positions:
        pos_data = {} if plan_ok else fetch_batch(list(positions.keys()), "positions")
        cached_exit_map = {}
        if plan_ok:
            cached_exit_map = {e.get("ticker"): e.get("why", "planned_exit")
                               for e in cached_plan.get("exit_plan", [])
                               if e.get("ticker")}
        hdr("EXIT EVALUATION  (EOD -- midline + stop + max-hold)")
        sorted_scan_pos = sorted(
            positions.items(),
            key=lambda kv: float(kv[1].get("pnl_pct", 0) or 0),
        )
        for ticker, pos in sorted_scan_pos:
            if ticker in already_sold_today and abs(float(pos.get("qty", 0) or 0)) <= 1e-6:
                scan_exit_stats["already_logged"] += 1
                continue
            entry_date = pos.get("entry_date", "")
            entered_today = (entry_date == str(today))
            pnl_frac = pos.get("pnl_pct", 0) / 100
            if pnl_frac <= EXIT_STOP_LOSS:
                scan_stop_breaches[ticker] = pnl_frac

            # ── Stop-loss: Alpaca unrealized P&L — no yfinance needed ─────
            if pnl_frac <= EXIT_STOP_LOSS:
                why = f"stop_loss ({pnl_frac*100:.1f}%)"
                row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%  ${pos['pnl_dollar']:+.2f}",
                    f"EXIT: {_trunc(why,20)}")
                scan_exit_stats["attempted"] += 1
                sell_res = do_sell(client, ticker, extended_hours=USE_EXTENDED_HOURS_SELL, urgency="urgent")
                if sell_res.get("ok") and sell_res.get("filled"):
                    if sell_res.get("exit_complete", True):
                        scan_exit_stats["filled"] += 1
                        exits += 1; cur = pos["current_price"]
                        cur = sell_res.get("price") if sell_res.get("price") is not None else cur
                        sold_dollars = sell_res.get("dollars") if sell_res.get("dollars") is not None else pos["market_value"]
                        dh = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days \
                             if pos.get("entry_date") else 0
                        log_tx("SELL", ticker, pos.get("strategy","?"), cur, sold_dollars,
                               rgm, float(get_account_safe(client).equity),
                               pos["pnl_pct"], pos["pnl_dollar"], dh, why,
                               sell_method=sell_res.get("sell_method",""),
                               cur_at_submit=sell_res.get("cur_at_submit"),
                               bid_at_submit=sell_res.get("bid_at_submit"),
                               limit_price_used=sell_res.get("limit_price_used"),
                               sell_latency_s=sell_res.get("sell_latency_s"),
                               fill_slippage_bps=sell_res.get("fill_slippage_bps"))
                        sells_log.append({"t": datetime.now().strftime("%H:%M"),
                                           "tk": ticker, "st": pos.get("strategy","?"),
                                           "px": cur, "why": why})
                        already_sold_today.add(ticker); del positions[ticker]
                    else:
                        scan_exit_stats["partial"] += 1
                        rem = sell_res.get("remaining_qty")
                        rem_txt = f"{float(rem):.4f} sh remain" if rem is not None else "residual shares remain"
                        row(ticker, f"PARTIAL SELL ({rem_txt}) — will retry this session")
                elif sell_res.get("pending"):
                    scan_exit_stats["pending"] += 1
                    uid = f"{ticker}|{entry_date or 'unknown'}"
                    scan_stoploss_look_items[uid] = {
                        "id": uid,
                        "ticker": ticker,
                        "strategy": pos.get("strategy", "?"),
                        "entry_date": entry_date or "unknown",
                        "pnl_frac": pnl_frac,
                        "root_cause": "After-hours limit still pending",
                        "explanation": "Stop breached but extended-hours order is limit-only and did not fill immediately; follow-up occurs next regular-hours run.",
                    }
                    row(ticker, "SELL pending (after-hours limit open)")
                else:
                    scan_exit_stats["failed"] += 1
                    uid = f"{ticker}|{entry_date or 'unknown'}"
                    scan_stoploss_look_items[uid] = {
                        "id": uid,
                        "ticker": ticker,
                        "strategy": pos.get("strategy", "?"),
                        "entry_date": entry_date or "unknown",
                        "pnl_frac": pnl_frac,
                        "root_cause": "Sell attempt failed",
                        "explanation": "Stop breached and an exit was attempted, but the broker/order flow returned a failure state.",
                    }
                    row(ticker, "SELL attempt failed (will retry next run)")
                continue

            # ── Max-hold: position data only — no yfinance needed ─────────
            if pos.get("entry_date"):
                try:
                    days = (datetime.today() -
                            datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days
                    if days >= EXIT_DAYS_MAX:
                        why = f"max_hold {days}d ({pnl_frac*100:+.1f}%)"
                        row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%  ${pos['pnl_dollar']:+.2f}",
                            f"EXIT: {_trunc(why,20)}")
                        scan_exit_stats["attempted"] += 1
                        sell_res = do_sell(client, ticker, extended_hours=USE_EXTENDED_HOURS_SELL, urgency="normal")
                        if sell_res.get("ok") and sell_res.get("filled"):
                            if sell_res.get("exit_complete", True):
                                scan_exit_stats["filled"] += 1
                                exits += 1; cur = pos["current_price"]
                                cur = sell_res.get("price") if sell_res.get("price") is not None else cur
                                sold_dollars = sell_res.get("dollars") if sell_res.get("dollars") is not None else pos["market_value"]
                                log_tx("SELL", ticker, pos.get("strategy","?"), cur, sold_dollars,
                                       rgm, float(get_account_safe(client).equity),
                                       pos["pnl_pct"], pos["pnl_dollar"], days, why,
                                       sell_method=sell_res.get("sell_method",""),
                                       cur_at_submit=sell_res.get("cur_at_submit"),
                                       bid_at_submit=sell_res.get("bid_at_submit"),
                                       limit_price_used=sell_res.get("limit_price_used"),
                                       sell_latency_s=sell_res.get("sell_latency_s"),
                                       fill_slippage_bps=sell_res.get("fill_slippage_bps"))
                                sells_log.append({"t": datetime.now().strftime("%H:%M"),
                                                   "tk": ticker, "st": pos.get("strategy","?"),
                                                   "px": cur, "why": why})
                                already_sold_today.add(ticker); del positions[ticker]
                            else:
                                scan_exit_stats["partial"] += 1
                                rem = sell_res.get("remaining_qty")
                                rem_txt = f"{float(rem):.4f} sh remain" if rem is not None else "residual shares remain"
                                row(ticker, f"PARTIAL SELL ({rem_txt}) — will retry this session")
                        elif sell_res.get("pending"):
                            scan_exit_stats["pending"] += 1
                            row(ticker, "SELL pending (after-hours limit open)")
                        else:
                            scan_exit_stats["failed"] += 1
                            row(ticker, "SELL attempt failed (will retry next run)")
                        continue
                except Exception: pass

            # ── Midline: needs price/MA data from yfinance (EOD only) ─────
            if plan_ok:
                ex = ticker in cached_exit_map
                why = cached_exit_map.get(ticker, "HOLD")
            else:
                if ticker not in pos_data:
                    scan_exit_stats["no_data_skip"] += 1
                    row(ticker, "no price data (stop/max-hold already checked)"); continue
                ex, why = check_exit(pos_data[ticker], pos, eod_only=True)
            row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%  ${pos['pnl_dollar']:+.2f}",
                f"EXIT: {_trunc(why,20)}" if ex else "HOLD")
            sell_res = do_sell(client, ticker, extended_hours=USE_EXTENDED_HOURS_SELL, urgency="low") if ex else {"ok": False, "filled": False}
            if ex and sell_res.get("ok") and sell_res.get("filled"):
                scan_exit_stats["attempted"] += 1
                if sell_res.get("exit_complete", True):
                    scan_exit_stats["filled"] += 1
                    exits += 1; cur = pos["current_price"]
                    cur = sell_res.get("price") if sell_res.get("price") is not None else cur
                    sold_dollars = sell_res.get("dollars") if sell_res.get("dollars") is not None else pos["market_value"]
                    dh = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days \
                         if pos.get("entry_date") else 0
                    log_tx("SELL", ticker, pos.get("strategy","?"), cur, sold_dollars,
                           rgm, float(get_account_safe(client).equity),
                           pos["pnl_pct"], pos["pnl_dollar"], dh, why,
                           sell_method=sell_res.get("sell_method",""),
                           cur_at_submit=sell_res.get("cur_at_submit"),
                           bid_at_submit=sell_res.get("bid_at_submit"),
                           limit_price_used=sell_res.get("limit_price_used"),
                           sell_latency_s=sell_res.get("sell_latency_s"),
                           fill_slippage_bps=sell_res.get("fill_slippage_bps"))
                    sells_log.append({"t": datetime.now().strftime("%H:%M"),
                                       "tk": ticker, "st": pos.get("strategy","?"),
                                       "px": cur, "why": why})
                    already_sold_today.add(ticker); del positions[ticker]
                else:
                    scan_exit_stats["partial"] += 1
                    rem = sell_res.get("remaining_qty")
                    rem_txt = f"{float(rem):.4f} sh remain" if rem is not None else "residual shares remain"
                    row(ticker, f"PARTIAL SELL ({rem_txt}) — will retry this session")
            elif ex and sell_res.get("pending"):
                scan_exit_stats["attempted"] += 1
                scan_exit_stats["pending"] += 1
                row(ticker, "SELL pending (after-hours limit open)")
            elif ex:
                scan_exit_stats["attempted"] += 1
                scan_exit_stats["failed"] += 1
                row(ticker, "SELL attempt failed (will retry next run)")
            else:
                scan_exit_stats["holds"] += 1
        ftr()
        hdr("EXIT EVAL SUMMARY")
        row("Exit eval",
            f"attempted {scan_exit_stats['attempted']} | filled {scan_exit_stats['filled']} | "
            f"partial {scan_exit_stats['partial']} | pending {scan_exit_stats['pending']} | failed {scan_exit_stats['failed']}")
        row("Other skips", f"already logged today {scan_exit_stats['already_logged']}  |  "
                           f"no price data {scan_exit_stats['no_data_skip']}  |  holds {scan_exit_stats['holds']}")
        if scan_stop_breaches:
            row("Stop-loss breaches", str(len(scan_stop_breaches)))
            for tk, frac in sorted(scan_stop_breaches.items(), key=lambda kv: kv[1]):
                row(tk, f"{frac*100:+.2f}%  (threshold {EXIT_STOP_LOSS*100:+.2f}%)")
        else:
            row("Stop-loss breaches", "none")
        added_look_scan = _append_stoploss_look_items(list(scan_stoploss_look_items.values()), "scan")
        row("Stop-loss look file", str(STOP_LOSS_LOOK_FILE))
        row("New investigations added", str(added_look_scan))
        ftr()

    # Full universe download and scan (or cached plan reuse)
    hdr("DATA DOWNLOAD")
    row(f"Universe: {UNIVERSE}  |  Alpaca primary / yfinance fallback")
    ftr()

    if plan_ok:
        all_data = {}
        scan = []
        all_sigs = list(cached_plan.get("signals", []))
        hdr("SIGNAL SCAN")
        row(f"Month: {MN[month]}  |  Regime: {rgm.upper()}")
        row(f"Primary: {sc['p']}  |  Secondary: {sc['s']} (display only — schedule not enforced)")
        row("Source", "cached prep plan")
        row("Universe scanned in prep", str(cached_plan.get("scan_universe_count", 0)))
        ftr()
    elif signals_cache_ok:
        all_data = {}
        scan = []
        all_sigs = list(cached_plan.get("signals", []))
        hdr("SIGNAL SCAN")
        row(f"Month: {MN[month]}  |  Regime: {rgm.upper()}")
        row(f"Primary: {sc['p']}  |  Secondary: {sc['s']} (display only — schedule not enforced)")
        row("Source", f"cached signals ({signals_note})")
        row("Universe scanned in prep", str(cached_plan.get("scan_universe_count", 0)))
        ftr()
    else:
        tickers  = get_live_tickers()
        scan     = [t for t in tickers if t not in positions]
        all_data = fetch_batch(scan, "universe")

        hdr("SIGNAL SCAN")
        row(f"Month: {MN[month]}  |  Regime: {rgm.upper()}")
        row(f"Primary: {sc['p']}  |  Secondary: {sc['s']} (display only — schedule not enforced)")
        row("Source", "live scan")
        ftr()
        all_sigs = []
        for ticker, df in all_data.items():
            for s in get_signals(ticker, df, month, rgm):
                s["month"] = month; s["regime"] = rgm
                all_sigs.append(s)

    # Defensive de-dupe: merged universes/data glitches should not double-submit
    # the same ticker+strategy signal in one scan run.
    deduped_sigs = []
    seen_sig_keys = set()
    for s in all_sigs:
        k = (s.get("ticker"), s.get("strategy"))
        if k in seen_sig_keys:
            continue
        seen_sig_keys.add(k)
        deduped_sigs.append(s)
    all_sigs = deduped_sigs

    hdr(f"SIGNALS FOUND  --  {len(all_sigs)}")
    if not all_sigs:
        blank(); row("No signals today."); blank()
        row(_trunc(sc["note"], W-4)); blank()
    else:
        trow("TICKER","STRATEGY","TIER","PRICE","RSI","VOL_Z","TRIGGER",
             widths=[7,14,5,7,5,6,20])
        div()
        for s in all_sigs:
            tier = "eq"  # schedule removed — all strategies equal weight
            trow(s["ticker"], s["strategy"], tier, f"${s['close']:.2f}",
                 f"{s.get('rsi',0):.1f}", f"{s.get('vol_z',0):.2f}",
                 s.get("trigger",""), widths=[7,14,5,7,5,6,20])
        blank()
    ftr()

    allow_entries = (
        mode_name in ("scan", "morning_scan")
        if not EVENING_ONLY_ENTRIES
        else mode_name == "scan"
    )

    # ── Deterministic sort only (no seasonal cash priority) ──────────────
    all_sigs.sort(key=lambda s: s["strategy"])

    if not allow_entries:
        hdr("ENTRY ORDERS")
        row("Skipped", "evening-only — buys at 3:50pm ET scan only")
        entries = 0; buys_log = []; unconfirmed_buys = 0; pending_buys = []
        ftr()
    else:
        already_held   = set(positions.keys())
        viable         = [s for s in all_sigs if s["ticker"] not in already_held]
        entries = 0; buys_log = []; unconfirmed_buys = 0; pending_buys = []
        cash = float(get_account_safe(client).cash); avail = max(0.0, cash - reserve)
        n_open = len(positions)

        if ab_test_active():
            half = equity * AB_TEST_EQUITY_SPLIT
            assigned = ab_assign_groups(viable)
            ab_log_scan(assigned, len(viable))
            a_open, b_open = ab_open_counts(positions)
            a_dep = ab_deployed(positions, "A")
            b_dep = ab_deployed(positions, "B")
            n_a_left = sum(1 for s in assigned if s.get("ab_group") == "A")
            n_b_left = sum(1 for s in assigned if s.get("ab_group") == "B")
            n_a_batch = n_a_left
            n_b_batch = n_b_left

            hdr("A/B TEST — ENTRY ORDERS")
            row("Viable signals", str(len(viable)))
            row("Split today", f"A={n_a_batch}  B={n_b_batch}  (target ~{AB_RATIO_A_TO_B}:1)")
            row("Open now", f"A={a_open}  B={b_open}  (live ratio {a_open}:{b_open})")
            row("Budget left", f"A=${max(0,half-a_dep):.0f}  B=${max(0,half-b_dep):.0f}  of ${half:.0f} each")
            for sig in assigned:
                ticker = sig["ticker"]; strategy = sig["strategy"]
                group = sig["ab_group"]
                batch_left = n_b_left if group == "B" else n_a_left
                dep = b_dep if group == "B" else a_dep
                da = ab_size_for_group(group, equity, batch_left, dep)
                skip = ""
                if avail <= 1.0:
                    skip = "reserve floor"
                elif dep + da > half + 1.0:
                    skip = f"{group} half budget"
                if not skip and da > avail:
                    skip = "not enough cash"
                if not skip and has_earnings_soon(ticker):
                    skip = f"earnings ≤{EARNINGS_SKIP_DAYS}d"
                if skip:
                    row(f"  SKIP [{group}] {ticker}  {strategy}", _trunc(skip, 22))
                    continue
                row(f"  ENTER [{group}] {ticker}  {strategy}", f"${da:.2f}")
                buy_res = do_buy(client, ticker, da, strategy,
                                 expected_price=sig["close"], fast_submit=True)
                if buy_res.get("ok"):
                    n_open += 1
                    avail -= da
                    if group == "B":
                        b_open += 1
                        b_dep += da
                        n_b_left = max(0, n_b_left - 1)
                    else:
                        a_open += 1
                        a_dep += da
                        n_a_left = max(0, n_a_left - 1)
                    if buy_res.get("filled"):
                        entries += 1
                        entries_today += 1
                        buy_price = buy_res.get("price") or sig["close"]
                        buy_dollars = buy_res.get("dollars") or da
                        log_tx("BUY", ticker, strategy, buy_price, buy_dollars, rgm,
                               float(get_account_safe(client).equity),
                               expected_price=sig["close"],
                               order_price=buy_res.get("order_price", sig["close"]),
                               execution_method=buy_res.get("execution_method", "buy_market"),
                               ab_group=group)
                        buys_log.append({"t": datetime.now().strftime("%H:%M"),
                                          "tk": ticker, "st": strategy,
                                          "px": round(buy_price, 2), "$": round(buy_dollars, 2),
                                          "grp": group})
                    else:
                        unconfirmed_buys += 1
                        pending_buys.append({
                            "ticker": ticker,
                            "strategy": strategy,
                            "dollars": da,
                            "expected_price": sig["close"],
                            "order_id": buy_res.get("order_id"),
                            "ab_group": group,
                        })
                        row(f"  BUY SUBMITTED [{group}] {ticker}",
                            "fill pending — batched confirmation after entries")
        else:
            # ── Equal-weight position sizing (schedule removed 2026-07-18) ─
            n_viable = len(viable)
            n_slots = min(n_viable, max_trades)
            hdr("ENTRY ORDERS")
            if n_slots <= 0:
                row("Skipped", f"no entry slots (max_trades={max_trades})")
            else:
                for sig in all_sigs:
                    ticker = sig["ticker"]; strategy = sig["strategy"]
                    skip = ""
                    if not entry_slot_ok(entries_today, max_trades):   skip = "entry cap"
                    elif MAX_OPEN_POSITIONS and n_open >= MAX_OPEN_POSITIONS:
                        skip = f"cap {MAX_OPEN_POSITIONS}"
                    elif avail <= 1.0:    skip = "reserve floor"
                    da = max(MIN_TRADE_SIZE,
                             min(equity * OFFSCHEDULE_SIZE_PCT, avail))
                    if not skip and da > avail: skip = "not enough cash"
                    if not skip and has_earnings_soon(ticker): skip = f"earnings ≤{EARNINGS_SKIP_DAYS}d"
                    if skip:
                        row(f"  SKIP [eq] {ticker}  {strategy}", _trunc(skip, 20))
                        continue
                    row(f"  ENTER [eq] {ticker}  {strategy}", f"${da:.2f}")
                    buy_res = do_buy(client, ticker, da, strategy, expected_price=sig["close"], fast_submit=True)
                    if buy_res.get("ok"):
                        n_open += 1
                        avail -= da
                        if buy_res.get("filled"):
                            entries += 1
                            entries_today += 1
                            buy_price = buy_res.get("price") if buy_res.get("price") is not None else sig["close"]
                            buy_dollars = buy_res.get("dollars") if buy_res.get("dollars") is not None else da
                            log_tx("BUY", ticker, strategy, buy_price, buy_dollars, rgm,
                                   float(get_account_safe(client).equity),
                                   expected_price=sig["close"],
                                   order_price=buy_res.get("order_price", sig["close"]),
                                   execution_method=buy_res.get("execution_method", "buy_market"))
                            buys_log.append({"t": datetime.now().strftime("%H:%M"),
                                             "tk": ticker, "st": strategy,
                                             "px": round(buy_price, 2), "$": round(buy_dollars, 2)})
                        else:
                            unconfirmed_buys += 1
                            pending_buys.append({
                                "ticker": ticker,
                                "strategy": strategy,
                                "dollars": da,
                                "expected_price": sig["close"],
                                "order_id": buy_res.get("order_id"),
                            })
                            row(f"  BUY SUBMITTED [eq] {ticker}",
                                "fill pending — batched confirmation after entries")
        if entries == 0 and not all_sigs: row("  No entries placed.")
        if pending_buys:
            batched = poll_pending_buys(client, pending_buys, rgm)
            entries += batched
            entries_today += batched
        ftr()

    # Place GTC stop-market orders for all open positions.
    # Wait 5s first so newly submitted market buys have time to fill and
    # appear in Alpaca positions before we try to attach stops to them.
    total_buy_submits = entries + unconfirmed_buys
    if total_buy_submits > 0:
        hdr("GTC STOP PLACEMENT")
        row(f"Waiting 5s for {total_buy_submits} buy submit(s) to settle...")
        ftr()
        time.sleep(5)
    place_all_stops(client)

    # Evening scan (~3:45pm ET): refresh stops to current price so overnight
    # protection isn't anchored to stale entry prices.
    try:
        from zoneinfo import ZoneInfo
        now_et = datetime.now(ZoneInfo("America/New_York"))
        if now_et.hour == 15:
            place_eod_stops(client)
    except Exception as e:
        log.warning(f"  EOD stop refresh check failed: {e}")

    acct2 = get_account_safe(client)
    eq2 = float(acct2.equity); ca2 = float(acct2.cash)
    pos2 = enrich(client, get_positions(client))

    hdr("SESSION SUMMARY")
    row("Regime",   rgm.upper())
    row("Universe", UNIVERSE)
    row("Strategy", f"{sc['p']} + {sc['s']} (display only — schedule not enforced)")
    row("Scanned",  str(len(all_data)))
    row("Signals",  str(len(all_sigs)))
    row("Entries",  str(entries))
    row("Buy submits", f"{entries} confirmed  |  {unconfirmed_buys} unconfirmed")
    row("Exits",    str(exits))
    row("Open pos", str(len(pos2)))
    row("Equity",   f"${eq2:,.2f}")
    row("Cash",     f"${ca2:,.2f}")
    ftr()

    scan_run_mode = "scan_morning" if mode_name == "morning_scan" else "scan_evening"
    log_run(scan_run_mode, rgm, eq2, ca2, len(all_sigs), entries, exits, pos2,
            cache_hit=(plan_ok or signals_cache_ok))
    write_daily(today, eq2, ca2, rgm, month, pos2, all_sigs, buys_log, sells_log)
    write_dashboard()
    if ab_test_active() or ab_load_registry().get("entries"):
        ab_write_dashboard(eq2, ca2, pos2)


# =============================================================================
#  ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    _run_started_at = time.time()

    mode = os.getenv("BOT_MODE", "").strip().lower()
    if not mode or mode == "auto":
        mode = detect_mode()
    else:
        log.info(f"Mode from BOT_MODE env: {mode}")

    log.info(f"Mode: {mode}")

    client = TradingClient(API_KEY, API_SECRET, paper=PAPER_TRADING)
    # Note: TradingClient has no timeout= kwarg — see socket.setdefaulttimeout(45) above.
    acct   = get_account_safe(client)
    equity = float(acct.equity)
    cash   = float(acct.cash)

    spy_raw = fetch_stock("SPY")
    spy_df  = add_ind(spy_raw) if spy_raw is not None else None
    rgm     = regime(spy_df)

    hdr(); row("RUBBER BAND BOT  v8"); div()
    row("Mode",     mode.upper())
    row("Time",     datetime.utcnow().strftime("%H:%M UTC"))
    row("Regime",   rgm.upper())
    row("Universe", UNIVERSE)
    row("Equity",   f"${equity:,.2f}")
    ftr()

    if mode == "morning_prep":
        run_prep(client, equity, cash, rgm, mode_name="morning")
    elif mode == "evening_prep":
        run_prep(client, equity, cash, rgm, mode_name="evening")
    elif mode == "morning_scan":
        run_scan(client, equity, cash, rgm, mode_name="morning_scan")
    elif mode == "scan":
        run_scan(client, equity, cash, rgm, mode_name=mode)
    elif mode == "exits":
        run_exits(client, equity, cash, rgm)
    elif mode == "ext_exits":
        # Post-market exits (4pm–8pm ET): extended hours limit sells only.
        # No GTC stop orders can be placed in extended hours.
        # No new buys — exits only (stop-loss, time-stop, midline).
        run_exits(client, equity, cash, rgm, extended_hours=True)
    elif mode == "weekly":
        # Weekly mode prints a compact weekly snapshot and writes weekly markdown.
        write_weekly(client, equity, cash)
    else:
        run_summary(client, equity, cash, rgm)
