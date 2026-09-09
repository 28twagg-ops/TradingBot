# Daily Slippage Watch
*Updated: 2026-09-09 13:56 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-09-09 | 2 | -1.06% | -0.56pp | 1/2 | -0.0345% | **WATCH** |
| 2026-09-08 | 3 | -0.55% | -0.05pp | 3/3 | -0.0345% | **OK** |
| 2026-09-04 | 1 | -0.61% | -0.11pp | 1/1 | -0.0345% | **OK** |
| 2026-09-03 | 1 | -0.70% | -0.20pp | 1/1 | -0.0345% | **OK** |
| 2026-09-02 | 3 | -1.34% | -0.84pp | 2/3 | -0.0345% | **ALERT** |
| 2026-09-01 | 3 | -0.79% | -0.29pp | 2/3 | -0.0345% | **OK** |
| 2026-08-31 | 5 | -1.05% | -0.55pp | 3/5 | -0.0345% | **WATCH** |
| 2026-08-28 | 2 | -0.75% | -0.25pp | 2/2 | -0.0345% | **OK** |
| 2026-08-27 | 2 | -0.55% | -0.05pp | 2/2 | -0.0345% | **OK** |

## Today (2026-09-09) detail

- Stop count: **2**
- Mean stop P&L: **-1.06%** (overshoot -0.56pp)
- Within -1.0%: 1/2
- Worst: MGM -1.2%, MKSI -0.9%
- Stop execution methods:
  - `market_urgent_full`: 2

## Historical baseline (all logs)
- Stop samples: 464
- Mean stop P&L: -1.36%
- Mean overshoot: -0.86pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
