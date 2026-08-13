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
