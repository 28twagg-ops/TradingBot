# Daily Slippage Watch
*Updated: 2026-08-11 16:06 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-08-11 | 6 | -0.83% | -0.33pp | 4/6 | -0.0367% | **OK** |
| 2026-08-10 | 2 | -1.25% | -0.76pp | 1/2 | -0.0367% | **ALERT** |
| 2026-08-07 | 1 | -0.52% | -0.02pp | 1/1 | -0.0367% | **OK** |
| 2026-08-06 | 1 | -0.71% | -0.21pp | 1/1 | -0.0367% | **OK** |
| 2026-08-05 | 2 | -0.66% | -0.16pp | 2/2 | -0.0367% | **OK** |
| 2026-08-04 | 1 | -0.66% | -0.16pp | 1/1 | -0.0367% | **OK** |
| 2026-08-03 | 5 | -0.57% | -0.07pp | 5/5 | -0.0367% | **OK** |
| 2026-07-31 | 3 | -0.57% | -0.07pp | 3/3 | -0.0367% | **OK** |
| 2026-07-30 | 4 | -2.35% | -1.85pp | 0/4 | -0.0367% | **ALERT** |
| 2026-07-29 | 4 | -4.71% | -4.21pp | 3/4 | -0.0367% | **ALERT** |

## Today (2026-08-11) detail

- Stop count: **6**
- Mean stop P&L: **-0.83%** (overshoot -0.33pp)
- Within -1.0%: 4/6
- Worst: GOOG -1.4%, CDW -1.3%, ADM -0.6%, AIG -0.6%, AAPL -0.6%
- Stop execution methods:
  - `market_urgent_full`: 6

## Historical baseline (all logs)
- Stop samples: 424
- Mean stop P&L: -1.41%
- Mean overshoot: -0.91pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
