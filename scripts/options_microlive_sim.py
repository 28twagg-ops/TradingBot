"""
options_microlive_sim.py — $500 Micro-Live Paper Simulation

Simulates real live conditions (including slippage) on a $500 starting account
using $50/trade sizing. Used to verify strategy survivability before real $ deployment.
"""

import sys
import pandas as pd
import numpy as np
from pathlib import Path

def run_simulation(strategy_id: str, starting_capital: float = 500.0, trade_size: float = 50.0, slippage_pct: float = 0.02):
    ledger_path = Path("logs/options_trial/_ledger/master_ledger.csv")
    if not ledger_path.exists():
        print("No master ledger found.")
        return
        
    df = pd.read_csv(ledger_path)
    if "strategy_id" not in df.columns or "pnl_pct" not in df.columns:
        print("Ledger missing required columns.")
        return

    # Filter to exits for the target strategy
    exits = df[(df["strategy_id"] == strategy_id) & (df["event"].str.contains("exit|sell|close", case=False, na=False))].copy()
    if exits.empty:
        print(f"No exits found for {strategy_id}.")
        return

    exits["ts"] = pd.to_datetime(exits["ts"])
    exits = exits.sort_values("ts")
    exits["pnl_pct"] = pd.to_numeric(exits["pnl_pct"], errors="coerce")
    exits = exits.dropna(subset=["pnl_pct"])

    equity = starting_capital
    peak = starting_capital
    max_dd = 0.0

    print(f"=== MICRO-LIVE SIMULATION: {strategy_id} ===")
    print(f"Starting Capital: ${starting_capital:.2f}")
    print(f"Trade Size:       ${trade_size:.2f}")
    print(f"Slippage:         {slippage_pct*100:.1f}%\n")
    print(f"{'Date':<20} {'Raw PnL%':>10} {'Sim PnL$':>10} {'Equity':>10} {'Drawdown':>10}")
    print("-" * 65)

    for _, row in exits.iterrows():
        raw_pct = row["pnl_pct"]
        # Apply slippage (reduces wins, worsens losses)
        net_pct = raw_pct - slippage_pct
        
        # Calculate dollar PnL based on fixed trade size
        # Cap loss at 100% of trade size
        net_pct = max(-1.0, net_pct)
        trade_pnl = trade_size * net_pct
        
        equity += trade_pnl
        if equity > peak:
            peak = equity
        dd = (peak - equity) / peak if peak > 0 else 0
        if dd > max_dd:
            max_dd = dd

        dt_str = str(row["ts"])[:19]
        print(f"{dt_str:<20} {raw_pct*100:>9.1f}% {trade_pnl:>10.2f} {equity:>10.2f} {dd*100:>9.1f}%")
        
        if equity <= 0:
            print(f"\n[!] ACCOUNT BLOWN UP on {dt_str}")
            break

    print("-" * 65)
    print(f"Final Equity: ${equity:.2f} ({((equity/starting_capital)-1)*100:+.1f}%)")
    print(f"Max Drawdown: {max_dd*100:.1f}%")
    if equity > starting_capital:
        print("Verdict: SURVIVED - READY FOR REAL LIVE TRADING")
    else:
        print("Verdict: FAILED")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("strategy_id", help="Strategy ID to simulate (e.g. S174)")
    args = parser.parse_args()
    run_simulation(args.strategy_id)
