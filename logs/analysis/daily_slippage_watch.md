# Daily Slippage Watch
*Updated: 2026-09-02 16:36 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-09-02 | 3 | -1.34% | -0.84pp | 2/3 | -0.0351% | **ALERT** |
| 2026-09-01 | 3 | -0.79% | -0.29pp | 2/3 | -0.0351% | **OK** |
| 2026-08-31 | 5 | -1.05% | -0.55pp | 3/5 | -0.0351% | **WATCH** |
| 2026-08-28 | 2 | -0.75% | -0.25pp | 2/2 | -0.0351% | **OK** |
| 2026-08-27 | 2 | -0.55% | -0.05pp | 2/2 | -0.0351% | **OK** |
| 2026-08-26 | 3 | -0.77% | -0.27pp | 2/3 | -0.0351% | **OK** |
| 2026-08-25 | 3 | -0.67% | -0.17pp | 3/3 | -0.0351% | **OK** |
| 2026-08-24 | 1 | -0.59% | -0.09pp | 1/1 | -0.0351% | **OK** |
| 2026-08-21 | 1 | -0.65% | -0.15pp | 1/1 | -0.0351% | **OK** |

## Today (2026-09-02) detail

- Stop count: **3**
- Mean stop P&L: **-1.34%** (overshoot -0.84pp)
- Within -1.0%: 2/3
- Worst: BWXT -2.3%, AIZ -0.9%, SYNA -0.8%
- Stop execution methods:
  - `market_urgent_full`: 3

## Historical baseline (all logs)
- Stop samples: 457
- Mean stop P&L: -1.37%
- Mean overshoot: -0.87pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
