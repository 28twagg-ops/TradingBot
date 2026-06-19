# Empirical Slippage Methodology — Schedule Engine D3 Sims

Updated: 2026-06-20

## History

### Method 1 — Post-hoc worse-of sum (2026-06-18, **buggy**)

After gap-model `run_simulation()`, adjusted each stop trade's `pnl_dollar` by adding
`-1.18pp` overshoot, then **summed** all `pnl_dollar` values for total return.

**Bug:** Overlapping positions made linear sum non-compounding. dual_window 3yr empirical
reported **-191.6%** (impossible for stop-capped strategies).

### Method 2 — Equity walk + unconditional worse-of (2026-06-19, **fixed compounding, wrong overlay**)

Replaced sum with chronological equity walk (exits → entries, sim-derived notionals).
Applied `min(gap_fill, empirical_sample)` on **every** stop.

**Problem:** Schedule-engine gap stops already average **-1.71%** vs live **-1.68%**.
Unconditional worse-of double-counted slippage the gap model already priced in.
dual_window 3yr empirical: **-107.5%**; evening_only: **-34.3%**.

Test 33's worse-of logic (+266% gap → +27% empirical) used an **idealized** gap baseline
that did not include realistic OHLC stop fills — that logic does not transfer here.

### Method 3 — Option A conditional overlay (**current**, 2026-06-20)

Treat schedule-engine gap as the realistic stop baseline. Only apply empirical when the
gap fill is **more optimistic than live reality**:

- Threshold: gap stop fill **better than -1.2%** (less negative)
- Action: replace with one draw from live stop distribution (249 samples, mean -1.68%)
- Otherwise: leave gap fill unchanged

Compounding via the same equity walk as Method 2.

## Rationale

| Model | Gap stop mean | Empirical mean (live) |
|-------|---------------|------------------------|
| validation_sim Test 33 | Idealized ~-0.5% at trigger | -1.68% |
| pdt_schedule_engine | **-1.71%** (OHLC fills) | -1.68% |

When gap ≈ live, empirical overlay should only correct the **optimistic tail** of stop
fills (those better than -1.2%), not re-penalize trades already filled at realistic levels.

## References

- User decision: LIVE-ONLY PATH response 2026-06-20
- `simulations/pdt_removal_suite.py` — `EMPIRICAL_OVERRIDE_THRESHOLD_PCT`, `_adjusted_stop_pnl_pct()`
- `logs/analysis/pdt_removal_audit.md` — PDT removal context
