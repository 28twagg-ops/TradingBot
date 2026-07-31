# Daily Slippage Watch
*Updated: 2026-07-31 14:17 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-07-31 | 2 | -0.55% | -0.05pp | 2/2 | -0.0374% | **OK** |
| 2026-07-30 | 4 | -2.35% | -1.85pp | 0/4 | -0.0374% | **ALERT** |
| 2026-07-29 | 4 | -4.71% | -4.21pp | 3/4 | -0.0374% | **ALERT** |
| 2026-07-28 | 2 | -0.59% | -0.09pp | 2/2 | -0.0374% | **OK** |
| 2026-07-27 | 4 | -0.68% | -0.18pp | 4/4 | -0.0374% | **OK** |
| 2026-07-23 | 2 | -0.99% | -0.49pp | 1/2 | -0.0374% | **WATCH** |
| 2026-07-22 | 1 | -0.51% | -0.01pp | 1/1 | -0.0374% | **OK** |
| 2026-07-21 | 5 | -0.92% | -0.42pp | 3/5 | -0.0374% | **WATCH** |
| 2026-07-20 | 3 | -0.59% | -0.09pp | 3/3 | -0.0374% | **OK** |

## Today (2026-07-31) detail

- Stop count: **2**
- Mean stop P&L: **-0.55%** (overshoot -0.05pp)
- Within -1.0%: 2/2
- Worst: FFIV -0.6%, CI -0.5%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 405
- Mean stop P&L: -1.45%
- Mean overshoot: -0.95pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
