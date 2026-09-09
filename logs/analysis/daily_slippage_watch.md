# Daily Slippage Watch
*Updated: 2026-09-09 18:16 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-09-09 | 3 | -0.88% | -0.38pp | 2/3 | -0.0343% | **OK** |
| 2026-09-08 | 3 | -0.55% | -0.05pp | 3/3 | -0.0343% | **OK** |
| 2026-09-04 | 1 | -0.61% | -0.11pp | 1/1 | -0.0343% | **OK** |
| 2026-09-03 | 1 | -0.70% | -0.20pp | 1/1 | -0.0343% | **OK** |
| 2026-09-02 | 3 | -1.34% | -0.84pp | 2/3 | -0.0343% | **ALERT** |
| 2026-09-01 | 3 | -0.79% | -0.29pp | 2/3 | -0.0343% | **OK** |
| 2026-08-31 | 5 | -1.05% | -0.55pp | 3/5 | -0.0343% | **WATCH** |
| 2026-08-28 | 2 | -0.75% | -0.25pp | 2/2 | -0.0343% | **OK** |
| 2026-08-27 | 2 | -0.55% | -0.05pp | 2/2 | -0.0343% | **OK** |

## Today (2026-09-09) detail

- Stop count: **3**
- Mean stop P&L: **-0.88%** (overshoot -0.38pp)
- Within -1.0%: 2/3
- Worst: MGM -1.2%, MKSI -0.9%, BAX -0.5%
- Stop execution methods:
  - `market_urgent_full`: 3

## Historical baseline (all logs)
- Stop samples: 465
- Mean stop P&L: -1.36%
- Mean overshoot: -0.86pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
