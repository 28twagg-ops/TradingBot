# Daily Slippage Watch
*Updated: 2026-11-05 14:49 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-11-05 | 1 | -7.61% | -7.11pp | 0/1 | -0.0295% | **ALERT** |
| 2026-11-03 | 1 | -0.70% | -0.20pp | 1/1 | -0.0295% | **OK** |
| 2026-11-02 | 2 | -0.35% | +0.15pp | 2/2 | -0.0295% | **OK** |
| 2026-10-30 | 1 | -0.54% | -0.04pp | 1/1 | -0.0295% | **OK** |
| 2026-10-29 | 1 | -1.44% | -0.94pp | 0/1 | -0.0295% | **ALERT** |
| 2026-10-28 | 2 | -0.71% | -0.21pp | 2/2 | -0.0295% | **OK** |
| 2026-10-27 | 2 | -0.53% | -0.03pp | 2/2 | -0.0295% | **OK** |
| 2026-10-23 | 3 | -0.84% | -0.34pp | 2/3 | -0.0295% | **OK** |

## Today (2026-11-05) detail

- Stop count: **1**
- Mean stop P&L: **-7.61%** (overshoot -7.11pp)
- Within -1.0%: 0/1
- Worst: DASH -7.6%
- Stop execution methods:
  - `market_urgent_full`: 1

## Historical baseline (all logs)
- Stop samples: 533
- Mean stop P&L: -1.30%
- Mean overshoot: -0.80pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
