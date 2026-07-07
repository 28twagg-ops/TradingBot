# Daily Slippage Watch
*Updated: 2026-07-07 21:10 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-07-07 | 2 | -1.92% | -1.42pp | 0/2 | -0.0422% | **ALERT** |
| 2026-07-02 | 3 | -0.54% | -0.04pp | 3/3 | -0.0422% | **OK** |
| 2026-07-01 | 1 | -0.56% | -0.06pp | 1/1 | -0.0422% | **OK** |
| 2026-06-30 | 1 | -0.95% | -0.45pp | 1/1 | -0.0422% | **WATCH** |
| 2026-06-26 | 6 | -1.37% | -0.87pp | 4/6 | -0.0422% | **ALERT** |
| 2026-06-25 | 2 | -0.67% | -0.17pp | 2/2 | -0.0422% | **OK** |
| 2026-06-24 | 24 | -1.48% | -0.98pp | 11/24 | -0.0422% | **ALERT** |

## Today (2026-07-07) detail

- Stop count: **2**
- Mean stop P&L: **-1.92%** (overshoot -1.42pp)
- Within -1.0%: 0/2
- Worst: BWA -2.6%, F -1.2%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 361
- Mean stop P&L: -1.47%
- Mean overshoot: -0.97pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
