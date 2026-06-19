# Return Methodology Reconciliation

**Generated:** 2026-06-16  
**Question:** Why do documentation / `validation_sim.py` show returns like **+1129% OOS (7yr)** while the portfolio PDT sim showed **+135% (8yr)**?

---

## Short answer

They measure **different things**. The high numbers in docs are from the **validation simulator** counting **tens of thousands of fixed-stake trades** across **~900 stocks** with **aggregated trade P&L**. The lower number is a **cash-constrained portfolio** on **120 tickers** with **daily-bar approximation**. Both can be correct at the same time.

---

## Side-by-side

| Dimension | validation_sim (docs) | sim_pdt_schedule.py |
|-----------|----------------------|---------------------|
| Universe | S&P 500 + MidCap (~900) | 120 S&P sample |
| Trade generation | Pre-scan every signal on every stock | Portfolio loop, signals per day |
| OOS trade count (7yr) | ~83,000 | ~5,000–18,000 |
| Return metric | `(final_cash - 500) / 500` on **portfolio sim** of all scheduled trades | Same formula, fewer trades |
| Entry | Close on signal bar | Close (afternoon) / open (morning) |
| Stop model | Overnight gap + 2× stop slippage floor | Daily Low / open gap |
| Min trade size | **0.01** (aligned with live) after this plan | 0.01 |
| Compounding | Fixed stake off equity (signal scaling) | Equal-share cash split |
| Typical 7yr OOS | **+500% to +1129%** (stop -0.5%, hold 3d) | **+50% to +135%** (schedule-dependent) |

---

## Why validation_sim returns look huge

### 1. Massive trade throughput

Test 1 in `validation_sim_2026-05-29.txt` reports **124,630 IS trades** and **83,120 OOS trades** over 7 years on 900 stocks. Each trade uses ~$20–$100 from a $500 account when cash allows, but **many positions overlap** — the sim redeploys cash as positions exit.

Total **account** return is NOT the sum of trade percentages. Example from code comments: compounding mode can show **+93,000%** over 20yr — mathematically summing edges on overlapping capital.

### 2. Fixed-stake vs account growth

Default `simulate()` uses **fixed $100 stakes** on $500 (`compound=False`). Portfolio functions (`simulate_prioritized_gaps`) use **current equity** for sizing with signal scaling — profits increase deployable cash within the sim window.

### 3. "+121pp" in code comments

Comments like `20%/20% beats 20%/12% by +121pp` mean **percentage points difference** between two sim configs (e.g. 80% → 201% total return), not a 121% account return from $500.

### 4. Per-strategy standalone returns

Test 2 yearly tables show **each strategy alone** on all its signals across 900 stocks. A strategy with +300% standalone does not mean your live account earned +300% — you only hold scheduled subset.

---

## Why portfolio PDT sim looks smaller

1. **120 tickers** vs 900 — fewer signals per day  
2. **Daily bars** — misses intraday stop timing nuance  
3. **Cash binding** — can't take all 900 signals; real account ~$500  
4. **No overlapping parallel book** — simpler equity curve  

Overnight PDT on 120 tickers still beat intraday (+135% vs +77% over 8yr in our run) — direction is trustworthy; **magnitude** is conservative.

---

## Slippage impact (live logs)

From `live_slippage_profile_2026-06-16.json` (Jun 10–16, 2026):

- SELL slippage mean: **~-0.058%** per execution  
- Stop-loss overshoot vs -0.5%: material on deferred exits  

`validation_sim` Test 22 sweeps **0%–0.30%** round-trip spread; Test 33 replays empirical stop distribution from `transactions.csv`.

---

## What to trust for a $500 live account

| Use case | Best model |
|----------|------------|
| Strategy ranking / schedule choice | `validation_sim` OOS + walk-forward |
| PDT schedule (afternoon/morning) | `overnight_pdt_validation.py` with slippage overlay |
| Expected dollar growth on $500 | Portfolio sim with **900 stocks**, **MIN_TRADE_SIZE=0.01**, **empirical slippage** — expect **well below** +1129% but **above** naive 2-scan if overnight schedule wins |
| Whether to add a new strategy | `strategy_expansion_study.py` standalone OOS Sharpe |

---

## Reconciliation formula (approximate)

```
validation_sim_ret ≈ (avg_trade_edge × trades_taken × avg_stake) / 500
```

With ~83k OOS trades, even **0.1% avg edge** per trade on overlapping $50 stakes produces **hundreds of %** account return in sim — because the same $500 is **reused** hundreds of times per year.

Live account: **3 day trades/week PDT cap**, **fractional positions**, **slippage**, and **cannot scale to 900 parallel signals** → real growth tracks **portfolio sim** more than raw validation headline.

---

## Files

- Authoritative engine: `simulations/validation_sim.py`
- PDT schedule: `simulations/overnight_pdt_validation.py`
- Strategy sweep: `simulations/strategy_expansion_study.py`
- Slippage: `simulations/results/live_slippage_profile_2026-06-16.json`
