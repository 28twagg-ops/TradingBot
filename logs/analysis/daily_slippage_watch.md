# Daily Slippage Watch
*Updated: 2026-08-18 19:21 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-08-18 | 4 | -0.54% | -0.04pp | 4/4 | -0.0359% | **OK** |
| 2026-08-17 | 2 | -0.54% | -0.04pp | 2/2 | -0.0359% | **OK** |
| 2026-08-14 | 1 | -0.56% | -0.06pp | 1/1 | -0.0359% | **OK** |
| 2026-08-12 | 2 | -0.74% | -0.24pp | 2/2 | -0.0359% | **OK** |
| 2026-08-11 | 6 | -0.83% | -0.33pp | 4/6 | -0.0359% | **OK** |
| 2026-08-10 | 2 | -1.25% | -0.76pp | 1/2 | -0.0359% | **ALERT** |
| 2026-08-07 | 1 | -0.52% | -0.02pp | 1/1 | -0.0359% | **OK** |
| 2026-08-06 | 1 | -0.71% | -0.21pp | 1/1 | -0.0359% | **OK** |
| 2026-08-05 | 2 | -0.66% | -0.16pp | 2/2 | -0.0359% | **OK** |

## Today (2026-08-18) detail

- Stop count: **4**
- Mean stop P&L: **-0.54%** (overshoot -0.04pp)
- Within -1.0%: 4/4
- Worst: AEE -0.6%, AKAM -0.5%, AFL -0.5%, AON -0.5%
- Stop execution methods:
  - `market_urgent_full`: 4

## Historical baseline (all logs)
- Stop samples: 433
- Mean stop P&L: -1.40%
- Mean overshoot: -0.90pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
