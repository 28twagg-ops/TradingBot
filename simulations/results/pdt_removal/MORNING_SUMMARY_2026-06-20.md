# Morning summary — overnight autonomous run (2026-06-20)

**STATUS: PARTIAL — stopped at Stage 1. Stages 2–5 did NOT run.**

## Read first

| # | Question | Answer |
|---|----------|--------|
| 1 | Did Stage 1 pass? | **NO — FAILED** |
| 2 | Why did -0.8% fail when -1.2% failed? | Tightening helped (dual -40%→-22%) but **dual_window still -21.9%** — overlay still punishes ~27% of stops; gap stops already avg **-1.71% ≈ live -1.68%** |
| 3 | D6 unlimited vs capped? | **NOT TESTED** — blocked |
| 4 | What ran? | Stage 1 sanity check only. Full report: `simulations/results/pdt_removal/OVERNIGHT_RUN_STOPPED_AT_STAGE_1.md` |

## Stage 1 numbers (-0.8% threshold, 3yr)

| Mode | Gap | Empirical | Overrides |
|------|-----|-----------|-----------|
| dual_window | +35.3% | **-21.9%** | 438/1603 (27%) |
| evening_only | +23.4% | **-12.8%** | 217/578 (38%) |

Cross-check: gap engine = blind equity walk ✓ (math OK; methodology not OK).

## Awaiting your decision

Proceed with **gap ≈ empirical** for D3 schedule comparison, or specify a different overlay rule. **No third threshold guess without approval.**
