"""
╔══════════════════════════════════════════════════════════════════════╗
║           RUBBER BAND SNAP BOT — Phase 2 Paper Trading              ║
║                                                                      ║
║  Strategy: Short-term mean reversion after downside extremes        ║
║  Broker:   Alpaca Markets (paper → live with one config change)     ║
║  Schedule: Run this script daily at 4:15pm ET on market days        ║
╚══════════════════════════════════════════════════════════════════════╝

SETUP (run once in your terminal):
    pip install alpaca-py yfinance pandas numpy

HOW TO RUN:
    python rubber_band_bot.py

TO SWITCH FROM PAPER → LIVE:
    Change PAPER_TRADING = True  to  PAPER_TRADING = False
    Change API_KEY and API_SECRET to your LIVE Alpaca keys
    That is it. Nothing else changes.
"""

import os, json, time, logging, csv
from datetime import datetime, timedelta, date
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


# ══════════════════════════════════════════════════════════════════════════════
#  CONFIGURATION  — EDIT BEFORE RUNNING
# ══════════════════════════════════════════════════════════════════════════════

# --- YOUR ALPACA KEYS ---
# Paper keys:  paper.alpaca.markets → Your Account → API Keys
# Live keys:   app.alpaca.markets   → Your Account → API Keys
API_KEY    = "PKHCGGIGXDTSZA5VBRQFUYKDOC"
API_SECRET = "7PJmeXW574pZpshia3Kgrf9G8sobnr8EJrGBKjnVHtZV"

# --- PAPER OR LIVE ---
# True  = paper trading  (safe, fake money, always start here)
# False = LIVE trading   (real money — only flip after 30+ days paper validation)
PAPER_TRADING = True

# --- POSITION SIZING ---
POSITION_SIZE_PCT   = 0.02   # 2% of account equity per trade
MAX_OPEN_POSITIONS  = 2      # max stocks held at once
MAX_PORTFOLIO_HEAT  = 0.40   # max 40% of capital deployed at once

# --- EXIT RULES ---
EXIT_DAYS_MAX  = 7           # hard exit after this many calendar days
EXIT_STOP_LOSS = -0.03       # exit if down more than 3% from entry
# Primary exit: close above 20-day MA midline (computed in exit logic)

# --- SIGNAL PARAMETERS (validated in 23-year backtest) ---
CONSEC_DOWN_DAYS = 5         # consecutive down closes required (3-5 range)
RSI_PERIOD       = 14
RSI_THRESHOLD    = 25        # extreme oversold threshold
BB_WINDOW        = 20
BB_STD           = 2.5       # lower band standard deviations
VOL_ZSCORE_MIN   = 1.5       # volume spike threshold
VOL_WINDOW       = 20
MA_TREND_WINDOW  = 200       # bull/bear filter
MA_EXIT_WINDOW   = 20        # midline = primary exit target
MIN_STOCK_PRICE  = 5.0
MIN_HISTORY_DAYS = 220

# --- PDT RULE ---
MAX_DAY_TRADES = 3           # max day-trades per rolling 5 business days

# --- FILES ---
LOG_DIR      = Path("logs")
TRADE_LOG    = LOG_DIR / "trades.csv"
PDT_LOG      = LOG_DIR / "pdt_ledger.json"
SIGNAL_LOG   = LOG_DIR / "signals.csv"
POSITION_LOG = LOG_DIR / "open_positions.json"

# --- UNIVERSE ---
import pandas as pd

def get_live_tickers():
    print("Fetching live S&P 500 and MidCap 400 lists...")
    
    # This disguise tells Wikipedia we are a normal Windows computer, not a bot
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    # 1. Fetch live S&P 500 tickers from Wikipedia (using the disguise)
    sp500_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500_table = pd.read_html(sp500_url, storage_options=headers)[0]
    sp500_tickers = sp500_table['Symbol'].tolist()
    
    # 2. Fetch live S&P MidCap 400 tickers from Wikipedia (using the disguise)
    midcap_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_400_companies'
    midcap_table = pd.read_html(midcap_url, storage_options=headers)[0]
    midcap_tickers = midcap_table['Symbol'].tolist()
    
    # 3. Combine them into one massive list
    combined_tickers = sp500_tickers + midcap_tickers
    
    # 4. Automatically fix the Yahoo Finance dot-to-dash problem (BRK.B -> BRK-B)
    clean_tickers = [ticker.replace('.', '-') for ticker in combined_tickers]
    
    return clean_tickers

# Create the master list for the bot to use
SP500_TICKERS = get_live_tickers()


# ══════════════════════════════════════════════════════════════════════════════
#  LOGGING
# ══════════════════════════════════════════════════════════════════════════════

LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_DIR / f"bot_{date.today()}.log"),
    ],
)
log = logging.getLogger("RubberBandBot")


# ══════════════════════════════════════════════════════════════════════════════
#  ALPACA
# ══════════════════════════════════════════════════════════════════════════════

def get_client() -> TradingClient:
    if "PASTE" in API_KEY:
        log.error("Set your API_KEY and API_SECRET at the top of this file first.")
        raise SystemExit(1)
    return TradingClient(API_KEY, API_SECRET, paper=PAPER_TRADING)


# ══════════════════════════════════════════════════════════════════════════════
#  DATA
# ══════════════════════════════════════════════════════════════════════════════

def fetch_stock(ticker: str, days: int = 260) -> pd.DataFrame | None:
    try:
        end   = datetime.today()
        start = end - timedelta(days=days * 2)
        df = yf.download(ticker, start=start, end=end,
                         progress=False, auto_adjust=True)
        if df.empty or len(df) < MIN_HISTORY_DAYS:
            return None
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        df = df[["Open", "High", "Low", "Close", "Volume"]].dropna()
        if float(df["Close"].iloc[-1]) < MIN_STOCK_PRICE:
            return None
        return df
    except Exception:
        return None


def fetch_all(tickers: list) -> dict:
    log.info(f"Downloading EOD data for {len(tickers)} stocks...")
    data = {}
    batch = 40
    for i in range(0, len(tickers), batch):
        chunk = tickers[i : i + batch]
        for t in chunk:
            df = fetch_stock(t)
            if df is not None:
                data[t] = df
        fetched = min(i + batch, len(tickers))
        log.info(f"  {fetched}/{len(tickers)} fetched...")
        time.sleep(1.5)
    log.info(f"  Ready: {len(data)} stocks with sufficient history")
    return data


# ══════════════════════════════════════════════════════════════════════════════
#  INDICATORS
# ══════════════════════════════════════════════════════════════════════════════

def rsi(close: pd.Series, n: int = 14) -> pd.Series:
    d = close.diff()
    g = d.clip(lower=0).rolling(n).mean()
    l = (-d.clip(upper=0)).rolling(n).mean()
    return 100 - 100 / (1 + g / (l + 1e-10))


def bb_lower(close: pd.Series, w: int = 20, sd: float = 2.5) -> pd.Series:
    return close.rolling(w).mean() - sd * close.rolling(w).std()


def bb_midline(close: pd.Series, w: int = 20) -> pd.Series:
    return close.rolling(w).mean()


def vol_zscore(volume: pd.Series, w: int = 20) -> pd.Series:
    avg = volume.rolling(w).mean()
    std = volume.rolling(w).std()
    return (volume - avg) / (std + 1e-10)


def consec_down(close: pd.Series) -> int:
    vals = close.values
    count = 0
    for i in range(len(vals) - 1, 0, -1):
        if vals[i] < vals[i - 1]:
            count += 1
        else:
            break
    return count


# ══════════════════════════════════════════════════════════════════════════════
#  SIGNAL — THE RUBBER BAND SNAP
# ══════════════════════════════════════════════════════════════════════════════

def check_signal(ticker: str, df: pd.DataFrame) -> dict | None:
    """
    All four conditions must be true:
      1. Over-extension:  3-5+ consecutive down closes OR RSI < 25
      2. Band touch:      Close <= lower Bollinger Band (20d, 2.5 sigma)
      3. Volume confirm:  Volume Z-score >= 1.5
      4. Trend filter:    Close > 200-day MA (bull market only)
    """
    try:
        c, v = df["Close"], df["Volume"]

        rsi_val  = float(rsi(c, RSI_PERIOD).iloc[-1])
        bb_val   = float(bb_lower(c, BB_WINDOW, BB_STD).iloc[-1])
        vz_val   = float(vol_zscore(v, VOL_WINDOW).iloc[-1])
        ma200    = float(c.rolling(MA_TREND_WINDOW).mean().iloc[-1])
        c_now    = float(c.iloc[-1])
        cd       = consec_down(c)

        if any(pd.isna(x) for x in [rsi_val, bb_val, vz_val, ma200]):
            return None

        c1_consec = cd >= CONSEC_DOWN_DAYS
        c1_rsi    = rsi_val < RSI_THRESHOLD
        c1 = c1_consec or c1_rsi
        c2 = c_now <= bb_val
        c3 = vz_val >= VOL_ZSCORE_MIN
        c4 = c_now > ma200

        if c1 and c2 and c3 and c4:
            return {
                "ticker":       ticker,
                "signal_date":  str(date.today()),
                "close":        round(c_now, 2),
                "rsi":          round(rsi_val, 1),
                "bb_lower":     round(bb_val, 2),
                "vol_zscore":   round(vz_val, 2),
                "ma_200":       round(ma200, 2),
                "consec_down":  cd,
                "c1_consec":    c1_consec,
                "c1_rsi":       c1_rsi,
            }
        return None
    except Exception:
        return None


# ══════════════════════════════════════════════════════════════════════════════
#  EXIT LOGIC
# ══════════════════════════════════════════════════════════════════════════════

def check_exit(ticker: str, df: pd.DataFrame,
               entry_price: float, entry_date: str) -> tuple[bool, str]:
    """
    Returns (should_exit, reason).
    Rules (first triggered wins):
      1. Close > 20d MA midline  — bounce complete, take profit
      2. Held 7+ calendar days   — hard time stop
      3. Down >= 3% from entry   — stop loss
    """
    try:
        c      = df["Close"]
        c_now  = float(c.iloc[-1])
        mid    = float(bb_midline(c, MA_EXIT_WINDOW).iloc[-1])
        days   = (datetime.today() - datetime.strptime(entry_date, "%Y-%m-%d")).days
        pnl    = (c_now - entry_price) / entry_price

        if c_now > mid:
            return True, f"above_midline (${c_now:.2f} > MA20 ${mid:.2f}, +{pnl*100:.1f}%)"
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

def load_pdt() -> list:
    if PDT_LOG.exists():
        with open(PDT_LOG) as f:
            return json.load(f)
    return []


def save_pdt(ledger: list):
    with open(PDT_LOG, "w") as f:
        json.dump(ledger, f)


def pdt_count(ledger: list) -> int:
    cutoff = date.today() - timedelta(days=7)
    return sum(1 for d in ledger
               if datetime.strptime(d, "%Y-%m-%d").date() >= cutoff)


def pdt_ok(ledger: list) -> bool:
    n = pdt_count(ledger)
    if n >= MAX_DAY_TRADES:
        log.warning(f"PDT limit: {n}/{MAX_DAY_TRADES} day-trades used.")
        return False
    return True


# ══════════════════════════════════════════════════════════════════════════════
#  POSITIONS
# ══════════════════════════════════════════════════════════════════════════════

def load_positions() -> dict:
    if POSITION_LOG.exists():
        with open(POSITION_LOG) as f:
            return json.load(f)
    return {}


def save_positions(p: dict):
    with open(POSITION_LOG, "w") as f:
        json.dump(p, f, indent=2)


def sync_positions(client: TradingClient, local: dict) -> dict:
    try:
        live = {p.symbol for p in client.get_all_positions()}
        cleaned = {k: v for k, v in local.items() if k in live}
        dropped = set(local) - set(cleaned)
        if dropped:
            log.info(f"  Position sync: removed stale {dropped}")
        return cleaned
    except Exception as e:
        log.warning(f"  Sync failed: {e}")
        return local


def portfolio_heat(positions: dict, balance: float) -> float:
    deployed = sum(p.get("dollar_amt", 0) for p in positions.values())
    return deployed / max(balance + deployed, 1)


# ══════════════════════════════════════════════════════════════════════════════
#  ORDERS
# ══════════════════════════════════════════════════════════════════════════════

def buy(client: TradingClient, ticker: str, dollars: float) -> bool:
    try:
        req = MarketOrderRequest(
            symbol=ticker,
            notional=round(dollars, 2),
            side=OrderSide.BUY,
            time_in_force=TimeInForce.DAY,
        )
        order = client.submit_order(req)
        log.info(f"  BUY  {ticker}  ${dollars:.2f}  id={order.id}")
        return True
    except Exception as e:
        log.error(f"  BUY FAILED {ticker}: {e}")
        return False


def sell(client: TradingClient, ticker: str) -> bool:
    try:
        client.close_position(ticker)
        log.info(f"  SELL {ticker}  (full position closed)")
        return True
    except Exception as e:
        log.error(f"  SELL FAILED {ticker}: {e}")
        return False


# ══════════════════════════════════════════════════════════════════════════════
#  TRADE LOG
# ══════════════════════════════════════════════════════════════════════════════

FIELDS = ["date","ticker","action","price","dollar_amount","pnl_pct",
          "pnl_dollar","hold_days","exit_reason","rsi","vol_z",
          "consec_down","equity","mode"]


def write_trade(rec: dict):
    init = not TRADE_LOG.exists()
    with open(TRADE_LOG, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if init:
            w.writeheader()
        w.writerow({k: rec.get(k, "") for k in FIELDS})


def write_signal(sig: dict):
    init = not SIGNAL_LOG.exists()
    with open(SIGNAL_LOG, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(sig.keys()))
        if init:
            w.writeheader()
        w.writerow(sig)


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════════════

def run():
    log.info("=" * 65)
    log.info("  RUBBER BAND SNAP BOT")
    log.info(f"  Mode:  {'PAPER' if PAPER_TRADING else '*** LIVE ***'}")
    log.info(f"  Date:  {date.today()}")
    log.info("=" * 65)

    # Weekend check
    if datetime.today().weekday() >= 5:
        log.info("Weekend — no market. Exiting.")
        return

    # Connect
    log.info("Connecting to Alpaca...")
    client  = get_client()
    account = client.get_account()
    equity  = float(account.equity)
    cash    = float(account.cash)
    log.info(f"  Equity: ${equity:,.2f}  |  Cash: ${cash:,.2f}")

    # Load state
    pdt_ledger = load_pdt()
    positions  = sync_positions(client, load_positions())
    heat       = portfolio_heat(positions, cash)
    pdt_used   = pdt_count(pdt_ledger)

    log.info(f"  Open positions: {len(positions)}  {list(positions.keys())}")
    log.info(f"  PDT used:       {pdt_used}/{MAX_DAY_TRADES}")
    log.info(f"  Portfolio heat: {heat*100:.1f}%")

    # ── PHASE 1: FAST HOLDINGS PRE-CHECK ───────────────────────────────────
    if positions:
        log.info("-" * 40)
        log.info("FAST STOP-LOSS CHECK")
        pos_data = fetch_all(list(positions.keys()))
        
        to_close = []
        for ticker, pos in positions.items():
            if ticker not in pos_data:
                continue
            df    = pos_data[ticker]
            c_now = float(df["Close"].iloc[-1])
            ep    = pos["entry_price"]
            ed    = pos["entry_date"]
            pnl   = (c_now - ep) / ep
            days  = (datetime.today() - datetime.strptime(ed, "%Y-%m-%d")).days
            ex, reason = check_exit(ticker, df, ep, ed)
            
            status = f"EXIT: {reason}" if ex else "HOLD"
            log.info(f"  {ticker:6s}  entry=${ep:.2f}  now=${c_now:.2f}"
                     f"  P&L={pnl*100:+.1f}%  held={days}d  → {status}")
            if ex:
                to_close.append((ticker, reason, c_now, pnl, days, pos))

        for ticker, reason, c_now, pnl, days, pos in to_close:
            if sell(client, ticker):
                write_trade({
                    "date": str(date.today()), "ticker": ticker, "action": "SELL",
                    "price": c_now, "dollar_amount": pos["dollar_amt"],
                    "pnl_pct": round(pnl * 100, 2),
                    "pnl_dollar": round(pnl * pos["dollar_amt"], 2),
                    "hold_days": days, "exit_reason": reason,
                    "rsi": pos.get("rsi", ""), "vol_z": pos.get("vol_z", ""),
                    "consec_down": pos.get("consec_down", ""),
                    "equity": round(equity, 2),
                    "mode": "paper" if PAPER_TRADING else "live",
                })
                del positions[ticker]
        save_positions(positions)

    # ── PHASE 2: NEW SIGNAL SCAN ───────────────────────────────────────────
    log.info("-" * 40)
    log.info("MARKET SCAN")
    # Fetch universe, ignoring what we already hold
    scan_tickers = [t for t in SP500_TICKERS if t not in positions]
    data = fetch_all(scan_tickers)

    signals = []
    for ticker, df in data.items():
        sig = check_signal(ticker, df)
        if sig:
            signals.append(sig)
            write_signal(sig)

    log.info(f"  Signals found: {len(signals)}")
    for s in signals:
        trigger = "RSI" if s["c1_rsi"] else f"{s['consec_down']}d-down"
        log.info(f"  ✦ {s['ticker']:6s}  ${s['close']:.2f}  "
                 f"RSI={s['rsi']}  vol_z={s['vol_zscore']}  [{trigger}]")

    # ── ENTRIES ────────────────────────────────────────────────────────────
    log.info("-" * 40)
    log.info("ENTRIES")

    cash = float(client.get_account().cash)
    heat = portfolio_heat(positions, cash)

    for sig in signals:
        ticker = sig["ticker"]

        if len(positions) >= MAX_OPEN_POSITIONS:
            log.info(f"  SKIP {ticker}: max positions reached")
            break
        if heat >= MAX_PORTFOLIO_HEAT:
            log.info(f"  SKIP {ticker}: portfolio heat {heat*100:.1f}% at limit")
            break
        if not pdt_ok(pdt_ledger):
            log.info(f"  SKIP {ticker}: PDT limit reached")
            break

        dollar_amt = equity * POSITION_SIZE_PCT
        if dollar_amt < 1.0 or dollar_amt > cash * 0.95:
            log.info(f"  SKIP {ticker}: cash insufficient (${cash:.2f})")
            continue

        log.info(f"  ENTERING {ticker}  ${dollar_amt:.2f}"
                 f"  RSI={sig['rsi']}  vol_z={sig['vol_zscore']}"
                 f"  consec={sig['consec_down']}")

        if buy(client, ticker, dollar_amt):
            positions[ticker] = {
                "entry_price": sig["close"],
                "entry_date":  str(date.today()),
                "dollar_amt":  round(dollar_amt, 2),
                "rsi":         sig["rsi"],
                "vol_z":       sig["vol_zscore"],
                "consec_down": sig["consec_down"],
            }
            write_trade({
                "date": str(date.today()), "ticker": ticker, "action": "BUY",
                "price": sig["close"], "dollar_amount": round(dollar_amt, 2),
                "pnl_pct": 0, "pnl_dollar": 0, "hold_days": 0,
                "rsi": sig["rsi"], "vol_z": sig["vol_zscore"],
                "consec_down": sig["consec_down"],
                "equity": round(equity, 2),
                "mode": "paper" if PAPER_TRADING else "live",
            })
            cash  -= dollar_amt
            heat   = portfolio_heat(positions, cash)

    save_positions(positions)
    save_pdt(pdt_ledger)

    # ── SUMMARY ────────────────────────────────────────────────────────────
    cash_now = float(client.get_account().cash)
    log.info("=" * 65)
    log.info("  DONE")
    log.info(f"  Open positions: {list(positions.keys())}")
    log.info(f"  Signals today:  {len(signals)}")
    log.info(f"  Cash remaining: ${cash_now:,.2f}")
    log.info(f"  Logs folder:    {LOG_DIR.absolute()}")
    log.info("=" * 65)

if __name__ == "__main__":
    run()