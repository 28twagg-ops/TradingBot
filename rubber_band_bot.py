"""
╔══════════════════════════════════════════════════════════════════════════╗
║        RUBBER BAND BOT  v3  —  Calendar-Aware Year-Round System        ║
║                                                                         ║
║  Strategy auto-selected by MONTH + REGIME from 5-year backtest data    ║
║  Universe: Live S&P 500 + S&P MidCap 400 (~900 tickers, Wikipedia)     ║
║  Broker:   Alpaca Markets  |  paper → live = one config line            ║
║                                                                         ║
║  SCHEDULE (Task Scheduler / cron):                                      ║
║    4:15 pm ET  →  python rubber_band_bot_v3.py                         ║
║    9:35 am ET  →  python rubber_band_bot_v3.py --mode exits            ║
╚══════════════════════════════════════════════════════════════════════════╝

SETUP:
    pip install alpaca-py yfinance pandas numpy

FULL DAILY RUN (4:15pm):
    python rubber_band_bot_v3.py

MORNING EXIT CHECK (9:35am):
    python rubber_band_bot_v3.py --mode exits

GO LIVE:
    Set PAPER_TRADING = False and paste live Alpaca keys. Nothing else changes.
"""

import sys, json, time, logging, csv, argparse
from datetime import datetime, timedelta, date
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

from alpaca.trading.client   import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums    import OrderSide, TimeInForce


# ══════════════════════════════════════════════════════════════════════════════
#  CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

import os

API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")

if not API_KEY or not API_SECRET:
    raise ValueError("API keys not found. Check GitHub Secrets.")
PAPER_TRADING      = True    # False = real money (only after 30+ days paper)

POSITION_SIZE_PCT  = 0.02
MAX_OPEN_POSITIONS = 2
MAX_PORTFOLIO_HEAT = 0.40

EXIT_DAYS_MAX  = 7
EXIT_STOP_LOSS = -0.03

MAX_DAY_TRADES   = 3
MIN_STOCK_PRICE  = 5.0
MIN_HISTORY_DAYS = 220

LOG_DIR      = Path("logs")
TRADE_LOG    = LOG_DIR / "trades.csv"
PDT_LOG      = LOG_DIR / "pdt_ledger.json"
SIGNAL_LOG   = LOG_DIR / "signals.csv"
POSITION_LOG = LOG_DIR / "open_positions.json"


# ══════════════════════════════════════════════════════════════════════════════
#  CALENDAR STRATEGY SCHEDULE
#  Hard-coded from 5-year backtest. Each month gets a primary + secondary.
#
#  Key data points driving these choices:
#    Jan  MomReversal +3.67%, 62% win  |  RubberBand_Corr -0.44% (DISABLED)
#    Feb  52wkLow +1.37%               |  RubberBand_Corr -2.09% (DISABLED)
#    Mar  52wkLow +1.85%, 68% win      |  strong value month
#    Apr  RubberBand_Corr +0.71%       |  regime determines strict/relaxed
#    May  RubberBand_Corr +1.93%, 58%  |  strong
#    Jun  52wkLow +1.81%, Sharpe 1.72  |  best Jun strategy
#    Jul  52wkLow +2.86%, 66% win      |  excellent
#    Aug  RubberBand_Corr +4.72%, 70%  |  BEST month for this strategy
#    Sep  GoldenCross +0.07%           |  worst month — this is best available
#    Oct  RubberBand_Corr +3.29%, 70%  |  second best month
#    Nov  RubberBand_Corr +4.77%, 86%  |  HIGHEST WIN RATE of the year
#    Dec  MomReversal +1.34%, 58%      |  year-end recovery plays
# ══════════════════════════════════════════════════════════════════════════════

SCHEDULE = {
    1:  {"primary": "MomReversal", "secondary": "52wkLow",
         "note": "Jan — MomReversal +3.67%. RubberBand negative this month."},
    2:  {"primary": "52wkLow",     "secondary": "MomReversal",
         "note": "Feb — 52wkLow +1.37%. RubberBand_Corr -2.09% (disabled)."},
    3:  {"primary": "52wkLow",     "secondary": "MomReversal",
         "note": "Mar — 52wkLow +1.85%, 68% win. Strong value month."},
    4:  {"primary": "RubberBand",  "secondary": "52wkLow",
         "note": "Apr — RubberBand_Corr +0.71%. Regime sets strict/relaxed."},
    5:  {"primary": "RubberBand",  "secondary": "52wkLow",
         "note": "May — RubberBand_Corr +1.93%, 58% win. Strong month."},
    6:  {"primary": "52wkLow",     "secondary": "RubberBand",
         "note": "Jun — 52wkLow +1.81%, Sharpe 1.72. Best Jun strategy."},
    7:  {"primary": "52wkLow",     "secondary": "RubberBand",
         "note": "Jul — 52wkLow +2.86%, 66% win. Excellent value month."},
    8:  {"primary": "RubberBand",  "secondary": "52wkLow",
         "note": "Aug — RubberBand_Corr +4.72%, 70% win. Best month of year."},
    9:  {"primary": "GoldenCross", "secondary": "52wkLow",
         "note": "Sep — weakest month. GoldenCross best available at +0.07%."},
    10: {"primary": "RubberBand",  "secondary": "52wkLow",
         "note": "Oct — RubberBand_Corr +3.29%, 70% win. Second best month."},
    11: {"primary": "RubberBand",  "secondary": "MomReversal",
         "note": "Nov — RubberBand_Corr +4.77%, 86% WIN RATE. Best month."},
    12: {"primary": "MomReversal", "secondary": "52wkLow",
         "note": "Dec — MomReversal +1.34%. Year-end recovery trades."},
}

BULL_PARAMS       = {"consec_down":5,"rsi_thresh":25,"bb_std":2.5,"vol_z_min":1.5,"require_ma200":True}
CORRECTION_PARAMS = {"consec_down":3,"rsi_thresh":30,"bb_std":2.0,"vol_z_min":0.5,"require_ma200":False}
BEAR_PARAMS       = {"consec_down":5,"rsi_thresh":20,"bb_std":2.5,"vol_z_min":1.0,"require_ma200":False}


# ══════════════════════════════════════════════════════════════════════════════
#  TICKER UNIVERSE — live from Wikipedia, no hardcoded fallback
# ══════════════════════════════════════════════════════════════════════════════

def get_live_tickers() -> list:
    """
    Fetches current S&P 500 + S&P MidCap 400 from Wikipedia at runtime.
    ~900 stocks. No hardcoded list — always reflects actual index membership.
    If Wikipedia fails, bot exits with a clear error rather than running on stale data.
    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    log.info("Fetching live ticker lists from Wikipedia...")

    try:
        sp500 = pd.read_html(
            "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
            storage_options=headers)[0]["Symbol"].tolist()
        log.info(f"  S&P 500:    {len(sp500)} tickers")
    except Exception as e:
        log.error(f"FATAL: Could not load S&P 500 from Wikipedia: {e}")
        raise SystemExit(1)

    try:
        mid400 = pd.read_html(
            "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies",
            storage_options=headers)[0]["Symbol"].tolist()
        log.info(f"  S&P MidCap: {len(mid400)} tickers")
    except Exception as e:
        log.error(f"FATAL: Could not load S&P 400 from Wikipedia: {e}")
        raise SystemExit(1)

    combined = list(dict.fromkeys(sp500 + mid400))
    cleaned  = [t.replace(".", "-") for t in combined]
    log.info(f"  Total universe: {len(cleaned)} unique tickers")
    return cleaned


# ══════════════════════════════════════════════════════════════════════════════
#  LOGGING
# ══════════════════════════════════════════════════════════════════════════════

LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_DIR / f"bot_{date.today()}.log"),
    ],
)
log = logging.getLogger("RBv3")


# ══════════════════════════════════════════════════════════════════════════════
#  ALPACA
# ══════════════════════════════════════════════════════════════════════════════

def get_client() -> TradingClient:
    if "PASTE" in API_KEY:
        log.error("Set API_KEY and API_SECRET at the top of this file.")
        raise SystemExit(1)
    return TradingClient(API_KEY, API_SECRET, paper=PAPER_TRADING)


# ══════════════════════════════════════════════════════════════════════════════
#  DATA
# ══════════════════════════════════════════════════════════════════════════════

def fetch_stock(ticker: str, days: int = 280) -> pd.DataFrame | None:
    try:
        end   = datetime.today()
        start = end - timedelta(days=days + 60)
        df = yf.download(ticker, start=start, end=end,
                         progress=False, auto_adjust=True)
        if df.empty or len(df) < MIN_HISTORY_DAYS:
            return None
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        df = df[["Open","High","Low","Close","Volume"]].dropna()
        if float(df["Close"].iloc[-1]) < MIN_STOCK_PRICE:
            return None
        return df
    except Exception:
        return None


def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    c, v = df["Close"], df["Volume"]
    df   = df.copy()
    d    = c.diff()
    g    = d.clip(lower=0).rolling(14).mean()
    l    = (-d.clip(upper=0)).rolling(14).mean()
    df["RSI"]        = 100 - 100 / (1 + g / (l + 1e-10))
    df["BB_Lower25"] = c.rolling(20).mean() - 2.5 * c.rolling(20).std()
    df["BB_Lower20"] = c.rolling(20).mean() - 2.0 * c.rolling(20).std()
    df["BB_Mid"]     = c.rolling(20).mean()
    avg              = v.rolling(20).mean()
    std              = v.rolling(20).std()
    df["Vol_Z"]      = (v - avg) / (std + 1e-10)
    df["MA50"]       = c.rolling(50).mean()
    df["MA200"]      = c.rolling(200).mean()
    df["Low252"]     = c.rolling(252).min()
    df["Ret60"]      = c.pct_change(60)
    return df


def fetch_batch(tickers: list, label: str = "") -> dict:
    data  = {}
    total = len(tickers)
    for i in range(0, total, 40):
        chunk = tickers[i:i+40]
        for t in chunk:
            df = fetch_stock(t)
            if df is not None:
                data[t] = add_indicators(df)
        done = min(i+40, total)
        log.info(f"  [{label}]  {done}/{total}  ({len(data)} valid)")
        time.sleep(1.5)
    return data


# ══════════════════════════════════════════════════════════════════════════════
#  REGIME DETECTION
# ══════════════════════════════════════════════════════════════════════════════

def detect_regime(spy_df: pd.DataFrame | None) -> str:
    if spy_df is None or len(spy_df) < 210:
        return "bull"
    ma200 = float(spy_df["MA200"].iloc[-1])
    c_now = float(spy_df["Close"].iloc[-1])
    r     = c_now / (ma200 + 1e-10)
    if   r >= 1.00: return "bull"
    elif r >= 0.93: return "correction"
    else:           return "bear"


def consec_down(close: pd.Series) -> int:
    vals = close.values
    n = 0
    for i in range(len(vals)-1, 0, -1):
        if vals[i] < vals[i-1]: n += 1
        else: break
    return n


# ══════════════════════════════════════════════════════════════════════════════
#  SIGNAL FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def sig_rubber_band(ticker, df, params) -> dict | None:
    try:
        c     = df["Close"]
        c_now = float(c.iloc[-1])
        rsi_v = float(df["RSI"].iloc[-1])
        bb_v  = float(df["BB_Lower25" if params["bb_std"]>=2.4 else "BB_Lower20"].iloc[-1])
        vz_v  = float(df["Vol_Z"].iloc[-1])
        ma200 = float(df["MA200"].iloc[-1])
        cd    = consec_down(c)
        if any(pd.isna(x) for x in [rsi_v, bb_v, vz_v, ma200]):
            return None
        c1 = (cd >= params["consec_down"]) or (rsi_v < params["rsi_thresh"])
        c2 = c_now <= bb_v
        c3 = vz_v  >= params["vol_z_min"]
        c4 = (c_now > ma200) if params["require_ma200"] else True
        if c1 and c2 and c3 and c4:
            return {"ticker":ticker,"strategy":"RubberBand","date":str(date.today()),
                    "close":round(c_now,2),"rsi":round(rsi_v,1),"vol_z":round(vz_v,2),
                    "trigger":"RSI" if rsi_v<params["rsi_thresh"] else f"{cd}d-down"}
        return None
    except Exception: return None


def sig_52wk_low(ticker, df) -> dict | None:
    try:
        c_now = float(df["Close"].iloc[-1])
        low52 = float(df["Low252"].iloc[-1])
        rsi_v = float(df["RSI"].iloc[-1])
        vz_v  = float(df["Vol_Z"].iloc[-1])
        if any(pd.isna(x) for x in [low52, rsi_v]): return None
        if (c_now <= low52*1.05) and (vz_v >= 0.5) and (rsi_v > 10):
            return {"ticker":ticker,"strategy":"52wkLow","date":str(date.today()),
                    "close":round(c_now,2),"rsi":round(rsi_v,1),"vol_z":round(vz_v,2),
                    "trigger":f"{((c_now/low52)-1)*100:.1f}% above 52wk low"}
        return None
    except Exception: return None


def sig_momentum_reversal(ticker, df) -> dict | None:
    try:
        c     = df["Close"]
        c_now = float(c.iloc[-1])
        ret60 = float(df["Ret60"].iloc[-1])
        ret5  = float(c.pct_change(5).iloc[-1])
        rsi_v = float(df["RSI"].iloc[-1])
        vz_v  = float(df["Vol_Z"].iloc[-1])
        if any(pd.isna(x) for x in [ret60, ret5, rsi_v]): return None
        if (ret60<-0.12) and (ret5>-0.02) and (rsi_v<40) and (vz_v>=0.3):
            return {"ticker":ticker,"strategy":"MomReversal","date":str(date.today()),
                    "close":round(c_now,2),"rsi":round(rsi_v,1),"vol_z":round(vz_v,2),
                    "trigger":f"{ret60*100:.1f}% drop/60d, stabilising"}
        return None
    except Exception: return None


def sig_golden_cross(ticker, df) -> dict | None:
    try:
        ma50   = float(df["MA50"].iloc[-1])
        ma200  = float(df["MA200"].iloc[-1])
        ma50_p = float(df["MA50"].iloc[-2])
        ma200_p= float(df["MA200"].iloc[-2])
        c_now  = float(df["Close"].iloc[-1])
        if any(pd.isna(x) for x in [ma50,ma200,ma50_p,ma200_p]): return None
        if (ma50>ma200) and (ma50_p<=ma200_p):
            return {"ticker":ticker,"strategy":"GoldenCross","date":str(date.today()),
                    "close":round(c_now,2),"rsi":0.0,"vol_z":0.0,
                    "trigger":"50MA crossed above 200MA"}
        return None
    except Exception: return None


# ══════════════════════════════════════════════════════════════════════════════
#  CALENDAR + REGIME ROUTER
# ══════════════════════════════════════════════════════════════════════════════

def get_signals(ticker, df, month, regime) -> list:
    sched   = SCHEDULE[month]
    primary = sched["primary"]
    sec     = sched["secondary"]
    params  = (BULL_PARAMS if regime=="bull"
               else CORRECTION_PARAMS if regime=="correction"
               else BEAR_PARAMS)

    # Bear override — never buy dips in a bear market
    if regime == "bear":
        primary, sec = "52wkLow", "MomReversal"

    sigs = []
    for name in [primary, sec]:
        s = None
        if name == "RubberBand":    s = sig_rubber_band(ticker, df, params)
        elif name == "52wkLow":     s = sig_52wk_low(ticker, df)
        elif name == "MomReversal": s = sig_momentum_reversal(ticker, df)
        elif name == "GoldenCross": s = sig_golden_cross(ticker, df)
        if s: sigs.append(s)
    return sigs


# ══════════════════════════════════════════════════════════════════════════════
#  EXITS
# ══════════════════════════════════════════════════════════════════════════════

def check_exit(df, entry_price, entry_date) -> tuple[bool, str]:
    try:
        c_now = float(df["Close"].iloc[-1])
        mid   = float(df["BB_Mid"].iloc[-1])
        days  = (datetime.today()-datetime.strptime(entry_date,"%Y-%m-%d")).days
        pnl   = (c_now - entry_price) / entry_price
        if c_now > mid:
            return True, f"above_midline (${c_now:.2f}>${mid:.2f}, {pnl*100:+.1f}%)"
        if days >= EXIT_DAYS_MAX:
            return True, f"max_hold_{days}d ({pnl*100:+.1f}%)"
        if pnl <= EXIT_STOP_LOSS:
            return True, f"stop_loss ({pnl*100:.1f}%)"
        return False, ""
    except Exception: return False, ""


# ══════════════════════════════════════════════════════════════════════════════
#  PDT + POSITIONS + ORDERS
# ══════════════════════════════════════════════════════════════════════════════

def load_pdt():    return json.load(open(PDT_LOG))      if PDT_LOG.exists()      else []
def save_pdt(l):   json.dump(l, open(PDT_LOG,"w"))
def load_pos():    return json.load(open(POSITION_LOG)) if POSITION_LOG.exists() else {}
def save_pos(p):   json.dump(p, open(POSITION_LOG,"w"), indent=2)

def pdt_count(l):
    cutoff = date.today()-timedelta(days=7)
    return sum(1 for d in l if datetime.strptime(d,"%Y-%m-%d").date()>=cutoff)

def pdt_ok(l):
    n = pdt_count(l)
    if n>=MAX_DAY_TRADES:
        log.warning(f"PDT: {n}/{MAX_DAY_TRADES} used"); return False
    return True

def sync_pos(client, local):
    try:
        live    = {p.symbol for p in client.get_all_positions()}
        cleaned = {k:v for k,v in local.items() if k in live}
        dropped = set(local)-set(cleaned)
        if dropped: log.info(f"  Sync removed: {dropped}")
        return cleaned
    except Exception as e:
        log.warning(f"  Sync failed: {e}"); return local

def heat(positions, cash):
    return sum(p.get("dollar_amt",0) for p in positions.values()) / max(cash+sum(p.get("dollar_amt",0) for p in positions.values()),1)

def place_buy(client, ticker, dollars):
    try:
        order = client.submit_order(MarketOrderRequest(
            symbol=ticker, notional=round(dollars,2),
            side=OrderSide.BUY, time_in_force=TimeInForce.DAY))
        log.info(f"  BUY  {ticker:8s}  ${dollars:8.2f}  id={order.id}")
        return True
    except Exception as e:
        log.error(f"  BUY FAILED {ticker}: {e}"); return False

def place_sell(client, ticker):
    try:
        client.close_position(ticker)
        log.info(f"  SELL {ticker:8s}  closed"); return True
    except Exception as e:
        log.error(f"  SELL FAILED {ticker}: {e}"); return False


# ══════════════════════════════════════════════════════════════════════════════
#  CSV LOGGING
# ══════════════════════════════════════════════════════════════════════════════

TRADE_F = ["date","ticker","strategy","action","price","dollar_amount",
           "pnl_pct","pnl_dollar","hold_days","exit_reason",
           "rsi","vol_z","trigger","month","regime","equity","mode"]
SIG_F   = ["date","ticker","strategy","close","rsi","vol_z","trigger","month","regime"]

def _csv(path, fields, row):
    init = not path.exists()
    with open(path,"a",newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if init: w.writeheader()
        w.writerow({k:row.get(k,"") for k in fields})

def log_trade(r):  _csv(TRADE_LOG,  TRADE_F, r)
def log_signal(r): _csv(SIGNAL_LOG, SIG_F,   r)


# ══════════════════════════════════════════════════════════════════════════════
#  DISPLAY
# ══════════════════════════════════════════════════════════════════════════════

W = 72

def hdr(title=""):
    bar = "═"*W
    print(f"\n╔{bar}╗")
    if title:
        t  = f"  {title}  "
        lp = (W-len(t))//2; rp = W-len(t)-lp
        print(f"║{' '*lp}{t}{' '*max(0,rp)}║")
        print(f"╠{bar}╣")

def ftr():  print(f"╚{'═'*W}╝")
def div():  print(f"╠{'═'*W}╣")
def blank():print(f"║{' '*W}║")

def row(label, value=""):
    content = f"  {label:<36s}  {value}" if value else f"  {label}"
    pad = W-len(content)
    print(f"║{content}{' '*max(0,pad)}║")


# ══════════════════════════════════════════════════════════════════════════════
#  SHARED EXIT RUNNER  (used by both modes)
# ══════════════════════════════════════════════════════════════════════════════

def run_exits(client, positions, equity, regime, month):
    to_close = []
    pos_data = fetch_batch(list(positions.keys()), "positions")

    hdr("EXIT EVALUATION")
    for ticker, pos in positions.items():
        if ticker not in pos_data:
            row(f"{ticker:8s}", "no data — skipping"); continue
        df      = pos_data[ticker]
        ep      = pos["entry_price"]; ed = pos["entry_date"]
        c_now   = float(df["Close"].iloc[-1])
        pnl     = (c_now-ep)/ep
        days    = (datetime.today()-datetime.strptime(ed,"%Y-%m-%d")).days
        ex, why = check_exit(df, ep, ed)
        row(f"{ticker:8s}  ${ep:.2f}→${c_now:.2f}  {pnl*100:+.1f}%  {days}d",
            f"EXIT — {why}" if ex else "HOLD")
        if ex: to_close.append((ticker, why, c_now, pnl, days, pos))
    if not to_close: row("No exits triggered.")
    ftr()

    for ticker, why, c_now, pnl, days, pos in to_close:
        if place_sell(client, ticker):
            log_trade({"date":str(date.today()),"ticker":ticker,
                       "strategy":pos.get("strategy","?"),"action":"SELL",
                       "price":c_now,"dollar_amount":pos["dollar_amt"],
                       "pnl_pct":round(pnl*100,2),"pnl_dollar":round(pnl*pos["dollar_amt"],2),
                       "hold_days":days,"exit_reason":why,
                       "rsi":pos.get("rsi",""),"vol_z":pos.get("vol_z",""),
                       "trigger":pos.get("trigger",""),"month":month,"regime":regime,
                       "equity":round(equity,2),"mode":"paper" if PAPER_TRADING else "live"})
            del positions[ticker]

    save_pos(positions)
    return positions, len(to_close)


# ══════════════════════════════════════════════════════════════════════════════
#  MODE 1 — EXITS ONLY (9:35am ET)
# ══════════════════════════════════════════════════════════════════════════════

def run_exits_only():
    hdr(); row("RUBBER BAND BOT  v3  —  MORNING EXIT CHECK")
    div(); row("Mode", "PAPER" if PAPER_TRADING else "*** LIVE ***")
    row("Time", datetime.now().strftime("%H:%M:%S  —  9:35am exit scan")); ftr()

    if datetime.today().weekday() >= 5:
        log.info("Weekend."); return

    client    = get_client()
    acct      = client.get_account()
    equity    = float(acct.equity)
    positions = sync_pos(client, load_pos())

    if not positions:
        hdr("MORNING CHECK"); row("No open positions."); ftr(); return

    month  = date.today().month
    spy_raw = fetch_stock("SPY")
    spy_df  = add_indicators(spy_raw) if spy_raw else None
    regime  = detect_regime(spy_df)

    run_exits(client, positions, equity, regime, month)
    log.info("Morning exit check complete.")


# ══════════════════════════════════════════════════════════════════════════════
#  MODE 2 — FULL SCAN (4:15pm ET)
# ══════════════════════════════════════════════════════════════════════════════

def run_full_scan():
    month    = date.today().month
    sched    = SCHEDULE[month]

    hdr(); row("RUBBER BAND BOT  v3  —  DAILY SCAN")
    div()
    row("Mode",  "PAPER TRADING" if PAPER_TRADING else "*** LIVE TRADING ***")
    row("Date",  f"{date.today()}   {datetime.now().strftime('%H:%M:%S')}")
    row("Month strategy", sched["note"]); ftr()

    if datetime.today().weekday() >= 5:
        log.info("Weekend."); return

    client  = get_client()
    acct    = client.get_account()
    equity  = float(acct.equity)
    cash    = float(acct.cash)

    hdr("ACCOUNT")
    row("Equity", f"${equity:>12,.2f}"); row("Cash", f"${cash:>12,.2f}"); ftr()

    pdt       = load_pdt()
    positions = sync_pos(client, load_pos())

    hdr("PORTFOLIO STATE")
    row("Open positions",  f"{len(positions)}  {list(positions.keys())}")
    row("PDT trades used", f"{pdt_count(pdt)}/{MAX_DAY_TRADES}")
    row("Portfolio heat",  f"{heat(positions,cash)*100:.1f}%"); ftr()

    # Universe
    all_tickers = get_live_tickers()

    # SPY regime
    spy_raw = fetch_stock("SPY")
    spy_df = add_indicators(spy_raw) if spy_raw is not None and not spy_raw.empty else None
    regime  = detect_regime(spy_df)
    spy_now   = float(spy_df["Close"].iloc[-1])  if spy_df is not None else 0
    spy_ma200 = float(spy_df["MA200"].iloc[-1])  if spy_df is not None else 0

    hdr("MARKET REGIME")
    row("SPY", f"${spy_now:,.2f}  |  200MA ${spy_ma200:,.2f}  |  ratio {spy_now/max(spy_ma200,1)*100:.1f}%")
    div()
    row("Regime",           regime.upper())
    row("Primary strategy", sched["primary"])
    row("Secondary",        sched["secondary"]); ftr()

    # Exit check first (on held stocks only — fast)
    if positions:
        positions, _ = run_exits(client, positions, equity, regime, month)

    # Full universe scan
    hdr("DATA DOWNLOAD")
    row(f"Scanning {len(all_tickers)} stocks  (S&P 500 + MidCap 400)")
    row("Takes ~10-15 min. Progress every 40 stocks."); ftr()

    scan_tickers = [t for t in all_tickers if t not in positions]
    all_data     = fetch_batch(scan_tickers, "universe")

    # Signal scan
    hdr("SIGNAL SCAN")
    row(f"Month: {date.today().strftime('%B')}  |  Regime: {regime.upper()}")
    row(f"Primary: {sched['primary']}  |  Secondary: {sched['secondary']}"); ftr()

    all_sigs = []
    for ticker, df in all_data.items():
        for s in get_signals(ticker, df, month, regime):
            s["month"] = month; s["regime"] = regime
            all_sigs.append(s); log_signal(s)

    hdr(f"SIGNALS  —  {len(all_sigs)} found")
    if not all_sigs:
        blank(); row("No signals today.")
        blank(); row(sched["note"]); blank()
    else:
        div()
        row(f"  {'Ticker':<8}  {'Strategy':<16}  {'Price':>7}  {'RSI':>5}  {'Vol_Z':>6}  Trigger")
        div()
        for s in all_sigs:
            row(f"  {s['ticker']:<8}  {s['strategy']:<16}  ${s['close']:>6.2f}"
                f"  {s.get('rsi',0):>5.1f}  {s.get('vol_z',0):>6.2f}  {s.get('trigger','')}")
        blank()
    ftr()

    # Entries
    hdr("ENTRY ORDERS")
    cash    = float(client.get_account().cash)
    entries = 0

    for sig in all_sigs:
        ticker = sig["ticker"]
        ph     = heat(positions, cash)
        skip   = ""
        if len(positions) >= MAX_OPEN_POSITIONS: skip = "max positions"
        elif ph           >= MAX_PORTFOLIO_HEAT: skip = f"heat {ph*100:.0f}%"
        elif not pdt_ok(pdt):                    skip = "PDT limit"
        dollar_amt = equity * POSITION_SIZE_PCT
        if not skip:
            if dollar_amt < 1.0:           skip = "size < $1"
            elif dollar_amt > cash * 0.95: skip = f"low cash ${cash:.0f}"

        if skip:
            row(f"  SKIP  {ticker:<8}  {sig['strategy']:<16}", skip); continue

        row(f"  ENTER {ticker:<8}  {sig['strategy']:<16}  ${dollar_amt:.2f}")
        if place_buy(client, ticker, dollar_amt):
            positions[ticker] = {"entry_price":sig["close"],"entry_date":str(date.today()),
                                  "dollar_amt":round(dollar_amt,2),"strategy":sig["strategy"],
                                  "rsi":sig.get("rsi",""),"vol_z":sig.get("vol_z",""),
                                  "trigger":sig.get("trigger",""),"regime":regime,"month":month}
            log_trade({"date":str(date.today()),"ticker":ticker,"strategy":sig["strategy"],
                       "action":"BUY","price":sig["close"],"dollar_amount":round(dollar_amt,2),
                       "pnl_pct":0,"pnl_dollar":0,"hold_days":0,
                       "rsi":sig.get("rsi",""),"vol_z":sig.get("vol_z",""),
                       "trigger":sig.get("trigger",""),"month":month,"regime":regime,
                       "equity":round(equity,2),"mode":"paper" if PAPER_TRADING else "live"})
            cash -= dollar_amt; entries += 1
        if len(positions) >= MAX_OPEN_POSITIONS: break

    if entries == 0 and not all_sigs: row("  No entries placed.")
    ftr()

    save_pos(positions); save_pdt(pdt)

    hdr("SESSION SUMMARY")
    row("Regime",         regime.upper())
    row("Month strategy", f"{sched['primary']} + {sched['secondary']}")
    row("Stocks scanned", str(len(all_data)))
    row("Signals found",  str(len(all_sigs)))
    row("Entries placed", str(entries))
    row("Open positions", str(list(positions.keys())))
    row("Cash remaining", f"${float(client.get_account().cash):,.2f}")
    row("Logs",           str(LOG_DIR.absolute())); ftr()


# ══════════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rubber Band Bot v3")
    parser.add_argument("--mode", choices=["scan","exits"], default="scan",
                        help="scan=full 4:15pm run | exits=morning 9:35am check")
    args = parser.parse_args()

    if args.mode == "exits":
        run_exits_only()
    else:
        run_full_scan()
