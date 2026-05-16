# 📊 Paper Bot — Performance Dashboard (PAPER TRADING)
*Updated: 2026-05-16 09:48 UTC*

> ⚠️ **Paper trading only — no real money involved.**

## Account Snapshot
| | |
|---|---|
| **Current Equity** | $99575.31 |
| **Starting Equity** | $100000.00 |
| **Total Return** | -0.42% ($-424.69) |
| **Max Drawdown** | -99.48% |
| **Current Cash** | $83958.29 |
| **Open Positions** | 0 () |
| **Last Run** | 2026-05-16 09:48:54 |

## Trade Performance
| Metric | Value |
|---|---|
| **Total Closed Trades** | 7 |
| **Win Rate** | 42.9% |
| **Avg Win** | +0.33% |
| **Avg Loss** | -1.98% |
| **Profit Factor** | 1.51x |
| **Avg Hold Days** | 0.0d |
| **Total Realised P&L** | $+9.88 |

## Tranche Feature  (new in paper bot)
| Parameter | Value |
|---|---|
| Tranche 1 (entry day) | 50% of target size |
| Tranche 2 (next day) | 50% — only if price ≤ entry×1.005 |
| Partial exit | Sell 50% at midline, ride rest to time/stop |

## Exit Reasons
| Exit | Trades | WR | Avg P&L% |
|---|---|---|---|
| `rsi_exit` | 4 | 75% | +0.21% |
| `stop_loss` | 3 | 0% | -2.59% |

## Recent Closed Trades
| Date | Ticker | Strategy | P&L% | P&L$ | Hold | Exit |
|---|---|---|---|---|---|---|
| 2026-05-16 | **LINKUSD** | `CryptoRSI` | -3.76% | $-0.09 | 0d | stop_loss (-3.8%) |
| 2026-05-16 | **ETHUSD** | `CryptoRSI` | -1.97% | $-14.00 | 0d | stop_loss (-2.0%) |
| 2026-05-10 | **BTCUSD** | `CryptoRSI` | +0.18% | $+5.25 | 0d | rsi_exit (RSI=68) |
| 2026-05-10 | **SOLUSD** | `CryptoRSI` | +0.47% | $+13.63 | 0d | rsi_exit (RSI=63) |
| 2026-05-10 | **LINKUSD** | `CryptoRSI` | -0.15% | $-4.35 | 0d | rsi_exit (RSI=58) |
| 2026-05-10 | **AVAXUSD** | `CryptoRSI` | +0.35% | $+10.38 | 0d | rsi_exit (RSI=64) |
| 2026-05-06 | **ACGL** | `Pullback50` | -2.04% | $-0.94 | 0d | stop_loss (-2.0%) |

---
*Auto-generated. Paper account only.*