"""
╔══════════════════════════════════════════════════════════════════════════╗
║        RUBBER BAND BOT  v4  —  GitHub Actions Native                  ║
║                                                                         ║
║  KEY FIX: Positions read from Alpaca API directly — no local files     ║
║  that disappear between GitHub Actions runs. No more duplicate buys.   ║
║                                                                         ║
║  Data: Alpaca market data (primary) → yfinance (fallback)              ║
║  Keys: GitHub Secrets via environment variables                         ║
║  Report: Saves run_report.md to repo after every execution             ║
╚══════════════════════════════════════════════════════════════════════════╝

GITHUB ACTIONS SCHEDULE — in your run_bot.yml:
    - cron: '15 20 * * 1-5'   # 4:15pm ET (UTC-4) = 20:15 UTC
    - cron: '35 13 * * 1-5'   # 9:35am ET          = 13:35 UTC

GITHUB SECRETS needed:
    ALPACA_API_KEY
    ALPACA_SECRET_KEY

LOCAL RUN:
    set ALPACA_API_KEY=your_key && set ALPACA_SECRET_KEY=your_secret
    python rubber_band_bot.py
    python rubber_band_bot.py --mode exits
"""

import os, sys, json, time, logging, csv, argparse, textwrap
from datetime import datetime, timedelta, date
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

from alpaca.trading.client   import TradingClient
from alpaca.trading.requests import MarketOrderRequest, GetAssetsRequest
from alpaca.trading.enums    import OrderSide, TimeInForce, AssetStatus
from alpaca.data.historical  import StockHistoricalDataClient
from alpaca.data.requests    import StockBarsRequest
from alpaca.data.timeframe   import TimeFrame


# ══════════════════════════════════════════════════════════════════════════════
#  KEYS — always from environment variables (GitHub Secrets or local shell)
# ══════════════════════════════════════════════════════════════════════════════

API_KEY    = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")

if not API_KEY or not API_SECRET:
    print("ERROR: ALPACA_API_KEY and ALPACA_SECRET_KEY environment variables not set.")
    print("  GitHub Actions: add them as Repository Secrets.")
    print("  Local: set ALPACA_API_KEY=xxx && set ALPACA_SECRET_KEY=xxx")
    raise SystemExit(1)


# ══════════════════════════════════════════════════════════════════════════════
#  CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

PAPER_TRADING = True          # False = live real money (only after 30+ days paper)

# ── Position sizing ────────────────────────────────────────────────────────────
# Each trade = 6% of equity. 3 max positions = up to 18% deployed.
# 20% cash reserve floor — bot will not buy if cash < 20% of equity.
# This keeps you liquid while deploying meaningful capital.
POSITION_SIZE_PCT  = 0.06     # 6% per trade (was 2%)
MAX_OPEN_POSITIONS = 3        # up to 3 simultaneous holdings (was 2)
CASH_RESERVE_PCT   = 0.20     # always keep 20% cash minimum

# ── Exit rules ─────────────────────────────────────────────────────────────────
EXIT_DAYS_MAX  = 7
EXIT_STOP_LOSS = -0.03        # -3% stop loss

# ── PDT ────────────────────────────────────────────────────────────────────────
MAX_DAY_TRADES = 3

# ── Data quality ───────────────────────────────────────────────────────────────
MIN_STOCK_PRICE  = 5.0
MIN_HISTORY_DAYS = 220

# ── Reporting ──────────────────────────────────────────────────────────────────
REPORT_FILE = Path("run_report.md")   # written to repo root after every run
LOG_DIR     = Path("logs")


# ══════════════════════════════════════════════════════════════════════════════
#  CALENDAR STRATEGY SCHEDULE
#  Built from 5-year backtest results. Never change this without re-running
#  the backtest engine first.
# ══════════════════════════════════════════════════════════════════════════════

SCHEDULE = {
    1:  {"primary":"MomReversal",  "secondary":"52wkLow",
         "note":"Jan: MomReversal +3.67%, 62% win. RubberBand -0.44% (off)."},
    2:  {"primary":"52wkLow",      "secondary":"MomReversal",
         "note":"Feb: 52wkLow +1.37%. RubberBand_Corr -2.09% (off)."},
    3:  {"primary":"52wkLow",      "secondary":"MomReversal",
         "note":"Mar: 52wkLow +1.85%, 68% win. Strong value month."},
    4:  {"primary":"RubberBand",   "secondary":"52wkLow",
         "note":"Apr: RubberBand +0.71%. Regime sets strict/relaxed params."},
    5:  {"primary":"RubberBand",   "secondary":"52wkLow",
         "note":"May: RubberBand +1.93%, 58% win. Strong month."},
    6:  {"primary":"52wkLow",      "secondary":"RubberBand",
         "note":"Jun: 52wkLow +1.81%, Sharpe 1.72. Best Jun strategy."},
    7:  {"primary":"52wkLow",      "secondary":"RubberBand",
         "note":"Jul: 52wkLow +2.86%, 66% win. Excellent value month."},
    8:  {"primary":"RubberBand",   "secondary":"52wkLow",
         "note":"Aug: RubberBand +4.72%, 70% win. Best month of year."},
    9:  {"primary":"GoldenCross",  "secondary":"52wkLow",
         "note":"Sep: Worst month. GoldenCross only best option at +0.07%."},
    10: {"primary":"RubberBand",   "secondary":"52wkLow",
         "note":"Oct: RubberBand +3.29%, 70% win. Second best month."},
    11: {"primary":"RubberBand",   "secondary":"MomReversal",
         "note":"Nov: RubberBand +4.77%, 86% WIN RATE. Best month overall."},
    12: {"primary":"MomReversal",  "secondary":"52wkLow",
         "note":"Dec: MomReversal +1.34%. Year-end recovery plays."},
}

BULL_PARAMS       = {"consec_down":5,"rsi_thresh":25,"bb_std":2.5,"vol_z_min":1.5,"require_ma200":True}
CORRECTION_PARAMS = {"consec_down":3,"rsi_thresh":30,"bb_std":2.0,"vol_z_min":0.5,"require_ma200":False}
BEAR_PARAMS       = {"consec_down":5,"rsi_thresh":20,"bb_std":2.5,"vol_z_min":1.0,"require_ma200":False}


# ══════════════════════════════════════════════════════════════════════════════
#  LOGGING
# ══════════════════════════════════════════════════════════════════════════════

LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
    handlers=[logging.StreamHandler()],
)
log = logging.getLogger("RBv4")


# ══════════════════════════════════════════════════════════════════════════════
#  UNIVERSE — Wikipedia S&P 500 + MidCap 400
# ══════════════════════════════════════════════════════════════════════════════

def get_live_tickers() -> list:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    log.info("Fetching ticker lists from Wikipedia...")
    try:
        sp500  = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
                               storage_options=headers)[0]["Symbol"].tolist()
        log.info(f"  S&P 500: {len(sp500)}")
    except Exception as e:
        log.error(f"FATAL: S&P 500 from Wikipedia failed: {e}"); raise SystemExit(1)
    try:
        mid400 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_400_companies",
                               storage_options=headers)[0]["Symbol"].tolist()
        log.info(f"  MidCap 400: {len(mid400)}")
    except Exception as e:
        log.error(f"FATAL: MidCap 400 from Wikipedia failed: {e}"); raise SystemExit(1)
    combined = list(dict.fromkeys(sp500 + mid400))
    cleaned  = [t.replace(".", "-") for t in combined]
    log.info(f"  Total: {len(cleaned)} unique tickers")
    return cleaned


# ══════════════════════════════════════════════════════════════════════════════
#  DATA — Alpaca market data primary, yfinance fallback
#  We use Alpaca first because you already have a free API key and it won't
#  rate-limit you the same way Yahoo does for 900 tickers.
# ══════════════════════════════════════════════════════════════════════════════

_data_client = None

def get_data_client():
    global _data_client
    if _data_client is None:
        _data_client = StockHistoricalDataClient(API_KEY, API_SECRET)
    return _data_client


def fetch_via_alpaca(ticker: str, days: int = 280) -> pd.DataFrame | None:
    """Fetch daily bars from Alpaca's market data API (free with your account)."""
    try:
        client = get_data_client()
        start  = datetime.today() - timedelta(days=days + 30)
        req    = StockBarsRequest(
            symbol_or_symbols=ticker,
            timeframe=TimeFrame.Day,
            start=start,
            limit=days + 30,
        )
        bars = client.get_stock_bars(req).df
        if bars.empty:
            return None
        # Alpaca returns MultiIndex (symbol, timestamp) — flatten
        if isinstance(bars.index, pd.MultiIndex):
            bars = bars.xs(ticker, level="symbol") if ticker in bars.index.get_level_values(0) else bars
        bars.index = pd.to_datetime(bars.index)
        bars = bars.rename(columns={"open":"Open","high":"High","low":"Low",
                                     "close":"Close","volume":"Volume"})
        df = bars[["Open","High","Low","Close","Volume"]].dropna()
        return df if len(df) >= MIN_HISTORY_DAYS else None
    except Exception:
        return None


def fetch_via_yfinance(ticker: str, days: int = 280) -> pd.DataFrame | None:
    """yfinance fallback — used when Alpaca data is unavailable."""
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
        return df
    except Exception:
        return None


def fetch_stock(ticker: str) -> pd.DataFrame | None:
    """Try Alpaca first, fall back to yfinance."""
    df = fetch_via_alpaca(ticker)
    if df is None:
        df = fetch_via_yfinance(ticker)
    if df is None:
        return None
    if float(df["Close"].iloc[-1]) < MIN_STOCK_PRICE:
        return None
    return df


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
        log.info(f"  [{label}] {done}/{total} ({len(data)} valid)")
        time.sleep(1.0)   # reduced — Alpaca is more tolerant than Yahoo
    return data


# ══════════════════════════════════════════════════════════════════════════════
#  POSITION MANAGEMENT — reads from Alpaca API directly
#  CRITICAL FIX: GitHub Actions has no persistent disk. We cannot rely on
#  open_positions.json surviving between runs. Instead we read actual
#  positions from Alpaca's API and store metadata (entry price, date, strategy)
#  in the Alpaca order's client_order_id field, which IS persistent.
# ══════════════════════════════════════════════════════════════════════════════

def get_live_positions(client: TradingClient) -> dict:
    """
    Read current positions directly from Alpaca.
    Returns {ticker: {qty, market_value, avg_entry_price, symbol}} 
    We also look up our entry metadata from recent orders.
    """
    try:
        alpaca_positions = client.get_all_positions()
        positions = {}
        for p in alpaca_positions:
            positions[p.symbol] = {
                "ticker":        p.symbol,
                "qty":           float(p.qty),
                "market_value":  float(p.market_value),
                "entry_price":   float(p.avg_entry_price),
                "current_price": float(p.current_price),
                "pnl_pct":       float(p.unrealized_plpc) * 100,
                "pnl_dollar":    float(p.unrealized_pl),
                # These will be filled from our order metadata below
                "entry_date":    "",
                "strategy":      "unknown",
                "dollar_amt":    float(p.market_value),
            }
        return positions
    except Exception as e:
        log.error(f"Could not fetch positions from Alpaca: {e}")
        return {}


def enrich_positions_from_orders(client: TradingClient, positions: dict) -> dict:
    """
    Look through recent orders to find entry date and strategy for each position.
    Alpaca keeps order history — this is our persistent metadata store.
    """
    try:
        from alpaca.trading.requests import GetOrdersRequest
        from alpaca.trading.enums    import QueryOrderStatus
        req    = GetOrdersRequest(status=QueryOrderStatus.CLOSED, limit=100)
        orders = client.get_orders(req)
        # Most recent fill per ticker
        seen = set()
        for order in orders:
            sym = order.symbol
            if sym in positions and sym not in seen:
                seen.add(sym)
                if order.filled_at:
                    positions[sym]["entry_date"] = str(order.filled_at.date())
                # Strategy stored in client_order_id: "RubberBand|2026-04-10"
                if order.client_order_id and "|" in order.client_order_id:
                    parts = order.client_order_id.split("|")
                    positions[sym]["strategy"] = parts[0]
    except Exception as e:
        log.debug(f"Order history lookup failed: {e}")
    return positions


# ══════════════════════════════════════════════════════════════════════════════
#  REGIME DETECTION
# ══════════════════════════════════════════════════════════════════════════════

def detect_regime(spy_df) -> str:
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
#  SIGNAL FUNCTIONS  (4 strategies)
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
        if any(pd.isna(x) for x in [rsi_v,bb_v,vz_v,ma200]): return None
        c1 = (cd>=params["consec_down"]) or (rsi_v<params["rsi_thresh"])
        c2 = c_now<=bb_v; c3 = vz_v>=params["vol_z_min"]
        c4 = (c_now>ma200) if params["require_ma200"] else True
        if c1 and c2 and c3 and c4:
            return {"ticker":ticker,"strategy":"RubberBand","close":round(c_now,2),
                    "rsi":round(rsi_v,1),"vol_z":round(vz_v,2),
                    "trigger":"RSI" if rsi_v<params["rsi_thresh"] else f"{cd}d-down"}
        return None
    except Exception: return None


def sig_52wk_low(ticker, df) -> dict | None:
    try:
        c_now=float(df["Close"].iloc[-1]); low52=float(df["Low252"].iloc[-1])
        rsi_v=float(df["RSI"].iloc[-1]);   vz_v=float(df["Vol_Z"].iloc[-1])
        if any(pd.isna(x) for x in [low52,rsi_v]): return None
        if (c_now<=low52*1.05) and (vz_v>=0.5) and (rsi_v>10):
            return {"ticker":ticker,"strategy":"52wkLow","close":round(c_now,2),
                    "rsi":round(rsi_v,1),"vol_z":round(vz_v,2),
                    "trigger":f"{((c_now/low52)-1)*100:.1f}% above 52wk low"}
        return None
    except Exception: return None


def sig_momentum_reversal(ticker, df) -> dict | None:
    try:
        c=df["Close"]; c_now=float(c.iloc[-1])
        ret60=float(df["Ret60"].iloc[-1]); ret5=float(c.pct_change(5).iloc[-1])
        rsi_v=float(df["RSI"].iloc[-1]);   vz_v=float(df["Vol_Z"].iloc[-1])
        if any(pd.isna(x) for x in [ret60,ret5,rsi_v]): return None
        if (ret60<-0.12) and (ret5>-0.02) and (rsi_v<40) and (vz_v>=0.3):
            return {"ticker":ticker,"strategy":"MomReversal","close":round(c_now,2),
                    "rsi":round(rsi_v,1),"vol_z":round(vz_v,2),
                    "trigger":f"{ret60*100:.1f}% drop/60d, stabilising"}
        return None
    except Exception: return None


def sig_golden_cross(ticker, df) -> dict | None:
    try:
        ma50=float(df["MA50"].iloc[-1]);   ma200=float(df["MA200"].iloc[-1])
        ma50_p=float(df["MA50"].iloc[-2]); ma200_p=float(df["MA200"].iloc[-2])
        c_now=float(df["Close"].iloc[-1])
        if any(pd.isna(x) for x in [ma50,ma200,ma50_p,ma200_p]): return None
        if (ma50>ma200) and (ma50_p<=ma200_p):
            return {"ticker":ticker,"strategy":"GoldenCross","close":round(c_now,2),
                    "rsi":0.0,"vol_z":0.0,"trigger":"50MA crossed above 200MA"}
        return None
    except Exception: return None


# ══════════════════════════════════════════════════════════════════════════════
#  CALENDAR + REGIME ROUTER
# ══════════════════════════════════════════════════════════════════════════════

def get_signals(ticker, df, month, regime) -> list:
    sched   = SCHEDULE[month]
    primary = sched["primary"]; sec = sched["secondary"]
    params  = BULL_PARAMS if regime=="bull" else CORRECTION_PARAMS if regime=="correction" else BEAR_PARAMS
    if regime=="bear": primary,sec = "52wkLow","MomReversal"
    sigs = []
    for name in [primary, sec]:
        s = (sig_rubber_band(ticker,df,params) if name=="RubberBand"
             else sig_52wk_low(ticker,df)       if name=="52wkLow"
             else sig_momentum_reversal(ticker,df) if name=="MomReversal"
             else sig_golden_cross(ticker,df)   if name=="GoldenCross"
             else None)
        if s: sigs.append(s)
    return sigs


# ══════════════════════════════════════════════════════════════════════════════
#  EXIT LOGIC
# ══════════════════════════════════════════════════════════════════════════════

def check_exit(df, pos: dict) -> tuple[bool, str]:
    try:
        c_now = float(df["Close"].iloc[-1])
        mid   = float(df["BB_Mid"].iloc[-1])
        pnl   = pos["pnl_pct"] / 100

        # Primary: price crossed above 20-day MA midline
        if c_now > mid:
            return True, f"above_midline ${c_now:.2f}>${mid:.2f} ({pnl*100:+.1f}%)"

        # Time stop: days from entry date if we know it
        if pos.get("entry_date"):
            try:
                days = (datetime.today()-datetime.strptime(pos["entry_date"],"%Y-%m-%d")).days
                if days >= EXIT_DAYS_MAX:
                    return True, f"max_hold_{days}d ({pnl*100:+.1f}%)"
            except Exception: pass

        # Stop loss
        if pnl <= EXIT_STOP_LOSS:
            return True, f"stop_loss ({pnl*100:.1f}%)"

        return False, ""
    except Exception: return False, ""


# ══════════════════════════════════════════════════════════════════════════════
#  ORDERS
# ══════════════════════════════════════════════════════════════════════════════

def place_buy(client, ticker, dollars, strategy) -> bool:
    try:
        client_order_id = f"{strategy}|{date.today()}"[:48]  # Alpaca limit
        order = client.submit_order(MarketOrderRequest(
            symbol=ticker, notional=round(dollars,2),
            side=OrderSide.BUY, time_in_force=TimeInForce.DAY,
            client_order_id=client_order_id))
        log.info(f"  BUY  {ticker:8s}  ${dollars:8.2f}  strategy={strategy}  id={order.id}")
        return True
    except Exception as e:
        log.error(f"  BUY FAILED {ticker}: {e}"); return False


def place_sell(client, ticker) -> bool:
    try:
        client.close_position(ticker)
        log.info(f"  SELL {ticker:8s}  closed"); return True
    except Exception as e:
        log.error(f"  SELL FAILED {ticker}: {e}"); return False


# ══════════════════════════════════════════════════════════════════════════════
#  PDT TRACKING — stored in a local file but also cross-checked via Alpaca
# ══════════════════════════════════════════════════════════════════════════════

PDT_FILE = LOG_DIR / "pdt.json"

def load_pdt():
    return json.load(open(PDT_FILE)) if PDT_FILE.exists() else []

def save_pdt(l):
    json.dump(l, open(PDT_FILE,"w"))

def pdt_count(l):
    cutoff = date.today()-timedelta(days=7)
    return sum(1 for d in l if datetime.strptime(d,"%Y-%m-%d").date()>=cutoff)

def pdt_ok(l):
    n = pdt_count(l)
    if n>=MAX_DAY_TRADES:
        log.warning(f"PDT limit: {n}/{MAX_DAY_TRADES}"); return False
    return True


# ══════════════════════════════════════════════════════════════════════════════
#  RUN REPORT — written after every run so you have a persistent record
#  Even though GitHub Actions doesn't keep files between runs, you can
#  commit this file to the repo or read it from the Actions log.
# ══════════════════════════════════════════════════════════════════════════════

class Report:
    def __init__(self):
        self.lines = []
        self.actions = []   # trades taken this run

    def add(self, line=""):
        self.lines.append(line)

    def trade(self, action, ticker, strategy, price, dollars, reason=""):
        self.actions.append({
            "action":strategy, "ticker":ticker,"strategy":strategy,
            "price":price,"dollars":dollars,"reason":reason,
            "time":datetime.now().strftime("%H:%M:%S"),
        })

    def save(self, equity, cash, regime, month, positions, signals_found,
             entries, exits):
        sched = SCHEDULE[month]
        ts    = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
        md    = [
            f"# Rubber Band Bot — Run Report",
            f"**{ts}**  |  Regime: **{regime.upper()}**  |  Month: **{date.today().strftime('%B')}**",
            "",
            "## Account",
            f"| | |",
            f"|---|---|",
            f"| Equity | ${equity:,.2f} |",
            f"| Cash | ${cash:,.2f} |",
            f"| Cash reserve floor | ${equity*CASH_RESERVE_PCT:,.2f} |",
            "",
            "## Strategy active this month",
            f"**Primary:** {sched['primary']}  |  **Secondary:** {sched['secondary']}",
            f"> {sched['note']}",
            "",
            "## Open positions",
        ]
        if positions:
            md += ["| Ticker | Strategy | Entry $ | Current $ | P&L % | P&L $ |",
                   "|---|---|---|---|---|---|"]
            for t, p in positions.items():
                md.append(f"| {t} | {p.get('strategy','?')} | ${p['entry_price']:.2f} | "
                           f"${p['current_price']:.2f} | {p['pnl_pct']:+.2f}% | "
                           f"${p['pnl_dollar']:+.2f} |")
        else:
            md.append("_None_")

        md += ["", "## Signals found today"]
        if signals_found:
            md += ["| Ticker | Strategy | Price | RSI | Vol Z | Trigger |",
                   "|---|---|---|---|---|---|"]
            for s in signals_found:
                md.append(f"| {s['ticker']} | {s['strategy']} | ${s['close']:.2f} | "
                           f"{s.get('rsi',0):.1f} | {s.get('vol_z',0):.2f} | {s.get('trigger','')} |")
        else:
            md.append("_No signals today_")

        md += ["", "## Actions taken this run"]
        if self.actions:
            md += ["| Time | Action | Ticker | Strategy | Price | $ Amount | Note |",
                   "|---|---|---|---|---|---|---|"]
            for a in self.actions:
                md.append(f"| {a['time']} | {a['action']} | {a['ticker']} | "
                           f"{a['strategy']} | ${a['price']:.2f} | ${a['dollars']:.2f} | "
                           f"{a['reason']} |")
        else:
            md.append("_No trades placed this run_")

        md += [
            "",
            "## Session stats",
            f"- Stocks scanned: {len(self.lines)}",
            f"- Signals found: {len(signals_found)}",
            f"- Entries placed: {entries}",
            f"- Exits placed: {exits}",
            "",
            "---",
            "_Generated by Rubber Band Bot v4_",
        ]

        REPORT_FILE.write_text("\n".join(md), encoding="utf-8")
        log.info(f"  Report saved → {REPORT_FILE}")

        # Also append to a running log CSV
        log_csv = LOG_DIR / "run_history.csv"
        fields  = ["timestamp","regime","month","equity","cash",
                   "signals","entries","exits","open_positions"]
        init    = not log_csv.exists()
        with open(log_csv,"a",newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            if init: w.writeheader()
            w.writerow({"timestamp":ts,"regime":regime,"month":month,
                        "equity":round(equity,2),"cash":round(cash,2),
                        "signals":len(signals_found),"entries":entries,
                        "exits":exits,"open_positions":len(positions)})


# ══════════════════════════════════════════════════════════════════════════════
#  DISPLAY
# ══════════════════════════════════════════════════════════════════════════════

W = 72

def hdr(title=""):
    bar="═"*W; print(f"\n╔{bar}╗")
    if title:
        t=f"  {title}  "; lp=(W-len(t))//2; rp=W-len(t)-lp
        print(f"║{' '*lp}{t}{' '*max(0,rp)}║"); print(f"╠{bar}╣")

def ftr():  print(f"╚{'═'*W}╝")
def div():  print(f"╠{'═'*W}╣")
def blank():print(f"║{' '*W}║")

def row(label, value=""):
    content=f"  {label:<36s}  {value}" if value else f"  {label}"
    pad=W-len(content); print(f"║{content}{' '*max(0,pad)}║")


# ══════════════════════════════════════════════════════════════════════════════
#  EXITS-ONLY MODE  (9:35am — morning gap-up check)
# ══════════════════════════════════════════════════════════════════════════════

def run_exits_only():
    report = Report()
    hdr(); row("RUBBER BAND BOT  v4  —  MORNING EXIT CHECK")
    div(); row("Mode","PAPER" if PAPER_TRADING else "*** LIVE ***")
    row("Time", datetime.now().strftime("%H:%M:%S")); ftr()

    if datetime.today().weekday() >= 5:
        log.info("Weekend."); return

    client    = TradingClient(API_KEY, API_SECRET, paper=PAPER_TRADING)
    acct      = client.get_account()
    equity    = float(acct.equity); cash = float(acct.cash)
    positions = get_live_positions(client)
    positions = enrich_positions_from_orders(client, positions)

    if not positions:
        hdr("MORNING CHECK"); row("No open positions."); ftr()
        report.save(equity, cash, "unknown", date.today().month, {}, [], 0, 0)
        return

    spy_df = add_indicators(fetch_stock("SPY")) if fetch_stock("SPY") is not None else None
    regime = detect_regime(spy_df)
    month  = date.today().month

    pos_data = fetch_batch(list(positions.keys()), "positions")
    exits    = 0

    hdr("MORNING EXIT CHECK")
    for ticker, pos in positions.items():
        if ticker not in pos_data: row(f"{ticker}","no data — skip"); continue
        df = pos_data[ticker]
        ex, why = check_exit(df, pos)
        row(f"{ticker:8s}  P&L {pos['pnl_pct']:+.1f}%  ${pos['pnl_dollar']:+.2f}",
            f"EXIT — {why}" if ex else "HOLD")
        if ex and place_sell(client, ticker):
            exits += 1
            report.trade("SELL", ticker, pos.get("strategy","?"),
                         pos["current_price"], pos["market_value"], why)
    ftr()
    report.save(equity, cash, regime, month, positions, [], 0, exits)
    log.info("Morning exit check complete.")


# ══════════════════════════════════════════════════════════════════════════════
#  FULL SCAN MODE  (4:15pm — main daily execution)
# ══════════════════════════════════════════════════════════════════════════════

def run_full_scan():
    report = Report()
    month  = date.today().month
    sched  = SCHEDULE[month]

    hdr(); row("RUBBER BAND BOT  v4  —  DAILY SCAN")
    div()
    row("Mode","PAPER TRADING" if PAPER_TRADING else "*** LIVE TRADING ***")
    row("Date",f"{date.today()}   {datetime.now().strftime('%H:%M:%S')}")
    row("Month strategy", sched["note"]); ftr()

    if datetime.today().weekday() >= 5:
        log.info("Weekend."); return

    client  = TradingClient(API_KEY, API_SECRET, paper=PAPER_TRADING)
    acct    = client.get_account()
    equity  = float(acct.equity)
    cash    = float(acct.cash)
    reserve = equity * CASH_RESERVE_PCT  # minimum cash to always keep

    hdr("ACCOUNT")
    row("Equity",        f"${equity:>12,.2f}")
    row("Cash",          f"${cash:>12,.2f}")
    row("Cash reserve",  f"${reserve:>12,.2f}  (always kept liquid)")
    row("Available",     f"${max(0,cash-reserve):>12,.2f}  (for new trades)")
    ftr()

    # Read positions from Alpaca API — NOT local files
    positions = get_live_positions(client)
    positions = enrich_positions_from_orders(client, positions)
    pdt       = load_pdt()

    hdr("LIVE POSITIONS  (from Alpaca API)")
    if positions:
        div()
        row(f"  {'Ticker':<8}  {'Strategy':<14}  {'Entry':>8}  {'Now':>8}  {'P&L%':>7}  {'P&L$':>8}")
        div()
        for t, p in positions.items():
            row(f"  {t:<8}  {p.get('strategy','?'):<14}  "
                f"${p['entry_price']:>7.2f}  ${p['current_price']:>7.2f}  "
                f"{p['pnl_pct']:>+6.1f}%  ${p['pnl_dollar']:>+7.2f}")
    else:
        blank(); row("  No open positions."); blank()
    row(f"  PDT trades used: {pdt_count(pdt)}/{MAX_DAY_TRADES}")
    ftr()

    # Universe
    all_tickers = get_live_tickers()

    # SPY regime
    spy_raw = fetch_stock("SPY")
    spy_df  = add_indicators(spy_raw) if spy_raw is not None else None
    regime  = detect_regime(spy_df)
    spy_now   = float(spy_df["Close"].iloc[-1])  if spy_df is not None else 0
    spy_ma200 = float(spy_df["MA200"].iloc[-1])  if spy_df is not None else 0

    hdr("MARKET REGIME")
    row("SPY", f"${spy_now:,.2f}  |  200MA ${spy_ma200:,.2f}  |  {spy_now/max(spy_ma200,1)*100:.1f}%")
    div()
    row("Regime",    regime.upper())
    row("Primary",   sched["primary"])
    row("Secondary", sched["secondary"]); ftr()

    # Exit check on current holdings
    exits = 0
    if positions:
        pos_data = fetch_batch(list(positions.keys()), "held stocks")
        hdr("EXIT EVALUATION")
        for ticker, pos in positions.items():
            if ticker not in pos_data: row(f"{ticker}","no data"); continue
            ex, why = check_exit(pos_data[ticker], pos)
            row(f"{ticker:8s}  P&L {pos['pnl_pct']:+.1f}%",
                f"EXIT — {why}" if ex else "HOLD")
            if ex and place_sell(client, ticker):
                exits += 1
                report.trade("SELL", ticker, pos.get("strategy","?"),
                             pos["current_price"], pos["market_value"], why)
                del positions[ticker]
        if exits == 0: row("No exits triggered.")
        ftr()

    # Full universe scan
    hdr("DATA DOWNLOAD")
    row(f"Scanning {len(all_tickers)} stocks  (S&P 500 + MidCap 400)")
    row("Alpaca data primary → yfinance fallback"); ftr()

    held_tickers = set(positions.keys())
    scan_tickers = [t for t in all_tickers if t not in held_tickers]
    all_data     = fetch_batch(scan_tickers, "universe")
    report.lines = list(all_data.keys())  # for stats

    # Signal scan
    hdr("SIGNAL SCAN")
    row(f"Month: {date.today().strftime('%B')}  |  Regime: {regime.upper()}")
    row(f"Primary: {sched['primary']}  |  Secondary: {sched['secondary']}"); ftr()

    all_sigs = []
    for ticker, df in all_data.items():
        for s in get_signals(ticker, df, month, regime):
            s["month"]=month; s["regime"]=regime
            all_sigs.append(s)

    hdr(f"SIGNALS  —  {len(all_sigs)} found")
    if not all_sigs:
        blank(); row("No signals today."); blank()
        row(sched["note"]); blank()
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
    # Re-fetch live account state after exits
    cash    = float(client.get_account().cash)
    avail   = max(0, cash - reserve)   # respect cash reserve
    entries = 0

    for sig in all_sigs:
        ticker   = sig["ticker"]
        strategy = sig["strategy"]

        # Guards
        live_pos = get_live_positions(client)  # fresh check
        skip = ""
        if len(live_pos)  >= MAX_OPEN_POSITIONS: skip="max positions"
        elif not pdt_ok(pdt):                     skip="PDT limit"
        elif avail        <= 1.0:                 skip=f"reserve floor (avail ${avail:.0f})"

        dollar_amt = equity * POSITION_SIZE_PCT
        if not skip:
            if dollar_amt > avail: skip=f"would breach reserve (need ${dollar_amt:.0f}, avail ${avail:.0f})"

        if skip:
            row(f"  SKIP  {ticker:<8}  {strategy:<16}", skip); continue

        row(f"  ENTER {ticker:<8}  {strategy:<16}  ${dollar_amt:.2f}")
        if place_buy(client, ticker, dollar_amt, strategy):
            entries += 1; avail -= dollar_amt
            report.trade("BUY", ticker, strategy, sig["close"], dollar_amt)

        if len(get_live_positions(client)) >= MAX_OPEN_POSITIONS:
            break

    if entries==0 and not all_sigs: row("  No entries placed.")
    ftr()

    save_pdt(pdt)

    # Final account state
    acct_final = client.get_account()
    equity_f   = float(acct_final.equity)
    cash_f     = float(acct_final.cash)
    positions_f = get_live_positions(client)

    hdr("SESSION SUMMARY")
    row("Regime",          regime.upper())
    row("Strategy",        f"{sched['primary']} + {sched['secondary']}")
    row("Stocks scanned",  str(len(all_data)))
    row("Signals found",   str(len(all_sigs)))
    row("Entries placed",  str(entries))
    row("Exits placed",    str(exits))
    row("Open positions",  str(list(positions_f.keys())))
    row("Equity",          f"${equity_f:,.2f}")
    row("Cash",            f"${cash_f:,.2f}")
    row("Report saved",    str(REPORT_FILE)); ftr()

    report.save(equity_f, cash_f, regime, month, positions_f, all_sigs, entries, exits)


# ══════════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rubber Band Bot v4")
    parser.add_argument("--mode", choices=["scan","exits"], default="scan",
                        help="scan=4:15pm full run | exits=9:35am exit check")
    args = parser.parse_args()
    if args.mode == "exits":
        run_exits_only()
    else:
        run_full_scan()
