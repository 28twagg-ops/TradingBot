# Daily Slippage Watch
*Updated: 2026-06-18 14:15 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-06-18 | 2 | -0.92% | -0.42pp | 1/2 | -0.0492% | **WATCH** |
| 2026-06-17 | 34 | -0.83% | -0.33pp | 26/34 | -0.0492% | **OK** |
| 2026-06-16 | 30 | -1.56% | -1.06pp | 9/30 | -0.0442% | **ALERT** |
| 2026-06-15 | 27 | -2.03% | -1.53pp | 9/27 | -0.0492% | **ALERT** |
| 2026-06-12 | 27 | -1.39% | -0.89pp | 10/27 | -0.0404% | **ALERT** |
| 2026-06-11 | 12 | -4.16% | -3.66pp | 1/12 | -0.0383% | **ALERT** |
| 2026-06-10 | 8 | -3.63% | -3.13pp | 2/8 | -0.0458% | **ALERT** |
| 2026-06-09 | 17 | -1.04% | -0.54pp | 11/17 | -0.0492% | **WATCH** |
| 2026-06-08 | 6 | -1.61% | -1.11pp | 3/6 | -0.0492% | **ALERT** |
| 2026-06-05 | 9 | -2.10% | -1.60pp | 1/9 | -0.0492% | **ALERT** |

## Today (2026-06-18) detail

- Stop count: **2**
- Mean stop P&L: **-0.92%** (overshoot -0.42pp)
- Within -1.0%: 1/2
- Worst: CF -1.0%, VC -0.8%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 247
- Mean stop P&L: -1.68%
- Mean overshoot: -1.18pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
