# -*- coding: utf-8 -*-
"""
PAPER BOT v1  *** PAPER TRADING — NO REAL MONEY ***
========================================================================
Paper-trading mirror of Rubber Band Bot v8 with two additions:

  1. TRANCHE BUYS  (proportional scale-in)
     First signal:  buy 50% of target size immediately.
     Next morning:  buy remaining 50% IF price is still ≤ entry × 1.005
                    (still a good setup) AND the window hasn't expired.
     This reduces timing risk on entry — you're not all-in on a single
     closing price that may gap away by open the next day.

  2. PARTIAL SELLS  (proportional scale-out)
     First exit trigger (midline crossing): sell 50% of position,
     move stop to cover remaining 50%.
     Second trigger (time stop, stop-loss, or second midline): sell rest.
     Stop-loss always exits the FULL remaining position immediately.
     This lets winners run past the midline while banking partial profit.

SEPARATE FROM LIVE BOT:
  - Uses ALPACA_PAPER_KEY / ALPACA_PAPER_SECRET env vars
  - PAPER_TRADING = True (hardcoded, cannot be changed)
  - Logs to logs/paper/ directory (never collides with live bot logs)
  - Add a SECOND cron entry pointing to paper_bot.py to run in parallel

GITHUB SECRETS required (separate from live bot secrets):
  ALPACA_PAPER_KEY
  ALPACA_PAPER_SECRET
========================================================================
"""

import os, json, time, logging, csv, math
from datetime import datetime, timedelta, date
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

from alpaca.trading.client   import TradingClient
from alpaca.trading.requests import (MarketOrderRequest, GetOrdersRequest,
                                      StopOrderRequest,
                                      LimitOrderRequest)
from alpaca.trading.enums    import (OrderSide, TimeInForce, QueryOrderStatus,
                                     OrderType, OrderStatus)
from alpaca.data.historical  import StockHistoricalDataClient, CryptoHistoricalDataClient
from alpaca.data.requests    import StockBarsRequest, CryptoBarsRequest
from alpaca.data.timeframe   import TimeFrame


# =============================================================================
#  KEYS  (paper account — separate secrets from live bot)
# =============================================================================

API_KEY    = os.getenv("ALPACA_PAPER_KEY")
API_SECRET = os.getenv("ALPACA_PAPER_SECRET")

if not API_KEY or not API_SECRET:
    print("ERROR: Set ALPACA_PAPER_KEY and ALPACA_PAPER_SECRET as environment variables.")
    raise SystemExit(1)


# =============================================================================
#  CONFIGURATION
# =============================================================================

PAPER_TRADING = True   # HARDCODED — this bot NEVER uses real money

# ---- Universe ----------------------------------------------------------------
UNIVERSE = "both"

# ---- Position sizing (same validated params as live bot) --------------------
SEASONAL_SIZE_PCT    = 0.20
OFFSCHEDULE_SIZE_PCT = 0.12
CASH_RESERVE_PCT     = 0.05
MIN_TRADE_SIZE       = 20.0

# ---- Tranche buy parameters (NEW in paper bot) ------------------------------
# First buy = TRANCHE1_FRAC × target dollar amount.
# Second buy = TRANCHE2_FRAC × target dollar amount (next morning, if still valid).
# TRANCHE_WINDOW_DAYS: how many calendar days after entry to attempt tranche 2.
# TRANCHE_MAX_ABOVE:   skip tranche 2 if price has risen more than this above entry.
#   1.005 = don't add if stock already moved +0.5% above entry (setup may be gone).
TRANCHE1_FRAC       = 0.50
TRANCHE2_FRAC       = 0.50
TRANCHE_WINDOW_DAYS = 1
TRANCHE_MAX_ABOVE   = 1.005

# ---- Partial exit parameter (NEW in paper bot) ------------------------------
# On first voluntary exit (midline crossing): sell this fraction.
# Remaining (1 - PARTIAL_EXIT_FRAC) rides to next exit trigger.
# Stop-loss ALWAYS exits the full position, regardless of this setting.
PARTIAL_EXIT_FRAC = 0.50

# ---- TEST MODE  (stress-test exit logic — flip to False for normal paper trading)
# When True: stop tightens to -0.1% and max hold shrinks to 1 day.
# Almost every position will trigger a stop or time exit within 1-2 sessions,
# letting you verify all exit code paths (stop full-exit, max-hold full-exit,
# midline partial-exit + remainder) without waiting weeks for natural triggers.
# Signal and tranche logic are unchanged so you can still verify those paths.
# Flip TEST_MODE = False once you're satisfied with the exit behaviour.
TEST_MODE = True

# ---- Exit rules --------------------------------------------------------------
# TEST_MODE overrides: -0.1% stop / 1d hold  →  almost everything exits fast.
# Normal mode:         -0.5% stop / 3d hold  →  matches live bot validation.
EXIT_DAYS_MAX  = 1     if TEST_MODE else 3
EXIT_STOP_LOSS = -0.001 if TEST_MODE else -0.005

# ---- Extended-hours selling --------------------------------------------------
# When True: exit signals that fire at 3:50pm place post-market LIMIT sells
# (extended_hours=True, TimeInForce.DAY) that execute between 4pm and 8pm ET.
# Benefits:
#   1. Fills at/near closing price with no overnight exposure on exited positions
#   2. DAY limit orders work on fractional shares — no GTC fractional rejection
#   3. If the limit doesn't fill by 8pm (rare), it expires; the 9:35am morning
#      run re-evaluates and exits with a regular market order.
# The 9:35am morning run always uses regular market hours (extended hours = off).
USE_EXTENDED_HOURS_SELL = True

# ---- Crypto weekend mode ----------------------------------------------------
# On weekends the stock market is closed. This mode runs the paper bot against
# a small basket of liquid crypto pairs to:
#   1. Test the full buy → stop → limit-sell → market-fallback flow end-to-end
#   2. Test extended-hours (24/7) limit sells vs market sells on real fills
#   3. Accumulate paper P&L data on crypto mean-reversion signals
#
# Strategy: RSI(<35) oversold mean-reversion — same concept as stock strategies.
# Position size: 3% of equity per coin (small, testing focus not returns).
# Stop: -1.5% (crypto is noisier than stocks; wider stop to survive volatility).
# Hold: 1 run cycle (~6h); sell on next run if above entry or at stop.
#
# Flip to False if you only want weekday stock trading.
CRYPTO_WEEKEND_MODE = True

CRYPTO_PAIRS = [
    "BTC/USD",   # Bitcoin — most liquid
    "ETH/USD",   # Ethereum
    "SOL/USD",   # Solana — good mean-reversion
    "AVAX/USD",  # Avalanche
    "LINK/USD",  # Chainlink
]
CRYPTO_POSITION_PCT = 0.03   # 3% of equity per coin
CRYPTO_STOP_LOSS    = -0.015  # -1.5% stop (wider than stocks)
CRYPTO_RSI_ENTRY    = 60      # buy when RSI ≤ this (oversold)
CRYPTO_RSI_EXIT     = 55      # sell partial when RSI ≥ this (recovered)
CRYPTO_LOG_DIR      = LOG_DIR / "crypto"

# ---- Daily entry cap ---------------------------------------------------------
MAX_DAY_TRADES = 5

# ---- Data quality ------------------------------------------------------------
MIN_STOCK_PRICE  = 5.0
MIN_HISTORY_DAYS = 220

# ---- Paths (paper-specific) --------------------------------------------------
LOG_DIR    = Path("logs") / "paper"
DAILY_DIR  = LOG_DIR / "daily"
WEEKLY_DIR = LOG_DIR / "weekly"
TX_FILE    = LOG_DIR / "transactions.csv"
RUNS_FILE  = LOG_DIR / "runs.csv"
PDT_FILE   = LOG_DIR / "pdt.json"
TRANCHES_FILE = LOG_DIR / "tranches.json"   # tranche state (new)

for d in [LOG_DIR, DAILY_DIR, WEEKLY_DIR]:
    d.mkdir(parents=True, exist_ok=True)

W = 68


# =============================================================================
#  CALENDAR STRATEGY SCHEDULE  (identical to live bot)
# =============================================================================

SCHEDULE = {
    1:  {"p": "MomReversal", "s": "52wkLow",     "note": "Jan: MomReversal primary, 52wkLow secondary"},
    2:  {"p": "52wkLow",     "s": "VolumeSpike",  "note": "Feb: 52wkLow + VolumeSpike"},
    3:  {"p": "GapDown",     "s": "52wkLow",      "note": "Mar: GapDown primary"},
    4:  {"p": "RSIRecovery", "s": "Pullback50",   "note": "Apr: RSIRecovery primary"},
    5:  {"p": "RSIRecovery", "s": "52wkLow",      "note": "May: RSIRecovery primary"},
    6:  {"p": "GapDown",     "s": "VolumeSpike",  "note": "Jun: GapDown primary"},
    7:  {"p": "52wkLow",     "s": "Pullback50",   "note": "Jul: 52wkLow + Pullback50"},
    8:  {"p": "VolumeSpike", "s": "52wkLow",      "note": "Aug: VolumeSpike primary"},
    9:  {"p": "GapDown",     "s": "VolumeSpike",  "note": "Sep: GapDown + VolumeSpike"},
    10: {"p": "RubberBand",  "s": "GapDown",      "note": "Oct: RubberBand + GapDown"},
    11: {"p": "RSIRecovery", "s": "MomReversal",  "note": "Nov: RSIRecovery primary"},
    12: {"p": "MomReversal", "s": "VolumeSpike",  "note": "Dec: MomReversal + VolumeSpike"},
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
log = logging.getLogger("PaperBot")


# =============================================================================
#  DISPLAY HELPERS
# =============================================================================

def _trunc(s, n):
    s = str(s)
    return s if len(s) <= n else s[:n-1] + "…"

def hdr(title=""):
    if title: print(f"+{'='*W}+\n|  {title:<{W-2}}|")
    else:     print(f"+{'='*W}+")

def ftr():  print(f"+{'='*W}+")
def div():  print(f"+{'-'*W}+")
def blank():print(f"|{' '*W}|")

def row(label="", value=""):
    if value:
        lab = str(label); val = str(value)
        gap = W - 2 - len(lab) - len(val)
        if gap < 1: lab = lab[:W-4-len(val)]; gap = 2
        print(f"|  {lab}{' '*gap}{val}  |")
    else:
        print(f"|  {_trunc(str(label), W-2):<{W-2}}|")

def trow(*cols, widths=None):
    if not widths: widths = [W // len(cols)] * len(cols)
    parts = [_trunc(str(c), w-1).ljust(w) for c, w in zip(cols, widths)]
    inner = "".join(parts).rstrip()
    print(f"|  {inner:<{W-2}}|")


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
    df["GapPct"] = (o - c.shift(1)) / (c.shift(1) + 1e-10)
    df["Green"]  = (c > o).astype(int)
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
#  REGIME  (identical to live bot)
# =============================================================================

def regime(spy_df):
    if spy_df is None: return "corr"
    try:
        c = spy_df["Close"]; m = spy_df["BBM"].iloc[-1]
        r = spy_df["R60"].iloc[-1]
        if   c.iloc[-1] > m and r >  0.05: return "bull"
        elif c.iloc[-1] < m and r < -0.05: return "bear"
        else:                               return "corr"
    except Exception: return "corr"

def consec_down(close):
    n = 0
    for i in range(len(close)-1, 0, -1):
        if close.iloc[i] < close.iloc[i-1]: n += 1
        else: break
    return n


# =============================================================================
#  SIGNALS  (identical to live bot)
# =============================================================================

def _rb(ticker, df, p):
    c = df["Close"]; rsi = df["RSI"]; bbl = df["BBL25"] if p["bb_std"] == 2.5 else df["BBL20"]
    if p.get("require_ma200") and c.iloc[-1] < df["MA200"].iloc[-1]: return None
    cd = consec_down(c)
    if (cd >= p["consec_down"] and rsi.iloc[-1] < p["rsi_thresh"] and
            c.iloc[-1] < bbl.iloc[-1]):
        return {"ticker": ticker, "strategy": "RubberBand",
                "close": float(c.iloc[-1]), "rsi": float(rsi.iloc[-1]),
                "trigger": f"cd{cd} rsi{rsi.iloc[-1]:.0f}"}
    return None

def _52(ticker, df):
    c = df["Close"]
    if c.iloc[-1] <= df["L252"].iloc[-1] * 1.02:
        return {"ticker": ticker, "strategy": "52wkLow",
                "close": float(c.iloc[-1]), "trigger": "near_52wk_low"}
    return None

def _mr(ticker, df):
    c = df["Close"]; r1 = df["Ret1"]
    if r1.iloc[-1] < -0.04 and r1.iloc[-2] < -0.03:
        return {"ticker": ticker, "strategy": "MomReversal",
                "close": float(c.iloc[-1]), "trigger": f"2d_drop_{r1.iloc[-1]*100:.1f}%"}
    return None

def _gd(ticker, df):
    gap = df["GapPct"].iloc[-1]
    rsi = df["RSI"].iloc[-1]
    vol = df["VZ"].iloc[-1]
    if gap < -0.03 and rsi < 35 and vol > 1.0:
        return {"ticker": ticker, "strategy": "GapDown",
                "close": float(df["Close"].iloc[-1]),
                "trigger": f"gap{gap*100:.1f}% rsi{rsi:.0f}"}
    return None

def _vs(ticker, df):
    vz  = df["VZ"].iloc[-1]
    rsi = df["RSI"].iloc[-1]
    r1  = df["Ret1"].iloc[-1]
    if vz > 2.0 and rsi < 40 and r1 < -0.02:
        return {"ticker": ticker, "strategy": "VolumeSpike",
                "close": float(df["Close"].iloc[-1]),
                "vol_z": float(vz), "rsi": float(rsi),
                "trigger": f"vz{vz:.1f} rsi{rsi:.0f}"}
    return None

def _pb(ticker, df):
    c    = df["Close"].iloc[-1]
    ma50 = df["MA50"].iloc[-1]
    r1   = df["Ret1"].iloc[-1]
    rsi  = df["RSI"].iloc[-1]
    if c > ma50 * 0.95 and c < ma50 * 1.02 and r1 < -0.02 and rsi < 45:
        return {"ticker": ticker, "strategy": "Pullback50",
                "close": float(c),
                "trigger": f"near_ma50 rsi{rsi:.0f}"}
    return None

def _rsi(ticker, df):
    rsi = df["RSI"]
    c   = df["Close"]
    if rsi.iloc[-2] < 30 and rsi.iloc[-1] > 30:
        return {"ticker": ticker, "strategy": "RSIRecovery",
                "close": float(c.iloc[-1]),
                "rsi": float(rsi.iloc[-1]),
                "trigger": f"rsi_cross30 prev{rsi.iloc[-2]:.0f}"}
    return None

def get_signals(ticker, df, month, rgm):
    sc = SCHEDULE[month]
    p  = {"bull": BULL_P, "corr": CORR_P, "bear": BEAR_P}[rgm]
    fns = {"RubberBand": lambda: _rb(ticker, df, p),
           "52wkLow":    lambda: _52(ticker, df),
           "MomReversal":lambda: _mr(ticker, df),
           "GapDown":    lambda: _gd(ticker, df),
           "VolumeSpike":lambda: _vs(ticker, df),
           "Pullback50": lambda: _pb(ticker, df),
           "RSIRecovery":lambda: _rsi(ticker, df)}
    sched_strats = {sc["p"], sc["s"]}
    results = []
    for strat, fn in fns.items():
        try:
            sig = fn()
            if sig:
                sig["seasonal"] = strat in sched_strats
                sig.setdefault("vol_z", float(df["VZ"].iloc[-1]))
                results.append(sig)
        except Exception: pass
    return results


# =============================================================================
#  EXIT LOGIC  (identical to live bot)
# =============================================================================

def check_exit(df, pos, eod_only=False):
    try:
        c     = df["Close"]; bbm = df["BBM"]
        if c.empty: return False, "no_data"

        cur   = float(c.iloc[-1])
        ma    = float(bbm.iloc[-1])
        entry = pos.get("entry_price", cur)
        pnl   = (cur - entry) / entry if entry else 0

        if pnl <= EXIT_STOP_LOSS:
            return True, f"stop_loss ({pnl*100:.1f}%)"

        if pos.get("entry_date"):
            try:
                days = (datetime.today() -
                        datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days
                if days >= EXIT_DAYS_MAX:
                    return True, f"max_hold {days}d ({pnl*100:+.1f}%)"
            except Exception: pass

        if eod_only and cur > ma:
            return True, f"midline ({pnl*100:+.1f}%)"

        return False, "hold"
    except Exception:
        return False, "error"


# =============================================================================
#  POSITIONS  (identical to live bot)
# =============================================================================

def get_positions(client):
    try:
        return {p.symbol: p for p in client.get_all_positions()}
    except Exception as e:
        log.error(f"get_positions failed: {e}"); return {}

def enrich(client, positions):
    out = {}
    for sym, p in positions.items():
        entry_px = float(p.avg_entry_price)
        cur_px   = float(p.current_price)
        mkt_val  = float(p.market_value)
        cost     = float(p.cost_basis)
        pnl_d    = mkt_val - cost
        pnl_p    = pnl_d / cost * 100 if cost else 0
        qty      = abs(float(p.qty))

        entry_date = None
        try:
            req = GetOrdersRequest(status=QueryOrderStatus.CLOSED, symbols=[sym],
                                   limit=20)
            orders = client.get_orders(req)
            buy_orders = [o for o in orders
                          if o.side == OrderSide.BUY and
                          o.status in (OrderStatus.filled,
                                       OrderStatus.partially_filled)]
            if buy_orders:
                newest = max(buy_orders,
                             key=lambda o: o.filled_at or o.submitted_at)
                t = newest.filled_at or newest.submitted_at
                entry_date = t.strftime("%Y-%m-%d") if t else None
        except Exception: pass

        strat = "?"
        try:
            req = GetOrdersRequest(status=QueryOrderStatus.CLOSED, symbols=[sym],
                                   limit=5)
            for o in client.get_orders(req):
                if o.side == OrderSide.BUY and o.client_order_id:
                    parts = o.client_order_id.split("|")
                    if len(parts) >= 1:
                        strat = parts[0]; break
        except Exception: pass

        out[sym] = {"entry_price": entry_px, "current_price": cur_px,
                    "market_value": mkt_val, "cost_basis": cost,
                    "pnl_dollar": pnl_d, "pnl_pct": pnl_p,
                    "qty": qty, "dollar_amt": cost,
                    "entry_date": entry_date, "strategy": strat}
    return out


# =============================================================================
#  PDT TRACKING  (identical to live bot)
# =============================================================================

def load_pdt(): return json.load(open(PDT_FILE)) if PDT_FILE.exists() else []
def save_pdt(l): json.dump(l, open(PDT_FILE, "w"))

def pdt_n(l):
    today = str(date.today())
    return sum(1 for e in l if e == today)

def pdt_ok(l):
    return pdt_n(l) < MAX_DAY_TRADES


# =============================================================================
#  TRANCHE STATE  (new in paper bot)
# =============================================================================

def load_tranches():
    """Load tranche tracking dict. Returns {} if file doesn't exist."""
    if TRANCHES_FILE.exists():
        try:
            return json.load(open(TRANCHES_FILE))
        except Exception:
            return {}
    return {}

def save_tranches(t):
    """Persist tranche state to disk."""
    with open(TRANCHES_FILE, "w") as f:
        json.dump(t, f, indent=2)
        f.flush(); os.fsync(f.fileno())

def clean_tranches(positions):
    """Remove tranche entries for tickers no longer held."""
    tr = load_tranches()
    removed = [k for k in list(tr.keys()) if k not in positions]
    for k in removed:
        del tr[k]
    if removed:
        save_tranches(tr)
        log.info(f"  Tranches cleaned: removed {removed}")


# =============================================================================
#  ORDERS
# =============================================================================

def do_buy(client, ticker, dollars, strategy):
    try:
        cid = f"{strategy}|{ticker}|{date.today()}"[:48]
        o = client.submit_order(MarketOrderRequest(
            symbol=ticker, notional=round(dollars, 2),
            side=OrderSide.BUY, time_in_force=TimeInForce.DAY,
            client_order_id=cid))
        log.info(f"  BUY  {ticker}  ${dollars:.2f}  [{strategy}]  id={o.id}")
        return True
    except Exception as e:
        log.error(f"  BUY FAILED {ticker}: {e}"); return False

def cancel_stop_orders(client, ticker):
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, symbols=[ticker])
        for o in client.get_orders(req):
            if o.side == OrderSide.SELL:
                try:
                    client.cancel_order_by_id(str(o.id))
                    log.info(f"  SELL order cancelled {ticker}  "
                             f"type={getattr(o,'order_type','?')}  id={o.id}")
                except Exception as ce:
                    log.warning(f"  cancel failed {ticker} id={o.id}: {ce}")
    except Exception as e:
        log.warning(f"  cancel_stop_orders failed {ticker}: {e}")

def ensure_stop(client, ticker, entry_price, qty):
    """Place GTC stop-MARKET sell for the given qty.
    Skipped silently if a GTC stop already exists.

    Fractional-share handling: Alpaca rejects GTC orders on fractional qty.
    We floor to whole shares. If the position is < 1 share the stop is skipped
    entirely — the 9:35am software exit will catch it instead.
    """
    stop_price = round(entry_price * (1.0 + EXIT_STOP_LOSS), 2)
    stop_qty   = math.floor(qty)
    if stop_qty < 1:
        log.warning(f"  STOP skipped {ticker}: position is {qty:.4f} shares "
                    f"(<1 whole share) — 9:35am software exit will handle it")
        return False
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.OPEN, symbols=[ticker])
        for o in client.get_orders(req):
            if (getattr(o, "order_type", None) in (OrderType.STOP,
                                                    OrderType.STOP_LIMIT)
                    and o.side == OrderSide.SELL):
                log.info(f"  STOP already live {ticker} @ ${o.stop_price}")
                return True
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
    """Ensure every open position has a GTC stop-market order."""
    try:
        positions = client.get_all_positions()
        if not positions: return
        log.info(f"  place_all_stops: checking {len(positions)} positions...")
        for p in positions:
            ensure_stop(client, p.symbol,
                        float(p.avg_entry_price), float(p.qty))
    except Exception as e:
        log.warning(f"  place_all_stops failed: {e}")

def do_partial_sell(client, ticker, fraction=PARTIAL_EXIT_FRAC, extended_hours=False):
    """Sell FRACTION of the current position (partial exit).
    Cancels existing stop first, then re-places stop on the remaining qty.
    extended_hours=True: post-market limit (4–8pm ET), works on fractional shares.
    Returns True if the sell was submitted successfully."""
    cancel_stop_orders(client, ticker)
    try:
        pos      = client.get_open_position(ticker)
        full_qty = abs(float(pos.qty))
        sell_qty = max(0.001, round(full_qty * fraction, 9))
        remain   = round(full_qty - sell_qty, 9)
        cur      = float(pos.current_price)
        # Extended hours: limit slightly tighter (0.15% below) — still fills easily
        # at post-market prices which are typically near close.
        lim      = round(cur * (0.9985 if extended_hours else 0.998), 2)
        eh_tag   = " [extended-hours]" if extended_hours else ""

        order_kwargs = dict(
            symbol=ticker, qty=str(sell_qty),
            side=OrderSide.SELL,
            time_in_force=TimeInForce.DAY,
            limit_price=lim)
        if extended_hours:
            order_kwargs["extended_hours"] = True

        o = client.submit_order(LimitOrderRequest(**order_kwargs))
        log.info(f"  PARTIAL SELL{eh_tag} {ticker}  {sell_qty:.4f}/{full_qty:.4f} shares  "
                 f"limit=${lim:.2f}  id={o.id}")

        for _ in range(4):
            time.sleep(5)
            try:
                o2 = client.get_order_by_id(str(o.id))
                if o2.status in (OrderStatus.filled, OrderStatus.partially_filled):
                    log.info(f"  PARTIAL SELL filled {ticker}")
                    if remain > 0:
                        ensure_stop(client, ticker,
                                    float(pos.avg_entry_price), remain)
                    return True
            except Exception: pass

        # Limit didn't fill — cancel and use market
        try: client.cancel_order_by_id(str(o.id))
        except Exception: pass
        o2 = client.submit_order(MarketOrderRequest(
            symbol=ticker, qty=str(sell_qty),
            side=OrderSide.SELL,
            time_in_force=TimeInForce.DAY))
        log.info(f"  PARTIAL SELL market {ticker}  qty={sell_qty}  id={o2.id}")
        time.sleep(3)
        if remain > 0:
            ensure_stop(client, ticker, float(pos.avg_entry_price), remain)
        return True
    except Exception as e:
        log.error(f"  PARTIAL SELL FAILED {ticker}: {e}")
        return False

def do_sell(client, ticker, extended_hours=False):
    """Exit entire position (cancel stop → limit sell → market fallback).
    extended_hours=True: places post-market limit (4–8pm ET) instead of
    a regular-session order. Works on fractional shares (DAY limit).
    If the limit doesn't fill by 8pm it expires; 9:35am run re-exits.
    """
    cancel_stop_orders(client, ticker)
    eh_tag = " [extended-hours]" if extended_hours else ""

    try:
        pos = client.get_open_position(ticker)
        qty = abs(float(pos.qty))
        cur = float(pos.current_price)
        lim = round(cur * (0.9985 if extended_hours else 0.998), 2)

        order_kwargs = dict(
            symbol=ticker, qty=str(qty),
            side=OrderSide.SELL,
            time_in_force=TimeInForce.DAY,
            limit_price=lim)
        if extended_hours:
            order_kwargs["extended_hours"] = True

        o = client.submit_order(LimitOrderRequest(**order_kwargs))
        log.info(f"  SELL LIMIT{eh_tag} {ticker}  qty={qty}  limit=${lim:.2f}  id={o.id}")

        for _ in range(4):
            time.sleep(5)
            try:
                o2 = client.get_order_by_id(str(o.id))
                if o2.status in (OrderStatus.filled, OrderStatus.partially_filled):
                    log.info(f"  SELL filled {ticker}")
                    return True
            except Exception: pass

        try: client.cancel_order_by_id(str(o.id))
        except Exception: pass
    except Exception: pass

    # Market fallback (regular hours only — extended hours doesn't allow market orders)
    if not extended_hours:
        try:
            pos = client.get_open_position(ticker)
            qty = abs(float(pos.qty))
            o = client.submit_order(MarketOrderRequest(
                symbol=ticker, qty=str(qty),
                side=OrderSide.SELL,
                time_in_force=TimeInForce.DAY))
            log.info(f"  SELL MARKET {ticker}  qty={qty}  id={o.id}")
            return True
        except Exception:
            pass

    # Final check — position might already be closed (stop fired, or EH limit filled)
    try:
        client.get_open_position(ticker)
        if extended_hours:
            log.info(f"  {ticker} EH limit pending — will re-check at 9:35am")
            return True   # order is alive, treat as success
        log.error(f"  SELL FAILED {ticker} — position still open")
        return False
    except Exception:
        log.info(f"  {ticker} already closed"); return True


# =============================================================================
#  TRANCHE 2 CHECK  (new in paper bot)
# =============================================================================

def check_pending_tranches(client, positions, avail, pdt, equity, rgm):
    """Called once per run_scan, before new entry orders.
    Fills tranche-2 buys for positions opened exactly TRANCHE_WINDOW_DAYS ago
    where the price is still at or near entry (setup still valid).
    Returns (n_filled, updated_avail)."""
    tranches = load_tranches()
    today    = date.today()
    filled   = 0
    reserve  = equity * CASH_RESERVE_PCT

    hdr("TRANCHE 2 CHECK")
    pending = {k: v for k, v in tranches.items()
               if not v.get("tranche2_filled") and not v.get("tranche2_skipped")}
    if not pending:
        row("No pending tranche-2 fills today."); ftr(); return 0, avail

    for ticker, tr in list(pending.items()):
        if ticker not in positions:
            tr["tranche2_skipped"] = True
            row(ticker, "SKIP — position closed"); continue

        pos = positions[ticker]
        entry_date = pos.get("entry_date")
        if not entry_date:
            row(ticker, "SKIP — no entry date"); continue

        try:
            days_since = (today - date.fromisoformat(entry_date)).days
        except Exception:
            row(ticker, "SKIP — bad entry date"); continue

        if days_since < TRANCHE_WINDOW_DAYS:
            row(ticker, f"WAIT — entered {days_since}d ago (window={TRANCHE_WINDOW_DAYS}d)")
            continue

        if days_since > TRANCHE_WINDOW_DAYS:
            tr["tranche2_skipped"] = True
            row(ticker, f"SKIP — window expired ({days_since}d ago)"); continue

        cur_price   = pos.get("current_price", 0)
        entry_price = pos.get("entry_price", 0)

        if entry_price > 0 and cur_price > entry_price * TRANCHE_MAX_ABOVE:
            tr["tranche2_skipped"] = True
            row(ticker, f"SKIP — price moved up too much "
                f"(${cur_price:.2f} vs entry ${entry_price:.2f})"); continue

        t2_dollars = tr.get("target_dollars", 0) * TRANCHE2_FRAC
        if t2_dollars < MIN_TRADE_SIZE:
            tr["tranche2_skipped"] = True
            row(ticker, f"SKIP — t2 size ${t2_dollars:.2f} < min ${MIN_TRADE_SIZE}")
            continue

        if avail - t2_dollars < reserve:
            row(ticker, f"SKIP — not enough cash (avail=${avail:.2f})"); continue

        if not pdt_ok(pdt):
            row(ticker, "SKIP — PDT limit"); continue

        strat = tr.get("strategy", "?")
        row(f"  TRANCHE2 [{ticker}]  {strat}",
            f"${t2_dollars:.2f}  entry=${entry_price:.2f} cur=${cur_price:.2f}")
        if do_buy(client, ticker, t2_dollars, strat):
            tr["tranche2_filled"] = True
            avail -= t2_dollars
            filled += 1
            pdt.append(str(today))
            log_tx("BUY", ticker, strat, cur_price, t2_dollars, "N/A",
                   float(client.get_account().equity))

    save_tranches(tranches)
    ftr()
    return filled, avail


# =============================================================================
#  TRANSACTION LOG  (identical to live bot — different TX_FILE path)
# =============================================================================

TX_F = ["timestamp","date","action","ticker","strategy","price","dollar_amount",
        "pnl_pct","pnl_dollar","hold_days","exit_reason","regime","equity_after"]

def log_tx(action, ticker, strategy, price, dollars, rgm, equity,
           pnl_pct=0, pnl_dollar=0, hold_days=0, exit_reason=""):
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
    }
    try:
        init = not TX_FILE.exists()
        with open(TX_FILE, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=TX_F)
            if init: w.writeheader()
            w.writerow(row_data)
            f.flush(); os.fsync(f.fileno())
        log.info(f"  TX logged: {action} {ticker}  "
                 f"{'P&L '+str(round(pnl_pct,2))+'%' if action=='SELL' else '$'+str(round(dollars,2))}")
    except Exception as e:
        log.error(f"  TX LOG FAILED {action} {ticker}: {e}")
        print(f"TX_FALLBACK|{row_data}", flush=True)

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
#  PERFORMANCE DASHBOARD  (paper-specific paths)
# =============================================================================

def write_dashboard():
    try:
        STARTING_EQUITY = 100000.0   # paper account starting capital
        DASH_FILE = LOG_DIR / "dashboard.md"
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
        trough_equity  = min(eq_series) if eq_series else STARTING_EQUITY
        total_ret_pct  = (current_equity - STARTING_EQUITY) / STARTING_EQUITY * 100
        max_dd_pct     = (trough_equity - peak_equity) / peak_equity * 100 if peak_equity else 0

        last_run      = runs[-1] if runs else {}
        current_cash  = last_run.get("cash", 0)
        open_pos_cnt  = last_run.get("open_positions", "0")
        open_tickers  = last_run.get("tickers", "")
        last_run_time = last_run.get("timestamp", "N/A")

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

        strat_map = {b["ticker"]: b.get("strategy", "?") for b in buys_tx}
        from collections import defaultdict
        by_exit  = defaultdict(list)
        by_strat = defaultdict(list)
        for s in sells_tx:
            key = (s.get("exit_reason") or "unknown").split("(")[0].strip().split(" ")[0]
            by_exit[key].append(s)
            st  = strat_map.get(s["ticker"], s.get("strategy", "?")) or "?"
            by_strat[st].append(s)

        daily_eq = {}
        for r in runs:
            d = r.get("timestamp", "")[:10]
            if d: daily_eq[d] = r["equity"]
        eq_dates = sorted(daily_eq.keys())

        now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
        L = []
        L.append("# 📊 Paper Bot — Performance Dashboard (PAPER TRADING)")
        L.append(f"*Updated: {now_str}*\n")
        L.append("> ⚠️ **Paper trading only — no real money involved.**\n")

        L.append("## Account Snapshot")
        L.append("| | |"); L.append("|---|---|")
        L.append(f"| **Current Equity** | ${current_equity:.2f} |")
        L.append(f"| **Starting Equity** | ${STARTING_EQUITY:.2f} |")
        L.append(f"| **Total Return** | {total_ret_pct:+.2f}% (${current_equity - STARTING_EQUITY:+.2f}) |")
        L.append(f"| **Max Drawdown** | {max_dd_pct:.2f}% |")
        L.append(f"| **Current Cash** | ${current_cash:.2f} |")
        L.append(f"| **Open Positions** | {open_pos_cnt} ({open_tickers}) |")
        L.append(f"| **Last Run** | {last_run_time} |")
        L.append("")

        L.append("## Trade Performance")
        L.append("| Metric | Value |"); L.append("|---|---|")
        L.append(f"| **Total Closed Trades** | {total_closed} |")
        L.append(f"| **Win Rate** | {win_rate:.1f}% |")
        L.append(f"| **Avg Win** | +{avg_win:.2f}% |")
        L.append(f"| **Avg Loss** | {avg_loss:.2f}% |")
        L.append(f"| **Profit Factor** | {pf:.2f}x |")
        L.append(f"| **Avg Hold Days** | {avg_hold:.1f}d |")
        L.append(f"| **Total Realised P&L** | ${total_pnl:+.2f} |")
        L.append("")

        L.append("## Tranche Feature  (new in paper bot)")
        L.append("| Parameter | Value |"); L.append("|---|---|")
        L.append(f"| Tranche 1 (entry day) | {TRANCHE1_FRAC*100:.0f}% of target size |")
        L.append(f"| Tranche 2 (next day) | {TRANCHE2_FRAC*100:.0f}% — only if price ≤ entry×{TRANCHE_MAX_ABOVE} |")
        L.append(f"| Partial exit | Sell {PARTIAL_EXIT_FRAC*100:.0f}% at midline, ride rest to time/stop |")
        L.append("")

        if by_exit:
            L.append("## Exit Reasons")
            L.append("| Exit | Trades | WR | Avg P&L% |"); L.append("|---|---|---|---|")
            for reason, grp in sorted(by_exit.items(), key=lambda x: -len(x[1])):
                gw = [s for s in grp if s["pnl_pct"] > 0]
                L.append(f"| `{reason}` | {len(grp)} | {len(gw)/len(grp)*100:.0f}% "
                         f"| {sum(s['pnl_pct'] for s in grp)/len(grp):+.2f}% |")
            L.append("")

        recent = sells_tx[-20:][::-1]
        if recent:
            L.append("## Recent Closed Trades")
            L.append("| Date | Ticker | Strategy | P&L% | P&L$ | Hold | Exit |")
            L.append("|---|---|---|---|---|---|---|")
            for s in recent:
                st = strat_map.get(s["ticker"], s.get("strategy", "?")) or "?"
                L.append(f"| {s['date']} | **{s['ticker']}** | `{st}` "
                         f"| {s['pnl_pct']:+.2f}% | ${s['pnl_dollar']:+.2f} "
                         f"| {s['hold_days']}d | {s.get('exit_reason','')} |")
            L.append("")

        L.append("---")
        L.append("*Auto-generated. Paper account only.*")
        DASH_FILE.write_text("\n".join(L))
        log.info("  Dashboard written → logs/paper/dashboard.md")
    except Exception as e:
        log.warning(f"  write_dashboard failed: {e}")


# =============================================================================
#  DAILY LOG
# =============================================================================

def write_daily(today, equity, cash, rgm, month, positions, signals, buys, sells):
    sc = SCHEDULE[month]
    op_pnl = sum(p.get("pnl_dollar", 0) for p in positions.values())
    fname  = DAILY_DIR / f"{today}.md"
    L = [f"# Paper Bot Daily Log -- {today}", "*(PAPER TRADING)*", "",
         "## Account", "| | |", "|---|---|",
         f"| Equity | **${equity:,.2f}** |",
         f"| Cash | ${cash:,.2f} |",
         f"| Open P&L | ${op_pnl:+,.2f} |",
         f"| Regime | {rgm.upper()} |",
         f"| Universe | {UNIVERSE} |",
         f"| Strategies | {sc['p']} + {sc['s']} |", "",
         "## Holdings"]
    if positions:
        L += ["| Ticker | Strategy | Entry | Now | P&L% | P&L$ |",
              "|---|---|---|---|---|---|"]
        for t, p in positions.items():
            L.append(f"| **{t}** | `{p.get('strategy','?')}` "
                     f"| ${p['entry_price']:.2f} | ${p['current_price']:.2f} "
                     f"| {p['pnl_pct']:+.1f}% | ${p['pnl_dollar']:+.2f} |")
    else:
        L.append("*No open positions.*")
    if buys or sells:
        L += ["", "## Today's Trades"]
        for b in buys:
            L.append(f"- **BUY**  {b['tk']}  `{b['st']}`  ${b['$']:.2f}  @ ${b['px']:.2f}  {b['t']}")
        for s in sells:
            L.append(f"- **SELL** {s['tk']}  `{s['st']}`  @ ${s['px']:.2f}  ({s['why']})  {s['t']}")
    if signals:
        L += ["", f"## Signals ({len(signals)} found)"]
        for s in signals[:20]:
            tier = "SEAS" if s.get("seasonal") else "off"
            L.append(f"- [{tier}] **{s['ticker']}**  `{s['strategy']}`  "
                     f"${s['close']:.2f}  {s.get('trigger','')}")
    fname.write_text("\n".join(L))
    log.info(f"  Daily log → {fname}")


# =============================================================================
#  TIME AUTO-DETECTION  (identical to live bot)
# =============================================================================

def detect_mode():
    from zoneinfo import ZoneInfo
    now = datetime.now(ZoneInfo("America/New_York"))
    h = now.hour; m = now.minute; dow = now.weekday()
    # Weekend (Sat=5, Sun=6): crypto mode if enabled
    if dow >= 5:
        return "crypto" if CRYPTO_WEEKEND_MODE else "weekly"
    # Friday after 5pm: treat as weekend
    if dow == 4 and h >= 17:
        return "crypto" if CRYPTO_WEEKEND_MODE else "weekly"
    # Weekday scan window: 3:45–4:10pm ET
    if (h == 15 and m >= 45) or (h == 16 and m <= 10): return "scan"
    # Weekday exits window: 9:30am–3pm ET
    if (h == 9 and m >= 30) or (10 <= h <= 15): return "exits"
    return "summary"


# =============================================================================
#  STATUS SUMMARY
# =============================================================================

def run_summary(client, equity, cash, rgm):
    positions = enrich(client, get_positions(client))
    invested  = sum(p.get("dollar_amt", 0) for p in positions.values())
    open_pnl  = sum(p.get("pnl_dollar", 0) for p in positions.values())
    hdr("PAPER BOT — ACCOUNT STATUS")
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
        tranches = load_tranches()
        for t, p in positions.items():
            tr    = tranches.get(t, {})
            t2    = "T2✓" if tr.get("tranche2_filled") else ("T1" if tr else "")
            psold = "½sold" if tr.get("partial_sold") else ""
            note  = f"{t2} {psold}".strip()
            trow(t, f"{p.get('strategy','?')} {note}",
                 f"${p.get('dollar_amt',0):.2f}", f"${p['entry_price']:.2f}",
                 f"${p['current_price']:.2f}", f"{p['pnl_pct']:+.1f}%",
                 f"${p['pnl_dollar']:+.2f}", widths=[7,14,9,7,7,6,7])
        blank()
        row("Total invested", f"${invested:,.2f}")
        row("Total open P&L", f"${open_pnl:+,.2f}")
    else:
        blank(); row("No open positions."); blank()
    ftr()
    log_run("summary", rgm, equity, cash, 0, 0, 0, positions)


# =============================================================================
#  EXITS RUN  (modified: partial sell on midline)
# =============================================================================

def run_exits(client, equity, cash, rgm):
    place_all_stops(client)
    positions = enrich(client, get_positions(client))
    if not positions:
        hdr("PAPER BOT MORNING CHECK"); blank(); row("No open positions."); blank(); ftr()
        log_run("exits", rgm, equity, cash, 0, 0, 0, {}); return

    pos_data = fetch_batch(list(positions.keys()), "positions")
    exits    = 0
    exited   = set()
    tranches = load_tranches()

    already_sold_today = set()
    today_str = str(date.today())
    if TX_FILE.exists():
        with open(TX_FILE, newline="") as _f:
            for _r in csv.DictReader(_f):
                if _r.get("action") == "SELL" and _r.get("date") == today_str:
                    already_sold_today.add(_r["ticker"])

    hdr("PAPER BOT EXIT CHECK")
    row("Exit logic", f"stop{EXIT_STOP_LOSS*100:.0f}% / {EXIT_DAYS_MAX}d / midline(partial)")
    div()
    for ticker, pos in positions.items():
        if ticker in already_sold_today:
            row(ticker, "already sold today"); continue

        pnl_frac = pos.get("pnl_pct", 0) / 100
        tr       = tranches.get(ticker, {})

        # ── Stop-loss: ALWAYS full exit ────────────────────────────────────
        if pnl_frac <= EXIT_STOP_LOSS:
            why = f"stop_loss ({pnl_frac*100:.1f}%)"
            row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%", f"FULL EXIT: {why}")
            if do_sell(client, ticker):
                exits += 1; exited.add(ticker); already_sold_today.add(ticker)
                cur = pos["current_price"]
                dh  = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days \
                      if pos.get("entry_date") else 0
                log_tx("SELL", ticker, pos.get("strategy","?"), cur, pos["market_value"],
                       rgm, float(client.get_account().equity),
                       pos["pnl_pct"], pos["pnl_dollar"], dh, why)
                tranches.pop(ticker, None)
            continue

        # ── Max-hold: ALWAYS full exit ─────────────────────────────────────
        if pos.get("entry_date"):
            try:
                days = (datetime.today() -
                        datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days
                if days >= EXIT_DAYS_MAX:
                    why = f"max_hold {days}d ({pnl_frac*100:+.1f}%)"
                    row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%", f"FULL EXIT: {why}")
                    if do_sell(client, ticker):
                        exits += 1; exited.add(ticker); already_sold_today.add(ticker)
                        cur = pos["current_price"]
                        log_tx("SELL", ticker, pos.get("strategy","?"), cur, pos["market_value"],
                               rgm, float(client.get_account().equity),
                               pos["pnl_pct"], pos["pnl_dollar"], days, why)
                        tranches.pop(ticker, None)
                    continue
            except Exception: pass

        # ── Midline: PARTIAL exit first time, full exit if already partial ─
        if ticker not in pos_data:
            row(ticker, "no price data"); continue
        ex, why = check_exit(pos_data[ticker], pos, eod_only=False)
        if ex and "midline" in why:
            if not tr.get("partial_sold"):
                row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%",
                    f"PARTIAL EXIT (50%): {why}")
                if do_partial_sell(client, ticker, PARTIAL_EXIT_FRAC):
                    exits += 1; already_sold_today.add(ticker)
                    cur = pos["current_price"]
                    dh  = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days \
                          if pos.get("entry_date") else 0
                    log_tx("SELL", ticker, pos.get("strategy","?"), cur,
                           pos["market_value"] * PARTIAL_EXIT_FRAC,
                           rgm, float(client.get_account().equity),
                           pos["pnl_pct"], pos["pnl_dollar"] * PARTIAL_EXIT_FRAC,
                           dh, f"partial_{why}")
                    tr["partial_sold"] = True
                    tranches[ticker]   = tr
            else:
                row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%",
                    f"FULL EXIT (remaining 50%): {why}")
                if do_sell(client, ticker):
                    exits += 1; exited.add(ticker); already_sold_today.add(ticker)
                    cur = pos["current_price"]
                    dh  = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days \
                          if pos.get("entry_date") else 0
                    log_tx("SELL", ticker, pos.get("strategy","?"), cur,
                           pos["market_value"],
                           rgm, float(client.get_account().equity),
                           pos["pnl_pct"], pos["pnl_dollar"], dh, f"remainder_{why}")
                    tranches.pop(ticker, None)
        else:
            row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%",
                f"EXIT: {_trunc(why,22)}" if ex else "HOLD")
            if ex and do_sell(client, ticker):
                exits += 1; exited.add(ticker); already_sold_today.add(ticker)
                cur = pos["current_price"]
                dh  = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days \
                      if pos.get("entry_date") else 0
                log_tx("SELL", ticker, pos.get("strategy","?"), cur, pos["market_value"],
                       rgm, float(client.get_account().equity),
                       pos["pnl_pct"], pos["pnl_dollar"], dh, why)
                tranches.pop(ticker, None)
    ftr()

    save_tranches(tranches)
    log_run("exits", rgm, equity, cash, 0, 0, exits, positions)


# =============================================================================
#  FULL SCAN  (modified: tranche buys + partial sells)
# =============================================================================

def run_scan(client, equity, cash, rgm):
    today  = date.today(); month = today.month; sc = SCHEDULE[month]
    reserve = equity * CASH_RESERVE_PCT; avail = max(0.0, cash - reserve)

    hdr("PAPER BOT v1  --  DAILY SCAN  (PAPER TRADING)")
    row("Mode",     "*** PAPER — NO REAL MONEY ***")
    row("Date",     str(today))
    row("Universe", UNIVERSE)
    row("Month",    f"{MN[month]}: {sc['p']} + {sc['s']}")
    row("Regime",   rgm.upper())
    row("Exit",     f"midline(partial) / stop{EXIT_STOP_LOSS*100:.0f}% / {EXIT_DAYS_MAX}d max")
    row("Tranches", f"T1={TRANCHE1_FRAC*100:.0f}% entry / T2={TRANCHE2_FRAC*100:.0f}% next-day")
    ftr()

    hdr("ACCOUNT")
    row("Equity",    f"${equity:,.2f}")
    row("Cash",      f"${cash:,.2f}")
    row("Reserve",   f"${reserve:,.2f}")
    row("Available", f"${avail:,.2f}")
    row("Target seasonal", f"${equity*SEASONAL_SIZE_PCT:,.2f}  "
        f"→ T1 ${equity*SEASONAL_SIZE_PCT*TRANCHE1_FRAC:,.2f}  "
        f"T2 ${equity*SEASONAL_SIZE_PCT*TRANCHE2_FRAC:,.2f}")
    row("Target off-sched", f"${equity*OFFSCHEDULE_SIZE_PCT:,.2f}  "
        f"→ T1 ${equity*OFFSCHEDULE_SIZE_PCT*TRANCHE1_FRAC:,.2f}")
    ftr()

    positions = enrich(client, get_positions(client))
    pdt       = load_pdt()
    tranches  = load_tranches()
    clean_tranches(positions)   # remove stale tranche entries

    hdr(f"HOLDINGS  ({len(positions)} open)")
    if positions:
        trow("TICKER","STRATEGY","INVESTED","ENTRY","NOW","P&L%","TRANCHE",
             widths=[7,14,9,7,7,6,8])
        div()
        for t, p in positions.items():
            tr    = tranches.get(t, {})
            t_note = ("T1+T2" if tr.get("tranche2_filled") else
                      ("T1" if tr else ""))
            if tr.get("partial_sold"): t_note += " ½sold"
            trow(t, p.get("strategy","?"),
                 f"${p.get('dollar_amt',0):.2f}", f"${p['entry_price']:.2f}",
                 f"${p['current_price']:.2f}", f"{p['pnl_pct']:+.1f}%",
                 t_note, widths=[7,14,9,7,7,6,8])
        blank()
        inv = sum(p.get("dollar_amt",0) for p in positions.values())
        pnl = sum(p.get("pnl_dollar",0) for p in positions.values())
        row("Total invested", f"${inv:,.2f}")
        row("Total open P&L", f"${pnl:+,.2f}")
    else:
        blank(); row("No open positions."); blank()
    row(f"PDT used: {pdt_n(pdt)}/{MAX_DAY_TRADES}")
    ftr()

    # ── Check tranche-2 fills FIRST ───────────────────────────────────────
    t2_filled, avail = check_pending_tranches(
        client, positions, avail, pdt, equity, rgm)

    # ── Exit check on held positions (EOD) ────────────────────────────────
    exits = 0; sells_log = []
    already_sold_today = set()
    if TX_FILE.exists():
        with open(TX_FILE, newline="") as _f:
            for _r in csv.DictReader(_f):
                if _r.get("action") == "SELL" and _r.get("date") == str(today):
                    already_sold_today.add(_r["ticker"])

    tranches = load_tranches()   # reload after tranche check
    if positions:
        pos_data = fetch_batch(list(positions.keys()), "positions")
        hdr("EXIT EVALUATION  (EOD — midline partial + stop + max-hold)")
        for ticker, pos in list(positions.items()):
            if ticker in already_sold_today:
                row(ticker, "already sold today"); continue

            pnl_frac = pos.get("pnl_pct", 0) / 100
            tr       = tranches.get(ticker, {})

            # Stop-loss: full exit always
            if pnl_frac <= EXIT_STOP_LOSS:
                why = f"stop_loss ({pnl_frac*100:.1f}%)"
                row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%", f"FULL EXIT: {why}")
                if do_sell(client, ticker, extended_hours=USE_EXTENDED_HOURS_SELL):
                    exits += 1; cur = pos["current_price"]
                    dh = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days \
                         if pos.get("entry_date") else 0
                    log_tx("SELL", ticker, pos.get("strategy","?"), cur, pos["market_value"],
                           rgm, float(client.get_account().equity),
                           pos["pnl_pct"], pos["pnl_dollar"], dh, why)
                    sells_log.append({"t": datetime.now().strftime("%H:%M"),
                                       "tk": ticker, "st": pos.get("strategy","?"),
                                       "px": cur, "why": why})
                    already_sold_today.add(ticker)
                    del positions[ticker]
                    tranches.pop(ticker, None)
                continue

            # Max-hold: full exit always
            if pos.get("entry_date"):
                try:
                    days = (datetime.today() -
                            datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days
                    if days >= EXIT_DAYS_MAX:
                        why = f"max_hold {days}d ({pnl_frac*100:+.1f}%)"
                        row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%", f"FULL EXIT: {why}")
                        if do_sell(client, ticker, extended_hours=USE_EXTENDED_HOURS_SELL):
                            exits += 1; cur = pos["current_price"]
                            log_tx("SELL", ticker, pos.get("strategy","?"), cur, pos["market_value"],
                                   rgm, float(client.get_account().equity),
                                   pos["pnl_pct"], pos["pnl_dollar"], days, why)
                            sells_log.append({"t": datetime.now().strftime("%H:%M"),
                                               "tk": ticker, "st": pos.get("strategy","?"),
                                               "px": cur, "why": why})
                            already_sold_today.add(ticker)
                            del positions[ticker]
                            tranches.pop(ticker, None)
                        continue
                except Exception: pass

            # Midline: partial first time, full on second
            if ticker not in pos_data:
                row(ticker, "no price data"); continue
            ex, why = check_exit(pos_data[ticker], pos, eod_only=True)
            if ex and "midline" in why:
                if not tr.get("partial_sold"):
                    row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%",
                        f"PARTIAL EXIT (50%): {why}")
                    if do_partial_sell(client, ticker, PARTIAL_EXIT_FRAC,
                                       extended_hours=USE_EXTENDED_HOURS_SELL):
                        exits += 1; cur = pos["current_price"]
                        dh = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days \
                             if pos.get("entry_date") else 0
                        log_tx("SELL", ticker, pos.get("strategy","?"), cur,
                               pos["market_value"] * PARTIAL_EXIT_FRAC,
                               rgm, float(client.get_account().equity),
                               pos["pnl_pct"], pos["pnl_dollar"] * PARTIAL_EXIT_FRAC,
                               dh, f"partial_{why}")
                        sells_log.append({"t": datetime.now().strftime("%H:%M"),
                                           "tk": ticker, "st": pos.get("strategy","?"),
                                           "px": cur, "why": f"partial_{why}"})
                        already_sold_today.add(ticker)
                        tr["partial_sold"] = True
                        tranches[ticker]   = tr
                else:
                    row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%",
                        f"FULL EXIT (remainder): {why}")
                    if do_sell(client, ticker, extended_hours=USE_EXTENDED_HOURS_SELL):
                        exits += 1; cur = pos["current_price"]
                        dh = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days \
                             if pos.get("entry_date") else 0
                        log_tx("SELL", ticker, pos.get("strategy","?"), cur,
                               pos["market_value"],
                               rgm, float(client.get_account().equity),
                               pos["pnl_pct"], pos["pnl_dollar"], dh, f"remainder_{why}")
                        sells_log.append({"t": datetime.now().strftime("%H:%M"),
                                           "tk": ticker, "st": pos.get("strategy","?"),
                                           "px": cur, "why": f"remainder_{why}"})
                        already_sold_today.add(ticker); del positions[ticker]
                        tranches.pop(ticker, None)
            else:
                row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%",
                    f"EXIT: {_trunc(why,20)}" if ex else "HOLD")
                if ex and do_sell(client, ticker, extended_hours=USE_EXTENDED_HOURS_SELL):
                    exits += 1; cur = pos["current_price"]
                    dh = (datetime.today() - datetime.strptime(pos["entry_date"], "%Y-%m-%d")).days \
                         if pos.get("entry_date") else 0
                    log_tx("SELL", ticker, pos.get("strategy","?"), cur, pos["market_value"],
                           rgm, float(client.get_account().equity),
                           pos["pnl_pct"], pos["pnl_dollar"], dh, why)
                    sells_log.append({"t": datetime.now().strftime("%H:%M"),
                                       "tk": ticker, "st": pos.get("strategy","?"),
                                       "px": cur, "why": why})
                    already_sold_today.add(ticker); del positions[ticker]
                    tranches.pop(ticker, None)
        ftr()
    save_tranches(tranches)

    # ── Universe scan ─────────────────────────────────────────────────────
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

    # Sort: seasonal first
    all_sigs.sort(key=lambda s: (0 if s.get("seasonal") else 1))

    # Signal-scaled sizing (same logic as live bot)
    already_held  = set(positions.keys())
    viable        = [s for s in all_sigs if s["ticker"] not in already_held]
    n_viable      = max(1, len(viable))
    n_sea_pending = sum(1 for s in viable if s.get("seasonal"))

    equal_share = avail / n_viable
    sea_da = max(MIN_TRADE_SIZE,
                 min(equity * SEASONAL_SIZE_PCT, equal_share))
    off_da = max(MIN_TRADE_SIZE,
                 min(equity * OFFSCHEDULE_SIZE_PCT,
                     equal_share * (OFFSCHEDULE_SIZE_PCT / SEASONAL_SIZE_PCT)))
    scale_active = equal_share < equity * SEASONAL_SIZE_PCT

    # ── Entry orders (TRANCHE 1 only = 50% of target) ─────────────────────
    hdr("ENTRY ORDERS  (TRANCHE 1 — 50% of target)")
    cash = float(client.get_account().cash); avail = max(0.0, cash - reserve)
    if scale_active and n_viable > 1:
        row(f"Signal scaling: {n_viable} signals → "
            f"sea=${sea_da:.0f} off=${off_da:.0f}")
    entries = 0; buys_log = []
    n_unfilled_sea = n_sea_pending
    tranches = load_tranches()

    for sig in all_sigs:
        ticker   = sig["ticker"]; strategy = sig["strategy"]
        is_seas  = sig.get("seasonal", False)
        skip = ""
        if not pdt_ok(pdt):   skip = "PDT limit"
        elif avail <= 1.0:    skip = "reserve floor"
        da_target = sea_da if is_seas else off_da
        da_t1     = da_target * TRANCHE1_FRAC   # buy 50% now

        if not skip and not is_seas and n_unfilled_sea > 0:
            if avail - da_t1 < sea_da * TRANCHE1_FRAC:
                skip = "seasonal reserve"
        if not skip and da_t1 > avail: skip = "not enough cash"

        tier = "S" if is_seas else "o"
        if skip:
            row(f"  SKIP [{tier}] {ticker}  {strategy}", _trunc(skip, 20))
            continue
        row(f"  ENTER [{tier}] {ticker}  {strategy}",
            f"T1 ${da_t1:.2f}  (of target ${da_target:.2f})")
        if do_buy(client, ticker, da_t1, strategy):
            entries += 1; avail -= da_t1
            pdt.append(str(today))
            if is_seas: n_unfilled_sea = max(0, n_unfilled_sea - 1)
            log_tx("BUY", ticker, strategy, sig["close"], da_t1, rgm,
                   float(client.get_account().equity))
            buys_log.append({"t": datetime.now().strftime("%H:%M"),
                              "tk": ticker, "st": strategy,
                              "px": sig["close"], "$": da_t1})
            # Save tranche state for tranche-2 check tomorrow
            tranches[ticker] = {
                "target_dollars":  da_target,
                "tranche1_dollars": da_t1,
                "tranche1_date":   str(today),
                "tranche2_filled": False,
                "tranche2_skipped": False,
                "partial_sold":    False,
                "strategy":        strategy,
            }

    save_tranches(tranches)
    if entries == 0 and not all_sigs: row("  No entries placed.")
    ftr()

    # GTC stop placement for new buys
    if entries > 0:
        hdr("GTC STOP PLACEMENT")
        row(f"Waiting 5s for {entries} buy(s) to fill...")
        ftr()
        time.sleep(5)
    place_all_stops(client)

    save_pdt(pdt)
    acct2 = client.get_account()
    eq2   = float(acct2.equity); ca2 = float(acct2.cash)
    pos2  = enrich(client, get_positions(client))

    hdr("SESSION SUMMARY")
    row("Regime",        rgm.upper())
    row("Universe",      UNIVERSE)
    row("Strategy",      f"{sc['p']} + {sc['s']}")
    row("Scanned",       str(len(all_data)))
    row("Signals",       str(len(all_sigs)))
    row("T2 fills",      str(t2_filled))
    row("T1 entries",    str(entries))
    row("Exits",         str(exits))
    row("Open pos",      str(len(pos2)))
    row("Equity",        f"${eq2:,.2f}")
    row("Cash",          f"${ca2:,.2f}")
    ftr()

    log_run("scan", rgm, eq2, ca2, len(all_sigs), entries, exits, pos2)
    write_daily(today, eq2, ca2, rgm, month, pos2, all_sigs, buys_log, sells_log)
    write_dashboard()


# =============================================================================
#  CRYPTO WEEKEND MODE
# =============================================================================

def _fetch_crypto_ohlcv(symbol, days=30):
    """Fetch OHLCV for a crypto pair via yfinance. Returns DataFrame or None.
    yfinance symbol: BTC/USD → BTC-USD"""
    yf_sym = symbol.replace("/", "-")
    try:
        import yfinance as yf
        df = yf.download(yf_sym, period=f"{days}d", interval="1h",
                         auto_adjust=True, progress=False)
        if df is None or len(df) < 20: return None
        df.columns = [c.lower() for c in df.columns]
        df.index   = pd.to_datetime(df.index, utc=True)
        return df
    except Exception as e:
        log.warning(f"  crypto fetch failed {symbol}: {e}"); return None


def _crypto_rsi(df, period=14):
    """RSI on hourly close prices."""
    delta = df["close"].diff()
    gain  = delta.clip(lower=0).rolling(period).mean()
    loss  = (-delta.clip(upper=0)).rolling(period).mean()
    rs    = gain / loss.replace(0, 1e-9)
    return (100 - 100 / (1 + rs)).iloc[-1]


def _crypto_signals(pairs):
    """Return list of dicts for crypto pairs where RSI is oversold."""
    signals = []
    for sym in pairs:
        df = _fetch_crypto_ohlcv(sym, days=14)
        if df is None or len(df) < 20: continue
        rsi   = _crypto_rsi(df)
        close = float(df["close"].iloc[-1])
        # Change over last 24h (24 hourly bars)
        prev24 = float(df["close"].iloc[-25]) if len(df) >= 25 else close
        chg24  = (close - prev24) / prev24 * 100
        # Volume spike: last bar vs 24h avg
        vol_avg = float(df["volume"].tail(24).mean()) or 1
        vol_z   = (float(df["volume"].iloc[-1]) - vol_avg) / vol_avg
        signals.append({
            "symbol": sym, "close": close, "rsi": rsi,
            "chg24": chg24, "vol_z": vol_z,
        })
        log.info(f"  {sym:<12} close=${close:>10,.2f}  RSI={rsi:.1f}  "
                 f"24h={chg24:+.2f}%  vol_z={vol_z:+.2f}")
    return signals


def run_crypto_weekend(client, equity, cash):
    """Weekend crypto paper-trading run.
    Goals:
      1. Scan CRYPTO_PAIRS for oversold RSI signals → buy entries
      2. Check existing crypto positions → test full sell flow
         (limit sell → market fallback, extended-hours path)
      3. Log everything to logs/paper/crypto/
    """
    CRYPTO_LOG_DIR.mkdir(parents=True, exist_ok=True)
    now_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    reserve = equity * 0.05  # keep 5% cash reserve

    hdr()
    row("PAPER BOT — CRYPTO WEEKEND MODE"); div()
    row("Time",    now_str)
    row("Equity",  f"${equity:,.2f}")
    row("Cash",    f"${cash:,.2f}")
    row("Pairs",   ", ".join(CRYPTO_PAIRS))
    row("Signal",  f"RSI ≤ {CRYPTO_RSI_ENTRY} (oversold entry)")
    row("Stop",    f"{CRYPTO_STOP_LOSS*100:.1f}%  (wider for crypto volatility)")
    row("Size",    f"{CRYPTO_POSITION_PCT*100:.0f}% per coin  "
                   f"(${equity*CRYPTO_POSITION_PCT:,.0f} target)")
    row("Purpose", "Testing sell strategies: limit, market, partial")
    ftr()

    # ── Step 1: check and exit existing crypto positions ─────────────────────
    all_positions = {}
    try:
        for p in client.get_all_positions():
            sym = getattr(p, "symbol", "")
            # Alpaca crypto positions: "BTCUSD", "ETHUSD" etc.
            if any(c in sym for c in ["BTC","ETH","SOL","AVAX","LINK"]):
                all_positions[sym] = p
    except Exception as e:
        log.warning(f"  get_all_positions failed: {e}")

    exits = 0
    if all_positions:
        hdr(f"CRYPTO HOLDINGS  ({len(all_positions)} open)")
        for sym, pos in all_positions.items():
            qty    = abs(float(pos.qty))
            cur    = float(pos.current_price)
            ep     = float(pos.avg_entry_price)
            pnl_p  = (cur - ep) / ep * 100
            unreal = float(pos.unrealized_pl)
            row(f"{sym}", f"qty={qty:.6f}  entry=${ep:.2f}  now=${cur:.2f}  "
                f"P&L={pnl_p:+.2f}%  ${unreal:+.2f}")

            # Exit conditions:
            #  a) Stop loss hit
            #  b) RSI recovered above exit threshold
            should_exit = False
            exit_reason = ""

            if pnl_p <= CRYPTO_STOP_LOSS * 100:
                should_exit = True
                exit_reason = f"stop_loss ({pnl_p:.1f}%)"

            if not should_exit:
                # Get RSI for this pair
                pair_sym = sym.replace("USD", "/USD")  # BTCUSD → BTC/USD
                df = _fetch_crypto_ohlcv(pair_sym, days=3)
                if df is not None:
                    rsi = _crypto_rsi(df)
                    row(f"  {sym} RSI", f"{rsi:.1f}")
                    if rsi >= CRYPTO_RSI_EXIT:
                        should_exit = True
                        exit_reason = f"rsi_exit (RSI={rsi:.0f})"

            if should_exit:
                row(f"  EXIT {sym}", exit_reason)
                # Test BOTH sell paths: first try limit sell, then market fallback
                # Crypto is 24/7 so no "extended hours" concept — always DAY limit
                try:
                    cancel_stop_orders(client, sym)
                    pos2 = client.get_open_position(sym)
                    qty2 = abs(float(pos2.qty))
                    cur2 = float(pos2.current_price)
                    lim  = round(cur2 * 0.9990, 4)  # 0.10% below — fast fill
                    o = client.submit_order(LimitOrderRequest(
                        symbol=sym, qty=str(qty2),
                        side=OrderSide.SELL,
                        time_in_force=TimeInForce.GTC,   # crypto allows GTC on fractional
                        limit_price=lim,
                    ))
                    log.info(f"  CRYPTO SELL LIMIT {sym}  qty={qty2:.6f}  "
                             f"limit=${lim:.4f}  id={o.id}")
                    row(f"  SELL LIMIT {sym}", f"lim=${lim:.4f}  qty={qty2:.6f}")

                    # Wait 15s for fill
                    time.sleep(15)
                    try:
                        o2 = client.get_order_by_id(str(o.id))
                        if o2.status in (OrderStatus.filled, OrderStatus.partially_filled):
                            log.info(f"  CRYPTO SELL LIMIT filled {sym} @ {o2.filled_avg_price}")
                            row(f"  ✅ SELL LIMIT filled {sym}",
                                f"@ ${float(o2.filled_avg_price or cur2):.4f}")
                            exits += 1
                            # Log to crypto CSV
                            _crypto_log_tx("SELL", sym, pnl_p, unreal, exit_reason, equity)
                            continue
                    except Exception: pass

                    # Limit not filled → cancel and market sell
                    try:
                        client.cancel_order_by_id(str(o.id))
                    except Exception: pass
                    row(f"  SELL LIMIT timeout {sym}", "→ market fallback")
                    client.close_position(sym)
                    row(f"  ✅ SELL MARKET {sym}", "closed")
                    exits += 1
                    _crypto_log_tx("SELL_MKT", sym, pnl_p, unreal, exit_reason, equity)

                except Exception as e:
                    log.warning(f"  CRYPTO SELL failed {sym}: {e}")
                    row(f"  ❌ SELL failed {sym}", str(e)[:40])
            else:
                row(f"  HOLD {sym}", f"P&L={pnl_p:+.2f}%  (waiting for RSI≥{CRYPTO_RSI_EXIT})")
        ftr()
    else:
        hdr("CRYPTO HOLDINGS"); blank(); row("No crypto positions."); blank(); ftr()

    # ── Step 2: scan for new entries ─────────────────────────────────────────
    hdr("CRYPTO SIGNAL SCAN")
    row(f"Scanning {len(CRYPTO_PAIRS)} pairs for RSI ≤ {CRYPTO_RSI_ENTRY}...")
    ftr()

    signals = _crypto_signals(CRYPTO_PAIRS)
    entry_signals = [s for s in signals if s["rsi"] <= CRYPTO_RSI_ENTRY]

    hdr(f"CRYPTO SIGNALS  ({len(entry_signals)} of {len(signals)} oversold)")
    if signals:
        trow("PAIR", "PRICE", "RSI", "24h%", "VOL_Z", "ACTION",
             widths=[10, 12, 6, 7, 7, 10])
        div()
        for s in signals:
            action = "BUY" if s["rsi"] <= CRYPTO_RSI_ENTRY else "watch"
            trow(s["symbol"], f"${s['close']:,.2f}", f"{s['rsi']:.1f}",
                 f"{s['chg24']:+.2f}%", f"{s['vol_z']:+.2f}", action,
                 widths=[10, 12, 6, 7, 7, 10])
    blank(); ftr()

    # ── Step 3: place entries ─────────────────────────────────────────────────
    hdr("CRYPTO ENTRY ORDERS")
    already_held = {p.symbol for p in client.get_all_positions()
                    if any(c in p.symbol for c in ["BTC","ETH","SOL","AVAX","LINK"])}
    entries = 0
    for s in entry_signals:
        alpaca_sym = s["symbol"].replace("/", "")  # BTC/USD → BTCUSD
        if alpaca_sym in already_held:
            row(f"  SKIP {s['symbol']}", "already held"); continue
        avail = max(0.0, cash - reserve)
        da    = min(equity * CRYPTO_POSITION_PCT, avail)
        if da < 5.0:
            row(f"  SKIP {s['symbol']}", "insufficient cash"); continue

        row(f"  ENTER {s['symbol']}", f"${da:.2f}  RSI={s['rsi']:.1f}")
        try:
            o = client.submit_order(MarketOrderRequest(
                symbol=s["symbol"],    # Alpaca crypto uses "BTC/USD" format
                notional=round(da, 2),
                side=OrderSide.BUY,
                time_in_force=TimeInForce.GTC,
            ))
            log.info(f"  CRYPTO BUY {s['symbol']}  ${da:.2f}  id={o.id}")
            entries += 1; cash -= da
            _crypto_log_tx("BUY", s["symbol"], 0.0, 0.0, "rsi_entry", equity)
            row(f"  ✅ BUY {s['symbol']}", f"id={o.id}")
        except Exception as e:
            log.warning(f"  CRYPTO BUY failed {s['symbol']}: {e}")
            row(f"  ❌ BUY failed {s['symbol']}", str(e)[:40])
    if not entry_signals:
        blank(); row("No oversold signals this run."); blank()
    ftr()

    # ── Summary ───────────────────────────────────────────────────────────────
    hdr("CRYPTO SESSION SUMMARY")
    row("Pairs scanned",  str(len(signals)))
    row("Entry signals",  str(len(entry_signals)))
    row("Entries placed", str(entries))
    row("Exits placed",   str(exits))
    row("Test focus",     "limit sell → market fallback → partial sell")
    ftr()

    log_run("crypto", "crypto", equity, cash, len(signals), entries, exits, {})
    write_dashboard()


def _crypto_log_tx(action, symbol, pnl_pct, pnl_dollar, reason, equity):
    """Append a crypto trade to transactions.csv so the dashboard shows it."""
    try:
        init = not TX_FILE.exists()
        with open(TX_FILE, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=TX_F)
            if init: w.writeheader()
            w.writerow({
                "timestamp":    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "date":         str(date.today()),
                "action":       action,
                "ticker":       symbol,
                "strategy":     "CryptoRSI",
                "price":        0,
                "dollar_amount":0,
                "pnl_pct":      round(pnl_pct, 3),
                "pnl_dollar":   round(pnl_dollar, 2),
                "hold_days":    0,
                "exit_reason":  reason,
                "regime":       "crypto",
                "equity_after": round(equity, 2),
            })
    except Exception as e:
        log.warning(f"  _crypto_log_tx failed: {e}")


# =============================================================================
#  ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    mode = detect_mode()
    log.info(f"Mode auto-detected: {mode}")

    client = TradingClient(API_KEY, API_SECRET, paper=True)   # ALWAYS paper=True
    acct   = client.get_account()
    equity = float(acct.equity)
    cash   = float(acct.cash)

    # Safety guard: paper account should be funded with ~$100k.
    # If equity < $5,000 it almost certainly means the paper bot is pointing at
    # the live account (wrong keys) — abort immediately before touching anything.
    if equity < 5000.0:
        print(f"ABORT: equity=${equity:.2f} is too low for a paper account.")
        print("This usually means ALPACA_PAPER_KEY/ALPACA_PAPER_SECRET are pointing")
        print("at the live account. Set the correct paper trading keys and retry.")
        raise SystemExit(1)

    spy_raw = fetch_stock("SPY")
    spy_df  = add_ind(spy_raw) if spy_raw is not None else None
    rgm     = regime(spy_df)

    hdr(); row("PAPER BOT v1  (PAPER TRADING — NO REAL MONEY)"); div()
    row("Mode",     mode.upper())
    row("Time",     datetime.utcnow().strftime("%H:%M UTC"))
    row("Regime",   rgm.upper())
    row("Universe", UNIVERSE)
    row("Equity",   f"${equity:,.2f}")
    row("Tranches", f"T1={TRANCHE1_FRAC*100:.0f}% / T2={TRANCHE2_FRAC*100:.0f}%  "
        f"window={TRANCHE_WINDOW_DAYS}d  max_above={TRANCHE_MAX_ABOVE}")
    row("Partial exit", f"{PARTIAL_EXIT_FRAC*100:.0f}% at midline, remainder rides")
    if TEST_MODE:
        div()
        row("*** TEST MODE ACTIVE ***",
            f"stop={EXIT_STOP_LOSS*100:.1f}%  hold={EXIT_DAYS_MAX}d")
        row("Flip TEST_MODE=False in paper_bot.py for normal paper trading.")
    ftr()

    if mode == "crypto":
        run_crypto_weekend(client, equity, cash)
    elif mode == "scan":
        run_scan(client, equity, cash, rgm)
    elif mode == "exits":
        run_exits(client, equity, cash, rgm)
    elif mode == "weekly":
        run_summary(client, equity, cash, rgm)
    else:
        run_summary(client, equity, cash, rgm)
