"""
options_microlive_sim.py - $500 Micro-Live Paper Simulation

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
    
    # Allow partial column matches to support various ledger formats
    strat_col = next((c for c in df.columns if 'strategy' in c.lower()), None)
    event_col = next((c for c in df.columns if 'event' in c.lower() or 'action' in c.lower()), None)
    pnl_col = next((c for c in df.columns if 'pnl_pct' in c or 'return_pct' in c), None)

    if not strat_col or not event_col or not pnl_col:
        print("Ledger missing required columns. Found:", df.columns.tolist())
        return

    # Filter to exits for the target strategy
    exits = df[(df[strat_col] == strategy_id) & (df[event_col].str.contains("exit|sell|close", case=False, na=False))].copy()
    if exits.empty:
        print(f"No exits found for {strategy_id}.")
        return

    exits["ts"] = pd.to_datetime(exits["ts"], format="mixed", utc=True)
    exits = exits.sort_values("ts")
    exits["pnl_pct"] = pd.to_numeric(exits[pnl_col], errors="coerce")
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

    wins = 0
    total = len(exits)

    for _, row in exits.iterrows():
        raw_pct = row["pnl_pct"]
        # Convert fraction to float percentage properly
        # E.g. raw_pct = 0.5 for 50%, not 50.0
        # The ledger stores pl_pct as decimal (0.50) or percentage (50.0). We normalize it.
        if abs(raw_pct) > 10.0:  # Assumed to be actual percent, e.g. 50.0
            raw_pct = raw_pct / 100.0
            
        # Apply slippage (reduces wins, worsens losses)
        net_pct = raw_pct - slippage_pct
        
        # Calculate dollar PnL based on fixed trade size
        # Cap loss at 100% of trade size
        net_pct = max(-1.0, net_pct)
        trade_pnl = trade_size * net_pct
        
        if trade_pnl > 0:
            wins += 1
            
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
    print(f"Win Rate:     {(wins/total)*100:.1f}%")
    
    if equity > starting_capital:
        print("Verdict: SURVIVED - READY FOR REAL LIVE TRADING")
    else:
        print("Verdict: FAILED")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("strategy_id", nargs="?", help="Strategy ID to simulate (e.g. S174)")
    parser.add_argument("--all", action="store_true", help="Run on all strategies with n>=5")
    args = parser.parse_args()
    
    if args.all:
        import pandas as pd
        df = pd.read_csv("logs/options_trial/_ledger/master_ledger.csv")
        strat_col = next((c for c in df.columns if 'strategy' in c.lower()), None)
        if strat_col:
            exits = df[df["event"].str.contains("exit|sell|close", case=False, na=False)]
            counts = exits[strat_col].value_counts()
            candidates = counts[counts >= 5].index
            for sid in candidates:
                run_simulation(sid)
                print("\n" + "="*80 + "\n")
    elif args.strategy_id:
        run_simulation(args.strategy_id)
    else:
        parser.print_help()
