# Strategy Research — 2026-10-23

**Base commit (branch start):** `6c5cbac322` (`origin/main` tip at branch creation)  
**Primary evidence:** `logs/options_trial/reports/2026-10-23_strategy_selection.*`, `2026-10-23_data_quality.*`, `2026-10-23_buckets.*`  
**Live gate (unchanged):** `LIVE_OPTIONS_ENTRIES=0`, `LIVE_OPTIONS_MAX_CAP=250` in `.github/workflows/run_bot.yml`

This report ranks **paper** arms for deeper experimentation only. It does **not** recommend enabling live entries.

---

## 1. Book health (ALL exits)

| Metric | Value | Note |
|---|---:|---|
| Total exits | 3774 | Full ledger |
| Orphan exits | 422 (11.2%) | **ALERT** (>10%) — attribution debt |
| ALL win% / med% / $ | 39.3% / −40.0% / +$6,692 | Contaminated by TAINTED days |
| CLEAN n / win% / med% / $ | 1738 / 48.1% / −29.3% / +$18,405 | Prefer for promotion |
| TAINTED n / win% / med% / $ | 2036 / 31.8% / −41.2% / −$11,713 | Outages / reconcile_fill |
| KEEP-only CLEAN | 833 / 60.3% / +50.0% / +$12,087 | Optimistic cohort lens |

Recent daily exit health (2026-10-02 → 2026-10-23) is mostly **OK** (0 reconcile-ish), which is a meaningful infrastructure improvement vs August–September BUGGY stretch.

---

## 2. Deep dive — priority names

### S406 RubberBand_ITM3 — CONTINUE BASELINE + left-tail diagnostic

| Lens | n | WR | Med% | Avg% | p10% (ALL) | $ |
|---|---:|---:|---:|---:|---:|---:|
| CLEAN | 75 | 58.7 | +53.3 | +78.5 | — | +930 |
| ALL | 143 | 55.9 | +50.0 | +107.9 | −61.0 | +3,191 |

- Largest CLEAN KEEP rubber-band arm; still active (15 entries / 14 exits last 5d on ALL).
- Fat left tail on ALL (p10 < −45%) blocks any live escalation discussion.
- **Hypothesis for paper twin (new ID if changing mechanics):** tighter max premium or earlier EOD on high-IV names reduces p10 damage without killing median.

### S404 GapDown_OTM2 — CONTINUE BASELINE + left-tail diagnostic

| Lens | n | WR | Med% | Avg% | p10% (ALL) | $ |
|---|---:|---:|---:|---:|---:|---:|
| CLEAN | 53 | 64.2 | +53.2 | +32.8 | — | +1,161 |
| ALL | 93 | 51.6 | +26.7 | +12.7 | −66.3 | +909 |

- Best CLEAN $ among live-allow peers; WR strong on CLEAN.
- ALL median collapses vs CLEAN → TAINTED / attribution sensitivity.
- Live allow-list member historically; **entries must stay OFF** until p10 protocol clears.

### S430 DayTrader_ORB (opening-drive **proxy**) — DIAGNOSTIC / gather n

| Lens | n | WR | Med% | p10% | $ | Days |
|---|---:|---:|---:|---:|---:|---:|
| CLEAN / ALL | 4 | 50 | +5.4 | −44.3 | +14 | 7 |

- **Documented as opening-drive proxy**, not classical ORB. A true ORB arm needs a **new strategy ID** + separate history.
- Data-validity fix (this branch): stale yesterday→today fallback removed; no signals without same-session bar.
- Do not KEEP/KILL until n≥15–30.

### S431 DayTrader_RS — DIAGNOSTIC (silent)

- n=0 exits. Needs fresh SPY context + same-session stock bar (both now fail-closed on stale data).
- Likely under-firing if SPY snapshot/bar lag; watch post-fix runs before declaring broken.

### S432 DayTrader_ORB_RS — DIAGNOSTIC / gather n

| n | WR | Med% | p10% | $ |
|---:|---:|---:|---:|---:|
| 4 | 50 | +17.1 | −38.9 | +21 |

- Slightly better median than S430 at same tiny n; treat as joint DayTrader family until n grows.

---

## 3. Research priority labels (active / interesting)

| Label | Strategies | Rationale |
|---|---|---|
| **DEEPER EXPERIMENTATION** | S406, S404, S362, S397, S167, S166, S410, S430→new-ORB | Strong CLEAN or interesting microstructure; paper-only arms / twins |
| **CONTINUE BASELINE** | S406, S404 (as currently coded), promising-cohort KEEP set | Keep collecting under existing IDs |
| **DIAGNOSTIC** | S430, S431, S432, silent S169–S175 / S200+ zeros | Validity, sample, or scanner health |
| **REDUCE** | Fat-left ALL watches with weak CLEAN, high top-symbol share | Cap bucket share; do not expand |
| **EXCLUDED** | CLEAN KILL list (S212, S202, S360, S218, …), DROPPED S173/S174 new entries | Already paused / kill-tagged |

---

## 4. Top deeper-experimentation candidates (paper only)

New mechanical arms → **new IDs**. Do not rewrite S430 meaning.

| # | Candidate | Hypothesis | Design notes |
|---:|---|---|---|
| 1 | **S406 left-tail twin** (new ID, e.g. S440) | Cap premium ≤$40 and/or force EOD sweep earlier on VZ>2 cuts p10 while preserving med | Mirror S406 scanner; separate bucket history |
| 2 | **S404 gap-quality twin** (new ID) | Require gap≤−3% (S166-like) on OTM2 structure improves WR stability | Combine S404 strike logic + S166 gap threshold |
| 3 | **S362 RubberBand_3DTE** | CLEAN KEEP peer (n=33, med +57.1%); test as S406 DTE neighbor | Already live in paper; deepen via regime slice |
| 4 | **S397 GapDown_ITM1** | CLEAN n=35, WR 68.6%, med +56.1% — ITM1 vs S404 OTM2 contrast | Paper compare group only |
| 5 | **S167 1-OTM GapDown** | CLEAN med +106% (n=19) but ALL p10 −72% — high ceiling / high risk | Size-cap experiment, not promotion |
| 6 | **S166 strong gap** | CLEAN n=12, WR 66.7%, med +60.8%; building sample | Continue until n≥30 |
| 7 | **S410 RubberBand_OTM1** | CLEAN n=10, med +58.3%; small but clean | Watch concentration (top share 72.7% ALL) |
| 8 | **True ORB arm (new ID, e.g. S433)** | 15-min opening range breakout ≠ S430 drive proxy | Intraday bars required; never alias as S430 |
| 9 | **S430 post-validity rebaseline** | After stale-bar fix, remeasure hit rate / WR for 10 sessions | Same ID OK (definition unchanged; data gate tightened) |
| 10 | **Orphan-rate reduction (infra)** | Tagging / idempotent adopt lowers 11.2% orphan exits | Not alpha — prerequisite for trusting $ ranks |

Stop at ≤10. Prefer #1–#4 + #8–#10 over expanding the silent zero-exit grid.

---

## 5. Regime / multiple-testing caveats

- **Multiple testing:** 100+ scanners / DTE×strike grid → expect lucky CLEAN KEEP tails. Prefer pre-registered twins with new IDs over reinterpreting old ones.
- **Regime:** Post-2026-10-02 OK days are a short clean window; do not overweight 1–2 weeks vs full CLEAN since 2026-08-03 (med −40.5% — still harsh).
- **KEEP-only optimism:** +$12k / 60% WR is conditional on past keepers; full CLEAN book med is still negative.
- **Concentration:** Several watches show top-symbol share >25% (S410 73%, S396 75%) — symbol luck risk.

---

## 6. Paper execution realism

- Fills: limit ask−0.01, OI≥100, spread≤25%, min cost $20 (mirror live filter when enabled).
- Virtual $500 buckets ≠ live $250 sleeve; paper capacity overstates concurrency.
- EOD / protective stops differ under GHA latency; TAINTED mass in Aug–Sep proves ops risk dominates some “alpha.”
- DayTrader arms use developing daily bar (and snapshots) — partial-session bias remains even after freshness fixes.

---

## 7. Live safety confirmation

| Control | Status |
|---|---|
| `LIVE_OPTIONS_ENTRIES` | **0** (workflow) + fail-closed parser (missing/invalid → OFF) |
| `LIVE_OPTIONS_MAX_CAP` | **250** (missing/invalid/≤0 → 250) |
| `LIVE_STOCK_CASH_RESERVE` | **250** |
| Myers ↔ options execution | **Not merged** |

---

## 8. Suggested next measurements (paper)

1. After deploy: confirm S430/S431/S432 no longer fire on weekend/stale bars (log reject reasons if wired).  
2. Track orphan rate weekly; target <10%.  
3. Hold S404/S406 live discussion until CLEAN p10 protocol + twin confirmation.  
4. Only then consider paper twins in the table above (new IDs).
