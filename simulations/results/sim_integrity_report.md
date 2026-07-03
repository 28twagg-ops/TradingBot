# Options Sim Integrity Report (Gate 2A)

_DEVELOPMENT ONLY - NOT FOR TRADING DECISIONS_

Generated: 2026-07-03
Engine: `simulations/options_strategy_simulator.py`
Dataset: SYNTHETIC development data (Black-Scholes + adversarial spread model). Real Alpaca 1-min data required for Phase 3.

## Overall: ALL 6 PASS

| # | Check | Result |
|---|-------|--------|
| | 1. Zero Edge Baseline | PASS |
| | 2. Single Trade Audit | PASS |
| | 3. Boundary Check | PASS |
| | 4. Compounding Check | PASS |
| | 5. Fill Rate Reality Check | PASS |
| | 6. Liquidity Filter Audit | PASS |

## Details

### 1. Zero Edge Baseline - PASS

Random signals must lose money (spread + fees). Expected P&L/signal = $-1.76, total P&L = $-919.19 over 99 fills.

`{'exp_pnl_per_signal': -1.7575, 'total_pnl': -919.19, 'fills': 99}`

### 2. Single Trade Audit - PASS

Recomputed P&L for 5 filled trades within $0.02 of engine P&L; entry=limit(ask-$0.01), exit=bid>=0. Mismatches: none

`{'audited': 5, 'mismatches': 0}`

### 3. Boundary Check - PASS

Long options cannot lose >100% of premium (gross). Trades with >100% gross loss: 0 (must be 0). Trades flagged >500% gain (rare, informational): 0.

`{'over_100pct_loss': 0, 'over_500pct_gain': 0, 'fills': 109}`

### 4. Compounding Check - PASS

Equity curve sizes against RUNNING equity (the -191% bug fix). Checked 47 trades; consistency errors: none. First trade equity 500.00->498.92 

`{'trades': 47, 'errors': 0, 'final_equity': 324.55}`

### 5. Fill Rate Reality Check - PASS

Fill rate among tradeable signals = 16.5% (must be >10% and <95%; limit=ask-$0.01 fills only if next-window ask drops to the limit). 131/795 filled.

`{'fill_rate': 0.1648, 'filled': 131, 'tradeable': 795}`

### 6. Liquidity Filter Audit - PASS

72.6% of raw signals skipped by liquidity filters (must be >10% and <90%). Breakdown: {'spread>25%': 950, 'open_interest<100': 595, 'bid=0': 125, 'cost>$75': 508}

`{'skipped_frac': 0.726, 'skipped': 2178, 'considered': 3000, 'reasons': {'spread>25%': 950, 'open_interest<100': 595, 'bid=0': 125, 'cost>$75': 508}}`

## What this proves (and does not)

- PROVES: the engine applies fees, fill logic, compounding, and boundaries correctly; random trading loses money; liquidity filters and fill modelling behave sanely.
- DOES NOT PROVE: any strategy has real edge. That requires the production run on collected Alpaca 1-minute data (Phase 3), which cannot start until ~4 weeks of real data exist.
