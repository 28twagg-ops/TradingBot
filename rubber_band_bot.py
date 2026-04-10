"""
╔══════════════════════════════════════════════════════════════════════════╗
║         RUBBER BAND BOT  v2  —  Year-Round Multi-Strategy             ║
║                                                                        ║
║  4 strategies, automatic regime detection, year-round signal flow     ║
║  Broker: Alpaca Markets  |  paper=True → flip to False for live       ║
║  Schedule: run daily at 4:15 pm ET via Task Scheduler / cron         ║
╚══════════════════════════════════════════════════════════════════════════╝

SETUP:
    pip install alpaca-py yfinance pandas numpy

RUN:
    python rubber_band_bot.py

LIVE:
    Set PAPER_TRADING = False and swap in your live API keys.
    Everything else stays the same.
"""

import json, time, logging, csv
from datetime import datetime, timedelta, date
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

from alpaca.trading.client   import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums    import OrderSide, TimeInForce


# ══════════════════════════════════════════════════════════════════════════════
#  CONFIGURATION — edit before running
# ══════════════════════════════════════════════════════════════════════════════

API_KEY    = "PASTE_YOUR_API_KEY_HERE"
API_SECRET = "PASTE_YOUR_SECRET_KEY_HERE"

PAPER_TRADING      = True    # True = paper (safe). False = LIVE real money.

POSITION_SIZE_PCT  = 0.02    # 2% of equity per trade
MAX_OPEN_POSITIONS = 2
MAX_PORTFOLIO_HEAT = 0.40    # max 40% capital deployed

EXIT_DAYS_MAX  = 7           # hard exit after N calendar days
EXIT_STOP_LOSS = -0.03       # stop loss at -3%

MAX_DAY_TRADES = 3           # PDT rule limit
MIN_STOCK_PRICE  = 5.0
MIN_HISTORY_DAYS = 220

LOG_DIR      = Path("logs")
TRADE_LOG    = LOG_DIR / "trades.csv"
PDT_LOG      = LOG_DIR / "pdt_ledger.json"
SIGNAL_LOG   = LOG_DIR / "signals.csv"
POSITION_LOG = LOG_DIR / "open_positions.json"


# ══════════════════════════════════════════════════════════════════════════════
#  STRATEGY PARAMETER SETS  (auto-selected by regime)
# ══════════════════════════════════════════════════════════════════════════════

BULL_PARAMS = {
    "consec_down": 5, "rsi_thresh": 25, "bb_std": 2.5,
    "vol_z_min": 1.5, "require_ma200": True,
}
CORRECTION_PARAMS = {
    "consec_down": 3, "rsi_thresh": 30, "bb_std": 2.0,
    "vol_z_min": 0.5, "require_ma200": False,
}
BEAR_PARAMS = {
    "consec_down": 5, "rsi_thresh": 20, "bb_std": 2.5,
    "vol_z_min": 1.0, "require_ma200": False,
}


# ══════════════════════════════════════════════════════════════════════════════
#  TICKER UNIVERSE
# ══════════════════════════════════════════════════════════════════════════════

def get_live_tickers() -> list:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        sp500 = pd.read_html(
            "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
            storage_options=headers)[0]["Symbol"].tolist()
        mid400 = pd.read_html(
            "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies",
            storage_options=headers)[0]["Symbol"].tolist()
        tickers = sp500 + mid400
    except Exception:
        tickers = [
            "AAPL","MSFT","NVDA","AMD","INTC","ADBE","CRM","CSCO","TXN","QCOM",
            "GOOGL","META","NFLX","DIS","CMCSA","T","VZ","JPM","BAC","GS","MS",
            "V","MA","AXP","C","WFC","JNJ","PFE","UNH","ABBV","TMO","ABT","LLY",
            "MRK","AMZN","TSLA","HD","MCD","NKE","COST","WMT","PG","KO","PEP",
            "BA","CAT","HON","GE","UPS","LMT","RTX","DE","MMM","XOM","CVX","COP",
            "SLB","OXY","NEE","DUK","SO","NEM","FCX","PLTR","COIN",
        ]
    return [t.replace(".", "-") for t in tickers]


# ══════════════════════════════════════════════════════════════════════════════
#  LOGGING SETUP
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
log = logging.getLogger("RBBot")


# ══════════════════════════════════════════════════════════════════════════════
#  ALPACA
# ══════════════════════════════════════════════════════════════════════════════

def get_client() -> TradingClient:
    if "PASTE" in API_KEY:
        log.error("Set API_KEY and API_SECRET at the top of this file first.")
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
    df["RSI"]       = 100 - 100 / (1 + g / (l + 1e-10))
    df["BB_Lower"]  = c.rolling(20).mean() - 2.5 * c.rolling(20).std()
    df["BB_Lower2"] = c.rolling(20).mean() - 2.0 * c.rolling(20).std()
    df["BB_Mid"]    = c.rolling(20).mean()
    avg = v.rolling(20).mean(); std = v.rolling(20).std()
    df["Vol_Z"]     = (v - avg) / (std + 1e-10)
    df["MA20"]      = c.rolling(20).mean()
    df["MA50"]      = c.rolling(50).mean()
    df["MA150"]     = c.rolling(150).mean()
    df["MA200"]     = c.rolling(200).mean()
    df["Low252"]    = c.rolling(252).min()
    df["Ret60"]     = c.pct_change(60)
    return df


def fetch_all(tickers: list) -> dict:
    data = {}
    batch = 40
    for i in range(0, len(tickers), batch):
        chunk = tickers[i:i+batch]
        for t in chunk:
            df = fetch_stock(t)
            if df is not None:
                data[t] = add_indicators(df)
        log.info(f"  data  {min(i+batch,len(tickers))}/{len(tickers)}  "
                 f"({len(data)} valid)")
        time.sleep(1.5)
    return data


# ══════════════════════════════════════════════════════════════════════════════
#  REGIME DETECTION
# ══════════════════════════════════════════════════════════════════════════════

def detect_regime(spy_df: pd.DataFrame | None) -> str:
    if spy_df is None or len(spy_df) < 210:
        return "bull"
    ma200 = float(spy_df["Close"].rolling(200).mean().iloc[-1])
    c_now = float(spy_df["Close"].iloc[-1])
    ratio = c_now / (ma200 + 1e-10)
    if ratio >= 1.00: return "bull"
    if ratio >= 0.93: return "correction"
    return "bear"


def consec_down(close: pd.Series) -> int:
    vals = close.values
    n = 0
    for i in range(len(vals)-1, 0, -1):
        if vals[i] < vals[i-1]: n += 1
        else: break
    return n


# ══════════════════════════════════════════════════════════════════════════════
#  STRATEGY SIGNALS
# ══════════════════════════════════════════════════════════════════════════════

def sig_rubber_band(ticker: str, df: pd.DataFrame, params: dict) -> dict | None:
    """
    Rubber Band Snap — validated 23-yr backtest: OOS +0.91%, Sharpe 1.40.
    Strict in bull, relaxed (no MA200 gate) in correction.
    """
    try:
        c     = df["Close"]
        c_now = float(c.iloc[-1])
        rsi_v = float(df["RSI"].iloc[-1])
        bb_col= "BB_Lower" if params["bb_std"] >= 2.4 else "BB_Lower2"
        bb_v  = float(df[bb_col].iloc[-1])
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
            return {"ticker": ticker, "strategy": "RubberBand",
                    "date": str(date.today()), "close": round(c_now, 2),
                    "rsi": round(rsi_v, 1), "vol_z": round(vz_v, 2),
                    "trigger": "RSI" if rsi_v < params["rsi_thresh"]
                                else f"{cd}d-down"}
        return None
    except Exception:
        return None


def sig_52wk_low(ticker: str, df: pd.DataFrame) -> dict | None:
    """
    52-Week Low Reversal — #1 in 23-yr backtest: OOS +0.99%, Sharpe 0.96,
    NEGATIVE degradation. Works in any regime.
    """
    try:
        c_now = float(df["Close"].iloc[-1])
        low52 = float(df["Low252"].iloc[-1])
        rsi_v = float(df["RSI"].iloc[-1])
        vz_v  = float(df["Vol_Z"].iloc[-1])

        if any(pd.isna(x) for x in [low52, rsi_v]):
            return None

        if (c_now <= low52 * 1.05) and (vz_v >= 0.5) and (rsi_v > 10):
            return {"ticker": ticker, "strategy": "52wkLow",
                    "date": str(date.today()), "close": round(c_now, 2),
                    "rsi": round(rsi_v, 1), "vol_z": round(vz_v, 2),
                    "trigger": f"{((c_now/low52)-1)*100:.1f}% above 52wk low"}
        return None
    except Exception:
        return None


def sig_momentum_reversal(ticker: str, df: pd.DataFrame) -> dict | None:
    """
    Momentum Reversal (60-day contrarian) — OOS +0.62%, Sharpe 0.84,
    negative degradation. Fires after 12%+ drop + stabilisation.
    Best in corrections and Sept-Oct recovery periods.
    """
    try:
        c     = df["Close"]
        c_now = float(c.iloc[-1])
        ret60 = float(df["Ret60"].iloc[-1])
        ret5  = float(c.pct_change(5).iloc[-1])
        rsi_v = float(df["RSI"].iloc[-1])
        vz_v  = float(df["Vol_Z"].iloc[-1])

        if any(pd.isna(x) for x in [ret60, ret5, rsi_v]):
            return None

        if (ret60 < -0.12) and (ret5 > -0.02) and (rsi_v < 40) and (vz_v >= 0.3):
            return {"ticker": ticker, "strategy": "MomReversal",
                    "date": str(date.today()), "close": round(c_now, 2),
                    "rsi": round(rsi_v, 1), "vol_z": round(vz_v, 2),
                    "trigger": f"{ret60*100:.1f}% drop/60d"}
        return None
    except Exception:
        return None


def sig_golden_cross(ticker: str, df: pd.DataFrame) -> dict | None:
    """
    Golden Cross — 50MA crosses above 200MA. Bull-market trend-following.
    Secondary signal; fires rarely but catches strong breakouts.
    """
    try:
        c_now  = float(df["Close"].iloc[-1])
        ma50   = float(df["MA50"].iloc[-1])
        ma200  = float(df["MA200"].iloc[-1])
        ma50_p = float(df["MA50"].iloc[-2])
        ma200_p= float(df["MA200"].iloc[-2])

        if any(pd.isna(x) for x in [ma50, ma200, ma50_p, ma200_p]):
            return None

        if (ma50 > ma200) and (ma50_p <= ma200_p):
            return {"ticker": ticker, "strategy": "GoldenCross",
                    "date": str(date.today()), "close": round(c_now, 2),
                    "rsi": 0.0, "vol_z": 0.0,
                    "trigger": "50MA x above 200MA"}
        return None
    except Exception:
        return None


# ══════════════════════════════════════════════════════════════════════════════
#  REGIME ROUTER
# ══════════════════════════════════════════════════════════════════════════════

def get_signals(ticker: str, df: pd.DataFrame, regime: str) -> list:
    """
    Routes each ticker through the correct strategy set for the regime.

    BULL:        RubberBand (strict) + 52wkLow + GoldenCross
    CORRECTION:  RubberBand (relaxed, no MA200) + 52wkLow + MomReversal
    BEAR:        52wkLow + MomReversal  (RubberBand disabled)
    """
    sigs = []
    if regime == "bull":
        for fn in [
            lambda t, d: sig_rubber_band(t, d, BULL_PARAMS),
            sig_52wk_low,
            sig_golden_cross,
        ]:
            s = fn(ticker, df)
            if s: sigs.append(s)

    elif regime == "correction":
        for fn in [
            lambda t, d: sig_rubber_band(t, d, CORRECTION_PARAMS),
            sig_52wk_low,
            sig_momentum_reversal,
        ]:
            s = fn(ticker, df)
            if s: sigs.append(s)

    else:  # bear
        for fn in [sig_52wk_low, sig_momentum_reversal]:
            s = fn(ticker, df)
            if s: sigs.append(s)

    return sigs


# ══════════════════════════════════════════════════════════════════════════════
#  EXIT LOGIC
# ══════════════════════════════════════════════════════════════════════════════

def check_exit(df: pd.DataFrame, entry_price: float,
               entry_date: str) -> tuple[bool, str]:
    try:
        c_now = float(df["Close"].iloc[-1])
        mid   = float(df["BB_Mid"].iloc[-1])
        days  = (datetime.today() -
                 datetime.strptime(entry_date, "%Y-%m-%d")).days
        pnl   = (c_now - entry_price) / entry_price

        if c_now > mid:
            return True, f"above_midline (${c_now:.2f} > MA20 ${mid:.2f}, {pnl*100:+.1f}%)"
        if days >= EXIT_DAYS_MAX:
            return True, f"max_hold_{days}d ({pnl*100:+.1f}%)"
        if pnl <= EXIT_STOP_LOSS:
            return True, f"stop_loss ({pnl*100:.1f}%)"
        return False, ""
    except Exception:
        return False, ""


# ══════════════════════════════════════════════════════════════════════════════
#  PDT
# ══════════════════════════════════════════════════════════════════════════════

def load_pdt():
    return json.load(open(PDT_LOG)) if PDT_LOG.exists() else []

def save_pdt(l):
    json.dump(l, open(PDT_LOG,"w"))

def pdt_count(l):
    cutoff = date.today() - timedelta(days=7)
    return sum(1 for d in l if datetime.strptime(d,"%Y-%m-%d").date() >= cutoff)

def pdt_ok(l):
    n = pdt_count(l)
    if n >= MAX_DAY_TRADES:
        log.warning(f"PDT limit: {n}/{MAX_DAY_TRADES}")
        return False
    return True


# ══════════════════════════════════════════════════════════════════════════════
#  POSITIONS
# ══════════════════════════════════════════════════════════════════════════════

def load_positions():
    return json.load(open(POSITION_LOG)) if POSITION_LOG.exists() else {}

def save_positions(p):
    json.dump(p, open(POSITION_LOG,"w"), indent=2)

def sync_positions(client, local):
    try:
        live    = {p.symbol for p in client.get_all_positions()}
        cleaned = {k: v for k, v in local.items() if k in live}
        dropped = set(local) - set(cleaned)
        if dropped: log.info(f"  sync: removed stale {dropped}")
        return cleaned
    except Exception as e:
        log.warning(f"  sync failed: {e}")
        return local

def heat(positions, cash):
    deployed = sum(p.get("dollar_amt",0) for p in positions.values())
    return deployed / max(cash + deployed, 1)


# ══════════════════════════════════════════════════════════════════════════════
#  ORDERS
# ══════════════════════════════════════════════════════════════════════════════

def place_buy(client, ticker, dollars):
    try:
        order = client.submit_order(MarketOrderRequest(
            symbol=ticker, notional=round(dollars, 2),
            side=OrderSide.BUY, time_in_force=TimeInForce.DAY))
        log.info(f"  BUY   {ticker:8s}  ${dollars:8.2f}  id={order.id}")
        return True
    except Exception as e:
        log.error(f"  BUY FAILED {ticker}: {e}")
        return False

def place_sell(client, ticker):
    try:
        client.close_position(ticker)
        log.info(f"  SELL  {ticker:8s}  closed")
        return True
    except Exception as e:
        log.error(f"  SELL FAILED {ticker}: {e}")
        return False


# ══════════════════════════════════════════════════════════════════════════════
#  LOGGING TO CSV
# ══════════════════════════════════════════════════════════════════════════════

TRADE_F = ["date","ticker","strategy","action","price","dollar_amount",
           "pnl_pct","pnl_dollar","hold_days","exit_reason",
           "rsi","vol_z","trigger","regime","equity","mode"]

SIG_F   = ["date","ticker","strategy","close","rsi","vol_z","trigger","regime"]

def _csv(path, fields, row):
    init = not path.exists()
    with open(path,"a",newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if init: w.writeheader()
        w.writerow({k: row.get(k,"") for k in fields})

def log_trade(r):   _csv(TRADE_LOG, TRADE_F, r)
def log_signal(r):  _csv(SIGNAL_LOG, SIG_F,  r)


# ══════════════════════════════════════════════════════════════════════════════
#  DISPLAY HELPERS  (clean box-drawing UI)
# ══════════════════════════════════════════════════════════════════════════════

W = 70

def hdr(title=""):
    bar = "═" * W
    if title:
        t   = f"  {title}  "
        lp  = (W - len(t)) // 2
        rp  = W - len(t) - lp
        print(f"\n╔{bar}╗")
        print(f"║{' '*lp}{t}{' '*rp}║")
        print(f"╠{bar}╣")
    else:
        print(f"\n╔{bar}╗")

def ftr():
    print(f"╚{'═'*W}╝")

def row(label, value=""):
    if value:
        content = f"  {label:<34s}  {value}"
    else:
        content = f"  {label}"
    pad = W - len(content)
    print(f"║{content}{' '*max(0,pad)}║")

def div():
    print(f"╠{'═'*W}╣")

def blank():
    print(f"║{' '*W}║")


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════════

def run():

    hdr()
    row("RUBBER BAND BOT  v2  —  Year-Round Multi-Strategy")
    div()
    row("Mode",  "PAPER TRADING" if PAPER_TRADING else "*** LIVE TRADING ***")
    row("Date",  f"{date.today()}   {datetime.now().strftime('%H:%M:%S')}")
    ftr()

    if datetime.today().weekday() >= 5:
        log.info("Weekend — markets closed. Exiting.")
        return

    # ── Alpaca ────────────────────────────────────────────────────────────────
    client  = get_client()
    acct    = client.get_account()
    equity  = float(acct.equity)
    cash    = float(acct.cash)

    hdr("ACCOUNT")
    row("Equity",  f"${equity:>12,.2f}")
    row("Cash",    f"${cash:>12,.2f}")
    ftr()

    # ── State ─────────────────────────────────────────────────────────────────
    pdt       = load_pdt()
    positions = sync_positions(client, load_positions())
    ph        = heat(positions, cash)

    hdr("PORTFOLIO STATE")
    row("Open positions", f"{len(positions)}  {list(positions.keys())}")
    row("PDT trades used", f"{pdt_count(pdt)}/{MAX_DAY_TRADES}")
    row("Portfolio heat",  f"{ph*100:.1f}%")
    ftr()

    # ── Download data ─────────────────────────────────────────────────────────
    hdr("DATA DOWNLOAD")
    row("Fetching live S&P 500 + MidCap 400 ticker list...")
    ftr()

    all_tickers = list(set(get_live_tickers() + list(positions.keys())))
    all_data    = {}
    spy_df      = None

    # Fetch SPY first for regime detection
    spy_raw = fetch_stock("SPY")
    if spy_raw is not None:
        spy_df = add_indicators(spy_raw)

    log.info(f"Downloading {len(all_tickers)} stocks...")
    batch = 40
    for i in range(0, len(all_tickers), batch):
        chunk = all_tickers[i:i+batch]
        for t in chunk:
            df = fetch_stock(t)
            if df is not None:
                all_data[t] = add_indicators(df)
        log.info(f"  {min(i+batch,len(all_tickers))}/{len(all_tickers)} "
                 f"fetched  ({len(all_data)} valid)")
        time.sleep(1.5)

    log.info(f"Download complete — {len(all_data)} stocks ready")

    # ── Regime ────────────────────────────────────────────────────────────────
    regime    = detect_regime(spy_df)
    spy_now   = float(spy_df["Close"].iloc[-1]) if spy_df is not None else 0
    spy_ma200 = float(spy_df["MA200"].iloc[-1]) if spy_df is not None else 0

    REGIME_DESC = {
        "bull":       "RubberBand (strict) + 52wkLow + GoldenCross",
        "correction": "RubberBand (relaxed, no MA200) + 52wkLow + MomReversal",
        "bear":       "52wkLow + MomReversal only  (capital preservation)",
    }

    hdr("MARKET REGIME")
    row("SPY price",          f"${spy_now:,.2f}")
    row("SPY 200-day MA",     f"${spy_ma200:,.2f}")
    row("Ratio",              f"{spy_now/max(spy_ma200,1)*100:.1f}% of 200MA")
    div()
    row("Regime detected",    regime.upper())
    row("Active strategies",  REGIME_DESC[regime])
    ftr()

    # ── Exits ─────────────────────────────────────────────────────────────────
    hdr("EXIT EVALUATION")
    to_close = []
    for ticker, pos in positions.items():
        if ticker not in all_data:
            row(f"{ticker:8s}", "no data — skipping")
            continue
        df    = all_data[ticker]
        ep    = pos["entry_price"]
        ed    = pos["entry_date"]
        c_now = float(df["Close"].iloc[-1])
        pnl   = (c_now - ep) / ep
        days  = (datetime.today() - datetime.strptime(ed,"%Y-%m-%d")).days
        ex, why = check_exit(df, ep, ed)
        status = f"EXIT — {why}" if ex else "HOLD"
        row(f"{ticker:8s}  entry=${ep:.2f}  now=${c_now:.2f}  "
            f"P&L={pnl*100:+.1f}%  {days}d held", status)
        if ex:
            to_close.append((ticker, why, c_now, pnl, days, pos))
    if not to_close:
        row("No exits triggered today.")
    ftr()

    for ticker, why, c_now, pnl, days, pos in to_close:
        if place_sell(client, ticker):
            log_trade({
                "date": str(date.today()), "ticker": ticker,
                "strategy": pos.get("strategy","?"), "action": "SELL",
                "price": c_now, "dollar_amount": pos["dollar_amt"],
                "pnl_pct": round(pnl*100,2),
                "pnl_dollar": round(pnl*pos["dollar_amt"],2),
                "hold_days": days, "exit_reason": why,
                "rsi": pos.get("rsi",""), "vol_z": pos.get("vol_z",""),
                "trigger": pos.get("trigger",""),
                "regime": pos.get("regime_at_entry",""),
                "equity": round(equity,2),
                "mode": "paper" if PAPER_TRADING else "live",
            })
            del positions[ticker]

    save_positions(positions)

    # ── Signal scan ───────────────────────────────────────────────────────────
    hdr("SIGNAL SCAN")
    row(f"Scanning {len(all_data)} stocks", f"regime: {regime.upper()}")
    ftr()

    all_sigs = []
    for ticker, df in all_data.items():
        if ticker in positions:
            continue
        for s in get_signals(ticker, df, regime):
            s["regime"] = regime
            all_sigs.append(s)
            log_signal(s)

    hdr(f"SIGNALS FOUND  —  {len(all_sigs)} total")
    if not all_sigs:
        blank()
        row("No signals detected today.")
        blank()
        if regime == "correction":
            row("CORRECTION regime: relaxed params active.")
            row("Signals fire when individual stocks show oversold + stabilisation.")
        elif regime == "bear":
            row("BEAR regime: only 52wkLow + MomReversal active.")
            row("Capital preservation mode. Waiting for extreme setups.")
        else:
            row("BULL regime: strict Rubber Band params.")
            row("Signals are rare but high-quality when they appear.")
        blank()
    else:
        div()
        row(f"  {'Ticker':<8}  {'Strategy':<16}  {'Price':>7}  "
            f"{'RSI':>5}  {'Vol_Z':>6}  Trigger")
        div()
        for s in all_sigs:
            row(f"  {s['ticker']:<8}  {s['strategy']:<16}  "
                f"${s['close']:>6.2f}  {s.get('rsi',0):>5.1f}  "
                f"{s.get('vol_z',0):>6.2f}  {s.get('trigger','')}")
        blank()
    ftr()

    # ── Entries ───────────────────────────────────────────────────────────────
    hdr("ENTRY ORDERS")
    cash    = float(client.get_account().cash)
    ph      = heat(positions, cash)
    entries = 0

    for sig in all_sigs:
        ticker = sig["ticker"]
        skip   = ""
        if len(positions) >= MAX_OPEN_POSITIONS: skip = "max positions"
        elif ph           >= MAX_PORTFOLIO_HEAT:  skip = f"heat {ph*100:.0f}%"
        elif not pdt_ok(pdt):                     skip = "PDT limit"

        dollar_amt = equity * POSITION_SIZE_PCT
        if not skip:
            if dollar_amt < 1.0:            skip = "size too small"
            elif dollar_amt > cash * 0.95:  skip = f"low cash ${cash:.0f}"

        if skip:
            row(f"  SKIP  {ticker:<8}  {sig['strategy']:<16}", skip)
            continue

        row(f"  ENTER {ticker:<8}  {sig['strategy']:<16}  ${dollar_amt:.2f}")
        if place_buy(client, ticker, dollar_amt):
            positions[ticker] = {
                "entry_price": sig["close"], "entry_date": str(date.today()),
                "dollar_amt":  round(dollar_amt,2), "strategy": sig["strategy"],
                "rsi":         sig.get("rsi",""), "vol_z": sig.get("vol_z",""),
                "trigger":     sig.get("trigger",""), "regime_at_entry": regime,
            }
            log_trade({
                "date": str(date.today()), "ticker": ticker,
                "strategy": sig["strategy"], "action": "BUY",
                "price": sig["close"], "dollar_amount": round(dollar_amt,2),
                "pnl_pct": 0, "pnl_dollar": 0, "hold_days": 0,
                "rsi": sig.get("rsi",""), "vol_z": sig.get("vol_z",""),
                "trigger": sig.get("trigger",""), "regime": regime,
                "equity": round(equity,2),
                "mode": "paper" if PAPER_TRADING else "live",
            })
            cash -= dollar_amt
            ph    = heat(positions, cash)
            entries += 1
        if len(positions) >= MAX_OPEN_POSITIONS:
            break

    if entries == 0 and not all_sigs:
        row("No entries placed.")
    ftr()

    save_positions(positions)
    save_pdt(pdt)

    # ── Summary ───────────────────────────────────────────────────────────────
    cash_final = float(client.get_account().cash)

    hdr("SESSION SUMMARY")
    row("Regime",         regime.upper())
    row("Signals found",  str(len(all_sigs)))
    row("Entries placed", str(entries))
    row("Exits placed",   str(len(to_close)))
    row("Open positions", str(list(positions.keys())))
    row("Cash remaining", f"${cash_final:,.2f}")
    row("Logs folder",    str(LOG_DIR.absolute()))
    ftr()


if __name__ == "__main__":
    run()
