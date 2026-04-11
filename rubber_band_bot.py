"""
RUBBER BAND BOT v5
==================
Calendar-aware, regime-switching, multi-strategy trading bot.
Runs on GitHub Actions triggered by cron-job.org.

WHAT RUNS WHEN (auto-detected by time, no --mode flag needed):
  9:35am ET  -> exits-only check (morning gap-up scan)
  4:15pm ET  -> full daily scan + entries + daily summary written
  Weekend    -> weekly summary written, no trading
  Other time -> off-hours status summary, no trading

LOGS (committed back to repo after every run):
  logs/daily/YYYY-MM-DD.md    one file per trading day
  logs/weekly/YYYY-WNN.md     one file per week
  logs/transactions.csv       every trade ever placed
  logs/runs.csv               every run, one row

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
from alpaca.trading.requests import MarketOrderRequest, GetOrdersRequest
from alpaca.trading.enums    import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.data.historical  import StockHistoricalDataClient
from alpaca.data.requests    import StockBarsRequest
from alpaca.data.timeframe   import TimeFrame


# ══════════════════════════════════════════════════════════════════════════════
#  KEYS
# ══════════════════════════════════════════════════════════════════════════════

API_KEY    = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")

if not API_KEY or not API_SECRET:
    print("ERROR: Set ALPACA_API_KEY and ALPACA_SECRET_KEY as environment variables.")
    raise SystemExit(1)


# ══════════════════════════════════════════════════════════════════════════════
#  CONFIGURATION
# ══════════════════════════════════════════════════════════════════════════════

PAPER_TRADING      = True   # flip to False only after 30+ days paper validation

POSITION_SIZE_PCT  = 0.08   # 8% of equity per trade  (semi-aggressive)
MAX_OPEN_POSITIONS = 4      # up to 4 simultaneous holdings
CASH_RESERVE_PCT   = 0.15   # always keep 15% cash minimum

EXIT_DAYS_MAX  = 7
EXIT_STOP_LOSS = -0.03

MAX_DAY_TRADES   = 3
MIN_STOCK_PRICE  = 5.0
MIN_HISTORY_DAYS = 220

LOG_DIR    = Path("logs")
DAILY_DIR  = LOG_DIR / "daily"
WEEKLY_DIR = LOG_DIR / "weekly"
TX_FILE    = LOG_DIR / "transactions.csv"
RUNS_FILE  = LOG_DIR / "runs.csv"
PDT_FILE   = LOG_DIR / "pdt.json"

for d in [LOG_DIR, DAILY_DIR, WEEKLY_DIR]:
    d.mkdir(parents=True, exist_ok=True)

W = 68  # box inner width — NEVER exceed this


# ══════════════════════════════════════════════════════════════════════════════
#  CALENDAR STRATEGY SCHEDULE  (from 5-year backtest)
# ══════════════════════════════════════════════════════════════════════════════

SCHEDULE = {
    1:  {"p":"MomReversal", "s":"52wkLow",    "note":"Jan: MomReversal+3.67% RubberBand DISABLED"},
    2:  {"p":"52wkLow",     "s":"MomReversal","note":"Feb: 52wkLow+1.37% RubberBand DISABLED"},
    3:  {"p":"52wkLow",     "s":"MomReversal","note":"Mar: 52wkLow+1.85% 68%win"},
    4:  {"p":"RubberBand",  "s":"52wkLow",    "note":"Apr: RubberBand+0.71% regime sets params"},
    5:  {"p":"RubberBand",  "s":"52wkLow",    "note":"May: RubberBand+1.93% 58%win"},
    6:  {"p":"52wkLow",     "s":"RubberBand", "note":"Jun: 52wkLow+1.81% Sharpe 1.72"},
    7:  {"p":"52wkLow",     "s":"RubberBand", "note":"Jul: 52wkLow+2.86% 66%win"},
    8:  {"p":"RubberBand",  "s":"52wkLow",    "note":"Aug: RubberBand+4.72% 70%win BEST MONTH"},
    9:  {"p":"GoldenCross", "s":"52wkLow",    "note":"Sep: Worst month. GoldenCross best option"},
    10: {"p":"RubberBand",  "s":"52wkLow",    "note":"Oct: RubberBand+3.29% 70%win"},
    11: {"p":"RubberBand",  "s":"MomReversal","note":"Nov: RubberBand+4.77% 86%WIN RATE"},
    12: {"p":"MomReversal", "s":"52wkLow",    "note":"Dec: MomReversal+1.34% year-end"},
}

MN = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",
      7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}

BULL_P = {"consec_down":5,"rsi_thresh":25,"bb_std":2.5,"vol_z_min":1.5,"require_ma200":True}
CORR_P = {"consec_down":3,"rsi_thresh":30,"bb_std":2.0,"vol_z_min":0.5,"require_ma200":False}
BEAR_P = {"consec_down":5,"rsi_thresh":20,"bb_std":2.5,"vol_z_min":1.0,"require_ma200":False}


# ══════════════════════════════════════════════════════════════════════════════
#  LOGGING
# ══════════════════════════════════════════════════════════════════════════════

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s", datefmt="%H:%M:%S",
    handlers=[logging.StreamHandler()])
log = logging.getLogger("RBv5")


# ══════════════════════════════════════════════════════════════════════════════
#  DISPLAY — strict W-character box, values right-aligned, no overflow
# ══════════════════════════════════════════════════════════════════════════════

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

def ftr():
    print(f"+{'='*W}+")

def div():
    print(f"+{'-'*W}+")

def blank():
    print(f"|{' '*W}|")

def row(label="", value=""):
    label = str(label)
    value = str(value)
    if value:
        val_max  = min(len(value), W - 6)
        val_str  = _trunc(value, val_max)
        lbl_max  = W - 4 - len(val_str)
        lbl_str  = _trunc(label, max(1, lbl_max))
        content  = f"  {lbl_str:<{max(1,lbl_max)}}  {val_str}"
    else:
        content = f"  {_trunc(label, W-2)}"
    # enforce exact width
    if len(content) > W: content = content[:W]
    pad = W - len(content)
    print(f"|{content}{' '*pad}|")

def trow(*cols, widths=None):
    """Table row with fixed column widths."""
    if widths is None:
        w_each = W // max(len(cols),1)
        widths = [w_each] * len(cols)
    parts = [_trunc(str(c), w) for c, w in zip(cols, widths)]
    padded = [f"{p:<{w}}" for p, w in zip(parts, widths)]
    content = "  " + "  ".join(padded)
    content = content[:W]
    pad = W - len(content)
    print(f"|{content}{' '*pad}|")


# ══════════════════════════════════════════════════════════════════════════════
#  UNIVERSE
# ══════════════════════════════════════════════════════════════════════════════

def get_live_tickers():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    log.info("Fetching tickers from Wikipedia...")
    try:
        sp500  = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
                               storage_options=headers)[0]["Symbol"].tolist()
    except Exception as e:
        log.error(f"FATAL S&P 500: {e}"); raise SystemExit(1)
    try:
        mid400 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_400_companies",
                               storage_options=headers)[0]["Symbol"].tolist()
    except Exception as e:
        log.error(f"FATAL MidCap 400: {e}"); raise SystemExit(1)
    combined = list(dict.fromkeys(sp500 + mid400))
    cleaned  = [t.replace(".", "-") for t in combined]
    log.info(f"  {len(sp500)} + {len(mid400)} = {len(cleaned)} tickers")
    return cleaned


# ══════════════════════════════════════════════════════════════════════════════
#  DATA
# ══════════════════════════════════════════════════════════════════════════════

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
        df = yf.download(ticker, start=datetime.today()-timedelta(days=days+60),
                         end=datetime.today(), progress=False, auto_adjust=True)
        if df.empty or len(df)<MIN_HISTORY_DAYS: return None
        if isinstance(df.columns, pd.MultiIndex): df.columns=df.columns.get_level_values(0)
        return df[["Open","High","Low","Close","Volume"]].dropna()
    except Exception: return None

def fetch_stock(ticker):
    df = _alpaca(ticker) or _yf(ticker)
    if df is None: return None
    if float(df["Close"].iloc[-1]) < MIN_STOCK_PRICE: return None
    return df

def add_ind(df):
    c, v = df["Close"], df["Volume"]
    df   = df.copy()
    d=c.diff(); g=d.clip(lower=0).rolling(14).mean(); l=(-d.clip(upper=0)).rolling(14).mean()
    df["RSI"]   = 100-100/(1+g/(l+1e-10))
    df["BBL25"] = c.rolling(20).mean()-2.5*c.rolling(20).std()
    df["BBL20"] = c.rolling(20).mean()-2.0*c.rolling(20).std()
    df["BBM"]   = c.rolling(20).mean()
    avg=v.rolling(20).mean(); sv=v.rolling(20).std()
    df["VZ"]    = (v-avg)/(sv+1e-10)
    df["MA50"]  = c.rolling(50).mean()
    df["MA200"] = c.rolling(200).mean()
    df["L252"]  = c.rolling(252).min()
    df["R60"]   = c.pct_change(60)
    return df

def fetch_batch(tickers, label=""):
    data={}
    for i in range(0,len(tickers),40):
        for t in tickers[i:i+40]:
            df=fetch_stock(t)
            if df is not None: data[t]=add_ind(df)
        log.info(f"  [{label}] {min(i+40,len(tickers))}/{len(tickers)} ({len(data)} valid)")
        time.sleep(1.0)
    return data


# ══════════════════════════════════════════════════════════════════════════════
#  REGIME
# ══════════════════════════════════════════════════════════════════════════════

def regime(spy_df):
    if spy_df is None or len(spy_df)<210: return "bull"
    r = float(spy_df["Close"].iloc[-1]) / (float(spy_df["MA200"].iloc[-1])+1e-10)
    return "bull" if r>=1.0 else "correction" if r>=0.93 else "bear"

def consec_down(close):
    vals=close.values; n=0
    for i in range(len(vals)-1,0,-1):
        if vals[i]<vals[i-1]: n+=1
        else: break
    return n


# ══════════════════════════════════════════════════════════════════════════════
#  SIGNALS
# ══════════════════════════════════════════════════════════════════════════════

def _rb(ticker, df, p):
    try:
        c=df["Close"]; cn=float(c.iloc[-1]); rsi=float(df["RSI"].iloc[-1])
        bb=float(df["BBL25" if p["bb_std"]>=2.4 else "BBL20"].iloc[-1])
        vz=float(df["VZ"].iloc[-1]); ma200=float(df["MA200"].iloc[-1])
        cd=consec_down(c)
        if any(pd.isna(x) for x in [rsi,bb,vz,ma200]): return None
        c1=(cd>=p["consec_down"])or(rsi<p["rsi_thresh"])
        c2=cn<=bb; c3=vz>=p["vol_z_min"]; c4=(cn>ma200) if p["require_ma200"] else True
        if c1 and c2 and c3 and c4:
            return {"ticker":ticker,"strategy":"RubberBand","close":round(cn,2),
                    "rsi":round(rsi,1),"vol_z":round(vz,2),
                    "trigger":"RSI" if rsi<p["rsi_thresh"] else f"{cd}d-down"}
    except Exception: pass
    return None

def _52(ticker, df):
    try:
        cn=float(df["Close"].iloc[-1]); low=float(df["L252"].iloc[-1])
        rsi=float(df["RSI"].iloc[-1]); vz=float(df["VZ"].iloc[-1])
        if any(pd.isna(x) for x in [low,rsi]): return None
        if (cn<=low*1.05)and(vz>=0.5)and(rsi>10):
            return {"ticker":ticker,"strategy":"52wkLow","close":round(cn,2),
                    "rsi":round(rsi,1),"vol_z":round(vz,2),
                    "trigger":f"{((cn/low)-1)*100:.1f}% above 52wk low"}
    except Exception: pass
    return None

def _mr(ticker, df):
    try:
        c=df["Close"]; cn=float(c.iloc[-1]); r60=float(df["R60"].iloc[-1])
        r5=float(c.pct_change(5).iloc[-1]); rsi=float(df["RSI"].iloc[-1]); vz=float(df["VZ"].iloc[-1])
        if any(pd.isna(x) for x in [r60,r5,rsi]): return None
        if (r60<-0.12)and(r5>-0.02)and(rsi<40)and(vz>=0.3):
            return {"ticker":ticker,"strategy":"MomReversal","close":round(cn,2),
                    "rsi":round(rsi,1),"vol_z":round(vz,2),
                    "trigger":f"{r60*100:.1f}% drop/60d stabilising"}
    except Exception: pass
    return None

def _gc(ticker, df):
    try:
        m50=float(df["MA50"].iloc[-1]); m200=float(df["MA200"].iloc[-1])
        m50p=float(df["MA50"].iloc[-2]); m200p=float(df["MA200"].iloc[-2])
        cn=float(df["Close"].iloc[-1])
        if any(pd.isna(x) for x in [m50,m200,m50p,m200p]): return None
        if (m50>m200)and(m50p<=m200p):
            return {"ticker":ticker,"strategy":"GoldenCross","close":round(cn,2),
                    "rsi":0.0,"vol_z":0.0,"trigger":"50MA x 200MA"}
    except Exception: pass
    return None

def get_signals(ticker, df, month, rgm):
    sc=SCHEDULE[month]; pri=sc["p"]; sec=sc["s"]
    prm=(BULL_P if rgm=="bull" else CORR_P if rgm=="correction" else BEAR_P)
    if rgm=="bear": pri,sec="52wkLow","MomReversal"
    sigs=[]
    for name in [pri,sec]:
        s=(_rb(ticker,df,prm) if name=="RubberBand" else
           _52(ticker,df)     if name=="52wkLow"    else
           _mr(ticker,df)     if name=="MomReversal" else
           _gc(ticker,df)     if name=="GoldenCross" else None)
        if s: sigs.append(s)
    return sigs


# ══════════════════════════════════════════════════════════════════════════════
#  EXIT
# ══════════════════════════════════════════════════════════════════════════════

def check_exit(df, pos):
    try:
        cn=float(df["Close"].iloc[-1]); mid=float(df["BBM"].iloc[-1])
        pnl=pos.get("pnl_pct",0)/100
        if cn>mid: return True,f"above midline (+{pnl*100:.1f}%)"
        if pos.get("entry_date"):
            days=(datetime.today()-datetime.strptime(pos["entry_date"],"%Y-%m-%d")).days
            if days>=EXIT_DAYS_MAX: return True,f"max hold {days}d ({pnl*100:+.1f}%)"
        if pnl<=EXIT_STOP_LOSS: return True,f"stop loss ({pnl*100:.1f}%)"
    except Exception: pass
    return False,""


# ══════════════════════════════════════════════════════════════════════════════
#  POSITIONS — always from Alpaca API
# ══════════════════════════════════════════════════════════════════════════════

def get_positions(client):
    try:
        out={}
        for p in client.get_all_positions():
            out[p.symbol]={"ticker":p.symbol,"qty":float(p.qty),
                "market_value":float(p.market_value),"entry_price":float(p.avg_entry_price),
                "current_price":float(p.current_price),
                "pnl_pct":float(p.unrealized_plpc)*100,"pnl_dollar":float(p.unrealized_pl),
                "dollar_amt":float(p.market_value),"entry_date":"","strategy":"unknown"}
        return out
    except Exception as e:
        log.error(f"get_positions failed: {e}"); return {}

def enrich(client, positions):
    try:
        req=GetOrdersRequest(status=QueryOrderStatus.CLOSED,limit=200)
        orders=client.get_orders(req); seen=set()
        for o in sorted(orders, key=lambda x: x.submitted_at or datetime.min):
            sym=o.symbol
            if sym in positions and sym not in seen:
                seen.add(sym)
                if o.filled_at: positions[sym]["entry_date"]=str(o.filled_at.date())
                if o.client_order_id and "|" in o.client_order_id:
                    positions[sym]["strategy"]=o.client_order_id.split("|")[0]
    except Exception as e:
        log.debug(f"enrich failed: {e}")
    return positions


# ══════════════════════════════════════════════════════════════════════════════
#  PDT
# ══════════════════════════════════════════════════════════════════════════════

def load_pdt(): return json.load(open(PDT_FILE)) if PDT_FILE.exists() else []
def save_pdt(l): json.dump(l,open(PDT_FILE,"w"))
def pdt_n(l):
    c=date.today()-timedelta(days=7)
    return sum(1 for d in l if datetime.strptime(d,"%Y-%m-%d").date()>=c)
def pdt_ok(l):
    n=pdt_n(l)
    if n>=MAX_DAY_TRADES: log.warning(f"PDT {n}/{MAX_DAY_TRADES}"); return False
    return True


# ══════════════════════════════════════════════════════════════════════════════
#  ORDERS
# ══════════════════════════════════════════════════════════════════════════════

def do_buy(client, ticker, dollars, strategy):
    try:
        cid=f"{strategy}|{date.today()}"[:48]
        o=client.submit_order(MarketOrderRequest(symbol=ticker,notional=round(dollars,2),
            side=OrderSide.BUY,time_in_force=TimeInForce.DAY,client_order_id=cid))
        log.info(f"  BUY {ticker} ${dollars:.2f} [{strategy}] id={o.id}"); return True
    except Exception as e:
        log.error(f"  BUY FAILED {ticker}: {e}"); return False

def do_sell(client, ticker):
    try:
        client.close_position(ticker); log.info(f"  SELL {ticker} closed"); return True
    except Exception as e:
        log.error(f"  SELL FAILED {ticker}: {e}"); return False


# ══════════════════════════════════════════════════════════════════════════════
#  TRANSACTION LOG
# ══════════════════════════════════════════════════════════════════════════════

TX_F=["timestamp","date","action","ticker","strategy","price","dollar_amount",
      "pnl_pct","pnl_dollar","hold_days","exit_reason","regime","equity_after"]

def log_tx(action,ticker,strategy,price,dollars,rgm,equity,
           pnl_pct=0,pnl_dollar=0,hold_days=0,exit_reason=""):
    init=not TX_FILE.exists()
    with open(TX_FILE,"a",newline="") as f:
        w=csv.DictWriter(f,fieldnames=TX_F)
        if init: w.writeheader()
        w.writerow({"timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "date":str(date.today()),"action":action,"ticker":ticker,
            "strategy":strategy,"price":round(price,2),"dollar_amount":round(dollars,2),
            "pnl_pct":round(pnl_pct,2),"pnl_dollar":round(pnl_dollar,2),
            "hold_days":hold_days,"exit_reason":exit_reason,"regime":rgm,
            "equity_after":round(equity,2)})

RUN_F=["timestamp","mode","regime","equity","cash","signals","entries","exits",
       "open_positions","tickers"]

def log_run(mode,rgm,equity,cash,signals,entries,exits,positions):
    init=not RUNS_FILE.exists()
    with open(RUNS_FILE,"a",newline="") as f:
        w=csv.DictWriter(f,fieldnames=RUN_F)
        if init: w.writeheader()
        w.writerow({"timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "mode":mode,"regime":rgm,"equity":round(equity,2),"cash":round(cash,2),
            "signals":signals,"entries":entries,"exits":exits,
            "open_positions":len(positions),"tickers":"|".join(positions.keys())})


# ══════════════════════════════════════════════════════════════════════════════
#  DAILY LOG
# ══════════════════════════════════════════════════════════════════════════════

def write_daily(today, equity, cash, rgm, month, positions, signals, buys, sells):
    sc=SCHEDULE[month]
    op_pnl=sum(p.get("pnl_dollar",0) for p in positions.values())
    fname=DAILY_DIR/f"{today}.md"
    L=[f"# Daily Log — {today}","",
       "## Account","| | |","|---|---|",
       f"| Equity | **${equity:,.2f}** |",
       f"| Cash | ${cash:,.2f} |",
       f"| Reserve floor | ${equity*CASH_RESERVE_PCT:,.2f} |",
       f"| Open P&L | ${op_pnl:+,.2f} |",
       f"| Regime | {rgm.upper()} |",
       f"| Strategies | {sc['p']} + {sc['s']} |","",
       "## Holdings"]
    if positions:
        L+=["| Ticker | Strategy | Invested | Entry | Now | P&L% | P&L$ | Days |",
            "|--------|----------|----------|-------|-----|------|------|------|"]
        for t,p in positions.items():
            dh=""
            if p.get("entry_date"):
                try: dh=str((datetime.today()-datetime.strptime(p["entry_date"],"%Y-%m-%d")).days)+"d"
                except: pass
            L.append(f"| {t} | {p.get('strategy','?')} | ${p.get('dollar_amt',0):,.2f} "
                     f"| ${p['entry_price']:.2f} | ${p['current_price']:.2f} "
                     f"| {p['pnl_pct']:+.2f}% | ${p['pnl_dollar']:+.2f} | {dh} |")
    else:
        L.append("_No open positions._")
    L+=["","## Trades today"]
    if buys or sells:
        L+=["| Time | Action | Ticker | Strategy | Price | Amount | Note |",
            "|------|--------|--------|----------|-------|--------|------|"]
        for b in buys: L.append(f"| {b['t']} | BUY | {b['tk']} | {b['st']} | ${b['px']:.2f} | ${b['$']:.2f} | — |")
        for s in sells: L.append(f"| {s['t']} | SELL | {s['tk']} | {s['st']} | ${s['px']:.2f} | {s.get('$','—')} | {s['why']} |")
    else:
        L.append("_No trades today._")
    L+=["","## Signals detected"]
    if signals:
        L+=["| Ticker | Strategy | Price | RSI | Vol Z | Trigger |",
            "|--------|----------|-------|-----|-------|---------|"]
        for s in signals:
            L.append(f"| {s['ticker']} | {s['strategy']} | ${s['close']:.2f} "
                     f"| {s.get('rsi',0):.1f} | {s.get('vol_z',0):.2f} | {s.get('trigger','')} |")
    else:
        L.append("_No signals today._")
    L+=["","---",f"_RBv5 {datetime.now().strftime('%H:%M UTC')}_"]
    fname.write_text("\n".join(L),encoding="utf-8")
    log.info(f"  Daily log -> {fname}")


# ══════════════════════════════════════════════════════════════════════════════
#  WEEKLY SUMMARY
# ══════════════════════════════════════════════════════════════════════════════

def write_weekly(client, equity, cash):
    today=date.today(); wk=today.isocalendar()[1]
    fname=WEEKLY_DIR/f"{today.year}-W{wk:02d}.md"
    positions=enrich(client,get_positions(client))
    week_tx=[]
    if TX_FILE.exists():
        with open(TX_FILE,newline="") as f:
            for tx in csv.DictReader(f):
                try:
                    if datetime.strptime(tx["date"],"%Y-%m-%d").date()>=today-timedelta(days=7):
                        week_tx.append(tx)
                except: pass
    buys=[t for t in week_tx if t["action"]=="BUY"]
    sells=[t for t in week_tx if t["action"]=="SELL"]
    real_pnl=sum(float(t.get("pnl_dollar",0)) for t in sells)
    open_pnl=sum(p.get("pnl_dollar",0) for p in positions.values())
    invested=sum(p.get("dollar_amt",0) for p in positions.values())

    hdr(f"WEEKLY SUMMARY  Week {wk} / {today.year}")
    row("Equity",           f"${equity:,.2f}")
    row("Cash",             f"${cash:,.2f}")
    row("Total invested",   f"${invested:,.2f}")
    row("Open P&L",         f"${open_pnl:+,.2f}")
    row("Realised P&L",     f"${real_pnl:+,.2f}")
    row("Trades this week", f"{len(buys)} buys  {len(sells)} sells")
    ftr()

    L=[f"# Weekly Summary — Week {wk}, {today.year}",f"_{today}_","",
       "## Account","| | |","|---|---|",
       f"| Equity | **${equity:,.2f}** |",
       f"| Cash | ${cash:,.2f} |",
       f"| Invested | ${invested:,.2f} |",
       f"| Open P&L | ${open_pnl:+,.2f} |",
       f"| Realised P&L | ${real_pnl:+,.2f} |","",
       "## Holdings"]
    if positions:
        L+=["| Ticker | Strategy | Invested | Entry | Now | P&L% | P&L$ |",
            "|--------|----------|----------|-------|-----|------|------|"]
        for t,p in positions.items():
            L.append(f"| {t} | {p.get('strategy','?')} | ${p.get('dollar_amt',0):,.2f} "
                     f"| ${p['entry_price']:.2f} | ${p['current_price']:.2f} "
                     f"| {p['pnl_pct']:+.2f}% | ${p['pnl_dollar']:+.2f} |")
    else:
        L.append("_No open positions._")
    L+=["","## Trades this week"]
    if week_tx:
        L+=["| Date | Action | Ticker | Strategy | Amount | P&L |",
            "|------|--------|--------|----------|--------|-----|"]
        for t in week_tx:
            pstr=f"${float(t.get('pnl_dollar',0)):+.2f}" if t["action"]=="SELL" else "—"
            L.append(f"| {t['date']} | {t['action']} | {t['ticker']} "
                     f"| {t['strategy']} | ${float(t['dollar_amount']):.2f} | {pstr} |")
    else:
        L.append("_No trades._")
    nm=today.month%12+1; ns=SCHEDULE[nm]
    L+=["","## Next session",
        f"- Month: **{MN[nm]}**",
        f"- Primary: **{ns['p']}**  Secondary: **{ns['s']}**",
        f"- Note: {ns['note']}","","---",
        f"_RBv5 {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}_"]
    fname.write_text("\n".join(L),encoding="utf-8")
    log.info(f"  Weekly summary -> {fname}")


# ══════════════════════════════════════════════════════════════════════════════
#  TIME AUTO-DETECTION
# ══════════════════════════════════════════════════════════════════════════════

def detect_mode():
    now=datetime.utcnow(); h=now.hour; dow=now.weekday()
    if dow>=5: return "weekly"
    if dow==4 and h>=21: return "weekly"
    if 13<=h<14: return "exits"
    if 20<=h<22: return "scan"
    return "summary"


# ══════════════════════════════════════════════════════════════════════════════
#  STATUS SUMMARY (off-hours)
# ══════════════════════════════════════════════════════════════════════════════

def run_summary(client, equity, cash, rgm):
    positions=enrich(client,get_positions(client))
    invested=sum(p.get("dollar_amt",0) for p in positions.values())
    open_pnl=sum(p.get("pnl_dollar",0) for p in positions.values())

    hdr("ACCOUNT STATUS")
    row("Equity",        f"${equity:,.2f}")
    row("Cash",          f"${cash:,.2f}")
    row("Regime",        rgm.upper())
    row("Total invested",f"${invested:,.2f}")
    row("Open P&L",      f"${open_pnl:+,.2f}")
    ftr()

    hdr(f"HOLDINGS  ({len(positions)} positions)")
    if positions:
        trow("TICKER","STRATEGY","INVESTED","ENTRY","NOW","P&L%","P&L$",
             widths=[7,14,9,7,7,6,7])
        div()
        for t,p in positions.items():
            trow(t, p.get("strategy","?"),
                 f"${p.get('dollar_amt',0):.2f}",
                 f"${p['entry_price']:.2f}",
                 f"${p['current_price']:.2f}",
                 f"{p['pnl_pct']:+.1f}%",
                 f"${p['pnl_dollar']:+.2f}",
                 widths=[7,14,9,7,7,6,7])
        blank()
        row("Total invested", f"${invested:,.2f}")
        row("Total open P&L", f"${open_pnl:+,.2f}")
    else:
        blank(); row("No open positions."); blank()
    ftr()

    hdr("RECENT TRANSACTIONS")
    if TX_FILE.exists():
        with open(TX_FILE,newline="") as f:
            txs=list(csv.DictReader(f))
        for tx in (txs[-6:] if len(txs)>=6 else txs)[::-1]:
            pnl=f"  P&L ${float(tx.get('pnl_dollar',0)):+.2f}" if tx["action"]=="SELL" else ""
            row(f"{tx['date']}  {tx['action']}  {tx['ticker']}  {tx['strategy']}  ${float(tx['dollar_amount']):.2f}{pnl}")
    else:
        row("No transactions yet.")
    ftr()
    log_run("summary",rgm,equity,cash,0,0,0,positions)


# ══════════════════════════════════════════════════════════════════════════════
#  EXITS RUN
# ══════════════════════════════════════════════════════════════════════════════

def run_exits(client, equity, cash, rgm):
    positions=enrich(client,get_positions(client))
    if not positions:
        hdr("MORNING CHECK"); blank(); row("No open positions."); blank(); ftr()
        log_run("exits",rgm,equity,cash,0,0,0,{})
        return
    pos_data=fetch_batch(list(positions.keys()),"positions")
    exits=0

    hdr("EXIT CHECK")
    for ticker,pos in positions.items():
        if ticker not in pos_data: row(ticker,"no data"); continue
        ex,why=check_exit(pos_data[ticker],pos)
        row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%  ${pos['pnl_dollar']:+.2f}",
            f"EXIT: {_trunc(why,22)}" if ex else "HOLD")
        if ex and do_sell(client,ticker):
            exits+=1
            cur=pos["current_price"]
            dh=(datetime.today()-datetime.strptime(pos["entry_date"],"%Y-%m-%d")).days if pos.get("entry_date") else 0
            log_tx("SELL",ticker,pos.get("strategy","?"),cur,pos["market_value"],
                   rgm,float(client.get_account().equity),
                   pos["pnl_pct"],pos["pnl_dollar"],dh,why)
    ftr()
    log_run("exits",rgm,equity,cash,0,0,exits,positions)


# ══════════════════════════════════════════════════════════════════════════════
#  FULL SCAN
# ══════════════════════════════════════════════════════════════════════════════

def run_scan(client, equity, cash, rgm):
    today=date.today(); month=today.month; sc=SCHEDULE[month]
    reserve=equity*CASH_RESERVE_PCT; avail=max(0.0,cash-reserve)

    hdr("RUBBER BAND BOT v5  —  DAILY SCAN")
    row("Mode",   "PAPER" if PAPER_TRADING else "*** LIVE ***")
    row("Date",   str(today))
    row("Month",  f"{MN[month]}: {sc['p']} + {sc['s']}")
    row("Regime", rgm.upper())
    ftr()

    hdr("ACCOUNT")
    row("Equity",    f"${equity:,.2f}")
    row("Cash",      f"${cash:,.2f}")
    row("Reserve",   f"${reserve:,.2f}  (always kept)")
    row("Available", f"${avail:,.2f}  (for new trades)")
    ftr()

    positions=enrich(client,get_positions(client)); pdt=load_pdt()

    hdr(f"HOLDINGS  ({len(positions)} open)")
    if positions:
        trow("TICKER","STRATEGY","INVESTED","ENTRY","NOW","P&L%","P&L$",
             widths=[7,14,9,7,7,6,7])
        div()
        for t,p in positions.items():
            trow(t,p.get("strategy","?"),
                 f"${p.get('dollar_amt',0):.2f}",
                 f"${p['entry_price']:.2f}",
                 f"${p['current_price']:.2f}",
                 f"{p['pnl_pct']:+.1f}%",
                 f"${p['pnl_dollar']:+.2f}",
                 widths=[7,14,9,7,7,6,7])
        blank()
        inv=sum(p.get("dollar_amt",0) for p in positions.values())
        pnl=sum(p.get("pnl_dollar",0) for p in positions.values())
        row("Total invested",f"${inv:,.2f}")
        row("Total open P&L",f"${pnl:+,.2f}")
    else:
        blank(); row("No open positions."); blank()
    row(f"PDT used: {pdt_n(pdt)}/{MAX_DAY_TRADES}")
    ftr()

    # Exit check
    exits=0; sells_log=[]
    if positions:
        pos_data=fetch_batch(list(positions.keys()),"positions")
        hdr("EXIT EVALUATION")
        for ticker,pos in list(positions.items()):
            if ticker not in pos_data: row(ticker,"no data"); continue
            ex,why=check_exit(pos_data[ticker],pos)
            row(f"{ticker}  P&L {pos['pnl_pct']:+.1f}%  ${pos['pnl_dollar']:+.2f}",
                f"EXIT: {_trunc(why,20)}" if ex else "HOLD")
            if ex and do_sell(client,ticker):
                exits+=1; cur=pos["current_price"]
                dh=(datetime.today()-datetime.strptime(pos["entry_date"],"%Y-%m-%d")).days if pos.get("entry_date") else 0
                log_tx("SELL",ticker,pos.get("strategy","?"),cur,pos["market_value"],
                       rgm,float(client.get_account().equity),
                       pos["pnl_pct"],pos["pnl_dollar"],dh,why)
                sells_log.append({"t":datetime.now().strftime("%H:%M"),"tk":ticker,
                                   "st":pos.get("strategy","?"),"px":cur,"why":why})
                del positions[ticker]
        ftr()

    # Full scan
    hdr("DATA DOWNLOAD")
    row(f"Scanning S&P 500 + MidCap 400 (~900 stocks)")
    row("Alpaca data primary / yfinance fallback")
    ftr()
    tickers=get_live_tickers()
    scan=    [t for t in tickers if t not in positions]
    all_data=fetch_batch(scan,"universe")

    hdr("SIGNAL SCAN")
    row(f"Month: {MN[month]}  Regime: {rgm.upper()}")
    row(f"Primary: {sc['p']}  Secondary: {sc['s']}")
    ftr()
    all_sigs=[]
    for ticker,df in all_data.items():
        for s in get_signals(ticker,df,month,rgm):
            s["month"]=month; s["regime"]=rgm; all_sigs.append(s)

    hdr(f"SIGNALS FOUND  —  {len(all_sigs)}")
    if not all_sigs:
        blank(); row("No signals today."); blank()
        row(_trunc(sc["note"],W-4)); blank()
    else:
        trow("TICKER","STRATEGY","PRICE","RSI","VOL_Z","TRIGGER",
             widths=[7,14,7,5,6,24])
        div()
        for s in all_sigs:
            trow(s["ticker"],s["strategy"],f"${s['close']:.2f}",
                 f"{s.get('rsi',0):.1f}",f"{s.get('vol_z',0):.2f}",
                 s.get("trigger",""), widths=[7,14,7,5,6,24])
        blank()
    ftr()

    # Entries
    hdr("ENTRY ORDERS")
    cash=float(client.get_account().cash); avail=max(0.0,cash-reserve)
    entries=0; buys_log=[]
    for sig in all_sigs:
        ticker=sig["ticker"]; strategy=sig["strategy"]
        lp=get_positions(client)
        skip=""
        if len(lp)>=MAX_OPEN_POSITIONS: skip="max positions"
        elif not pdt_ok(pdt):           skip="PDT limit"
        elif avail<=1.0:                skip="reserve floor"
        da=equity*POSITION_SIZE_PCT
        if not skip and da>avail:       skip="reserve breach"
        if skip:
            row(f"  SKIP  {ticker}  {strategy}",_trunc(skip,20)); continue
        row(f"  ENTER {ticker}  {strategy}",f"${da:.2f}")
        if do_buy(client,ticker,da,strategy):
            entries+=1; avail-=da
            log_tx("BUY",ticker,strategy,sig["close"],da,rgm,
                   float(client.get_account().equity))
            buys_log.append({"t":datetime.now().strftime("%H:%M"),"tk":ticker,
                              "st":strategy,"px":sig["close"],"$":da})
        if len(get_positions(client))>=MAX_OPEN_POSITIONS: break
    if entries==0 and not all_sigs: row("  No entries placed.")
    ftr()

    save_pdt(pdt)
    acct2=client.get_account(); eq2=float(acct2.equity); ca2=float(acct2.cash)
    pos2=enrich(client,get_positions(client))

    hdr("SESSION SUMMARY")
    row("Regime",        rgm.upper())
    row("Strategy",      f"{sc['p']} + {sc['s']}")
    row("Scanned",       str(len(all_data)))
    row("Signals",       str(len(all_sigs)))
    row("Entries",       str(entries))
    row("Exits",         str(exits))
    row("Open pos",      str(len(pos2)))
    row("Equity",        f"${eq2:,.2f}")
    row("Cash",          f"${ca2:,.2f}")
    ftr()

    log_run("scan",rgm,eq2,ca2,len(all_sigs),entries,exits,pos2)
    write_daily(today,eq2,ca2,rgm,month,pos2,all_sigs,buys_log,sells_log)


# ══════════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

if __name__=="__main__":
    mode=detect_mode()
    log.info(f"Mode auto-detected: {mode}")

    client=TradingClient(API_KEY,API_SECRET,paper=PAPER_TRADING)
    acct=client.get_account()
    equity=float(acct.equity); cash=float(acct.cash)

    spy_raw=fetch_stock("SPY")
    spy_df=add_ind(spy_raw) if spy_raw is not None else None
    rgm=regime(spy_df)

    hdr(); row("RUBBER BAND BOT  v5"); div()
    row("Mode",   mode.upper())
    row("Time",   datetime.utcnow().strftime("%H:%M UTC"))
    row("Regime", rgm.upper())
    row("Equity", f"${equity:,.2f}")
    ftr()

    if mode=="scan":
        run_scan(client,equity,cash,rgm)
    elif mode=="exits":
        run_exits(client,equity,cash,rgm)
    elif mode=="weekly":
        run_summary(client,equity,cash,rgm)
        write_weekly(client,equity,cash)
    else:
        run_summary(client,equity,cash,rgm)
