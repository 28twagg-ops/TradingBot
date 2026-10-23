# Rainbow Curve BTC/ETH Back Analysis

Generated: 2026-10-16 10:51

## Method

- Model: `log10(price) = a · ln(days_since_origin) + b` (OLS), nine parallel bands at log10 offsets −0.4…+0.4.
- Walk-forward: each day fitted on history **through prior close only** (warmup ~730 days).
- Costs: 0.1% round-trip fee; full capital long-only.
- Origins: BTC `2009-01-03`, ETH `2015-08-07`. ETH uses the same methodology on its own history (no canonical ETH rainbow).

### Rules

| Rule | Entry | Exit |
|---|---|---|
| buy_hold | first valid day | end |
| deep_value | band ≤ 2 | band ≥ 8 |
| accumulate_distribute | band ≤ 3 | band ≥ 7 |
| center_fade | band < 6 | band ≥ 6 |

## BTC-USD

- History: **2014-09-17 → 2026-10-16** (4413 days, 3683 scored)
- **Now:** $81,328.06 | center $143,819.85 | residual -0.248 log10 | **band 3 — 3 Accumulate**
- Latest fit: a=2.5112, b=-16.8877, R²=0.9194

| Rule | Terminal | vs BH | CAGR | Max DD | Trades |
|---|---:|---:|---:|---:|---:|
| buy_hold | 133.86x | +0.0% | +62.5% | -83.4% | 1 |
| deep_value | 23.17x | -82.7% | +36.6% | -61.8% | 3 |
| accumulate_distribute | 10.98x | -91.8% | +26.8% | -61.8% | 3 |
| center_fade | 9.38x | -93.0% | +24.9% | -66.7% | 37 |

**Buy-and-hold wins** on terminal wealth (133.86x); no band-timing rule beat it.

## ETH-USD

- History: **2017-11-09 → 2026-10-16** (3264 days, 2534 scored)
- **Now:** $2,431.10 | center $3,551.75 | residual -0.165 log10 | **band 3 — 3 Accumulate**
- Latest fit: a=0.8536, b=-3.5478, R²=0.5788

| Rule | Terminal | vs BH | CAGR | Max DD | Trades |
|---|---:|---:|---:|---:|---:|
| buy_hold | 13.13x | +0.0% | +45.0% | -79.4% | 1 |
| deep_value | 1.54x | -88.3% | +6.4% | -67.6% | 1 |
| accumulate_distribute | 7.08x | -46.1% | +32.6% | -44.5% | 5 |
| center_fade | 4.96x | -62.2% | +26.0% | -56.6% | 59 |

**Buy-and-hold wins** on terminal wealth (13.13x); no band-timing rule beat it.

Equity curves: `rainbow_btc_eth_equity.csv`

## Caveats

- Rainbow is a **descriptive** long-cycle frame, not a proven alpha source; walk-forward reduces but does not eliminate fit instability early in history.
- Full capital in/out ignores position sizing, taxes, custody, and multi-year cash drag psychology.
- Past band timing that underperformed buy-hold is still useful as a risk dashboard (where we sit on the curve today).
