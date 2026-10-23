# Myers Stock Investor — Backtest Audit Report

**Date:** 2026-10-21  
**Model:** 1.1.0  
**Mode:** EXPLORATORY (not point-in-time validated)

## 1. Original reported results (v1.0.0, pre-audit)

| Metric | Strategy | SPY (reported) |
|---|---:|---:|
| Cumulative return | +18% | **+144%** |
| Max drawdown | -2.4% | -24.5% |
| Trades | 2 | — |
| Terminal | ~$118k | ~$195k |

Internal inconsistency in the original report: SPY terminal ~$194,585 on $100,000 start is **+94.6%**, not +144%. The +144% figure was a metric-window bug.

## 2. Root causes found

### A. SPY “+144%” inflation (CONFIRMED BUG — FIXED)

- Decisions began at the **first quarter-end** (2020-03-31), after the COVID crash.
- Benchmark metrics were computed on the equity series **aligned to that later start**, so SPY was measured from the trough (~Mar 2020) to Dec 2024 ≈ **+144%**.
- True buy-and-hold from **2020-01-02 → 2024-12-31** on yfinance auto-adjusted SPY closes:

| Field | Value |
|---|---|
| First / last | 2020-01-02 / 2024-12-31 |
| Adj close | 295.39 → 574.79 |
| Cumulative | **+94.6%** |
| CAGR | **14.3%** |
| Max DD (daily) | **-33.7%** |

This is consistent with ~high-90% S&P total-return ballpark for 2020–2024 (exact index vs SPY and dividend handling differ slightly).

### B. Strategy / SPY drawdown understated (CONFIRMED BUG — FIXED)

- Old engine recorded equity only on quarter-ends, then **forward-filled** to daily dates.
- Holdings were **not marked to market** between rebalances → strategy DD looked like **-2.4%**.
- New engine: **quarterly decisions, daily MTM**.
- Corrected SPY DD **-33.7%** (includes Feb–Mar 2020).
- Corrected strategy DD **-3.3%** (still small because ~83% cash).

### C. Cash / trade accounting

- Position sizing ~5% of equity per buy; costs = commission+slippage bps.
- Trades (sim): **2020-03-31 BUY MRK** (~$5,005), **BUY AAPL** (~$5,005).
- No sells — both held through end.
- Cash default earns **0%** (`cash_annual_rate` configurable).
- Avg cash **83.1%**, avg invested **16.9%** → most “performance” is cash drag + small equity sleeve.

### D. Why only two trades (NOT a sizing bug)

Across 200 decision rows (10 names × 20 quarter-ends):

| Filter | Count |
|---|---:|
| WATCH | 190 |
| BUY_CANDIDATE | **10** |
| score≥70 & MOS≥25% | 10 |
| score≥70 & MOS≥15% | 11 |

Dominant rejection categories:

1. **insufficient_margin_of_safety** (most common)
2. **excessive_valuation** (negative MOS)
3. **low_business_quality_or_score** (score &lt; 70)

Closest near-miss: **MRK 2022-03-31** score 75, MOS ~20% (fails 25% gate).

The two executed buys are AAPL+MRK on the COVID quarter-end when DCF MOS cleared 25%. Later BUY_CANDIDATE rows for the same names were skipped (`already_held`). No other name cleared conservative gates often enough to add a third name under 5% caps.

**Conclusion:** Infrequent trading is primarily **strict MOS + expensive mega-cap universe + look-ahead-ish DCF levels**, not a broken order ticket.

## 3. Corrected results (v1.1.0, daily MTM, same 10-name universe)

| Metric | Conservative Acquirer | SPY (same calendar) |
|---|---:|---:|
| Start / end | $100,000 → $118,088 | $100,000 → $194,585 |
| Cumulative | **+18.1%** | **+94.6%** |
| CAGR | 3.4% | 14.3% |
| Max DD | -3.3% | -33.7% |
| Sharpe | 0.97 | 0.74 |
| Trades | 2 | — |
| Avg cash | 83.1% | 0% |

Strategy cumulative was roughly right; **benchmark and drawdowns were wrong**.

## 4. Strategy comparison (exploratory, identical window/universe)

| Profile | Cum | MaxDD | Trades | Avg Cash |
|---|---:|---:|---:|---:|
| conservative_acquirer (A) | 18.1% | -3.3% | 2 | 83% |
| balanced_value (B, MOS≥15%) | 18.1% | -3.3% | 2 | 83% |
| quality_fair_value (C) | 0.0% | 0.0% | 0 | 100% |
| simple_reference (F) | **83.1%** | -10.0% | 10 | 39% |
| SPY | **94.6%** | -33.7% | — | — |

On this survivor mega-cap list, easing MOS from 25%→15% barely changes outcomes. Equal-weight reference deploys more capital and approaches SPY but still trails. **All exploratory — not validated PIT performance.**

## 5. Fixes shipped

- Daily mark-to-market equity + cash/invested curves
- Benchmark aligned to full `[start, end]` trading calendar
- Independent `spy_total_return_audit()`
- Rejection diagnostics CSV + category tallies
- Strategy profiles A–F + `myers compare`
- Reverse DCF fields on valuation
- `research_mode: exploratory|validated` (validated refuses without PIT provider)
- Regression tests for SPY window bug, daily DD, cash buys, reverse DCF

## 6. Remaining limitations

- yfinance fundamentals are **not** filing-date point-in-time
- Universe is a **modern survivor** list (bias)
- DCF is simplified FCFF; mega-caps often show negative MOS vs market
- Customer concentration / key-person still UNKNOWN without 10-K NLP
- No ZIP artifact claimed in this environment unless generated separately

## 7. Recommended next work

1. Expand universe beyond mega-caps (mid-cap cash compounders)
2. Wire PIT fundamentals provider → enable `validated` mode
3. Run deep_value + ranking profiles on broader set
4. Normalize cyclical earnings; peer EV/EBITDA bands
5. Optional SEC major-customer extraction
