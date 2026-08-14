# Daily Comprehensive Action Review — 2026-08-14

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260814T130055Z

- UTC timestamp: `20260814T130055Z`
- GitHub run: [#7083](https://github.com/28twagg-ops/TradingBot/actions/runs/31802734831)
- Run id: `31802734831`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`11s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 817 | 41.9 | -47.5 | +15.6 | $+8,217 |
| TAINTED | 1728 | 33.1 | -38.8 | +11.7 | $-8,922 |
| KEEP-only | 292 | 63.7 | +37.6 | +43.5 | $+5,715 |
| KEEP-only recent | 104 | 59.6 | +50.0 | +56.6 | $+1,689 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T09:00:58.956870-04:00","date":"2026-08-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.17},"signals":0,"placed":0,"equity":132455.8,"open_positions":13,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"7083","github_run_id":"31802734831","status":"ok","data_quality":{"clean":{"n":817,"win":41.86,"med":-47.45,"avg":15.61,"pnl":8216.53},"tainted":{"n":1728,"win":33.1,"med":-38.81,"avg":11.71,"pnl":-8922.34},"keep_only":{"n":292,"win":63.7,"med":37.59,"avg":43.47,"pnl":5715.45},"keep_only_recent":{"n":104,"win":59.62,"med":50.0,"avg":56.62,"pnl":1689.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:00:56  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.36|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $467.36|
|  Cash                                                           $209.57|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $257.79|
|  Open P&L                                                        $+1.70|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $69.97     $97.48   $98.92   +1.5%   $+1.02  |
|  AES      Pullback50      $94.22     $14.72   $14.74   +0.1%   $+0.13  |
|  AFL      Pullback50      $93.60     $120.39  $121.10  +0.6%   $+0.55  |
|                                                                        |
|  Total invested                                                 $257.79|
|  Total open P&L                                                  $+1.70|
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
  open_lots=18 paper_keys=yes dry_run=False
  alpaca positions=15
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T09:00:58.956870-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $132455.80, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (after_hours) --                                      |
|Equity       : $132,455.80                                              |
|Open Risk    : 18 lots (13 broker pos)                                  |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 18 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=817   win= 41.9%  med= -47.5%  $+8,217           |
|  TAINTED            n=1728  win= 33.1%  med= -38.8%  $-8,922           |
|  KEEP-only          n=292   win= 63.7%  med= +37.6%  $+5,715           |
|  KEEP recent        n=104   win= 59.6%  med= +50.0%  $+1,689           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (13)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  MARA260904C00010500           4    -37.0%   $    -68.00               |
|  DKNG260821C00026500           3    -39.0%   $    -48.00               |
|  DKNG260821C00027000           3    -51.6%   $    -48.00               |
|  MARA260828C00010000           2    -38.0%   $    -38.00               |
|  MARA260911C00010500           2    -33.9%   $    -38.00               |
|  DIS260814C00104000            1    +58.5%   $    +31.00               |
|  MARA260814P00009500          -1   -300.0%   $    -28.50               |
|  ARM260814P00245000           -1    +96.0%   $    +24.00               |
|  ... 5 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=0.7s reconcile=0.17s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.7s. run=#7083 https://github.com/28twagg-ops/TradingBot/actions/runs/31802734831
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=81 drop=24
Orphan rate: 13.2% (336/2545) ALERT
# Options signal frequency

_Generated 2026-08-14T09:01:05.399393_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  1742 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=817 med=-47.5% | TAINTED n=1728 med=-38.8% | KEEP-only n=292 med=+37.6% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.36 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T130549Z

- UTC timestamp: `20260814T130549Z`
- GitHub run: [#7084](https://github.com/28twagg-ops/TradingBot/actions/runs/31803111270)
- Run id: `31803111270`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`11s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 817 | 41.9 | -47.5 | +15.6 | $+8,217 |
| TAINTED | 1728 | 33.1 | -38.8 | +11.7 | $-8,922 |
| KEEP-only | 292 | 63.7 | +37.6 | +43.5 | $+5,715 |
| KEEP-only recent | 104 | 59.6 | +50.0 | +56.6 | $+1,689 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T09:05:52.577630-04:00","date":"2026-08-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.43},"signals":0,"placed":0,"equity":132504.28,"open_positions":13,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"7084","github_run_id":"31803111270","status":"ok","data_quality":{"clean":{"n":817,"win":41.86,"med":-47.45,"avg":15.61,"pnl":8216.53},"tainted":{"n":1728,"win":33.1,"med":-38.81,"avg":11.71,"pnl":-8922.34},"keep_only":{"n":292,"win":63.7,"med":37.59,"avg":43.47,"pnl":5715.45},"keep_only_recent":{"n":104,"win":59.62,"med":50.0,"avg":56.62,"pnl":1689.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:05:50  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.36|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $467.36|
|  Cash                                                           $209.57|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $257.79|
|  Open P&L                                                        $+1.70|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $69.97     $97.48   $98.92   +1.5%   $+1.02  |
|  AES      Pullback50      $94.22     $14.72   $14.74   +0.1%   $+0.13  |
|  AFL      Pullback50      $93.60     $120.39  $121.10  +0.6%   $+0.55  |
|                                                                        |
|  Total invested                                                 $257.79|
|  Total open P&L                                                  $+1.70|
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
  open_lots=18 paper_keys=yes dry_run=False
  alpaca positions=15
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T09:05:52.577630-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $132504.28, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (after_hours) --                                      |
|Equity       : $132,504.28                                              |
|Open Risk    : 18 lots (13 broker pos)                                  |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 18 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=817   win= 41.9%  med= -47.5%  $+8,217           |
|  TAINTED            n=1728  win= 33.1%  med= -38.8%  $-8,922           |
|  KEEP-only          n=292   win= 63.7%  med= +37.6%  $+5,715           |
|  KEEP recent        n=104   win= 59.6%  med= +50.0%  $+1,689           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (13)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  MARA260904C00010500           4    -37.0%   $    -68.00               |
|  DKNG260821C00026500           3    -39.0%   $    -48.00               |
|  DKNG260821C00027000           3    -51.6%   $    -48.00               |
|  MARA260828C00010000           2    -38.0%   $    -38.00               |
|  MARA260911C00010500           2    -33.9%   $    -38.00               |
|  DIS260814C00104000            1    +58.5%   $    +31.00               |
|  MARA260814P00009500          -1   -300.0%   $    -28.50               |
|  ARM260814P00245000           -1    +96.0%   $    +24.00               |
|  ... 5 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=1.1s reconcile=0.43s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.1s. run=#7084 https://github.com/28twagg-ops/TradingBot/actions/runs/31803111270
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=81 drop=24
Orphan rate: 13.2% (336/2545) ALERT
# Options signal frequency

_Generated 2026-08-14T09:05:59.422177_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  1742 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=817 med=-47.5% | TAINTED n=1728 med=-38.8% | KEEP-only n=292 med=+37.6% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.36 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T131051Z

- UTC timestamp: `20260814T131051Z`
- GitHub run: [#7085](https://github.com/28twagg-ops/TradingBot/actions/runs/31803483572)
- Run id: `31803483572`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`11s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 817 | 41.9 | -47.5 | +15.6 | $+8,217 |
| TAINTED | 1728 | 33.1 | -38.8 | +11.7 | $-8,922 |
| KEEP-only | 292 | 63.7 | +37.6 | +43.5 | $+5,715 |
| KEEP-only recent | 104 | 59.6 | +50.0 | +56.6 | $+1,689 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T09:10:56.721841-04:00","date":"2026-08-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.4,"phases_s":{"reconcile":0.63},"signals":0,"placed":0,"equity":132235.8,"open_positions":13,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"7085","github_run_id":"31803483572","status":"ok","data_quality":{"clean":{"n":817,"win":41.86,"med":-47.45,"avg":15.61,"pnl":8216.53},"tainted":{"n":1728,"win":33.1,"med":-38.81,"avg":11.71,"pnl":-8922.34},"keep_only":{"n":292,"win":63.7,"med":37.59,"avg":43.47,"pnl":5715.45},"keep_only_recent":{"n":104,"win":59.62,"med":50.0,"avg":56.62,"pnl":1689.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:10:52  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.45|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $469.45|
|  Cash                                                           $209.57|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.88|
|  Open P&L                                                        $+3.79|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $69.53     $97.48   $98.30   +0.8%   $+0.58  |
|  AES      Pullback50      $94.22     $14.72   $14.74   +0.1%   $+0.13  |
|  AFL      Pullback50      $96.14     $120.39  $124.38  +3.3%   $+3.09  |
|                                                                        |
|  Total invested                                                 $259.88|
|  Total open P&L                                                  $+3.79|
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
  open_lots=18 paper_keys=yes dry_run=False
  alpaca positions=15
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T09:10:56.721841-04:00 ===

[Run context]
After hours (09:10 ET) — exit summary only.
Paper auth OK — equity $132235.80, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (after_hours) --                                      |
|Equity       : $132,235.80                                              |
|Open Risk    : 18 lots (13 broker pos)                                  |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 18 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=817   win= 41.9%  med= -47.5%  $+8,217           |
|  TAINTED            n=1728  win= 33.1%  med= -38.8%  $-8,922           |
|  KEEP-only          n=292   win= 63.7%  med= +37.6%  $+5,715           |
|  KEEP recent        n=104   win= 59.6%  med= +50.0%  $+1,689           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (13)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  MARA260904C00010500           4    -37.0%   $    -68.00               |
|  DKNG260821C00026500           3    -39.0%   $    -48.00               |
|  DKNG260821C00027000           3    -51.6%   $    -48.00               |
|  MARA260828C00010000           2    -38.0%   $    -38.00               |
|  MARA260911C00010500           2    -33.9%   $    -38.00               |
|  DIS260814C00104000            1    +58.5%   $    +31.00               |
|  MARA260814P00009500          -1   -300.0%   $    -28.50               |
|  ARM260814P00245000           -1    +96.0%   $    +24.00               |
|  ... 5 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=1.4s reconcile=0.63s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.4s. run=#7085 https://github.com/28twagg-ops/TradingBot/actions/runs/31803483572
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=81 drop=24
Orphan rate: 13.2% (336/2545) ALERT
# Options signal frequency

_Generated 2026-08-14T09:11:03.880032_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  1742 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=817 med=-47.5% | TAINTED n=1728 med=-38.8% | KEEP-only n=292 med=+37.6% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=469.45 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T131553Z

- UTC timestamp: `20260814T131553Z`
- GitHub run: [#7086](https://github.com/28twagg-ops/TradingBot/actions/runs/31803858506)
- Run id: `31803858506`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`11s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 817 | 41.9 | -47.5 | +15.6 | $+8,217 |
| TAINTED | 1728 | 33.1 | -38.8 | +11.7 | $-8,922 |
| KEEP-only | 292 | 63.7 | +37.6 | +43.5 | $+5,715 |
| KEEP-only recent | 104 | 59.6 | +50.0 | +56.6 | $+1,689 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T09:15:57.125357-04:00","date":"2026-08-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":132184.08,"open_positions":13,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"7086","github_run_id":"31803858506","status":"ok","data_quality":{"clean":{"n":817,"win":41.86,"med":-47.45,"avg":15.61,"pnl":8216.53},"tainted":{"n":1728,"win":33.1,"med":-38.81,"avg":11.71,"pnl":-8922.34},"keep_only":{"n":292,"win":63.7,"med":37.59,"avg":43.47,"pnl":5715.45},"keep_only_recent":{"n":104,"win":59.62,"med":50.0,"avg":56.62,"pnl":1689.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:15:54  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.45|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $469.45|
|  Cash                                                           $209.57|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.88|
|  Open P&L                                                        $+3.79|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $69.53     $97.48   $98.30   +0.8%   $+0.58  |
|  AES      Pullback50      $94.22     $14.72   $14.74   +0.1%   $+0.13  |
|  AFL      Pullback50      $96.14     $120.39  $124.38  +3.3%   $+3.09  |
|                                                                        |
|  Total invested                                                 $259.88|
|  Total open P&L                                                  $+3.79|
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
  open_lots=18 paper_keys=yes dry_run=False
  alpaca positions=15
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T09:15:57.125357-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $132184.08, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (after_hours) --                                      |
|Equity       : $132,184.08                                              |
|Open Risk    : 18 lots (13 broker pos)                                  |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 18 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=817   win= 41.9%  med= -47.5%  $+8,217           |
|  TAINTED            n=1728  win= 33.1%  med= -38.8%  $-8,922           |
|  KEEP-only          n=292   win= 63.7%  med= +37.6%  $+5,715           |
|  KEEP recent        n=104   win= 59.6%  med= +50.0%  $+1,689           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (13)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  MARA260904C00010500           4    -37.0%   $    -68.00               |
|  DKNG260821C00026500           3    -39.0%   $    -48.00               |
|  DKNG260821C00027000           3    -51.6%   $    -48.00               |
|  MARA260828C00010000           2    -38.0%   $    -38.00               |
|  MARA260911C00010500           2    -33.9%   $    -38.00               |
|  DIS260814C00104000            1    +58.5%   $    +31.00               |
|  MARA260814P00009500          -1   -300.0%   $    -28.50               |
|  ARM260814P00245000           -1    +96.0%   $    +24.00               |
|  ... 5 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=1.0s reconcile=0.19s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.0s. run=#7086 https://github.com/28twagg-ops/TradingBot/actions/runs/31803858506
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=81 drop=24
Orphan rate: 13.2% (336/2545) ALERT
# Options signal frequency

_Generated 2026-08-14T09:16:03.950884_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  1742 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=817 med=-47.5% | TAINTED n=1728 med=-38.8% | KEEP-only n=292 med=+37.6% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=469.45 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T132049Z

- UTC timestamp: `20260814T132049Z`
- GitHub run: [#7087](https://github.com/28twagg-ops/TradingBot/actions/runs/31804232153)
- Run id: `31804232153`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`10s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 817 | 41.9 | -47.5 | +15.6 | $+8,217 |
| TAINTED | 1728 | 33.1 | -38.8 | +11.7 | $-8,922 |
| KEEP-only | 292 | 63.7 | +37.6 | +43.5 | $+5,715 |
| KEEP-only recent | 104 | 59.6 | +50.0 | +56.6 | $+1,689 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T09:20:52.312138-04:00","date":"2026-08-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.26},"signals":0,"placed":0,"equity":131191.8,"open_positions":13,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"7087","github_run_id":"31804232153","status":"ok","data_quality":{"clean":{"n":817,"win":41.86,"med":-47.45,"avg":15.61,"pnl":8216.53},"tainted":{"n":1728,"win":33.1,"med":-38.81,"avg":11.71,"pnl":-8922.34},"keep_only":{"n":292,"win":63.7,"med":37.59,"avg":43.47,"pnl":5715.45},"keep_only_recent":{"n":104,"win":59.62,"med":50.0,"avg":56.62,"pnl":1689.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:20:50  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.45|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $469.45|
|  Cash                                                           $209.57|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.88|
|  Open P&L                                                        $+3.79|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $69.53     $97.48   $98.30   +0.8%   $+0.58  |
|  AES      Pullback50      $94.22     $14.72   $14.74   +0.1%   $+0.13  |
|  AFL      Pullback50      $96.14     $120.39  $124.38  +3.3%   $+3.09  |
|                                                                        |
|  Total invested                                                 $259.88|
|  Total open P&L                                                  $+3.79|
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
  open_lots=18 paper_keys=yes dry_run=False
  alpaca positions=15
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T09:20:52.312138-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $131191.80, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (after_hours) --                                      |
|Equity       : $131,191.80                                              |
|Open Risk    : 18 lots (13 broker pos)                                  |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 18 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=817   win= 41.9%  med= -47.5%  $+8,217           |
|  TAINTED            n=1728  win= 33.1%  med= -38.8%  $-8,922           |
|  KEEP-only          n=292   win= 63.7%  med= +37.6%  $+5,715           |
|  KEEP recent        n=104   win= 59.6%  med= +50.0%  $+1,689           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (13)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  MARA260904C00010500           4    -37.0%   $    -68.00               |
|  DKNG260821C00026500           3    -39.0%   $    -48.00               |
|  DKNG260821C00027000           3    -51.6%   $    -48.00               |
|  MARA260828C00010000           2    -38.0%   $    -38.00               |
|  MARA260911C00010500           2    -33.9%   $    -38.00               |
|  DIS260814C00104000            1    +58.5%   $    +31.00               |
|  MARA260814P00009500          -1   -300.0%   $    -28.50               |
|  ARM260814P00245000           -1    +96.0%   $    +24.00               |
|  ... 5 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=0.8s reconcile=0.26s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.8s. run=#7087 https://github.com/28twagg-ops/TradingBot/actions/runs/31804232153
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=81 drop=24
Orphan rate: 13.2% (336/2545) ALERT
# Options signal frequency

_Generated 2026-08-14T09:20:58.843465_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  1742 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=817 med=-47.5% | TAINTED n=1728 med=-38.8% | KEEP-only n=292 med=+37.6% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=469.45 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T132550Z

- UTC timestamp: `20260814T132550Z`
- GitHub run: [#7088](https://github.com/28twagg-ops/TradingBot/actions/runs/31804608859)
- Run id: `31804608859`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`10s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 817 | 41.9 | -47.5 | +15.6 | $+8,217 |
| TAINTED | 1728 | 33.1 | -38.8 | +11.7 | $-8,922 |
| KEEP-only | 292 | 63.7 | +37.6 | +43.5 | $+5,715 |
| KEEP-only recent | 104 | 59.6 | +50.0 | +56.6 | $+1,689 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T09:25:53.627882-04:00","date":"2026-08-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":130503.8,"open_positions":13,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"7088","github_run_id":"31804608859","status":"ok","data_quality":{"clean":{"n":817,"win":41.86,"med":-47.45,"avg":15.61,"pnl":8216.53},"tainted":{"n":1728,"win":33.1,"med":-38.81,"avg":11.71,"pnl":-8922.34},"keep_only":{"n":292,"win":63.7,"med":37.59,"avg":43.47,"pnl":5715.45},"keep_only_recent":{"n":104,"win":59.62,"med":50.0,"avg":56.62,"pnl":1689.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:25:51  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $469.45|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $469.45|
|  Cash                                                           $209.57|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $259.88|
|  Open P&L                                                        $+3.79|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (3 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $69.53     $97.48   $98.30   +0.8%   $+0.58  |
|  AES      Pullback50      $94.22     $14.72   $14.74   +0.1%   $+0.13  |
|  AFL      Pullback50      $96.14     $120.39  $124.38  +3.3%   $+3.09  |
|                                                                        |
|  Total invested                                                 $259.88|
|  Total open P&L                                                  $+3.79|
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
  open_lots=18 paper_keys=yes dry_run=False
  alpaca positions=15
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T09:25:53.627882-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $130503.80, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (after_hours) --                                      |
|Equity       : $130,503.80                                              |
|Open Risk    : 18 lots (13 broker pos)                                  |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 18 Active Lots | 0 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=817   win= 41.9%  med= -47.5%  $+8,217           |
|  TAINTED            n=1728  win= 33.1%  med= -38.8%  $-8,922           |
|  KEEP-only          n=292   win= 63.7%  med= +37.6%  $+5,715           |
|  KEEP recent        n=104   win= 59.6%  med= +50.0%  $+1,689           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
|  b112 lab0112_s212_w3_1045..   0%  -68.1%    11                        |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (13)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  MARA260904C00010500           4    -37.0%   $    -68.00               |
|  DKNG260821C00026500           3    -39.0%   $    -48.00               |
|  DKNG260821C00027000           3    -51.6%   $    -48.00               |
|  MARA260828C00010000           2    -38.0%   $    -38.00               |
|  MARA260911C00010500           2    -33.9%   $    -38.00               |
|  DIS260814C00104000            1    +58.5%   $    +31.00               |
|  MARA260814P00009500          -1   -300.0%   $    -28.50               |
|  ARM260814P00245000           -1    +96.0%   $    +24.00               |
|  ... 5 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=0.6s reconcile=0.11s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.6s. run=#7088 https://github.com/28twagg-ops/TradingBot/actions/runs/31804608859
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=81 drop=24
Orphan rate: 13.2% (336/2545) ALERT
# Options signal frequency

_Generated 2026-08-14T09:26:00.024761_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     4 | WARN | <<<
| Total open lots             |    18 | INFO |
| Total closed lots           |  1742 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=817 med=-47.5% | TAINTED n=1728 med=-38.8% | KEEP-only n=292 med=+37.6% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=469.45 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T133053Z

- UTC timestamp: `20260814T133053Z`
- GitHub run: [#7089](https://github.com/28twagg-ops/TradingBot/actions/runs/31804991289)
- Run id: `31804991289`
- Live bot: exit=`0`, duration=`217s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 817 | 41.9 | -47.5 | +15.6 | $+8,217 |
| TAINTED | 1728 | 33.1 | -38.8 | +11.7 | $-8,922 |
| KEEP-only | 292 | 63.7 | +37.6 | +43.5 | $+5,715 |
| KEEP-only recent | 104 | 59.6 | +50.0 | +56.6 | $+1,689 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T09:25:53.627882-04:00","date":"2026-08-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":130503.8,"open_positions":13,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"7088","github_run_id":"31804608859","status":"ok","data_quality":{"clean":{"n":817,"win":41.86,"med":-47.45,"avg":15.61,"pnl":8216.53},"tainted":{"n":1728,"win":33.1,"med":-38.81,"avg":11.71,"pnl":-8922.34},"keep_only":{"n":292,"win":63.7,"med":37.59,"avg":43.47,"pnl":5715.45},"keep_only_recent":{"n":104,"win":59.62,"med":50.0,"avg":56.62,"pnl":1689.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:30:54  INFO      Mode: morning_prep
13:30:55  INFO        [prep_positions] 3/3 (3 valid)
13:30:55  INFO      Fetching tickers (universe=both)...
13:30:55  INFO        S&P 500: 503
13:30:55  INFO        MidCap 400: 400
13:30:55  INFO        Total: 903 tickers
13:30:58  INFO        [prep_universe] 40/900 (40 valid)
13:31:00  INFO        [prep_universe] 80/900 (80 valid)
13:31:02  INFO        [prep_universe] 120/900 (120 valid)
13:31:04  INFO        [prep_universe] 160/900 (160 valid)
13:31:07  INFO        [prep_universe] 200/900 (199 valid)
13:31:09  INFO        [prep_universe] 240/900 (238 valid)
13:31:21  INFO        [prep_universe] 280/900 (278 valid)
13:31:35  INFO        [prep_universe] 320/900 (318 valid)
13:31:46  INFO        [prep_universe] 360/900 (358 valid)
13:31:57  INFO        [prep_universe] 400/900 (397 valid)
13:32:10  INFO        [prep_universe] 440/900 (437 valid)
13:32:22  INFO        [prep_universe] 480/900 (477 valid)
13:32:33  INFO        [prep_universe] 520/900 (517 valid)
13:32:46  INFO        [prep_universe] 560/900 (557 valid)
13:32:57  INFO        [prep_universe] 600/900 (597 valid)
13:33:11  INFO        [prep_universe] 640/900 (637 valid)
13:33:22  INFO        [prep_universe] 680/900 (677 valid)
13:33:33  INFO        [prep_universe] 720/900 (717 valid)
13:33:46  INFO        [prep_universe] 760/900 (757 valid)
13:33:57  INFO        [prep_universe] 800/900 (797 valid)
13:34:10  INFO        [prep_universe] 840/900 (836 valid)
13:34:21  INFO        [prep_universe] 880/900 (876 valid)
13:34:28  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.55|
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
|  Invested                                                       $256.98|
|  Open P&L                                                        $+0.89|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $69.21     $97.48   $97.85   +0.4%   $+0.26  |
|  AES      Pullback50      $94.20     $14.72   $14.74   +0.1%   $+0.11  |
|  AFL      Pullback50      $93.58     $120.39  $121.07  +0.6%   $+0.53  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  AES       OrderType.STOP    6         None        14.67               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      1|
|  Signal candidates                                                   33|
|  Universe scanned                                                   900|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=18 paper_keys=yes dry_run=False
  alpaca positions=15
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T09:34:33.196655-04:00 ===

[Run context]
Paper auth OK — equity $129094.78, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
2026-08-14 09:34:36,096 INFO   EXIT [b419|lab0419_s365_w1_0928_1005_r2|S365] stop_loss (-54.0%) SELL 1 MARA260828C00010000 @<= 0.20
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+139.6%) SELL failed DIS260814C00104000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-08-14 09:34:37,127 INFO   EXIT [b81|lab0081_s210_w1_0928_1005_r2|S210] stop_loss (-51.6%) SELL 1 DKNG260821C00027000 @<= 0.16
  EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-66.7%) SELL failed XOM260814C00170000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 already=6 failed=3

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260814T133628Z

- UTC timestamp: `20260814T133628Z`
- GitHub run: [#7090](https://github.com/28twagg-ops/TradingBot/actions/runs/31805390955)
- Run id: `31805390955`
- Live bot: exit=`0`, duration=`220s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 817 | 41.9 | -47.5 | +15.6 | $+8,217 |
| TAINTED | 1728 | 33.1 | -38.8 | +11.7 | $-8,922 |
| KEEP-only | 292 | 63.7 | +37.6 | +43.5 | $+5,715 |
| KEEP-only recent | 104 | 59.6 | +50.0 | +56.6 | $+1,689 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T09:25:53.627882-04:00","date":"2026-08-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":130503.8,"open_positions":13,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"7088","github_run_id":"31804608859","status":"ok","data_quality":{"clean":{"n":817,"win":41.86,"med":-47.45,"avg":15.61,"pnl":8216.53},"tainted":{"n":1728,"win":33.1,"med":-38.81,"avg":11.71,"pnl":-8922.34},"keep_only":{"n":292,"win":63.7,"med":37.59,"avg":43.47,"pnl":5715.45},"keep_only_recent":{"n":104,"win":59.62,"med":50.0,"avg":56.62,"pnl":1689.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:36:28  INFO      Mode: morning_prep
13:36:31  INFO        [prep_positions] 3/3 (3 valid)
13:36:31  INFO      Fetching tickers (universe=both)...
13:36:32  INFO        S&P 500: 503
13:36:33  INFO        MidCap 400: 400
13:36:33  INFO        Total: 903 tickers
13:36:35  INFO        [prep_universe] 40/900 (40 valid)
13:36:39  INFO        [prep_universe] 80/900 (80 valid)
13:36:41  INFO        [prep_universe] 120/900 (120 valid)
13:36:42  INFO        [prep_universe] 160/900 (160 valid)
13:36:45  INFO        [prep_universe] 200/900 (199 valid)
13:36:47  INFO        [prep_universe] 240/900 (238 valid)
13:36:58  INFO        [prep_universe] 280/900 (278 valid)
13:37:12  INFO        [prep_universe] 320/900 (318 valid)
13:37:23  INFO        [prep_universe] 360/900 (358 valid)
13:37:34  INFO        [prep_universe] 400/900 (397 valid)
13:37:47  INFO        [prep_universe] 440/900 (437 valid)
13:37:58  INFO        [prep_universe] 480/900 (477 valid)
13:38:09  INFO        [prep_universe] 520/900 (517 valid)
13:38:23  INFO        [prep_universe] 560/900 (557 valid)
13:38:34  INFO        [prep_universe] 600/900 (597 valid)
13:38:45  INFO        [prep_universe] 640/900 (637 valid)
13:38:59  INFO        [prep_universe] 680/900 (677 valid)
13:39:10  INFO        [prep_universe] 720/900 (717 valid)
13:39:21  INFO        [prep_universe] 760/900 (757 valid)
13:39:35  INFO        [prep_universe] 800/900 (797 valid)
13:39:47  INFO        [prep_universe] 840/900 (836 valid)
13:39:58  INFO        [prep_universe] 880/900 (876 valid)
13:40:05  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.59|
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
|  Invested                                                       $257.02|
|  Open P&L                                                        $+0.93|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $69.35     $97.48   $98.05   +0.6%   $+0.40  |
|  AES      Pullback50      $94.24     $14.72   $14.74   +0.2%   $+0.15  |
|  AFL      Pullback50      $93.43     $120.39  $120.88  +0.4%   $+0.38  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  AES       OrderType.STOP    6         None        14.67               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      1|
|  Signal candidates                                                   44|
|  Universe scanned                                                   900|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=18 paper_keys=yes dry_run=False
  alpaca positions=15
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T09:40:11.432294-04:00 ===

[Run context]
Paper auth OK — equity $128448.74, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
2026-08-14 09:40:15,731 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+52.4%) SELL 1 DIS260814C00105000 @<= 0.65
2026-08-14 09:40:17,054 INFO   EXIT [b418|lab0418_s365_w1_0928_1005_r1|S365] stop_loss (-54.0%) SELL 1 MARA260828C00010000 @<= 0.24
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+175.5%) SELL failed DIS260814C00104000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
  EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-100.0%) SELL failed XOM260814C00170000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
```

---

## Run 20260814T134127Z

- UTC timestamp: `20260814T134127Z`
- GitHub run: [#7091](https://github.com/28twagg-ops/TradingBot/actions/runs/31805780285)
- Run id: `31805780285`
- Live bot: exit=`0`, duration=`218s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 817 | 41.9 | -47.5 | +15.6 | $+8,217 |
| TAINTED | 1728 | 33.1 | -38.8 | +11.7 | $-8,922 |
| KEEP-only | 292 | 63.7 | +37.6 | +43.5 | $+5,715 |
| KEEP-only recent | 104 | 59.6 | +50.0 | +56.6 | $+1,689 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T09:25:53.627882-04:00","date":"2026-08-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":130503.8,"open_positions":13,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"7088","github_run_id":"31804608859","status":"ok","data_quality":{"clean":{"n":817,"win":41.86,"med":-47.45,"avg":15.61,"pnl":8216.53},"tainted":{"n":1728,"win":33.1,"med":-38.81,"avg":11.71,"pnl":-8922.34},"keep_only":{"n":292,"win":63.7,"med":37.59,"avg":43.47,"pnl":5715.45},"keep_only_recent":{"n":104,"win":59.62,"med":50.0,"avg":56.62,"pnl":1689.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:41:28  INFO      Mode: morning_prep
13:41:30  INFO        [prep_positions] 3/3 (3 valid)
13:41:30  INFO        Universe cache hit: 903 tickers (tickers_2026-08-14.json)
13:41:32  INFO        [prep_universe] 40/900 (40 valid)
13:41:33  INFO        [prep_universe] 80/900 (80 valid)
13:41:35  INFO        [prep_universe] 120/900 (120 valid)
13:41:36  INFO        [prep_universe] 160/900 (160 valid)
13:41:37  INFO        [prep_universe] 200/900 (199 valid)
13:41:45  INFO        [prep_universe] 240/900 (238 valid)
13:41:56  INFO        [prep_universe] 280/900 (278 valid)
13:42:07  INFO        [prep_universe] 320/900 (318 valid)
13:42:21  INFO        [prep_universe] 360/900 (358 valid)
13:42:32  INFO        [prep_universe] 400/900 (397 valid)
13:42:44  INFO        [prep_universe] 440/900 (437 valid)
13:42:57  INFO        [prep_universe] 480/900 (477 valid)
13:43:08  INFO        [prep_universe] 520/900 (517 valid)
13:43:22  INFO        [prep_universe] 560/900 (557 valid)
13:43:32  INFO        [prep_universe] 600/900 (597 valid)
13:43:43  INFO        [prep_universe] 640/900 (637 valid)
13:43:57  INFO        [prep_universe] 680/900 (677 valid)
13:44:07  INFO        [prep_universe] 720/900 (717 valid)
13:44:21  INFO        [prep_universe] 760/900 (757 valid)
13:44:31  INFO        [prep_universe] 800/900 (797 valid)
13:44:45  INFO        [prep_universe] 840/900 (836 valid)
13:44:55  INFO        [prep_universe] 880/900 (876 valid)
13:45:02  INFO        [prep_universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.97|
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
|  Invested                                                       $257.40|
|  Open P&L                                                        $+1.31|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $69.61     $97.48   $98.41   +1.0%   $+0.66  |
|  AES      Pullback50      $94.25     $14.72   $14.74   +0.2%   $+0.16  |
|  AFL      Pullback50      $93.55     $120.39  $121.03  +0.5%   $+0.50  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  AES       OrderType.STOP    6         None        14.67               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      1|
|  Signal candidates                                                   40|
|  Universe scanned                                                   900|
+========================================================================+
```

### Options bot full output

```text

## Run 20260814T134608Z

- UTC timestamp: `20260814T134608Z`
- GitHub run: [#7092](https://github.com/28twagg-ops/TradingBot/actions/runs/31806167893)
- Run id: `31806167893`
- Live bot: exit=`0`, duration=`239s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 817 | 41.9 | -47.5 | +15.6 | $+8,217 |
| TAINTED | 1728 | 33.1 | -38.8 | +11.7 | $-8,922 |
| KEEP-only | 292 | 63.7 | +37.6 | +43.5 | $+5,715 |
| KEEP-only recent | 104 | 59.6 | +50.0 | +56.6 | $+1,689 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T09:25:53.627882-04:00","date":"2026-08-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":130503.8,"open_positions":13,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"7088","github_run_id":"31804608859","status":"ok","data_quality":{"clean":{"n":817,"win":41.86,"med":-47.45,"avg":15.61,"pnl":8216.53},"tainted":{"n":1728,"win":33.1,"med":-38.81,"avg":11.71,"pnl":-8922.34},"keep_only":{"n":292,"win":63.7,"med":37.59,"avg":43.47,"pnl":5715.45},"keep_only_recent":{"n":104,"win":59.62,"med":50.0,"avg":56.62,"pnl":1689.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:46:09  INFO      Mode: morning_scan
13:46:10  INFO        [positions] 3/3 (3 valid)
13:46:10  INFO        SELL order cancelled AES  type=OrderType.STOP  id=21360f6f-8227-4691-bb1d-4ef06f06e7d0
13:46:10  INFO        SELL LIMIT AES  qty=6.391983695  limit=$14.74  id=2e6d0e46-5839-4064-9757-120195ecb4a1
13:46:31  INFO        SELL LIMIT filled AES (confirmed by position check)
13:46:31  INFO        TX logged: SELL AES  P&L 0.14%
13:46:31  INFO        Universe cache hit: 903 tickers (tickers_2026-08-14.json)
13:46:32  INFO        [universe] 40/901 (40 valid)
13:46:34  INFO        [universe] 80/901 (80 valid)
13:46:36  INFO        [universe] 120/901 (120 valid)
13:46:37  INFO        [universe] 160/901 (160 valid)
13:46:39  INFO        [universe] 200/901 (199 valid)
13:46:44  INFO        [universe] 240/901 (238 valid)
13:46:57  INFO        [universe] 280/901 (278 valid)
13:47:08  INFO        [universe] 320/901 (318 valid)
13:47:22  INFO        [universe] 360/901 (358 valid)
13:47:32  INFO        [universe] 400/901 (397 valid)
13:47:45  INFO        [universe] 440/901 (437 valid)
13:47:56  INFO        [universe] 480/901 (477 valid)
13:48:10  INFO        [universe] 520/901 (517 valid)
13:48:20  INFO        [universe] 560/901 (557 valid)
13:48:34  INFO        [universe] 600/901 (597 valid)
13:48:44  INFO        [universe] 640/901 (637 valid)
13:48:58  INFO        [universe] 680/901 (677 valid)
13:49:09  INFO        [universe] 720/901 (717 valid)
13:49:22  INFO        [universe] 760/901 (757 valid)
13:49:33  INFO        [universe] 800/901 (797 valid)
13:49:43  INFO        [universe] 840/901 (836 valid)
13:49:57  INFO        [universe] 880/901 (876 valid)
13:50:04  INFO        [universe] 901/901 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.96|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-14|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled  GapDown, GoldenPocket, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $466.96|
|  Cash                                                           $209.57|
|  Reserve                                          $23.35  (always kept)|
|  Available                                    $186.22  (for new trades)|
|  Trade size             $70.04  (15% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (3 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $69.52     $97.48   $98.29   +0.8%   $+0.57  |
|  AES      Pullback50      $94.22     $14.72   $14.74   +0.1%   $+0.13  |
|  AFL      Pullback50      $93.65     $120.39  $121.17  +0.7%   $+0.60  |
|                                                                        |
|  Total invested                                                 $257.39|
|  Total open P&L                                                  $+1.30|
|  Buys today: 0  |  entry cap: 0  |  max open: 3                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (51840.7m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  AES  P&L +0.1%  $+0.13                       EXIT: max_hold 3d (+0.1%)|
|  AFL  P&L +0.7%  $+0.60                                            HOLD|
|  ACGL  P&L +0.8%  $+0.57                                           HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 1 | filled 1 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 2|
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
|                         SIGNALS FOUND  --  48                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      eq     $306.22  26.3   -1.94   50MA bounce (-|
|  ADM      Pullback50      eq     $80.71   42.4   -2.49   50MA bounce (+|
|  CAH      Pullback50      eq     $230.95  52.0   -2.70   50MA bounce (+|
|  ED       Pullback50      eq     $108.56  36.8   -3.37   50MA bounce (-|
|  D        Pullback50      eq     $68.69   39.6   -2.13   50MA bounce (-|
|  ELV      Pullback50      eq     $398.42  65.0   -2.61   50MA bounce (+|
|  EVRG     Pullback50      eq     $83.89   37.9   -3.09   50MA bounce (-|
|  ES       Pullback50      eq     $72.21   35.9   -2.16   50MA bounce (-|
|  ECL      Pullback50      eq     $275.25  54.8   -2.99   50MA bounce (+|
|  F        Pullback50      eq     $14.13   40.2   -2.28   50MA bounce (-|
|  JBHT     Pullback50      eq     $281.97  50.9   -2.74   50MA bounce (+|
|  LRCX     Pullback50      eq     $339.30  64.1   -2.05   50MA bounce (+|
|  L        Pullback50      eq     $112.77  16.3   -2.71   50MA bounce (-|
|  MPWR     Pullback50      eq     $1393.~  54.6   -1.96   50MA bounce (-|
|  MAA      Pullback50      eq     $134.57  52.8   -2.09   50MA bounce (-|
|  O        Pullback50      eq     $63.12   28.7   -2.19   50MA bounce (+|
|  TRGP     Pullback50      eq     $271.90  53.3   -2.45   50MA bounce (+|
|  TT       Pullback50      eq     $478.29  47.8   -1.58   50MA bounce (+|
|  VTR      Pullback50      eq     $90.75   31.8   -2.37   50MA bounce (+|
|  WRB      Pullback50      eq     $70.46   21.3   -2.40   50MA bounce (-|
|  WST      Pullback50      eq     $345.45  68.6   -1.73   50MA bounce (+|
|  XEL      Pullback50      eq     $78.99   39.6   -2.82   50MA bounce (-|
|  ALLY     Pullback50      eq     $44.65   57.9   -2.04   50MA bounce (-|
|  ALV      Pullback50      eq     $121.78  55.8   -2.27   50MA bounce (+|
|  AM       Pullback50      eq     $22.20   53.3   -2.78   50MA bounce (+|
|  BKH      Pullback50      eq     $74.06   47.2   -2.23   50MA bounce (+|
|  CGNX     Pullback50      eq     $64.59   55.2   -1.83   50MA bounce (-|
|  CUZ      Pullback50      eq     $30.10   29.0   -2.28   50MA bounce (-|13:50:06  INFO        place_all_stops: checking 2 positions...
13:50:06  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
13:50:06  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
13:50:07  INFO        Daily log -> logs/daily/2026-08-14.md
13:50:07  INFO        Dashboard written → logs/dashboard.md

|  EEFT     Pullback50      eq     $73.95   42.0   -1.99   50MA bounce (+|
|  FBIN     Pullback50      eq     $48.02   38.9   -2.16   50MA bounce (+|
|  GATX     Pullback50      eq     $178.68  38.6   -2.35   50MA bounce (+|
|  GBCI     Pullback50      eq     $49.95   56.6   -2.50   50MA bounce (-|
|  FR       Pullback50      eq     $63.63   26.3   -2.34   50MA bounce (-|
|  GHC      Pullback50      eq     $1174.~  48.8   -2.78   50MA bounce (+|
|  KEX      Pullback50      eq     $138.67  39.9   -2.42   50MA bounce (-|
|  LAMR     Pullback50      eq     $155.85  39.3   -2.03   50MA bounce (-|
|  MOH      Pullback50      eq     $209.20  60.7   -0.66   50MA bounce (-|
|  MSM      Pullback50      eq     $121.51  37.8   -3.06   50MA bounce (+|
|  NWE      Pullback50      eq     $71.53   46.9   -2.55   50MA bounce (+|
|  SBRA     Pullback50      eq     $19.93   21.7   -1.67   50MA bounce (-|
|  SFM      Pullback50      eq     $82.42   60.8   -1.91   50MA bounce (+|
|  SLAB     Pullback50      eq     $218.43  59.5   -2.35   50MA bounce (+|
|  TLN      Pullback50      eq     $369.00  58.1   -2.53   50MA bounce (-|
|  TNL      Pullback50      eq     $75.29   46.6   -2.12   50MA bounce (+|
|  TCBI     Pullback50      eq     $101.35  68.3   -1.74   50MA bounce (-|
|  TEX      Pullback50      eq     $66.78   44.2   -1.89   50MA bounce (+|
|  VIAV     Pullback50      eq     $43.84   60.4   -2.11   50MA bounce (+|
|  WAL      Pullback50      eq     $82.27   48.5   -1.86   50MA bounce (+|
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
|  Scanned                                                            897|
|  Signals                                                             48|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                1|
|  Open pos                                                             2|
|  Equity                                                         $466.80|
|  Cash                                                           $303.76|
+========================================================================+
```

### Options bot full output

```text

## Run 20260814T135108Z

- UTC timestamp: `20260814T135108Z`
- GitHub run: [#7093](https://github.com/28twagg-ops/TradingBot/actions/runs/31806557829)
- Run id: `31806557829`
- Live bot: exit=`0`, duration=`233s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 817 | 41.9 | -47.5 | +15.6 | $+8,217 |
| TAINTED | 1728 | 33.1 | -38.8 | +11.7 | $-8,922 |
| KEEP-only | 292 | 63.7 | +37.6 | +43.5 | $+5,715 |
| KEEP-only recent | 104 | 59.6 | +50.0 | +56.6 | $+1,689 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T09:25:53.627882-04:00","date":"2026-08-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":130503.8,"open_positions":13,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"7088","github_run_id":"31804608859","status":"ok","data_quality":{"clean":{"n":817,"win":41.86,"med":-47.45,"avg":15.61,"pnl":8216.53},"tainted":{"n":1728,"win":33.1,"med":-38.81,"avg":11.71,"pnl":-8922.34},"keep_only":{"n":292,"win":63.7,"med":37.59,"avg":43.47,"pnl":5715.45},"keep_only_recent":{"n":104,"win":59.62,"med":50.0,"avg":56.62,"pnl":1689.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:51:10  INFO      Mode: morning_scan
13:51:11  INFO        [positions] 2/2 (2 valid)
13:51:11  INFO        Universe cache hit: 903 tickers (tickers_2026-08-14.json)
13:51:14  INFO        [universe] 40/901 (40 valid)
13:51:15  INFO        [universe] 80/901 (80 valid)
13:51:17  INFO        [universe] 120/901 (120 valid)
13:51:18  INFO        [universe] 160/901 (160 valid)
13:51:20  INFO        [universe] 200/901 (199 valid)
13:51:25  INFO        [universe] 240/901 (238 valid)
13:51:38  INFO        [universe] 280/901 (278 valid)
13:51:49  INFO        [universe] 320/901 (318 valid)
13:52:00  INFO        [universe] 360/901 (358 valid)
13:52:13  INFO        [universe] 400/901 (397 valid)
13:52:24  INFO        [universe] 440/901 (437 valid)
13:52:38  INFO        [universe] 480/901 (477 valid)
13:52:49  INFO        [universe] 520/901 (517 valid)
13:53:02  INFO        [universe] 560/901 (557 valid)
13:53:12  INFO        [universe] 600/901 (597 valid)
13:53:23  INFO        [universe] 640/901 (637 valid)
13:53:37  INFO        [universe] 680/901 (677 valid)
13:53:48  INFO        [universe] 720/901 (717 valid)
13:54:01  INFO        [universe] 760/901 (757 valid)
13:54:12  INFO        [universe] 800/901 (797 valid)
13:54:26  INFO        [universe] 840/901 (836 valid)
13:54:36  INFO        [universe] 880/901 (876 valid)
13:54:43  INFO        [universe] 901/901 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.05|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-14|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled  GapDown, GoldenPocket, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $467.05|
|  Cash                                                           $303.76|
|  Reserve                                          $23.35  (always kept)|
|  Available                                    $280.41  (for new trades)|
|  Trade size             $70.06  (15% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (2 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ACGL     Pullback50      $69.59     $97.48   $98.39   +0.9%   $+0.64  |
|  AFL      Pullback50      $93.69     $120.39  $121.22  +0.7%   $+0.64  |
|                                                                        |
|  Total invested                                                 $163.29|
|  Total open P&L                                                  $+1.29|
|  Buys today: 0  |  entry cap: 1  |  max open: 3                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (51845.7m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  AFL  P&L +0.7%  $+0.64                                            HOLD|
|  ACGL  P&L +0.9%  $+0.64                                           HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 0 | filled 0 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 2|
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
|                         SIGNALS FOUND  --  42                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      eq     $306.33  26.4   -1.93   50MA bounce (-|
|  ADM      Pullback50      eq     $80.68   42.3   -2.48   50MA bounce (+|
|  COHR     Pullback50      eq     $337.56  60.1   -1.45   50MA bounce (+|
|  D        Pullback50      eq     $68.63   39.1   -2.12   50MA bounce (-|
|  ESS      Pullback50      eq     $288.32  47.5   -1.98   50MA bounce (-|
|  ECL      Pullback50      eq     $275.72  55.4   -2.98   50MA bounce (+|
|  ES       Pullback50      eq     $72.10   35.5   -2.15   50MA bounce (-|
|  F        Pullback50      eq     $14.16   40.6   -2.26   50MA bounce (-|
|  L        Pullback50      eq     $112.56  15.5   -2.71   50MA bounce (-|
|  LRCX     Pullback50      eq     $339.33  64.1   -2.02   50MA bounce (+|
|  MAA      Pullback50      eq     $134.37  52.3   -2.09   50MA bounce (-|
|  MPWR     Pullback50      eq     $1392.~  54.6   -1.95   50MA bounce (-|
|  O        Pullback50      eq     $63.12   28.7   -2.18   50MA bounce (+|
|  SPG      Pullback50      eq     $221.30  30.4   -2.87   50MA bounce (-|
|  VTR      Pullback50      eq     $90.59   31.3   -2.36   50MA bounce (+|
|  WRB      Pullback50      eq     $70.45   21.3   -2.39   50MA bounce (-|
|  WST      Pullback50      eq     $346.81  70.4   -1.72   50MA bounce (+|
|  XEL      Pullback50      eq     $79.23   41.3   -2.81   50MA bounce (-|
|  ALLY     Pullback50      eq     $44.76   58.7   -2.03   50MA bounce (+|
|  ALV      Pullback50      eq     $122.16  56.7   -2.25   50MA bounce (+|
|  AM       Pullback50      eq     $22.27   54.2   -2.76   50MA bounce (+|
|  BKH      Pullback50      eq     $74.20   47.9   -2.23   50MA bounce (+|
|  CGNX     Pullback50      eq     $64.69   55.3   -1.81   50MA bounce (+|
|  CUZ      Pullback50      eq     $30.06   28.4   -2.28   50MA bounce (-|
|  ENS      Pullback50      eq     $205.01  61.2   -1.57   50MA bounce (-|
|  FCFS     Pullback50      eq     $213.32  56.9   -1.48   50MA bounce (-|
|  FBIN     Pullback50      eq     $48.28   39.6   -2.15   50MA bounce (+|
|  FR       Pullback50      eq     $63.72   27.4   -2.34   50MA bounce (-|
|  GBCI     Pullback50      eq     $50.02   56.9   -2.48   50MA bounce (-|
|  GATX     Pullback50      eq     $179.50  40.4   -2.35   50MA bounce (+|13:54:46  INFO        BUY  AAPL  $70.06  [Pullback50]  id=dcc0303c-3bb2-4bb2-a023-685ad8ebfcb7
13:55:00  INFO        place_all_stops: checking 3 positions...
13:55:00  INFO        STOP skipped AAPL: fractional (0.2288 shares) — software exit will handle it
13:55:00  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
13:55:00  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
13:55:00  INFO        Daily log -> logs/daily/2026-08-14.md
13:55:00  INFO        Dashboard written → logs/dashboard.md

|  KEX      Pullback50      eq     $138.29  39.2   -2.42   50MA bounce (-|
|  LAMR     Pullback50      eq     $155.71  38.9   -2.03   50MA bounce (-|
|  MOH      Pullback50      eq     $209.34  60.8   -0.66   50MA bounce (-|
|  MSM      Pullback50      eq     $121.95  39.1   -3.06   50MA bounce (+|
|  POR      Pullback50      eq     $50.58   46.0   -2.39   50MA bounce (-|
|  PII      Pullback50      eq     $68.91   38.6   -2.05   50MA bounce (-|
|  SBRA     Pullback50      eq     $19.96   21.8   -1.67   50MA bounce (+|
|  SLAB     Pullback50      eq     $218.43  59.5   -2.35   50MA bounce (+|
|  SFM      Pullback50      eq     $82.55   61.1   -1.90   50MA bounce (+|
|  TCBI     Pullback50      eq     $101.35  68.3   -1.74   50MA bounce (-|
|  TLN      Pullback50      eq     $368.48  57.9   -2.50   50MA bounce (-|
|  TNL      Pullback50      eq     $75.47   47.2   -2.12   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] AAPL  Pullback50                                   $70.06|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] ADM  Pullback50                                      cap 3|
|    SKIP [eq] COHR  Pullback50                                     cap 3|
|    SKIP [eq] D  Pullback50                                        cap 3|
|    SKIP [eq] ESS  Pullback50                                      cap 3|
|    SKIP [eq] ECL  Pullback50                                      cap 3|
|    SKIP [eq] ES  Pullback50                                       cap 3|
|    SKIP [eq] F  Pullback50                                        cap 3|
|    SKIP [eq] L  Pullback50                                        cap 3|
|    SKIP [eq] LRCX  Pullback50                                     cap 3|
|    SKIP [eq] MAA  Pullback50                                      cap 3|
|    SKIP [eq] MPWR  Pullback50                                     cap 3|
|    SKIP [eq] O  Pullback50                                        cap 3|
|    SKIP [eq] SPG  Pullback50                                      cap 3|
|    SKIP [eq] VTR  Pullback50                                      cap 3|
|    SKIP [eq] WRB  Pullback50                                      cap 3|
|    SKIP [eq] WST  Pullback50                                      cap 3|
|    SKIP [eq] XEL  Pullback50                                      cap 3|
|    SKIP [eq] ALLY  Pullback50                                     cap 3|
|    SKIP [eq] ALV  Pullback50                                      cap 3|
|    SKIP [eq] AM  Pullback50                                       cap 3|
|    SKIP [eq] BKH  Pullback50                                      cap 3|
|    SKIP [eq] CGNX  Pullback50                                     cap 3|
|    SKIP [eq] CUZ  Pullback50                                      cap 3|
|    SKIP [eq] ENS  Pullback50                                      cap 3|
|    SKIP [eq] FCFS  Pullback50                                     cap 3|
|    SKIP [eq] FBIN  Pullback50                                     cap 3|
|    SKIP [eq] FR  Pullback50                                       cap 3|
|    SKIP [eq] GBCI  Pullback50                                     cap 3|
|    SKIP [eq] GATX  Pullback50                                     cap 3|
|    SKIP [eq] KEX  Pullback50                                      cap 3|
|    SKIP [eq] LAMR  Pullback50                                     cap 3|
|    SKIP [eq] MOH  Pullback50                                      cap 3|
|    SKIP [eq] MSM  Pullback50                                      cap 3|
|    SKIP [eq] POR  Pullback50                                      cap 3|
|    SKIP [eq] PII  Pullback50                                      cap 3|
|    SKIP [eq] SBRA  Pullback50                                     cap 3|
|    SKIP [eq] SLAB  Pullback50                                     cap 3|
|    SKIP [eq] SFM  Pullback50                                      cap 3|
|    SKIP [eq] TCBI  Pullback50                                     cap 3|
|    SKIP [eq] TLN  Pullback50                                      cap 3|
|    SKIP [eq] TNL  Pullback50                                      cap 3|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      1|
+------------------------------------------------------------------------+
|  AAPL                                                 still unconfirmed|
+========================================================================+
+========================================================================+

+========================================================================+
|                           GTC STOP PLACEMENT                           |
+========================================================================+
|  Waiting 5s for 1 buy submit(s) to settle...                           |
+========================================================================+

+========================================================================+
|                            SESSION SUMMARY                             |
+========================================================================+
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Strategy  VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Scanned                                                            897|
|  Signals                                                             42|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  1 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $467.19|
|  Cash                                                           $233.71|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=17 paper_keys=yes dry_run=False
  alpaca positions=12
  FLAG b419|S365|eac2479e missing from Alpaca
  FLAG b418|S365|46f439ef missing from Alpaca
  FLAG b0|ORPHAN|d85edad3 missing from Alpaca
  FLAG b0|ORPHAN|f2e8a18a missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T09:55:03.321311-04:00 ===

[Run context]
Paper auth OK — equity $125568.69, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+296.2%) SELL failed DIS260814C00104000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-08-14 09:55:06,862 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-100.0%) SELL 1 XOM260814C00170000 @<= 0.01
Protective stops: placed=0 already=5 failed=1

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
```

---

## Run 20260814T135617Z

- UTC timestamp: `20260814T135617Z`
- GitHub run: [#7094](https://github.com/28twagg-ops/TradingBot/actions/runs/31806954149)
- Run id: `31806954149`
- Live bot: exit=`0`, duration=`217s`
- Options bot: exit=`0`, duration=`0s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 817 | 41.9 | -47.5 | +15.6 | $+8,217 |
| TAINTED | 1728 | 33.1 | -38.8 | +11.7 | $-8,922 |
| KEEP-only | 292 | 63.7 | +37.6 | +43.5 | $+5,715 |
| KEEP-only recent | 104 | 59.6 | +50.0 | +56.6 | $+1,689 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T09:25:53.627882-04:00","date":"2026-08-14","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":130503.8,"open_positions":13,"pending_orders":0,"open_lots":18,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"7088","github_run_id":"31804608859","status":"ok","data_quality":{"clean":{"n":817,"win":41.86,"med":-47.45,"avg":15.61,"pnl":8216.53},"tainted":{"n":1728,"win":33.1,"med":-38.81,"avg":11.71,"pnl":-8922.34},"keep_only":{"n":292,"win":63.7,"med":37.59,"avg":43.47,"pnl":5715.45},"keep_only_recent":{"n":104,"win":59.62,"med":50.0,"avg":56.62,"pnl":1689.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
13:56:18  INFO      Mode: morning_scan
13:56:18  INFO        [positions] 3/3 (3 valid)
13:56:18  INFO        Universe cache hit: 903 tickers (tickers_2026-08-14.json)
13:56:19  INFO        [universe] 40/900 (40 valid)
13:56:20  INFO        [universe] 80/900 (80 valid)
13:56:23  INFO        [universe] 120/900 (120 valid)
13:56:24  INFO        [universe] 160/900 (160 valid)
13:56:25  INFO        [universe] 200/900 (199 valid)
13:56:32  INFO        [universe] 240/900 (238 valid)
13:56:45  INFO        [universe] 280/900 (278 valid)
13:56:56  INFO        [universe] 320/900 (318 valid)
13:57:09  INFO        [universe] 360/900 (358 valid)
13:57:20  INFO        [universe] 400/900 (397 valid)
13:57:32  INFO        [universe] 440/900 (437 valid)
13:57:45  INFO        [universe] 480/900 (477 valid)
13:57:56  INFO        [universe] 520/900 (517 valid)
13:58:09  INFO        [universe] 560/900 (557 valid)
13:58:20  INFO        [universe] 600/900 (597 valid)
13:58:33  INFO        [universe] 640/900 (637 valid)
13:58:46  INFO        [universe] 680/900 (677 valid)
13:58:56  INFO        [universe] 720/900 (717 valid)
13:59:09  INFO        [universe] 760/900 (757 valid)
13:59:19  INFO        [universe] 800/900 (797 valid)
13:59:32  INFO        [universe] 840/900 (836 valid)
13:59:45  INFO        [universe] 880/900 (876 valid)
13:59:52  INFO        [universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.14|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-14|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled  GapDown, GoldenPocket, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $467.14|
|  Cash                                                           $233.71|
|  Reserve                                          $23.36  (always kept)|
|  Available                                    $210.35  (for new trades)|
|  Trade size             $70.07  (15% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (3 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $69.98     $306.10  $305.81  -0.1%   $-0.07  |
|  ACGL     Pullback50      $69.73     $97.48   $98.58   +1.1%   $+0.78  |
|  AFL      Pullback50      $93.72     $120.39  $121.26  +0.7%   $+0.67  |
|                                                                        |
|  Total invested                                                 $233.43|
|  Total open P&L                                                  $+1.38|
|  Buys today: 0  |  entry cap: 0  |  max open: 3                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (51850.8m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  AAPL  P&L -0.1%  $-0.07                                           HOLD|
|  AFL  P&L +0.7%  $+0.67                                            HOLD|
|  ACGL  P&L +1.1%  $+0.78                                           HOLD|
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
|                         SIGNALS FOUND  --  53                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AES      Pullback50      eq     $14.74   39.2   -2.26   50MA bounce (+|
|  ADM      Pullback50      eq     $80.65   42.2   -2.48   50MA bounce (+|
|  ED       Pullback50      eq     $108.55  36.7   -3.36   50MA bounce (-|
|  D        Pullback50      eq     $68.67   39.5   -2.11   50MA bounce (-|
|  ESS      Pullback50      eq     $287.38  46.4   -1.97   50MA bounce (-|
|  ES       Pullback50      eq     $72.10   35.5   -2.15   50MA bounce (-|
|  EVRG     Pullback50      eq     $83.81   37.3   -3.08   50MA bounce (-|
|  ECL      Pullback50      eq     $275.50  55.1   -2.98   50MA bounce (+|
|  F        Pullback50      eq     $14.18   41.1   -2.23   50MA bounce (-|
|  FTV      Pullback50      eq     $61.72   44.8   -1.93   50MA bounce (+|
|  HLT      Pullback50      eq     $328.23  48.0   -2.40   50MA bounce (-|
|  HIG      Pullback50      eq     $137.88  44.6   -2.63   50MA bounce (+|
|  JBHT     Pullback50      eq     $281.89  50.8   -2.73   50MA bounce (+|
|  LRCX     Pullback50      eq     $337.50  63.7   -1.98   50MA bounce (-|
|  L        Pullback50      eq     $112.86  17.1   -2.70   50MA bounce (-|
|  MPWR     Pullback50      eq     $1389.~  54.3   -1.95   50MA bounce (-|
|  MAA      Pullback50      eq     $134.50  52.6   -2.09   50MA bounce (-|
|  MS       Pullback50      eq     $218.66  55.3   -2.51   50MA bounce (+|
|  RSG      Pullback50      eq     $216.04  48.3   -3.17   50MA bounce (+|
|  O        Pullback50      eq     $63.05   27.8   -2.17   50MA bounce (+|
|  SPG      Pullback50      eq     $221.24  30.3   -2.86   50MA bounce (-|
|  SNA      Pullback50      eq     $404.09  46.9   -2.49   50MA bounce (+|
|  WRB      Pullback50      eq     $70.40   21.2   -2.39   50MA bounce (-|
|  VTR      Pullback50      eq     $90.56   31.3   -2.35   50MA bounce (+|
|  WST      Pullback50      eq     $346.48  70.2   -1.71   50MA bounce (+|
|  WM       Pullback50      eq     $225.44  28.0   -2.45   50MA bounce (-|
|  XEL      Pullback50      eq     $79.17   40.9   -2.80   50MA bounce (-|
|  ALLY     Pullback50      eq     $44.70   58.3   -2.03   50MA bounce (-|13:59:54  INFO        place_all_stops: checking 3 positions...
13:59:54  INFO        STOP skipped AAPL: fractional (0.2288 shares) — software exit will handle it
13:59:54  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
13:59:54  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
13:59:54  INFO        Daily log -> logs/daily/2026-08-14.md
13:59:54  INFO        Dashboard written → logs/dashboard.md

|  ALV      Pullback50      eq     $122.23  56.8   -2.24   50MA bounce (+|
|  AM       Pullback50      eq     $22.29   54.4   -2.76   50MA bounce (+|
|  BC       Pullback50      eq     $81.60   53.0   -2.48   50MA bounce (+|
|  CGNX     Pullback50      eq     $64.60   55.2   -1.78   50MA bounce (-|
|  CUZ      Pullback50      eq     $30.00   27.3   -2.27   50MA bounce (-|
|  FBIN     Pullback50      eq     $48.12   39.1   -2.15   50MA bounce (+|
|  GHC      Pullback50      eq     $1179.~  50.1   -2.72   50MA bounce (+|
|  FR       Pullback50      eq     $63.62   26.2   -2.33   50MA bounce (-|
|  GATX     Pullback50      eq     $179.50  40.4   -2.35   50MA bounce (+|
|  GBCI     Pullback50      eq     $50.05   57.1   -2.48   50MA bounce (-|
|  KEX      Pullback50      eq     $138.52  39.6   -2.42   50MA bounce (-|
|  JAZZ     Pullback50      eq     $244.36  36.5   -1.88   50MA bounce (+|
|  LAMR     Pullback50      eq     $156.20  40.2   -2.03   50MA bounce (-|
|  MOH      Pullback50      eq     $209.63  61.1   -0.65   50MA bounce (-|
|  MSM      Pullback50      eq     $121.56  37.9   -3.05   50MA bounce (+|
|  PII      Pullback50      eq     $69.18   39.3   -2.05   50MA bounce (-|
|  R        Pullback50      eq     $263.85  44.0   -2.30   50MA bounce (-|
|  SBRA     Pullback50      eq     $20.01   22.1   -1.66   50MA bounce (+|
|  SFM      Pullback50      eq     $82.50   61.0   -1.90   50MA bounce (+|
|  SLAB     Pullback50      eq     $218.44  59.6   -2.29   50MA bounce (+|
|  TCBI     Pullback50      eq     $101.34  68.3   -1.74   50MA bounce (-|
|  TLN      Pullback50      eq     $368.16  57.8   -2.48   50MA bounce (-|
|  TNL      Pullback50      eq     $75.19   46.2   -2.11   50MA bounce (+|
|  VC       Pullback50      eq     $107.54  58.8   -2.27   50MA bounce (-|
|  VIAV     Pullback50      eq     $43.87   60.4   -2.09   50MA bounce (+|
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
|  Signals                                                             53|
|  Entries                                                              0|
|  Buy submits                              0 confirmed  |  0 unconfirmed|
|  Exits                                                                0|
|  Open pos                                                             3|
|  Equity                                                         $467.21|
|  Cash                                                           $233.71|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=15 paper_keys=yes dry_run=False
  alpaca positions=12
  FLAG b418|S365|46f439ef missing from Alpaca
  FLAG b0|ORPHAN|d85edad3 missing from Alpaca
  FLAG b0|ORPHAN|f2e8a18a missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T09:59:56.935130-04:00 ===

[Run context]
Paper auth OK — equity $124978.65, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+296.2%) SELL failed DIS260814C00104000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 already=5 failed=1

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260814T140127Z

- UTC timestamp: `20260814T140127Z`
- GitHub run: [#7095](https://github.com/28twagg-ops/TradingBot/actions/runs/31807356051)
- Run id: `31807356051`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`93s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 818 | 41.8 | -47.5 | +15.5 | $+8,202 |
| TAINTED | 1744 | 33.1 | -38.9 | +12.6 | $-9,061 |
| KEEP-only | 293 | 63.5 | +37.5 | +43.2 | $+5,700 |
| KEEP-only recent | 105 | 59.0 | +50.0 | +55.6 | $+1,674 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T10:01:32.270057-04:00","date":"2026-08-14","mode":"entry+manage","header":"entry+manage (24 new)","elapsed_s":84.0,"phases_s":{"reconcile":0.39,"cancel":0.06,"manage":3.23,"protective_stops":0.63,"scan":62.98,"entries":12.26,"reconcile2":1.73},"signals":66,"placed":24,"equity":125278.65,"open_positions":17,"pending_orders":4,"open_lots":27,"submitted_today":24,"filled_today":20,"unattributed_contracts":0,"top_signals":["S165:MARA","S165:MSTR","S164:MARA","S164:MSTR","S168:MARA","S168:MSTR","S167:MARA","S167:MSTR"],"github_run":"7095","github_run_id":"31807356051","status":"ok","data_quality":{"clean":{"n":818,"win":41.81,"med":-47.48,"avg":15.53,"pnl":8201.53},"tainted":{"n":1744,"win":33.08,"med":-38.91,"avg":12.6,"pnl":-9061.34},"keep_only":{"n":293,"win":63.48,"med":37.5,"avg":43.15,"pnl":5700.45},"keep_only_recent":{"n":105,"win":59.05,"med":50.0,"avg":55.62,"pnl":1674.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
14:01:28  INFO      Mode: exits
14:01:29  INFO        Daily log -> logs/daily/2026-08-14.md
14:01:29  INFO        Daily log reconciled -> logs/daily/2026-08-14.md (1 ledger rows)
14:01:29  INFO        place_all_stops: checking 3 positions...
14:01:29  INFO        STOP skipped AAPL: fractional (0.2288 shares) — software exit will handle it
14:01:29  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
14:01:29  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
14:01:30  INFO        [positions] 3/3 (3 valid)
14:01:30  INFO        Daily log -> logs/daily/2026-08-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.04|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.0%  $-0.01                                           HOLD|
|  AFL  P&L +0.6%  $+0.58                                            HOLD|
|  ACGL  P&L +1.0%  $+0.72                                           HOLD|
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
  open_lots=12 paper_keys=yes dry_run=False
  alpaca positions=12
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T10:01:32.270057-04:00 ===

[Run context]
Paper auth OK — equity $125278.65, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+296.2%) SELL failed DIS260814C00104000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 already=5 failed=1

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 66 signal(s); top: ['S165:MARA', 'S165:MSTR', 'S164:MARA', 'S164:MSTR', 'S168:MARA', 'S168:MSTR', 'S167:MARA', 'S167:MSTR']
Paper lab: $124929 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 46 no tradeable call, 42 pending order
Placed 24 new entry order(s).
Protective stops: placed=6 already=5 failed=2

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (entry+manage) --                                     |
|Equity       : $125,278.65                                              |
|Open Risk    : 27 lots (17 broker pos)                                  |
|Today's Run  : 66 signals -> 24 orders submitted                        |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 27 Active Lots | 4 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=818   win= 41.8%  med= -47.5%  $+8,202           |
|  TAINTED            n=1744  win= 33.1%  med= -38.9%  $-9,061           |
|  KEEP-only          n=293   win= 63.5%  med= +37.5%  $+5,700           |
|  KEEP recent        n=105   win= 59.0%  med= +50.0%  $+1,674           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b109 lab0109_s212_w1_0928..   0%  -77.5%    10                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
+========================================================================+
+========================================================================+
|[PENDING ORDERS (4)]                                                    |
+========================================================================+
|  Top groups: S398:MARA(2), S405:MARA(2)                                |
|  ---------------------------------------------------------             |
|  b784 S398 MARA     limit=0.22                                         |
|  b785 S398 MARA     limit=0.22                                         |
|  b814 S405 MARA     limit=0.22                                         |
|  b815 S405 MARA     limit=0.22                                         |
+========================================================================+
+========================================================================+
|[PENDING EXITS (1)]                                                     |
+========================================================================+
|  b0   ORPHAN XOM260814C00170000 x1 stop_loss (-100.0%)                 |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (17)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  DIS260814C00104000            1   +328.3%   $   +174.00               |
|  MARA260904C00010500           4    -41.3%   $    -76.00               |
|  DIS260814C00106000           -1  -1047.1%   $    -59.33               |
|  MARA260911C00010500           2    -46.4%   $    -52.00               |
|  MARA260814P00009500          -1   -373.7%   $    -35.50               |
|  ARM260814P00245000           -1   -116.0%   $    -29.00               |
|  META260817C00625000           4    -13.6%   $    -24.00               |
|  MARA260821C00009000           4    -10.6%   $    -20.00               |
|  ... 9 more position(s)                                                |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=84.0s reconcile=0.39s cancel=0.06s manage=3.23s scan=62.98s entries=12.26s
STATUS: options_morning_bot run complete (PAPER) elapsed=84.0s. run=#7095 https://github.com/28twagg-ops/TradingBot/actions/runs/31807356051
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 3 buckets closed trades, $-14.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 13.3% (340/2562) ALERT
# Options signal frequency

_Generated 2026-08-14T10:03:01.404246_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |    27 | INFO |
| Total closed lots           |  1755 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=818 med=-47.5% | TAINTED n=1744 med=-38.9% | KEEP-only n=293 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.05 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T140552Z

- UTC timestamp: `20260814T140552Z`
- GitHub run: [#7096](https://github.com/28twagg-ops/TradingBot/actions/runs/31807773940)
- Run id: `31807773940`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`91s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 818 | 41.8 | -47.5 | +15.5 | $+8,202 |
| TAINTED | 1749 | 33.0 | -39.0 | +12.4 | $-9,221 |
| KEEP-only | 293 | 63.5 | +37.5 | +43.2 | $+5,700 |
| KEEP-only recent | 105 | 59.0 | +50.0 | +55.6 | $+1,674 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T10:05:56.248819-04:00","date":"2026-08-14","mode":"entry+manage","header":"entry+manage (18 new)","elapsed_s":81.7,"phases_s":{"reconcile":0.3,"cancel":0.01,"manage":5.22,"protective_stops":0.33,"scan":66.38,"entries":7.77,"reconcile2":0.63},"signals":66,"placed":18,"equity":125130.05,"open_positions":18,"pending_orders":12,"open_lots":37,"submitted_today":42,"filled_today":30,"unattributed_contracts":0,"top_signals":["S165:MARA","S165:MSTR","S164:MARA","S164:MSTR","S168:MARA","S168:MSTR","S167:MARA","S167:MSTR"],"github_run":"7096","github_run_id":"31807773940","status":"ok","data_quality":{"clean":{"n":818,"win":41.81,"med":-47.48,"avg":15.53,"pnl":8201.53},"tainted":{"n":1749,"win":33.05,"med":-39.02,"avg":12.42,"pnl":-9221.34},"keep_only":{"n":293,"win":63.48,"med":37.5,"avg":43.15,"pnl":5700.45},"keep_only_recent":{"n":105,"win":59.05,"med":50.0,"avg":55.62,"pnl":1674.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
14:05:52  INFO      Mode: exits
14:05:53  INFO        Daily log -> logs/daily/2026-08-14.md
14:05:53  INFO        Daily log reconciled -> logs/daily/2026-08-14.md (1 ledger rows)
14:05:53  INFO        place_all_stops: checking 3 positions...
14:05:53  INFO        STOP skipped AAPL: fractional (0.2288 shares) — software exit will handle it
14:05:53  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
14:05:53  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
14:05:54  INFO        [positions] 3/3 (3 valid)
14:05:54  INFO        Daily log -> logs/daily/2026-08-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.79|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.1%  $-0.05                                           HOLD|
|  AFL  P&L +0.4%  $+0.39                                            HOLD|
|  ACGL  P&L +1.0%  $+0.68                                           HOLD|
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
  open_lots=27 paper_keys=yes dry_run=False
  alpaca positions=19
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T10:05:56.248819-04:00 ===

[Run context]
Paper auth OK — equity $125130.05, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+322.6%) SELL failed DIS260814C00104000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 already=11 failed=2

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 66 signal(s); top: ['S165:MARA', 'S165:MSTR', 'S164:MARA', 'S164:MSTR', 'S168:MARA', 'S168:MSTR', 'S167:MARA', 'S167:MSTR']
Paper lab: $125455 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  [b110 DKNG] ENTRY failed: {"buy_limit_price":"0.46","code":40310000,"existing_order_id":"74fdbdeb-357e-4b5e-9736-5a0aa5cbf691","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.18"}
  [b111 DKNG] ENTRY failed: {"buy_limit_price":"0.46","code":40310000,"existing_order_id":"74fdbdeb-357e-4b5e-9736-5a0aa5cbf691","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.18"}
  [b322 MARA] ENTRY failed: {"buy_limit_price":"0.44","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b323 MARA] ENTRY failed: {"buy_limit_price":"0.44","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b778 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"35321683-9f63-4281-90b8-2c2ce154d9e7","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.21"}
  [b779 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"35321683-9f63-4281-90b8-2c2ce154d9e7","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.21"}
  [b802 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"35321683-9f63-4281-90b8-2c2ce154d9e7","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.21"}
  [b803 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"35321683-9f63-4281-90b8-2c2ce154d9e7","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.21"}
  Skipped: 100 no tradeable call, 38 already attempted today, 36 pending order
Placed 18 new entry order(s).
Protective stops: placed=1 already=11 failed=2

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (entry+manage) --                                     |
|Equity       : $125,130.05                                              |
|Open Risk    : 37 lots (18 broker pos)                                  |
|Today's Run  : 66 signals -> 18 orders submitted                        |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 37 Active Lots | 12 Pending Orders                       |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=818   win= 41.8%  med= -47.5%  $+8,202           |
|  TAINTED            n=1749  win= 33.0%  med= -39.0%  $-9,221           |
|  KEEP-only          n=293   win= 63.5%  med= +37.5%  $+5,700           |
|  KEEP recent        n=105   win= 59.0%  med= +50.0%  $+1,674           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b109 lab0109_s212_w1_0928..   0%  -77.5%    10                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
+========================================================================+
+========================================================================+
|[PENDING ORDERS (12)]                                                   |
+========================================================================+
|  Top groups: S398:MARA(2), S405:MARA(2), S212:MCD(2)                   |
|  ---------------------------------------------------------             |
|  b784 S398 MARA     limit=0.22                                         |
|  b785 S398 MARA     limit=0.22                                         |
|  b814 S405 MARA     limit=0.22                                         |
|  b815 S405 MARA     limit=0.22                                         |
|  b110 S212 MCD      limit=0.12                                         |
|  ... 7 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|[PENDING EXITS (1)]                                                     |
+========================================================================+
|  b0   ORPHAN XOM260814C00170000 x1 stop_loss (-100.0%)                 |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (18)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  DIS260814C00104000            1   +307.5%   $   +163.00               |
|  MARA260904C00010500           4    -41.3%   $    -76.00               |
|  MARA260911C00010500           2    -46.4%   $    -52.00               |
|  DIS260814C00106000           -1   -870.6%   $    -49.33               |
|  META260817C00625000           4    -20.5%   $    -36.00               |
|  MARA260814P00009500          -1   -363.2%   $    -34.50               |
|  ARM260814P00245000           -1   -116.0%   $    -29.00               |
|  MARA260821C00009500          12     -8.0%   $    -24.00               |
|  ... 10 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=81.7s reconcile=0.3s cancel=0.01s manage=5.22s scan=66.38s entries=7.77s
STATUS: options_morning_bot run complete (PAPER) elapsed=81.7s. run=#7096 https://github.com/28twagg-ops/TradingBot/actions/runs/31807773940
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 3 buckets closed trades, $-14.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 13.4% (345/2567) ALERT
# Options signal frequency

_Generated 2026-08-14T10:07:23.772642_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     5 | WARN | <<<
| Total open lots             |    37 | INFO |
| Total closed lots           |  1755 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=818 med=-47.5% | TAINTED n=1749 med=-39.0% | KEEP-only n=293 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T141056Z

- UTC timestamp: `20260814T141056Z`
- GitHub run: [#7097](https://github.com/28twagg-ops/TradingBot/actions/runs/31808173637)
- Run id: `31808173637`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`108s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 818 | 41.8 | -47.5 | +15.5 | $+8,202 |
| TAINTED | 1751 | 33.1 | -39.0 | +12.4 | $-9,217 |
| KEEP-only | 293 | 63.5 | +37.5 | +43.2 | $+5,700 |
| KEEP-only recent | 105 | 59.0 | +50.0 | +55.6 | $+1,674 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T10:11:01.946012-04:00","date":"2026-08-14","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":97.6,"phases_s":{"reconcile":0.76,"cancel":0.07,"manage":10.4,"protective_stops":1.84,"scan":70.76,"entries":10.82,"reconcile2":0.48},"signals":63,"placed":2,"equity":125304.52,"open_positions":19,"pending_orders":8,"open_lots":41,"submitted_today":44,"filled_today":36,"unattributed_contracts":0,"top_signals":["S165:MARA","S165:MSTR","S164:MARA","S164:MSTR","S168:MARA","S168:MSTR","S167:MARA","S167:MSTR"],"github_run":"7097","github_run_id":"31808173637","status":"ok","data_quality":{"clean":{"n":818,"win":41.81,"med":-47.48,"avg":15.53,"pnl":8201.53},"tainted":{"n":1751,"win":33.07,"med":-39.02,"avg":12.4,"pnl":-9217.34},"keep_only":{"n":293,"win":63.48,"med":37.5,"avg":43.15,"pnl":5700.45},"keep_only_recent":{"n":105,"win":59.05,"med":50.0,"avg":55.62,"pnl":1674.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
14:10:57  INFO      Mode: exits
14:10:58  INFO        Daily log -> logs/daily/2026-08-14.md
14:10:58  INFO        Daily log reconciled -> logs/daily/2026-08-14.md (1 ledger rows)
14:10:58  INFO        place_all_stops: checking 3 positions...
14:10:58  INFO        STOP skipped AAPL: fractional (0.2288 shares) — software exit will handle it
14:10:58  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
14:10:58  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
14:10:59  INFO        [positions] 3/3 (3 valid)
14:10:59  INFO        Daily log -> logs/daily/2026-08-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.85|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.1%  $-0.05                                           HOLD|
|  AFL  P&L +0.4%  $+0.42                                            HOLD|
|  ACGL  P&L +1.1%  $+0.73                                           HOLD|
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
  alpaca positions=20
  FLAG b281|S351|80ae1177 missing from Alpaca
  FLAG b280|S351|e990d51a missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T10:11:01.946012-04:00 ===

[Run context]
Paper auth OK — equity $125304.52, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+307.5%) SELL failed DIS260814C00104000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
2026-08-14 10:11:12,045 INFO   EXIT [b279|lab0279_s350_w2_1005_1045_r2|S350] stop_loss (-66.7%) SELL 1 MSTR260814C00101000 @<= 0.02
Protective stops: placed=2 already=11 failed=2

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 63 signal(s); top: ['S165:MARA', 'S165:MSTR', 'S164:MARA', 'S164:MSTR', 'S168:MARA', 'S168:MSTR', 'S167:MARA', 'S167:MSTR']
Paper lab: $125242 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  [b282 MSTR] ENTRY failed: {"buy_limit_price":"0.15","code":40310000,"existing_order_id":"b69ed636-0837-44d4-9438-4d80b9884f97","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.1"}
  [b283 MSTR] ENTRY failed: {"buy_limit_price":"0.15","code":40310000,"existing_order_id":"b69ed636-0837-44d4-9438-4d80b9884f97","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.1"}
  [b322 MARA] ENTRY failed: {"buy_limit_price":"0.43","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b323 MARA] ENTRY failed: {"buy_limit_price":"0.43","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  Skipped: 48 no tradeable call, 4 already attempted today, 20 pending order
Placed 2 new entry order(s).
Protective stops: placed=0 already=13 failed=2

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (entry+manage) --                                     |
|Equity       : $125,304.52                                              |
|Open Risk    : 41 lots (19 broker pos)                                  |
|Today's Run  : 63 signals -> 2 orders submitted                         |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 41 Active Lots | 8 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=818   win= 41.8%  med= -47.5%  $+8,202           |
|  TAINTED            n=1751  win= 33.1%  med= -39.0%  $-9,217           |
|  KEEP-only          n=293   win= 63.5%  med= +37.5%  $+5,700           |
|  KEEP recent        n=105   win= 59.0%  med= +50.0%  $+1,674           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b109 lab0109_s212_w1_0928..   0%  -77.5%    10                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
+========================================================================+
+========================================================================+
|[PENDING ORDERS (8)]                                                    |
+========================================================================+
|  Top groups: S398:MARA(2), S405:MARA(2), S212:MCD(2)                   |
|  ---------------------------------------------------------             |
|  b784 S398 MARA     limit=0.22                                         |
|  b785 S398 MARA     limit=0.22                                         |
|  b814 S405 MARA     limit=0.22                                         |
|  b815 S405 MARA     limit=0.22                                         |
|  b110 S212 MCD      limit=0.12                                         |
|  ... 3 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|[PENDING EXITS (2)]                                                     |
+========================================================================+
|  b0   ORPHAN XOM260814C00170000 x1 stop_loss (-100.0%)                 |
|  b279 S350 MSTR260814C00101000 x1 stop_loss (-66.7%)                   |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (19)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  DIS260814C00104000            1   +309.4%   $   +164.00               |
|  MARA260904C00010500           4    -43.5%   $    -80.00               |
|  ARM260814P00245000           -1   -240.0%   $    -60.00               |
|  DIS260814C00106000           -1   -923.5%   $    -52.33               |
|  MARA260911C00010500           2    -44.6%   $    -50.00               |
|  META260817C00625000           4    -25.0%   $    -44.00               |
|  MARA260814P00009500          -1   -363.2%   $    -34.50               |
|  MARA260821C00009000           4    -12.8%   $    -24.00               |
|  ... 11 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=97.6s reconcile=0.76s cancel=0.07s manage=10.4s scan=70.76s entries=10.82s
STATUS: options_morning_bot run complete (PAPER) elapsed=97.6s. run=#7097 https://github.com/28twagg-ops/TradingBot/actions/runs/31808173637
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 3 buckets closed trades, $-14.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 13.4% (345/2569) ALERT
# Options signal frequency

_Generated 2026-08-14T10:12:45.414614_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  1757 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=818 med=-47.5% | TAINTED n=1751 med=-39.0% | KEEP-only n=293 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.85 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T141551Z

- UTC timestamp: `20260814T141551Z`
- GitHub run: [#7098](https://github.com/28twagg-ops/TradingBot/actions/runs/31808575591)
- Run id: `31808575591`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`106s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 818 | 41.8 | -47.5 | +15.5 | $+8,202 |
| TAINTED | 1751 | 33.1 | -39.0 | +12.4 | $-9,217 |
| KEEP-only | 293 | 63.5 | +37.5 | +43.2 | $+5,700 |
| KEEP-only recent | 105 | 59.0 | +50.0 | +55.6 | $+1,674 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T10:15:56.293162-04:00","date":"2026-08-14","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":96.4,"phases_s":{"reconcile":0.39,"cancel":0.06,"manage":11.9,"protective_stops":1.31,"scan":71.1,"entries":8.92,"reconcile2":0.5},"signals":65,"placed":4,"equity":124630.52,"open_positions":20,"pending_orders":10,"open_lots":43,"submitted_today":48,"filled_today":38,"unattributed_contracts":0,"top_signals":["S165:MARA","S165:MSTR","S164:MARA","S164:MSTR","S168:MARA","S168:MSTR","S167:MARA","S167:MSTR"],"github_run":"7098","github_run_id":"31808575591","status":"ok","data_quality":{"clean":{"n":818,"win":41.81,"med":-47.48,"avg":15.53,"pnl":8201.53},"tainted":{"n":1751,"win":33.07,"med":-39.02,"avg":12.4,"pnl":-9217.34},"keep_only":{"n":293,"win":63.48,"med":37.5,"avg":43.15,"pnl":5700.45},"keep_only_recent":{"n":105,"win":59.05,"med":50.0,"avg":55.62,"pnl":1674.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
14:15:52  INFO      Mode: exits
14:15:53  INFO        Daily log -> logs/daily/2026-08-14.md
14:15:53  INFO        Daily log reconciled -> logs/daily/2026-08-14.md (1 ledger rows)
14:15:53  INFO        place_all_stops: checking 3 positions...
14:15:53  INFO        STOP skipped AAPL: fractional (0.2288 shares) — software exit will handle it
14:15:53  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
14:15:53  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
14:15:53  INFO        [positions] 3/3 (3 valid)
14:15:54  INFO        Daily log -> logs/daily/2026-08-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.65|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.2%  $-0.14                                           HOLD|
|  AFL  P&L +0.4%  $+0.36                                            HOLD|
|  ACGL  P&L +1.0%  $+0.66                                           HOLD|
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
  open_lots=41 paper_keys=yes dry_run=False
  alpaca positions=21
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T10:15:56.293162-04:00 ===

[Run context]
Paper auth OK — equity $124630.52, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+309.4%) SELL failed DIS260814C00104000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 already=13 failed=2

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 65 signal(s); top: ['S165:MARA', 'S165:MSTR', 'S164:MARA', 'S164:MSTR', 'S168:MARA', 'S168:MSTR', 'S167:MARA', 'S167:MSTR']
Paper lab: $124151 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  [b322 MARA] ENTRY failed: {"buy_limit_price":"0.44","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b323 MARA] ENTRY failed: {"buy_limit_price":"0.44","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  Skipped: 50 no tradeable call, 4 already attempted today, 22 pending order
Placed 4 new entry order(s).
Protective stops: placed=1 already=13 failed=2

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (entry+manage) --                                     |
|Equity       : $124,630.52                                              |
|Open Risk    : 43 lots (20 broker pos)                                  |
|Today's Run  : 65 signals -> 4 orders submitted                         |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 43 Active Lots | 10 Pending Orders                       |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=818   win= 41.8%  med= -47.5%  $+8,202           |
|  TAINTED            n=1751  win= 33.1%  med= -39.0%  $-9,217           |
|  KEEP-only          n=293   win= 63.5%  med= +37.5%  $+5,700           |
|  KEEP recent        n=105   win= 59.0%  med= +50.0%  $+1,674           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b109 lab0109_s212_w1_0928..   0%  -77.5%    10                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
+========================================================================+
+========================================================================+
|[PENDING ORDERS (10)]                                                   |
+========================================================================+
|  Top groups: S398:MARA(2), S405:MARA(2), S212:MCD(2)                   |
|  ---------------------------------------------------------             |
|  b784 S398 MARA     limit=0.22                                         |
|  b785 S398 MARA     limit=0.22                                         |
|  b814 S405 MARA     limit=0.22                                         |
|  b815 S405 MARA     limit=0.22                                         |
|  b110 S212 MCD      limit=0.12                                         |
|  ... 5 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|[PENDING EXITS (2)]                                                     |
+========================================================================+
|  b0   ORPHAN XOM260814C00170000 x1 stop_loss (-100.0%)                 |
|  b279 S350 MSTR260814C00101000 x1 stop_loss (-66.7%)                   |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (20)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  DIS260814C00104000            1   +326.4%   $   +173.00               |
|  DIS260814C00106000           -1  -1488.2%   $    -84.33               |
|  MARA260904C00010500           4    -41.3%   $    -76.00               |
|  ARM260814P00245000           -1   -240.0%   $    -60.00               |
|  MARA260911C00010500           2    -41.1%   $    -46.00               |
|  META260817C00625000           4    -20.5%   $    -36.00               |
|  MARA260814P00009500          -1   -363.2%   $    -34.50               |
|  MARA260821C00009000           4    -10.6%   $    -20.00               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=96.4s reconcile=0.39s cancel=0.06s manage=11.9s scan=71.1s entries=8.92s
STATUS: options_morning_bot run complete (PAPER) elapsed=96.4s. run=#7098 https://github.com/28twagg-ops/TradingBot/actions/runs/31808575591
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 3 buckets closed trades, $-14.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 13.4% (345/2569) ALERT
# Options signal frequency

_Generated 2026-08-14T10:17:38.638971_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |    43 | INFO |
| Total closed lots           |  1757 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=818 med=-47.5% | TAINTED n=1751 med=-39.0% | KEEP-only n=293 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.65 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T142047Z

- UTC timestamp: `20260814T142047Z`
- GitHub run: [#7099](https://github.com/28twagg-ops/TradingBot/actions/runs/31808977798)
- Run id: `31808977798`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`93s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 818 | 41.8 | -47.5 | +15.5 | $+8,202 |
| TAINTED | 1751 | 33.1 | -39.0 | +12.4 | $-9,217 |
| KEEP-only | 293 | 63.5 | +37.5 | +43.2 | $+5,700 |
| KEEP-only recent | 105 | 59.0 | +50.0 | +55.6 | $+1,674 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T10:20:51.449956-04:00","date":"2026-08-14","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":83.0,"phases_s":{"reconcile":0.14,"cancel":0.01,"manage":5.61,"protective_stops":0.33,"scan":71.95,"entries":3.8,"reconcile2":0.25},"signals":66,"placed":0,"equity":123766.41,"open_positions":20,"pending_orders":8,"open_lots":43,"submitted_today":48,"filled_today":40,"unattributed_contracts":0,"top_signals":["S165:MARA","S165:MSTR","S164:MARA","S164:MSTR","S168:MARA","S168:MSTR","S167:MARA","S167:MSTR"],"github_run":"7099","github_run_id":"31808977798","status":"ok","data_quality":{"clean":{"n":818,"win":41.81,"med":-47.48,"avg":15.53,"pnl":8201.53},"tainted":{"n":1751,"win":33.07,"med":-39.02,"avg":12.4,"pnl":-9217.34},"keep_only":{"n":293,"win":63.48,"med":37.5,"avg":43.15,"pnl":5700.45},"keep_only_recent":{"n":105,"win":59.05,"med":50.0,"avg":55.62,"pnl":1674.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
14:20:48  INFO      Mode: exits
14:20:48  INFO        Daily log -> logs/daily/2026-08-14.md
14:20:48  INFO        Daily log reconciled -> logs/daily/2026-08-14.md (1 ledger rows)
14:20:48  INFO        place_all_stops: checking 3 positions...
14:20:48  INFO        STOP skipped AAPL: fractional (0.2288 shares) — software exit will handle it
14:20:48  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
14:20:48  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
14:20:49  INFO        [positions] 3/3 (3 valid)
14:20:49  INFO        Daily log -> logs/daily/2026-08-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.02|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.2%  $-0.14                                           HOLD|
|  AFL  P&L +0.6%  $+0.59                                            HOLD|
|  ACGL  P&L +1.2%  $+0.82                                           HOLD|
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
  open_lots=43 paper_keys=yes dry_run=False
  alpaca positions=21
  FLAG b277|S350|5dfa966e missing from Alpaca
  FLAG b276|S350|bd1582a3 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T10:20:51.449956-04:00 ===

[Run context]
Paper auth OK — equity $123766.41, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+335.8%) SELL failed DIS260814C00104000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 already=13 failed=2

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 66 signal(s); top: ['S165:MARA', 'S165:MSTR', 'S164:MARA', 'S164:MSTR', 'S168:MARA', 'S168:MSTR', 'S167:MARA', 'S167:MSTR']
Paper lab: $123362 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  [b322 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b323 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  Skipped: 48 no tradeable call, 4 already attempted today, 26 pending order
Placed 0 new entry order(s).
Protective stops: placed=1 already=13 failed=2

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (entry+manage) --                                     |
|Equity       : $123,766.41                                              |
|Open Risk    : 43 lots (20 broker pos)                                  |
|Today's Run  : 66 signals -> 0 orders submitted                         |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 43 Active Lots | 8 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=818   win= 41.8%  med= -47.5%  $+8,202           |
|  TAINTED            n=1751  win= 33.1%  med= -39.0%  $-9,217           |
|  KEEP-only          n=293   win= 63.5%  med= +37.5%  $+5,700           |
|  KEEP recent        n=105   win= 59.0%  med= +50.0%  $+1,674           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b109 lab0109_s212_w1_0928..   0%  -77.5%    10                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
+========================================================================+
+========================================================================+
|[PENDING ORDERS (8)]                                                    |
+========================================================================+
|  Top groups: S398:MARA(2), S405:MARA(2), S212:MCD(2)                   |
|  ---------------------------------------------------------             |
|  b784 S398 MARA     limit=0.22                                         |
|  b785 S398 MARA     limit=0.22                                         |
|  b814 S405 MARA     limit=0.22                                         |
|  b815 S405 MARA     limit=0.22                                         |
|  b110 S212 MCD      limit=0.12                                         |
|  ... 3 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|[PENDING EXITS (2)]                                                     |
+========================================================================+
|  b0   ORPHAN XOM260814C00170000 x1 stop_loss (-100.0%)                 |
|  b279 S350 MSTR260814C00101000 x1 stop_loss (-66.7%)                   |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (20)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  DIS260814C00104000            1   +345.3%   $   +183.00               |
|  MARA260904C00010500           4    -43.5%   $    -80.00               |
|  META260817C00625000           4    -38.6%   $    -68.00               |
|  DIS260814C00106000           -1  -1100.0%   $    -62.33               |
|  ARM260814P00245000           -1   -196.0%   $    -49.00               |
|  MARA260911C00010500           2    -41.1%   $    -46.00               |
|  MSTR260821C00103000           4    -14.5%   $    -40.00               |
|  MARA260814P00009500          -1   -394.7%   $    -37.50               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=83.0s reconcile=0.14s cancel=0.01s manage=5.61s scan=71.95s entries=3.8s
STATUS: options_morning_bot run complete (PAPER) elapsed=83.0s. run=#7099 https://github.com/28twagg-ops/TradingBot/actions/runs/31808977798
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 3 buckets closed trades, $-14.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 13.4% (345/2569) ALERT
# Options signal frequency

_Generated 2026-08-14T10:22:20.180157_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |    43 | INFO |
| Total closed lots           |  1757 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=818 med=-47.5% | TAINTED n=1751 med=-39.0% | KEEP-only n=293 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.02 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T142549Z

- UTC timestamp: `20260814T142549Z`
- GitHub run: [#7100](https://github.com/28twagg-ops/TradingBot/actions/runs/31809387286)
- Run id: `31809387286`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`95s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 818 | 41.8 | -47.5 | +15.5 | $+8,202 |
| TAINTED | 1751 | 33.1 | -39.0 | +12.4 | $-9,217 |
| KEEP-only | 293 | 63.5 | +37.5 | +43.2 | $+5,700 |
| KEEP-only recent | 105 | 59.0 | +50.0 | +55.6 | $+1,674 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T10:25:55.325898-04:00","date":"2026-08-14","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":85.4,"phases_s":{"reconcile":0.4,"cancel":0.06,"manage":10.25,"protective_stops":1.34,"scan":62.48,"entries":8.06,"reconcile2":0.45},"signals":65,"placed":0,"equity":122841.3,"open_positions":19,"pending_orders":8,"open_lots":41,"submitted_today":48,"filled_today":40,"unattributed_contracts":0,"top_signals":["S165:MARA","S165:MSTR","S164:MARA","S164:MSTR","S168:MARA","S168:MSTR","S167:MARA","S167:MSTR"],"github_run":"7100","github_run_id":"31809387286","status":"ok","data_quality":{"clean":{"n":818,"win":41.81,"med":-47.48,"avg":15.53,"pnl":8201.53},"tainted":{"n":1751,"win":33.07,"med":-39.02,"avg":12.4,"pnl":-9217.34},"keep_only":{"n":293,"win":63.48,"med":37.5,"avg":43.15,"pnl":5700.45},"keep_only_recent":{"n":105,"win":59.05,"med":50.0,"avg":55.62,"pnl":1674.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
14:25:51  INFO      Mode: exits
14:25:52  INFO        Daily log -> logs/daily/2026-08-14.md
14:25:52  INFO        Daily log reconciled -> logs/daily/2026-08-14.md (1 ledger rows)
14:25:52  INFO        place_all_stops: checking 3 positions...
14:25:52  INFO        STOP skipped AAPL: fractional (0.2288 shares) — software exit will handle it
14:25:52  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
14:25:52  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
14:25:52  INFO        [positions] 3/3 (3 valid)
14:25:52  INFO        Daily log -> logs/daily/2026-08-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $467.10|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.4%  $-0.26                                           HOLD|
|  AFL  P&L +0.7%  $+0.67                                            HOLD|
|  ACGL  P&L +1.4%  $+0.93                                           HOLD|
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
  open_lots=43 paper_keys=yes dry_run=False
  alpaca positions=21
  FLAG b283|S351|15c7567c missing from Alpaca
  FLAG b282|S351|2d160cbd missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T10:25:55.325898-04:00 ===

[Run context]
Paper auth OK — equity $122863.34, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+364.2%) SELL failed DIS260814C00104000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 already=13 failed=2

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 65 signal(s); top: ['S165:MARA', 'S165:MSTR', 'S164:MARA', 'S164:MSTR', 'S168:MARA', 'S168:MSTR', 'S167:MARA', 'S167:MSTR']
Paper lab: $123138 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  [b322 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b323 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  Skipped: 46 no tradeable call, 8 already attempted today, 24 pending order
Placed 0 new entry order(s).
Protective stops: placed=0 already=13 failed=2

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (entry+manage) --                                     |
|Equity       : $122,841.30                                              |
|Open Risk    : 41 lots (19 broker pos)                                  |
|Today's Run  : 65 signals -> 0 orders submitted                         |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 41 Active Lots | 8 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=818   win= 41.8%  med= -47.5%  $+8,202           |
|  TAINTED            n=1751  win= 33.1%  med= -39.0%  $-9,217           |
|  KEEP-only          n=293   win= 63.5%  med= +37.5%  $+5,700           |
|  KEEP recent        n=105   win= 59.0%  med= +50.0%  $+1,674           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b109 lab0109_s212_w1_0928..   0%  -77.5%    10                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
+========================================================================+
+========================================================================+
|[PENDING ORDERS (8)]                                                    |
+========================================================================+
|  Top groups: S398:MARA(2), S405:MARA(2), S212:MCD(2)                   |
|  ---------------------------------------------------------             |
|  b784 S398 MARA     limit=0.22                                         |
|  b785 S398 MARA     limit=0.22                                         |
|  b814 S405 MARA     limit=0.22                                         |
|  b815 S405 MARA     limit=0.22                                         |
|  b110 S212 MCD      limit=0.12                                         |
|  ... 3 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|[PENDING EXITS (2)]                                                     |
+========================================================================+
|  b0   ORPHAN XOM260814C00170000 x1 stop_loss (-100.0%)                 |
|  b279 S350 MSTR260814C00101000 x1 stop_loss (-66.7%)                   |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (19)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  DIS260814C00104000            1   +354.7%   $   +188.00               |
|  MARA260904C00010500           4    -43.5%   $    -80.00               |
|  META260817C00625000           4    -40.9%   $    -72.00               |
|  DIS260814C00106000           -1  -1241.2%   $    -70.33               |
|  ARM260814P00245000           -1   -196.0%   $    -49.00               |
|  MARA260911C00010500           2    -41.1%   $    -46.00               |
|  MARA260814P00009500          -1   -405.3%   $    -38.50               |
|  MSTR260821C00103000           4    -13.0%   $    -36.00               |
|  ... 11 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=85.4s reconcile=0.4s cancel=0.06s manage=10.25s scan=62.48s entries=8.06s
STATUS: options_morning_bot run complete (PAPER) elapsed=85.4s. run=#7100 https://github.com/28twagg-ops/TradingBot/actions/runs/31809387286
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 3 buckets closed trades, $-14.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 13.4% (345/2569) ALERT
# Options signal frequency

_Generated 2026-08-14T10:27:26.404402_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     7 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  1757 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=818 med=-47.5% | TAINTED n=1751 med=-39.0% | KEEP-only n=293 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=467.09 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T143052Z

- UTC timestamp: `20260814T143052Z`
- GitHub run: [#7101](https://github.com/28twagg-ops/TradingBot/actions/runs/31809796518)
- Run id: `31809796518`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`108s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 819 | 41.8 | -47.5 | +15.5 | $+8,201 |
| TAINTED | 1752 | 33.0 | -39.0 | +12.3 | $-9,247 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T10:30:56.864793-04:00","date":"2026-08-14","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":98.8,"phases_s":{"reconcile":0.25,"cancel":0.02,"manage":19.64,"protective_stops":0.31,"scan":72.84,"entries":4.77,"reconcile2":0.14},"signals":64,"placed":0,"equity":123425.2,"open_positions":20,"pending_orders":6,"open_lots":42,"submitted_today":48,"filled_today":42,"unattributed_contracts":0,"top_signals":["S165:MARA","S165:MSTR","S164:MARA","S164:MSTR","S168:MARA","S168:MSTR","S167:MARA","S167:MSTR"],"github_run":"7101","github_run_id":"31809796518","status":"ok","data_quality":{"clean":{"n":819,"win":41.76,"med":-47.45,"avg":15.47,"pnl":8200.53},"tainted":{"n":1752,"win":33.05,"med":-39.02,"avg":12.35,"pnl":-9247.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
14:30:53  INFO      Mode: exits
14:30:53  INFO        Daily log -> logs/daily/2026-08-14.md
14:30:53  INFO        Daily log reconciled -> logs/daily/2026-08-14.md (1 ledger rows)
14:30:53  INFO        place_all_stops: checking 3 positions...
14:30:53  INFO        STOP skipped AAPL: fractional (0.2288 shares) — software exit will handle it
14:30:53  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
14:30:53  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
14:30:54  INFO        [positions] 3/3 (3 valid)
14:30:54  INFO        Daily log -> logs/daily/2026-08-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.93|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.4%  $-0.28                                           HOLD|
|  AFL  P&L +0.7%  $+0.63                                            HOLD|
|  ACGL  P&L +1.2%  $+0.82                                           HOLD|
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
  open_lots=41 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T10:30:56.864793-04:00 ===

[Run context]
Paper auth OK — equity $123409.24, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+345.3%) SELL failed DIS260814C00104000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=1 already=13 failed=2

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 64 signal(s); top: ['S165:MARA', 'S165:MSTR', 'S164:MARA', 'S164:MSTR', 'S168:MARA', 'S168:MSTR', 'S167:MARA', 'S167:MSTR']
Paper lab: $123538 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  [b322 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b323 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  Skipped: 46 no tradeable call, 9 already attempted today, 20 pending order
Placed 0 new entry order(s).
Protective stops: placed=1 already=13 failed=2

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (entry+manage) --                                     |
|Equity       : $123,425.20                                              |
|Open Risk    : 42 lots (20 broker pos)                                  |
|Today's Run  : 64 signals -> 0 orders submitted                         |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 42 Active Lots | 6 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=819   win= 41.8%  med= -47.5%  $+8,201           |
|  TAINTED            n=1752  win= 33.0%  med= -39.0%  $-9,247           |
|  KEEP-only          n=294   win= 63.3%  med= +37.5%  $+5,699           |
|  KEEP recent        n=106   win= 58.5%  med= +50.0%  $+1,673           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b109 lab0109_s212_w1_0928..   0%  -77.5%    10                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
+========================================================================+
+========================================================================+
|[PENDING ORDERS (6)]                                                    |
+========================================================================+
|  Top groups: S398:MARA(2), S405:MARA(2), S212:MCD(2)                   |
|  ---------------------------------------------------------             |
|  b784 S398 MARA     limit=0.22                                         |
|  b785 S398 MARA     limit=0.22                                         |
|  b814 S405 MARA     limit=0.22                                         |
|  b815 S405 MARA     limit=0.22                                         |
|  b110 S212 MCD      limit=0.12                                         |
|  ... 1 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|[PENDING EXITS (1)]                                                     |
+========================================================================+
|  b0   ORPHAN XOM260814C00170000 x1 stop_loss (-100.0%)                 |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (20)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  DIS260814C00104000            1   +330.2%   $   +175.00               |
|  META260817C00625000           4    -47.7%   $    -84.00               |
|  MARA260904C00010500           4    -41.3%   $    -76.00               |
|  ARM260814P00245000           -1   -256.0%   $    -64.00               |
|  DIS260814C00106000           -1   -994.1%   $    -56.33               |
|  MARA260911C00010500           2    -39.3%   $    -44.00               |
|  META260817C00622500           2    -40.8%   $    -40.00               |
|  MARA260814P00009500          -1   -373.7%   $    -35.50               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=98.8s reconcile=0.25s cancel=0.02s manage=19.64s scan=72.84s entries=4.77s
STATUS: options_morning_bot run complete (PAPER) elapsed=98.8s. run=#7101 https://github.com/28twagg-ops/TradingBot/actions/runs/31809796518
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 4 buckets closed trades, $-15.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 13.4% (345/2571) ALERT
# Options signal frequency

_Generated 2026-08-14T10:32:41.611530_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |    42 | INFO |
| Total closed lots           |  1759 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=819 med=-47.5% | TAINTED n=1752 med=-39.0% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.92 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T143551Z

- UTC timestamp: `20260814T143551Z`
- GitHub run: [#7102](https://github.com/28twagg-ops/TradingBot/actions/runs/31810218050)
- Run id: `31810218050`
- Live bot: exit=`0`, duration=`5s`
- Options bot: exit=`0`, duration=`123s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 819 | 41.8 | -47.5 | +15.5 | $+8,201 |
| TAINTED | 1752 | 33.0 | -39.0 | +12.3 | $-9,247 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T10:35:58.459827-04:00","date":"2026-08-14","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":113.3,"phases_s":{"reconcile":0.51,"cancel":0.08,"manage":12.2,"protective_stops":1.78,"scan":86.47,"entries":9.22,"reconcile2":0.51},"signals":60,"placed":0,"equity":123916.62,"open_positions":20,"pending_orders":6,"open_lots":42,"submitted_today":48,"filled_today":42,"unattributed_contracts":0,"top_signals":["S165:MARA","S165:MSTR","S164:MARA","S164:MSTR","S168:MARA","S168:MSTR","S167:MARA","S167:MSTR"],"github_run":"7102","github_run_id":"31810218050","status":"ok","data_quality":{"clean":{"n":819,"win":41.76,"med":-47.45,"avg":15.47,"pnl":8200.53},"tainted":{"n":1752,"win":33.05,"med":-39.02,"avg":12.35,"pnl":-9247.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
14:35:52  INFO      Mode: exits
14:35:55  INFO        Daily log -> logs/daily/2026-08-14.md
14:35:55  INFO        Daily log reconciled -> logs/daily/2026-08-14.md (1 ledger rows)
14:35:55  INFO        place_all_stops: checking 3 positions...
14:35:55  INFO        STOP skipped AAPL: fractional (0.2288 shares) — software exit will handle it
14:35:55  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
14:35:55  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
14:35:56  INFO        [positions] 3/3 (3 valid)
14:35:56  INFO        Daily log -> logs/daily/2026-08-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.60|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.4%  $-0.31                                           HOLD|
|  AFL  P&L +0.5%  $+0.47                                            HOLD|
|  ACGL  P&L +1.0%  $+0.68                                           HOLD|
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
  open_lots=42 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T10:35:58.459827-04:00 ===

[Run context]
Paper auth OK — equity $123916.62, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
2026-08-14 10:36:05,048 INFO   EXIT [b263|lab0263_s403_w1_0928_1005_r2|S403] stop_loss (-52.3%) SELL 1 META260817C00625000 @<= 0.22
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+303.8%) SELL failed DIS260814C00104000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 already=14 failed=2

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 60 signal(s); top: ['S165:MARA', 'S165:MSTR', 'S164:MARA', 'S164:MSTR', 'S168:MARA', 'S168:MSTR', 'S167:MARA', 'S167:MSTR']
Paper lab: $124094 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  [b322 MARA] ENTRY failed: {"buy_limit_price":"0.39","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b323 MARA] ENTRY failed: {"buy_limit_price":"0.39","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  Skipped: 42 no tradeable call, 11 already attempted today, 18 pending order
Placed 0 new entry order(s).
Protective stops: placed=0 already=14 failed=2

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (entry+manage) --                                     |
|Equity       : $123,916.62                                              |
|Open Risk    : 42 lots (20 broker pos)                                  |
|Today's Run  : 60 signals -> 0 orders submitted                         |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 42 Active Lots | 6 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=819   win= 41.8%  med= -47.5%  $+8,201           |
|  TAINTED            n=1752  win= 33.0%  med= -39.0%  $-9,247           |
|  KEEP-only          n=294   win= 63.3%  med= +37.5%  $+5,699           |
|  KEEP recent        n=106   win= 58.5%  med= +50.0%  $+1,673           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b109 lab0109_s212_w1_0928..   0%  -77.5%    10                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
+========================================================================+
+========================================================================+
|[PENDING ORDERS (6)]                                                    |
+========================================================================+
|  Top groups: S398:MARA(2), S405:MARA(2), S212:MCD(2)                   |
|  ---------------------------------------------------------             |
|  b784 S398 MARA     limit=0.22                                         |
|  b785 S398 MARA     limit=0.22                                         |
|  b814 S405 MARA     limit=0.22                                         |
|  b815 S405 MARA     limit=0.22                                         |
|  b110 S212 MCD      limit=0.12                                         |
|  ... 1 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|[PENDING EXITS (2)]                                                     |
+========================================================================+
|  b0   ORPHAN XOM260814C00170000 x1 stop_loss (-100.0%)                 |
|  b263 S403 META260817C00625000 x1 stop_loss (-52.3%)                   |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (20)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  DIS260814C00104000            1   +320.8%   $   +170.00               |
|  META260817C00625000           4    -54.5%   $    -96.00               |
|  MARA260904C00010500           4    -41.3%   $    -76.00               |
|  DIS260814C00106000           -1   -888.2%   $    -50.33               |
|  ARM260814P00245000           -1   -196.0%   $    -49.00               |
|  META260817C00622500           2    -46.9%   $    -46.00               |
|  MARA260911C00010500           2    -39.3%   $    -44.00               |
|  MARA260814P00009500          -1   -342.1%   $    -32.50               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=113.3s reconcile=0.51s cancel=0.08s manage=12.2s scan=86.47s entries=9.22s
STATUS: options_morning_bot run complete (PAPER) elapsed=113.3s. run=#7102 https://github.com/28twagg-ops/TradingBot/actions/runs/31810218050
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 4 buckets closed trades, $-15.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 13.4% (345/2571) ALERT
# Options signal frequency

_Generated 2026-08-14T10:37:57.584253_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |    42 | INFO |
| Total closed lots           |  1759 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=819 med=-47.5% | TAINTED n=1752 med=-39.0% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.59 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T144048Z

- UTC timestamp: `20260814T144048Z`
- GitHub run: [#7103](https://github.com/28twagg-ops/TradingBot/actions/runs/31810632453)
- Run id: `31810632453`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`84s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 820 | 41.7 | -47.5 | +15.4 | $+8,180 |
| TAINTED | 1752 | 33.0 | -39.0 | +12.3 | $-9,247 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T10:40:52.932717-04:00","date":"2026-08-14","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":74.3,"phases_s":{"reconcile":0.3,"cancel":0.01,"manage":5.98,"protective_stops":0.31,"scan":61.98,"entries":4.32,"reconcile2":0.23},"signals":59,"placed":0,"equity":124165.2,"open_positions":20,"pending_orders":6,"open_lots":41,"submitted_today":48,"filled_today":42,"unattributed_contracts":0,"top_signals":["S165:MARA","S165:MSTR","S164:MARA","S164:MSTR","S168:MARA","S168:MSTR","S167:MARA","S167:MSTR"],"github_run":"7103","github_run_id":"31810632453","status":"ok","data_quality":{"clean":{"n":820,"win":41.71,"med":-47.48,"avg":15.39,"pnl":8179.53},"tainted":{"n":1752,"win":33.05,"med":-39.02,"avg":12.35,"pnl":-9247.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
14:40:49  INFO      Mode: exits
14:40:50  INFO        Daily log -> logs/daily/2026-08-14.md
14:40:50  INFO        Daily log reconciled -> logs/daily/2026-08-14.md (1 ledger rows)
14:40:50  INFO        place_all_stops: checking 3 positions...
14:40:50  INFO        STOP skipped AAPL: fractional (0.2288 shares) — software exit will handle it
14:40:50  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
14:40:50  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
14:40:50  INFO        [positions] 3/3 (3 valid)
14:40:50  INFO        Daily log -> logs/daily/2026-08-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.57|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.3%  $-0.22                                           HOLD|
|  AFL  P&L +0.4%  $+0.40                                            HOLD|
|  ACGL  P&L +0.9%  $+0.64                                           HOLD|
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
  open_lots=42 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T10:40:52.932717-04:00 ===

[Run context]
Paper auth OK — equity $124165.20, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
2026-08-14 10:40:55,560 INFO   EXIT [b262|lab0262_s403_w1_0928_1005_r1|S403] stop_loss (-54.5%) SELL 1 META260817C00625000 @<= 0.21
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+313.2%) SELL failed DIS260814C00104000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 already=14 failed=2

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 59 signal(s); top: ['S165:MARA', 'S165:MSTR', 'S164:MARA', 'S164:MSTR', 'S168:MARA', 'S168:MSTR', 'S167:MARA', 'S167:MSTR']
Paper lab: $124345 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  [b322 MARA] ENTRY failed: {"buy_limit_price":"0.44","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b323 MARA] ENTRY failed: {"buy_limit_price":"0.44","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  Skipped: 40 no tradeable call, 11 already attempted today, 18 pending order
Placed 0 new entry order(s).
Protective stops: placed=0 already=14 failed=2

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (entry+manage) --                                     |
|Equity       : $124,165.20                                              |
|Open Risk    : 41 lots (20 broker pos)                                  |
|Today's Run  : 59 signals -> 0 orders submitted                         |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 41 Active Lots | 6 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=820   win= 41.7%  med= -47.5%  $+8,180           |
|  TAINTED            n=1752  win= 33.0%  med= -39.0%  $-9,247           |
|  KEEP-only          n=294   win= 63.3%  med= +37.5%  $+5,699           |
|  KEEP recent        n=106   win= 58.5%  med= +50.0%  $+1,673           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b109 lab0109_s212_w1_0928..   0%  -77.5%    10                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
+========================================================================+
+========================================================================+
|[PENDING ORDERS (6)]                                                    |
+========================================================================+
|  Top groups: S398:MARA(2), S405:MARA(2), S212:MCD(2)                   |
|  ---------------------------------------------------------             |
|  b784 S398 MARA     limit=0.22                                         |
|  b785 S398 MARA     limit=0.22                                         |
|  b814 S405 MARA     limit=0.22                                         |
|  b815 S405 MARA     limit=0.22                                         |
|  b110 S212 MCD      limit=0.12                                         |
|  ... 1 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|[PENDING EXITS (2)]                                                     |
+========================================================================+
|  b0   ORPHAN XOM260814C00170000 x1 stop_loss (-100.0%)                 |
|  b262 S403 META260817C00625000 x1 stop_loss (-54.5%)                   |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (20)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  DIS260814C00104000            1   +313.2%   $   +166.00               |
|  MARA260904C00010500           4    -41.3%   $    -76.00               |
|  META260817C00625000           3    -54.5%   $    -72.00               |
|  DIS260814C00106000           -1  -1170.6%   $    -66.33               |
|  ARM260814P00245000           -1   -196.0%   $    -49.00               |
|  META260817C00622500           2    -49.0%   $    -48.00               |
|  MARA260911C00010500           2    -39.3%   $    -44.00               |
|  MSTR260821C00103000           4    -13.0%   $    -36.00               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=74.3s reconcile=0.3s cancel=0.01s manage=5.98s scan=61.98s entries=4.32s
STATUS: options_morning_bot run complete (PAPER) elapsed=74.3s. run=#7103 https://github.com/28twagg-ops/TradingBot/actions/runs/31810632453
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 5 buckets closed trades, $-36.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 13.4% (345/2572) ALERT
# Options signal frequency

_Generated 2026-08-14T10:42:12.942091_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |    41 | INFO |
| Total closed lots           |  1760 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=820 med=-47.5% | TAINTED n=1752 med=-39.0% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.58 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260814T144549Z

- UTC timestamp: `20260814T144549Z`
- GitHub run: [#7104](https://github.com/28twagg-ops/TradingBot/actions/runs/31811056170)
- Run id: `31811056170`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`97s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 820 | 41.7 | -47.5 | +15.4 | $+8,180 |
| TAINTED | 1753 | 33.0 | -39.0 | +12.3 | $-9,262 |
| KEEP-only | 294 | 63.3 | +37.5 | +42.9 | $+5,699 |
| KEEP-only recent | 106 | 58.5 | +50.0 | +54.8 | $+1,673 |

- KEEP strategies (10): S173, S174, S210, S218, S350, S397, S398, S401, S404, S406
- KILL strategies (16): ORPHAN, S165, S203, S207, S211, S212, S217, S351, S354, S355, S360, S364, S403, S405, S407, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-14T10:45:53.559373-04:00","date":"2026-08-14","mode":"entry+manage","header":"entry+manage (11 new)","elapsed_s":86.7,"phases_s":{"reconcile":0.13,"cancel":0.02,"manage":3.51,"protective_stops":0.53,"scan":72.01,"entries":8.67,"reconcile2":0.5},"signals":61,"placed":11,"equity":123936.15,"open_positions":20,"pending_orders":8,"open_lots":47,"submitted_today":59,"filled_today":51,"unattributed_contracts":0,"top_signals":["S165:MARA","S165:MSTR","S164:MARA","S164:MSTR","S168:MARA","S168:MSTR","S167:MARA","S167:MSTR"],"github_run":"7104","github_run_id":"31811056170","status":"ok","data_quality":{"clean":{"n":820,"win":41.71,"med":-47.48,"avg":15.39,"pnl":8179.53},"tainted":{"n":1753,"win":33.03,"med":-39.02,"avg":12.3,"pnl":-9262.34},"keep_only":{"n":294,"win":63.27,"med":37.5,"avg":42.89,"pnl":5699.45},"keep_only_recent":{"n":106,"win":58.49,"med":50.0,"avg":54.78,"pnl":1673.0},"keep_strategies":["S173","S174","S210","S218","S350","S397","S398","S401","S404","S406"],"kill_strategies":["ORPHAN","S165","S203","S207","S211","S212","S217","S351","S354","S355","S360","S364","S403","S405","S407","S408"]}}
```

### Live bot full output

```text
14:45:50  INFO      Mode: exits
14:45:50  INFO        Daily log -> logs/daily/2026-08-14.md
14:45:50  INFO        Daily log reconciled -> logs/daily/2026-08-14.md (1 ledger rows)
14:45:50  INFO        place_all_stops: checking 3 positions...
14:45:50  INFO        STOP skipped AAPL: fractional (0.2288 shares) — software exit will handle it
14:45:50  INFO        STOP skipped ACGL: fractional (0.7073 shares) — software exit will handle it
14:45:50  INFO        STOP skipped AFL: fractional (0.7729 shares) — software exit will handle it
14:45:51  INFO        [positions] 3/3 (3 valid)
14:45:51  INFO        Daily log -> logs/daily/2026-08-14.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.72|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AAPL  P&L -0.3%  $-0.22                                           HOLD|
|  AFL  P&L +0.5%  $+0.51                                            HOLD|
|  ACGL  P&L +1.0%  $+0.67                                           HOLD|
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
  open_lots=41 paper_keys=yes dry_run=False
  alpaca positions=21
  FLAG b265|S403|ce27dcf6 missing from Alpaca
  FLAG b264|S403|6ee11340 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-14T10:45:53.559373-04:00 ===

[Run context]
Paper auth OK — equity $123936.15, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+318.9%) SELL failed DIS260814C00104000: {"code":40310000,"message":"account not eligible to trade uncovered option contracts"}
Protective stops: placed=0 already=13 failed=2

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 61 signal(s); top: ['S165:MARA', 'S165:MSTR', 'S164:MARA', 'S164:MSTR', 'S168:MARA', 'S168:MSTR', 'S167:MARA', 'S167:MSTR']
Paper lab: $123893 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  [b98 SLB] ENTRY failed: {"buy_limit_price":"0.43","code":40310000,"existing_order_id":"ba3a9288-f9ba-4516-84f5-746c9389767d","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b99 SLB] ENTRY failed: {"buy_limit_price":"0.43","code":40310000,"existing_order_id":"ba3a9288-f9ba-4516-84f5-746c9389767d","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b113 DKNG] ENTRY failed: {"buy_limit_price":"0.5","code":40310000,"existing_order_id":"74fdbdeb-357e-4b5e-9736-5a0aa5cbf691","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.18"}
  [b322 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b323 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b324 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b325 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"777a1d0e-df63-4958-95f8-63bf3b7bead4","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.19"}
  [b780 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"35321683-9f63-4281-90b8-2c2ce154d9e7","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.21"}
  [b781 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"35321683-9f63-4281-90b8-2c2ce154d9e7","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.21"}
  [b780 MSTR] ENTRY failed: {"buy_limit_price":"0.62","code":40310000,"existing_order_id":"e934d619-cf52-451a-b83d-df862c9d22be","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.31"}
  [b781 MSTR] ENTRY failed: {"buy_limit_price":"0.62","code":40310000,"existing_order_id":"e934d619-cf52-451a-b83d-df862c9d22be","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.31"}
  [b796 MARA] ENTRY failed: {"buy_limit_price":"0.14","code":40310000,"existing_order_id":"41dc4546-299e-49a6-9a52-dbbbb7cf9fed","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.06"}
  [b797 MARA] ENTRY failed: {"buy_limit_price":"0.14","code":40310000,"existing_order_id":"41dc4546-299e-49a6-9a52-dbbbb7cf9fed","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.06"}
  [b796 MSTR] ENTRY failed: {"buy_limit_price":"0.43","code":40310000,"existing_order_id":"de5df230-ce8f-4731-b321-016b9a532c84","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.24"}
  [b797 MSTR] ENTRY failed: {"buy_limit_price":"0.43","code":40310000,"existing_order_id":"de5df230-ce8f-4731-b321-016b9a532c84","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.24"}
  [b804 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"35321683-9f63-4281-90b8-2c2ce154d9e7","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.21"}
  [b805 MARA] ENTRY failed: {"buy_limit_price":"0.42","code":40310000,"existing_order_id":"35321683-9f63-4281-90b8-2c2ce154d9e7","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.21"}
  [b804 MSTR] ENTRY failed: {"buy_limit_price":"0.62","code":40310000,"existing_order_id":"e934d619-cf52-451a-b83d-df862c9d22be","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.31"}
  [b805 MSTR] ENTRY failed: {"buy_limit_price":"0.62","code":40310000,"existing_order_id":"e934d619-cf52-451a-b83d-df862c9d22be","message":"potential wash trade detected. use complex orders","reject_reason":"sell order exists, buy limit price should be less than existing sell limit price","sell_limit_price":"0.31"}
  Skipped: 87 no tradeable call, 11 already attempted today, 35 pending order
Placed 11 new entry order(s).
Protective stops: placed=1 already=13 failed=2

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (entry+manage) --                                     |
|Equity       : $123,936.15                                              |
|Open Risk    : 47 lots (20 broker pos)                                  |
|Today's Run  : 61 signals -> 11 orders submitted                        |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 0 (Ledger is clean)                                      |
|Lab Status   : 47 Active Lots | 8 Pending Orders                        |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=820   win= 41.7%  med= -47.5%  $+8,180           |
|  TAINTED            n=1753  win= 33.0%  med= -39.0%  $-9,262           |
|  KEEP-only          n=294   win= 63.3%  med= +37.5%  $+5,699           |
|  KEEP recent        n=106   win= 58.5%  med= +50.0%  $+1,673           |
|  KEEP(10): S173,S174,S210,S218,S350,S397,S398,S401...                  |
|  KILL(16): ORPHAN,S165,S203,S207,S211,S212,S217,S351...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  82%  +126.9%    11                       |
|  b238 lab0238_s401_w3_1045..  80%  +109.5%    15                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b109 lab0109_s212_w1_0928..   0%  -77.5%    10                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.4%    15                        |
+========================================================================+
+========================================================================+
|[PENDING ORDERS (8)]                                                    |
+========================================================================+
|  Top groups: S405:MARA(3), S398:MARA(2), S212:MCD(2)                   |
|  ---------------------------------------------------------             |
|  b784 S398 MARA     limit=0.22                                         |
|  b785 S398 MARA     limit=0.22                                         |
|  b814 S405 MARA     limit=0.22                                         |
|  b815 S405 MARA     limit=0.22                                         |
|  b110 S212 MCD      limit=0.12                                         |
|  ... 3 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|[PENDING EXITS (2)]                                                     |
+========================================================================+
|  b0   ORPHAN XOM260814C00170000 x1 stop_loss (-100.0%)                 |
|  b262 S403 META260817C00625000 x1 stop_loss (-54.5%)                   |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (20)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  DIS260814C00104000            1   +318.9%   $   +169.00               |
|  MARA260904C00010500           4    -43.5%   $    -80.00               |
|  META260817C00625000           3    -59.1%   $    -78.00               |
|  DIS260814C00106000           -1  -1258.8%   $    -71.33               |
|  ARM260814P00245000           -1   -256.0%   $    -64.00               |
|  MSTR260821C00103000           4    -20.3%   $    -56.00               |
|  MARA260821C00009500          20     -9.1%   $    -44.00               |
|  MARA260911C00010500           2    -39.3%   $    -44.00               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-14.log
elapsed=86.7s reconcile=0.13s cancel=0.02s manage=3.51s scan=72.01s entries=8.67s
STATUS: options_morning_bot run complete (PAPER) elapsed=86.7s. run=#7104 https://github.com/28twagg-ops/TradingBot/actions/runs/31811056170
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_buckets.csv
Summary: 5 buckets closed trades, $-36.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 13.4% (345/2573) ALERT
# Options signal frequency

_Generated 2026-08-14T10:47:26.117500_

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
## Ledger health — 2026-08-14
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   678 | WARN | <<<
| Missing exit records (post) |   678 | WARN | <<<
| State/ledger mismatches     |     8 | WARN | <<<
| Total open lots             |    47 | INFO |
| Total closed lots           |  1761 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-14_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=820 med=-47.5% | TAINTED n=1753 med=-39.0% | KEEP-only n=294 med=+37.5% | KILL=16 KEEP=10
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.72 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
