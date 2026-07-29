# Daily Slippage Watch
*Updated: 2026-07-29 14:24 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-07-29 | 2 | -8.71% | -8.21pp | 1/2 | -0.0386% | **ALERT** |
| 2026-07-28 | 2 | -0.59% | -0.09pp | 2/2 | -0.0386% | **OK** |
| 2026-07-27 | 4 | -0.68% | -0.18pp | 4/4 | -0.0386% | **OK** |
| 2026-07-23 | 2 | -0.99% | -0.49pp | 1/2 | -0.0386% | **WATCH** |
| 2026-07-22 | 1 | -0.51% | -0.01pp | 1/1 | -0.0386% | **OK** |
| 2026-07-21 | 5 | -0.92% | -0.42pp | 3/5 | -0.0386% | **WATCH** |
| 2026-07-20 | 3 | -0.59% | -0.09pp | 3/3 | -0.0386% | **OK** |
| 2026-07-17 | 3 | -0.72% | -0.22pp | 3/3 | -0.0386% | **OK** |
| 2026-07-16 | 2 | -0.66% | -0.16pp | 2/2 | -0.0386% | **OK** |

## Today (2026-07-29) detail

- Stop count: **2**
- Mean stop P&L: **-8.71%** (overshoot -8.21pp)
- Within -1.0%: 1/2
- Worst: LII -16.4%, HLT -1.0%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 397
- Mean stop P&L: -1.45%
- Mean overshoot: -0.95pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
