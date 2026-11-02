#!/usr/bin/env python3
"""Fetch traceable daily stock bars for unattended, research-only Rubber Band validation."""
import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
import yfinance as yf

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--symbols", default="SPY,AAPL,MSFT,NVDA,AMD,GOOGL,AMZN,META,TSLA,JPM,XOM,JNJ")
    ap.add_argument("--start",default="2015-01-01")
    ap.add_argument("--output-dir",type=Path,default=Path("data/validation_csv"))
    args=ap.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    manifest={"retrieved_at_utc":datetime.now(timezone.utc).isoformat(),"source":"Yahoo Finance via yfinance; research use only",
              "auto_adjust":True,"start":args.start,"symbols":{},"warnings":["Selected present-day tickers: survivorship bias possible.","OHLC is adjusted by yfinance; verify split/dividend behavior and timestamp chronology.","This is not live quote or option-chain execution data."]}
    good=0
    for symbol in [x.strip().upper() for x in args.symbols.split(",") if x.strip()]:
        try:
            df=yf.download(symbol,start=args.start,auto_adjust=True,progress=False,threads=False)
            if df.empty or len(df)<300: raise ValueError("fewer than 300 bars")
            # yfinance currently may return MultiIndex columns for one ticker.
            if hasattr(df.columns,"nlevels") and df.columns.nlevels>1:
                df.columns=df.columns.get_level_values(0)
            columns=["Open","High","Low","Close","Volume"]
            if not all(x in df.columns for x in columns): raise ValueError("OHLCV missing")
            df=df[columns].dropna()
            if len(df)<300: raise ValueError("too many missing values")
            target=args.output_dir/f"{symbol}.csv"
            with target.open("w",newline="") as f:
                writer=csv.writer(f);writer.writerow(["Date"]+columns)
                for date,row in df.iterrows():
                    writer.writerow([str(date.date())]+[float(row[k]) for k in columns])
            manifest["symbols"][symbol]={"bars":len(df),"first_date":str(df.index[0].date()),
                                          "last_date":str(df.index[-1].date()),"status":"downloaded"}
            good+=1
        except Exception as exc:
            manifest["symbols"][symbol]={"status":"FAILED","error":str(exc)[:250]}
    (args.output_dir/"source_manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    print(json.dumps(manifest,indent=2))
    # Strict minimum - one missing symbol is not a silent success.
    if good != len(manifest["symbols"]):raise SystemExit("INCOMPLETE_SOURCE_DATA: some symbols failed")
if __name__=="__main__":main()
