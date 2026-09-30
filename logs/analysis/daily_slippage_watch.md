# Daily Slippage Watch
*Updated: 2026-09-30 18:06 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-09-30 | 1 | -0.55% | -0.05pp | 1/1 | -0.0315% | **OK** |
| 2026-09-29 | 2 | -0.53% | -0.03pp | 2/2 | -0.0315% | **OK** |
| 2026-09-28 | 1 | -0.94% | -0.44pp | 1/1 | -0.0315% | **WATCH** |
| 2026-09-25 | 2 | -0.94% | -0.44pp | 1/2 | -0.0315% | **WATCH** |
| 2026-09-24 | 2 | -0.86% | -0.36pp | 2/2 | -0.0315% | **OK** |
| 2026-09-23 | 2 | -1.97% | -1.47pp | 1/2 | -0.0315% | **ALERT** |
| 2026-09-22 | 2 | -1.32% | -0.82pp | 1/2 | -0.0315% | **ALERT** |
| 2026-09-21 | 3 | -0.66% | -0.16pp | 3/3 | -0.0315% | **OK** |
| 2026-09-18 | 2 | -1.53% | -1.03pp | 1/2 | -0.0315% | **ALERT** |
| 2026-09-17 | 2 | -0.69% | -0.19pp | 2/2 | -0.0315% | **OK** |

## Today (2026-09-30) detail

- Stop count: **1**
- Mean stop P&L: **-0.55%** (overshoot -0.05pp)
- Within -1.0%: 1/1
- Worst: CMS -0.6%
- Stop execution methods:
  - `market_urgent_full`: 1

## Historical baseline (all logs)
- Stop samples: 499
- Mean stop P&L: -1.33%
- Mean overshoot: -0.83pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
