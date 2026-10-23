# OVERNIGHT RUN — STOPPED AT STAGE 1

**STATUS: PARTIAL — stopped at Stage 1 gate (FAILED). Stages 2–5 did NOT run.**

**Run date:** 2026-06-20 (overnight autonomous)  
**Confidence:** BROKEN for empirical overlay at -0.8%; CONFIRMED for gap-model math (cross-check passes)

---

## Headline (morning review order)

1. **Stage 1: FAILED** — do not trust any D3/D4/D5/D6/D7 numbers; they were not run.
2. **Methodology:** -0.8% threshold still produces **-21.9%** empirical on dual_window (gate failure). evening_only **-12.8%** is borderline but dual_window blocks the gate.
3. **D6 position concentration:** **NOT RUN** — blocked by Stage 1.
4. **Recommendation:** Likely need **gap ≈ empirical** (no overlay) for schedule-engine D3, pending user decision. Do not guess a third threshold unattended.

---

## Stage 1 gate evaluation

### PASS criteria (both modes)

Empirical meaningfully below gap but not wildly negative; tightening threshold from -1.2% should reduce penalty vs -40%/-20%, not reproduce large negative returns.

### FAIL criteria met

| Mode | Gap | Empirical (-0.8%) | Gate |
|------|-----|-------------------|------|
| **dual_window** | **+35.3%** | **-21.9%** | **FAIL** — 57pp erosion; below plausible floor (~-15%) |
| **evening_only** | **+23.4%** | **-12.8%** | **MARGINAL** — 36pp erosion; near floor but dual fails gate |

Cross-check: gap engine vs blind equity walk **matches exactly** for both modes (math sound; overlay methodology is the problem).

**Gate result: FAIL.** Sequence halted per overnight instructions.

---

## Stage 1 detailed results (-0.8% threshold, 3yr)

| Mode | Eligible (better than -0.8%) | Gap return | Empirical return | Overrides |
|------|------------------------------|------------|------------------|-----------|
| dual_window | 439/1603 (**27.4%**) | +35.3% | **-21.9%** | 438 (27.3%) |
| evening_only | 217/578 (**37.5%**) | +23.4% | **-12.8%** | 217 (37.5%) |

### Gap stop-fill distribution (% of all gap stops)

**dual_window** (mean **-1.71%**):

| Band | % |
|------|---|
| Better than -0.5% | 0.1% |
| -0.5% to -0.8% | **27.3%** ← only band overridden |
| -0.8% to -1.2% | 24.6% |
| -1.2% to -1.68% | 16.2% |
| Worse than -1.68% | 31.9% |

**evening_only** (mean **-1.59%**):

| Band | % |
|------|---|
| Better than -0.5% | 0.0% |
| -0.5% to -0.8% | **37.5%** ← only band overridden |
| -0.8% to -1.2% | 28.5% |
| -1.2% to -1.68% | 11.4% |
| Worse than -1.68% | 22.5% |

### Independent cross-check (Rule 2)

| Mode | Engine gap | Blind equity walk | Match |
|------|------------|-------------------|-------|
| dual_window | +35.32% | +35.32% | ✓ |
| evening_only | +23.39% | +23.39% | ✓ |

---

## Threshold comparison (full audit trail)

| Method / threshold | dual_window empirical | evening_only empirical | Eligible % (dual / evening) | Status |
|--------------------|----------------------|------------------------|----------------------------|--------|
| Post-hoc sum + worse-of | **-191.6%** | — | — | BROKEN (no compounding) |
| In-engine worse-of @ -1.2% | **-40.1%** | **-20.8%** | 52% / 65% | BROKEN |
| Option A conditional @ **-0.8%** | **-21.9%** | **-12.8%** | 27% / 38% | **BROKEN (gate)** |

Tightening -1.2% → -0.8% **did** reduce the penalty (dual -40% → -22%; evening -21% → -13%) but **not enough** to pass the gate. dual_window remains implausibly negative for a stop-capped strategy.

---

## Diagnosis

### What is NOT broken

- Gap-model simulation and compounding (cross-check confirms).
- Option A conditional logic implementation (only -0.5% to -0.8% band gets live sample replacement).

### What IS the issue

1. **Schedule-engine gap stops already match live reality.** Gap mean **-1.71%** vs live **-1.68%**. The gap model already embeds realistic OHLC stop fills; an overlay punishes the same trades again.

2. **Even a 27–38% override rate compounds through cash paths.** Replacing ~-0.65% fills with live samples (~-1.68% mean) on hundreds of trades, with path-dependent sizing, flips +35% strategies negative.

3. **Test 33 (+266% → +27%) is not a valid anchor for this harness.** That used idealized gap fills; schedule-engine gap is already conservative.

### Recommended next step (user decision required)

**Option A — gap ≈ empirical for D3:** Use gap model as both "gap" and "empirical" columns in schedule comparison (or note empirical = gap with rationale). Most defensible given stop-fill distribution.

**Option B — incremental overlay only:** Apply a fixed incremental penalty (e.g. -0.3pp) only on the -0.5% to -0.8% band instead of full live-sample replacement — requires explicit user approval; do not implement unattended.

**Do NOT:** Guess -0.6% or another threshold without user input.

---

## Stages NOT run

| Stage | Status |
|-------|--------|
| 2 — Full D3 matrix (20 runs) | **SKIPPED** (gate fail) |
| 3 — D2 validation_sim baseline | **SKIPPED** |
| 4 — D4/D5/D6/D7 | **SKIPPED** |
| 5 — phase3_sim_summary | **SKIPPED** |

`master_results_table.csv` was **not** updated with tonight's Stage 1 re-run numbers (per instructions: do not partially update with unvalidated results). Last rows remain from prior -0.8% attempt (2026-06-20).

---

## Files

- This report: `simulations/results/pdt_removal/OVERNIGHT_RUN_STOPPED_AT_STAGE_1.md`
- Stage 1 log: `simulations/results/pdt_removal/stage1_gate_run.log`
- Methodology history: `simulations/results/pdt_removal/empirical_methodology_note_2026-06-20.md`

---

## Live bot / holiday

Unchanged. Jun 19 2026 Juneteenth marked in `logs/analysis/paper_trading_validation.md`. Monitoring resumes Mon 2026-06-22.
