# -*- coding: utf-8 -*-
"""
RUBBER BAND BOT v7
==================
Calendar-aware, regime-switching, multi-strategy trading bot.
Runs on GitHub Actions triggered by cron-job.org.

CHANGES FROM v6 (sim-validated across 2yr/3yr/5yr/7yr, 900 stocks):
  - Exit simplified: midline only (price > 20-day MA)
    Removed momentum decay layer + RSI requirement
    Midline alone was the most consistent exit across every timeframe
  - Max hold reduced: 14d -> 5d (deep sweep winner, OOS +113.6%)
  - Stop loss tightened: -3% -> -2% (deep sweep: tighter = better OOS)
    Reasoning: 2x slippage floor means -5% stop = -10% worst-case loss.
    Cutting to -2% (floor -4%) caps losses and recycles cash faster.
  - Position sizing: 20% seasonal / 12% off-schedule (tiered by strategy)
  - Removed MAX_OPEN_POSITIONS cap: cash availability is the real constraint

  ENTRY STRATEGIES (bake-off validated, 5yr 900 stocks):
    KEPT:    RubberBand  (51.7% win, 0.84 Sharpe -- best Sharpe)
             52wkLow     (53.4% win, 0.60 Sharpe)
             MomReversal (54.4% win, 0.47 Sharpe, lowest drawdown)
    ADDED:   GapDown     (53.9% win, 0.51 Sharpe -- panic-to-recovery)
             VolumeSpike (58.5% win, consistent all regimes -- institutional)
             Pullback50  (58.2% win -- uptrend dip-buy)
    REMOVED: GoldenCross (negative Sharpe, lost money)

WHAT RUNS WHEN (auto-detected by time, no flags needed):
  9:35am ET  -> exits-only check
  4:15pm ET  -> full daily scan + entries + daily log
  Weekend    -> weekly summary, no trading
  Other      -> status summary, no trading

LOGS committed back to repo after every run:
  logs/daily/YYYY-MM-DD.md
  logs/weekly/YYYY-WNN.md
  logs/transactions.csv
  logs/runs.csv

GITHUB SECRETS required:
  ALPACA_API_KEY
  ALPACA_SECRET_KEY
"""

import os, json, time, logging, csv
from datetime import datetime, timedelta, date
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

from alpaca.trading.client   import TradingClient
from alpaca.trading.requests import (MarketOrderRequest, GetOrdersRequest,
                                      StopOrderRequest)
from alpaca.trading.enums    import (OrderSide, TimeInForce, QueryOrderStatus,
                                     OrderType)
from alpaca.data.historical  import StockHistoricalDataClient
from alpaca.data.requests    import StockBarsRequest
from alpaca.data.timeframe   import TimeFrame


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
#   Off-schedule signals (other 4 strategies firing off-schedule): 12%
#
#   Sweep result (7yr, 900 stocks):
#     20%/12% wins (+394.7% total, +109.8% OOS, 28.1% dd)
#     Consistent winner across 3yr and 7yr runs.
#
#   Weak-month reduction (Feb/Mar/Sep → 5%) was tested and rejected:
#     Reduces total return by ~52pp and OOS by ~18pp vs no reduction.
#     Even underperforming months generate enough profitable trades at
#     full sizing to outweigh the savings from cutting size.
SEASONAL_SIZE_PCT    = 0.20   # primary + secondary scheduled strategies
OFFSCHEDULE_SIZE_PCT = 0.12   # all other strategies
CASH_RESERVE_PCT     = 0.10   # sim-validated at 10%

# ---- Exit rules (v7 -- deep param sweep validated, 7yr 899 stocks) ----------
# Midline only: price crosses above 20-day moving average
# Deep sweep (15 combos: 5 stops x 3 holds) winner by OOS return:
#   -2% stop / 5d hold  →  OOS +113.6%,  OOS DD 11.6%,  OOS win 55.0%
# Tighter stop (-2% floor -4%) cuts losses fast, recycles cash sooner.
# Every step wider (-2.5 → -3 → -4 → -5%) reduced OOS return despite
# higher win rate, because the 2x slippage floor magnifies wide-stop losses.
EXIT_DAYS_MAX      = 5
EXIT_STOP_LOSS     = -0.02

# ---- Daily entry cap ---------------------------------------------------------
# Cap sweep (5yr, 900 stocks): 5/day = +215% vs 3/day = +187% (+28pp)
# PDT diagnostic showed 0 same-day round trips so PDT rule doesn't bind.
# 5/day captures 96% of "no cap" return while staying realistic.
MAX_DAY_TRADES   = 5

# ---- Data quality ------------------------------------------------------------
MIN_STOCK_PRICE  = 5.0
MIN_HISTORY_DAYS = 220

# ---- Paths -------------------------------------------------------------------
LOG_DIR    = Path("logs")
DAILY_DIR  = LOG_DIR / "daily"
WEEKLY_DIR = LOG_DIR / "weekly"
TX_FILE    = LOG_DIR / "transactions.csv"
RUNS_FILE  = LOG_DIR / "runs.csv"
PDT_FILE   = LOG_DIR / "pdt.json"

for d in [LOG_DIR, DAILY_DIR, WEEKLY_DIR]:
    d.mkdir(parents=True, exist_ok=True)

W = 68   # display box inner width


# =============================================================================
#  CALENDAR STRATEGY SCHEDULE  (v7 bake-off validated)
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
    3:  {"p": "52wkLow",     "s": "MomReversal",  "note": "Mar: 52wkLow+1.85% 68%win"},
    4:  {"p": "RubberBand",  "s": "Pullback50",   "note": "Apr: RubberBand + Pullback50 (58.2% win)"},
    5:  {"p": "RubberBand",  "s": "52wkLow",      "note": "May: RubberBand+1.93% 58%win"},
    6:  {"p": "52wkLow",     "s": "VolumeSpike",  "note": "Jun: 52wkLow + VolumeSpike"},
    7:  {"p": "52wkLow",     "s": "Pullback50",   "note": "Jul: 52wkLow + Pullback50 (bull dip-buy)"},
    8:  {"p": "RubberBand",  "s": "52wkLow",      "note": "Aug: RubberBand+4.72% 70%win BEST MONTH"},
    9:  {"p": "GapDown",     "s": "VolumeSpike",  "note": "Sep: GapDown replaces GoldenCross + VolSpike"},
    10: {"p": "RubberBand",  "s": "GapDown",      "note": "Oct: RubberBand + GapDown (53.9% win)"},
    11: {"p": "RubberBand",  "s": "MomReversal",  "note": "Nov: RubberBand+4.77% 86%WIN RATE"},
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
log = logging.getLogger("RBv7")


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


# =============================================================================
#  UNIVERSE
# =============================================================================

def get_live_tickers():
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
            log.error(f"FATAL S&P 500: {e}"); raise SystemExit(1)

    if UNIVERSE in ("midcap", "both"):
        try:
            mid400 = pd.read_html(
                "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies",
                storage_options=headers)[0]["Symbol"].tolist()
            log.info(f"  MidCap 400: {len(mid400)}")
        except Exception as e:
            log.error(f"FATAL MidCap 400: {e}"); raise SystemExit(1)

    combined = list(dict.fromkeys(sp500 + mid400))
    cleaned  = [t.replace(".", "-") for t in combined]
    log.info(f"  Total: {len(cleaned)} tickers")
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
    return df

def fetch_batch(tickers, label=""):
    data = {}
    for i in range(0, len(tickers), 40):
        for t in tickers[i:i+40]:
            df = fetch_stock(t)
            if df is not None: data[t] = add_ind(df)
        log.info(f"  [{label}] {min(i+40,len(tickers))}/{len(tickers)} ({len(data)} valid)")
        time.sleep(1.0)
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
#  ENTRY SIGNALS  (v7 -- bake-off validated)
#
#  KEPT (passed bake-off):
#    RubberBand   -- 51.7% win, 0.84 Sharpe (best Sharpe of all)
#    52wkLow      -- 53.4% win, 0.60 Sharpe, 83.6% return
#    MomReversal  -- 54.4% win, 0.47 Sharpe, 129% return, lowest DD
#
#  ADDED (new, bake-off validated):
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

def get_signals(ticker, df, month, rgm):
    """Check ALL 6 strategies every day.
    Signals from the monthly scheduled pair are tagged seasonal=True and
    get entry priority when cash is tight (sorted first).
    Seasonal signals get SEASONAL_SIZE_PCT; all others get OFFSCHEDULE_SIZE_PCT.
    """
    sc = SCHEDULE[month]
    seasonal_set = {sc["p"], sc["s"]}
    if rgm == "bear":
        seasonal_set = {"52wkLow", "MomReversal"}  # bear override
    prm = BULL_P if rgm == "bull" else CORR_P if rgm == "correction" else BEAR_P

    all_strategies = ["RubberBand", "52wkLow", "MomReversal",
                      "GapDown", "VolumeSpike", "Pullback50"]
    sigs = []
    for name in all_strategies:
        s = (_rb(ticker, df, prm) if name == "RubberBand"  else
             _52(ticker, df)      if name == "52wkLow"     else
             _mr(ticker, df)      if name == "MomReversal" else
             _gd(ticker, df)      if name == "GapDown"     else
             _vs(ticker, df)      if name == "VolumeSpike" else
             _pb(ticker, df)      if name == "Pullback50"  else None)
        if s:
            s["seasonal"] = (name in seasonal_set)
            sigs.append(s)
    # Seasonal signals first, then alphabetical within each tier
    sigs.sort(key=lambda x: (not x["seasonal"], x["strategy"]))
    return sigs


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

def check_exit(df, pos):
    try:
        c_now  = float(df["Close"].iloc[-1])
        mid    = float(df["BBM"].iloc[-1])
        pnl    = pos.get("pnl_pct", 0) / 100

        if pd.isna(mid):
            return False, ""

        # Hard stops first -- override everything
        if pnl <= EXIT_STOP_LOSS:
            return True, f"stop_loss ({pnl*100:.1f}%)"

        if pos.get("entry_date"):
            try:
                days = (datetime.today() -
                        datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days
                if days >= EXIT_DAYS_MAX:
                    return True, f"max_hold {days}d ({pnl*100:+.1f}%)"
            except Exception: pass

        # Midline exit: price recovered above 20-day MA
        if c_now > mid:
            return True, f"midline ({pnl*100:+.1f}%)"

    except Exception: pass
    return False, ""


# =============================================================================
#  POSITIONS
# =============================================================================

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
        for o in sorted(orders, key=lambda x: x.submitted_at or datetime.min):
            sym = o.symbol
            if sym in positions and sym not in seen:
                seen.add(sym)
                if o.filled_at: positions[sym]["entry_date"] = str(o.filled_at.date())
                if o.client_order_id and "|" in o.client_order_id:
                    positions[sym]["strategy"] = o.client_order_id.split("|")[0]
    except Exception as e: log.debug(f"enrich failed: {e}")
    return positions


# =============================================================================
#  PDT
# =============================================================================

def load_pdt(): return json.load(open(PDT_FILE)) if PDT_FILE.exists() else []
def save_pdt(l): json.dump(l, open(PDT_FILE, "w"))

def pdt_n(l):
    c = date.today() - timedelta(days=7)
    return sum(1 for d in l if datetime.strptime(d, "%Y-%m-%d").date() >= c)

def pdt_ok(l):
    n = pdt_n(l)
    if n >= MAX_DAY_TRADES: log.warning(f"PDT {n}/{MAX_DAY_TRADES}"); return False
    return True


# =============================================================================
#  ORDERS
# =============================================================================

def do_buy(client, ticker, dollars, strategy):
    try:
        cid = f"{strategy}|{date.today()}"[:48]
        o = client.submit_order(MarketOrderRequest(
            symbol=ticker, notional=round(dollars, 2),
            side=OrderSide.BUY, time_in_force=TimeInForce.DAY,
            client_order_id=cid))
        log.info(f"  BUY  {ticker}  ${dollars:.2f}  [{strategy}]  id={o.id}")
        return True
    except Exception as e:
        log.error(f"  BUY FAILED {ticker}: {e}"); return False

def cancel_stop_orders(client, ticker):
    """Cancel any open GTC stop-sell orders for a ticker.
    Called before a software-triggered exit so we don't double-sell."""
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, symbols=[ticker])
        for o in client.get_orders(req):
            if (getattr(o, "order_type", None) == OrderType.STOP
                    and o.side == OrderSide.SELL):
                client.cancel_order_by_id(str(o.id))
                log.info(f"  STOP cancelled {ticker}  id={o.id}")
    except Exception as e:
        log.warning(f"  STOP cancel failed {ticker}: {e}")


def ensure_stop(client, ticker, entry_price, qty):
    """Place a GTC stop-market sell at entry_price × (1 + EXIT_STOP_LOSS).
    Skipped if a stop order already exists.  Safe to call repeatedly."""
    stop_price = round(entry_price * (1.0 + EXIT_STOP_LOSS), 2)
    try:
        # Check if a stop-sell already exists for this ticker
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, symbols=[ticker])
        for o in client.get_orders(req):
            if (getattr(o, "order_type", None) == OrderType.STOP
                    and o.side == OrderSide.SELL):
                log.info(f"  STOP already live {ticker} @ ${o.stop_price}")
                return True
        # Place new GTC stop-market order
        o = client.submit_order(StopOrderRequest(
            symbol=ticker,
            qty=str(round(qty, 9)),
            side=OrderSide.SELL,
            time_in_force=TimeInForce.GTC,
            stop_price=stop_price,
        ))
        log.info(f"  STOP placed {ticker}  qty={qty:.4f}  "
                 f"stop=${stop_price:.2f}  id={o.id}")
        return True
    except Exception as e:
        log.warning(f"  STOP placement failed {ticker}: {e}")
        return False


def do_sell(client, ticker):
    cancel_stop_orders(client, ticker)   # remove server-side stop before closing
    try:
        client.close_position(ticker)
        log.info(f"  SELL {ticker} closed"); return True
    except Exception as e:
        # Position may already be gone (stop fired at Alpaca) — not an error
        log.warning(f"  SELL {ticker}: {e}"); return False


# =============================================================================
#  TRANSACTION LOG
# =============================================================================

TX_F = ["timestamp","date","action","ticker","strategy","price","dollar_amount",
        "pnl_pct","pnl_dollar","hold_days","exit_reason","regime","equity_after"]

def log_tx(action, ticker, strategy, price, dollars, rgm, equity,
           pnl_pct=0, pnl_dollar=0, hold_days=0, exit_reason=""):
    init = not TX_FILE.exists()
    with open(TX_FILE, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=TX_F)
        if init: w.writeheader()
        w.writerow({"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "date": str(date.today()), "action": action, "ticker": ticker,
                    "strategy": strategy, "price": round(price, 2),
                    "dollar_amount": round(dollars, 2), "pnl_pct": round(pnl_pct, 2),
                    "pnl_dollar": round(pnl_dollar, 2), "hold_days": hold_days,
                    "exit_reason": exit_reason, "regime": rgm,
                    "equity_after": round(equity, 2)})

RUN_F = ["timestamp","mode","regime","equity","cash","signals","entries",
         "exits","open_positions","tickers","universe"]

def log_run(mode, rgm, equity, cash, signals, entries, exits, positions):
    init = not RUNS_FILE.exists()
    with open(RUNS_FILE, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=RUN_F)
        if init: w.writeheader()
        w.writerow({"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "mode": mode, "regime": rgm, "equity": round(equity, 2),
                    "cash": round(cash, 2), "signals": signals, "entries": entries,
                    "exits": exits, "open_positions": len(positions),
                    "tickers": "|".join(positions.keys()), "universe": UNIVERSE})


# =============================================================================
#  DAILY LOG
# =============================================================================

def write_daily(today, equity, cash, rgm, month, positions, signals, buys, sells):
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
         f"| Exit mode | midline / stop{EXIT_STOP_LOSS*100:.0f}% / {EXIT_DAYS_MAX}d max |",
         f"| Strategies | {sc['p']} + {sc['s']} |", "",
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
    if buys or sells:
        L += ["| Time | Action | Ticker | Strategy | Price | Amount | Note |",
              "|------|--------|--------|----------|-------|--------|------|"]
        for b in buys:
            L.append(f"| {b['t']} | BUY  | {b['tk']} | {b['st']} | ${b['px']:.2f} | ${b['$']:.2f} | -- |")
        for s in sells:
            L.append(f"| {s['t']} | SELL | {s['tk']} | {s['st']} | ${s['px']:.2f} | -- | {s['why']} |")
    else:
        L.append("_No trades today._")
    L += ["", "## Signals"]
    if signals:
        L += ["| Ticker | Strategy | Price | RSI | Vol Z | Trigger |",
              "|--------|----------|-------|-----|-------|---------|"]
        for s in signals:
            L.append(f"| {s['ticker']} | {s['strategy']} | ${s['close']:.2f} "
                     f"| {s.get('rsi',0):.1f} | {s.get('vol_z',0):.2f} | {s.get('trigger','')} |")
    else:
        L.append("_No signals today._")
    L += ["", "---", f"_RBv7 {datetime.now().strftime('%H:%M UTC')}_"]
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

    hdr(f"WEEKLY SUMMARY  Week {wk} / {today.year}")
    row("Equity",          f"${equity:,.2f}")
    row("Cash",            f"${cash:,.2f}")
    row("Total invested",  f"${invested:,.2f}")
    row("Open P&L",        f"${open_pnl:+,.2f}")
    row("Realised P&L",    f"${real_pnl:+,.2f}")
    row("Trades this week",f"{len(buys)} buys  {len(sells)} sells")
    ftr()

    # ── Year-by-year performance ──────────────────────────────────────────────
    yr_rows = year_by_year_from_log()
    if yr_rows:
        hdr("YEAR-BY-YEAR PERFORMANCE")
        trow("YEAR","START","END","RETURN","TRADES","WIN%","",
             widths=[6,11,11,9,8,7,5])
        div()
        for r in yr_rows:
            flag = "✓" if r["profitable"] else "✗"
            trow(r["year"],
                 f"${r['start_eq']:,.0f}", f"${r['end_eq']:,.0f}",
                 f"{r['ret_pct']:+.1f}%",
                 str(r["n_trades"]),
                 f"{r['win_rate']:.1f}%",
                 flag,
                 widths=[6,11,11,9,8,7,5])
        blank()
        profitable_n = sum(1 for r in yr_rows if r["profitable"])
        best  = max(yr_rows, key=lambda r: r["ret_pct"])
        worst = min(yr_rows, key=lambda r: r["ret_pct"])
        row("Profitable years", f"{profitable_n}/{len(yr_rows)}  "
            f"({profitable_n/len(yr_rows)*100:.0f}%)")
        row("Best  year", f"{best['year']}  ({best['ret_pct']:+.1f}%)")
        row("Worst year", f"{worst['year']}  ({worst['ret_pct']:+.1f}%)")
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
          f"_RBv7 {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}_"]
    fname.write_text("\n".join(L), encoding="utf-8")
    log.info(f"  Weekly summary -> {fname}")


# =============================================================================
#  TIME AUTO-DETECTION
# =============================================================================

def detect_mode():
    now = datetime.utcnow(); h = now.hour; dow = now.weekday()
    if dow >= 5: return "weekly"
    if dow == 4 and h >= 21: return "weekly"
    if 13 <= h < 14: return "exits"
    if 20 <= h < 22: return "scan"
    return "summary"


# =============================================================================
#  STATUS SUMMARY
# =============================================================================

def run_summary(client, equity, cash, rgm):
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

    hdr("EXIT LOGIC ACTIVE  (v7)")
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
#  EXITS RUN
# =============================================================================

def run_exits(client, equity, cash, rgm):
    positions = enrich(client, get_positions(client))
    if not positions:
        hdr("MORNING CHECK"); blank(); row("No open positions."); blank(); ftr()
        log_run("exits", rgm, equity, cash, 0, 0, 0, {}); return

    pos_data = fetch_batch(list(positions.keys()), "positions")
    exits = 0
    exited = set()
    hdr("EXIT CHECK")
    row("Exit logic", f"midline / stop{EXIT_STOP_LOSS*100:.0f}% / {EXIT_DAYS_MAX}d max")
    div()
    for ticker, pos in positions.items():
        if ticker not in pos_data: row(ticker, "no data"); continue
        ex, why = check_exit(pos_data[ticker], pos)
        row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%  ${pos['pnl_dollar']:+.2f}",
            f"EXIT: {_trunc(why,22)}" if ex else "HOLD")
        if ex and do_sell(client, ticker):
            exits += 1
            exited.add(ticker)
            cur = pos["current_price"]
            dh  = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days \
                  if pos.get("entry_date") else 0
            log_tx("SELL", ticker, pos.get("strategy","?"), cur, pos["market_value"],
                   rgm, float(client.get_account().equity),
                   pos["pnl_pct"], pos["pnl_dollar"], dh, why)
    ftr()

    # ── Ensure every held position has a server-side stop order ──────────────
    # Runs at 9:35am after market open so fill prices are confirmed.
    # Protects against bot outages -- stop lives at Alpaca even if bot is down.
    hdr("STOP ORDERS")
    row(f"Checking broker-side stop @ entry × {1+EXIT_STOP_LOSS:.0%}")
    div()
    for ticker, pos in positions.items():
        if ticker in exited: continue
        ep  = pos.get("entry_price", 0)
        qty = pos.get("qty", 0)
        if ep > 0 and qty > 0:
            ensure_stop(client, ticker, ep, qty)
            row(ticker, f"stop @ ${ep*(1+EXIT_STOP_LOSS):.2f}  qty={qty:.4f}")
        else:
            row(ticker, "skip (no entry price)")
    ftr()

    log_run("exits", rgm, equity, cash, 0, 0, exits, positions)


# =============================================================================
#  FULL SCAN
# =============================================================================

def run_scan(client, equity, cash, rgm):
    today = date.today(); month = today.month; sc = SCHEDULE[month]
    reserve = equity * CASH_RESERVE_PCT; avail = max(0.0, cash - reserve)

    hdr("RUBBER BAND BOT v7  --  DAILY SCAN")
    row("Mode",     "PAPER" if PAPER_TRADING else "*** LIVE ***")
    row("Date",     str(today))
    row("Universe", UNIVERSE)
    row("Month",    f"{MN[month]}: {sc['p']} + {sc['s']}")
    row("Regime",   rgm.upper())
    row("Exit",     f"midline / stop{EXIT_STOP_LOSS*100:.0f}% / {EXIT_DAYS_MAX}d max")
    ftr()

    hdr("ACCOUNT")
    row("Equity",    f"${equity:,.2f}")
    row("Cash",      f"${cash:,.2f}")
    row("Reserve",   f"${reserve:,.2f}  (always kept)")
    row("Available",     f"${avail:,.2f}  (for new trades)")
    row("Seasonal trade",  f"${equity*SEASONAL_SIZE_PCT:,.2f}  ({SEASONAL_SIZE_PCT*100:.0f}% -- scheduled strategies)")
    row("Off-sched trade", f"${equity*OFFSCHEDULE_SIZE_PCT:,.2f}  ({OFFSCHEDULE_SIZE_PCT*100:.0f}% -- other strategies)")
    ftr()

    positions = enrich(client, get_positions(client)); pdt = load_pdt()

    hdr(f"HOLDINGS  ({len(positions)} open)")
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
        inv = sum(p.get("dollar_amt",0) for p in positions.values())
        pnl = sum(p.get("pnl_dollar",0) for p in positions.values())
        row("Total invested", f"${inv:,.2f}")
        row("Total open P&L", f"${pnl:+,.2f}")
    else:
        blank(); row("No open positions."); blank()
    row(f"PDT used: {pdt_n(pdt)}/{MAX_DAY_TRADES}")
    ftr()

    # Exit check on held positions
    exits = 0; sells_log = []
    if positions:
        pos_data = fetch_batch(list(positions.keys()), "positions")
        hdr("EXIT EVALUATION")
        for ticker, pos in list(positions.items()):
            if ticker not in pos_data: row(ticker, "no data"); continue
            ex, why = check_exit(pos_data[ticker], pos)
            row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%  ${pos['pnl_dollar']:+.2f}",
                f"EXIT: {_trunc(why,20)}" if ex else "HOLD")
            if ex and do_sell(client, ticker):
                exits += 1; cur = pos["current_price"]
                dh = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days \
                     if pos.get("entry_date") else 0
                log_tx("SELL", ticker, pos.get("strategy","?"), cur, pos["market_value"],
                       rgm, float(client.get_account().equity),
                       pos["pnl_pct"], pos["pnl_dollar"], dh, why)
                sells_log.append({"t": datetime.now().strftime("%H:%M"),
                                   "tk": ticker, "st": pos.get("strategy","?"),
                                   "px": cur, "why": why})
                del positions[ticker]
        ftr()

    # Full universe download and scan
    hdr("DATA DOWNLOAD")
    row(f"Universe: {UNIVERSE}  |  Alpaca primary / yfinance fallback")
    ftr()
    tickers  = get_live_tickers()
    scan     = [t for t in tickers if t not in positions]
    all_data = fetch_batch(scan, "universe")

    hdr("SIGNAL SCAN")
    row(f"Month: {MN[month]}  |  Regime: {rgm.upper()}")
    row(f"Primary: {sc['p']}  |  Secondary: {sc['s']}")
    ftr()
    all_sigs = []
    for ticker, df in all_data.items():
        for s in get_signals(ticker, df, month, rgm):
            s["month"] = month; s["regime"] = rgm
            all_sigs.append(s)

    hdr(f"SIGNALS FOUND  --  {len(all_sigs)}")
    if not all_sigs:
        blank(); row("No signals today."); blank()
        row(_trunc(sc["note"], W-4)); blank()
    else:
        trow("TICKER","STRATEGY","TIER","PRICE","RSI","VOL_Z","TRIGGER",
             widths=[7,14,5,7,5,6,20])
        div()
        for s in all_sigs:
            tier = "SEAS" if s.get("seasonal") else "off"
            trow(s["ticker"], s["strategy"], tier, f"${s['close']:.2f}",
                 f"{s.get('rsi',0):.1f}", f"{s.get('vol_z',0):.2f}",
                 s.get("trigger",""), widths=[7,14,5,7,5,6,20])
        blank()
    ftr()

    # Entries
    hdr("ENTRY ORDERS")
    cash = float(client.get_account().cash); avail = max(0.0, cash - reserve)
    entries = 0; buys_log = []
    for sig in all_sigs:
        ticker = sig["ticker"]; strategy = sig["strategy"]
        is_seasonal = sig.get("seasonal", False)
        lp = get_positions(client)
        skip = ""
        if not pdt_ok(pdt):   skip = "PDT limit"
        elif avail <= 1.0:    skip = "reserve floor"
        da = equity * (SEASONAL_SIZE_PCT if is_seasonal else OFFSCHEDULE_SIZE_PCT)
        if not skip and da > avail: skip = "not enough cash"
        tier = "S" if is_seasonal else "o"
        if skip:
            row(f"  SKIP [{tier}] {ticker}  {strategy}", _trunc(skip, 20)); continue
        row(f"  ENTER [{tier}] {ticker}  {strategy}", f"${da:.2f}")
        if do_buy(client, ticker, da, strategy):
            entries += 1; avail -= da
            log_tx("BUY", ticker, strategy, sig["close"], da, rgm,
                   float(client.get_account().equity))
            buys_log.append({"t": datetime.now().strftime("%H:%M"),
                              "tk": ticker, "st": strategy,
                              "px": sig["close"], "$": da})
    if entries == 0 and not all_sigs: row("  No entries placed.")
    ftr()

    # ── Ensure stop orders on all open positions ──────────────────────────────
    # Covers both pre-existing holds and any buys that may have already filled.
    # New buys placed after market close queue for next morning's open; their
    # stops will be confirmed at the 9:35am run once fill price is known.
    hdr("STOP ORDERS")
    row(f"Broker-side GTC stop @ entry × {1+EXIT_STOP_LOSS:.0%}  (Alpaca-hosted)")
    div()
    pos_now = enrich(client, get_positions(client))
    for ticker, pos in pos_now.items():
        ep  = pos.get("entry_price", 0)
        qty = pos.get("qty", 0)
        if ep > 0 and qty > 0:
            ensure_stop(client, ticker, ep, qty)
            row(ticker, f"stop @ ${ep*(1+EXIT_STOP_LOSS):.2f}  qty={qty:.4f}")
        else:
            row(ticker, "pending fill — stop set at 9:35am check")
    if not pos_now:
        blank(); row("No open positions to protect."); blank()
    ftr()

    save_pdt(pdt)
    acct2 = client.get_account()
    eq2 = float(acct2.equity); ca2 = float(acct2.cash)
    pos2 = enrich(client, get_positions(client))

    hdr("SESSION SUMMARY")
    row("Regime",   rgm.upper())
    row("Universe", UNIVERSE)
    row("Strategy", f"{sc['p']} + {sc['s']}")
    row("Scanned",  str(len(all_data)))
    row("Signals",  str(len(all_sigs)))
    row("Entries",  str(entries))
    row("Exits",    str(exits))
    row("Open pos", str(len(pos2)))
    row("Equity",   f"${eq2:,.2f}")
    row("Cash",     f"${ca2:,.2f}")
    ftr()

    log_run("scan", rgm, eq2, ca2, len(all_sigs), entries, exits, pos2)
    write_daily(today, eq2, ca2, rgm, month, pos2, all_sigs, buys_log, sells_log)


# =============================================================================
#  ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    mode = detect_mode()
    log.info(f"Mode auto-detected: {mode}")

    client = TradingClient(API_KEY, API_SECRET, paper=PAPER_TRADING)
    acct   = client.get_account()
    equity = float(acct.equity)
    cash   = float(acct.cash)

    spy_raw = fetch_stock("SPY")
    spy_df  = add_ind(spy_raw) if spy_raw is not None else None
    rgm     = regime(spy_df)

    hdr(); row("RUBBER BAND BOT  v7"); div()
    row("Mode",     mode.upper())
    row("Time",     datetime.utcnow().strftime("%H:%M UTC"))
    row("Regime",   rgm.upper())
    row("Universe", UNIVERSE)
    row("Equity",   f"${equity:,.2f}")
    ftr()

    if mode == "scan":
        run_scan(client, equity, cash, rgm)
    elif mode == "exits":
        run_exits(client, equity, cash, rgm)
    elif mode == "weekly":
        run_summary(client, equity, cash, rgm)
        write_weekly(client, equity, cash)
    else:
        run_summary(client, equity, cash, rgm)
