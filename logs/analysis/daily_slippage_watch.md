# Daily Slippage Watch
*Updated: 2026-07-14 21:40 UTC*

Tracks **stop P&L** (position loss vs entry) vs **execution slippage** (fill vs limit). Target: stops near -0.5% trigger when no overnight gap.

| Day | Stops | Mean stop | Overshoot vs -0.5% | Within -1% | SELL slip | Status |
|-----|-------|-----------|---------------------|------------|-----------|--------|
| 2026-07-14 | 3 | -0.56% | -0.06pp | 3/3 | -0.0402% | **OK** |
| 2026-07-13 | 6 | -0.64% | -0.14pp | 6/6 | -0.0402% | **OK** |
| 2026-07-10 | 1 | -0.54% | -0.04pp | 1/1 | -0.0402% | **OK** |
| 2026-07-08 | 2 | -1.44% | -0.94pp | 1/2 | -0.0402% | **ALERT** |
| 2026-07-07 | 2 | -1.92% | -1.42pp | 0/2 | -0.0402% | **ALERT** |
| 2026-07-02 | 3 | -0.54% | -0.04pp | 3/3 | -0.0402% | **OK** |
| 2026-07-01 | 1 | -0.56% | -0.06pp | 1/1 | -0.0402% | **OK** |

## Today (2026-07-14) detail

- Stop count: **3**
- Mean stop P&L: **-0.56%** (overshoot -0.06pp)
- Within -1.0%: 3/3
- Worst: HON -0.6%, NDSN -0.6%, NI -0.5%
- Stop execution methods:
  - `market_urgent_full`: 3

## Historical baseline (all logs)
- Stop samples: 373
- Mean stop P&L: -1.45%
- Mean overshoot: -0.95pp

**Alert** if overshoot < -0.8pp or mean stop < -1.2%. **OK** if overshoot > -0.5pp and mean stop > -0.9%.
