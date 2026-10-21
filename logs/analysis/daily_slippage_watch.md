# Daily Slippage Watch
*Updated: 2026-10-21 23:37 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-10-21 | 3 | -0.62% | -0.12pp | 3/3 | -0.0301% | **OK** |
| 2026-10-19 | 3 | -0.77% | -0.27pp | 2/3 | -0.0301% | **OK** |
| 2026-10-16 | 2 | -0.73% | -0.23pp | 2/2 | -0.0301% | **OK** |
| 2026-10-15 | 1 | -1.40% | -0.90pp | 0/1 | -0.0301% | **ALERT** |
| 2026-10-14 | 2 | -0.59% | -0.09pp | 2/2 | -0.0301% | **OK** |
| 2026-10-13 | 1 | -1.21% | -0.71pp | 0/1 | -0.0301% | **ALERT** |
| 2026-10-09 | 1 | -0.51% | -0.01pp | 1/1 | -0.0301% | **OK** |
| 2026-10-08 | 1 | -0.83% | -0.33pp | 1/1 | -0.0301% | **OK** |

## Today (2026-10-21) detail

- Stop count: **3**
- Mean stop P&L: **-0.62%** (overshoot -0.12pp)
- Within -1.0%: 3/3
- Worst: XYZ -0.8%, ADBE -0.6%, UAL -0.5%
- Stop execution methods:
  - `market_urgent_full`: 3

## Historical baseline (all logs)
- Stop samples: 519
- Mean stop P&L: -1.30%
- Mean overshoot: -0.80pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
