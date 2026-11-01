"""Scheduled, zero-cost, VIRTUAL ONLY trading research. NO broker API usage."""
import argparse,datetime as dt,json,math
from pathlib import Path
from zoneinfo import ZoneInfo
from arena import PaperAccount,council
ROOT=Path(__file__).parent
CONFIG=json.loads((ROOT/"config.json").read_text())
TICKERS=["SPY","QQQ","AAPL","MSFT","BTC-USD","ETH-USD","SOL-USD"]
COINS={"BTC-USD","ETH-USD","SOL-USD"}
UTC=dt.timezone.utc
def initial():
    return {w["id"]:{"events":[],"cash":100.,"positions":{},"seen":{}} for w in CONFIG["workers"]}
def market(now):
    import yfinance as yf
    res={}
    for ticker in TICKERS:
        try:
            d=yf.download(ticker,period="30d",interval="1h",progress=False,threads=False,auto_adjust=True,timeout=10)
            if d.empty:continue
            if hasattr(d.columns,"levels"):d.columns=[str(x[0]).lower() for x in d.columns]
            else:d.columns=[str(x).lower() for x in d.columns]
            bars=[]
            for timestamp,r in d.dropna(subset=["close"]).iterrows():
                ts=timestamp.to_pydatetime()
                if not ts.tzinfo:bars=[];break
                ts=ts.astimezone(UTC)
                if ts+dt.timedelta(hours=1)>now-dt.timedelta(minutes=5):continue
                p=float(r["close"])
                if math.isfinite(p) and p>0:bars.append((ts.isoformat().replace("+00:00","Z"),p))
            if len(bars)>60:res[ticker]=bars
        except Exception as e:print("Feed unavailable",ticker,type(e).__name__)
    return res
def signal(worker,vals,generation_index=0):
    # A successor changes its bounded, deterministic paper strategy. It never
    # executes model-generated code, and original a generation is unchanged.
    if generation_index:
        n=int(worker[1:])
        phase=(generation_index-1)%4
        lookback=(8,12,18,24)[phase]
        threshold=(.009,.012,.016,.020)[phase]
        x=vals[-1]
        short=sum(vals[-13:-1])/12
        long=sum(vals[-41:-1])/40
        deviation=x/long-1
        if n in (3,4,8):
            return 1 if deviation < -threshold else -1 if x > short else 0
        if n in (1,5,7,9):
            return 1 if x/vals[-lookback-1]-1 > threshold and x>long else -1 if x<short else 0
        return 1 if x > max(vals[-lookback-1:-1])*(1+threshold/2) else -1 if x<short else 0
    x=vals[-1];a=sum(vals[-21:-1])/20;b=sum(vals[-51:-1])/50
    mom=x/vals[-13]-1;z=x/(sum(vals[-31:-1])/30)-1
    hi=max(vals[-21:-1]);lo=min(vals[-21:-1])
    n=int(worker[1:])
    if n==1:return 1 if x>hi*1.005 else -1 if x<a else 0
    if n==2:return 1 if x>a>b else -1 if x<a else 0
    if n==3:return 1 if z<-.02 else -1 if z>.01 else 0
    if n==4:return 1 if x<lo*.995 else -1 if x>a else 0
    if n==5:return 1 if mom>.02 else -1 if mom<-.01 else 0
    if n==6:return 1 if x>hi else -1 if x<a else 0
    if n==7:return 1 if x/vals[-7]>1.012 else -1 if x<a else 0
    if n==8:return 1 if z<-.015 and x>b else -1 if z>.01 else 0
    if n==9:return 1 if mom>.01 and x>b else -1 if mom<-.005 else 0
    return 1 if x>hi and x>b else -1 if x<a else 0
def run_one(accounts,bars,now):
    results={}
    quotes={s:b[-1][1] for s,b in bars.items()}
    eastern=now.astimezone(ZoneInfo("America/New_York"))
    stocks_open=eastern.weekday()<5 and 9<=eastern.hour<16
    for w in CONFIG["workers"]:
        wid=w["id"];record=accounts[wid]
        try:
            acc=PaperAccount(wid)
            for old in record["events"]:
                new=acc.trade(timestamp=old["timestamp"],asset_class=old["asset_class"],symbol=old["symbol"],
                    side=old["side"],qty=old["qty"],price=old["price"],fee=old["fee"],source_id=old["source_id"])
                if old!=new:raise ValueError("ledger hash mismatch")
            if acc.holdings!=record["positions"] or abs(acc.cash-record["cash"])>1e-6:
                raise ValueError("ledger cash mismatch")
            choices=[]
            for ticker,b in bars.items():
                if wid in ("S09","S10") and ticker not in COINS:continue
                if ticker not in COINS and not stocks_open:continue
                ts=dt.datetime.fromisoformat(b[-1][0].replace("Z","+00:00"))
                if now-ts>dt.timedelta(hours=3) or record["seen"].get(ticker)==b[-1][0]:continue
                choices.append((ticker,b[-1][0],b[-1][1],signal(wid,[p for _,p in b],record.get("generation_index",0))))
            action="HOLD"
            for ticker,timestamp,price,s in choices:
                kind="crypto" if ticker in COINS else "us_equity"
                order_symbol=ticker.replace("-USD","/USD") if kind=="crypto" else ticker
                qty=acc.holdings.get(kind+":"+order_symbol,0)
                if s<0 and qty>1e-8:
                    fee=max(.01,qty*price*(.002 if kind=="crypto" else .001))
                    if qty*price<=fee:continue
                    acc.trade(timestamp=now.isoformat().replace("+00:00","Z"),asset_class=kind,
                        symbol=order_symbol,side="SELL",qty=qty,price=price,fee=fee,
                        source_id="YAHOO:"+ticker+":"+timestamp)
                    action="SELL "+ticker;break
            if action=="HOLD":
                for ticker,timestamp,price,s in choices:
                    kind="crypto" if ticker in COINS else "us_equity"
                    order_symbol=ticker.replace("-USD","/USD") if kind=="crypto" else ticker
                    if s<=0 or acc.holdings.get(kind+":"+order_symbol,0)>1e-8:continue
                    budget=min(40.,acc.cash*.4)
                    qty=math.floor(budget/price/1.01*1e6)/1e6
                    fee=max(.01,qty*price*(.002 if kind=="crypto" else .001))
                    if qty*price<1 or qty*price+fee>acc.cash:continue
                    acc.trade(timestamp=now.isoformat().replace("+00:00","Z"),asset_class=kind,
                        symbol=order_symbol,side="BUY",qty=qty,price=price,fee=fee,
                        source_id="YAHOO:"+ticker+":"+timestamp)
                    action="BUY "+ticker;break
            for ticker,timestamp,_,_ in choices:record["seen"][ticker]=timestamp
            record["cash"]=acc.cash;record["positions"]=dict(acc.holdings);record["events"]=acc.events
            nav=acc.cash;missing=[]
            for key,qty in acc.holdings.items():
                if qty<=0:continue
                ticker=key.split(":",1)[1].replace("/USD","-USD")
                if ticker not in quotes:missing.append(ticker)
                else:nav+=qty*quotes[ticker]
            verdict=council(acc.statement())
            results[wid]={"action":action,"generation_index":record.get("generation_index",0),"cash":acc.cash,"equity":None if missing else round(nav,4),
                "ledger_events":len(acc.events),"council":verdict["status"],"missing_quotes":missing}
        except Exception as e:results[wid]={"action":"QUARANTINED","equity":None,"error":str(e)}
    return results
def main():
    p=argparse.ArgumentParser();p.add_argument("--dir",required=True);args=p.parse_args()
    out=Path(args.dir);out.mkdir(parents=True,exist_ok=True)
    now=dt.datetime.now(UTC);statefile=out/"state.json"
    accounts=json.loads(statefile.read_text()) if statefile.exists() else initial()
    if set(accounts)!={x["id"] for x in CONFIG["workers"]}:raise ValueError("worker roster mismatch")
    bars=market(now)
    if not bars:raise RuntimeError("No observable market data; no artificial trades")
    result=run_one(accounts,bars,now)
    statefile.write_text(json.dumps(accounts,indent=2)+"\n")
    (out/"last_run.json").write_text(json.dumps({"timestamp":now.isoformat(),
        "market_source":"Yahoo completed 1h bars, INDICATIVE not executable fills",
        "results":result},indent=2)+"\n")
    lines=["# Autonomous Arena — $100 virtual accounts","",
      "**Rule-based simulated workers, NOT LLM agents or Alpaca orders.**",
      "Stocks/crypto indicative Yahoo hourly prices; NO options executed.",
      "All 10 workers start at $100; no real money or new AI charges.","",
      "Updated: "+now.isoformat(),"",
      "| Worker | Virtual action | Equity | Cash | Council |",
      "|---|---|---:|---:|---|"]
    from generation_manager import alias
    for wid,r in result.items():
        public_name=alias(wid,accounts[wid].get("generation_index",0))
        eq="Unavailable" if r.get("equity") is None else str(round(r["equity"],2))
        lines.append("| {} | {} | {} | {} | {} |".format(public_name,r["action"],eq,r.get("cash","—"),r.get("council","QUARANTINED")))
    lines+=["","**Review status:** Missing independently executable market quotes means",
      "the evidence council cannot certify a real-world trading edge.",""]
    (out/"DASHBOARD.md").write_text("\n".join(lines))
    print("Saved",len(result),"virtual worker snapshots")
if __name__=="__main__":main()
