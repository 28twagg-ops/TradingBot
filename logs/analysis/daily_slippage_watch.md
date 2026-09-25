# Daily Slippage Watch
*Updated: 2026-09-25 15:47 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-09-25 | 1 | -1.39% | -0.89pp | 0/1 | -0.0321% | **ALERT** |
| 2026-09-24 | 2 | -0.86% | -0.36pp | 2/2 | -0.0321% | **OK** |
| 2026-09-23 | 2 | -1.97% | -1.47pp | 1/2 | -0.0321% | **ALERT** |
| 2026-09-22 | 2 | -1.32% | -0.82pp | 1/2 | -0.0321% | **ALERT** |
| 2026-09-21 | 3 | -0.66% | -0.16pp | 3/3 | -0.0321% | **OK** |
| 2026-09-18 | 2 | -1.53% | -1.03pp | 1/2 | -0.0321% | **ALERT** |
| 2026-09-17 | 2 | -0.69% | -0.19pp | 2/2 | -0.0321% | **OK** |
| 2026-09-16 | 5 | -0.62% | -0.12pp | 5/5 | -0.0321% | **OK** |
| 2026-09-15 | 4 | -0.85% | -0.35pp | 3/4 | -0.0321% | **OK** |
| 2026-09-14 | 1 | -0.58% | -0.08pp | 1/1 | -0.0321% | **OK** |

## Today (2026-09-25) detail

- Stop count: **1**
- Mean stop P&L: **-1.39%** (overshoot -0.89pp)
- Within -1.0%: 0/1
- Worst: KNF -1.4%
- Stop execution methods:
  - `market_urgent_full`: 1

## Historical baseline (all logs)
- Stop samples: 494
- Mean stop P&L: -1.33%
- Mean overshoot: -0.83pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
