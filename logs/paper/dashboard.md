# 📊 Paper Bot — Performance Dashboard (PAPER TRADING)
*Updated: 2026-05-10 09:43 UTC*

> ⚠️ **Paper trading only — no real money involved.**

## Account Snapshot
| | |
|---|---|
| **Current Equity** | $99874.40 |
| **Starting Equity** | $100000.00 |
| **Total Return** | -0.13% ($-125.60) |
| **Max Drawdown** | -99.48% |
| **Current Cash** | $96878.17 |
| **Open Positions** | 0 () |
| **Last Run** | 2026-05-10 09:43:11 |

## Trade Performance
| Metric | Value |
|---|---|
| **Total Closed Trades** | 4 |
| **Win Rate** | 50.0% |
| **Avg Win** | +0.41% |
| **Avg Loss** | -1.09% |
| **Profit Factor** | 4.54x |
| **Avg Hold Days** | 0.0d |
| **Total Realised P&L** | $+18.72 |

## Tranche Feature  (new in paper bot)
| Parameter | Value |
|---|---|
| Tranche 1 (entry day) | 50% of target size |
| Tranche 2 (next day) | 50% — only if price ≤ entry×1.005 |
| Partial exit | Sell 50% at midline, ride rest to time/stop |

## Exit Reasons
| Exit | Trades | WR | Avg P&L% |
|---|---|---|---|
| `rsi_exit` | 3 | 67% | +0.22% |
| `stop_loss` | 1 | 0% | -2.04% |

## Recent Closed Trades
| Date | Ticker | Strategy | P&L% | P&L$ | Hold | Exit |
|---|---|---|---|---|---|---|
| 2026-05-10 | **SOLUSD** | `CryptoRSI` | +0.47% | $+13.63 | 0d | rsi_exit (RSI=63) |
| 2026-05-10 | **LINKUSD** | `CryptoRSI` | -0.15% | $-4.35 | 0d | rsi_exit (RSI=58) |
| 2026-05-10 | **AVAXUSD** | `CryptoRSI` | +0.35% | $+10.38 | 0d | rsi_exit (RSI=64) |
| 2026-05-06 | **ACGL** | `Pullback50` | -2.04% | $-0.94 | 0d | stop_loss (-2.0%) |

---
*Auto-generated. Paper account only.*