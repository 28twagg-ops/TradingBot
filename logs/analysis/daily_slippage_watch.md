# Daily Slippage Watch
*Updated: 2026-08-03 14:40 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-08-03 | 3 | -0.59% | -0.09pp | 3/3 | -0.0373% | **OK** |
| 2026-07-31 | 3 | -0.57% | -0.07pp | 3/3 | -0.0373% | **OK** |
| 2026-07-30 | 4 | -2.35% | -1.85pp | 0/4 | -0.0373% | **ALERT** |
| 2026-07-29 | 4 | -4.71% | -4.21pp | 3/4 | -0.0373% | **ALERT** |
| 2026-07-28 | 2 | -0.59% | -0.09pp | 2/2 | -0.0373% | **OK** |
| 2026-07-27 | 4 | -0.68% | -0.18pp | 4/4 | -0.0373% | **OK** |
| 2026-07-23 | 2 | -0.99% | -0.49pp | 1/2 | -0.0373% | **WATCH** |
| 2026-07-22 | 1 | -0.51% | -0.01pp | 1/1 | -0.0373% | **OK** |
| 2026-07-21 | 5 | -0.92% | -0.42pp | 3/5 | -0.0373% | **WATCH** |

## Today (2026-08-03) detail

- Stop count: **3**
- Mean stop P&L: **-0.59%** (overshoot -0.09pp)
- Within -1.0%: 3/3
- Worst: PWR -0.7%, ALGN -0.5%, CPT -0.5%
- Stop execution methods:
  - `market_urgent_full`: 3

## Historical baseline (all logs)
- Stop samples: 409
- Mean stop P&L: -1.44%
- Mean overshoot: -0.94pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
