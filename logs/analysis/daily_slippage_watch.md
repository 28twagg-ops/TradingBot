# Daily Slippage Watch
*Updated: 2026-07-08 14:46 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-07-08 | 1 | -2.36% | -1.86pp | 0/1 | -0.0421% | **ALERT** |
| 2026-07-07 | 2 | -1.92% | -1.42pp | 0/2 | -0.0421% | **ALERT** |
| 2026-07-02 | 3 | -0.54% | -0.04pp | 3/3 | -0.0421% | **OK** |
| 2026-07-01 | 1 | -0.56% | -0.06pp | 1/1 | -0.0421% | **OK** |
| 2026-06-30 | 1 | -0.95% | -0.45pp | 1/1 | -0.0421% | **WATCH** |
| 2026-06-26 | 6 | -1.37% | -0.87pp | 4/6 | -0.0421% | **ALERT** |
| 2026-06-25 | 2 | -0.67% | -0.17pp | 2/2 | -0.0421% | **OK** |

## Today (2026-07-08) detail

- Stop count: **1**
- Mean stop P&L: **-2.36%** (overshoot -1.86pp)
- Within -1.0%: 0/1
- Worst: DECK -2.4%
- Stop execution methods:
  - `market_urgent_full`: 1

## Historical baseline (all logs)
- Stop samples: 362
- Mean stop P&L: -1.47%
- Mean overshoot: -0.97pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
