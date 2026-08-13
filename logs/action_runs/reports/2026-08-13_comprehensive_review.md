# Daily Comprehensive Action Review — 2026-08-13

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260813T130054Z

- UTC timestamp: `20260813T130054Z`
- GitHub run: [#6951](https://github.com/28twagg-ops/TradingBot/actions/runs/31702731008)
- Run id: `31702731008`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`12s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 782 | 42.2 | -47.1 | +12.1 | $+8,202 |
| TAINTED | 1701 | 33.1 | -39.0 | +10.2 | $-8,382 |
| KEEP-only | 275 | 64.7 | +37.7 | +42.1 | $+5,447 |
| KEEP-only recent | 88 | 61.4 | +51.2 | +54.0 | $+1,398 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S403, S404, S406
- KILL strategies (15): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-13T09:00:59.124269-04:00","date":"2026-08-13","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.71},"signals":0,"placed":0,"equity":131219.66,"open_positions":26,"pending_orders":0,"open_lots":24,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"6951","github_run_id":"31702731008","status":"ok","data_quality":{"clean":{"n":782,"win":42.2,"med":-47.14,"avg":12.07,"pnl":8202.42},"tainted":{"n":1701,"win":33.1,"med":-39.02,"avg":10.24,"pnl":-8382.34},"keep_only":{"n":275,"win":64.73,"med":37.69,"avg":42.15,"pnl":5447.45},"keep_only_recent":{"n":88,"win":61.36,"med":51.22,"avg":53.96,"pnl":1398.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S405","S407","S408"]}}
```

### Live bot full output

```text
13:00:55  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $465.51|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $465.51|
|  Cash                                                           $209.49|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $256.02|
|  Open P&L                                                        $-0.07|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $68.96     $97.48   $97.50   +0.0%   $+0.01  |
|  AES      Pullback50      $93.74     $14.72   $14.67   -0.4%   $-0.35  |
|  AFL      Pullback50      $93.31     $120.39  $120.73  +0.3%   $+0.26  |
|                                                                        |
|  Total invested                                                 $256.02|
|  Total open P&L                                                  $-0.07|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-08-12  SELL  ALGN  Pullback50  $93.06  P&L $-0.12                |
|  2026-08-12  SELL  AKAM  Pullback50  $93.09  P&L $-0.17                |
|  2026-08-12  SELL  AXP  Pullback50  $94.12  P&L $+0.93                 |
|  2026-08-12  SELL  ADM  Pullback50  $12.64  P&L $-0.12                 |
|  2026-08-12  SELL  EXR  Pullback50  $68.70  P&L $-0.36                 |
|  2026-08-11  SELL  DHI  Pullback50  $93.11  P&L $-0.11                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=28 paper_keys=yes dry_run=False
  alpaca positions=28
  FLAG b0|ORPHAN|3136bb09 missing from Alpaca
  FLAG b0|ORPHAN|8c94dd36 missing from Alpaca
  FLAG b0|ORPHAN|e480c540 missing from Alpaca
  FLAG b0|ORPHAN|2f2b17aa missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-13T09:00:59.124269-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $131219.66, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (after_hours) --                                      |
|Equity       : $131,219.66                                              |
|Open Risk    : 24 lots (26 broker pos)                                  |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 24 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=782   win= 42.2%  med= -47.1%  $+8,202           |
|  TAINTED            n=1701  win= 33.1%  med= -39.0%  $-8,382           |
|  KEEP-only          n=275   win= 64.7%  med= +37.7%  $+5,447           |
|  KEEP recent        n=88    win= 61.4%  med= +51.2%  $+1,398           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S403...                  |
|  KILL(15): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  79%  +107.1%    14                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.9%    14                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[PENDING EXITS (6)]                                                     |
+========================================================================+
|  b863 S408 AAPL260814C00317500 x1 stop_loss (-90.2%)                   |
|  b0   ORPHAN UBER260814C00081000 x1 stop_loss (-96.7%)                 |
|  b316 S355 AAPL260817C00320000 x1 stop_loss (-85.6%)                   |
|  b0   ORPHAN CVNA260814C00076000 x2 stop_loss (-63.0%)                 |
|  b98  S211 CVNA260814C00074000 x1 take_profit (+61.8%)                 |
|  ... 1 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (26)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  AAPL260814C00317500          17    -90.2%   $   -937.22               |
|  PATH260821C00015500           7    -27.3%   $    -84.00               |
|  CVNA260814C00076000           2    -63.0%   $    -58.00               |
|  AAPL260817C00320000           1    -85.6%   $    -53.69               |
|  SNOW260814C00360000           1   -100.0%   $    -45.00               |
|  PATH260814C00016000          12    -38.8%   $    -38.00               |
|  PATH260814C00015000           4    -22.5%   $    -36.00               |
|  C260814C00139000              2    -23.4%   $    -30.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-13.log
elapsed=1.4s reconcile=0.71s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.4s. run=#6951 https://github.com/28twagg-ops/TradingBot/actions/runs/31702731008
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 12.2% (303/2483) ALERT
# Options signal frequency

_Generated 2026-08-13T09:01:06.517968_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-13
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |    24 | WARN | <<<
| Total open lots             |    24 | INFO |
| Total closed lots           |  1713 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=782 med=-47.1% | TAINTED n=1701 med=-39.0% | KEEP-only n=275 med=+37.7% | KILL=15 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=465.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260813T130553Z

- UTC timestamp: `20260813T130553Z`
- GitHub run: [#6952](https://github.com/28twagg-ops/TradingBot/actions/runs/31703148740)
- Run id: `31703148740`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`10s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 782 | 42.2 | -47.1 | +12.1 | $+8,202 |
| TAINTED | 1701 | 33.1 | -39.0 | +10.2 | $-8,382 |
| KEEP-only | 275 | 64.7 | +37.7 | +42.1 | $+5,447 |
| KEEP-only recent | 88 | 61.4 | +51.2 | +54.0 | $+1,398 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S403, S404, S406
- KILL strategies (15): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-13T09:05:59.260250-04:00","date":"2026-08-13","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":131463.66,"open_positions":26,"pending_orders":0,"open_lots":24,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"6952","github_run_id":"31703148740","status":"ok","data_quality":{"clean":{"n":782,"win":42.2,"med":-47.14,"avg":12.07,"pnl":8202.42},"tainted":{"n":1701,"win":33.1,"med":-39.02,"avg":10.24,"pnl":-8382.34},"keep_only":{"n":275,"win":64.73,"med":37.69,"avg":42.15,"pnl":5447.45},"keep_only_recent":{"n":88,"win":61.36,"med":51.22,"avg":53.96,"pnl":1398.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S405","S407","S408"]}}
```

### Live bot full output

```text
13:05:54  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $465.51|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $465.51|
|  Cash                                                           $209.49|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $256.02|
|  Open P&L                                                        $-0.07|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $68.96     $97.48   $97.50   +0.0%   $+0.01  |
|  AES      Pullback50      $93.74     $14.72   $14.67   -0.4%   $-0.35  |
|  AFL      Pullback50      $93.31     $120.39  $120.73  +0.3%   $+0.26  |
|                                                                        |
|  Total invested                                                 $256.02|
|  Total open P&L                                                  $-0.07|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-08-12  SELL  ALGN  Pullback50  $93.06  P&L $-0.12                |
|  2026-08-12  SELL  AKAM  Pullback50  $93.09  P&L $-0.17                |
|  2026-08-12  SELL  AXP  Pullback50  $94.12  P&L $+0.93                 |
|  2026-08-12  SELL  ADM  Pullback50  $12.64  P&L $-0.12                 |
|  2026-08-12  SELL  EXR  Pullback50  $68.70  P&L $-0.36                 |
|  2026-08-11  SELL  DHI  Pullback50  $93.11  P&L $-0.11                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=24 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-13T09:05:59.260250-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $131463.66, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (after_hours) --                                      |
|Equity       : $131,463.66                                              |
|Open Risk    : 24 lots (26 broker pos)                                  |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 24 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=782   win= 42.2%  med= -47.1%  $+8,202           |
|  TAINTED            n=1701  win= 33.1%  med= -39.0%  $-8,382           |
|  KEEP-only          n=275   win= 64.7%  med= +37.7%  $+5,447           |
|  KEEP recent        n=88    win= 61.4%  med= +51.2%  $+1,398           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S403...                  |
|  KILL(15): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  79%  +107.1%    14                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.9%    14                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[PENDING EXITS (6)]                                                     |
+========================================================================+
|  b863 S408 AAPL260814C00317500 x1 stop_loss (-90.2%)                   |
|  b0   ORPHAN UBER260814C00081000 x1 stop_loss (-96.7%)                 |
|  b316 S355 AAPL260817C00320000 x1 stop_loss (-85.6%)                   |
|  b0   ORPHAN CVNA260814C00076000 x2 stop_loss (-63.0%)                 |
|  b98  S211 CVNA260814C00074000 x1 take_profit (+61.8%)                 |
|  ... 1 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (26)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  AAPL260814C00317500          17    -90.2%   $   -937.22               |
|  PATH260821C00015500           7    -27.3%   $    -84.00               |
|  CVNA260814C00076000           2    -63.0%   $    -58.00               |
|  AAPL260817C00320000           1    -85.6%   $    -53.69               |
|  SNOW260814C00360000           1   -100.0%   $    -45.00               |
|  PATH260814C00016000          12    -38.8%   $    -38.00               |
|  PATH260814C00015000           4    -22.5%   $    -36.00               |
|  C260814C00139000              2    -23.4%   $    -30.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-13.log
elapsed=0.7s reconcile=0.13s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.7s. run=#6952 https://github.com/28twagg-ops/TradingBot/actions/runs/31703148740
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 12.2% (303/2483) ALERT
# Options signal frequency

_Generated 2026-08-13T09:06:05.758535_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-13
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |    24 | WARN | <<<
| Total open lots             |    24 | INFO |
| Total closed lots           |  1713 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=782 med=-47.1% | TAINTED n=1701 med=-39.0% | KEEP-only n=275 med=+37.7% | KILL=15 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=465.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260813T131047Z

- UTC timestamp: `20260813T131047Z`
- GitHub run: [#6953](https://github.com/28twagg-ops/TradingBot/actions/runs/31703561516)
- Run id: `31703561516`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 782 | 42.2 | -47.1 | +12.1 | $+8,202 |
| TAINTED | 1701 | 33.1 | -39.0 | +10.2 | $-8,382 |
| KEEP-only | 275 | 64.7 | +37.7 | +42.1 | $+5,447 |
| KEEP-only recent | 88 | 61.4 | +51.2 | +54.0 | $+1,398 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S403, S404, S406
- KILL strategies (15): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-13T09:10:51.019794-04:00","date":"2026-08-13","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":131411.66,"open_positions":26,"pending_orders":0,"open_lots":24,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"6953","github_run_id":"31703561516","status":"ok","data_quality":{"clean":{"n":782,"win":42.2,"med":-47.14,"avg":12.07,"pnl":8202.42},"tainted":{"n":1701,"win":33.1,"med":-39.02,"avg":10.24,"pnl":-8382.34},"keep_only":{"n":275,"win":64.73,"med":37.69,"avg":42.15,"pnl":5447.45},"keep_only_recent":{"n":88,"win":61.36,"med":51.22,"avg":53.96,"pnl":1398.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S405","S407","S408"]}}
```

### Live bot full output

```text
13:10:48  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $465.51|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $465.51|
|  Cash                                                           $209.49|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $256.02|
|  Open P&L                                                        $-0.07|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $68.96     $97.48   $97.50   +0.0%   $+0.01  |
|  AES      Pullback50      $93.74     $14.72   $14.67   -0.4%   $-0.35  |
|  AFL      Pullback50      $93.31     $120.39  $120.73  +0.3%   $+0.26  |
|                                                                        |
|  Total invested                                                 $256.02|
|  Total open P&L                                                  $-0.07|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-08-12  SELL  ALGN  Pullback50  $93.06  P&L $-0.12                |
|  2026-08-12  SELL  AKAM  Pullback50  $93.09  P&L $-0.17                |
|  2026-08-12  SELL  AXP  Pullback50  $94.12  P&L $+0.93                 |
|  2026-08-12  SELL  ADM  Pullback50  $12.64  P&L $-0.12                 |
|  2026-08-12  SELL  EXR  Pullback50  $68.70  P&L $-0.36                 |
|  2026-08-11  SELL  DHI  Pullback50  $93.11  P&L $-0.11                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=24 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-13T09:10:51.019794-04:00 ===

[Run context]
After hours (09:10 ET) — exit summary only.
Paper auth OK — equity $131411.66, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (after_hours) --                                      |
|Equity       : $131,411.66                                              |
|Open Risk    : 24 lots (26 broker pos)                                  |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 24 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=782   win= 42.2%  med= -47.1%  $+8,202           |
|  TAINTED            n=1701  win= 33.1%  med= -39.0%  $-8,382           |
|  KEEP-only          n=275   win= 64.7%  med= +37.7%  $+5,447           |
|  KEEP recent        n=88    win= 61.4%  med= +51.2%  $+1,398           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S403...                  |
|  KILL(15): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  79%  +107.1%    14                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.9%    14                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[PENDING EXITS (6)]                                                     |
+========================================================================+
|  b863 S408 AAPL260814C00317500 x1 stop_loss (-90.2%)                   |
|  b0   ORPHAN UBER260814C00081000 x1 stop_loss (-96.7%)                 |
|  b316 S355 AAPL260817C00320000 x1 stop_loss (-85.6%)                   |
|  b0   ORPHAN CVNA260814C00076000 x2 stop_loss (-63.0%)                 |
|  b98  S211 CVNA260814C00074000 x1 take_profit (+61.8%)                 |
|  ... 1 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (26)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  AAPL260814C00317500          17    -90.2%   $   -937.22               |
|  PATH260821C00015500           7    -27.3%   $    -84.00               |
|  CVNA260814C00076000           2    -63.0%   $    -58.00               |
|  AAPL260817C00320000           1    -85.6%   $    -53.69               |
|  SNOW260814C00360000           1   -100.0%   $    -45.00               |
|  PATH260814C00016000          12    -38.8%   $    -38.00               |
|  PATH260814C00015000           4    -22.5%   $    -36.00               |
|  C260814C00139000              2    -23.4%   $    -30.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-13.log
elapsed=0.9s reconcile=0.12s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.9s. run=#6953 https://github.com/28twagg-ops/TradingBot/actions/runs/31703561516
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 12.2% (303/2483) ALERT
# Options signal frequency

_Generated 2026-08-13T09:10:57.859592_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-13
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |    24 | WARN | <<<
| Total open lots             |    24 | INFO |
| Total closed lots           |  1713 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=782 med=-47.1% | TAINTED n=1701 med=-39.0% | KEEP-only n=275 med=+37.7% | KILL=15 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=465.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260813T131550Z

- UTC timestamp: `20260813T131550Z`
- GitHub run: [#6954](https://github.com/28twagg-ops/TradingBot/actions/runs/31703972497)
- Run id: `31703972497`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`11s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 782 | 42.2 | -47.1 | +12.1 | $+8,202 |
| TAINTED | 1701 | 33.1 | -39.0 | +10.2 | $-8,382 |
| KEEP-only | 275 | 64.7 | +37.7 | +42.1 | $+5,447 |
| KEEP-only recent | 88 | 61.4 | +51.2 | +54.0 | $+1,398 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S403, S404, S406
- KILL strategies (15): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-13T09:15:53.669094-04:00","date":"2026-08-13","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.33},"signals":0,"placed":0,"equity":131381.62,"open_positions":26,"pending_orders":0,"open_lots":24,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"6954","github_run_id":"31703972497","status":"ok","data_quality":{"clean":{"n":782,"win":42.2,"med":-47.14,"avg":12.07,"pnl":8202.42},"tainted":{"n":1701,"win":33.1,"med":-39.02,"avg":10.24,"pnl":-8382.34},"keep_only":{"n":275,"win":64.73,"med":37.69,"avg":42.15,"pnl":5447.45},"keep_only_recent":{"n":88,"win":61.36,"med":51.22,"avg":53.96,"pnl":1398.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S405","S407","S408"]}}
```

### Live bot full output

```text
13:15:51  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $465.51|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $465.51|
|  Cash                                                           $209.49|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $256.02|
|  Open P&L                                                        $-0.07|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $68.96     $97.48   $97.50   +0.0%   $+0.01  |
|  AES      Pullback50      $93.74     $14.72   $14.67   -0.4%   $-0.35  |
|  AFL      Pullback50      $93.31     $120.39  $120.73  +0.3%   $+0.26  |
|                                                                        |
|  Total invested                                                 $256.02|
|  Total open P&L                                                  $-0.07|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-08-12  SELL  ALGN  Pullback50  $93.06  P&L $-0.12                |
|  2026-08-12  SELL  AKAM  Pullback50  $93.09  P&L $-0.17                |
|  2026-08-12  SELL  AXP  Pullback50  $94.12  P&L $+0.93                 |
|  2026-08-12  SELL  ADM  Pullback50  $12.64  P&L $-0.12                 |
|  2026-08-12  SELL  EXR  Pullback50  $68.70  P&L $-0.36                 |
|  2026-08-11  SELL  DHI  Pullback50  $93.11  P&L $-0.11                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=24 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-13T09:15:53.669094-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $131381.62, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (after_hours) --                                      |
|Equity       : $131,381.62                                              |
|Open Risk    : 24 lots (26 broker pos)                                  |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 24 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=782   win= 42.2%  med= -47.1%  $+8,202           |
|  TAINTED            n=1701  win= 33.1%  med= -39.0%  $-8,382           |
|  KEEP-only          n=275   win= 64.7%  med= +37.7%  $+5,447           |
|  KEEP recent        n=88    win= 61.4%  med= +51.2%  $+1,398           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S403...                  |
|  KILL(15): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  79%  +107.1%    14                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.9%    14                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[PENDING EXITS (6)]                                                     |
+========================================================================+
|  b863 S408 AAPL260814C00317500 x1 stop_loss (-90.2%)                   |
|  b0   ORPHAN UBER260814C00081000 x1 stop_loss (-96.7%)                 |
|  b316 S355 AAPL260817C00320000 x1 stop_loss (-85.6%)                   |
|  b0   ORPHAN CVNA260814C00076000 x2 stop_loss (-63.0%)                 |
|  b98  S211 CVNA260814C00074000 x1 take_profit (+61.8%)                 |
|  ... 1 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (26)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  AAPL260814C00317500          17    -90.2%   $   -937.22               |
|  PATH260821C00015500           7    -27.3%   $    -84.00               |
|  CVNA260814C00076000           2    -63.0%   $    -58.00               |
|  AAPL260817C00320000           1    -85.6%   $    -53.69               |
|  SNOW260814C00360000           1   -100.0%   $    -45.00               |
|  PATH260814C00016000          12    -38.8%   $    -38.00               |
|  PATH260814C00015000           4    -22.5%   $    -36.00               |
|  C260814C00139000              2    -23.4%   $    -30.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-13.log
elapsed=0.9s reconcile=0.33s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.9s. run=#6954 https://github.com/28twagg-ops/TradingBot/actions/runs/31703972497
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 12.2% (303/2483) ALERT
# Options signal frequency

_Generated 2026-08-13T09:16:00.387976_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-13
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |    24 | WARN | <<<
| Total open lots             |    24 | INFO |
| Total closed lots           |  1713 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=782 med=-47.1% | TAINTED n=1701 med=-39.0% | KEEP-only n=275 med=+37.7% | KILL=15 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=465.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260813T132053Z

- UTC timestamp: `20260813T132053Z`
- GitHub run: [#6955](https://github.com/28twagg-ops/TradingBot/actions/runs/31704380049)
- Run id: `31704380049`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 782 | 42.2 | -47.1 | +12.1 | $+8,202 |
| TAINTED | 1701 | 33.1 | -39.0 | +10.2 | $-8,382 |
| KEEP-only | 275 | 64.7 | +37.7 | +42.1 | $+5,447 |
| KEEP-only recent | 88 | 61.4 | +51.2 | +54.0 | $+1,398 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S403, S404, S406
- KILL strategies (15): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-13T09:20:56.624563-04:00","date":"2026-08-13","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.43},"signals":0,"placed":0,"equity":131347.66,"open_positions":26,"pending_orders":0,"open_lots":24,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"6955","github_run_id":"31704380049","status":"ok","data_quality":{"clean":{"n":782,"win":42.2,"med":-47.14,"avg":12.07,"pnl":8202.42},"tainted":{"n":1701,"win":33.1,"med":-39.02,"avg":10.24,"pnl":-8382.34},"keep_only":{"n":275,"win":64.73,"med":37.69,"avg":42.15,"pnl":5447.45},"keep_only_recent":{"n":88,"win":61.36,"med":51.22,"avg":53.96,"pnl":1398.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S405","S407","S408"]}}
```

### Live bot full output

```text
13:20:54  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $465.51|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $465.51|
|  Cash                                                           $209.49|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $256.02|
|  Open P&L                                                        $-0.07|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $68.96     $97.48   $97.50   +0.0%   $+0.01  |
|  AES      Pullback50      $93.74     $14.72   $14.67   -0.4%   $-0.35  |
|  AFL      Pullback50      $93.31     $120.39  $120.73  +0.3%   $+0.26  |
|                                                                        |
|  Total invested                                                 $256.02|
|  Total open P&L                                                  $-0.07|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-08-12  SELL  ALGN  Pullback50  $93.06  P&L $-0.12                |
|  2026-08-12  SELL  AKAM  Pullback50  $93.09  P&L $-0.17                |
|  2026-08-12  SELL  AXP  Pullback50  $94.12  P&L $+0.93                 |
|  2026-08-12  SELL  ADM  Pullback50  $12.64  P&L $-0.12                 |
|  2026-08-12  SELL  EXR  Pullback50  $68.70  P&L $-0.36                 |
|  2026-08-11  SELL  DHI  Pullback50  $93.11  P&L $-0.11                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=24 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-13T09:20:56.624563-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $131347.66, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (after_hours) --                                      |
|Equity       : $131,347.66                                              |
|Open Risk    : 24 lots (26 broker pos)                                  |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 24 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=782   win= 42.2%  med= -47.1%  $+8,202           |
|  TAINTED            n=1701  win= 33.1%  med= -39.0%  $-8,382           |
|  KEEP-only          n=275   win= 64.7%  med= +37.7%  $+5,447           |
|  KEEP recent        n=88    win= 61.4%  med= +51.2%  $+1,398           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S403...                  |
|  KILL(15): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  79%  +107.1%    14                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.9%    14                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[PENDING EXITS (6)]                                                     |
+========================================================================+
|  b863 S408 AAPL260814C00317500 x1 stop_loss (-90.2%)                   |
|  b0   ORPHAN UBER260814C00081000 x1 stop_loss (-96.7%)                 |
|  b316 S355 AAPL260817C00320000 x1 stop_loss (-85.6%)                   |
|  b0   ORPHAN CVNA260814C00076000 x2 stop_loss (-63.0%)                 |
|  b98  S211 CVNA260814C00074000 x1 take_profit (+61.8%)                 |
|  ... 1 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (26)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  AAPL260814C00317500          17    -90.2%   $   -937.22               |
|  PATH260821C00015500           7    -27.3%   $    -84.00               |
|  CVNA260814C00076000           2    -63.0%   $    -58.00               |
|  AAPL260817C00320000           1    -85.6%   $    -53.69               |
|  SNOW260814C00360000           1   -100.0%   $    -45.00               |
|  PATH260814C00016000          12    -38.8%   $    -38.00               |
|  PATH260814C00015000           4    -22.5%   $    -36.00               |
|  C260814C00139000              2    -23.4%   $    -30.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-13.log
elapsed=0.9s reconcile=0.43s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.9s. run=#6955 https://github.com/28twagg-ops/TradingBot/actions/runs/31704380049
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 12.2% (303/2483) ALERT
# Options signal frequency

_Generated 2026-08-13T09:21:01.354036_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-13
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |    24 | WARN | <<<
| Total open lots             |    24 | INFO |
| Total closed lots           |  1713 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=782 med=-47.1% | TAINTED n=1701 med=-39.0% | KEEP-only n=275 med=+37.7% | KILL=15 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=465.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260813T132549Z

- UTC timestamp: `20260813T132549Z`
- GitHub run: [#6956](https://github.com/28twagg-ops/TradingBot/actions/runs/31704800085)
- Run id: `31704800085`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`11s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 782 | 42.2 | -47.1 | +12.1 | $+8,202 |
| TAINTED | 1701 | 33.1 | -39.0 | +10.2 | $-8,382 |
| KEEP-only | 275 | 64.7 | +37.7 | +42.1 | $+5,447 |
| KEEP-only recent | 88 | 61.4 | +51.2 | +54.0 | $+1,398 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S403, S404, S406
- KILL strategies (15): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-13T09:25:52.698758-04:00","date":"2026-08-13","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":131207.66,"open_positions":26,"pending_orders":0,"open_lots":24,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"6956","github_run_id":"31704800085","status":"ok","data_quality":{"clean":{"n":782,"win":42.2,"med":-47.14,"avg":12.07,"pnl":8202.42},"tainted":{"n":1701,"win":33.1,"med":-39.02,"avg":10.24,"pnl":-8382.34},"keep_only":{"n":275,"win":64.73,"med":37.69,"avg":42.15,"pnl":5447.45},"keep_only_recent":{"n":88,"win":61.36,"med":51.22,"avg":53.96,"pnl":1398.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S405","S407","S408"]}}
```

### Live bot full output

```text
13:25:50  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $465.51|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $465.51|
|  Cash                                                           $209.49|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $256.02|
|  Open P&L                                                        $-0.07|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $68.96     $97.48   $97.50   +0.0%   $+0.01  |
|  AES      Pullback50      $93.74     $14.72   $14.67   -0.4%   $-0.35  |
|  AFL      Pullback50      $93.31     $120.39  $120.73  +0.3%   $+0.26  |
|                                                                        |
|  Total invested                                                 $256.02|
|  Total open P&L                                                  $-0.07|
+========================================================================+

+========================================================================+
|                        EXIT LOGIC ACTIVE  (v8)                         |
+========================================================================+
|  Profit target                              price > 20-day MA (midline)|
|  Stop loss                                             -0.5% from entry|
|  Time stop                                          max 3 calendar days|
+========================================================================+

+========================================================================+
|                          RECENT TRANSACTIONS                           |
+========================================================================+
|  2026-08-12  SELL  ALGN  Pullback50  $93.06  P&L $-0.12                |
|  2026-08-12  SELL  AKAM  Pullback50  $93.09  P&L $-0.17                |
|  2026-08-12  SELL  AXP  Pullback50  $94.12  P&L $+0.93                 |
|  2026-08-12  SELL  ADM  Pullback50  $12.64  P&L $-0.12                 |
|  2026-08-12  SELL  EXR  Pullback50  $68.70  P&L $-0.36                 |
|  2026-08-11  SELL  DHI  Pullback50  $93.11  P&L $-0.11                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=24 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-13T09:25:52.698758-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $131207.66, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (after_hours) --                                      |
|Equity       : $131,207.66                                              |
|Open Risk    : 24 lots (26 broker pos)                                  |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 24 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=782   win= 42.2%  med= -47.1%  $+8,202           |
|  TAINTED            n=1701  win= 33.1%  med= -39.0%  $-8,382           |
|  KEEP-only          n=275   win= 64.7%  med= +37.7%  $+5,447           |
|  KEEP recent        n=88    win= 61.4%  med= +51.2%  $+1,398           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S403...                  |
|  KILL(15): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  79%  +107.1%    14                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.9%    14                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[PENDING EXITS (6)]                                                     |
+========================================================================+
|  b863 S408 AAPL260814C00317500 x1 stop_loss (-90.2%)                   |
|  b0   ORPHAN UBER260814C00081000 x1 stop_loss (-96.7%)                 |
|  b316 S355 AAPL260817C00320000 x1 stop_loss (-85.6%)                   |
|  b0   ORPHAN CVNA260814C00076000 x2 stop_loss (-63.0%)                 |
|  b98  S211 CVNA260814C00074000 x1 take_profit (+61.8%)                 |
|  ... 1 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (26)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  AAPL260814C00317500          17    -90.2%   $   -937.22               |
|  PATH260821C00015500           7    -27.3%   $    -84.00               |
|  CVNA260814C00076000           2    -63.0%   $    -58.00               |
|  AAPL260817C00320000           1    -85.6%   $    -53.69               |
|  SNOW260814C00360000           1   -100.0%   $    -45.00               |
|  PATH260814C00016000          12    -38.8%   $    -38.00               |
|  PATH260814C00015000           4    -22.5%   $    -36.00               |
|  C260814C00139000              2    -23.4%   $    -30.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-13.log
elapsed=0.6s reconcile=0.12s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.6s. run=#6956 https://github.com/28twagg-ops/TradingBot/actions/runs/31704800085
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 12.2% (303/2483) ALERT
# Options signal frequency

_Generated 2026-08-13T09:25:59.079774_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-13
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |    24 | WARN | <<<
| Total open lots             |    24 | INFO |
| Total closed lots           |  1713 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=782 med=-47.1% | TAINTED n=1701 med=-39.0% | KEEP-only n=275 med=+37.7% | KILL=15 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=465.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260813T133051Z

- UTC timestamp: `20260813T133051Z`
- GitHub run: [#6957](https://github.com/28twagg-ops/TradingBot/actions/runs/31705205454)
- Run id: `31705205454`
- Live bot: exit=`0`, duration=`216s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 782 | 42.2 | -47.1 | +12.1 | $+8,202 |
| TAINTED | 1701 | 33.1 | -39.0 | +10.2 | $-8,382 |
| KEEP-only | 275 | 64.7 | +37.7 | +42.1 | $+5,447 |
| KEEP-only recent | 88 | 61.4 | +51.2 | +54.0 | $+1,398 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S403, S404, S406
- KILL strategies (15): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-13T09:25:52.698758-04:00","date":"2026-08-13","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":131207.66,"open_positions":26,"pending_orders":0,"open_lots":24,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"6956","github_run_id":"31704800085","status":"ok","data_quality":{"clean":{"n":782,"win":42.2,"med":-47.14,"avg":12.07,"pnl":8202.42},"tainted":{"n":1701,"win":33.1,"med":-39.02,"avg":10.24,"pnl":-8382.34},"keep_only":{"n":275,"win":64.73,"med":37.69,"avg":42.15,"pnl":5447.45},"keep_only_recent":{"n":88,"win":61.36,"med":51.22,"avg":53.96,"pnl":1398.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S405","S407","S408"]}}
```

### Live bot full output

```text
13:30:52  INFO      Mode: morning_prep
13:30:54  INFO        [prep_positions] 3/3 (3 valid)
13:30:54  INFO      Fetching tickers (universe=both)...
13:30:54  INFO        S&P 500: 503
13:30:54  INFO        MidCap 400: 400
13:30:54  INFO        Total: 903 tickers
13:30:55  INFO        [prep_universe] 40/900 (40 valid)
13:30:58  INFO        [prep_universe] 80/900 (80 valid)
13:31:01  INFO        [prep_universe] 120/900 (120 valid)
13:31:06  INFO        [prep_universe] 160/900 (160 valid)
13:31:07  INFO        [prep_universe] 200/900 (199 valid)
13:31:11  INFO        [prep_universe] 240/900 (238 valid)
13:31:19  INFO        [prep_universe] 280/900 (278 valid)
13:31:32  INFO        [prep_universe] 320/900 (318 valid)
13:31:45  INFO        [prep_universe] 360/900 (358 valid)
13:31:56  INFO        [prep_universe] 400/900 (397 valid)
13:32:09  INFO        [prep_universe] 440/900 (437 valid)
13:32:20  INFO        [prep_universe] 480/900 (477 valid)
13:32:31  INFO        [prep_universe] 520/900 (517 valid)
13:32:44  INFO        [prep_universe] 560/900 (557 valid)
13:32:57  INFO        [prep_universe] 600/900 (597 valid)
13:33:08  INFO        [prep_universe] 640/900 (637 valid)
13:33:21  INFO        [prep_universe] 680/900 (677 valid)
13:33:31  INFO        [prep_universe] 720/900 (717 valid)
13:33:44  INFO        [prep_universe] 760/900 (757 valid)
13:33:55  INFO        [prep_universe] 800/900 (797 valid)
13:34:08  INFO        [prep_universe] 840/900 (836 valid)
13:34:19  INFO        [prep_universe] 880/900 (876 valid)
13:34:25  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.04|
+========================================================================+

+========================================================================+
|                              MORNING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/morning_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       3|
|  Invested                                                       $257.55|
|  Open P&L                                                        $+1.46|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $69.50     $97.48   $98.26   +0.8%   $+0.55  |
|  AES      Pullback50      $94.12     $14.72   $14.72   +0.0%   $+0.03  |
|  AFL      Pullback50      $93.93     $120.39  $121.53  +0.9%   $+0.88  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                0|
|                                                                        |
|  No open sell orders.                                                  |
|                                                                        |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   42|
|  Universe scanned                                                   900|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=24 paper_keys=yes dry_run=False
  alpaca positions=24
  FLAG b0|ORPHAN|cd5fda70 missing from Alpaca
  FLAG b0|ORPHAN|f10eefde missing from Alpaca
  FLAG b0|ORPHAN|ce546f7d missing from Alpaca
  FLAG b0|ORPHAN|5db59d4a missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-13T09:34:30.317126-04:00 ===

[Run context]
Paper auth OK — equity $131119.53, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
2026-08-13 09:34:33,580 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-83.3%) SELL 1 XOM260814C00162500 @<= 0.04
2026-08-13 09:34:35,108 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+92.0%) SELL 2 CVNA260814C00075000 @<= 0.36
2026-08-13 09:34:35,455 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+78.6%) SELL 1 MCD260814C00280000 @<= 0.72
2026-08-13 09:34:36,103 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-97.3%) SELL 2 PATH260828C00016500 @<= 0.01
2026-08-13 09:34:36,771 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-91.1%) SELL 1 SNOW260814C00360000 @<= 0.05
2026-08-13 09:34:37,778 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-93.5%) SELL 14 AAPL260814C00317500 @<= 0.01
Protective stops: placed=1 already=15 failed=4

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260813T134149Z

- UTC timestamp: `20260813T134149Z`
- GitHub run: [#6959](https://github.com/28twagg-ops/TradingBot/actions/runs/31706079602)
- Run id: `31706079602`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 782 | 42.2 | -47.1 | +12.1 | $+8,202 |
| TAINTED | 1701 | 33.1 | -39.0 | +10.2 | $-8,382 |
| KEEP-only | 275 | 64.7 | +37.7 | +42.1 | $+5,447 |
| KEEP-only recent | 88 | 61.4 | +51.2 | +54.0 | $+1,398 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S403, S404, S406
- KILL strategies (15): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-13T09:25:52.698758-04:00","date":"2026-08-13","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":131207.66,"open_positions":26,"pending_orders":0,"open_lots":24,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"6956","github_run_id":"31704800085","status":"ok","data_quality":{"clean":{"n":782,"win":42.2,"med":-47.14,"avg":12.07,"pnl":8202.42},"tainted":{"n":1701,"win":33.1,"med":-39.02,"avg":10.24,"pnl":-8382.34},"keep_only":{"n":275,"win":64.73,"med":37.69,"avg":42.15,"pnl":5447.45},"keep_only_recent":{"n":88,"win":61.36,"med":51.22,"avg":53.96,"pnl":1398.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S405","S407","S408"]}}
```

### Live bot full output

```text
13:41:50  INFO      Mode: morning_prep
13:41:51  INFO        [prep_positions] 3/3 (3 valid)
13:41:51  INFO        Universe cache hit: 903 tickers (tickers_2026-08-13.json)
13:41:52  INFO        [prep_universe] 40/900 (40 valid)
13:41:54  INFO        [prep_universe] 80/900 (80 valid)
13:41:55  INFO        [prep_universe] 120/900 (120 valid)
13:41:57  INFO        [prep_universe] 160/900 (160 valid)
13:41:59  INFO        [prep_universe] 200/900 (199 valid)
13:42:06  INFO        [prep_universe] 240/900 (238 valid)
13:42:17  INFO        [prep_universe] 280/900 (278 valid)
13:42:30  INFO        [prep_universe] 320/900 (318 valid)
13:42:41  INFO        [prep_universe] 360/900 (358 valid)
13:42:55  INFO        [prep_universe] 400/900 (397 valid)
13:43:05  INFO        [prep_universe] 440/900 (437 valid)
13:43:19  INFO        [prep_universe] 480/900 (477 valid)
13:43:29  INFO        [prep_universe] 520/900 (517 valid)
13:43:42  INFO        [prep_universe] 560/900 (557 valid)
13:43:53  INFO        [prep_universe] 600/900 (597 valid)
13:44:07  INFO        [prep_universe] 640/900 (637 valid)
13:44:17  INFO        [prep_universe] 680/900 (677 valid)
13:44:31  INFO        [prep_universe] 720/900 (717 valid)
13:44:41  INFO        [prep_universe] 760/900 (757 valid)
13:44:55  INFO        [prep_universe] 800/900 (797 valid)
13:45:05  INFO        [prep_universe] 840/900 (836 valid)
```

### Options bot full output

```text

## Run 20260813T134654Z

- UTC timestamp: `20260813T134654Z`
- GitHub run: [#6960](https://github.com/28twagg-ops/TradingBot/actions/runs/31706514298)
- Run id: `31706514298`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 782 | 42.2 | -47.1 | +12.1 | $+8,202 |
| TAINTED | 1701 | 33.1 | -39.0 | +10.2 | $-8,382 |
| KEEP-only | 275 | 64.7 | +37.7 | +42.1 | $+5,447 |
| KEEP-only recent | 88 | 61.4 | +51.2 | +54.0 | $+1,398 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S403, S404, S406
- KILL strategies (15): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-13T09:25:52.698758-04:00","date":"2026-08-13","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":131207.66,"open_positions":26,"pending_orders":0,"open_lots":24,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"6956","github_run_id":"31704800085","status":"ok","data_quality":{"clean":{"n":782,"win":42.2,"med":-47.14,"avg":12.07,"pnl":8202.42},"tainted":{"n":1701,"win":33.1,"med":-39.02,"avg":10.24,"pnl":-8382.34},"keep_only":{"n":275,"win":64.73,"med":37.69,"avg":42.15,"pnl":5447.45},"keep_only_recent":{"n":88,"win":61.36,"med":51.22,"avg":53.96,"pnl":1398.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S405","S407","S408"]}}
```

### Live bot full output

```text
13:46:55  INFO      Mode: morning_scan
13:46:56  INFO        [positions] 3/3 (3 valid)
13:46:56  INFO        Universe cache hit: 903 tickers (tickers_2026-08-13.json)
13:46:57  INFO        [universe] 40/900 (40 valid)
13:46:58  INFO        [universe] 80/900 (80 valid)
13:47:00  INFO        [universe] 120/900 (120 valid)
13:47:01  INFO        [universe] 160/900 (160 valid)
13:47:03  INFO        [universe] 200/900 (199 valid)
13:47:10  INFO        [universe] 240/900 (238 valid)
13:47:24  INFO        [universe] 280/900 (278 valid)
13:47:34  INFO        [universe] 320/900 (318 valid)
13:47:47  INFO        [universe] 360/900 (358 valid)
13:47:58  INFO        [universe] 400/900 (397 valid)
13:48:11  INFO        [universe] 440/900 (437 valid)
13:48:21  INFO        [universe] 480/900 (477 valid)
13:48:34  INFO        [universe] 520/900 (517 valid)
13:48:47  INFO        [universe] 560/900 (557 valid)
13:48:58  INFO        [universe] 600/900 (597 valid)
13:49:11  INFO        [universe] 640/900 (637 valid)
13:49:21  INFO        [universe] 680/900 (677 valid)
13:49:34  INFO        [universe] 720/900 (717 valid)
13:49:47  INFO        [universe] 760/900 (757 valid)
13:49:58  INFO        [universe] 800/900 (797 valid)
13:50:11  INFO        [universe] 840/900 (836 valid)
```

### Options bot full output

```text

## Run 20260813T135123Z

- UTC timestamp: `20260813T135123Z`
- GitHub run: [#6961](https://github.com/28twagg-ops/TradingBot/actions/runs/31706952586)
- Run id: `31706952586`
- Live bot: exit=`0`, duration=`217s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 782 | 42.2 | -47.1 | +12.1 | $+8,202 |
| TAINTED | 1701 | 33.1 | -39.0 | +10.2 | $-8,382 |
| KEEP-only | 275 | 64.7 | +37.7 | +42.1 | $+5,447 |
| KEEP-only recent | 88 | 61.4 | +51.2 | +54.0 | $+1,398 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S403, S404, S406
- KILL strategies (15): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-13T09:25:52.698758-04:00","date":"2026-08-13","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":131207.66,"open_positions":26,"pending_orders":0,"open_lots":24,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"6956","github_run_id":"31704800085","status":"ok","data_quality":{"clean":{"n":782,"win":42.2,"med":-47.14,"avg":12.07,"pnl":8202.42},"tainted":{"n":1701,"win":33.1,"med":-39.02,"avg":10.24,"pnl":-8382.34},"keep_only":{"n":275,"win":64.73,"med":37.69,"avg":42.15,"pnl":5447.45},"keep_only_recent":{"n":88,"win":61.36,"med":51.22,"avg":53.96,"pnl":1398.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S405","S407","S408"]}}
```

### Live bot full output

```text
13:51:24  INFO      Mode: morning_scan
13:51:25  INFO        [positions] 3/3 (3 valid)
13:51:25  INFO        Universe cache hit: 903 tickers (tickers_2026-08-13.json)
13:51:26  INFO        [universe] 40/900 (40 valid)
13:51:27  INFO        [universe] 80/900 (80 valid)
13:51:29  INFO        [universe] 120/900 (120 valid)
13:51:30  INFO        [universe] 160/900 (160 valid)
13:51:31  INFO        [universe] 200/900 (199 valid)
13:51:39  INFO        [universe] 240/900 (238 valid)
13:51:52  INFO        [universe] 280/900 (278 valid)
13:52:03  INFO        [universe] 320/900 (318 valid)
13:52:16  INFO        [universe] 360/900 (358 valid)
13:52:26  INFO        [universe] 400/900 (397 valid)
13:52:40  INFO        [universe] 440/900 (437 valid)
13:52:53  INFO        [universe] 480/900 (477 valid)
13:53:03  INFO        [universe] 520/900 (517 valid)
13:53:16  INFO        [universe] 560/900 (557 valid)
13:53:26  INFO        [universe] 600/900 (597 valid)
13:53:40  INFO        [universe] 640/900 (637 valid)
13:53:53  INFO        [universe] 680/900 (677 valid)
13:54:03  INFO        [universe] 720/900 (717 valid)
13:54:16  INFO        [universe] 760/900 (757 valid)
13:54:27  INFO        [universe] 800/900 (797 valid)
13:54:41  INFO        [universe] 840/900 (836 valid)
13:54:51  INFO        [universe] 880/900 (876 valid)
13:54:58  INFO        [universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.55|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-13|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled  GapDown, GoldenPocket, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $466.55|
|  Cash                                                           $209.49|
|  Reserve                                          $23.33  (always kept)|
|  Available                                    $186.16  (for new trades)|
|  Trade size             $69.98  (15% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (3 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $69.27     $97.48   $97.94   +0.5%   $+0.32  |
|  AES      Pullback50      $94.06     $14.72   $14.71   -0.0%   $-0.03  |
|  AFL      Pullback50      $93.73     $120.39  $121.27  +0.7%   $+0.68  |
|                                                                        |
|  Total invested                                                 $257.06|
|  Total open P&L                                                  $+0.97|
|  Buys today: 0  |  entry cap: 0  |  max open: 3                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (50405.9m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  AES  P&L -0.0%  $-0.03                                            HOLD|
|  ACGL  P&L +0.5%  $+0.32                                           HOLD|
|  AFL  P&L +0.7%  $+0.68                                            HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 0 | filled 0 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 3|
|  Stop-loss breaches                                                none|
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+

+========================================================================+
|                             DATA DOWNLOAD                              |
+========================================================================+
|  Universe: both  |  Alpaca primary / yfinance fallback                 |
+========================================================================+

+========================================================================+
|                              SIGNAL SCAN                               |
+========================================================================+
|  Month: Aug  |  Regime: BULL                                           |
|  Primary: VolumeSpike  |  Secondary: 52wkLow (display only — schedule ~|
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  34                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  ADM      Pullback50      eq     $80.15   34.4   -2.52   50MA bounce (+|
|  CDW      Pullback50      eq     $136.99  53.1   -1.57   50MA bounce (+|
|  DDOG     Pullback50      eq     $248.85  50.6   -1.57   50MA bounce (+|
|  D        Pullback50      eq     $68.31   32.7   -2.13   50MA bounce (-|
|  EG       Pullback50      eq     $364.30  34.4   -2.59   50MA bounce (+|
|  EVRG     Pullback50      eq     $83.79   31.8   -3.07   50MA bounce (-|
|  ESS      Pullback50      eq     $286.43  42.7   -2.02   50MA bounce (-|
|  ES       Pullback50      eq     $72.40   36.4   -2.18   50MA bounce (+|
|  EXR      Pullback50      eq     $148.38  51.9   -1.91   50MA bounce (+|
|  GS       Pullback50      eq     $1048.~  47.2   -2.79   50MA bounce (-|
|  HRL      Pullback50      eq     $24.62   41.3   -2.54   50MA bounce (-|
|  JBHT     Pullback50      eq     $281.95  44.9   -2.43   50MA bounce (+|
|  IBKR     Pullback50      eq     $92.04   50.6   -2.80   50MA bounce (+|
|  KMI      Pullback50      eq     $31.80   39.0   -2.45   50MA bounce (-|
|  MAA      Pullback50      eq     $134.72  52.0   -2.07   50MA bounce (-|
|  HOOD     Pullback50      eq     $99.63   58.2   -2.27   50MA bounce (+|
|  O        Pullback50      eq     $63.19   29.1   -2.10   50MA bounce (+|
|  SPG      Pullback50      eq     $222.28  37.1   -2.94   50MA bounce (+|
|  STX      Pullback50      eq     $887.12  54.3   -2.62   50MA bounce (-|
|  TRGP     Pullback50      eq     $268.10  40.8   -2.56   50MA bounce (-|
|  VTR      Pullback50      eq     $90.29   30.0   -2.43   50MA bounce (+|
|  WRB      Pullback50      eq     $70.22   21.3   -2.18   50MA bounce (-|
|  XEL      Pullback50      eq     $79.31   37.7   -2.83   50MA bounce (+|
|  ALLY     Pullback50      eq     $44.63   62.4   -2.10   50MA bounce (+|
|  AM       Pullback50      eq     $22.21   43.3   -2.77   50MA bounce (+|
|  CUZ      Pullback50      eq     $29.94   25.9   -2.33   50MA bounce (-|
|  ELS      Pullback50      eq     $64.84   44.3   -2.07   50MA bounce (+|
|  GBCI     Pullback50      eq     $49.76   46.9   -2.68   50MA bounce (-|13:54:59  INFO        place_all_stops: checking 3 positions...
13:54:59  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
13:54:59  INFO        STOP-MARKET placed AES  qty=6 (pos=6.3920)  stop=$14.65  id=47179b8f-8af7-4aa8-bb36-a5f08d457290
13:54:59  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
13:55:00  INFO        Daily log -> logs/daily/2026-08-13.md
13:55:00  INFO        Dashboard written → logs/dashboard.md

|  FR       Pullback50      eq     $63.88   26.9   -2.45   50MA bounce (-|
|  MOH      Pullback50      eq     $209.01  62.4   -0.67   50MA bounce (-|
|  RYN      Pullback50      eq     $21.63   50.6   -2.12   50MA bounce (+|
|  SIGI     Pullback50      eq     $94.67   44.6   -1.88   50MA bounce (+|
|  VIAV     Pullback50      eq     $43.28   56.7   -2.09   50MA bounce (-|
|  XPO      Pullback50      eq     $209.96  47.0   -2.14   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|  Skipped                                  no entry slots (max_trades=0)|
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            896|
|  Signals                                                             34|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $466.77|
|  Cash                                                           $209.49|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=20 paper_keys=yes dry_run=False
  alpaca positions=19
  FLAG b0|ORPHAN|d9953782 missing from Alpaca
  FLAG b0|ORPHAN|4798ec8c missing from Alpaca
  FLAG b0|ORPHAN|312dbb34 missing from Alpaca
  FLAG b0|ORPHAN|36b3780d missing from Alpaca
  FLAG b0|ORPHAN|2bf8b0ff missing from Alpaca
  FLAG b0|ORPHAN|bf641e7d missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-13T09:55:01.995482-04:00 ===

[Run context]
Paper auth OK — equity $134501.84, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Protective stops: placed=1 already=13 failed=0

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
```

---

## Run 20260813T135612Z

- UTC timestamp: `20260813T135612Z`
- GitHub run: [#6962](https://github.com/28twagg-ops/TradingBot/actions/runs/31707391911)
- Run id: `31707391911`
- Live bot: exit=`0`, duration=`215s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 782 | 42.2 | -47.1 | +12.1 | $+8,202 |
| TAINTED | 1701 | 33.1 | -39.0 | +10.2 | $-8,382 |
| KEEP-only | 275 | 64.7 | +37.7 | +42.1 | $+5,447 |
| KEEP-only recent | 88 | 61.4 | +51.2 | +54.0 | $+1,398 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S403, S404, S406
- KILL strategies (15): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-13T09:25:52.698758-04:00","date":"2026-08-13","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":131207.66,"open_positions":26,"pending_orders":0,"open_lots":24,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"6956","github_run_id":"31704800085","status":"ok","data_quality":{"clean":{"n":782,"win":42.2,"med":-47.14,"avg":12.07,"pnl":8202.42},"tainted":{"n":1701,"win":33.1,"med":-39.02,"avg":10.24,"pnl":-8382.34},"keep_only":{"n":275,"win":64.73,"med":37.69,"avg":42.15,"pnl":5447.45},"keep_only_recent":{"n":88,"win":61.36,"med":51.22,"avg":53.96,"pnl":1398.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S405","S407","S408"]}}
```

### Live bot full output

```text
13:56:13  INFO      Mode: morning_scan
13:56:13  INFO        [positions] 3/3 (3 valid)
13:56:13  INFO        Universe cache hit: 903 tickers (tickers_2026-08-13.json)
13:56:14  INFO        [universe] 40/900 (40 valid)
13:56:15  INFO        [universe] 80/900 (80 valid)
13:56:17  INFO        [universe] 120/900 (120 valid)
13:56:18  INFO        [universe] 160/900 (160 valid)
13:56:20  INFO        [universe] 200/900 (199 valid)
13:56:28  INFO        [universe] 240/900 (238 valid)
13:56:41  INFO        [universe] 280/900 (278 valid)
13:56:51  INFO        [universe] 320/900 (318 valid)
13:57:05  INFO        [universe] 360/900 (358 valid)
13:57:15  INFO        [universe] 400/900 (397 valid)
13:57:28  INFO        [universe] 440/900 (437 valid)
13:57:38  INFO        [universe] 480/900 (477 valid)
13:57:51  INFO        [universe] 520/900 (517 valid)
13:58:04  INFO        [universe] 560/900 (557 valid)
13:58:14  INFO        [universe] 600/900 (597 valid)
13:58:27  INFO        [universe] 640/900 (637 valid)
13:58:40  INFO        [universe] 680/900 (677 valid)
13:58:51  INFO        [universe] 720/900 (717 valid)
13:59:04  INFO        [universe] 760/900 (757 valid)
13:59:17  INFO        [universe] 800/900 (797 valid)
13:59:27  INFO        [universe] 840/900 (836 valid)
13:59:40  INFO        [universe] 880/900 (876 valid)
13:59:44  INFO        [universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.92|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-13|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled  GapDown, GoldenPocket, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $466.92|
|  Cash                                                           $209.49|
|  Reserve                                          $23.35  (always kept)|
|  Available                                    $186.14  (for new trades)|
|  Trade size             $70.04  (15% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (3 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $69.49     $97.48   $98.24   +0.8%   $+0.54  |
|  AES      Pullback50      $94.06     $14.72   $14.71   -0.0%   $-0.03  |
|  AFL      Pullback50      $93.89     $120.39  $121.47  +0.9%   $+0.84  |
|                                                                        |
|  Total invested                                                 $257.43|
|  Total open P&L                                                  $+1.34|
|  Buys today: 0  |  entry cap: 0  |  max open: 3                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (50410.7m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  AES  P&L -0.0%  $-0.03                                            HOLD|
|  ACGL  P&L +0.8%  $+0.54                                           HOLD|
|  AFL  P&L +0.9%  $+0.84                                            HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 0 | filled 0 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 3|
|  Stop-loss breaches                                                none|
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+

+========================================================================+
|                             DATA DOWNLOAD                              |
+========================================================================+
|  Universe: both  |  Alpaca primary / yfinance fallback                 |
+========================================================================+

+========================================================================+
|                              SIGNAL SCAN                               |
+========================================================================+
|  Month: Aug  |  Regime: BULL                                           |
|  Primary: VolumeSpike  |  Secondary: 52wkLow (display only — schedule ~|
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  35                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  ADM      Pullback50      eq     $80.05   34.0   -2.51   50MA bounce (-|
|  CB       Pullback50      eq     $345.83  32.9   -1.90   50MA bounce (+|
|  DDOG     Pullback50      eq     $248.02  50.4   -1.55   50MA bounce (-|
|  D        Pullback50      eq     $68.28   32.4   -2.07   50MA bounce (-|
|  ESS      Pullback50      eq     $288.00  44.5   -2.01   50MA bounce (-|
|  EXR      Pullback50      eq     $148.72  52.9   -1.91   50MA bounce (+|
|  ES       Pullback50      eq     $72.29   35.6   -2.18   50MA bounce (+|
|  GS       Pullback50      eq     $1047.~  46.9   -2.77   50MA bounce (-|
|  HRL      Pullback50      eq     $24.69   42.3   -2.53   50MA bounce (-|
|  IRM      Pullback50      eq     $124.68  43.5   -2.50   50MA bounce (+|
|  JBHT     Pullback50      eq     $280.94  44.0   -2.42   50MA bounce (+|
|  KMI      Pullback50      eq     $31.70   37.8   -2.44   50MA bounce (-|
|  MAA      Pullback50      eq     $135.00  52.7   -2.07   50MA bounce (-|
|  PLD      Pullback50      eq     $141.93  35.0   -1.37   50MA bounce (-|
|  O        Pullback50      eq     $63.09   27.8   -2.08   50MA bounce (+|
|  RSG      Pullback50      eq     $215.80  47.8   -3.08   50MA bounce (+|
|  HOOD     Pullback50      eq     $99.48   58.0   -2.21   50MA bounce (+|
|  STX      Pullback50      eq     $888.80  54.5   -2.60   50MA bounce (+|
|  SPG      Pullback50      eq     $222.63  37.8   -2.93   50MA bounce (+|
|  VTR      Pullback50      eq     $90.29   30.0   -2.42   50MA bounce (+|
|  WRB      Pullback50      eq     $70.29   21.9   -2.18   50MA bounce (-|
|  XEL      Pullback50      eq     $79.17   36.8   -2.82   50MA bounce (-|
|  ALLY     Pullback50      eq     $44.64   62.5   -2.09   50MA bounce (+|
|  AM       Pullback50      eq     $22.18   43.0   -2.76   50MA bounce (+|
|  BKH      Pullback50      eq     $74.11   44.8   -2.22   50MA bounce (+|
|  CAVA     Pullback50      eq     $71.87   68.3   -1.55   50MA bounce (-|
|  CUZ      Pullback50      eq     $29.93   25.8   -2.33   50MA bounce (-|
|  ELS      Pullback50      eq     $64.83   44.2   -2.06   50MA bounce (+|13:59:47  INFO        place_all_stops: checking 3 positions...
13:59:47  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
13:59:47  INFO        STOP already live AES @ $14.65
13:59:47  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
13:59:47  INFO        Daily log -> logs/daily/2026-08-13.md
13:59:47  INFO        Dashboard written → logs/dashboard.md

|  FR       Pullback50      eq     $63.97   27.9   -2.44   50MA bounce (-|
|  GBCI     Pullback50      eq     $49.77   47.0   -2.68   50MA bounce (-|
|  MOH      Pullback50      eq     $208.51  61.9   -0.67   50MA bounce (-|
|  MSM      Pullback50      eq     $120.11  36.4   -2.89   50MA bounce (-|
|  SIGI     Pullback50      eq     $95.06   46.0   -1.88   50MA bounce (+|
|  VIAV     Pullback50      eq     $43.68   57.3   -2.08   50MA bounce (+|
|  XPO      Pullback50      eq     $210.47  47.5   -2.13   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|  Skipped                                  no entry slots (max_trades=0)|
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            896|
|  Signals                                                             35|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $466.69|
|  Cash                                                           $209.49|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=20 paper_keys=yes dry_run=False
  alpaca positions=19
  FLAG b0|ORPHAN|d9953782 missing from Alpaca
  FLAG b0|ORPHAN|4798ec8c missing from Alpaca
  FLAG b0|ORPHAN|312dbb34 missing from Alpaca
  FLAG b0|ORPHAN|36b3780d missing from Alpaca
  FLAG b0|ORPHAN|2bf8b0ff missing from Alpaca
  FLAG b0|ORPHAN|bf641e7d missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-13T09:59:49.415971-04:00 ===

[Run context]
Paper auth OK — equity $134601.84, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260813T140115Z

- UTC timestamp: `20260813T140115Z`
- GitHub run: [#6963](https://github.com/28twagg-ops/TradingBot/actions/runs/31707830898)
- Run id: `31707830898`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`98s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 790 | 41.9 | -47.4 | +11.4 | $+7,886 |
| TAINTED | 1710 | 33.1 | -38.8 | +10.1 | $-8,441 |
| KEEP-only | 275 | 64.7 | +37.7 | +42.1 | $+5,447 |
| KEEP-only recent | 88 | 61.4 | +51.2 | +54.0 | $+1,398 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S403, S404, S406
- KILL strategies (15): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-13T10:01:20.245599-04:00","date":"2026-08-13","mode":"entry+manage","header":"entry+manage (26 new)","elapsed_s":89.6,"phases_s":{"reconcile":0.53,"cancel":0.07,"manage":7.13,"protective_stops":0.91,"scan":63.18,"entries":13.81,"reconcile2":1.18},"signals":57,"placed":26,"equity":134161.84,"open_positions":24,"pending_orders":2,"open_lots":37,"submitted_today":26,"filled_today":26,"unattributed_contracts":0,"top_signals":["S210:DKNG","S210:AXP","S210:KMB","S210:GIS","S211:TWLO","S211:DIS","S212:NFLX","S212:DKNG"],"github_run":"6963","github_run_id":"31707830898","status":"ok","data_quality":{"clean":{"n":790,"win":41.9,"med":-47.36,"avg":11.41,"pnl":7886.28},"tainted":{"n":1710,"win":33.1,"med":-38.81,"avg":10.11,"pnl":-8441.34},"keep_only":{"n":275,"win":64.73,"med":37.69,"avg":42.15,"pnl":5447.45},"keep_only_recent":{"n":88,"win":61.36,"med":51.22,"avg":53.96,"pnl":1398.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S405","S407","S408"]}}
```

### Live bot full output

```text
14:01:16  INFO      Mode: exits
14:01:17  INFO        Daily log -> logs/daily/2026-08-13.md
14:01:17  INFO        Daily log reconciled -> logs/daily/2026-08-13.md (0 ledger rows)
14:01:17  INFO        place_all_stops: checking 3 positions...
14:01:17  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
14:01:17  INFO        STOP already live AES @ $14.65
14:01:17  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
14:01:18  INFO        [positions] 3/3 (3 valid)
14:01:18  INFO        Daily log -> logs/daily/2026-08-13.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.60|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.0%  $-0.03                                            HOLD|
|  ACGL  P&L +0.4%  $+0.27                                           HOLD|
|  AFL  P&L +0.8%  $+0.77                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=15 paper_keys=yes dry_run=False
  alpaca positions=19
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-13T10:01:20.245599-04:00 ===

[Run context]
Paper auth OK — equity $134161.84, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 57 signal(s); top: ['S210:DKNG', 'S210:AXP', 'S210:KMB', 'S210:GIS', 'S211:TWLO', 'S211:DIS', 'S212:NFLX', 'S212:DKNG']
Paper lab: $133906 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  [b95 DIS] ENTRY failed: {"buy_limit_price":"0.45","code":40310000,"existing_order_id":"4c875e10-6082-4dbf-b0c0-6184b5dd4bf4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  Skipped: 43 no tradeable call, 42 pending order
Placed 26 new entry order(s).
Protective stops: placed=7 already=14 failed=0

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (entry+manage) --                                     |
|Equity       : $134,161.84                                              |
|Open Risk    : 37 lots (24 broker pos)                                  |
|Today's Run  : 57 signals -> 26 orders submitted                        |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 37 Active Lots | 2 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=790   win= 41.9%  med= -47.4%  $+7,886           |
|  TAINTED            n=1710  win= 33.1%  med= -38.8%  $-8,441           |
|  KEEP-only          n=275   win= 64.7%  med= +37.7%  $+5,447           |
|  KEEP recent        n=88    win= 61.4%  med= +51.2%  $+1,398           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S403...                  |
|  KILL(15): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  79%  +107.1%    14                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.9%    14                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[PENDING ORDERS (2)]                                                    |
+========================================================================+
|  Top groups: S366:MARA(2)                                              |
|  ---------------------------------------------------------             |
|  b432 S366 MARA     limit=0.47                                         |
|  b433 S366 MARA     limit=0.47                                         |
+========================================================================+
+========================================================================+
|[PENDING EXITS (1)]                                                     |
+========================================================================+
|  b238 S401 XOM260814C00170000 x1 stop_loss (-100.0%)                   |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (24)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  PATH260814C00016000          12    -38.8%   $    -38.00               |
|  TTD260911C00014000            1    +42.9%   $    +21.00               |
|  TTD260828C00014000            2    +25.0%   $    +18.00               |
|  DIS260814C00105000            2    -16.7%   $    -14.00               |
|  PATH260821C00015500           7     +4.5%   $    +14.00               |
|  PATH260814C00015500           4    -17.6%   $    -12.00               |
|  MARA260828C00010000           2    -10.0%   $    -10.00               |
|  MARA260814C00009500           2    -12.1%   $     -8.00               |
|  ... 16 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-13.log
elapsed=89.6s reconcile=0.53s cancel=0.07s manage=7.13s scan=63.18s entries=13.81s
STATUS: options_morning_bot run complete (PAPER) elapsed=89.6s. run=#6963 https://github.com/28twagg-ops/TradingBot/actions/runs/31707830898
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.csv
Summary: 1 buckets closed trades, $-339.14 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 12.6% (315/2500) ALERT
# Options signal frequency

_Generated 2026-08-13T10:02:54.982854_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-13
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |    16 | WARN | <<<
| Total open lots             |    37 | INFO |
| Total closed lots           |  1718 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=790 med=-47.4% | TAINTED n=1710 med=-38.8% | KEEP-only n=275 med=+37.7% | KILL=15 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.6 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260813T140547Z

- UTC timestamp: `20260813T140547Z`
- GitHub run: [#6964](https://github.com/28twagg-ops/TradingBot/actions/runs/31708287562)
- Run id: `31708287562`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`90s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 792 | 41.8 | -47.5 | +11.2 | $+7,824 |
| TAINTED | 1710 | 33.1 | -38.8 | +10.1 | $-8,441 |
| KEEP-only | 275 | 64.7 | +37.7 | +42.1 | $+5,447 |
| KEEP-only recent | 88 | 61.4 | +51.2 | +54.0 | $+1,398 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S403, S404, S406
- KILL strategies (15): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-13T10:05:51.561412-04:00","date":"2026-08-13","mode":"entry+manage","header":"entry+manage (12 new)","elapsed_s":79.7,"phases_s":{"reconcile":0.11,"cancel":0.01,"manage":4.01,"protective_stops":0.29,"scan":68.08,"entries":5.94,"reconcile2":0.58},"signals":59,"placed":12,"equity":133916.16,"open_positions":24,"pending_orders":4,"open_lots":45,"submitted_today":38,"filled_today":36,"unattributed_contracts":0,"top_signals":["S210:DKNG","S210:AXP","S210:KMB","S210:GIS","S211:TWLO","S211:DIS","S212:NFLX","S212:DKNG"],"github_run":"6964","github_run_id":"31708287562","status":"ok","data_quality":{"clean":{"n":792,"win":41.79,"med":-47.48,"avg":11.23,"pnl":7824.28},"tainted":{"n":1710,"win":33.1,"med":-38.81,"avg":10.11,"pnl":-8441.34},"keep_only":{"n":275,"win":64.73,"med":37.69,"avg":42.15,"pnl":5447.45},"keep_only_recent":{"n":88,"win":61.36,"med":51.22,"avg":53.96,"pnl":1398.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S405","S407","S408"]}}
```

### Live bot full output

```text
14:05:48  INFO      Mode: exits
14:05:49  INFO        Daily log -> logs/daily/2026-08-13.md
14:05:49  INFO        Daily log reconciled -> logs/daily/2026-08-13.md (0 ledger rows)
14:05:49  INFO        place_all_stops: checking 3 positions...
14:05:49  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
14:05:49  INFO        STOP already live AES @ $14.65
14:05:49  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
14:05:49  INFO        [positions] 3/3 (3 valid)
14:05:49  INFO        Daily log -> logs/daily/2026-08-13.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.49|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.0%  $-0.03                                            HOLD|
|  ACGL  P&L +0.3%  $+0.23                                           HOLD|
|  AFL  P&L +0.8%  $+0.71                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=37 paper_keys=yes dry_run=False
  alpaca positions=26
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-13T10:05:51.561412-04:00 ===

[Run context]
Paper auth OK — equity $133916.16, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
2026-08-13 10:05:53,778 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-51.0%) SELL 12 PATH260814C00016000 @<= 0.01
2026-08-13 10:05:54,679 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-70.6%) SELL 1 LLY260814C01300000 @<= 0.02
Protective stops: placed=0 already=19 failed=2

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 59 signal(s); top: ['S210:DKNG', 'S210:AXP', 'S210:KMB', 'S210:GIS', 'S211:TWLO', 'S211:DIS', 'S212:NFLX', 'S212:DKNG']
Paper lab: $133809 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  [b95 DIS] ENTRY failed: {"buy_limit_price":"0.47","code":40310000,"existing_order_id":"4c875e10-6082-4dbf-b0c0-6184b5dd4bf4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b96 DIS] ENTRY failed: {"buy_limit_price":"0.47","code":40310000,"existing_order_id":"4c875e10-6082-4dbf-b0c0-6184b5dd4bf4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b97 DIS] ENTRY failed: {"buy_limit_price":"0.47","code":40310000,"existing_order_id":"4c875e10-6082-4dbf-b0c0-6184b5dd4bf4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b194 NKE] ENTRY failed: {"buy_limit_price":"0.27","code":40310000,"existing_order_id":"f499c970-18e9-486b-9b14-83f5f5505233","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.11"}
  [b195 NKE] ENTRY failed: {"buy_limit_price":"0.27","code":40310000,"existing_order_id":"f499c970-18e9-486b-9b14-83f5f5505233","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.11"}
  [b346 MARA] ENTRY failed: {"buy_limit_price":"0.11","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b347 MARA] ENTRY failed: {"buy_limit_price":"0.11","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b350 MARA] ENTRY failed: {"buy_limit_price":"0.11","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b351 MARA] ENTRY failed: {"buy_limit_price":"0.11","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b364 MARA] ENTRY failed: {"buy_limit_price":"0.11","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b365 MARA] ENTRY failed: {"buy_limit_price":"0.11","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b392 MARA] ENTRY failed: {"buy_limit_price":"0.31","code":40310000,"existing_order_id":"76cc4855-d840-4df8-b347-fa8491f26d3e","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.16"}
  [b393 MARA] ENTRY failed: {"buy_limit_price":"0.31","code":40310000,"existing_order_id":"76cc4855-d840-4df8-b347-fa8491f26d3e","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.16"}
  [b406 MARA] ENTRY failed: {"buy_limit_price":"0.31","code":40310000,"existing_order_id":"76cc4855-d840-4df8-b347-fa8491f26d3e","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.16"}
  [b407 MARA] ENTRY failed: {"buy_limit_price":"0.31","code":40310000,"existing_order_id":"76cc4855-d840-4df8-b347-fa8491f26d3e","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.16"}
  [b420 MARA] ENTRY failed: {"buy_limit_price":"0.52","code":40310000,"existing_order_id":"8f7aafd0-7b8f-4230-8227-dfd91d09ba6a","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.23"}
  [b421 MARA] ENTRY failed: {"buy_limit_price":"0.52","code":40310000,"existing_order_id":"8f7aafd0-7b8f-4230-8227-dfd91d09ba6a","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.23"}
  [b828 MARA] ENTRY failed: {"buy_limit_price":"0.04","code":40310000,"existing_order_id":"fc3fe151-dc32-4eb1-9b14-1076b3909f17","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.01"}
  [b829 MARA] ENTRY failed: {"buy_limit_price":"0.04","code":40310000,"existing_order_id":"fc3fe151-dc32-4eb1-9b14-1076b3909f17","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.01"}
  [b830 MARA] ENTRY failed: {"buy_limit_price":"0.04","code":40310000,"existing_order_id":"fc3fe151-dc32-4eb1-9b14-1076b3909f17","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.01"}
  [b831 MARA] ENTRY failed: {"buy_limit_price":"0.04","code":40310000,"existing_order_id":"fc3fe151-dc32-4eb1-9b14-1076b3909f17","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.01"}
  [b900 MARA] ENTRY failed: {"buy_limit_price":"0.33","code":40310000,"existing_order_id":"8ce1f2b0-c953-40fc-9ec1-1ec5895b05aa","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.16"}
  [b901 MARA] ENTRY failed: {"buy_limit_price":"0.33","code":40310000,"existing_order_id":"8ce1f2b0-c953-40fc-9ec1-1ec5895b05aa","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.16"}
  Skipped: 95 no tradeable call, 8 already attempted today, 38 pending order
Placed 12 new entry order(s).
Protective stops: placed=2 already=19 failed=0

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (entry+manage) --                                     |
|Equity       : $133,916.16                                              |
|Open Risk    : 45 lots (24 broker pos)                                  |
|Today's Run  : 59 signals -> 12 orders submitted                        |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 45 Active Lots | 4 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=792   win= 41.8%  med= -47.5%  $+7,824           |
|  TAINTED            n=1710  win= 33.1%  med= -38.8%  $-8,441           |
|  KEEP-only          n=275   win= 64.7%  med= +37.7%  $+5,447           |
|  KEEP recent        n=88    win= 61.4%  med= +51.2%  $+1,398           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S403...                  |
|  KILL(15): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  79%  +107.1%    14                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.9%    14                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[PENDING ORDERS (4)]                                                    |
+========================================================================+
|  Top groups: S366:MARA(4)                                              |
|  ---------------------------------------------------------             |
|  b432 S366 MARA     limit=0.47                                         |
|  b433 S366 MARA     limit=0.47                                         |
|  b434 S366 MARA     limit=0.45                                         |
|  b435 S366 MARA     limit=0.45                                         |
+========================================================================+
+========================================================================+
|[PENDING EXITS (1)]                                                     |
+========================================================================+
|  b238 S401 XOM260814C00170000 x1 stop_loss (-100.0%)                   |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (24)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  DKNG260821C00027000           8    -19.4%   $    -48.00               |
|  PATH260821C00015500           7    +11.4%   $    +35.00               |
|  TTD260828C00014000            2    +38.9%   $    +28.00               |
|  TTD260911C00014000            1    +46.9%   $    +23.00               |
|  ARM260814P00245000           -1    +64.0%   $    +16.00               |
|  PATH260814C00015000           4     +7.5%   $    +12.00               |
|  PATH260821C00015000           4     +4.2%   $    +12.00               |
|  MARA260814C00009500           2    -12.1%   $     -8.00               |
|  ... 16 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-13.log
elapsed=79.7s reconcile=0.11s cancel=0.01s manage=4.01s scan=68.08s entries=5.94s
STATUS: options_morning_bot run complete (PAPER) elapsed=79.7s. run=#6964 https://github.com/28twagg-ops/TradingBot/actions/runs/31708287562
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.csv
Summary: 1 buckets closed trades, $-401.14 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 12.7% (317/2502) ALERT
# Options signal frequency

_Generated 2026-08-13T10:07:17.089515_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-13
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |    14 | WARN | <<<
| Total open lots             |    45 | INFO |
| Total closed lots           |  1718 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=792 med=-47.5% | TAINTED n=1710 med=-38.8% | KEEP-only n=275 med=+37.7% | KILL=15 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.49 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260813T141050Z

- UTC timestamp: `20260813T141050Z`
- GitHub run: [#6965](https://github.com/28twagg-ops/TradingBot/actions/runs/31708712941)
- Run id: `31708712941`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`111s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 793 | 41.9 | -47.5 | +11.3 | $+7,906 |
| TAINTED | 1720 | 33.0 | -38.9 | +10.4 | $-8,942 |
| KEEP-only | 275 | 64.7 | +37.7 | +42.1 | $+5,447 |
| KEEP-only recent | 88 | 61.4 | +51.2 | +54.0 | $+1,398 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S403, S404, S406
- KILL strategies (15): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-13T10:10:55.383483-04:00","date":"2026-08-13","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":101.8,"phases_s":{"reconcile":0.56,"cancel":0.08,"manage":11.42,"protective_stops":1.92,"scan":68.89,"entries":14.4,"reconcile2":1.69},"signals":53,"placed":4,"equity":134009.36,"open_positions":26,"pending_orders":0,"open_lots":51,"submitted_today":42,"filled_today":44,"unattributed_contracts":0,"top_signals":["S210:DKNG","S210:AXP","S210:KMB","S210:GIS","S211:TWLO","S211:DIS","S212:NFLX","S212:DKNG"],"github_run":"6965","github_run_id":"31708712941","status":"ok","data_quality":{"clean":{"n":793,"win":41.87,"med":-47.45,"avg":11.3,"pnl":7905.53},"tainted":{"n":1720,"win":33.02,"med":-38.91,"avg":10.36,"pnl":-8942.34},"keep_only":{"n":275,"win":64.73,"med":37.69,"avg":42.15,"pnl":5447.45},"keep_only_recent":{"n":88,"win":61.36,"med":51.22,"avg":53.96,"pnl":1398.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S405","S407","S408"]}}
```

### Live bot full output

```text
14:10:51  INFO      Mode: exits
14:10:52  INFO        Daily log -> logs/daily/2026-08-13.md
14:10:52  INFO        Daily log reconciled -> logs/daily/2026-08-13.md (0 ledger rows)
14:10:52  INFO        place_all_stops: checking 3 positions...
14:10:52  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
14:10:52  INFO        STOP already live AES @ $14.65
14:10:52  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
14:10:53  INFO        [positions] 3/3 (3 valid)
14:10:53  INFO        Daily log -> logs/daily/2026-08-13.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.50|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.0%  $-0.03                                            HOLD|
|  ACGL  P&L +0.4%  $+0.28                                           HOLD|
|  AFL  P&L +0.7%  $+0.67                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           3|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                3|
|  Logged exits                                                         0|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  None                                                                  |
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=45 paper_keys=yes dry_run=False
  alpaca positions=27
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-13T10:10:55.383483-04:00 ===

[Run context]
Paper auth OK — equity $134011.36, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
2026-08-13 10:11:01,110 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+59.2%) SELL 5 CELH260814C00028000 @<= 0.42
Protective stops: placed=0 already=21 failed=1

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 53 signal(s); top: ['S210:DKNG', 'S210:AXP', 'S210:KMB', 'S210:GIS', 'S211:TWLO', 'S211:DIS', 'S212:NFLX', 'S212:DKNG']
Paper lab: $134199 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  [b96 DIS] ENTRY failed: {"buy_limit_price":"0.47","code":40310000,"existing_order_id":"4c875e10-6082-4dbf-b0c0-6184b5dd4bf4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b97 DIS] ENTRY failed: {"buy_limit_price":"0.47","code":40310000,"existing_order_id":"4c875e10-6082-4dbf-b0c0-6184b5dd4bf4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b166 MARA] ENTRY failed: {"buy_limit_price":"0.06","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b167 MARA] ENTRY failed: {"buy_limit_price":"0.06","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b194 NKE] ENTRY failed: {"buy_limit_price":"0.27","code":40310000,"existing_order_id":"f499c970-18e9-486b-9b14-83f5f5505233","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.11"}
  [b195 NKE] ENTRY failed: {"buy_limit_price":"0.27","code":40310000,"existing_order_id":"f499c970-18e9-486b-9b14-83f5f5505233","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.11"}
  [b236 MARA] ENTRY failed: {"buy_limit_price":"0.06","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b237 MARA] ENTRY failed: {"buy_limit_price":"0.06","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b346 MARA] ENTRY failed: {"buy_limit_price":"0.1","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b347 MARA] ENTRY failed: {"buy_limit_price":"0.1","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b350 MARA] ENTRY failed: {"buy_limit_price":"0.1","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b351 MARA] ENTRY failed: {"buy_limit_price":"0.1","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b364 MARA] ENTRY failed: {"buy_limit_price":"0.1","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b365 MARA] ENTRY failed: {"buy_limit_price":"0.1","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b392 MARA] ENTRY failed: {"buy_limit_price":"0.34","code":40310000,"existing_order_id":"76cc4855-d840-4df8-b347-fa8491f26d3e","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.16"}
  [b393 MARA] ENTRY failed: {"buy_limit_price":"0.34","code":40310000,"existing_order_id":"76cc4855-d840-4df8-b347-fa8491f26d3e","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.16"}
  [b406 MARA] ENTRY failed: {"buy_limit_price":"0.34","code":40310000,"existing_order_id":"76cc4855-d840-4df8-b347-fa8491f26d3e","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.16"}
  [b407 MARA] ENTRY failed: {"buy_limit_price":"0.34","code":40310000,"existing_order_id":"76cc4855-d840-4df8-b347-fa8491f26d3e","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.16"}
  [b420 MARA] ENTRY failed: {"buy_limit_price":"0.49","code":40310000,"existing_order_id":"8f7aafd0-7b8f-4230-8227-dfd91d09ba6a","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.23"}
  [b421 MARA] ENTRY failed: {"buy_limit_price":"0.49","code":40310000,"existing_order_id":"8f7aafd0-7b8f-4230-8227-dfd91d09ba6a","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.23"}
  [b900 MARA] ENTRY failed: {"buy_limit_price":"0.29","code":40310000,"existing_order_id":"8ce1f2b0-c953-40fc-9ec1-1ec5895b05aa","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.16"}
  [b901 MARA] ENTRY failed: {"buy_limit_price":"0.29","code":40310000,"existing_order_id":"8ce1f2b0-c953-40fc-9ec1-1ec5895b05aa","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.16"}
  [b914 MARA] ENTRY failed: {"buy_limit_price":"0.06","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  [b915 MARA] ENTRY failed: {"buy_limit_price":"0.06","code":40310000,"existing_order_id":"47cedf98-e2ba-412b-a1c0-f860ae6929ae","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.05"}
  Skipped: 46 no tradeable call, 8 pending order
Placed 4 new entry order(s).
Protective stops: placed=3 already=20 failed=0

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (entry+manage) --                                     |
|Equity       : $134,009.36                                              |
|Open Risk    : 51 lots (26 broker pos)                                  |
|Today's Run  : 53 signals -> 4 orders submitted                         |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 51 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=793   win= 41.9%  med= -47.5%  $+7,906           |
|  TAINTED            n=1720  win= 33.0%  med= -38.9%  $-8,942           |
|  KEEP-only          n=275   win= 64.7%  med= +37.7%  $+5,447           |
|  KEEP recent        n=88    win= 61.4%  med= +51.2%  $+1,398           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S403...                  |
|  KILL(15): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  79%  +107.1%    14                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.9%    14                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[PENDING EXITS (1)]                                                     |
+========================================================================+
|  b238 S401 XOM260814C00170000 x1 stop_loss (-100.0%)                   |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (26)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  DKNG260821C00027000           8    -16.1%   $    -40.00               |
|  PATH260821C00015500           7    +11.4%   $    +35.00               |
|  TTD260828C00014000            2    +38.9%   $    +28.00               |
|  TTD260911C00014000            1    +46.9%   $    +23.00               |
|  ARM260814P00245000           -1    +64.0%   $    +16.00               |
|  MARA260814C00009500           2    -24.2%   $    -16.00               |
|  MARA260821C00010000           4    -11.8%   $    -16.00               |
|  PATH260814C00015000           4    +10.0%   $    +16.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-13.log
elapsed=101.8s reconcile=0.56s cancel=0.08s manage=11.42s scan=68.89s entries=14.4s
STATUS: options_morning_bot run complete (PAPER) elapsed=101.8s. run=#6965 https://github.com/28twagg-ops/TradingBot/actions/runs/31708712941
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_buckets.csv
Summary: 1 buckets closed trades, $-319.89 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_strategy_selection.csv
Summary: keep=0 watch=81 drop=24
Orphan rate: 13.0% (326/2513) ALERT
# Options signal frequency

_Generated 2026-08-13T10:12:42.952240_

Headline counts are **unique (strategy, underlying, date)** from `ENTRY` lines in `logs/options_trial/runs/*.log`.
Raw log-line counts (multi-bucket duplicates) are shown below for debug.

### Unique underlying symbols per day (headline)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-08 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    1 |     6 |
| 2026-07-09 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    3 |     6 |
| 2026-07-10 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    1 |     3 |
| 2026-07-13 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    2 |     7 |
| 2026-07-14 |    0 |    0 |    3 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     5 |
| 2026-07-16 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    3 |    0 |     5 |
| 2026-07-17 |    0 |    0 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    2 |    0 |     4 |
| 2026-07-20 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |     1 |
| 2026-07-21 |    1 |    2 |    1 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     9 |
| 2026-07-22 |    1 |    1 |    1 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     4 |
| 2026-07-24 |    1 |    1 |    1 |    0 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-27 |    1 |    0 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     5 |
| 2026-07-28 |    1 |    1 |    1 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |
| 2026-07-29 |    1 |    2 |    1 |    1 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |     6 |

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 6 | 6 | 1.0 | ~38 active signal-days |
| S164 | 7 | 5 | 1.4 | ~27 active signal-days |
| S165 | 20 | 13 | 1.5 | ~25 active signal-days |
| S166 | 4 | 4 | 1.0 | ~38 active signal-days |
| S167 | 7 | 6 | 1.2 | ~33 active signal-days |
| S168 | 5 | 4 | 1.2 | ~30 active signal-days |
| S169 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S170 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S171 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S172 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S175 | 0 | 0 | 0.0 | inf (no unique entries yet) |
| S173 | 17 | 9 | 1.9 | ~20 active signal-days |
| S174 | 7 | 4 | 1.8 | ~22 active signal-days |

\* Formula: `ceil(30 / (avg_unique_per_active_day * 80%))`. Update when real exit rates are known.

## Signal frequency by window (all time, unique strategy×symbol×date×window)

| Window | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|--------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| w1     |    2 |    1 |    6 |    1 |    2 |    1 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    21 |
| w2     |    5 |    4 |   10 |    4 |    5 |    4 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    41 |
| w3     |    5 |    4 |   11 |    3 |    5 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    42 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 205 | 6 |
| S164 | 229 | 7 |
| S165 | 1675 | 20 |
| S166 | 105 | 4 |
| S167 | 229 | 7 |
| S168 | 150 | 5 |
| S169 | 0 | 0 |
| S170 | 0 | 0 |
| S171 | 0 | 0 |
| S172 | 0 | 0 |
| S175 | 0 | 0 |
| S173 | 1911 | 17 |
| S174 | 891 | 7 |

### Raw log lines per day (debug / multi-bucket)

| Date       | S163 | S164 | S165 | S166 | S167 | S168 | S169 | S170 | S171 | S172 | S175 | S173 | S174 | Total |
|------------|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|-----:|------:|
| 2026-07-07 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |    0 |   100 |
| 2026-07-08 |    0 |    0 |  100 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |  100 |   300 |
| 2026-07-09 |    0 |    0 |   24 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  100 |   15 |   139 |
| 2026-07-10 |    0 |    0 |  242 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  230 |  202 |   674 |
| 2026-07-13 |    0 |    0 |  190 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  212 |  188 |   590 |
| 2026-07-14 |    0 |    0 |  194 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  185 |  106 |   485 |
| 2026-07-15 |    0 |    0 |  146 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  154 |   58 |   358 |
| 2026-07-16 |    0 |    0 |  179 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  205 |   58 |   442 |
| 2026-07-17 |    0 |    0 |  127 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  207 |   58 |   392 |
| 2026-07-20 |    0 |    0 |  107 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |  143 |   58 |   308 |
| 2026-07-21 |   30 |   35 |  113 |   30 |   35 |   35 |    0 |    0 |    0 |    0 |    0 |  118 |   48 |   444 |
| 2026-07-22 |   40 |   47 |   86 |   15 |   45 |   20 |    0 |    0 |    0 |    0 |    0 |   77 |    0 |   330 |
| 2026-07-23 |   30 |   42 |   50 |   15 |   40 |   20 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   237 |
| 2026-07-24 |   75 |   87 |   85 |   15 |   77 |   55 |    0 |    0 |    0 |    0 |    0 |   40 |    0 |   434 |
| 2026-07-27 |   14 |    0 |   14 |   14 |   14 |   14 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    70 |
| 2026-07-28 |    6 |    8 |    8 |    8 |    8 |    6 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    44 |
| 2026-07-29 |   10 |   10 |   10 |    8 |   10 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    48 |

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-08-13
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |    13 | WARN | <<<
| Total open lots             |    51 | INFO |
| Total closed lots           |  1720 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-13_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=793 med=-47.5% | TAINTED n=1720 med=-38.9% | KEEP-only n=275 med=+37.7% | KILL=15 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.5 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
