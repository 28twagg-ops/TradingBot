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

## paper_bot.py (out of scope per guide)

Contains separate `pdt.json` logic and `MAX_DAY_TRADES`. Not modified in Phase C; track for later parity.

## EVENING_ONLY_ENTRIES — Phase 3 gate

Per guide C3 Step 5: **do not remove** until D3 schedule mode sims complete.  
Rename to `PREFER_EVENING_ENTRIES` only after sim decision.

## Post-audit action plan

1. Checkpoint tag `checkpoint-audit-complete-2026-06-18`
2. Commit API documentation comments (no field changes needed)
3. Remove `STRICT_SAME_DAY_EXIT` + `_pdt_blocks_exit` (separate commit)
4. Remove `pdt.json` machinery; entry cap via transactions.csv + in-scan counter
5. Phase 3 sim suite before touching EVENING_ONLY or live stop threshold
6. Paper trading 10 days before live PDT removal deploy (Phase E)

## C4 verification (fill after Phase C)

- [ ] Bot imports / py_compile PASS
- [ ] No `STRICT_SAME_DAY_EXIT` in codebase
- [ ] No `pdt.json` read/write in rubber_band_bot.py
- [ ] No `_pdt_blocks_exit` calls
- [ ] `EVENING_ONLY_ENTRIES` still present (Phase 3 pending)
- [ ] Paper mode cycle (manual — requires keys + workflow)
