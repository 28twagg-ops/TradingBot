"""Reproducible, cost-aware historical research for deterministic Arena rules.

Research report only: daily bars cannot certify the hourly live paper worker.
No AI code execution, broker calls, or promotion evidence written.
"""
import argparse
import datetime as dt
import json
import math
from pathlib import Path
from run_virtual import signal, UTC

SYMBOLS = ("SPY", "QQQ", "BTC-USD", "ETH-USD")
FEE = 0.0025  # per-side conservative combined fee/slippage assumption
WARMUP = 90

def simulate(closes, opens, worker, generation, start, end, fee=FEE):
    """At close i determine signal, execute at next bar open i+1."""
    if not (len(closes) == len(opens) and 0 <= start < end <= len(closes)):
        raise ValueError("BAD_BARS")
    if any(not math.isfinite(v) or v <= 0 for v in closes + opens):
        raise ValueError("BAD_PRICE")
    cash, shares, peak, drawdown, fills = 100.0, 0.0, 100.0, 0.0, 0
    curve = []
    for i in range(start, end):
        # Decision at yesterday's close, filled at today's open.
        if i > WARMUP:
            action = signal(worker, closes[:i], generation)
            price = opens[i]
            if action > 0 and shares == 0:
                shares = cash * (1-fee) / price
                cash = 0.0
                fills += 1
            elif action < 0 and shares > 0:
                cash = shares * price * (1-fee)
                shares = 0.0
                fills += 1
        nav = cash + shares * closes[i]
        peak = max(peak, nav)
        drawdown = max(drawdown, 100 * (1-nav/peak))
        curve.append(round(nav, 6))
    final = cash + shares * closes[end-1] * (1-fee if shares else 1)
    return {"net_return_pct": round(final-100, 4),
            "max_drawdown_pct": round(drawdown, 4),
            "fills": fills, "bars": end-start, "equity_curve": curve}

def research(symbol, closes, opens, worker, incumbent, successor):
    if len(closes) < 365 or len(closes) != len(opens):
        return {"status": "INSUFFICIENT_HISTORY"}
    split = int(len(closes) * 0.7)
    if len(closes)-split < 90:
        return {"status": "INSUFFICIENT_OUT_OF_SAMPLE"}
    train_old = simulate(closes, opens, worker, incumbent, WARMUP, split)
    train_new = simulate(closes, opens, worker, successor, WARMUP, split)
    # Both strategies are predetermined, never tuned on the test interval.
    test_old = simulate(closes, opens, worker, incumbent, split, len(closes))
    test_new = simulate(closes, opens, worker, successor, split, len(closes))
    return {"status": "RESEARCH_ONLY_NOT_PROMOTION_PROOF", "symbol": symbol,
            "incumbent_generation_index": incumbent, "candidate_generation_index": successor,
            "training": {"incumbent": train_old, "candidate": train_new},
            "out_of_sample": {"incumbent": test_old, "candidate": test_new},
            "limitations": "Daily-bar proxy, not the hourly multi-asset Arena execution. "
                           "Yahoo adjusted prices and open/close adjustments may differ. "
                           "No spread or market-impact observations; 25bp per side modeled. "
                           "No real executable fills. Repeated evaluation risks overfitting."}

def fetch_daily(symbol):
    import yfinance as yf
    data = yf.download(symbol, period="5y", interval="1d", auto_adjust=True,
                       progress=False, threads=False, timeout=15)
    if data.empty:
        raise ValueError("EMPTY_HISTORY")
    if hasattr(data.columns, "levels"):
        data.columns = [str(x[0]).lower() for x in data.columns]
    else:
        data.columns = [str(x).lower() for x in data.columns]
    data = data.dropna(subset=["open", "close"])
    return [float(x) for x in data["close"]], [float(x) for x in data["open"]]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", required=True)
    args = parser.parse_args()
    root = Path(args.dir)
    registry = json.loads((root / "generation_registry.json").read_text())
    results = {}
    # Fixed, predetermined symbol assignments; no current-index constituent filtering.
    for wid, slot in registry["workers"].items():
        symbol = SYMBOLS[(int(wid[1:])-1) % len(SYMBOLS)]
        try:
            close, opening = fetch_daily(symbol)
            results[wid] = research(symbol, close, opening, wid,
                                    slot["index"], slot["index"]+1)
        except (ValueError, OSError, RuntimeError, KeyError, TypeError) as exc:
            results[wid] = {"status": "DATA_UNAVAILABLE", "error_type": type(exc).__name__}
    report = {"generated_at": dt.datetime.now(UTC).isoformat(),
              "status": "RESEARCH_ONLY_NO_AUTOMATIC_PROMOTION",
              "execution": "signal prior daily close, fill next daily open",
              "universe": list(SYMBOLS), "per_side_cost_fraction": FEE,
              "workers": results}
    root.mkdir(parents=True, exist_ok=True)
    (root / "BACKTEST_RESEARCH.json").write_text(json.dumps(report, indent=2)+"\n")
    lines = ["# Arena historical research — NOT certified promotion evidence", "",
             "Daily-price proxy only; no live trading or automatic promotion.", "",
             "| Worker | Symbol | Incumbent OOS | Candidate OOS | Candidate fills | Status |",
             "|---|---|---:|---:|---:|---|"]
    for wid, result in results.items():
        if result["status"] == "RESEARCH_ONLY_NOT_PROMOTION_PROOF":
            old = result["out_of_sample"]["incumbent"]
            new = result["out_of_sample"]["candidate"]
            lines.append(f'| {wid} | {result["symbol"]} | {old["net_return_pct"]:+.2f}% | {new["net_return_pct"]:+.2f}% | {new["fills"]} | Research only |')
        else:
            lines.append(f'| {wid} | — | — | — | — | {result["status"]} |')
    (root / "BACKTEST_RESEARCH.md").write_text("\n".join(lines)+"\n")
    print("Wrote research-only comparison for", len(results), "workers")

if __name__ == "__main__":
    main()
