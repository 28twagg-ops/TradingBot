# PDT Removal Audit — Phase B1
Generated: 2026-06-18  
Repo: `TradingBot-git/rubber_band_bot.py` @ pre-removal checkpoint

## Executive summary

- **Alpaca deprecated API fields:** NOT used in live bot. `get_account()` only reads `.equity` and `.cash`. No July 6 crash risk from field reads.
- **PDT workarounds present:** `STRICT_SAME_DAY_EXIT`, `_pdt_blocks_exit()`, `pdt.json` / `pdt_n()` / `pdt_ok()`, `EVENING_ONLY_ENTRIES`.
- **Already deployed (note):** `MAX_OPEN_POSITIONS=5`, dashboard CI refresh, `morning_prep` disabled — predates this guide; F2 says cap needs separate user approval for live (already live).
- **`pdt_ok()` misnomer:** Compares today's buy count (from `pdt.json`) to `max_trades` (cash cap) — not Alpaca day-trade API.

## B3 — get_account() field audit

| Line | Fields read | Deprecated? |
|------|-------------|-------------|
| 968, 2526, 2589, 2660, 2907, 2970, 3018, 3192 | `.equity` | No |
| 3146 | `.cash` | No |
| 2751, 3243, 3283 | `.equity`, `.cash` | No |

**Result:** No `pattern_day_trader`, `daytrade_count`, `daytrading_buying_power`, etc. Action: add documentation comments only.

## Search term classification — rubber_band_bot.py

| Location | Term | Class | Action |
|----------|------|-------|--------|
| 49 | PDT-safe (docstring) | REVIEW | Update after removal |
| 178 | `PDT_FILE` / pdt.json | REMOVE | Delete file + refs |
| 185-188 | `EVENING_ONLY_ENTRIES`, `STRICT_SAME_DAY_EXIT` | REVIEW | Keep EVENING until Phase 3 sim; remove STRICT |
| 191-193 | `_pdt_blocks_exit()` | REMOVE | Delete; allow same-day midline/max-hold |
| 809-825 | `load_pdt`, `save_pdt`, `pdt_n`, `pdt_ok` | REMOVE | Replace with tx-based entry count |
| 1899, 1915 | weekly `pdt_n` display | REMOVE | Use tx buy count |
| 2175-2176 | build_plan `_pdt_blocks_exit` | REMOVE | Include same-day exits in plan |
| 2475, 2503-2508, 2728 | run_exits defer + stats | REMOVE | Delete defer branch |
| 2786, 2824, 3242 | run_scan pdt load/save/display | REMOVE | Use entry counter |
| 2841, 2885-2889, 3050 | scan exit defer + stats | REMOVE | Delete defer branch |
| 3111-3118 | `EVENING_ONLY_ENTRIES` | REVIEW | TODO Phase 3 — keep for now |
| 3158, 3188, 3218 | `pdt_ok`, `pdt.append` | REMOVE | Replace entry slot check |

## run_bot.yml

No PDT-specific references. No changes required for PDT removal.

## paper_bot.py — removed 2026-06-20

Deleted per user decision (live-only validation; paper trading skipped). Rebuild from
`rubber_band_bot.py` if needed later.

## Empirical slippage methodology (D3 sims — 2026-06-20)

Schedule-engine gap stops already average ~-1.71% vs live -1.68%. Unconditional worse-of
(Test 33 style) double-counts slippage on this baseline.

**Current method (Option A):** In `simulations/pdt_schedule_engine.py`, replace gap stop
fill with a live sample **only** when gap fill is better (less negative) than -1.2%.
See `simulations/results/pdt_removal/empirical_methodology_note_2026-06-20.md`.

Prior methods (post-hoc sum → equity-walk worse-of) documented in that file. Sanity check
2026-06-20: Option A still yields negative empirical returns for 3yr evening_only and
dual_window — full D3 matrix blocked pending user review.

## EVENING_ONLY_ENTRIES — Phase 3 gate

Per guide C3 Step 5: **do not remove** until D3 schedule mode sims complete.  
Rename to `PREFER_EVENING_ENTRIES` only after sim decision.

## Post-audit action plan

1. Checkpoint tag `checkpoint-audit-complete-2026-06-18`
2. Commit API documentation comments (no field changes needed)
3. Remove `STRICT_SAME_DAY_EXIT` + `_pdt_blocks_exit` (separate commit)
4. Remove `pdt.json` machinery; entry cap via transactions.csv + in-scan counter
5. Phase 3 sim suite before touching EVENING_ONLY or live stop threshold
6. ~~Paper trading 10 days before live PDT removal deploy (Phase E)~~ — skipped; live validation log instead (2026-06-19)

## C4 verification (Phase C — 2026-06-18)

- [x] py_compile PASS
- [x] `STRICT_SAME_DAY_EXIT` removed
- [x] `_pdt_blocks_exit` removed
- [x] `pdt.json` load/save/`pdt_ok` removed — replaced with `_count_buys_today()` / `entry_slot_ok()`
- [x] No deprecated Alpaca field reads (`.daytrade_count`, etc.)
- [x] `EVENING_ONLY_ENTRIES` kept pending Phase 3 D3 sim decision
- [ ] Paper mode full cycle (manual — requires workflow run)
