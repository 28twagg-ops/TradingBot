# Extensive Simulation Analysis — Synthesis (2026-06-17)

Master summary of the simulation plan runs. Source artifacts live in `TradingBot/simulations/results/` and this folder.

## Executive findings ($500 account, BOTH universe, gap model unless noted)

1. **Live stop slippage is the biggest real-world drag.** Empirical stops from `transactions.csv` (211 samples, mean **-1.82%**) crush returns vs the ideal gap model:
   - 3yr: +266% baseline → **+27%** with empirical stops (-238pp)
   - 20yr: +30,110% baseline → **+895%** with empirical stops (-29,214pp)

2. **Overnight PDT schedule is viable in sim** (afternoon entry, no same-day stops). `overnight_pdt_gaps` beats `strict_pdt` (hold losers, no intraday exit) at every horizon with slippage adjustment.

3. **Live 7 strategies are all profitable standalone** across 3yr/7yr/20yr. RubberBand is weakest OOS; expansion candidates (ADX_DI_14, SMA_20_50, Keltner_BO) dominate on longer horizons.

4. **MIN_TRADE_SIZE = 0.01** aligned with live bot — unlimited fractional entries in portfolio sim.

---

## Overnight PDT validation (scheduled portfolio, slippage-adjusted)

| Horizon | overnight_pdt_gaps | intraday_stops | overnight_morning | strict_pdt |
|---------|-------------------|----------------|-------------------|------------|
| 3yr     | +244.7%           | +819.1%        | +45.4%*           | +1.0%      |
| 7yr     | +1403.9%          | +5176.3%       | +45.4%*           | +8.1%      |
| 20yr    | +7718.2%          | +21872.8%      | +609.2%           | +544.7%    |

\*7yr `overnight_morning` used fixed logic (was -58% before bugfix; 3yr pre-fix was -58%).

`overnight_pdt_gaps` = gap-aware stop model (recommended PDT-safe baseline). `intraday_stops` is not PDT-safe but shows upside if day-trade limits were removed.

---

## Strategy expansion — top OOS standalone (not all in live bot)

| Strategy       | 3yr OOS | 7yr OOS | 20yr OOS |
|----------------|---------|---------|----------|
| Keltner_BO     | +316%   | +1324%  | +7222%   |
| BB_Breakout_20 | +252%   | +900%   | +4010%   |
| ADX_DI_14      | —       | +778%   | +22765%  |
| SMA_20_50      | +184%   | +555%   | +16408%  |
| RubberBand     | +21.5%  | +107%   | +673%    |

Live scheduled portfolio (gap model): 3yr +1129% | 7yr +4594% | 20yr +30110% (headline % — see methodology report).

---

## Slippage & spread sensitivity

- **SELL slippage mean:** -0.058% (from live logs)
- **Stop-loss overshoot:** mean -1.82% vs modeled -0.5%
- **Bid-ask spread (Test 22, 3yr):** +266% at 0% spread → +48.5% at 0.30% round-trip

---

## Artifacts in this folder

| File | Description |
|------|-------------|
| `live_slippage_profile_2026-06-16.md` | Empirical slippage distribution |
| `return_methodology_report.md` | Why validation % ≠ portfolio sim % |
| `strategy_expansion_3yr_2026-06-16.md` | 3yr expansion study |
| `strategy_expansion_20yr_2026-06-17.md` | 20yr expansion study |
| `overnight_pdt_3yr_2026-06-16.md` | 3yr PDT modes |
| `overnight_pdt_20yr_2026-06-17.md` | 20yr PDT modes |
| `validation_test_22_33_3yr.txt` | Spread + empirical stop tests (refreshed cache) |
| `validation_20yr_test_2_3_6_17_22_33.txt` | Full 20yr validation subset |

---

## Out of scope (per plan)

No live bot strategy changes until user reviews these reports.
