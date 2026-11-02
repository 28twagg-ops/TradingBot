#!/usr/bin/env python3
"""Research-only validation of daily-bar Rubber Band signals.

Inputs: one or more per-symbol OHLCV CSV files, with Date,Open,High,Low,Close,Volume.
A signal is formed AFTER the day's close, and can only be entered at NEXT day's open.
No downloads, broker calls, strategy mutation, or live order paths.
"""
import argparse
import csv
import json
import math
from collections import defaultdict
from datetime import datetime
from pathlib import Path

SCENARIOS = {"ideal": (0.0, 0.0), "realistic": (10.0, 1.0), "harsh": (30.0, 2.0)}
# Each scenario: per-side slippage in basis points; per-side fixed commission ($).

def read_symbol(path):
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            try:
                day = r.get("Date") or r.get("date") or r.get("timestamp")
                dt = datetime.fromisoformat(day[:10]).date()
                vals = {k: float(r.get(k, r.get(k.lower()))) for k in ("Open","High","Low","Close","Volume")}
                if not (0 < vals["Low"] <= min(vals["Open"], vals["Close"]) <= max(vals["Open"], vals["Close"]) <= vals["High"] and vals["Volume"] >= 0):
                    raise ValueError("invalid OHLCV")
                rows.append(dict(date=str(dt), **vals))
            except (TypeError, ValueError, KeyError) as e:
                raise ValueError(f"{path}: invalid bar {r}: {e}") from e
    rows.sort(key=lambda x: x["date"])
    if len({x["date"] for x in rows}) != len(rows):
        raise ValueError(f"{path}: duplicate dates")
    return rows

def signals(bars):
    for i in range(20, len(bars)-1):
        today, yesterday = bars[i], bars[i-1]
        gap = today["Open"] / yesterday["Close"] - 1
        midpoint = (today["High"] + today["Low"]) / 2
        # Matches historical_backtest.py's rubber_band expression, but delayed.
        if gap <= -0.015 and today["Close"] > midpoint:
            yield i

def simulate(symbols, slip_bps, fee, hold, stop_pct, capital, split_date):
    candidates = []
    for sym, bars in symbols.items():
        for i in signals(bars):
            if i + hold >= len(bars): continue
            entry_date = bars[i+1]["date"]
            # Non-overlap positions PER SYMBOL, checked in calendar order below.
            candidates.append((entry_date, sym, i))
    candidates.sort()
    last_exit = {}
    # One share per trade, no compounding or invented leverage: net P&L per share.
    result = []
    for entry_date, sym, i in candidates:
        bars = symbols[sym]
        exit_idx = i + hold
        if entry_date <= last_exit.get(sym, ""): continue
        raw_entry = bars[i+1]["Open"]
        entry = raw_entry * (1 + slip_bps / 10000)
        stop = raw_entry * (1-stop_pct) if stop_pct else None
        raw_exit = bars[exit_idx]["Close"]
        exit_date = bars[exit_idx]["date"]
        reason = "time"
        for j in range(i+1, exit_idx+1):
            b = bars[j]
            if stop is not None and b["Open"] <= stop:
                raw_exit, exit_date, reason = b["Open"], b["date"], "gap_stop"
                break
            if stop is not None and b["Low"] <= stop:
                raw_exit, exit_date, reason = stop, b["date"], "stop"
                break
        sold = max(0, raw_exit * (1-slip_bps/10000))
        pnl = sold-entry-2*fee
        result.append({"symbol":sym,"signal_date":bars[i]["date"],"entry_date":entry_date,
                       "exit_date":exit_date,"entry_price":round(entry,5),"exit_price":round(sold,5),
                       "net_pnl_per_share":round(pnl,5),"net_return_on_entry":pnl/entry,
                       "reason":reason,"period":"out_of_sample" if entry_date >= split_date else "in_sample"})
        last_exit[sym] = exit_date
    return result

def stats(trades):
    if not trades:return {"trades":0,"status":"INSUFFICIENT_DATA"}
    pnls = [t["net_pnl_per_share"] for t in trades]
    gains = sum(x for x in pnls if x>0); losses = -sum(x for x in pnls if x<0)
    returns = [t["net_return_on_entry"] for t in trades]
    return {"trades":len(trades),"win_rate":round(sum(x>0 for x in pnls)/len(pnls),4),
            "profit_factor":round(gains/losses,4) if losses else None,
            "mean_net_return":round(sum(returns)/len(returns),6),
            "gross_profit_per_share":round(gains,4),"gross_loss_per_share":round(losses,4)}
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--data-dir", type=Path, required=True, help="CSV files, one per symbol")
    p.add_argument("--output-dir", type=Path, default=Path("simulations/results/rubber_band_validation"))
    p.add_argument("--split-date", default="2024-01-01", help="Untouched out-of-sample boundary YYYY-MM-DD")
    p.add_argument("--hold-bars",type=int,default=3)
    p.add_argument("--stop-pct",type=float,default=0.005)
    p.add_argument("--starting-capital",type=float,default=500)
    args=p.parse_args()
    datetime.fromisoformat(args.split_date)
    if args.hold_bars<1 or not 0<=args.stop_pct<1 or args.starting_capital<=0: p.error("invalid hold, stop or capital")
    paths=sorted(args.data_dir.glob("*.csv"))
    if not paths:p.error("no CSV files; refusing to fabricate historical bars")
    symbols={x.stem.upper():read_symbol(x) for x in paths}
    args.output_dir.mkdir(parents=True,exist_ok=True)
    summary={"status":"RESEARCH_ONLY_NOT_LIVE_APPROVED","method":"close-confirmed signal; next-session open entry",
             "warnings":["Daily OHLC cannot establish intraday stop ordering or real fills.",
                         "One-share independent-trade analysis, not portfolio equity or Sharpe.",
                         "CSV survivorship and corporate-action adjustments require separate review.",
                         "Cost assumptions are scenarios, not broker-observed fills.",
                         "Current historical_backtest.py rubber_band has same-day look-ahead risk."],
             "split_date":args.split_date,"hold_bars":args.hold_bars,"stop_pct":args.stop_pct,
             "starting_capital_reference_only":args.starting_capital,"scenarios":{}}
    for name,(bps,fee) in SCENARIOS.items():
        trades=simulate(symbols,bps,fee,args.hold_bars,args.stop_pct,args.starting_capital,args.split_date)
        with open(args.output_dir/f"{name}_trades.csv","w",newline="") as f:
            writer=csv.DictWriter(f,fieldnames=["symbol","signal_date","entry_date","exit_date","entry_price","exit_price","net_pnl_per_share","net_return_on_entry","reason","period"])
            writer.writeheader();writer.writerows(trades)
        summary["scenarios"][name]={"assumptions":{"slippage_bps_per_side":bps,"fee_dollars_per_side_per_share":fee},
            "overall":stats(trades),"in_sample":stats([t for t in trades if t["period"]=="in_sample"]),
            "out_of_sample":stats([t for t in trades if t["period"]=="out_of_sample"])}
    oos=summary["scenarios"]["harsh"]["out_of_sample"]
    summary["gate"]="BLOCK" if oos["trades"]<200 or oos.get("profit_factor") is None or oos["profit_factor"]<=1.2 else "REVIEW_REQUIRED"
    (args.output_dir/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
    print(json.dumps({"gate":summary["gate"],"output":str(args.output_dir),"scenario_metrics":summary["scenarios"]},indent=2))
if __name__=="__main__":main()
