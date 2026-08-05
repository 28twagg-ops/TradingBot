# Daily Comprehensive Action Review — 2026-08-05

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260805T010224Z

- UTC timestamp: `20260805T010224Z`
- GitHub run: [#6100](https://github.com/28twagg-ops/TradingBot/actions/runs/30965143503)
- Run id: `30965143503`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T21:02:28.606763-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.48},"signals":0,"placed":0,"equity":144868.54,"open_positions":34,"pending_orders":0,"open_lots":201,"submitted_today":184,"filled_today":323,"unattributed_contracts":15,"top_signals":[],"github_run":"6100","github_run_id":"30965143503","status":"ok"}
```

### Live bot full output

```text
01:02:25  INFO      Mode: summary
01:02:26  INFO        Daily log -> logs/daily/2026-08-05.md
01:02:26  INFO        Daily log reconciled -> logs/daily/2026-08-05.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:02 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.46|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $474.46|
|  Cash                                                           $286.31|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.15|
|  Open P&L                                                        $+0.87|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.50     $14.70   $14.67   -0.1%   $-0.14  |
|  AVB      Pullback50      $94.64     $187.24  $189.25  +1.1%   $+1.00  |
|                                                                        |
|  Total invested                                                 $188.15|
|  Total open P&L                                                  $+0.87|
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
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
|  2026-08-04  SELL  ALGN  Pullback50  $92.57  P&L $-0.62                |
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=201 paper_keys=yes dry_run=False
  alpaca positions=36
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T21:02:28.606763-04:00 ===

[Run context]
After hours (21:02 ET) — exit summary only.
Paper auth OK — equity $144868.54, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $144,868.54                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    184                                     |
|  Orders filled today (ledger)  323                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             201                                     |
|  Broker option positions       34                                      |
|  Unattributed contracts        15 (orphan reconcile)                   |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=733  buckets=224  win=53%                            |
|  Returns   avg=+35.4%  med=+13.0%  p10=-66.2%  p90=+163.0%             |
|  Realized  $+13,667.61                                                 |
|  Raw incl dropped  trades=1267  real=$+12,072.06                       |
|  Today     trades=111  avg=+23.1%  med=+37.5%  real=$+176.00           |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  2 100% +654.7 +654.7 +906.2 $   +274         |
|  b197 lab0197_s218_w3_10  2 100% +528.1 +528.1 +737.5 $   +220         |
|  b844 lab0844_s407_w2_10  3 100% +312.4 +446.1 +446.1 $   +138         |
|  b845 lab0845_s407_w2_10  3 100% +271.7 +353.3 +423.1 $   +127         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  1 100% +320.0 +320.0 +320.0 $    +80         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  3 100% +201.5 +273.1 +273.1 $   +177         |
|  ... 216 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  2   0% -95.9 -95.9 -95.9 $    -94       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (34)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -23.2%   $   -327.22               |
|  OXY260807C00058000            7    -54.7%   $   -262.35               |
|  NKE260807C00042000           10    -32.9%   $   -211.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  SMCI260807P00027500           5    -78.3%   $   -180.00               |
|  AMZN260807C00297500          12    -42.0%   $   -173.67               |
|  AMZN260805C00287500          17    -29.5%   $   -171.00               |
|  AMZN260805C00290000          11    -55.2%   $   -162.33               |
|  ... 26 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-04.log
elapsed=1.0s reconcile=0.48s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.0s. run=#6100 https://github.com/28twagg-ops/TradingBot/actions/runs/30965143503
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.csv
Summary: 60 buckets closed trades, $+176.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.csv
Summary: keep=0 watch=101 drop=4
Orphan rate: 3.7% (47/1267)
# Options signal frequency

_Generated 2026-08-04T21:02:35.106025_

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
## Ledger health — 2026-08-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   201 | INFO |
| Total closed lots           |   753 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.46 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260805T014535Z

- UTC timestamp: `20260805T014535Z`
- GitHub run: [#6101](https://github.com/28twagg-ops/TradingBot/actions/runs/30967308695)
- Run id: `30967308695`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-04T21:45:39.594182-04:00","date":"2026-08-04","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.61},"signals":0,"placed":0,"equity":144992.54,"open_positions":34,"pending_orders":0,"open_lots":201,"submitted_today":184,"filled_today":323,"unattributed_contracts":15,"top_signals":[],"github_run":"6101","github_run_id":"30967308695","status":"ok"}
```

### Live bot full output

```text
01:45:36  INFO      Mode: summary
01:45:37  INFO        Daily log -> logs/daily/2026-08-05.md
01:45:37  INFO        Daily log reconciled -> logs/daily/2026-08-05.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.46|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $474.46|
|  Cash                                                           $286.31|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.15|
|  Open P&L                                                        $+0.87|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.50     $14.70   $14.67   -0.1%   $-0.14  |
|  AVB      Pullback50      $94.64     $187.24  $189.25  +1.1%   $+1.00  |
|                                                                        |
|  Total invested                                                 $188.15|
|  Total open P&L                                                  $+0.87|
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
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
|  2026-08-04  SELL  ALGN  Pullback50  $92.57  P&L $-0.62                |
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=201 paper_keys=yes dry_run=False
  alpaca positions=36
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-04T21:45:39.594182-04:00 ===

[Run context]
After hours (21:45 ET) — exit summary only.
Paper auth OK — equity $144992.54, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $144,992.54                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    184                                     |
|  Orders filled today (ledger)  323                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             201                                     |
|  Broker option positions       34                                      |
|  Unattributed contracts        15 (orphan reconcile)                   |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=733  buckets=224  win=53%                            |
|  Returns   avg=+35.4%  med=+13.0%  p10=-66.2%  p90=+163.0%             |
|  Realized  $+13,667.61                                                 |
|  Raw incl dropped  trades=1267  real=$+12,072.06                       |
|  Today     trades=111  avg=+23.1%  med=+37.5%  real=$+176.00           |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  2 100% +654.7 +654.7 +906.2 $   +274         |
|  b197 lab0197_s218_w3_10  2 100% +528.1 +528.1 +737.5 $   +220         |
|  b844 lab0844_s407_w2_10  3 100% +312.4 +446.1 +446.1 $   +138         |
|  b845 lab0845_s407_w2_10  3 100% +271.7 +353.3 +423.1 $   +127         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  1 100% +320.0 +320.0 +320.0 $    +80         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  3 100% +201.5 +273.1 +273.1 $   +177         |
|  ... 216 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  2   0% -95.9 -95.9 -95.9 $    -94       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (34)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -23.2%   $   -327.22               |
|  OXY260807C00058000            7    -54.7%   $   -262.35               |
|  NKE260807C00042000           10    -32.9%   $   -211.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  SMCI260807P00027500           5    -78.3%   $   -180.00               |
|  AMZN260807C00297500          12    -42.0%   $   -173.67               |
|  AMZN260805C00287500          17    -29.5%   $   -171.00               |
|  AMZN260805C00290000          11    -55.2%   $   -162.33               |
|  ... 26 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-04.log
elapsed=1.2s reconcile=0.61s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.2s. run=#6101 https://github.com/28twagg-ops/TradingBot/actions/runs/30967308695
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_buckets.csv
Summary: 60 buckets closed trades, $+176.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-04_strategy_selection.csv
Summary: keep=0 watch=101 drop=4
Orphan rate: 3.7% (47/1267)
# Options signal frequency

_Generated 2026-08-04T21:45:46.236290_

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
## Ledger health — 2026-08-04
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   201 | INFO |
| Total closed lots           |   753 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.46 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260805T044927Z

- UTC timestamp: `20260805T044927Z`
- GitHub run: [#6102](https://github.com/28twagg-ops/TradingBot/actions/runs/30976208881)
- Run id: `30976208881`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-05T00:49:30.121978-04:00","date":"2026-08-05","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":145220.54,"open_positions":34,"pending_orders":0,"open_lots":201,"submitted_today":0,"filled_today":0,"unattributed_contracts":15,"top_signals":[],"github_run":"6102","github_run_id":"30976208881","status":"ok"}
```

### Live bot full output

```text
04:49:27  INFO      Mode: summary
04:49:28  INFO        Daily log -> logs/daily/2026-08-05.md
04:49:28  INFO        Daily log reconciled -> logs/daily/2026-08-05.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         04:49 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.46|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $474.46|
|  Cash                                                           $286.31|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.15|
|  Open P&L                                                        $+0.87|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.50     $14.70   $14.67   -0.1%   $-0.14  |
|  AVB      Pullback50      $94.64     $187.24  $189.25  +1.1%   $+1.00  |
|                                                                        |
|  Total invested                                                 $188.15|
|  Total open P&L                                                  $+0.87|
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
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
|  2026-08-04  SELL  ALGN  Pullback50  $92.57  P&L $-0.62                |
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=201 paper_keys=yes dry_run=False
  alpaca positions=36
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-05T00:49:30.121978-04:00 ===

[Run context]
After hours (00:49 ET) — exit summary only.
Paper auth OK — equity $145220.54, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $145,220.54                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             201                                     |
|  Broker option positions       34                                      |
|  Unattributed contracts        15 (orphan reconcile)                   |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=733  buckets=224  win=53%                            |
|  Returns   avg=+35.4%  med=+13.0%  p10=-66.2%  p90=+163.0%             |
|  Realized  $+13,667.61                                                 |
|  Raw incl dropped  trades=1267  real=$+12,072.06                       |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  2 100% +654.7 +654.7 +906.2 $   +274         |
|  b197 lab0197_s218_w3_10  2 100% +528.1 +528.1 +737.5 $   +220         |
|  b844 lab0844_s407_w2_10  3 100% +312.4 +446.1 +446.1 $   +138         |
|  b845 lab0845_s407_w2_10  3 100% +271.7 +353.3 +423.1 $   +127         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  1 100% +320.0 +320.0 +320.0 $    +80         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  3 100% +201.5 +273.1 +273.1 $   +177         |
|  ... 216 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  2   0% -95.9 -95.9 -95.9 $    -94       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (34)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -23.2%   $   -327.22               |
|  OXY260807C00058000            7    -54.7%   $   -262.35               |
|  NKE260807C00042000           10    -32.9%   $   -211.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  SMCI260807P00027500           5    -78.3%   $   -180.00               |
|  AMZN260807C00297500          12    -42.0%   $   -173.67               |
|  AMZN260805C00287500          17    -29.5%   $   -171.00               |
|  AMZN260805C00290000          11    -55.2%   $   -162.33               |
|  ... 26 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-05.log
elapsed=0.5s reconcile=0.11s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.5s. run=#6102 https://github.com/28twagg-ops/TradingBot/actions/runs/30976208881
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.csv
Summary: keep=0 watch=101 drop=4
Orphan rate: 3.7% (47/1267)
# Options signal frequency

_Generated 2026-08-05T00:49:35.989140_

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
## Ledger health — 2026-08-05
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   201 | INFO |
| Total closed lots           |   753 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.46 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260805T130052Z

- UTC timestamp: `20260805T130052Z`
- GitHub run: [#6103](https://github.com/28twagg-ops/TradingBot/actions/runs/31008133578)
- Run id: `31008133578`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-05T09:00:55.747363-04:00","date":"2026-08-05","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.24},"signals":0,"placed":0,"equity":144094.98,"open_positions":34,"pending_orders":0,"open_lots":201,"submitted_today":0,"filled_today":0,"unattributed_contracts":15,"top_signals":[],"github_run":"6103","github_run_id":"31008133578","status":"ok"}
```

### Live bot full output

```text
13:00:53  INFO      Mode: summary
13:00:53  INFO        Daily log -> logs/daily/2026-08-05.md
13:00:53  INFO        Daily log reconciled -> logs/daily/2026-08-05.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.43|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $474.43|
|  Cash                                                           $286.31|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.12|
|  Open P&L                                                        $+0.84|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.86     $14.70   $14.73   +0.2%   $+0.22  |
|  AVB      Pullback50      $94.27     $187.24  $188.50  +0.7%   $+0.63  |
|                                                                        |
|  Total invested                                                 $188.12|
|  Total open P&L                                                  $+0.84|
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
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
|  2026-08-04  SELL  ALGN  Pullback50  $92.57  P&L $-0.62                |
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=201 paper_keys=yes dry_run=False
  alpaca positions=36
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-05T09:00:55.747363-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $144094.98, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $144,094.98                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             201                                     |
|  Broker option positions       34                                      |
|  Unattributed contracts        15 (orphan reconcile)                   |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=733  buckets=224  win=53%                            |
|  Returns   avg=+35.4%  med=+13.0%  p10=-66.2%  p90=+163.0%             |
|  Realized  $+13,667.61                                                 |
|  Raw incl dropped  trades=1267  real=$+12,072.06                       |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  2 100% +654.7 +654.7 +906.2 $   +274         |
|  b197 lab0197_s218_w3_10  2 100% +528.1 +528.1 +737.5 $   +220         |
|  b844 lab0844_s407_w2_10  3 100% +312.4 +446.1 +446.1 $   +138         |
|  b845 lab0845_s407_w2_10  3 100% +271.7 +353.3 +423.1 $   +127         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  1 100% +320.0 +320.0 +320.0 $    +80         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  3 100% +201.5 +273.1 +273.1 $   +177         |
|  ... 216 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  2   0% -95.9 -95.9 -95.9 $    -94       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (34)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -23.1%   $   -326.67               |
|  OXY260807C00058000            7    -54.7%   $   -262.35               |
|  NKE260807C00042000           10    -32.9%   $   -211.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  SMCI260807P00027500           5    -78.3%   $   -180.00               |
|  AMZN260805C00287500          17    -29.2%   $   -168.30               |
|  AMZN260807C00297500          12    -41.0%   $   -167.08               |
|  AMZN260805C00290000          11    -55.4%   $   -164.15               |
|  ... 26 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-05.log
elapsed=0.7s reconcile=0.24s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.7s. run=#6103 https://github.com/28twagg-ops/TradingBot/actions/runs/31008133578
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.csv
Summary: keep=0 watch=101 drop=4
Orphan rate: 3.7% (47/1267)
# Options signal frequency

_Generated 2026-08-05T09:01:01.990852_

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
## Ledger health — 2026-08-05
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   201 | INFO |
| Total closed lots           |   753 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.43 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260805T130552Z

- UTC timestamp: `20260805T130552Z`
- GitHub run: [#6104](https://github.com/28twagg-ops/TradingBot/actions/runs/31008526504)
- Run id: `31008526504`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-05T09:05:56.957874-04:00","date":"2026-08-05","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.29},"signals":0,"placed":0,"equity":143942.14,"open_positions":34,"pending_orders":0,"open_lots":201,"submitted_today":0,"filled_today":0,"unattributed_contracts":15,"top_signals":[],"github_run":"6104","github_run_id":"31008526504","status":"ok"}
```

### Live bot full output

```text
13:05:54  INFO      Mode: summary
13:05:55  INFO        Daily log -> logs/daily/2026-08-05.md
13:05:55  INFO        Daily log reconciled -> logs/daily/2026-08-05.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.43|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $474.43|
|  Cash                                                           $286.31|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.12|
|  Open P&L                                                        $+0.84|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.86     $14.70   $14.73   +0.2%   $+0.22  |
|  AVB      Pullback50      $94.27     $187.24  $188.50  +0.7%   $+0.63  |
|                                                                        |
|  Total invested                                                 $188.12|
|  Total open P&L                                                  $+0.84|
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
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
|  2026-08-04  SELL  ALGN  Pullback50  $92.57  P&L $-0.62                |
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=201 paper_keys=yes dry_run=False
  alpaca positions=36
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-05T09:05:56.957874-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $143942.14, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,942.14                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             201                                     |
|  Broker option positions       34                                      |
|  Unattributed contracts        15 (orphan reconcile)                   |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=733  buckets=224  win=53%                            |
|  Returns   avg=+35.4%  med=+13.0%  p10=-66.2%  p90=+163.0%             |
|  Realized  $+13,667.61                                                 |
|  Raw incl dropped  trades=1267  real=$+12,072.06                       |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  2 100% +654.7 +654.7 +906.2 $   +274         |
|  b197 lab0197_s218_w3_10  2 100% +528.1 +528.1 +737.5 $   +220         |
|  b844 lab0844_s407_w2_10  3 100% +312.4 +446.1 +446.1 $   +138         |
|  b845 lab0845_s407_w2_10  3 100% +271.7 +353.3 +423.1 $   +127         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  1 100% +320.0 +320.0 +320.0 $    +80         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  3 100% +201.5 +273.1 +273.1 $   +177         |
|  ... 216 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  2   0% -95.9 -95.9 -95.9 $    -94       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (34)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -23.1%   $   -326.67               |
|  OXY260807C00058000            7    -54.7%   $   -262.35               |
|  NKE260807C00042000           10    -32.9%   $   -211.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  SMCI260807P00027500           5    -78.3%   $   -180.00               |
|  AMZN260805C00287500          17    -29.2%   $   -168.30               |
|  AMZN260807C00297500          12    -41.0%   $   -167.08               |
|  AMZN260805C00290000          11    -55.4%   $   -164.15               |
|  ... 26 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-05.log
elapsed=0.6s reconcile=0.29s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.6s. run=#6104 https://github.com/28twagg-ops/TradingBot/actions/runs/31008526504
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.csv
Summary: keep=0 watch=101 drop=4
Orphan rate: 3.7% (47/1267)
# Options signal frequency

_Generated 2026-08-05T09:06:01.333914_

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
## Ledger health — 2026-08-05
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   201 | INFO |
| Total closed lots           |   753 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.43 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260805T131045Z

- UTC timestamp: `20260805T131045Z`
- GitHub run: [#6105](https://github.com/28twagg-ops/TradingBot/actions/runs/31008925219)
- Run id: `31008925219`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-05T09:10:49.978672-04:00","date":"2026-08-05","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.49},"signals":0,"placed":0,"equity":143522.98,"open_positions":34,"pending_orders":0,"open_lots":201,"submitted_today":0,"filled_today":0,"unattributed_contracts":15,"top_signals":[],"github_run":"6105","github_run_id":"31008925219","status":"ok"}
```

### Live bot full output

```text
13:10:46  INFO      Mode: summary
13:10:47  INFO        Daily log -> logs/daily/2026-08-05.md
13:10:47  INFO        Daily log reconciled -> logs/daily/2026-08-05.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.43|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $474.43|
|  Cash                                                           $286.31|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.12|
|  Open P&L                                                        $+0.84|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.86     $14.70   $14.73   +0.2%   $+0.22  |
|  AVB      Pullback50      $94.27     $187.24  $188.50  +0.7%   $+0.63  |
|                                                                        |
|  Total invested                                                 $188.12|
|  Total open P&L                                                  $+0.84|
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
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
|  2026-08-04  SELL  ALGN  Pullback50  $92.57  P&L $-0.62                |
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=201 paper_keys=yes dry_run=False
  alpaca positions=36
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-05T09:10:49.978672-04:00 ===

[Run context]
After hours (09:10 ET) — exit summary only.
Paper auth OK — equity $143522.98, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,522.98                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             201                                     |
|  Broker option positions       34                                      |
|  Unattributed contracts        15 (orphan reconcile)                   |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=733  buckets=224  win=53%                            |
|  Returns   avg=+35.4%  med=+13.0%  p10=-66.2%  p90=+163.0%             |
|  Realized  $+13,667.61                                                 |
|  Raw incl dropped  trades=1267  real=$+12,072.06                       |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  2 100% +654.7 +654.7 +906.2 $   +274         |
|  b197 lab0197_s218_w3_10  2 100% +528.1 +528.1 +737.5 $   +220         |
|  b844 lab0844_s407_w2_10  3 100% +312.4 +446.1 +446.1 $   +138         |
|  b845 lab0845_s407_w2_10  3 100% +271.7 +353.3 +423.1 $   +127         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  1 100% +320.0 +320.0 +320.0 $    +80         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  3 100% +201.5 +273.1 +273.1 $   +177         |
|  ... 216 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  2   0% -95.9 -95.9 -95.9 $    -94       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (34)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -23.1%   $   -326.67               |
|  OXY260807C00058000            7    -54.7%   $   -262.35               |
|  NKE260807C00042000           10    -32.9%   $   -211.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  SMCI260807P00027500           5    -78.3%   $   -180.00               |
|  AMZN260805C00287500          17    -29.2%   $   -168.30               |
|  AMZN260807C00297500          12    -41.0%   $   -167.08               |
|  AMZN260805C00290000          11    -55.4%   $   -164.15               |
|  ... 26 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-05.log
elapsed=1.0s reconcile=0.49s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.0s. run=#6105 https://github.com/28twagg-ops/TradingBot/actions/runs/31008925219
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.csv
Summary: keep=0 watch=101 drop=4
Orphan rate: 3.7% (47/1267)
# Options signal frequency

_Generated 2026-08-05T09:10:56.603338_

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
## Ledger health — 2026-08-05
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   201 | INFO |
| Total closed lots           |   753 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.43 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260805T131538Z

- UTC timestamp: `20260805T131538Z`
- GitHub run: [#6106](https://github.com/28twagg-ops/TradingBot/actions/runs/31009313744)
- Run id: `31009313744`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-05T09:15:41.773018-04:00","date":"2026-08-05","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.21},"signals":0,"placed":0,"equity":143282.98,"open_positions":34,"pending_orders":0,"open_lots":201,"submitted_today":0,"filled_today":0,"unattributed_contracts":15,"top_signals":[],"github_run":"6106","github_run_id":"31009313744","status":"ok"}
```

### Live bot full output

```text
13:15:39  INFO      Mode: summary
13:15:39  INFO        Daily log -> logs/daily/2026-08-05.md
13:15:39  INFO        Daily log reconciled -> logs/daily/2026-08-05.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.43|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $474.43|
|  Cash                                                           $286.31|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.12|
|  Open P&L                                                        $+0.84|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.86     $14.70   $14.73   +0.2%   $+0.22  |
|  AVB      Pullback50      $94.27     $187.24  $188.50  +0.7%   $+0.63  |
|                                                                        |
|  Total invested                                                 $188.12|
|  Total open P&L                                                  $+0.84|
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
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
|  2026-08-04  SELL  ALGN  Pullback50  $92.57  P&L $-0.62                |
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=201 paper_keys=yes dry_run=False
  alpaca positions=36
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-05T09:15:41.773018-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $143282.98, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,282.98                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             201                                     |
|  Broker option positions       34                                      |
|  Unattributed contracts        15 (orphan reconcile)                   |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=733  buckets=224  win=53%                            |
|  Returns   avg=+35.4%  med=+13.0%  p10=-66.2%  p90=+163.0%             |
|  Realized  $+13,667.61                                                 |
|  Raw incl dropped  trades=1267  real=$+12,072.06                       |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  2 100% +654.7 +654.7 +906.2 $   +274         |
|  b197 lab0197_s218_w3_10  2 100% +528.1 +528.1 +737.5 $   +220         |
|  b844 lab0844_s407_w2_10  3 100% +312.4 +446.1 +446.1 $   +138         |
|  b845 lab0845_s407_w2_10  3 100% +271.7 +353.3 +423.1 $   +127         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  1 100% +320.0 +320.0 +320.0 $    +80         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  3 100% +201.5 +273.1 +273.1 $   +177         |
|  ... 216 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  2   0% -95.9 -95.9 -95.9 $    -94       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (34)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -23.1%   $   -326.67               |
|  OXY260807C00058000            7    -54.7%   $   -262.35               |
|  NKE260807C00042000           10    -32.9%   $   -211.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  SMCI260807P00027500           5    -78.3%   $   -180.00               |
|  AMZN260805C00287500          17    -29.2%   $   -168.30               |
|  AMZN260807C00297500          12    -41.0%   $   -167.08               |
|  AMZN260805C00290000          11    -55.4%   $   -164.15               |
|  ... 26 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-05.log
elapsed=0.6s reconcile=0.21s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.6s. run=#6106 https://github.com/28twagg-ops/TradingBot/actions/runs/31009313744
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.csv
Summary: keep=0 watch=101 drop=4
Orphan rate: 3.7% (47/1267)
# Options signal frequency

_Generated 2026-08-05T09:15:47.852787_

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
## Ledger health — 2026-08-05
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   201 | INFO |
| Total closed lots           |   753 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.43 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260805T132041Z

- UTC timestamp: `20260805T132041Z`
- GitHub run: [#6107](https://github.com/28twagg-ops/TradingBot/actions/runs/31009699153)
- Run id: `31009699153`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-05T09:20:44.671566-04:00","date":"2026-08-05","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.53},"signals":0,"placed":0,"equity":143530.98,"open_positions":34,"pending_orders":0,"open_lots":201,"submitted_today":0,"filled_today":0,"unattributed_contracts":15,"top_signals":[],"github_run":"6107","github_run_id":"31009699153","status":"ok"}
```

### Live bot full output

```text
13:20:42  INFO      Mode: summary
13:20:42  INFO        Daily log -> logs/daily/2026-08-05.md
13:20:42  INFO        Daily log reconciled -> logs/daily/2026-08-05.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.21|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $474.21|
|  Cash                                                           $286.31|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $187.90|
|  Open P&L                                                        $+0.62|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.63     $14.70   $14.70   -0.0%   $-0.01  |
|  AVB      Pullback50      $94.27     $187.24  $188.50  +0.7%   $+0.63  |
|                                                                        |
|  Total invested                                                 $187.90|
|  Total open P&L                                                  $+0.62|
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
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
|  2026-08-04  SELL  ALGN  Pullback50  $92.57  P&L $-0.62                |
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=201 paper_keys=yes dry_run=False
  alpaca positions=36
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-05T09:20:44.671566-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $143530.98, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,530.98                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             201                                     |
|  Broker option positions       34                                      |
|  Unattributed contracts        15 (orphan reconcile)                   |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=733  buckets=224  win=53%                            |
|  Returns   avg=+35.4%  med=+13.0%  p10=-66.2%  p90=+163.0%             |
|  Realized  $+13,667.61                                                 |
|  Raw incl dropped  trades=1267  real=$+12,072.06                       |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  2 100% +654.7 +654.7 +906.2 $   +274         |
|  b197 lab0197_s218_w3_10  2 100% +528.1 +528.1 +737.5 $   +220         |
|  b844 lab0844_s407_w2_10  3 100% +312.4 +446.1 +446.1 $   +138         |
|  b845 lab0845_s407_w2_10  3 100% +271.7 +353.3 +423.1 $   +127         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  1 100% +320.0 +320.0 +320.0 $    +80         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  3 100% +201.5 +273.1 +273.1 $   +177         |
|  ... 216 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  2   0% -95.9 -95.9 -95.9 $    -94       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (34)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -23.1%   $   -326.67               |
|  OXY260807C00058000            7    -54.7%   $   -262.35               |
|  NKE260807C00042000           10    -32.9%   $   -211.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  SMCI260807P00027500           5    -78.3%   $   -180.00               |
|  AMZN260805C00287500          17    -29.2%   $   -168.30               |
|  AMZN260807C00297500          12    -41.0%   $   -167.08               |
|  AMZN260805C00290000          11    -55.4%   $   -164.15               |
|  ... 26 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-05.log
elapsed=1.0s reconcile=0.53s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.0s. run=#6107 https://github.com/28twagg-ops/TradingBot/actions/runs/31009699153
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.csv
Summary: keep=0 watch=101 drop=4
Orphan rate: 3.7% (47/1267)
# Options signal frequency

_Generated 2026-08-05T09:20:50.060723_

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
## Ledger health — 2026-08-05
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   201 | INFO |
| Total closed lots           |   753 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.21 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260805T132826Z

- UTC timestamp: `20260805T132826Z`
- GitHub run: [#6108](https://github.com/28twagg-ops/TradingBot/actions/runs/31010090105)
- Run id: `31010090105`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`61s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-05T09:28:29.387466-04:00","date":"2026-08-05","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":52.5,"phases_s":{"reconcile":0.1,"cancel":0.02,"manage":5.62,"scan":46.39,"entries":0.02},"signals":0,"placed":0,"equity":146042.98,"open_positions":34,"pending_orders":0,"open_lots":201,"submitted_today":0,"filled_today":0,"unattributed_contracts":15,"top_signals":[],"github_run":"6108","github_run_id":"31010090105","status":"ok"}
```

### Live bot full output

```text
13:28:26  INFO      Mode: summary
13:28:27  INFO        Daily log -> logs/daily/2026-08-05.md
13:28:27  INFO        Daily log reconciled -> logs/daily/2026-08-05.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:28 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.21|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $474.21|
|  Cash                                                           $286.31|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $187.90|
|  Open P&L                                                        $+0.62|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.63     $14.70   $14.70   -0.0%   $-0.01  |
|  AVB      Pullback50      $94.27     $187.24  $188.50  +0.7%   $+0.63  |
|                                                                        |
|  Total invested                                                 $187.90|
|  Total open P&L                                                  $+0.62|
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
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
|  2026-08-04  SELL  ALGN  Pullback50  $92.57  P&L $-0.62                |
|  2026-08-03  SELL  TSN  EarningsDrift  $93.73  P&L $+0.23              |
|  2026-08-03  SELL  FSLR  EarningsDrift  $93.03  P&L $-0.50             |
|  2026-08-03  SELL  ED  Pullback50  $69.86  P&L $-0.37                  |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=201 paper_keys=yes dry_run=False
  alpaca positions=36
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-05T09:28:29.387466-04:00 ===

[Run context]
Paper auth OK — equity $146042.98, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-05 09:28:30,476 INFO   EXIT [b194|lab0194_s218_w2_1005_1045_r1|S218] stop_loss (-73.3%) SELL 1 RBLX260807C00039500 @<= 0.09
  EXIT [b25|lab0025_s203_w1_0928_1005_r2|S203] stop_loss (-78.3%) SELL failed SMCI260807P00027500: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-05 09:28:30,655 INFO   EXIT [b24|lab0024_s203_w1_0928_1005_r1|S203] stop_loss (-78.3%) SELL 1 SMCI260807P00027500 @<= 0.11
2026-08-05 09:28:33,952 INFO   EXIT [b817|lab0817_s405_w2_1005_1045_r2|S405] stop_loss (-54.7%) SELL 1 OXY260807C00058000 @<= 0.28
2026-08-05 09:28:34,790 INFO   EXIT [b351|lab0351_s360_w2_1005_1045_r2|S360] stop_loss (-55.4%) SELL 1 AMZN260805C00290000 @<= 0.10

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 0 signals across top-5 strategies
Paper lab: $146275 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  All bucket slots blocked or closed for today's signals — skip entry loop.
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $146,042.98                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             201                                     |
|  Broker option positions       34                                      |
|  Unattributed contracts        15 (orphan reconcile)                   |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=733  buckets=224  win=53%                            |
|  Returns   avg=+35.4%  med=+13.0%  p10=-66.2%  p90=+163.0%             |
|  Realized  $+13,667.61                                                 |
|  Raw incl dropped  trades=1267  real=$+12,072.06                       |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b196 lab0196_s218_w3_10  2 100% +654.7 +654.7 +906.2 $   +274         |
|  b197 lab0197_s218_w3_10  2 100% +528.1 +528.1 +737.5 $   +220         |
|  b844 lab0844_s407_w2_10  3 100% +312.4 +446.1 +446.1 $   +138         |
|  b845 lab0845_s407_w2_10  3 100% +271.7 +353.3 +423.1 $   +127         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  1 100% +320.0 +320.0 +320.0 $    +80         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  3 100% +201.5 +273.1 +273.1 $   +177         |
|  ... 216 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b848 lab0848_s407_w4_11  2   0% -95.9 -95.9 -95.9 $    -94       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (4)                                                     |
+------------------------------------------------------------------------+
|  b194 S218 RBLX260807C00039500 x1 stop_loss (-73.3%)                   |
|  b24  S203 SMCI260807P00027500 x1 stop_loss (-78.3%)                   |
|  b817 S405 OXY260807C00058000 x1 stop_loss (-54.7%)                    |
|  b351 S360 AMZN260805C00290000 x1 stop_loss (-55.4%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (34)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -23.1%   $   -326.67               |
|  OXY260807C00058000            7    -54.7%   $   -262.35               |
|  NKE260807C00042000           10    -32.9%   $   -211.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  SMCI260807P00027500           5    -78.3%   $   -180.00               |
|  AMZN260805C00287500          17    -29.2%   $   -168.30               |
|  AMZN260807C00297500          12    -41.0%   $   -167.08               |
|  AMZN260805C00290000          11    -55.4%   $   -164.15               |
|  ... 26 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-05.log
elapsed=52.5s reconcile=0.1s cancel=0.02s manage=5.62s scan=46.39s entries=0.02s
STATUS: options_morning_bot run complete (PAPER) elapsed=52.5s. run=#6108 https://github.com/28twagg-ops/TradingBot/actions/runs/31010090105
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.csv
Summary: keep=0 watch=101 drop=4
Orphan rate: 3.7% (47/1267)
# Options signal frequency

_Generated 2026-08-05T09:29:27.305783_

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
## Ledger health — 2026-08-05
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   398 | WARN | <<<
| Missing exit records (post) |   398 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   201 | INFO |
| Total closed lots           |   753 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.21 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260805T133050Z

- UTC timestamp: `20260805T133050Z`
- GitHub run: [#6109](https://github.com/28twagg-ops/TradingBot/actions/runs/31010490558)
- Run id: `31010490558`
- Live bot: exit=`0`, duration=`218s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-05T09:28:29.387466-04:00","date":"2026-08-05","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":52.5,"phases_s":{"reconcile":0.1,"cancel":0.02,"manage":5.62,"scan":46.39,"entries":0.02},"signals":0,"placed":0,"equity":146042.98,"open_positions":34,"pending_orders":0,"open_lots":201,"submitted_today":0,"filled_today":0,"unattributed_contracts":15,"top_signals":[],"github_run":"6108","github_run_id":"31010090105","status":"ok"}
```

### Live bot full output

```text
13:30:51  INFO      Mode: morning_prep
13:30:52  INFO        [prep_positions] 2/2 (2 valid)
13:30:52  INFO      Fetching tickers (universe=both)...
13:30:52  INFO        S&P 500: 503
13:30:52  INFO        MidCap 400: 400
13:30:52  INFO        Total: 903 tickers
13:30:55  INFO        [prep_universe] 40/901 (40 valid)
13:30:57  INFO        [prep_universe] 80/901 (80 valid)
13:30:58  INFO        [prep_universe] 120/901 (120 valid)
13:31:00  INFO        [prep_universe] 160/901 (160 valid)
13:31:02  INFO        [prep_universe] 200/901 (199 valid)
13:31:06  INFO        [prep_universe] 240/901 (238 valid)
13:31:19  INFO        [prep_universe] 280/901 (278 valid)
13:31:30  INFO        [prep_universe] 320/901 (318 valid)
13:31:41  INFO        [prep_universe] 360/901 (358 valid)
13:31:54  INFO        [prep_universe] 400/901 (397 valid)
13:32:08  INFO        [prep_universe] 440/901 (437 valid)
13:32:18  INFO        [prep_universe] 480/901 (477 valid)
13:32:29  INFO        [prep_universe] 520/901 (517 valid)
13:32:43  INFO        [prep_universe] 560/901 (557 valid)
13:32:54  INFO        [prep_universe] 600/901 (597 valid)
13:33:05  INFO        [prep_universe] 640/901 (637 valid)
13:33:19  INFO        [prep_universe] 680/901 (677 valid)
13:33:30  INFO        [prep_universe] 720/901 (717 valid)
13:33:43  INFO        [prep_universe] 760/901 (757 valid)
13:33:54  INFO        [prep_universe] 800/901 (797 valid)
13:34:07  INFO        [prep_universe] 840/901 (836 valid)
13:34:18  INFO        [prep_universe] 880/901 (876 valid)
13:34:25  INFO        [prep_universe] 901/901 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.91|
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
|  Open positions                                                       2|
|  Invested                                                       $188.60|
|  Open P&L                                                        $+1.32|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.57     $14.70   $14.69   -0.1%   $-0.07  |
|  AVB      Pullback50      $95.03     $187.24  $190.02  +1.5%   $+1.39  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  AES       OrderType.STOP    6         None        14.62               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   52|
|  Universe scanned                                                   901|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=201 paper_keys=yes dry_run=False
  alpaca positions=36
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-05T09:34:30.774568-04:00 ===

[Run context]
Paper auth OK — equity $149563.92, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-05 09:34:32,605 INFO   EXIT [b166|lab0166_s216_w2_1005_1045_r1|S216] stop_loss (-64.7%) SELL 1 DKNG260807C00025500 @<= 0.12
2026-08-05 09:34:34,004 INFO   EXIT [b861|lab0861_s408_w3_1045_1120_r2|S408] take_profit (+586.5%) SELL 1 NVDA260805C00220000 @<= 1.28
2026-08-05 09:34:34,307 INFO   EXIT [b821|lab0821_s405_w4_1120_1135_r2|S405] stop_loss (-56.2%) SELL 1 OXY260807C00058000 @<= 0.27
2026-08-05 09:34:35,250 INFO   EXIT [b860|lab0860_s408_w3_1045_1120_r1|S408] stop_loss (-52.9%) SELL 1 NKE260807C00043500 @<= 0.05
  EXIT [b366|lab0366_s361_w3_1045_1120_r1|S361] take_profit (+766.5%) SELL failed NVDA260805C00217500: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-05 09:34:37,445 INFO   EXIT [b238|lab0238_s401_w3_1045_1120_r1|S401] take_profit (+766.5%) SELL 1 NVDA260805C00217500 @<= 2.37
2026-08-05 09:34:38,789 INFO   EXIT [b183|lab0183_s217_w3_1045_1120_r2|S217] stop_loss (-69.7%) SELL 1 RBLX260807C00040000 @<= 0.07
2026-08-05 09:34:39,352 INFO   EXIT [b237|lab0237_s401_w2_1005_1045_r2|S401] stop_loss (-96.4%) SELL 1 UBER260807C00077000 @<= 0.02
2026-08-05 09:34:39,563 INFO   EXIT [b265|lab0265_s403_w2_1005_1045_r2|S403] stop_loss (-57.1%) SELL 1 T260807C00023000 @<= 0.28
2026-08-05 09:34:41,111 INFO   EXIT [b109|lab0109_s212_w1_0928_1005_r2|S212] stop_loss (-100.0%) SELL 1 UBER260807C00078000 @<= 0.01
2026-08-05 09:34:41,493 INFO   EXIT [b195|lab0195_s218_w2_1005_1045_r2|S218] stop_loss (-73.3%) SELL 1 RBLX260807C00039500 @<= 0.09
2026-08-05 09:34:42,897 INFO   EXIT [b301|lab0301_s353_w3_1045_1120_r2|S353] take_profit (+67.1%) SELL 1 AMZN260807C00292500 @<= 0.97

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260805T133610Z

- UTC timestamp: `20260805T133610Z`
- GitHub run: [#6110](https://github.com/28twagg-ops/TradingBot/actions/runs/31010899706)
- Run id: `31010899706`
- Live bot: exit=`0`, duration=`214s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-05T09:28:29.387466-04:00","date":"2026-08-05","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":52.5,"phases_s":{"reconcile":0.1,"cancel":0.02,"manage":5.62,"scan":46.39,"entries":0.02},"signals":0,"placed":0,"equity":146042.98,"open_positions":34,"pending_orders":0,"open_lots":201,"submitted_today":0,"filled_today":0,"unattributed_contracts":15,"top_signals":[],"github_run":"6108","github_run_id":"31010090105","status":"ok"}
```

### Live bot full output

```text
13:36:11  INFO      Mode: morning_prep
13:36:12  INFO        [prep_positions] 2/2 (2 valid)
13:36:12  INFO      Fetching tickers (universe=both)...
13:36:12  INFO        S&P 500: 503
13:36:12  INFO        MidCap 400: 400
13:36:12  INFO        Total: 903 tickers
13:36:14  INFO        [prep_universe] 40/901 (40 valid)
13:36:15  INFO        [prep_universe] 80/901 (80 valid)
13:36:16  INFO        [prep_universe] 120/901 (120 valid)
13:36:17  INFO        [prep_universe] 160/901 (160 valid)
13:36:19  INFO        [prep_universe] 200/901 (199 valid)
13:36:26  INFO        [prep_universe] 240/901 (238 valid)
13:36:39  INFO        [prep_universe] 280/901 (278 valid)
13:36:50  INFO        [prep_universe] 320/901 (318 valid)
13:37:03  INFO        [prep_universe] 360/901 (358 valid)
13:37:13  INFO        [prep_universe] 400/901 (397 valid)
13:37:27  INFO        [prep_universe] 440/901 (437 valid)
13:37:37  INFO        [prep_universe] 480/901 (477 valid)
13:37:50  INFO        [prep_universe] 520/901 (517 valid)
13:38:00  INFO        [prep_universe] 560/901 (557 valid)
13:38:13  INFO        [prep_universe] 600/901 (597 valid)
13:38:26  INFO        [prep_universe] 640/901 (637 valid)
13:38:36  INFO        [prep_universe] 680/901 (677 valid)
13:38:50  INFO        [prep_universe] 720/901 (717 valid)
13:39:03  INFO        [prep_universe] 760/901 (757 valid)
13:39:13  INFO        [prep_universe] 800/901 (797 valid)
13:39:26  INFO        [prep_universe] 840/901 (836 valid)
13:39:39  INFO        [prep_universe] 880/901 (876 valid)
13:39:43  INFO        [prep_universe] 901/901 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.01|
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
|  Open positions                                                       2|
|  Invested                                                       $187.70|
|  Open P&L                                                        $+0.42|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.57     $14.70   $14.69   -0.1%   $-0.07  |
|  AVB      Pullback50      $94.13     $187.24  $188.23  +0.5%   $+0.49  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  AES       OrderType.STOP    6         None        14.62               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      0|
|  Signal candidates                                                   13|
|  Universe scanned                                                   901|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=201 paper_keys=yes dry_run=False
  alpaca positions=36
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-05T09:39:47.448026-04:00 ===

[Run context]
Paper auth OK — equity $148688.58, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-05 09:39:51,754 INFO   EXIT [b236|lab0236_s401_w2_1005_1045_r1|S401] stop_loss (-98.2%) SELL 1 UBER260807C00077000 @<= 0.02
2026-08-05 09:39:52,198 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-61.5%) SELL 1 AMZN260807C00305000 @<= 0.06
2026-08-05 09:39:52,861 INFO   EXIT [b795|lab0795_s399_w2_1005_1045_r2|S399] stop_loss (-50.0%) SELL 1 AMZN260807C00300000 @<= 0.14
2026-08-05 09:39:53,317 INFO   EXIT [b310|lab0310_s354_w4_1120_1135_r1|S354] stop_loss (-62.0%) SELL 1 OXY260807C00058000 @<= 0.23
2026-08-05 09:39:53,488 INFO   EXIT [b169|lab0169_s216_w3_1045_1120_r2|S216] stop_loss (-52.9%) SELL 1 DKNG260807C00025500 @<= 0.21
2026-08-05 09:39:54,614 INFO   EXIT [b351|lab0351_s360_w2_1005_1045_r2|S360] stop_loss (-85.1%) SELL 1 AMZN260805C00290000 @<= 0.05
2026-08-05 09:39:55,221 INFO   EXIT [b27|lab0027_s203_w2_1005_1045_r2|S203] stop_loss (-76.1%) SELL 1 SMCI260807P00027500 @<= 0.10
2026-08-05 09:39:55,958 INFO   EXIT [b860|lab0860_s408_w3_1045_1120_r1|S408] take_profit (+1116.2%) SELL 1 NVDA260805C00220000 @<= 2.29
  EXIT [b366|lab0366_s361_w3_1045_1120_r1|S361] take_profit (+1273.8%) SELL failed NVDA260805C00217500: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-05 09:39:56,728 INFO   EXIT [b383|lab0383_s362_w4_1120_1135_r2|S362] take_profit (+1273.8%) SELL 1 NVDA260805C00217500 @<= 4.06
2026-08-05 09:40:01,134 INFO   EXIT [b291|lab0291_s352_w2_1005_1045_r2|S352] stop_loss (-67.6%) SELL 1 AMZN260805C00287500 @<= 0.13
2026-08-05 09:40:02,965 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-66.7%) SELL 2 RBLX260807C00039500 @<= 0.12
2026-08-05 09:40:07,827 INFO   EXIT [b108|lab0108_s212_w1_0928_1005_r1|S212] stop_loss (-100.0%) SELL 1 UBER260807C00078000 @<= 0.01

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
```

---

## Run 20260805T134331Z

- UTC timestamp: `20260805T134331Z`
- GitHub run: [#6111](https://github.com/28twagg-ops/TradingBot/actions/runs/31011306256)
- Run id: `31011306256`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-05T09:28:29.387466-04:00","date":"2026-08-05","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":52.5,"phases_s":{"reconcile":0.1,"cancel":0.02,"manage":5.62,"scan":46.39,"entries":0.02},"signals":0,"placed":0,"equity":146042.98,"open_positions":34,"pending_orders":0,"open_lots":201,"submitted_today":0,"filled_today":0,"unattributed_contracts":15,"top_signals":[],"github_run":"6108","github_run_id":"31010090105","status":"ok"}
```

### Live bot full output

```text
13:43:32  INFO      Mode: morning_prep
13:43:33  INFO        [prep_positions] 2/2 (2 valid)
13:43:33  INFO        Universe cache hit: 903 tickers (tickers_2026-08-05.json)
13:43:34  INFO        [prep_universe] 40/901 (40 valid)
13:43:35  INFO        [prep_universe] 80/901 (80 valid)
13:43:36  INFO        [prep_universe] 120/901 (120 valid)
13:43:37  INFO        [prep_universe] 160/901 (160 valid)
13:43:38  INFO        [prep_universe] 200/901 (199 valid)
13:43:46  INFO        [prep_universe] 240/901 (238 valid)
13:43:58  INFO        [prep_universe] 280/901 (278 valid)
13:44:11  INFO        [prep_universe] 320/901 (318 valid)
13:44:22  INFO        [prep_universe] 360/901 (358 valid)
13:44:35  INFO        [prep_universe] 400/901 (397 valid)
13:44:47  INFO        [prep_universe] 440/901 (437 valid)
13:45:00  INFO        [prep_universe] 480/901 (477 valid)
13:45:11  INFO        [prep_universe] 520/901 (517 valid)
```

### Options bot full output

```text

## Run 20260805T134845Z

- UTC timestamp: `20260805T134845Z`
- GitHub run: [#6112](https://github.com/28twagg-ops/TradingBot/actions/runs/31011715512)
- Run id: `31011715512`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-05T09:28:29.387466-04:00","date":"2026-08-05","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":52.5,"phases_s":{"reconcile":0.1,"cancel":0.02,"manage":5.62,"scan":46.39,"entries":0.02},"signals":0,"placed":0,"equity":146042.98,"open_positions":34,"pending_orders":0,"open_lots":201,"submitted_today":0,"filled_today":0,"unattributed_contracts":15,"top_signals":[],"github_run":"6108","github_run_id":"31010090105","status":"ok"}
```

### Live bot full output

```text
13:48:46  INFO      Mode: morning_scan
13:48:47  INFO        [positions] 2/2 (2 valid)
13:48:47  INFO        Universe cache hit: 903 tickers (tickers_2026-08-05.json)
13:48:49  INFO        [universe] 40/901 (40 valid)
13:48:50  INFO        [universe] 80/901 (80 valid)
13:48:52  INFO        [universe] 120/901 (120 valid)
13:48:53  INFO        [universe] 160/901 (160 valid)
13:48:54  INFO        [universe] 200/901 (199 valid)
13:49:02  INFO        [universe] 240/901 (238 valid)
13:49:12  INFO        [universe] 280/901 (278 valid)
13:49:26  INFO        [universe] 320/901 (318 valid)
13:49:36  INFO        [universe] 360/901 (358 valid)
13:49:49  INFO        [universe] 400/901 (397 valid)
13:50:03  INFO        [universe] 440/901 (437 valid)
13:50:13  INFO        [universe] 480/901 (477 valid)
```

### Options bot full output

```text

## Run 20260805T135115Z

- UTC timestamp: `20260805T135115Z`
- GitHub run: [#6113](https://github.com/28twagg-ops/TradingBot/actions/runs/31012124184)
- Run id: `31012124184`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-05T09:28:29.387466-04:00","date":"2026-08-05","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":52.5,"phases_s":{"reconcile":0.1,"cancel":0.02,"manage":5.62,"scan":46.39,"entries":0.02},"signals":0,"placed":0,"equity":146042.98,"open_positions":34,"pending_orders":0,"open_lots":201,"submitted_today":0,"filled_today":0,"unattributed_contracts":15,"top_signals":[],"github_run":"6108","github_run_id":"31010090105","status":"ok"}
```

### Live bot full output

```text
13:51:15  INFO      Mode: morning_scan
13:51:17  INFO        [positions] 2/2 (2 valid)
13:51:17  INFO        Universe cache hit: 903 tickers (tickers_2026-08-05.json)
13:51:19  INFO        [universe] 40/901 (40 valid)
13:51:20  INFO        [universe] 80/901 (80 valid)
13:51:22  INFO        [universe] 120/901 (120 valid)
13:51:23  INFO        [universe] 160/901 (160 valid)
13:51:27  INFO        [universe] 200/901 (199 valid)
13:51:38  INFO        [universe] 240/901 (238 valid)
13:51:51  INFO        [universe] 280/901 (278 valid)
13:52:02  INFO        [universe] 320/901 (318 valid)
13:52:16  INFO        [universe] 360/901 (358 valid)
13:52:27  INFO        [universe] 400/901 (397 valid)
13:52:40  INFO        [universe] 440/901 (437 valid)
13:52:51  INFO        [universe] 480/901 (477 valid)
13:53:05  INFO        [universe] 520/901 (517 valid)
13:53:15  INFO        [universe] 560/901 (557 valid)
13:53:29  INFO        [universe] 600/901 (597 valid)
13:53:39  INFO        [universe] 640/901 (637 valid)
13:53:52  INFO        [universe] 680/901 (677 valid)
13:54:03  INFO        [universe] 720/901 (717 valid)
13:54:16  INFO        [universe] 760/901 (757 valid)
13:54:27  INFO        [universe] 800/901 (797 valid)
13:54:40  INFO        [universe] 840/901 (836 valid)
13:54:51  INFO        [universe] 880/901 (876 valid)
13:54:58  INFO        [universe] 901/901 (897 valid)
13:55:01  INFO        BUY  ALGN  $94.85  [Pullback50]  id=def0bb5b-95b6-48b2-91e4-07c70ab1daff
13:55:01  INFO        BUY  AMAT  $94.85  [Pullback50]  id=c71d32f2-d93d-49e5-a93c-6e48cd6e2f35
13:55:02  INFO        BUY  COHR  $72.89  [Pullback50]  id=4dd1172a-b852-4e7c-a2c7-60f6073016f9

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.27|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-05|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $474.27|
|  Cash                                                           $286.31|
|  Reserve                                          $23.71  (always kept)|
|  Available                                    $262.60  (for new trades)|
|  Trade size             $94.85  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (2 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.57     $14.70   $14.69   -0.1%   $-0.07  |
|  AVB      Pullback50      $94.39     $187.24  $188.74  +0.8%   $+0.75  |
|                                                                        |
|  Total invested                                                 $187.96|
|  Total open P&L                                                  $+0.68|
|  Buys today: 0  |  entry cap: 3  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (38885.8m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  AES  P&L -0.1%  $-0.07                                            HOLD|
|  AVB  P&L +0.8%  $+0.75                                            HOLD|
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
|                         SIGNALS FOUND  --  18                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  ALGN     Pullback50      eq     $173.31  44.3   -2.05   50MA bounce (-|
|  AMAT     Pullback50      eq     $551.33  48.6   -2.45   50MA bounce (+|
|  COHR     Pullback50      eq     $343.32  62.8   -1.94   50MA bounce (-|
|  FIX      Pullback50      eq     $1808.~  58.4   -1.97   50MA bounce (-|
|  FTV      Pullback50      eq     $60.73   43.8   -2.05   50MA bounce (-|
|  GEV      Pullback50      eq     $1029.~  49.3   -2.55   50MA bounce (+|
|  IBKR     Pullback50      eq     $90.34   46.2   -2.64   50MA bounce (-|
|  JBL      Pullback50      eq     $344.93  65.6   -2.85   50MA bounce (-|
|  MRNA     Pullback50      eq     $58.53   39.8   -2.47   50MA bounce (-|
|  RL       Pullback50      eq     $387.04  49.3   -2.49   50MA bounce (+|
|  TJX      Pullback50      eq     $158.94  61.2   -2.98   50MA bounce (+|
|  UNH      Pullback50      eq     $408.18  40.2   -1.66   50MA bounce (-|
|  WDC      Pullback50      eq     $562.55  64.8   -2.39   50MA bounce (-|
|  BWA      Pullback50      eq     $68.06   68.0   -1.98   50MA bounce (+|
|  BYD      Pullback50      eq     $87.72   44.3   -2.56   50MA bounce (+|
|  EXP      Pullback50      eq     $216.15  51.7   -1.92   50MA bounce (+|
|  NJR      Pullback50      eq     $56.40   30.1   -2.34   50MA bounce (-|
|  SWX      Pullback50      eq     $90.33   36.7   -2.95   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] ALGN  Pullback50                                   $94.85|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] AMAT  Pullback50                                   $94.85|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] COHR  Pullback50                                   $72.89|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|```

### Options bot full output

```text
