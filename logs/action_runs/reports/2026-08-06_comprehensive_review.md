# Daily Comprehensive Action Review — 2026-08-06

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260806T000917Z

- UTC timestamp: `20260806T000917Z`
- GitHub run: [#6242](https://github.com/28twagg-ops/TradingBot/actions/runs/31058724506)
- Run id: `31058724506`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-05T20:09:21.328652-04:00","date":"2026-08-05","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.22},"signals":0,"placed":0,"equity":143407.38,"open_positions":29,"pending_orders":0,"open_lots":178,"submitted_today":114,"filled_today":180,"unattributed_contracts":3,"top_signals":[],"github_run":"6242","github_run_id":"31058724506","status":"ok"}
```

### Live bot full output

```text
00:09:18  INFO      Mode: summary
00:09:19  INFO        Daily log -> logs/daily/2026-08-06.md
00:09:19  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         00:09 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.28|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $471.28|
|  Cash                                                           $282.79|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.49|
|  Open P&L                                                        $+1.21|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.67     $14.70   $14.70   +0.0%   $+0.03  |
|  AVB      Pullback50      $94.82     $187.24  $189.61  +1.3%   $+1.18  |
|                                                                        |
|  Total invested                                                 $188.49|
|  Total open P&L                                                  $+1.21|
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
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
|  2026-08-05  SELL  ALGN  Pullback50  $94.07  P&L $-0.77                |
|  2026-08-05  SELL  AMAT  Pullback50  $94.48  P&L $-0.32                |
|  2026-08-05  SELL  COHR  Pullback50  $72.51  P&L $-0.37                |
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=178 paper_keys=yes dry_run=False
  alpaca positions=31
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-05T20:09:21.328652-04:00 ===

[Run context]
After hours (20:09 ET) — exit summary only.
Paper auth OK — equity $143407.38, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,407.38                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    114                                     |
|  Orders filled today (ledger)  180                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             178                                     |
|  Broker option positions       29                                      |
|  Unattributed contracts        3 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1034  buckets=250  win=45%                           |
|  Returns   avg=+26.3%  med=-15.6%  p10=-73.8%  p90=+140.0%             |
|  Realized  $+11,975.32                                                 |
|  Raw incl dropped  trades=1568  real=$+10,379.77                       |
|  Today     trades=178  avg=+0.3%  med=-60.5%  real=$-1,932.81          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  4  50% +631.1 +566.7 +1446.7 $   +411        |
|  b196 lab0196_s218_w3_10  3 100% +453.8 +403.1 +906.2 $   +310         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 242 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (9)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN PLTR260807C00172500 x3 stop_loss (-54.4%)                 |
|  b802 S404 AMZN260807C00295000 x1 stop_loss (-90.1%)                   |
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b196 S218 RBLX260807C00040000 x1 stop_loss (-84.8%)                   |
|  b300 S353 AMZN260807C00292500 x1 stop_loss (-90.7%)                   |
|  ... 4 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (29)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -90.1%   $ -1,271.67               |
|  AMZN260807C00292500          20    -90.7%   $   -977.00               |
|  AMZN260805C00287500          16   -100.0%   $   -542.40               |
|  AMZN260807C00297500           9    -94.1%   $   -287.31               |
|  UBER260807C00078000           5    -98.0%   $   -247.22               |
|  DKNG260807C00024500           7    -59.4%   $   -163.80               |
|  AMZN260805C00290000           6   -100.0%   $   -161.54               |
|  AMD260805C00525000            3   -100.0%   $   -132.00               |
|  ... 21 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-05.log
elapsed=0.6s reconcile=0.22s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.6s. run=#6242 https://github.com/28twagg-ops/TradingBot/actions/runs/31058724506
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.csv
Summary: 91 buckets closed trades, $-1,932.81 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.csv
Summary: keep=0 watch=97 drop=8
Orphan rate: 5.6% (88/1568)
# Options signal frequency

_Generated 2026-08-05T20:09:26.186077_

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
| State/ledger mismatches     |    17 | WARN | <<<
| Total open lots             |   178 | INFO |
| Total closed lots           |  1013 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.28 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T014601Z

- UTC timestamp: `20260806T014601Z`
- GitHub run: [#6243](https://github.com/28twagg-ops/TradingBot/actions/runs/31063645034)
- Run id: `31063645034`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-05T21:46:06.586523-04:00","date":"2026-08-05","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.64},"signals":0,"placed":0,"equity":142567.38,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":114,"filled_today":180,"unattributed_contracts":3,"top_signals":[],"github_run":"6243","github_run_id":"31063645034","status":"ok"}
```

### Live bot full output

```text
01:46:02  INFO      Mode: summary
01:46:03  INFO        Daily log -> logs/daily/2026-08-06.md
01:46:03  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.28|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $471.28|
|  Cash                                                           $282.79|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.49|
|  Open P&L                                                        $+1.21|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.67     $14.70   $14.70   +0.0%   $+0.03  |
|  AVB      Pullback50      $94.82     $187.24  $189.61  +1.3%   $+1.18  |
|                                                                        |
|  Total invested                                                 $188.49|
|  Total open P&L                                                  $+1.21|
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
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
|  2026-08-05  SELL  ALGN  Pullback50  $94.07  P&L $-0.77                |
|  2026-08-05  SELL  AMAT  Pullback50  $94.48  P&L $-0.32                |
|  2026-08-05  SELL  COHR  Pullback50  $72.51  P&L $-0.37                |
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=178 paper_keys=yes dry_run=False
  alpaca positions=28
  FLAG b284|S351|54bb6ebf missing from Alpaca
  FLAG b289|S352|82e1a7ed missing from Alpaca
  FLAG b288|S352|e7fdb85e missing from Alpaca
  FLAG b295|S352|a680a6bd missing from Alpaca
  FLAG b294|S352|e9fc2a00 missing from Alpaca
  FLAG b286|S351|2cb27b7f missing from Alpaca
  FLAG b281|S351|88c4679e missing from Alpaca
  FLAG b277|S350|3cca0c6e missing from Alpaca
  FLAG b287|S351|9099ac70 missing from Alpaca
  FLAG b291|S352|96cedb0a missing from Alpaca
  FLAG b279|S350|d5580618 missing from Alpaca
  FLAG b278|S350|6610b657 missing from Alpaca
  FLAG b280|S351|28ea91e1 missing from Alpaca
  FLAG b364|S361|d9bf4849 missing from Alpaca
  FLAG b351|S360|a2c00773 missing from Alpaca
  FLAG b276|S350|8aa344cf missing from Alpaca
  FLAG b282|S351|01e106fd missing from Alpaca
  FLAG b280|S351|0bdfa45a missing from Alpaca
  FLAG b276|S350|61a84864 missing from Alpaca
  FLAG b0|ORPHAN|59e18c93 missing from Alpaca
  FLAG b351|S360|b91581d1 missing from Alpaca
  FLAG b0|ORPHAN|6dbf70e9 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-05T21:46:06.586523-04:00 ===

[Run context]
After hours (21:46 ET) — exit summary only.
Paper auth OK — equity $142567.38, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $142,567.38                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    114                                     |
|  Orders filled today (ledger)  180                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             156                                     |
|  Broker option positions       26                                      |
|  Unattributed contracts        3 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1034  buckets=250  win=45%                           |
|  Returns   avg=+26.3%  med=-15.6%  p10=-73.8%  p90=+140.0%             |
|  Realized  $+11,975.32                                                 |
|  Raw incl dropped  trades=1568  real=$+10,379.77                       |
|  Today     trades=178  avg=+0.3%  med=-60.5%  real=$-1,932.81          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  4  50% +631.1 +566.7 +1446.7 $   +411        |
|  b196 lab0196_s218_w3_10  3 100% +453.8 +403.1 +906.2 $   +310         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 242 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (9)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN PLTR260807C00172500 x3 stop_loss (-54.4%)                 |
|  b802 S404 AMZN260807C00295000 x1 stop_loss (-90.1%)                   |
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b196 S218 RBLX260807C00040000 x1 stop_loss (-84.8%)                   |
|  b300 S353 AMZN260807C00292500 x1 stop_loss (-90.7%)                   |
|  ... 4 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (26)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -90.1%   $ -1,271.67               |
|  AMZN260807C00292500          20    -90.7%   $   -977.00               |
|  AMZN260807C00297500           9    -94.1%   $   -287.31               |
|  UBER260807C00078000           5    -98.0%   $   -247.22               |
|  DKNG260807C00024500           7    -59.4%   $   -163.80               |
|  NKE260807C00042000           10    +13.9%   $    +89.00               |
|  RBLX260807C00040000           3    -84.8%   $    -84.00               |
|  TTD260807P00017000            4    -34.5%   $    -76.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-05.log
elapsed=1.2s reconcile=0.64s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.2s. run=#6243 https://github.com/28twagg-ops/TradingBot/actions/runs/31063645034
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_buckets.csv
Summary: 91 buckets closed trades, $-1,932.81 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-05_strategy_selection.csv
Summary: keep=0 watch=97 drop=8
Orphan rate: 5.6% (88/1568)
# Options signal frequency

_Generated 2026-08-05T21:46:13.437861_

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
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  1013 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.28 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T044947Z

- UTC timestamp: `20260806T044947Z`
- GitHub run: [#6244](https://github.com/28twagg-ops/TradingBot/actions/runs/31072306862)
- Run id: `31072306862`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T00:49:50.655895-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.23},"signals":0,"placed":0,"equity":143099.38,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":0,"filled_today":0,"unattributed_contracts":3,"top_signals":[],"github_run":"6244","github_run_id":"31072306862","status":"ok"}
```

### Live bot full output

```text
04:49:48  INFO      Mode: summary
04:49:48  INFO        Daily log -> logs/daily/2026-08-06.md
04:49:48  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         04:49 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.28|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $471.28|
|  Cash                                                           $282.79|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.49|
|  Open P&L                                                        $+1.21|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.67     $14.70   $14.70   +0.0%   $+0.03  |
|  AVB      Pullback50      $94.82     $187.24  $189.61  +1.3%   $+1.18  |
|                                                                        |
|  Total invested                                                 $188.49|
|  Total open P&L                                                  $+1.21|
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
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
|  2026-08-05  SELL  ALGN  Pullback50  $94.07  P&L $-0.77                |
|  2026-08-05  SELL  AMAT  Pullback50  $94.48  P&L $-0.32                |
|  2026-08-05  SELL  COHR  Pullback50  $72.51  P&L $-0.37                |
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=156 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T00:49:50.655895-04:00 ===

[Run context]
After hours (00:49 ET) — exit summary only.
Paper auth OK — equity $143099.38, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,099.38                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             156                                     |
|  Broker option positions       26                                      |
|  Unattributed contracts        3 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1034  buckets=250  win=45%                           |
|  Returns   avg=+26.3%  med=-15.6%  p10=-73.8%  p90=+140.0%             |
|  Realized  $+11,975.32                                                 |
|  Raw incl dropped  trades=1568  real=$+10,379.77                       |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  4  50% +631.1 +566.7 +1446.7 $   +411        |
|  b196 lab0196_s218_w3_10  3 100% +453.8 +403.1 +906.2 $   +310         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 242 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (9)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN PLTR260807C00172500 x3 stop_loss (-54.4%)                 |
|  b802 S404 AMZN260807C00295000 x1 stop_loss (-90.1%)                   |
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b196 S218 RBLX260807C00040000 x1 stop_loss (-84.8%)                   |
|  b300 S353 AMZN260807C00292500 x1 stop_loss (-90.7%)                   |
|  ... 4 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (26)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -90.1%   $ -1,271.67               |
|  AMZN260807C00292500          20    -90.7%   $   -977.00               |
|  AMZN260807C00297500           9    -94.1%   $   -287.31               |
|  UBER260807C00078000           5    -98.0%   $   -247.22               |
|  DKNG260807C00024500           7    -59.4%   $   -163.80               |
|  NKE260807C00042000           10    +13.9%   $    +89.00               |
|  RBLX260807C00040000           3    -84.8%   $    -84.00               |
|  TTD260807P00017000            4    -34.5%   $    -76.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=0.7s reconcile=0.23s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.7s. run=#6244 https://github.com/28twagg-ops/TradingBot/actions/runs/31072306862
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 5 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=97 drop=8
Orphan rate: 5.6% (88/1568)
# Options signal frequency

_Generated 2026-08-06T00:49:56.962302_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |   442 | WARN | <<<
| Missing exit records (post) |   438 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  1013 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.28 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T130047Z

- UTC timestamp: `20260806T130047Z`
- GitHub run: [#6245](https://github.com/28twagg-ops/TradingBot/actions/runs/31103873478)
- Run id: `31103873478`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T09:00:50.862409-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.48},"signals":0,"placed":0,"equity":143161.28,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":0,"filled_today":0,"unattributed_contracts":3,"top_signals":[],"github_run":"6245","github_run_id":"31103873478","status":"ok"}
```

### Live bot full output

```text
13:00:48  INFO      Mode: summary
13:00:48  INFO        Daily log -> logs/daily/2026-08-06.md
13:00:48  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.15|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $471.15|
|  Cash                                                           $282.79|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.36|
|  Open P&L                                                        $+1.08|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.54     $14.70   $14.68   -0.1%   $-0.10  |
|  AVB      Pullback50      $94.82     $187.24  $189.61  +1.3%   $+1.18  |
|                                                                        |
|  Total invested                                                 $188.36|
|  Total open P&L                                                  $+1.08|
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
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
|  2026-08-05  SELL  ALGN  Pullback50  $94.07  P&L $-0.77                |
|  2026-08-05  SELL  AMAT  Pullback50  $94.48  P&L $-0.32                |
|  2026-08-05  SELL  COHR  Pullback50  $72.51  P&L $-0.37                |
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=156 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T09:00:50.862409-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $143161.28, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,161.28                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             156                                     |
|  Broker option positions       26                                      |
|  Unattributed contracts        3 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1034  buckets=250  win=45%                           |
|  Returns   avg=+26.3%  med=-15.6%  p10=-73.8%  p90=+140.0%             |
|  Realized  $+11,975.32                                                 |
|  Raw incl dropped  trades=1568  real=$+10,379.77                       |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  4  50% +631.1 +566.7 +1446.7 $   +411        |
|  b196 lab0196_s218_w3_10  3 100% +453.8 +403.1 +906.2 $   +310         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 242 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (9)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN PLTR260807C00172500 x3 stop_loss (-54.4%)                 |
|  b802 S404 AMZN260807C00295000 x1 stop_loss (-90.1%)                   |
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b196 S218 RBLX260807C00040000 x1 stop_loss (-84.8%)                   |
|  b300 S353 AMZN260807C00292500 x1 stop_loss (-90.7%)                   |
|  ... 4 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (26)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -90.1%   $ -1,271.67               |
|  AMZN260807C00292500          20    -90.7%   $   -977.00               |
|  AMZN260807C00297500           9    -94.1%   $   -287.31               |
|  UBER260807C00078000           5    -98.0%   $   -247.67               |
|  DKNG260807C00024500           7    -59.4%   $   -163.80               |
|  NKE260807C00042000           10    +13.9%   $    +89.00               |
|  RBLX260807C00040000           3    -84.8%   $    -84.00               |
|  TTD260807P00017000            4    -34.5%   $    -76.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=1.0s reconcile=0.48s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.0s. run=#6245 https://github.com/28twagg-ops/TradingBot/actions/runs/31103873478
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 5 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=97 drop=8
Orphan rate: 5.6% (88/1568)
# Options signal frequency

_Generated 2026-08-06T09:00:57.383368_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |   442 | WARN | <<<
| Missing exit records (post) |   438 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  1013 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.15 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T130544Z

- UTC timestamp: `20260806T130544Z`
- GitHub run: [#6246](https://github.com/28twagg-ops/TradingBot/actions/runs/31104263757)
- Run id: `31104263757`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T09:05:49.841518-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.59},"signals":0,"placed":0,"equity":143173.28,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":0,"filled_today":0,"unattributed_contracts":3,"top_signals":[],"github_run":"6246","github_run_id":"31104263757","status":"ok"}
```

### Live bot full output

```text
13:05:47  INFO      Mode: summary
13:05:48  INFO        Daily log -> logs/daily/2026-08-06.md
13:05:48  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.15|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $471.15|
|  Cash                                                           $282.79|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.36|
|  Open P&L                                                        $+1.08|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.54     $14.70   $14.68   -0.1%   $-0.10  |
|  AVB      Pullback50      $94.82     $187.24  $189.61  +1.3%   $+1.18  |
|                                                                        |
|  Total invested                                                 $188.36|
|  Total open P&L                                                  $+1.08|
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
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
|  2026-08-05  SELL  ALGN  Pullback50  $94.07  P&L $-0.77                |
|  2026-08-05  SELL  AMAT  Pullback50  $94.48  P&L $-0.32                |
|  2026-08-05  SELL  COHR  Pullback50  $72.51  P&L $-0.37                |
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=156 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T09:05:49.841518-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $143173.28, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,173.28                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             156                                     |
|  Broker option positions       26                                      |
|  Unattributed contracts        3 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1034  buckets=250  win=45%                           |
|  Returns   avg=+26.3%  med=-15.6%  p10=-73.8%  p90=+140.0%             |
|  Realized  $+11,975.32                                                 |
|  Raw incl dropped  trades=1568  real=$+10,379.77                       |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  4  50% +631.1 +566.7 +1446.7 $   +411        |
|  b196 lab0196_s218_w3_10  3 100% +453.8 +403.1 +906.2 $   +310         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 242 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (9)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN PLTR260807C00172500 x3 stop_loss (-54.4%)                 |
|  b802 S404 AMZN260807C00295000 x1 stop_loss (-90.1%)                   |
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b196 S218 RBLX260807C00040000 x1 stop_loss (-84.8%)                   |
|  b300 S353 AMZN260807C00292500 x1 stop_loss (-90.7%)                   |
|  ... 4 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (26)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -90.1%   $ -1,271.67               |
|  AMZN260807C00292500          20    -90.7%   $   -977.00               |
|  AMZN260807C00297500           9    -94.1%   $   -287.31               |
|  UBER260807C00078000           5    -98.0%   $   -247.67               |
|  DKNG260807C00024500           7    -59.4%   $   -163.80               |
|  NKE260807C00042000           10    +13.9%   $    +89.00               |
|  RBLX260807C00040000           3    -84.8%   $    -84.00               |
|  TTD260807P00017000            4    -34.5%   $    -76.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=1.0s reconcile=0.59s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.0s. run=#6246 https://github.com/28twagg-ops/TradingBot/actions/runs/31104263757
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 5 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=97 drop=8
Orphan rate: 5.6% (88/1568)
# Options signal frequency

_Generated 2026-08-06T09:05:53.992074_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |   442 | WARN | <<<
| Missing exit records (post) |   438 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  1013 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.15 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T131049Z

- UTC timestamp: `20260806T131049Z`
- GitHub run: [#6247](https://github.com/28twagg-ops/TradingBot/actions/runs/31104647044)
- Run id: `31104647044`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T09:10:53.877911-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.61},"signals":0,"placed":0,"equity":143173.28,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":0,"filled_today":0,"unattributed_contracts":3,"top_signals":[],"github_run":"6247","github_run_id":"31104647044","status":"ok"}
```

### Live bot full output

```text
13:10:50  INFO      Mode: summary
13:10:51  INFO        Daily log -> logs/daily/2026-08-06.md
13:10:51  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.15|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $471.15|
|  Cash                                                           $282.79|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.36|
|  Open P&L                                                        $+1.08|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.54     $14.70   $14.68   -0.1%   $-0.10  |
|  AVB      Pullback50      $94.82     $187.24  $189.61  +1.3%   $+1.18  |
|                                                                        |
|  Total invested                                                 $188.36|
|  Total open P&L                                                  $+1.08|
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
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
|  2026-08-05  SELL  ALGN  Pullback50  $94.07  P&L $-0.77                |
|  2026-08-05  SELL  AMAT  Pullback50  $94.48  P&L $-0.32                |
|  2026-08-05  SELL  COHR  Pullback50  $72.51  P&L $-0.37                |
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=156 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T09:10:53.877911-04:00 ===

[Run context]
After hours (09:10 ET) — exit summary only.
Paper auth OK — equity $143173.28, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,173.28                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             156                                     |
|  Broker option positions       26                                      |
|  Unattributed contracts        3 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1034  buckets=250  win=45%                           |
|  Returns   avg=+26.3%  med=-15.6%  p10=-73.8%  p90=+140.0%             |
|  Realized  $+11,975.32                                                 |
|  Raw incl dropped  trades=1568  real=$+10,379.77                       |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  4  50% +631.1 +566.7 +1446.7 $   +411        |
|  b196 lab0196_s218_w3_10  3 100% +453.8 +403.1 +906.2 $   +310         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 242 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (9)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN PLTR260807C00172500 x3 stop_loss (-54.4%)                 |
|  b802 S404 AMZN260807C00295000 x1 stop_loss (-90.1%)                   |
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b196 S218 RBLX260807C00040000 x1 stop_loss (-84.8%)                   |
|  b300 S353 AMZN260807C00292500 x1 stop_loss (-90.7%)                   |
|  ... 4 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (26)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -90.1%   $ -1,271.67               |
|  AMZN260807C00292500          20    -90.7%   $   -977.00               |
|  AMZN260807C00297500           9    -94.1%   $   -287.31               |
|  UBER260807C00078000           5    -98.0%   $   -247.67               |
|  DKNG260807C00024500           7    -59.4%   $   -163.80               |
|  NKE260807C00042000           10    +13.9%   $    +89.00               |
|  RBLX260807C00040000           3    -84.8%   $    -84.00               |
|  TTD260807P00017000            4    -34.5%   $    -76.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=1.2s reconcile=0.61s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.2s. run=#6247 https://github.com/28twagg-ops/TradingBot/actions/runs/31104647044
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 5 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=97 drop=8
Orphan rate: 5.6% (88/1568)
# Options signal frequency

_Generated 2026-08-06T09:11:00.384862_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |   442 | WARN | <<<
| Missing exit records (post) |   438 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  1013 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.15 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T131546Z

- UTC timestamp: `20260806T131546Z`
- GitHub run: [#6248](https://github.com/28twagg-ops/TradingBot/actions/runs/31105034687)
- Run id: `31105034687`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`11s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T09:15:51.719885-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.57},"signals":0,"placed":0,"equity":143221.4,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":0,"filled_today":0,"unattributed_contracts":3,"top_signals":[],"github_run":"6248","github_run_id":"31105034687","status":"ok"}
```

### Live bot full output

```text
13:15:47  INFO      Mode: summary
13:15:48  INFO        Daily log -> logs/daily/2026-08-06.md
13:15:48  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.15|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $471.15|
|  Cash                                                           $282.79|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.36|
|  Open P&L                                                        $+1.08|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.54     $14.70   $14.68   -0.1%   $-0.10  |
|  AVB      Pullback50      $94.82     $187.24  $189.61  +1.3%   $+1.18  |
|                                                                        |
|  Total invested                                                 $188.36|
|  Total open P&L                                                  $+1.08|
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
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
|  2026-08-05  SELL  ALGN  Pullback50  $94.07  P&L $-0.77                |
|  2026-08-05  SELL  AMAT  Pullback50  $94.48  P&L $-0.32                |
|  2026-08-05  SELL  COHR  Pullback50  $72.51  P&L $-0.37                |
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=156 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T09:15:51.719885-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $143221.40, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,221.40                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             156                                     |
|  Broker option positions       26                                      |
|  Unattributed contracts        3 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1034  buckets=250  win=45%                           |
|  Returns   avg=+26.3%  med=-15.6%  p10=-73.8%  p90=+140.0%             |
|  Realized  $+11,975.32                                                 |
|  Raw incl dropped  trades=1568  real=$+10,379.77                       |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  4  50% +631.1 +566.7 +1446.7 $   +411        |
|  b196 lab0196_s218_w3_10  3 100% +453.8 +403.1 +906.2 $   +310         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 242 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (9)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN PLTR260807C00172500 x3 stop_loss (-54.4%)                 |
|  b802 S404 AMZN260807C00295000 x1 stop_loss (-90.1%)                   |
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b196 S218 RBLX260807C00040000 x1 stop_loss (-84.8%)                   |
|  b300 S353 AMZN260807C00292500 x1 stop_loss (-90.7%)                   |
|  ... 4 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (26)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -90.1%   $ -1,271.67               |
|  AMZN260807C00292500          20    -90.7%   $   -977.00               |
|  AMZN260807C00297500           9    -94.1%   $   -287.31               |
|  UBER260807C00078000           5    -98.0%   $   -247.67               |
|  DKNG260807C00024500           7    -59.4%   $   -163.80               |
|  NKE260807C00042000           10    +13.9%   $    +89.00               |
|  RBLX260807C00040000           3    -84.8%   $    -84.00               |
|  TTD260807P00017000            4    -34.5%   $    -76.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=1.1s reconcile=0.57s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.1s. run=#6248 https://github.com/28twagg-ops/TradingBot/actions/runs/31105034687
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 5 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=97 drop=8
Orphan rate: 5.6% (88/1568)
# Options signal frequency

_Generated 2026-08-06T09:15:58.379503_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |   442 | WARN | <<<
| Missing exit records (post) |   438 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  1013 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.15 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T132046Z

- UTC timestamp: `20260806T132046Z`
- GitHub run: [#6249](https://github.com/28twagg-ops/TradingBot/actions/runs/31105418675)
- Run id: `31105418675`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T09:20:49.719533-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.14},"signals":0,"placed":0,"equity":143277.28,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":0,"filled_today":0,"unattributed_contracts":3,"top_signals":[],"github_run":"6249","github_run_id":"31105418675","status":"ok"}
```

### Live bot full output

```text
13:20:47  INFO      Mode: summary
13:20:47  INFO        Daily log -> logs/daily/2026-08-06.md
13:20:47  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.15|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $471.15|
|  Cash                                                           $282.79|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.36|
|  Open P&L                                                        $+1.08|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.54     $14.70   $14.68   -0.1%   $-0.10  |
|  AVB      Pullback50      $94.82     $187.24  $189.61  +1.3%   $+1.18  |
|                                                                        |
|  Total invested                                                 $188.36|
|  Total open P&L                                                  $+1.08|
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
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
|  2026-08-05  SELL  ALGN  Pullback50  $94.07  P&L $-0.77                |
|  2026-08-05  SELL  AMAT  Pullback50  $94.48  P&L $-0.32                |
|  2026-08-05  SELL  COHR  Pullback50  $72.51  P&L $-0.37                |
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=156 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T09:20:49.719533-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $143277.28, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,277.28                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             156                                     |
|  Broker option positions       26                                      |
|  Unattributed contracts        3 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1034  buckets=250  win=45%                           |
|  Returns   avg=+26.3%  med=-15.6%  p10=-73.8%  p90=+140.0%             |
|  Realized  $+11,975.32                                                 |
|  Raw incl dropped  trades=1568  real=$+10,379.77                       |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  4  50% +631.1 +566.7 +1446.7 $   +411        |
|  b196 lab0196_s218_w3_10  3 100% +453.8 +403.1 +906.2 $   +310         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 242 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (9)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN PLTR260807C00172500 x3 stop_loss (-54.4%)                 |
|  b802 S404 AMZN260807C00295000 x1 stop_loss (-90.1%)                   |
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b196 S218 RBLX260807C00040000 x1 stop_loss (-84.8%)                   |
|  b300 S353 AMZN260807C00292500 x1 stop_loss (-90.7%)                   |
|  ... 4 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (26)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -90.1%   $ -1,271.67               |
|  AMZN260807C00292500          20    -90.7%   $   -977.00               |
|  AMZN260807C00297500           9    -94.1%   $   -287.31               |
|  UBER260807C00078000           5    -98.0%   $   -247.67               |
|  DKNG260807C00024500           7    -59.4%   $   -163.80               |
|  NKE260807C00042000           10    +13.9%   $    +89.00               |
|  RBLX260807C00040000           3    -84.8%   $    -84.00               |
|  TTD260807P00017000            4    -34.5%   $    -76.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=0.6s reconcile=0.14s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.6s. run=#6249 https://github.com/28twagg-ops/TradingBot/actions/runs/31105418675
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 5 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=97 drop=8
Orphan rate: 5.6% (88/1568)
# Options signal frequency

_Generated 2026-08-06T09:20:55.843252_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |   442 | WARN | <<<
| Missing exit records (post) |   438 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  1013 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.15 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T132544Z

- UTC timestamp: `20260806T132544Z`
- GitHub run: [#6250](https://github.com/28twagg-ops/TradingBot/actions/runs/31105807813)
- Run id: `31105807813`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T09:25:47.012611-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":143264.28,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":0,"filled_today":0,"unattributed_contracts":3,"top_signals":[],"github_run":"6250","github_run_id":"31105807813","status":"ok"}
```

### Live bot full output

```text
13:25:44  INFO      Mode: summary
13:25:45  INFO        Daily log -> logs/daily/2026-08-06.md
13:25:45  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.15|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $471.15|
|  Cash                                                           $282.79|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $188.36|
|  Open P&L                                                        $+1.08|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (2 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.54     $14.70   $14.68   -0.1%   $-0.10  |
|  AVB      Pullback50      $94.82     $187.24  $189.61  +1.3%   $+1.18  |
|                                                                        |
|  Total invested                                                 $188.36|
|  Total open P&L                                                  $+1.08|
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
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
|  2026-08-05  SELL  ALGN  Pullback50  $94.07  P&L $-0.77                |
|  2026-08-05  SELL  AMAT  Pullback50  $94.48  P&L $-0.32                |
|  2026-08-05  SELL  COHR  Pullback50  $72.51  P&L $-0.37                |
|  2026-08-04  SELL  ECHO  MomReversal  $73.53  P&L $+4.48               |
|  2026-08-04  SELL  AMD  Pullback50  $96.71  P&L $+3.16                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=156 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T09:25:47.012611-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $143264.28, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,264.28                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             156                                     |
|  Broker option positions       26                                      |
|  Unattributed contracts        3 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1034  buckets=250  win=45%                           |
|  Returns   avg=+26.3%  med=-15.6%  p10=-73.8%  p90=+140.0%             |
|  Realized  $+11,975.32                                                 |
|  Raw incl dropped  trades=1568  real=$+10,379.77                       |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  4  50% +631.1 +566.7 +1446.7 $   +411        |
|  b196 lab0196_s218_w3_10  3 100% +453.8 +403.1 +906.2 $   +310         |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  ... 242 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (9)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN PLTR260807C00172500 x3 stop_loss (-54.4%)                 |
|  b802 S404 AMZN260807C00295000 x1 stop_loss (-90.1%)                   |
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b196 S218 RBLX260807C00040000 x1 stop_loss (-84.8%)                   |
|  b300 S353 AMZN260807C00292500 x1 stop_loss (-90.7%)                   |
|  ... 4 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (26)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          35    -90.1%   $ -1,271.67               |
|  AMZN260807C00292500          20    -90.7%   $   -977.00               |
|  AMZN260807C00297500           9    -94.1%   $   -287.31               |
|  UBER260807C00078000           5    -98.0%   $   -247.67               |
|  DKNG260807C00024500           7    -59.4%   $   -163.80               |
|  NKE260807C00042000           10    +13.9%   $    +89.00               |
|  RBLX260807C00040000           3    -84.8%   $    -84.00               |
|  TTD260807P00017000            4    -34.5%   $    -76.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=0.5s reconcile=0.13s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.5s. run=#6250 https://github.com/28twagg-ops/TradingBot/actions/runs/31105807813
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 5 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=97 drop=8
Orphan rate: 5.6% (88/1568)
# Options signal frequency

_Generated 2026-08-06T09:25:53.073627_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     2 | WARN | <<<
| Orphaned lots (post-stable) |   442 | WARN | <<<
| Missing exit records (post) |   438 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  1013 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.15 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T133051Z

- UTC timestamp: `20260806T133051Z`
- GitHub run: [#6251](https://github.com/28twagg-ops/TradingBot/actions/runs/31106199390)
- Run id: `31106199390`
- Live bot: exit=`0`, duration=`217s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T09:25:47.012611-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":143264.28,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":0,"filled_today":0,"unattributed_contracts":3,"top_signals":[],"github_run":"6250","github_run_id":"31105807813","status":"ok"}
```

### Live bot full output

```text
13:30:53  INFO      Mode: morning_prep
13:30:54  INFO        [prep_positions] 2/2 (2 valid)
13:30:54  INFO      Fetching tickers (universe=both)...
13:30:54  INFO        S&P 500: 503
13:30:55  INFO        MidCap 400: 400
13:30:55  INFO        Total: 903 tickers
13:30:57  INFO        [prep_universe] 40/901 (40 valid)
13:30:59  INFO        [prep_universe] 80/901 (80 valid)
13:31:02  INFO        [prep_universe] 120/901 (120 valid)
13:31:03  INFO        [prep_universe] 160/901 (160 valid)
13:31:05  INFO        [prep_universe] 200/901 (199 valid)
13:31:09  INFO        [prep_universe] 240/901 (238 valid)
13:31:20  INFO        [prep_universe] 280/901 (278 valid)
13:31:33  INFO        [prep_universe] 320/901 (318 valid)
13:31:45  INFO        [prep_universe] 360/901 (358 valid)
13:31:55  INFO        [prep_universe] 400/901 (397 valid)
13:32:08  INFO        [prep_universe] 440/901 (437 valid)
13:32:19  INFO        [prep_universe] 480/901 (477 valid)
13:32:32  INFO        [prep_universe] 520/901 (517 valid)
13:32:43  INFO        [prep_universe] 560/901 (557 valid)
13:32:57  INFO        [prep_universe] 600/901 (597 valid)
13:33:08  INFO        [prep_universe] 640/901 (637 valid)
13:33:19  INFO        [prep_universe] 680/901 (677 valid)
13:33:32  INFO        [prep_universe] 720/901 (717 valid)
13:33:46  INFO        [prep_universe] 760/901 (757 valid)
13:33:56  INFO        [prep_universe] 800/901 (797 valid)
13:34:07  INFO        [prep_universe] 840/901 (836 valid)
13:34:21  INFO        [prep_universe] 880/901 (876 valid)
13:34:25  INFO        [prep_universe] 901/901 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.00|
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
|  Invested                                                       $189.21|
|  Open P&L                                                        $+1.93|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.63     $14.70   $14.70   -0.0%   $-0.01  |
|  AVB      Pullback50      $95.58     $187.24  $191.12  +2.1%   $+1.94  |
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
|  Exit candidates                                                      2|
|  Signal candidates                                                   28|
|  Universe scanned                                                   901|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=156 paper_keys=yes dry_run=False
  alpaca positions=27
  FLAG b0|ORPHAN|a20b38ca missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T09:34:30.613047-04:00 ===

[Run context]
Paper auth OK — equity $139851.07, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 09:34:36,058 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-87.5%) SELL 1 HOOD260807C00101000 @<= 0.07
2026-08-06 09:34:38,095 INFO   EXIT [b799|lab0799_s399_w4_1120_1135_r2|S399] stop_loss (-83.6%) SELL 1 AMD260807C00555000 @<= 0.07
2026-08-06 09:34:38,556 INFO   EXIT [b96|lab0096_s211_w2_1005_1045_r1|S211] stop_loss (-97.1%) SELL 1 AMZN260807C00297500 @<= 0.02
  EXIT [b366|lab0366_s361_w3_1045_1120_r1|S361] stop_loss (-82.2%) SELL failed DKNG260807C00024500: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-06 09:34:38,959 INFO   EXIT [b352|lab0352_s360_w3_1045_1120_r1|S360] stop_loss (-82.2%) SELL 1 DKNG260807C00024500 @<= 0.04
2026-08-06 09:34:39,647 INFO   EXIT [b171|lab0171_s216_w4_1120_1135_r2|S216] stop_loss (-75.0%) SELL 1 HOOD260807C00100000 @<= 0.11
  EXIT [b803|lab0803_s404_w2_1005_1045_r2|S404] stop_loss (-95.0%) SELL failed AMZN260807C00295000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-06 09:34:40,338 INFO   EXIT [b779|lab0779_s397_w2_1005_1045_r2|S397] stop_loss (-95.0%) SELL 1 AMZN260807C00295000 @<= 0.03
  EXIT [b301|lab0301_s353_w3_1045_1120_r2|S353] stop_loss (-94.4%) SELL failed AMZN260807C00292500: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-06 09:34:40,984 INFO   EXIT [b805|lab0805_s404_w3_1045_1120_r2|S404] stop_loss (-94.4%) SELL 1 AMZN260807C00292500 @<= 0.04
  EXIT [b112|lab0112_s212_w3_1045_1120_r1|S212] stop_loss (-100.0%) SELL failed UBER260807C00078000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-06 09:34:41,413 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-100.0%) SELL 3 UBER260807C00078000 @<= 0.01
2026-08-06 09:34:41,631 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+84.1%) SELL 2 T260807C00022500 @<= 0.82
2026-08-06 09:34:42,294 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-52.2%) SELL 2 TTD260807C00021500 @<= 0.19
2026-08-06 09:34:42,702 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-97.0%) SELL 2 RBLX260807C00040000 @<= 0.01
2026-08-06 09:34:43,377 INFO   EXIT [b115|lab0115_s212_w4_1120_1135_r2|S212] take_profit (+134.9%) SELL 1 AAPL260807C00317500 @<= 1.55

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260806T134117Z

- UTC timestamp: `20260806T134117Z`
- GitHub run: [#6253](https://github.com/28twagg-ops/TradingBot/actions/runs/31107000531)
- Run id: `31107000531`
- Live bot: exit=`0`, duration=`217s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T09:25:47.012611-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":143264.28,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":0,"filled_today":0,"unattributed_contracts":3,"top_signals":[],"github_run":"6250","github_run_id":"31105807813","status":"ok"}
```

### Live bot full output

```text
13:41:18  INFO      Mode: morning_prep
13:41:19  INFO        [prep_positions] 2/2 (2 valid)
13:41:19  INFO        Universe cache hit: 903 tickers (tickers_2026-08-06.json)
13:41:20  INFO        [prep_universe] 40/901 (40 valid)
13:41:21  INFO        [prep_universe] 80/901 (80 valid)
13:41:22  INFO        [prep_universe] 120/901 (120 valid)
13:41:23  INFO        [prep_universe] 160/901 (160 valid)
13:41:25  INFO        [prep_universe] 200/901 (199 valid)
13:41:32  INFO        [prep_universe] 240/901 (238 valid)
13:41:45  INFO        [prep_universe] 280/901 (278 valid)
13:41:59  INFO        [prep_universe] 320/901 (318 valid)
13:42:09  INFO        [prep_universe] 360/901 (358 valid)
13:42:22  INFO        [prep_universe] 400/901 (397 valid)
13:42:32  INFO        [prep_universe] 440/901 (437 valid)
13:42:45  INFO        [prep_universe] 480/901 (477 valid)
13:42:56  INFO        [prep_universe] 520/901 (517 valid)
13:43:09  INFO        [prep_universe] 560/901 (557 valid)
13:43:19  INFO        [prep_universe] 600/901 (597 valid)
13:43:32  INFO        [prep_universe] 640/901 (637 valid)
13:43:45  INFO        [prep_universe] 680/901 (677 valid)
13:43:58  INFO        [prep_universe] 720/901 (717 valid)
13:44:09  INFO        [prep_universe] 760/901 (757 valid)
13:44:22  INFO        [prep_universe] 800/901 (797 valid)
13:44:32  INFO        [prep_universe] 840/901 (836 valid)
13:44:45  INFO        [prep_universe] 880/901 (876 valid)
13:44:51  INFO        [prep_universe] 901/901 (897 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.15|
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
|  Invested                                                       $188.36|
|  Open P&L                                                        $+1.08|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AES      Pullback50      $93.60     $14.70   $14.69   -0.0%   $-0.04  |
|  AVB      Pullback50      $94.76     $187.24  $189.48  +1.2%   $+1.12  |
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
|  Exit candidates                                                      2|
|  Signal candidates                                                   19|
|  Universe scanned                                                   901|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=142 paper_keys=yes dry_run=False
  alpaca positions=23
  FLAG b171|S216|60327813 missing from Alpaca
  FLAG b170|S216|90e2384d missing from Alpaca
  FLAG b799|S399|243b5e9d missing from Alpaca
  FLAG b798|S399|13277a79 missing from Alpaca
  FLAG b115|S212|3b5b77dc missing from Alpaca
  FLAG b0|ORPHAN|ffafb5bd missing from Alpaca
  FLAG b0|ORPHAN|7933dacc missing from Alpaca
  FLAG b0|ORPHAN|c400d933 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T09:44:56.082389-04:00 ===

[Run context]
Paper auth OK — equity $141347.60, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
  EXIT [b112|lab0112_s212_w3_1045_1120_r1|S212] stop_loss (-100.0%) SELL failed UBER260807C00078000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b301|lab0301_s353_w3_1045_1120_r2|S353] stop_loss (-94.4%) SELL failed AMZN260807C00292500: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-06 09:44:57,619 INFO   EXIT [b781|lab0781_s397_w3_1045_1120_r2|S397] stop_loss (-94.4%) SELL 1 AMZN260807C00292500 @<= 0.04
2026-08-06 09:44:57,930 INFO   EXIT [b425|lab0425_s365_w4_1120_1135_r2|S365] take_profit (+59.0%) SELL 1 AAPL260814C00330000 @<= 0.96

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260806T134625Z

- UTC timestamp: `20260806T134625Z`
- GitHub run: [#6254](https://github.com/28twagg-ops/TradingBot/actions/runs/31107398964)
- Run id: `31107398964`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T09:25:47.012611-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":143264.28,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":0,"filled_today":0,"unattributed_contracts":3,"top_signals":[],"github_run":"6250","github_run_id":"31105807813","status":"ok"}
```

### Live bot full output

```text
13:46:26  INFO      Mode: morning_scan
13:46:28  INFO        [positions] 2/2 (2 valid)
13:46:28  INFO        SELL LIMIT AES  qty=6.37180185  limit=$14.68  id=a0aa1ea0-b54c-4a5c-8f97-a4980ece3847
13:46:48  INFO        SELL LIMIT filled AES (confirmed by position check)
13:46:49  INFO        TX logged: SELL AES  P&L -0.11%
13:46:49  INFO        SELL LIMIT AVB  qty=0.500096131  limit=$188.94  id=ace64a11-749d-4c83-9ef7-22ddc9d4210b
13:47:09  INFO        SELL LIMIT filled AVB (confirmed by position check)
13:47:09  INFO        TX logged: SELL AVB  P&L 1.12%
13:47:09  INFO        Universe cache hit: 903 tickers (tickers_2026-08-06.json)
13:47:11  INFO        [universe] 40/903 (40 valid)
13:47:13  INFO        [universe] 80/903 (80 valid)
13:47:15  INFO        [universe] 120/903 (120 valid)
13:47:16  INFO        [universe] 160/903 (160 valid)
13:47:17  INFO        [universe] 200/903 (199 valid)
13:47:25  INFO        [universe] 240/903 (238 valid)
13:47:35  INFO        [universe] 280/903 (278 valid)
13:47:46  INFO        [universe] 320/903 (318 valid)
13:48:00  INFO        [universe] 360/903 (358 valid)
13:48:11  INFO        [universe] 400/903 (397 valid)
13:48:24  INFO        [universe] 440/903 (437 valid)
13:48:35  INFO        [universe] 480/903 (477 valid)
13:48:48  INFO        [universe] 520/903 (517 valid)
13:48:59  INFO        [universe] 560/903 (557 valid)
13:49:12  INFO        [universe] 600/903 (597 valid)
13:49:22  INFO        [universe] 640/903 (637 valid)
13:49:36  INFO        [universe] 680/903 (677 valid)
13:49:47  INFO        [universe] 720/903 (717 valid)
13:50:00  INFO        [universe] 760/903 (757 valid)
13:50:11  INFO        [universe] 800/903 (797 valid)
```

### Options bot full output

```text

## Run 20260806T135109Z

- UTC timestamp: `20260806T135109Z`
- GitHub run: [#6255](https://github.com/28twagg-ops/TradingBot/actions/runs/31107802441)
- Run id: `31107802441`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T09:25:47.012611-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":143264.28,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":0,"filled_today":0,"unattributed_contracts":3,"top_signals":[],"github_run":"6250","github_run_id":"31105807813","status":"ok"}
```

### Live bot full output

```text
13:51:10  INFO      Mode: morning_scan
13:51:11  INFO        Universe cache hit: 903 tickers (tickers_2026-08-06.json)
13:51:13  INFO        [universe] 40/903 (40 valid)
13:51:15  INFO        [universe] 80/903 (80 valid)
13:51:16  INFO        [universe] 120/903 (120 valid)
13:51:17  INFO        [universe] 160/903 (160 valid)
13:51:28  INFO        [universe] 200/903 (199 valid)
13:51:39  INFO        [universe] 240/903 (238 valid)
13:51:50  INFO        [universe] 280/903 (278 valid)
13:52:03  INFO        [universe] 320/903 (318 valid)
13:52:14  INFO        [universe] 360/903 (358 valid)
13:52:27  INFO        [universe] 400/903 (397 valid)
13:52:38  INFO        [universe] 440/903 (437 valid)
13:52:52  INFO        [universe] 480/903 (477 valid)
13:53:02  INFO        [universe] 520/903 (517 valid)
13:53:16  INFO        [universe] 560/903 (557 valid)
13:53:27  INFO        [universe] 600/903 (597 valid)
13:53:40  INFO        [universe] 640/903 (637 valid)
13:53:51  INFO        [universe] 680/903 (677 valid)
13:54:02  INFO        [universe] 720/903 (717 valid)
13:54:15  INFO        [universe] 760/903 (757 valid)
13:54:26  INFO        [universe] 800/903 (797 valid)
13:54:39  INFO        [universe] 840/903 (836 valid)
13:54:50  INFO        [universe] 880/903 (876 valid)
13:54:57  INFO        [universe] 903/903 (899 valid)
13:55:00  INFO        BUY  DOV  $94.19  [Pullback50]  id=320a1116-d8fb-4f27-aac2-3277b32474ee
13:55:00  INFO        BUY  GEV  $94.19  [Pullback50]  id=986a63de-4e3b-4266-8827-bf73a705a174
13:55:00  INFO        BUY  GS  $94.19  [Pullback50]  id=399399d4-250a-469a-95d7-31f1530990e4
13:55:00  INFO        BUY  JBL  $94.19  [Pullback50]  id=5f6558da-80e7-4e83-943e-75d3d9199627
13:55:00  INFO        BUY  PWR  $70.64  [Pullback50]  id=656c979b-1400-486a-a450-003b355a94a9

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.93|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-06|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $470.93|
|  Cash                                                           $470.93|
|  Reserve                                          $23.55  (always kept)|
|  Available                                    $447.38  (for new trades)|
|  Trade size             $94.19  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (0 open)                           |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
|  Buys today: 0  |  entry cap: 5  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (40325.7m))|
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
|                         SIGNALS FOUND  --  17                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  DOV      Pullback50      eq     $213.53  49.4   -1.42   50MA bounce (-|
|  GEV      Pullback50      eq     $1025.~  46.2   -2.48   50MA bounce (+|
|  GS       Pullback50      eq     $1063.~  49.7   -2.42   50MA bounce (+|
|  JBL      Pullback50      eq     $344.38  68.5   -2.85   50MA bounce (-|
|  PWR      Pullback50      eq     $682.50  60.4   -1.68   50MA bounce (+|
|  SWKS     Pullback50      eq     $67.53   67.4   -1.72   50MA bounce (-|
|  TRGP     Pullback50      eq     $269.32  38.7   -2.63   50MA bounce (+|
|  TER      Pullback50      eq     $385.20  64.2   -1.70   50MA bounce (+|
|  WMB      Pullback50      eq     $73.09   48.9   -2.52   50MA bounce (-|
|  BWA      Pullback50      eq     $67.32   67.9   -2.16   50MA bounce (-|
|  CVLT     Pullback50      eq     $133.24  39.2   -1.51   50MA bounce (-|
|  CW       Pullback50      eq     $749.41  60.3   -2.12   50MA bounce (+|
|  ENTG     Pullback50      eq     $143.57  52.8   -2.15   50MA bounce (-|
|  EXEL     Pullback50      eq     $54.40   44.9   -2.06   50MA bounce (+|
|  NWE      Pullback50      eq     $70.23   39.3   -2.53   50MA bounce (-|
|  SLAB     Pullback50      eq     $218.74  63.3   -2.63   50MA bounce (+|
|  TEX      Pullback50      eq     $66.12   51.8   -1.92   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] DOV  Pullback50                                    $94.19|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] GEV  Pullback50                                    $94.19|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] GS  Pullback50                                     $94.19|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] JBL  Pullback50                                    $94.19|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] PWR  Pullback50                                    $70.64|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] SWKS  Pullback50                                     cap 5|
|    SKIP [eq] TRGP  Pullback50                                     cap 5|
|    SKIP [eq] TER  Pullback50                                      cap 5|
|    SKIP [eq] WMB  Pullback50                                      cap 5|
|    SKIP [eq] BWA  Pullback50                                      cap 5|
|    SKIP [eq] CVLT  Pullback50                                     cap 5|
|    SKIP [eq] CW  Pullback50                                       cap 5|
|    SKIP [eq] ENTG  Pullback50                                     cap 5|
|    SKIP [eq] EXEL  Pullback50                                     cap 5|
|    SKIP [eq] NWE  Pullback50                                      cap 5|
|    SKIP [eq] SLAB  Pullback50                                     cap 5|
|    SKIP [eq] TEX  Pullback50                                      cap 5|

+========================================================================+
|                         BUY FILL CONFIRMATION                          |
+========================================================================+
|  Pending submits                                                      5|```

### Options bot full output

```text

## Run 20260806T135947Z

- UTC timestamp: `20260806T135947Z`
- GitHub run: [#6256](https://github.com/28twagg-ops/TradingBot/actions/runs/31108211308)
- Run id: `31108211308`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T09:25:47.012611-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":143264.28,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":0,"filled_today":0,"unattributed_contracts":3,"top_signals":[],"github_run":"6250","github_run_id":"31105807813","status":"ok"}
```

### Live bot full output

```text
13:59:48  INFO      Mode: morning_scan
13:59:48  INFO        [positions] 5/5 (5 valid)
13:59:48  INFO        SELL LIMIT DOV  qty=0.440517507  limit=$213.12  id=33470aaa-25c0-45bd-a7c7-637095c185eb
14:00:18  INFO        SELL LIMIT filled DOV (confirmed by position check)
14:00:18  INFO        TX logged: SELL DOV  P&L -0.11%
14:00:18  INFO        SELL LIMIT GS  qty=0.088675219  limit=$1061.27  id=ed40fd94-b97d-44c1-a5b5-26408670d53c
14:00:48  INFO        SELL LIMIT filled GS (confirmed by position check)
14:00:49  INFO        TX logged: SELL GS  P&L 0.14%
14:00:49  INFO        SELL LIMIT PWR  qty=0.103661847  limit=$682.24  id=918e93f2-7abf-472b-9d6a-d3368600421c
```

### Options bot full output

```text

## Run 20260806T140644Z

- UTC timestamp: `20260806T140644Z`
- GitHub run: [#6258](https://github.com/28twagg-ops/TradingBot/actions/runs/31109042791)
- Run id: `31109042791`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T09:25:47.012611-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":143264.28,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":0,"filled_today":0,"unattributed_contracts":3,"top_signals":[],"github_run":"6250","github_run_id":"31105807813","status":"ok"}
```

### Live bot full output

```text
14:06:45  INFO      Mode: exits
14:06:46  INFO        Daily log -> logs/daily/2026-08-06.md
14:06:46  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
14:06:46  INFO        place_all_stops: checking 2 positions...
14:06:46  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
14:06:46  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
14:06:46  INFO        [positions] 2/2 (2 valid)
14:06:47  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.22|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +0.6%  $+0.54                                            HOLD|
|  JBL  P&L +0.8%  $+0.79                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=142 paper_keys=yes dry_run=False
  alpaca positions=23
  FLAG b171|S216|60327813 missing from Alpaca
  FLAG b170|S216|90e2384d missing from Alpaca
  FLAG b799|S399|243b5e9d missing from Alpaca
  FLAG b798|S399|13277a79 missing from Alpaca
  FLAG b115|S212|3b5b77dc missing from Alpaca
  FLAG b0|ORPHAN|ffafb5bd missing from Alpaca
  FLAG b0|ORPHAN|7933dacc missing from Alpaca
  FLAG b0|ORPHAN|c400d933 missing from Alpaca
  FLAG b0|ORPHAN|096ba088 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T10:06:48.993212-04:00 ===

[Run context]
Paper auth OK — equity $143932.43, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
  EXIT [b112|lab0112_s212_w3_1045_1120_r1|S212] stop_loss (-98.0%) SELL failed UBER260807C00078000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b366|lab0366_s361_w3_1045_1120_r1|S361] stop_loss (-67.0%) SELL failed DKNG260807C00024500: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-06 10:06:56,171 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-67.0%) SELL 2 DKNG260807C00024500 @<= 0.14
  EXIT [b301|lab0301_s353_w3_1045_1120_r2|S353] stop_loss (-96.3%) SELL failed AMZN260807C00292500: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-06 10:06:56,799 INFO   EXIT [b780|lab0780_s397_w3_1045_1120_r1|S397] stop_loss (-96.3%) SELL 1 AMZN260807C00292500 @<= 0.03
2026-08-06 10:06:57,604 INFO   EXIT [b790|lab0790_s398_w4_1120_1135_r1|S398] take_profit (+61.3%) SELL 1 UBER260807C00070000 @<= 0.52

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 814 signal(s); top: ['S165:AMD', 'S165:COIN', 'S165:CRWD', 'S165:SNOW', 'S165:MARA', 'S165:MSTR', 'S165:ARM', 'S165:PANW']
Paper lab: $144429 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260806T140939Z

- UTC timestamp: `20260806T140939Z`
- GitHub run: [#6259](https://github.com/28twagg-ops/TradingBot/actions/runs/31109329609)
- Run id: `31109329609`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T09:25:47.012611-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":143264.28,"open_positions":26,"pending_orders":0,"open_lots":156,"submitted_today":0,"filled_today":0,"unattributed_contracts":3,"top_signals":[],"github_run":"6250","github_run_id":"31105807813","status":"ok"}
```

### Live bot full output

```text
14:09:40  INFO      Mode: exits
14:09:42  INFO        Daily log -> logs/daily/2026-08-06.md
14:09:42  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
14:09:42  INFO        place_all_stops: checking 2 positions...
14:09:42  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
14:09:42  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
14:09:42  INFO        [positions] 2/2 (2 valid)
14:09:42  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:09 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.62|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +1.2%  $+1.09                                            HOLD|
|  JBL  P&L +1.7%  $+1.64                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=142 paper_keys=yes dry_run=False
  alpaca positions=26
  FLAG b171|S216|60327813 missing from Alpaca
  FLAG b170|S216|90e2384d missing from Alpaca
  FLAG b799|S399|243b5e9d missing from Alpaca
  FLAG b798|S399|13277a79 missing from Alpaca
  FLAG b115|S212|3b5b77dc missing from Alpaca
  FLAG b0|ORPHAN|ffafb5bd missing from Alpaca
  FLAG b0|ORPHAN|7933dacc missing from Alpaca
  FLAG b0|ORPHAN|c400d933 missing from Alpaca
  FLAG b0|ORPHAN|096ba088 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T10:09:45.264156-04:00 ===

[Run context]
Paper auth OK — equity $144383.11, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 10:09:53,681 INFO   EXIT [b113|lab0113_s212_w3_1045_1120_r2|S212] stop_loss (-98.0%) SELL 1 UBER260807C00078000 @<= 0.02
2026-08-06 10:09:57,990 INFO   EXIT [b303|lab0303_s353_w4_1120_1135_r2|S353] take_profit (+70.6%) SELL 1 UBER260807C00070000 @<= 0.56

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260806T141147Z

- UTC timestamp: `20260806T141147Z`
- GitHub run: [#6260](https://github.com/28twagg-ops/TradingBot/actions/runs/31109453007)
- Run id: `31109453007`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`172s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T10:11:51.716425-04:00","date":"2026-08-06","mode":"entry+manage","header":"entry+manage (14 new)","elapsed_s":162.9,"phases_s":{"reconcile":4.26,"cancel":0.02,"manage":9.42,"scan":67.88,"entries":78.23,"reconcile2":2.46},"signals":850,"placed":14,"equity":145089.53,"open_positions":31,"pending_orders":9,"open_lots":156,"submitted_today":40,"filled_today":37,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:COIN","S165:CRWD","S165:SNOW","S165:MARA","S165:MSTR","S165:ARM","S165:PANW"],"github_run":"6260","github_run_id":"31109453007","status":"ok"}
```

### Live bot full output

```text
14:11:48  INFO      Mode: exits
14:11:49  INFO        Daily log -> logs/daily/2026-08-06.md
14:11:49  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
14:11:49  INFO        place_all_stops: checking 2 positions...
14:11:49  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
14:11:49  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
14:11:49  INFO        [positions] 2/2 (2 valid)
14:11:49  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.66|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +1.1%  $+1.08                                            HOLD|
|  JBL  P&L +1.8%  $+1.69                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=130 paper_keys=yes dry_run=False
  alpaca positions=28
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T10:11:51.716425-04:00 ===

[Run context]
Paper auth OK — equity $145089.53, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 10:11:57,332 INFO   EXIT [b302|lab0302_s353_w4_1120_1135_r1|S353] take_profit (+76.8%) SELL 1 UBER260807C00070000 @<= 0.54

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 850 signal(s); top: ['S165:AMD', 'S165:COIN', 'S165:CRWD', 'S165:SNOW', 'S165:MARA', 'S165:MSTR', 'S165:ARM', 'S165:PANW']
Paper lab: $145639 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 286 no tradeable call, 184 already attempted today, 255 pending order
Placed 14 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $145,089.53                             |
|  Signals this run              850                                     |
|  Orders submitted (session)    40                                      |
|  Orders filled today (ledger)  37                                      |
|  Entries placed this run       14                                      |
|  Open virtual lots             156                                     |
|  Broker option positions       31                                      |
|  Pending orders                9                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1112  buckets=255  win=44%                           |
|  Returns   avg=+25.7%  med=-18.2%  p10=-75.6%  p90=+138.6%             |
|  Realized  $+11,994.46                                                 |
|  Raw incl dropped  trades=1646  real=$+10,398.91                       |
|  Today     trades=22  avg=-46.5%  med=-87.0%  real=$-597.85            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  5  60% +695.8 +954.5 +1446.7 $   +621        |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  6 100% +295.8 +273.1 +815.4 $   +602         |
|  ... 247 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (9)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S355:MARA(2), S361:MARA(2), S217:RBLX(2)|
+------------------------------------------------------------------------+
|  b314 S355 MARA     limit=0.48                                         |
|  b315 S355 MARA     limit=0.48                                         |
|  b364 S361 MARA     limit=0.22                                         |
|  b365 S361 MARA     limit=0.22                                         |
|  b180 S217 RBLX     limit=0.37                                         |
|  ... 4 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (5)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b0   ORPHAN DKNG260807C00024500 x2 stop_loss (-67.0%)                 |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (31)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34    -97.5%   $ -1,337.33               |
|  AMZN260807C00292500          16    -96.3%   $   -829.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260807C00042000           10    -29.8%   $   -191.00               |
|  UBER260807C00070000           6    +80.0%   $   +154.62               |
|  NKE260828C00045000           12    -19.3%   $   -146.00               |
|  TTD260807C00020500            4    -47.8%   $   -128.00               |
|  NKE260821C00044000           12    -14.3%   $   -108.00               |
|  ... 23 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=162.9s reconcile=4.26s cancel=0.02s manage=9.42s scan=67.88s entries=78.23s
STATUS: options_morning_bot run complete (PAPER) elapsed=162.9s. run=#6260 https://github.com/28twagg-ops/TradingBot/actions/runs/31109453007
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 17 buckets closed trades, $-597.85 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=95 drop=10
Orphan rate: 6.3% (103/1646)
# Options signal frequency

_Generated 2026-08-06T10:14:40.373539_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   441 | WARN | <<<
| Missing exit records (post) |   438 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  1076 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.66 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T141555Z

- UTC timestamp: `20260806T141555Z`
- GitHub run: [#6261](https://github.com/28twagg-ops/TradingBot/actions/runs/31109875389)
- Run id: `31109875389`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`145s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T10:15:58.980070-04:00","date":"2026-08-06","mode":"entry+manage","header":"entry+manage (5 new)","elapsed_s":137.2,"phases_s":{"reconcile":0.34,"cancel":0.03,"manage":15.99,"scan":62.95,"entries":56.81,"reconcile2":0.57},"signals":853,"placed":5,"equity":145504.33,"open_positions":34,"pending_orders":9,"open_lots":154,"submitted_today":45,"filled_today":42,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:COIN","S165:CRWD","S165:SNOW","S165:MARA","S165:MSTR","S165:ARM","S165:PANW"],"github_run":"6261","github_run_id":"31109875389","status":"ok"}
```

### Live bot full output

```text
14:15:56  INFO      Mode: exits
14:15:56  INFO        Daily log -> logs/daily/2026-08-06.md
14:15:56  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
14:15:56  INFO        place_all_stops: checking 2 positions...
14:15:56  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
14:15:56  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
14:15:56  INFO        [positions] 2/2 (2 valid)
14:15:56  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.78|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +1.4%  $+1.34                                            HOLD|
|  JBL  P&L +1.6%  $+1.54                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=156 paper_keys=yes dry_run=False
  alpaca positions=34
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T10:15:58.980070-04:00 ===

[Run context]
Paper auth OK — equity $145504.33, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 10:15:59,837 INFO   EXIT [b293|lab0293_s352_w3_1045_1120_r2|S352] take_profit (+98.6%) SELL 1 UBER260807C00070000 @<= 0.61
2026-08-06 10:16:01,575 INFO   EXIT [b317|lab0317_s355_w3_1045_1120_r2|S355] take_profit (+55.3%) SELL 1 UBER260814C00072000 @<= 0.63
2026-08-06 10:16:02,777 INFO   EXIT [b353|lab0353_s360_w3_1045_1120_r2|S360] stop_loss (-64.5%) SELL 1 DKNG260807C00024500 @<= 0.15
2026-08-06 10:16:06,775 INFO   EXIT [b903|lab0903_s411_w3_1045_1120_r2|S411] stop_loss (-50.7%) SELL 1 TTD260807C00020500 @<= 0.34

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 853 signal(s); top: ['S165:AMD', 'S165:COIN', 'S165:CRWD', 'S165:SNOW', 'S165:MARA', 'S165:MSTR', 'S165:ARM', 'S165:PANW']
Paper lab: $145730 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 246 no tradeable call, 275 already attempted today, 132 pending order
Placed 5 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $145,504.33                             |
|  Signals this run              853                                     |
|  Orders submitted (session)    45                                      |
|  Orders filled today (ledger)  42                                      |
|  Entries placed this run       5                                       |
|  Open virtual lots             154                                     |
|  Broker option positions       34                                      |
|  Pending orders                9                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1120  buckets=255  win=43%                           |
|  Returns   avg=+25.4%  med=-18.7%  p10=-75.7%  p90=+138.6%             |
|  Realized  $+11,857.46                                                 |
|  Raw incl dropped  trades=1654  real=$+10,261.91                       |
|  Today     trades=27  avg=-37.9%  med=-82.8%  real=$-672.85            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  5  60% +695.8 +954.5 +1446.7 $   +621        |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  6 100% +295.8 +273.1 +815.4 $   +602         |
|  ... 247 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (9)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S355:MARA(2), S361:MARA(2), S203:COP(2) |
+------------------------------------------------------------------------+
|  b314 S355 MARA     limit=0.48                                         |
|  b315 S355 MARA     limit=0.48                                         |
|  b364 S361 MARA     limit=0.22                                         |
|  b365 S361 MARA     limit=0.22                                         |
|  b786 S398 CRWD     limit=0.42                                         |
|  ... 4 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (4)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (34)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34    -97.5%   $ -1,337.33               |
|  AMZN260807C00292500          16    -96.3%   $   -829.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260807C00042000           10    -26.7%   $   -171.00               |
|  UBER260807C00070000           5    +98.6%   $   +158.85               |
|  NKE260828C00045000           12    -17.7%   $   -134.00               |
|  TTD260807C00020500            3    -49.3%   $    -99.00               |
|  NKE260821C00044000           12    -11.1%   $    -84.00               |
|  ... 26 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=137.2s reconcile=0.34s cancel=0.03s manage=15.99s scan=62.95s entries=56.81s
STATUS: options_morning_bot run complete (PAPER) elapsed=137.2s. run=#6261 https://github.com/28twagg-ops/TradingBot/actions/runs/31109875389
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 20 buckets closed trades, $-672.85 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=95 drop=10
Orphan rate: 6.3% (104/1654)
# Options signal frequency

_Generated 2026-08-06T10:18:21.710970_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   441 | WARN | <<<
| Missing exit records (post) |   438 | WARN | <<<
| State/ledger mismatches     |    17 | WARN | <<<
| Total open lots             |   154 | INFO |
| Total closed lots           |  1083 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.78 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T142044Z

- UTC timestamp: `20260806T142044Z`
- GitHub run: [#6262](https://github.com/28twagg-ops/TradingBot/actions/runs/31110291474)
- Run id: `31110291474`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`138s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T10:20:47.849022-04:00","date":"2026-08-06","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":130.2,"phases_s":{"reconcile":0.13,"cancel":0.03,"manage":16.73,"scan":57.62,"entries":54.6,"reconcile2":0.35},"signals":884,"placed":0,"equity":145606.16,"open_positions":35,"pending_orders":7,"open_lots":154,"submitted_today":45,"filled_today":44,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:COIN","S165:CRWD","S165:SNOW","S165:MARA","S165:MSTR","S165:ARM","S165:PANW"],"github_run":"6262","github_run_id":"31110291474","status":"ok"}
```

### Live bot full output

```text
14:20:45  INFO      Mode: exits
14:20:45  INFO        Daily log -> logs/daily/2026-08-06.md
14:20:45  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
14:20:45  INFO        place_all_stops: checking 2 positions...
14:20:45  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
14:20:45  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
14:20:45  INFO        [positions] 2/2 (2 valid)
14:20:45  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.04|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +1.4%  $+1.33                                            HOLD|
|  JBL  P&L +1.9%  $+1.82                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=154 paper_keys=yes dry_run=False
  alpaca positions=36
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T10:20:47.849022-04:00 ===

[Run context]
Paper auth OK — equity $145606.16, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 10:20:59,849 INFO   EXIT [b902|lab0902_s411_w3_1045_1120_r1|S411] stop_loss (-53.7%) SELL 1 TTD260807C00020500 @<= 0.28
2026-08-06 10:21:01,280 INFO   EXIT [b292|lab0292_s352_w3_1045_1120_r1|S352] take_profit (+61.3%) SELL 1 UBER260807C00070000 @<= 0.49
2026-08-06 10:21:04,593 INFO   EXIT [b352|lab0352_s360_w3_1045_1120_r1|S360] stop_loss (-64.5%) SELL 1 DKNG260807C00024500 @<= 0.15

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 884 signal(s); top: ['S165:AMD', 'S165:COIN', 'S165:CRWD', 'S165:SNOW', 'S165:MARA', 'S165:MSTR', 'S165:ARM', 'S165:PANW']
Paper lab: $145276 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 246 no tradeable call, 295 already attempted today, 124 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $145,606.16                             |
|  Signals this run              884                                     |
|  Orders submitted (session)    45                                      |
|  Orders filled today (ledger)  44                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             154                                     |
|  Broker option positions       35                                      |
|  Pending orders                7                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1123  buckets=256  win=43%                           |
|  Returns   avg=+25.3%  med=-18.4%  p10=-75.6%  p90=+138.5%             |
|  Realized  $+11,845.46                                                 |
|  Raw incl dropped  trades=1657  real=$+10,249.91                       |
|  Today     trades=29  avg=-34.0%  med=-82.2%  real=$-683.85            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  5  60% +695.8 +954.5 +1446.7 $   +621        |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  6 100% +295.8 +273.1 +815.4 $   +602         |
|  ... 248 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (7)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S355:MARA(2), S361:MARA(2), S210:CVNA(2)|
+------------------------------------------------------------------------+
|  b314 S355 MARA     limit=0.48                                         |
|  b315 S355 MARA     limit=0.48                                         |
|  b364 S361 MARA     limit=0.22                                         |
|  b365 S361 MARA     limit=0.22                                         |
|  b786 S398 CRWD     limit=0.42                                         |
|  ... 2 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (5)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b352 S360 DKNG260807C00024500 x1 stop_loss (-64.5%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (35)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34    -97.5%   $ -1,337.33               |
|  AMZN260807C00292500          16    -98.1%   $   -845.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260807C00042000           10    -20.4%   $   -131.00               |
|  NKE260828C00045000           12    -12.9%   $    -98.00               |
|  UBER260807C00070000           4    +73.7%   $    +95.08               |
|  COIN260807C00160000          10    +33.3%   $    +90.00               |
|  TTD260807C00020500            2    -52.2%   $    -70.00               |
|  ... 27 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=130.2s reconcile=0.13s cancel=0.03s manage=16.73s scan=57.62s entries=54.6s
STATUS: options_morning_bot run complete (PAPER) elapsed=130.2s. run=#6262 https://github.com/28twagg-ops/TradingBot/actions/runs/31110291474
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 22 buckets closed trades, $-683.85 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=95 drop=10
Orphan rate: 6.3% (104/1657)
# Options signal frequency

_Generated 2026-08-06T10:23:03.736662_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   441 | WARN | <<<
| Missing exit records (post) |   438 | WARN | <<<
| State/ledger mismatches     |    18 | WARN | <<<
| Total open lots             |   154 | INFO |
| Total closed lots           |  1086 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.04 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T142552Z

- UTC timestamp: `20260806T142552Z`
- GitHub run: [#6263](https://github.com/28twagg-ops/TradingBot/actions/runs/31110707743)
- Run id: `31110707743`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`134s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T10:25:56.794872-04:00","date":"2026-08-06","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":124.7,"phases_s":{"reconcile":0.26,"cancel":0.06,"manage":13.11,"scan":59.45,"entries":51.05,"reconcile2":0.26},"signals":865,"placed":0,"equity":144889.06,"open_positions":35,"pending_orders":7,"open_lots":153,"submitted_today":45,"filled_today":44,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:COIN","S165:CRWD","S165:SNOW","S165:MARA","S165:MSTR","S165:ARM","S165:PANW"],"github_run":"6263","github_run_id":"31110707743","status":"ok"}
```

### Live bot full output

```text
14:25:53  INFO      Mode: exits
14:25:54  INFO        Daily log -> logs/daily/2026-08-06.md
14:25:54  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
14:25:54  INFO        place_all_stops: checking 2 positions...
14:25:54  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
14:25:54  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
14:25:54  INFO        [positions] 2/2 (2 valid)
14:25:54  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.50|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +0.8%  $+0.74                                            HOLD|
|  JBL  P&L +2.0%  $+1.87                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=154 paper_keys=yes dry_run=False
  alpaca positions=37
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T10:25:56.794872-04:00 ===

[Run context]
Paper auth OK — equity $144889.06, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 10:26:09,699 INFO   EXIT [b901|lab0901_s411_w2_1005_1045_r2|S411] stop_loss (-58.2%) SELL 1 TTD260807C00020500 @<= 0.25

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 865 signal(s); top: ['S165:AMD', 'S165:COIN', 'S165:CRWD', 'S165:SNOW', 'S165:MARA', 'S165:MSTR', 'S165:ARM', 'S165:PANW']
Paper lab: $144386 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 240 no tradeable call, 286 already attempted today, 116 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $144,889.06                             |
|  Signals this run              865                                     |
|  Orders submitted (session)    45                                      |
|  Orders filled today (ledger)  44                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             153                                     |
|  Broker option positions       35                                      |
|  Pending orders                7                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1124  buckets=256  win=43%                           |
|  Returns   avg=+25.2%  med=-18.7%  p10=-75.5%  p90=+138.4%             |
|  Realized  $+11,806.46                                                 |
|  Raw incl dropped  trades=1658  real=$+10,210.91                       |
|  Today     trades=30  avg=-34.8%  med=-81.9%  real=$-722.85            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  5  60% +695.8 +954.5 +1446.7 $   +621        |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  6 100% +295.8 +273.1 +815.4 $   +602         |
|  ... 248 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (7)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S355:MARA(2), S361:MARA(2), S210:CVNA(2)|
+------------------------------------------------------------------------+
|  b314 S355 MARA     limit=0.48                                         |
|  b315 S355 MARA     limit=0.48                                         |
|  b364 S361 MARA     limit=0.22                                         |
|  b365 S361 MARA     limit=0.22                                         |
|  b786 S398 CRWD     limit=0.42                                         |
|  ... 2 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (5)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b352 S360 DKNG260807C00024500 x1 stop_loss (-64.5%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (35)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16    -98.1%   $   -845.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260807C00042000           10    -31.4%   $   -201.00               |
|  NKE260828C00045000           12    -16.1%   $   -122.00               |
|  NKE260821C00044000           12    -12.7%   $    -96.00               |
|  TTD260807P00017000            4    +32.7%   $    +72.00               |
|  UBER260807C00070000           4    +39.6%   $    +51.08               |
|  ... 27 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=124.7s reconcile=0.26s cancel=0.06s manage=13.11s scan=59.45s entries=51.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=124.7s. run=#6263 https://github.com/28twagg-ops/TradingBot/actions/runs/31110707743
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 23 buckets closed trades, $-722.85 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=95 drop=10
Orphan rate: 6.3% (104/1658)
# Options signal frequency

_Generated 2026-08-06T10:28:07.099018_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   441 | WARN | <<<
| Missing exit records (post) |   438 | WARN | <<<
| State/ledger mismatches     |    18 | WARN | <<<
| Total open lots             |   153 | INFO |
| Total closed lots           |  1087 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.5 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T143345Z

- UTC timestamp: `20260806T143345Z`
- GitHub run: [#6264](https://github.com/28twagg-ops/TradingBot/actions/runs/31111124053)
- Run id: `31111124053`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T10:25:56.794872-04:00","date":"2026-08-06","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":124.7,"phases_s":{"reconcile":0.26,"cancel":0.06,"manage":13.11,"scan":59.45,"entries":51.05,"reconcile2":0.26},"signals":865,"placed":0,"equity":144889.06,"open_positions":35,"pending_orders":7,"open_lots":153,"submitted_today":45,"filled_today":44,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:COIN","S165:CRWD","S165:SNOW","S165:MARA","S165:MSTR","S165:ARM","S165:PANW"],"github_run":"6263","github_run_id":"31110707743","status":"ok"}
```

### Live bot full output

```text
14:33:46  INFO      Mode: exits
14:33:47  INFO        Daily log -> logs/daily/2026-08-06.md
14:33:47  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
14:33:47  INFO        place_all_stops: checking 2 positions...
14:33:47  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
14:33:47  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
14:33:47  INFO        [positions] 2/2 (2 valid)
14:33:47  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:33 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.95|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +1.0%  $+0.96                                            HOLD|
|  JBL  P&L +2.2%  $+2.10                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=153 paper_keys=yes dry_run=False
  alpaca positions=37
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T10:33:49.585861-04:00 ===

[Run context]
Paper auth OK — equity $144369.04, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 10:33:55,103 INFO   EXIT [b900|lab0900_s411_w2_1005_1045_r1|S411] stop_loss (-56.7%) SELL 1 TTD260807C00020500 @<= 0.26
2026-08-06 10:33:56,647 INFO   EXIT [b847|lab0847_s407_w3_1045_1120_r2|S407] stop_loss (-57.4%) SELL 1 NKE260807C00043000 @<= 0.07

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 865 signal(s); top: ['S165:AMD', 'S165:COIN', 'S165:CRWD', 'S165:SNOW', 'S165:MARA', 'S165:MSTR', 'S165:ARM', 'S165:PANW']
Paper lab: $144444 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260806T143621Z

- UTC timestamp: `20260806T143621Z`
- GitHub run: [#6265](https://github.com/28twagg-ops/TradingBot/actions/runs/31111546847)
- Run id: `31111546847`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`137s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T10:36:25.712062-04:00","date":"2026-08-06","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":127.7,"phases_s":{"reconcile":0.46,"cancel":0.05,"manage":15.24,"scan":59.81,"entries":48.38,"reconcile2":3.25},"signals":882,"placed":1,"equity":144653.88,"open_positions":37,"pending_orders":6,"open_lots":155,"submitted_today":46,"filled_today":48,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:COIN","S165:CRWD","S165:SNOW","S165:MARA","S165:MSTR","S165:ARM","S165:PANW"],"github_run":"6265","github_run_id":"31111546847","status":"ok"}
```

### Live bot full output

```text
14:36:22  INFO      Mode: exits
14:36:23  INFO        Daily log -> logs/daily/2026-08-06.md
14:36:23  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
14:36:23  INFO        place_all_stops: checking 2 positions...
14:36:23  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
14:36:23  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
14:36:23  INFO        [positions] 2/2 (2 valid)
14:36:23  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.38|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +1.2%  $+1.11                                            HOLD|
|  JBL  P&L +2.5%  $+2.38                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=153 paper_keys=yes dry_run=False
  alpaca positions=38
  FLAG b900|S411|8d542670 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T10:36:25.712062-04:00 ===

[Run context]
Paper auth OK — equity $144653.88, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 10:36:30,263 INFO   EXIT [b846|lab0846_s407_w3_1045_1120_r1|S407] stop_loss (-57.4%) SELL 1 NKE260807C00043000 @<= 0.07

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 882 signal(s); top: ['S165:AMD', 'S165:COIN', 'S165:CRWD', 'S165:SNOW', 'S165:MARA', 'S165:MSTR', 'S165:ARM', 'S165:PANW']
Paper lab: $144181 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 234 no tradeable call, 298 already attempted today, 134 pending order
Placed 1 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $144,653.88                             |
|  Signals this run              882                                     |
|  Orders submitted (session)    46                                      |
|  Orders filled today (ledger)  48                                      |
|  Entries placed this run       1                                       |
|  Open virtual lots             155                                     |
|  Broker option positions       37                                      |
|  Pending orders                6                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1128  buckets=258  win=43%                           |
|  Returns   avg=+25.0%  med=-18.9%  p10=-75.2%  p90=+138.0%             |
|  Realized  $+11,737.46                                                 |
|  Raw incl dropped  trades=1662  real=$+10,141.91                       |
|  Today     trades=33  avg=-36.6%  med=-73.3%  real=$-779.85            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  5  60% +695.8 +954.5 +1446.7 $   +621        |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  6 100% +295.8 +273.1 +815.4 $   +602         |
|  ... 250 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (6)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S355:MARA(2), S361:MARA(2), S398:CRWD(1)|
+------------------------------------------------------------------------+
|  b314 S355 MARA     limit=0.48                                         |
|  b315 S355 MARA     limit=0.48                                         |
|  b364 S361 MARA     limit=0.22                                         |
|  b365 S361 MARA     limit=0.22                                         |
|  b786 S398 CRWD     limit=0.42                                         |
|  ... 1 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (5)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b352 S360 DKNG260807C00024500 x1 stop_loss (-64.5%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (37)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16    -98.1%   $   -845.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260807C00042000           10    -28.2%   $   -181.00               |
|  NKE260828C00045000           12    -19.3%   $   -146.00               |
|  NKE260821C00044000           12    -15.9%   $   -120.00               |
|  COIN260807C00160000          10    +33.3%   $    +90.00               |
|  GOOGL260810C00380000          2    -47.5%   $    -56.00               |
|  ... 29 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=127.7s reconcile=0.46s cancel=0.05s manage=15.24s scan=59.81s entries=48.38s
STATUS: options_morning_bot run complete (PAPER) elapsed=127.7s. run=#6265 https://github.com/28twagg-ops/TradingBot/actions/runs/31111546847
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 26 buckets closed trades, $-779.85 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=95 drop=10
Orphan rate: 6.3% (104/1662)
# Options signal frequency

_Generated 2026-08-06T10:38:38.937349_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   441 | WARN | <<<
| Missing exit records (post) |   438 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   155 | INFO |
| Total closed lots           |  1091 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.38 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T144051Z

- UTC timestamp: `20260806T144051Z`
- GitHub run: [#6266](https://github.com/28twagg-ops/TradingBot/actions/runs/31111963739)
- Run id: `31111963739`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`136s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T10:40:55.997436-04:00","date":"2026-08-06","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":126.2,"phases_s":{"reconcile":0.23,"cancel":0.05,"manage":18.62,"scan":73.67,"entries":29.86,"reconcile2":3.27},"signals":862,"placed":2,"equity":143945.83,"open_positions":36,"pending_orders":7,"open_lots":154,"submitted_today":48,"filled_today":49,"unattributed_contracts":0,"top_signals":["S165:AMD","S165:COIN","S165:CRWD","S165:SNOW","S165:MARA","S165:MSTR","S165:ARM","S165:PANW"],"github_run":"6266","github_run_id":"31111963739","status":"ok"}
```

### Live bot full output

```text
14:40:52  INFO      Mode: exits
14:40:52  INFO        Daily log -> logs/daily/2026-08-06.md
14:40:52  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
14:40:52  INFO        place_all_stops: checking 2 positions...
14:40:52  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
14:40:52  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
14:40:53  INFO        [positions] 2/2 (2 valid)
14:40:53  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.43|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +0.9%  $+0.86                                            HOLD|
|  JBL  P&L +1.8%  $+1.68                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=155 paper_keys=yes dry_run=False
  alpaca positions=39
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T10:40:55.997436-04:00 ===

[Run context]
Paper auth OK — equity $143945.83, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 10:40:57,746 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-57.1%) SELL 1 AMD260807C00550000 @<= 0.16

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 862 signal(s); top: ['S165:AMD', 'S165:COIN', 'S165:CRWD', 'S165:SNOW', 'S165:MARA', 'S165:MSTR', 'S165:ARM', 'S165:PANW']
Paper lab: $144151 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 192 no tradeable call, 284 already attempted today, 144 pending order
Placed 2 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $143,945.83                             |
|  Signals this run              862                                     |
|  Orders submitted (session)    48                                      |
|  Orders filled today (ledger)  49                                      |
|  Entries placed this run       2                                       |
|  Open virtual lots             154                                     |
|  Broker option positions       36                                      |
|  Pending orders                7                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1129  buckets=258  win=43%                           |
|  Returns   avg=+24.9%  med=-18.9%  p10=-75.2%  p90=+138.0%             |
|  Realized  $+11,718.46                                                 |
|  Raw incl dropped  trades=1663  real=$+10,122.91                       |
|  Today     trades=34  avg=-37.1%  med=-66.9%  real=$-798.85            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  5  60% +695.8 +954.5 +1446.7 $   +621        |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  6 100% +295.8 +273.1 +815.4 $   +602         |
|  ... 250 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  4   0% -82.2 -98.4 -98.6 $   -199       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (7)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S355:MARA(2), S361:MARA(2), S396:MARA(2)|
+------------------------------------------------------------------------+
|  b314 S355 MARA     limit=0.48                                         |
|  b315 S355 MARA     limit=0.48                                         |
|  b364 S361 MARA     limit=0.22                                         |
|  b365 S361 MARA     limit=0.22                                         |
|  b786 S398 CRWD     limit=0.42                                         |
|  ... 2 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (5)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b352 S360 DKNG260807C00024500 x1 stop_loss (-64.5%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (36)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16    -98.1%   $   -845.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260807C00042000           10    -25.1%   $   -161.00               |
|  COIN260807C00160000          10    +51.9%   $   +140.00               |
|  NKE260828C00045000           12    -16.1%   $   -122.00               |
|  NKE260821C00044000           12    -11.1%   $    -84.00               |
|  AMD260807C00537500            2    -47.8%   $    -64.00               |
|  ... 28 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=126.2s reconcile=0.23s cancel=0.05s manage=18.62s scan=73.67s entries=29.86s
STATUS: options_morning_bot run complete (PAPER) elapsed=126.2s. run=#6266 https://github.com/28twagg-ops/TradingBot/actions/runs/31111963739
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 26 buckets closed trades, $-798.85 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=95 drop=10
Orphan rate: 6.3% (105/1663)
# Options signal frequency

_Generated 2026-08-06T10:43:07.900383_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   441 | WARN | <<<
| Missing exit records (post) |   438 | WARN | <<<
| State/ledger mismatches     |    19 | WARN | <<<
| Total open lots             |   154 | INFO |
| Total closed lots           |  1091 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.43 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T144544Z

- UTC timestamp: `20260806T144544Z`
- GitHub run: [#6267](https://github.com/28twagg-ops/TradingBot/actions/runs/31112386054)
- Run id: `31112386054`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`256s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T10:45:48.485319-04:00","date":"2026-08-06","mode":"entry+manage","header":"entry+manage (37 new)","elapsed_s":247.4,"phases_s":{"reconcile":0.14,"cancel":0.03,"manage":16.26,"scan":62.67,"entries":161.97,"reconcile2":5.93},"signals":866,"placed":37,"equity":143819.79,"open_positions":39,"pending_orders":15,"open_lots":168,"submitted_today":85,"filled_today":78,"unattributed_contracts":4,"top_signals":["S165:AMD","S165:COIN","S165:CRWD","S165:SNOW","S165:MARA","S165:MSTR","S165:ARM","S165:PANW"],"github_run":"6267","github_run_id":"31112386054","status":"ok"}
```

### Live bot full output

```text
14:45:45  INFO      Mode: exits
14:45:46  INFO        Daily log -> logs/daily/2026-08-06.md
14:45:46  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
14:45:46  INFO        place_all_stops: checking 2 positions...
14:45:46  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
14:45:46  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
14:45:46  INFO        [positions] 2/2 (2 valid)
14:45:46  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.20|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +0.2%  $+0.16                                            HOLD|
|  JBL  P&L +1.2%  $+1.14                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=154 paper_keys=yes dry_run=False
  alpaca positions=37
  FLAG b352|S360|fc037c9c missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T10:45:48.485319-04:00 ===

[Run context]
Paper auth OK — equity $143819.79, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 10:45:52,150 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-56.1%) SELL 2 AMD260807C00545000 @<= 0.19
2026-08-06 10:45:53,415 INFO   EXIT [b108|lab0108_s212_w1_0928_1005_r1|S212] stop_loss (-54.2%) SELL 1 GOOGL260810C00380000 @<= 0.24
2026-08-06 10:45:55,624 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-53.4%) SELL 2 GOOGL260807C00372500 @<= 0.24
2026-08-06 10:45:59,941 INFO   EXIT [b859|lab0859_s408_w2_1005_1045_r2|S408] stop_loss (-59.3%) SELL 1 AMD260807C00552500 @<= 0.08
2026-08-06 10:46:02,073 INFO   EXIT [b75|lab0075_s209_w2_1005_1045_r2|S209] stop_loss (-50.7%) SELL 1 AMD260807C00537500 @<= 0.30

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 866 signal(s); top: ['S165:AMD', 'S165:COIN', 'S165:CRWD', 'S165:SNOW', 'S165:MARA', 'S165:MSTR', 'S165:ARM', 'S165:PANW']
Paper lab: $143663 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 475 no tradeable call, 289 already attempted today, 748 pending order
Placed 37 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $143,819.79                             |
|  Signals this run              866                                     |
|  Orders submitted (session)    85                                      |
|  Orders filled today (ledger)  78                                      |
|  Entries placed this run       37                                      |
|  Open virtual lots             168                                     |
|  Broker option positions       39                                      |
|  Unattributed contracts        4 (orphan reconcile)                    |
|  Pending orders                15                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1168  buckets=259  win=43%                           |
|  Returns   avg=+23.3%  med=-21.1%  p10=-76.1%  p90=+137.2%             |
|  Realized  $+11,070.70                                                 |
|  Raw incl dropped  trades=1702  real=$+9,475.15                        |
|  Today     trades=39  avg=-39.3%  med=-58.2%  real=$-986.85            |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  6  67% +585.4 +493.9 +1446.7 $   +623        |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  7 100% +270.8 +273.1 +815.4 $   +654         |
|  ... 251 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  5   0% -76.6 -98.2 -98.6 $   -231       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (15)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S361:MARA(2), S212:CVNA(2), S360:AMD(2) |
+------------------------------------------------------------------------+
|  b364 S361 MARA     limit=0.22                                         |
|  b365 S361 MARA     limit=0.22                                         |
|  b786 S398 CRWD     limit=0.42                                         |
|  b84  S210 CVNA     limit=0.33                                         |
|  b112 S212 CVNA     limit=0.33                                         |
|  ... 10 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (4)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (39)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16    -98.1%   $   -845.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260807C00042000           10    -29.8%   $   -191.00               |
|  NKE260828C00045000           12    -17.7%   $   -134.00               |
|  NKE260821C00044000           12    -12.7%   $    -96.00               |
|  MARA260814C00011500          15     -7.6%   $    -57.00               |
|  UBER260807C00078000           1    -98.0%   $    -49.53               |
|  ... 31 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=247.4s reconcile=0.14s cancel=0.03s manage=16.26s scan=62.67s entries=161.97s
STATUS: options_morning_bot run complete (PAPER) elapsed=247.4s. run=#6267 https://github.com/28twagg-ops/TradingBot/actions/runs/31112386054
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 29 buckets closed trades, $-986.85 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=95 drop=10
Orphan rate: 6.6% (112/1702)
# Options signal frequency

_Generated 2026-08-06T10:50:01.647345_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   440 | WARN | <<<
| Missing exit records (post) |   437 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   168 | INFO |
| Total closed lots           |  1123 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=472.23 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T145637Z

- UTC timestamp: `20260806T145637Z`
- GitHub run: [#6269](https://github.com/28twagg-ops/TradingBot/actions/runs/31113246842)
- Run id: `31113246842`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`133s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T10:56:40.501150-04:00","date":"2026-08-06","mode":"entry+manage","header":"entry+manage (9 new)","elapsed_s":126.0,"phases_s":{"reconcile":2.0,"cancel":0.05,"manage":11.46,"scan":49.24,"entries":62.5,"reconcile2":0.36},"signals":863,"placed":9,"equity":144051.76,"open_positions":39,"pending_orders":23,"open_lots":156,"submitted_today":94,"filled_today":79,"unattributed_contracts":4,"top_signals":["S165:AMD","S165:COIN","S165:CRWD","S165:SNOW","S165:MARA","S165:MSTR","S165:ARM","S165:PANW"],"github_run":"6269","github_run_id":"31113246842","status":"ok"}
```

### Live bot full output

```text
14:56:38  INFO      Mode: exits
14:56:38  INFO        Daily log -> logs/daily/2026-08-06.md
14:56:38  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
14:56:38  INFO        place_all_stops: checking 2 positions...
14:56:38  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
14:56:38  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
14:56:38  INFO        [positions] 2/2 (2 valid)
14:56:38  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.84|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +0.7%  $+0.70                                            HOLD|
|  JBL  P&L +1.3%  $+1.25                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=168 paper_keys=yes dry_run=False
  alpaca positions=41
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T10:56:40.501150-04:00 ===

[Run context]
Paper auth OK — equity $144051.76, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 10:56:44,583 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-59.3%) SELL 1 AMD260807C00552500 @<= 0.08
2026-08-06 10:56:45,968 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-52.5%) SELL 1 GOOGL260810C00380000 @<= 0.29

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 863 signal(s); top: ['S165:AMD', 'S165:COIN', 'S165:CRWD', 'S165:SNOW', 'S165:MARA', 'S165:MSTR', 'S165:ARM', 'S165:PANW']
Paper lab: $144448 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 278 no tradeable call, 187 already attempted today, 261 pending order
Placed 9 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $144,051.76                             |
|  Signals this run              863                                     |
|  Orders submitted (session)    94                                      |
|  Orders filled today (ledger)  79                                      |
|  Entries placed this run       9                                       |
|  Open virtual lots             156                                     |
|  Broker option positions       39                                      |
|  Unattributed contracts        4 (orphan reconcile)                    |
|  Pending orders                23                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1203  buckets=259  win=42%                           |
|  Returns   avg=+21.8%  med=-27.0%  p10=-77.4%  p90=+135.0%             |
|  Realized  $+10,286.93                                                 |
|  Raw incl dropped  trades=1737  real=$+8,691.38                        |
|  Today     trades=44  avg=-45.0%  med=-59.9%  real=$-1,185.85          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  6  67% +585.4 +493.9 +1446.7 $   +623        |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  7 100% +270.8 +273.1 +815.4 $   +654         |
|  ... 251 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (23)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S361:MARA(2), S212:CVNA(2), S360:AMD(2) |
+------------------------------------------------------------------------+
|  b364 S361 MARA     limit=0.22                                         |
|  b365 S361 MARA     limit=0.22                                         |
|  b786 S398 CRWD     limit=0.42                                         |
|  b84  S210 CVNA     limit=0.33                                         |
|  b112 S212 CVNA     limit=0.33                                         |
|  ... 18 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (5)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b0   ORPHAN GOOGL260810C00380000 x1 stop_loss (-52.5%)                |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (39)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16    -98.1%   $   -845.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260807C00042000           10    -28.2%   $   -181.00               |
|  NKE260828C00045000           12    -16.1%   $   -122.00               |
|  NKE260821C00044000           12    -11.1%   $    -84.00               |
|  UBER260807C00078000           1    -98.0%   $    -49.53               |
|  AAPL260814C00330000           5    +15.5%   $    +46.25               |
|  ... 31 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=126.0s reconcile=2.0s cancel=0.05s manage=11.46s scan=49.24s entries=62.5s
STATUS: options_morning_bot run complete (PAPER) elapsed=126.0s. run=#6269 https://github.com/28twagg-ops/TradingBot/actions/runs/31113246842
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 29 buckets closed trades, $-1,185.85 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=93 drop=12
Orphan rate: 7.1% (124/1737)
# Options signal frequency

_Generated 2026-08-06T10:58:50.814102_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   440 | WARN | <<<
| Missing exit records (post) |   437 | WARN | <<<
| State/ledger mismatches     |    24 | WARN | <<<
| Total open lots             |   156 | INFO |
| Total closed lots           |  1146 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=472.84 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T150630Z

- UTC timestamp: `20260806T150630Z`
- GitHub run: [#6271](https://github.com/28twagg-ops/TradingBot/actions/runs/31114116760)
- Run id: `31114116760`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`145s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T11:06:34.504268-04:00","date":"2026-08-06","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":136.0,"phases_s":{"reconcile":0.57,"cancel":0.03,"manage":11.78,"scan":59.99,"entries":62.77,"reconcile2":0.13},"signals":894,"placed":0,"equity":144497.57,"open_positions":39,"pending_orders":19,"open_lots":157,"submitted_today":94,"filled_today":83,"unattributed_contracts":3,"top_signals":["S165:AMD","S165:COIN","S165:CRWD","S165:SNOW","S165:MARA","S165:MSTR","S165:ARM","S165:PANW"],"github_run":"6271","github_run_id":"31114116760","status":"ok"}
```

### Live bot full output

```text
15:06:31  INFO      Mode: exits
15:06:32  INFO        Daily log -> logs/daily/2026-08-06.md
15:06:32  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
15:06:32  INFO        place_all_stops: checking 2 positions...
15:06:32  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
15:06:32  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
15:06:32  INFO        [positions] 2/2 (2 valid)
15:06:32  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.91|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +0.7%  $+0.64                                            HOLD|
|  JBL  P&L +1.5%  $+1.38                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=156 paper_keys=yes dry_run=False
  alpaca positions=41
  FLAG b0|ORPHAN|0d4a66ab missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T11:06:34.504268-04:00 ===

[Run context]
Paper auth OK — equity $144497.57, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 894 signal(s); top: ['S165:AMD', 'S165:COIN', 'S165:CRWD', 'S165:SNOW', 'S165:MARA', 'S165:MSTR', 'S165:ARM', 'S165:PANW']
Paper lab: $144848 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 298 no tradeable call, 241 already attempted today, 236 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $144,497.57                             |
|  Signals this run              894                                     |
|  Orders submitted (session)    94                                      |
|  Orders filled today (ledger)  83                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             157                                     |
|  Broker option positions       39                                      |
|  Unattributed contracts        3 (orphan reconcile)                    |
|  Pending orders                19                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1207  buckets=259  win=42%                           |
|  Returns   avg=+21.6%  med=-27.0%  p10=-77.6%  p90=+134.5%             |
|  Realized  $+10,216.43                                                 |
|  Raw incl dropped  trades=1741  real=$+8,620.88                        |
|  Today     trades=46  avg=-46.0%  med=-59.9%  real=$-1,254.35          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  6  67% +585.4 +493.9 +1446.7 $   +623        |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  7 100% +270.8 +273.1 +815.4 $   +654         |
|  ... 251 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (19)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S361:MARA(2), S212:CVNA(2), S360:AMD(2) |
+------------------------------------------------------------------------+
|  b364 S361 MARA     limit=0.22                                         |
|  b365 S361 MARA     limit=0.22                                         |
|  b786 S398 CRWD     limit=0.42                                         |
|  b84  S210 CVNA     limit=0.33                                         |
|  b112 S212 CVNA     limit=0.33                                         |
|  ... 14 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (4)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (39)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34    -97.5%   $ -1,337.33               |
|  AMZN260807C00292500          16    -98.1%   $   -845.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  COIN260807C00160000          13    +35.2%   $   +132.00               |
|  NKE260828C00045000           12    -12.9%   $    -98.00               |
|  NKE260807C00042000           10     -9.5%   $    -61.00               |
|  TSLA260810C00342500           4    +31.2%   $    +60.00               |
|  CRWD260807C00217500           4    -28.3%   $    -52.00               |
|  ... 31 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=136.0s reconcile=0.57s cancel=0.03s manage=11.78s scan=59.99s entries=62.77s
STATUS: options_morning_bot run complete (PAPER) elapsed=136.0s. run=#6271 https://github.com/28twagg-ops/TradingBot/actions/runs/31114116760
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 29 buckets closed trades, $-1,254.35 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=93 drop=12
Orphan rate: 7.2% (125/1741)
# Options signal frequency

_Generated 2026-08-06T11:08:56.189880_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   440 | WARN | <<<
| Missing exit records (post) |   437 | WARN | <<<
| State/ledger mismatches     |    24 | WARN | <<<
| Total open lots             |   157 | INFO |
| Total closed lots           |  1149 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=472.91 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T151045Z

- UTC timestamp: `20260806T151045Z`
- GitHub run: [#6272](https://github.com/28twagg-ops/TradingBot/actions/runs/31114535204)
- Run id: `31114535204`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`148s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T11:10:50.642784-04:00","date":"2026-08-06","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":139.3,"phases_s":{"reconcile":0.35,"cancel":0.05,"manage":13.39,"scan":61.71,"entries":63.13,"reconcile2":0.19},"signals":896,"placed":0,"equity":145003.48,"open_positions":39,"pending_orders":16,"open_lots":160,"submitted_today":94,"filled_today":86,"unattributed_contracts":3,"top_signals":["S165:AMD","S165:COIN","S165:CRWD","S165:SNOW","S165:MARA","S165:MSTR","S165:ARM","S165:PANW"],"github_run":"6272","github_run_id":"31114535204","status":"ok"}
```

### Live bot full output

```text
15:10:47  INFO      Mode: exits
15:10:48  INFO        Daily log -> logs/daily/2026-08-06.md
15:10:48  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
15:10:48  INFO        place_all_stops: checking 2 positions...
15:10:48  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
15:10:48  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
15:10:48  INFO        [positions] 2/2 (2 valid)
15:10:48  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.25|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +0.8%  $+0.77                                            HOLD|
|  JBL  P&L +1.7%  $+1.58                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=157 paper_keys=yes dry_run=False
  alpaca positions=41
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T11:10:50.642784-04:00 ===

[Run context]
Paper auth OK — equity $145003.48, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 896 signal(s); top: ['S165:AMD', 'S165:COIN', 'S165:CRWD', 'S165:SNOW', 'S165:MARA', 'S165:MSTR', 'S165:ARM', 'S165:PANW']
Paper lab: $144884 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 298 no tradeable call, 241 already attempted today, 226 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $145,003.48                             |
|  Signals this run              896                                     |
|  Orders submitted (session)    94                                      |
|  Orders filled today (ledger)  86                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             160                                     |
|  Broker option positions       39                                      |
|  Unattributed contracts        3 (orphan reconcile)                    |
|  Pending orders                16                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1207  buckets=259  win=42%                           |
|  Returns   avg=+21.6%  med=-27.0%  p10=-77.6%  p90=+134.5%             |
|  Realized  $+10,216.43                                                 |
|  Raw incl dropped  trades=1741  real=$+8,620.88                        |
|  Today     trades=46  avg=-46.0%  med=-59.9%  real=$-1,254.35          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  6  67% +585.4 +493.9 +1446.7 $   +623        |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  7 100% +270.8 +273.1 +815.4 $   +654         |
|  ... 251 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (16)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S361:MARA(2), S360:AMD(2), S361:AMD(2)  |
+------------------------------------------------------------------------+
|  b364 S361 MARA     limit=0.22                                         |
|  b365 S361 MARA     limit=0.22                                         |
|  b786 S398 CRWD     limit=0.42                                         |
|  b352 S360 AMD      limit=0.57                                         |
|  b353 S360 AMD      limit=0.57                                         |
|  ... 11 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (4)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (39)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34    -97.5%   $ -1,337.33               |
|  AMZN260807C00292500          16    -98.1%   $   -845.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260828C00045000           12    -11.3%   $    -86.00               |
|  META260807C00622500           4    -38.3%   $    -82.00               |
|  NKE260807C00042000           10    -12.6%   $    -81.00               |
|  COIN260807C00160000          13    +21.3%   $    +80.00               |
|  MARA260814C00011500          15     +8.4%   $    +63.00               |
|  ... 31 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=139.3s reconcile=0.35s cancel=0.05s manage=13.39s scan=61.71s entries=63.13s
STATUS: options_morning_bot run complete (PAPER) elapsed=139.3s. run=#6272 https://github.com/28twagg-ops/TradingBot/actions/runs/31114535204
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 29 buckets closed trades, $-1,254.35 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=93 drop=12
Orphan rate: 7.2% (125/1741)
# Options signal frequency

_Generated 2026-08-06T11:13:15.545484_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   440 | WARN | <<<
| Missing exit records (post) |   437 | WARN | <<<
| State/ledger mismatches     |    24 | WARN | <<<
| Total open lots             |   160 | INFO |
| Total closed lots           |  1149 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.25 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T152052Z

- UTC timestamp: `20260806T152052Z`
- GitHub run: [#6273](https://github.com/28twagg-ops/TradingBot/actions/runs/31115321203)
- Run id: `31115321203`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T11:10:50.642784-04:00","date":"2026-08-06","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":139.3,"phases_s":{"reconcile":0.35,"cancel":0.05,"manage":13.39,"scan":61.71,"entries":63.13,"reconcile2":0.19},"signals":896,"placed":0,"equity":145003.48,"open_positions":39,"pending_orders":16,"open_lots":160,"submitted_today":94,"filled_today":86,"unattributed_contracts":3,"top_signals":["S165:AMD","S165:COIN","S165:CRWD","S165:SNOW","S165:MARA","S165:MSTR","S165:ARM","S165:PANW"],"github_run":"6272","github_run_id":"31114535204","status":"ok"}
```

### Live bot full output

```text
15:20:53  INFO      Mode: exits
15:20:53  INFO        Daily log -> logs/daily/2026-08-06.md
15:20:53  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
15:20:53  INFO        place_all_stops: checking 2 positions...
15:20:53  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
15:20:53  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
15:20:54  INFO        [positions] 2/2 (2 valid)
15:20:54  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.84|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +0.7%  $+0.64                                            HOLD|
|  JBL  P&L +1.4%  $+1.31                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=160 paper_keys=yes dry_run=False
  alpaca positions=41
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T11:20:56.351649-04:00 ===

[Run context]
Paper auth OK — equity $143780.45, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 876 signal(s); top: ['S165:AMD', 'S165:COIN', 'S165:CRWD', 'S165:SNOW', 'S165:MARA', 'S165:MSTR', 'S165:ARM', 'S165:PANW']
Paper lab: $143790 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260806T153320Z

- UTC timestamp: `20260806T153320Z`
- GitHub run: [#6275](https://github.com/28twagg-ops/TradingBot/actions/runs/31116126039)
- Run id: `31116126039`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`205s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T11:33:25.940011-04:00","date":"2026-08-06","mode":"entry+manage","header":"entry+manage (9 new)","elapsed_s":195.8,"phases_s":{"reconcile":5.02,"cancel":0.15,"manage":24.29,"scan":64.06,"entries":100.11,"reconcile2":1.49},"signals":863,"placed":9,"equity":143240.64,"open_positions":46,"pending_orders":17,"open_lots":194,"submitted_today":138,"filled_today":156,"unattributed_contracts":5,"top_signals":["S165:AMD","S165:COIN","S165:CRWD","S165:SNOW","S165:MARA","S165:MSTR","S165:ARM","S165:PANW"],"github_run":"6275","github_run_id":"31116126039","status":"ok"}
```

### Live bot full output

```text
15:33:21  INFO      Mode: exits
15:33:22  INFO        Daily log -> logs/daily/2026-08-06.md
15:33:22  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
15:33:22  INFO        place_all_stops: checking 2 positions...
15:33:22  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
15:33:22  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
15:33:23  INFO        [positions] 2/2 (2 valid)
15:33:23  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:33 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.25|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +0.3%  $+0.25                                            HOLD|
|  JBL  P&L +1.2%  $+1.11                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=161 paper_keys=yes dry_run=False
  alpaca positions=45
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T11:33:25.940011-04:00 ===

[Run context]
Paper auth OK — equity $143240.64, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 11:33:34,250 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-50.0%) SELL 2 META260807C00625000 @<= 0.24
2026-08-06 11:33:35,025 INFO   EXIT [b848|lab0848_s407_w4_1120_1135_r1|S407] stop_loss (-53.2%) SELL 1 NKE260807C00043000 @<= 0.12

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 863 signal(s); top: ['S165:AMD', 'S165:COIN', 'S165:CRWD', 'S165:SNOW', 'S165:MARA', 'S165:MSTR', 'S165:ARM', 'S165:PANW']
Paper lab: $143071 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 372 no tradeable call, 136 already attempted today, 343 pending order
Placed 9 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $143,240.64                             |
|  Signals this run              863                                     |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  156                                     |
|  Entries placed this run       9                                       |
|  Open virtual lots             194                                     |
|  Broker option positions       46                                      |
|  Unattributed contracts        5 (orphan reconcile)                    |
|  Pending orders                17                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1253  buckets=260  win=42%                           |
|  Returns   avg=+23.7%  med=-24.4%  p10=-77.9%  p90=+137.4%             |
|  Realized  $+10,532.89                                                 |
|  Raw incl dropped  trades=1787  real=$+8,937.34                        |
|  Today     trades=58  avg=-43.1%  med=-70.0%  real=$-1,463.20          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  6  67% +585.4 +493.9 +1446.7 $   +623        |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  ... 252 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (17)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S361:MARA(2), S360:AMD(2), S407:AMD(2)  |
+------------------------------------------------------------------------+
|  b364 S361 MARA     limit=0.22                                         |
|  b365 S361 MARA     limit=0.22                                         |
|  b786 S398 CRWD     limit=0.42                                         |
|  b352 S360 AMD      limit=0.57                                         |
|  b353 S360 AMD      limit=0.57                                         |
|  ... 12 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (6)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b0   ORPHAN META260807C00625000 x2 stop_loss (-50.0%)                 |
|  ... 1 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (46)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260807C00042000           10    -34.5%   $   -221.00               |
|  AMD260807C00537500           10    -37.8%   $   -213.00               |
|  NKE260828C00045000           12    -19.3%   $   -146.00               |
|  NKE260821C00044000           12    -14.3%   $   -108.00               |
|  META260807C00622500           4    -45.8%   $    -98.00               |
|  ... 38 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=195.8s reconcile=5.02s cancel=0.15s manage=24.29s scan=64.06s entries=100.11s
STATUS: options_morning_bot run complete (PAPER) elapsed=195.8s. run=#6275 https://github.com/28twagg-ops/TradingBot/actions/runs/31116126039
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 32 buckets closed trades, $-1,463.20 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 7.5% (135/1787)
# Options signal frequency

_Generated 2026-08-06T11:36:47.429043_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    28 | WARN | <<<
| Total open lots             |   194 | INFO |
| Total closed lots           |  1185 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=472.25 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T154145Z

- UTC timestamp: `20260806T154145Z`
- GitHub run: [#6276](https://github.com/28twagg-ops/TradingBot/actions/runs/31116886852)
- Run id: `31116886852`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`22s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T11:41:49.040033-04:00","date":"2026-08-06","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":14.2,"phases_s":{"reconcile":2.13,"cancel":0.15,"manage":11.5},"signals":0,"placed":0,"equity":143281.1,"open_positions":44,"pending_orders":17,"open_lots":189,"submitted_today":138,"filled_today":167,"unattributed_contracts":8,"top_signals":[],"github_run":"6276","github_run_id":"31116886852","status":"ok"}
```

### Live bot full output

```text
15:41:46  INFO      Mode: exits
15:41:46  INFO        Daily log -> logs/daily/2026-08-06.md
15:41:46  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
15:41:46  INFO        place_all_stops: checking 2 positions...
15:41:46  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
15:41:46  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
15:41:47  INFO        [positions] 2/2 (2 valid)
15:41:47  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.44|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L +0.2%  $+0.21                                            HOLD|
|  JBL  P&L +1.4%  $+1.35                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=194 paper_keys=yes dry_run=False
  alpaca positions=47
  FLAG b0|ORPHAN|ef6da0ed missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T11:41:49.040033-04:00 ===

[Run context]
Paper auth OK — equity $143281.10, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
Cancelled 17 unfilled LAB entry order(s).
2026-08-06 11:41:59,284 INFO   EXIT [b849|lab0849_s407_w4_1120_1135_r2|S407] stop_loss (-53.2%) SELL 1 NKE260807C00043000 @<= 0.08

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $143,281.10                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             189                                     |
|  Broker option positions       44                                      |
|  Unattributed contracts        8 (orphan reconcile)                    |
|  Pending orders                17                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1277  buckets=260  win=42%                           |
|  Returns   avg=+25.8%  med=-28.3%  p10=-77.8%  p90=+139.2%             |
|  Realized  $+11,338.69                                                 |
|  Raw incl dropped  trades=1811  real=$+9,743.14                        |
|  Today     trades=61  avg=-41.2%  med=-60.5%  real=$-1,472.20          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  ... 252 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (17)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S361:MARA(2), S360:AMD(2), S407:AMD(2)  |
+------------------------------------------------------------------------+
|  b364 S361 MARA     limit=0.22                                         |
|  b365 S361 MARA     limit=0.22                                         |
|  b786 S398 CRWD     limit=0.42                                         |
|  b352 S360 AMD      limit=0.57                                         |
|  b353 S360 AMD      limit=0.57                                         |
|  ... 12 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (5)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b849 S407 NKE260807C00043000 x1 stop_loss (-53.2%)                    |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (44)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260807C00042000           10    -32.9%   $   -211.00               |
|  AMD260807C00537500           10    -36.1%   $   -203.00               |
|  NKE260828C00045000           12    -17.7%   $   -134.00               |
|  NKE260821C00044000           12    -15.9%   $   -120.00               |
|  COIN260807C00160000          22    -16.6%   $   -105.00               |
|  ... 36 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=14.2s reconcile=2.13s cancel=0.15s manage=11.5s
STATUS: options_morning_bot run complete (PAPER) elapsed=14.2s. run=#6276 https://github.com/28twagg-ops/TradingBot/actions/runs/31116886852
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 33 buckets closed trades, $-1,472.20 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 7.6% (138/1811)
# Options signal frequency

_Generated 2026-08-06T11:42:08.841468_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    28 | WARN | <<<
| Total open lots             |   189 | INFO |
| Total closed lots           |  1206 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=472.44 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T161349Z

- UTC timestamp: `20260806T161349Z`
- GitHub run: [#6281](https://github.com/28twagg-ops/TradingBot/actions/runs/31118842093)
- Run id: `31118842093`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`28s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T12:13:53.209048-04:00","date":"2026-08-06","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":21.5,"phases_s":{"reconcile":0.38,"cancel":0.18,"manage":20.38},"signals":0,"placed":0,"equity":142764.04,"open_positions":44,"pending_orders":0,"open_lots":188,"submitted_today":138,"filled_today":167,"unattributed_contracts":7,"top_signals":[],"github_run":"6281","github_run_id":"31118842093","status":"ok"}
```

### Live bot full output

```text
16:13:50  INFO      Mode: exits
16:13:50  INFO        Daily log -> logs/daily/2026-08-06.md
16:13:50  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
16:13:50  INFO        place_all_stops: checking 2 positions...
16:13:50  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
16:13:50  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
16:13:51  INFO        [positions] 2/2 (2 valid)
16:13:51  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:13 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.82|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L -0.1%  $-0.13                                            HOLD|
|  JBL  P&L +1.1%  $+1.07                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                2|
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
  open_lots=189 paper_keys=yes dry_run=False
  alpaca positions=46
  FLAG b849|S407|6ea5818a missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T12:13:53.209048-04:00 ===

[Run context]
Paper auth OK — equity $142764.04, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 12:13:56,130 INFO   EXIT [b319|lab0319_s355_w4_1120_1135_r2|S355] take_profit (+78.8%) SELL 1 UBER260814C00072000 @<= 0.76
2026-08-06 12:14:03,416 INFO   EXIT [b83|lab0083_s210_w2_1005_1045_r2|S210] stop_loss (-56.5%) SELL 1 CVNA260807C00073000 @<= 0.11
2026-08-06 12:14:05,975 INFO   EXIT [b167|lab0167_s216_w2_1005_1045_r2|S216] stop_loss (-60.7%) SELL 1 META260807C00622500 @<= 0.18
2026-08-06 12:14:08,834 INFO   EXIT [b818|lab0818_s405_w3_1045_1120_r1|S405] take_profit (+129.6%) SELL 1 UBER260807C00070000 @<= 0.74
2026-08-06 12:14:11,562 INFO   EXIT [b335|lab0335_s357_w4_1120_1135_r2|S357] take_profit (+52.4%) SELL 1 UBER260828C00075000 @<= 0.70

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $142,764.04                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             188                                     |
|  Broker option positions       44                                      |
|  Unattributed contracts        7 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1277  buckets=260  win=42%                           |
|  Returns   avg=+25.8%  med=-28.3%  p10=-77.8%  p90=+139.2%             |
|  Realized  $+11,338.69                                                 |
|  Raw incl dropped  trades=1811  real=$+9,743.14                        |
|  Today     trades=61  avg=-41.2%  med=-60.5%  real=$-1,472.20          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b319 lab0319_s355_w4_11  1 100% +328.6 +328.6 +328.6 $   +138         |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  ... 252 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (9)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b319 S355 UBER260814C00072000 x1 take_profit (+78.8%)                 |
|  ... 4 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (44)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500           10    -41.4%   $   -233.00               |
|  NKE260807C00042000           10    -34.5%   $   -221.00               |
|  COIN260807C00160000          22    -30.5%   $   -193.00               |
|  UBER260807C00070000           4   +126.5%   $   +163.08               |
|  NKE260828C00045000           12    -19.3%   $   -146.00               |
|  ... 36 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=21.5s reconcile=0.38s cancel=0.18s manage=20.38s
STATUS: options_morning_bot run complete (PAPER) elapsed=21.5s. run=#6281 https://github.com/28twagg-ops/TradingBot/actions/runs/31118842093
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 33 buckets closed trades, $-1,472.20 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 7.6% (138/1811)
# Options signal frequency

_Generated 2026-08-06T12:14:19.030635_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    28 | WARN | <<<
| Total open lots             |   188 | INFO |
| Total closed lots           |  1206 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.82 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T173551Z

- UTC timestamp: `20260806T173551Z`
- GitHub run: [#6296](https://github.com/28twagg-ops/TradingBot/actions/runs/31123548118)
- Run id: `31123548118`
- Live bot: exit=`0`, duration=`6s`
- Options bot: exit=`0`, duration=`39s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T13:35:59.097628-04:00","date":"2026-08-06","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":30.7,"phases_s":{"reconcile":0.64,"cancel":0.21,"manage":29.19},"signals":0,"placed":0,"equity":142843.92,"open_positions":44,"pending_orders":0,"open_lots":184,"submitted_today":138,"filled_today":167,"unattributed_contracts":2,"top_signals":[],"github_run":"6296","github_run_id":"31123548118","status":"ok"}
```

### Live bot full output

```text
17:35:52  INFO      Mode: exits
17:35:53  INFO        Daily log -> logs/daily/2026-08-06.md
17:35:53  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (4 ledger rows)
17:35:53  INFO        place_all_stops: checking 2 positions...
17:35:53  INFO        STOP skipped GEV: fractional (0.0924 shares) — software exit will handle it
17:35:53  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
17:35:54  INFO        [positions] 2/2 (2 valid)
17:35:54  INFO        SELL MARKET [urgent] GEV closed
17:35:56  INFO        TX logged: SELL GEV  P&L -0.71%
17:35:57  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.90|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GEV  P&L -0.7%  $-0.67                         EXIT: stop_loss (-0.7%)|
|  JBL  P&L +1.8%  $+1.68                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           2|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
|  Logged exits                                                         1|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  GEV                                         -0.71%  (threshold -0.50%)|
|  Count                                                                1|
+========================================================================+
|  Stop-loss look file                  logs/stop_losses_to_look_into.txt|
|  New investigations added                                             0|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=188 paper_keys=yes dry_run=False
  alpaca positions=46
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T13:35:59.097628-04:00 ===

[Run context]
Paper auth OK — equity $142843.92, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 13:36:03,109 INFO   EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] stop_loss (-64.4%) SELL 1 CVNA260807C00072000 @<= 0.13
2026-08-06 13:36:04,017 INFO   EXIT [b318|lab0318_s355_w4_1120_1135_r1|S355] take_profit (+60.0%) SELL 1 UBER260814C00072000 @<= 0.72
2026-08-06 13:36:09,446 INFO   EXIT [b845|lab0845_s407_w2_1005_1045_r2|S407] stop_loss (-54.5%) SELL 1 PLTR260807C00170000 @<= 0.06
2026-08-06 13:36:14,428 INFO   EXIT [b293|lab0293_s352_w3_1045_1120_r2|S352] stop_loss (-63.0%) SELL 1 CRWD260807C00217500 @<= 0.17
2026-08-06 13:36:16,633 INFO   EXIT [b780|lab0780_s397_w3_1045_1120_r1|S397] stop_loss (-56.7%) SELL 1 COIN260807C00157500 @<= 0.27
2026-08-06 13:36:21,588 INFO   EXIT [b29|lab0029_s203_w3_1045_1120_r2|S203] take_profit (+58.2%) SELL 1 TTD260807P00017000 @<= 0.84
2026-08-06 13:36:21,913 INFO   EXIT [b913|lab0913_s412_w1_0928_1005_r2|S412] stop_loss (-50.1%) SELL 1 NKE260807C00042000 @<= 0.30
2026-08-06 13:36:22,320 INFO   EXIT [b789|lab0789_s398_w3_1045_1120_r2|S398] take_profit (+107.9%) SELL 1 UBER260807C00070000 @<= 0.68
2026-08-06 13:36:22,854 INFO   EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] stop_loss (-52.9%) SELL 1 CVNA260807C00071000 @<= 0.25
2026-08-06 13:36:24,048 INFO   EXIT [b797|lab0797_s399_w3_1045_1120_r2|S399] stop_loss (-53.8%) SELL 1 AMD260807C00570000 @<= 0.01
2026-08-06 13:36:25,923 INFO   EXIT [b73|lab0073_s209_w1_0928_1005_r2|S209] stop_loss (-64.7%) SELL 1 UPST260807C00032000 @<= 0.03
2026-08-06 13:36:27,780 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-64.5%) SELL 1 META260807C00622500 @<= 0.16

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $142,843.92                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             184                                     |
|  Broker option positions       44                                      |
|  Unattributed contracts        2 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1281  buckets=261  win=42%                           |
|  Returns   avg=+25.9%  med=-27.0%  p10=-77.8%  p90=+138.6%             |
|  Realized  $+11,401.69                                                 |
|  Raw incl dropped  trades=1815  real=$+9,806.14                        |
|  Today     trades=65  avg=-35.8%  med=-59.3%  real=$-1,409.20          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  ... 253 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (17)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b83  S210 CVNA260807C00073000 x1 stop_loss (-56.5%)                   |
|  ... 12 more pending exit(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (44)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          22    -44.4%   $   -281.00               |
|  NKE260807C00042000            9    -48.5%   $   -279.90               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500           10    -44.9%   $   -253.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260821C00044000           12    -25.4%   $   -192.00               |
|  ... 36 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=30.7s reconcile=0.64s cancel=0.21s manage=29.19s
STATUS: options_morning_bot run complete (PAPER) elapsed=30.7s. run=#6296 https://github.com/28twagg-ops/TradingBot/actions/runs/31123548118
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 37 buckets closed trades, $-1,409.20 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=92 drop=13
Orphan rate: 7.6% (138/1815)
# Options signal frequency

_Generated 2026-08-06T13:36:35.356563_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    28 | WARN | <<<
| Total open lots             |   184 | INFO |
| Total closed lots           |  1210 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.84 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T174135Z

- UTC timestamp: `20260806T174135Z`
- GitHub run: [#6297](https://github.com/28twagg-ops/TradingBot/actions/runs/31123786232)
- Run id: `31123786232`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`26s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T13:41:38.819459-04:00","date":"2026-08-06","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":19.7,"phases_s":{"reconcile":0.62,"cancel":0.18,"manage":18.32},"signals":0,"placed":0,"equity":142314.8,"open_positions":43,"pending_orders":0,"open_lots":177,"submitted_today":138,"filled_today":167,"unattributed_contracts":4,"top_signals":[],"github_run":"6297","github_run_id":"31123786232","status":"ok"}
```

### Live bot full output

```text
17:41:35  INFO      Mode: exits
17:41:36  INFO        Daily log -> logs/daily/2026-08-06.md
17:41:36  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
17:41:36  INFO        place_all_stops: checking 1 positions...
17:41:36  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
17:41:37  INFO        [positions] 1/1 (1 valid)
17:41:37  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.67|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  JBL  P&L +1.6%  $+1.51                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=184 paper_keys=yes dry_run=False
  alpaca positions=46
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T13:41:38.819459-04:00 ===

[Run context]
Paper auth OK — equity $142314.80, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 13:41:41,797 INFO   EXIT [b72|lab0072_s209_w1_0928_1005_r1|S209] stop_loss (-64.7%) SELL 1 UPST260807C00032000 @<= 0.07
2026-08-06 13:41:42,482 INFO   EXIT [b835|lab0835_s406_w4_1120_1135_r2|S406] stop_loss (-54.5%) SELL 1 PLTR260807C00170000 @<= 0.02
2026-08-06 13:41:44,140 INFO   EXIT [b788|lab0788_s398_w3_1045_1120_r1|S398] take_profit (+120.3%) SELL 1 UBER260807C00070000 @<= 0.68
2026-08-06 13:41:47,576 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-64.5%) SELL 2 META260807C00622500 @<= 0.20
2026-08-06 13:41:49,171 INFO   EXIT [b74|lab0074_s209_w2_1005_1045_r1|S209] stop_loss (-52.0%) SELL 1 AMD260807C00537500 @<= 0.28
2026-08-06 13:41:49,728 INFO   EXIT [b912|lab0912_s412_w1_0928_1005_r1|S412] stop_loss (-50.1%) SELL 1 NKE260807C00042000 @<= 0.33
2026-08-06 13:41:54,657 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-53.8%) SELL 1 AMD260807C00570000 @<= 0.04
2026-08-06 13:41:56,911 INFO   EXIT [b292|lab0292_s352_w3_1045_1120_r1|S352] stop_loss (-52.2%) SELL 1 CRWD260807C00217500 @<= 0.23
2026-08-06 13:41:58,078 INFO   EXIT [b237|lab0237_s401_w2_1005_1045_r2|S401] stop_loss (-51.4%) SELL 1 TSLA260810C00342500 @<= 0.22

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $142,314.80                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             177                                     |
|  Broker option positions       43                                      |
|  Unattributed contracts        4 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1289  buckets=263  win=42%                           |
|  Returns   avg=+25.5%  med=-28.3%  p10=-77.8%  p90=+138.6%             |
|  Realized  $+11,332.19                                                 |
|  Raw incl dropped  trades=1823  real=$+9,736.64                        |
|  Today     trades=73  avg=-34.9%  med=-59.3%  real=$-1,478.70          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b318 lab0318_s355_w4_11  1 100% +292.9 +292.9 +292.9 $   +123         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  ... 255 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (18)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b83  S210 CVNA260807C00073000 x1 stop_loss (-56.5%)                   |
|  ... 13 more pending exit(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (43)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          22    -47.9%   $   -303.00               |
|  NKE260807C00042000            9    -51.6%   $   -297.90               |
|  AMD260807C00537500           10    -52.0%   $   -293.00               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260821C00044000           12    -25.4%   $   -192.00               |
|  ... 35 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=19.7s reconcile=0.62s cancel=0.18s manage=18.32s
STATUS: options_morning_bot run complete (PAPER) elapsed=19.7s. run=#6297 https://github.com/28twagg-ops/TradingBot/actions/runs/31123786232
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 43 buckets closed trades, $-1,478.70 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=92 drop=13
Orphan rate: 7.6% (139/1823)
# Options signal frequency

_Generated 2026-08-06T13:42:02.299064_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    28 | WARN | <<<
| Total open lots             |   177 | INFO |
| Total closed lots           |  1217 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.67 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T175144Z

- UTC timestamp: `20260806T175144Z`
- GitHub run: [#6299](https://github.com/28twagg-ops/TradingBot/actions/runs/31124268359)
- Run id: `31124268359`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`18s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T13:51:48.482716-04:00","date":"2026-08-06","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.9,"phases_s":{"reconcile":0.36,"cancel":0.03,"manage":8.14},"signals":0,"placed":0,"equity":142487.62,"open_positions":41,"pending_orders":0,"open_lots":169,"submitted_today":138,"filled_today":167,"unattributed_contracts":4,"top_signals":[],"github_run":"6299","github_run_id":"31124268359","status":"ok"}
```

### Live bot full output

```text
17:51:45  INFO      Mode: exits
17:51:46  INFO        Daily log -> logs/daily/2026-08-06.md
17:51:46  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
17:51:46  INFO        place_all_stops: checking 1 positions...
17:51:46  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
17:51:46  INFO        [positions] 1/1 (1 valid)
17:51:46  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         17:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.78|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  JBL  P&L +1.7%  $+1.65                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=177 paper_keys=yes dry_run=False
  alpaca positions=43
  FLAG b72|S209|15602775 missing from Alpaca
  FLAG b835|S406|a436d28c missing from Alpaca
  FLAG b0|ORPHAN|6987e147 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T13:51:48.482716-04:00 ===

[Run context]
Paper auth OK — equity $142487.62, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 13:51:51,025 INFO   EXIT [b290|lab0290_s352_w2_1005_1045_r1|S352] stop_loss (-54.8%) SELL 1 COIN260807C00160000 @<= 0.14
2026-08-06 13:51:51,497 INFO   EXIT [b363|lab0363_s361_w1_0928_1005_r2|S361] stop_loss (-50.1%) SELL 1 NKE260807C00042000 @<= 0.29
2026-08-06 13:51:53,638 INFO   EXIT [b284|lab0284_s351_w3_1045_1120_r1|S351] stop_loss (-52.2%) SELL 1 CRWD260807C00217500 @<= 0.19
2026-08-06 13:51:55,170 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-53.3%) SELL 2 AMD260807C00540000 @<= 0.22
2026-08-06 13:51:55,348 INFO   EXIT [b28|lab0028_s203_w3_1045_1120_r1|S203] take_profit (+52.7%) SELL 1 TTD260807P00017000 @<= 0.81
2026-08-06 13:51:55,565 INFO   EXIT [b298|lab0298_s353_w2_1005_1045_r1|S353] take_profit (+210.3%) SELL 1 UBER260807C00070000 @<= 1.01
2026-08-06 13:51:55,925 INFO   EXIT [b317|lab0317_s355_w3_1045_1120_r2|S355] take_profit (+100.0%) SELL 1 UBER260814C00072000 @<= 0.86
2026-08-06 13:51:56,078 INFO   EXIT [b334|lab0334_s357_w4_1120_1135_r1|S357] take_profit (+63.8%) SELL 1 UBER260828C00075000 @<= 0.87

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $142,487.62                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             169                                     |
|  Broker option positions       41                                      |
|  Unattributed contracts        4 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1295  buckets=264  win=42%                           |
|  Returns   avg=+25.4%  med=-28.3%  p10=-77.7%  p90=+138.3%             |
|  Realized  $+11,317.19                                                 |
|  Raw incl dropped  trades=1829  real=$+9,721.64                        |
|  Today     trades=79  avg=-32.0%  med=-56.5%  real=$-1,493.70          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 256 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (18)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b83  S210 CVNA260807C00073000 x1 stop_loss (-56.5%)                   |
|  ... 13 more pending exit(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (41)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          22    -54.8%   $   -347.00               |
|  AMD260807C00537500           10    -55.6%   $   -313.00               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260807C00042000            7    -50.1%   $   -224.70               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260821C00044000           12    -25.4%   $   -192.00               |
|  ... 33 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=8.9s reconcile=0.36s cancel=0.03s manage=8.14s
STATUS: options_morning_bot run complete (PAPER) elapsed=8.9s. run=#6299 https://github.com/28twagg-ops/TradingBot/actions/runs/31124268359
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 47 buckets closed trades, $-1,493.70 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=93 drop=12
Orphan rate: 7.6% (140/1829)
# Options signal frequency

_Generated 2026-08-06T13:52:03.217931_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    27 | WARN | <<<
| Total open lots             |   169 | INFO |
| Total closed lots           |  1222 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.81 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T182928Z

- UTC timestamp: `20260806T182928Z`
- GitHub run: [#6307](https://github.com/28twagg-ops/TradingBot/actions/runs/31125876398)
- Run id: `31125876398`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`17s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T14:29:34.418364-04:00","date":"2026-08-06","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.8,"phases_s":{"reconcile":0.51,"cancel":0.07,"manage":8.77},"signals":0,"placed":0,"equity":142822.37,"open_positions":34,"pending_orders":0,"open_lots":157,"submitted_today":138,"filled_today":167,"unattributed_contracts":5,"top_signals":[],"github_run":"6307","github_run_id":"31125876398","status":"ok"}
```

### Live bot full output

```text
18:29:31  INFO      Mode: exits
18:29:32  INFO        Daily log -> logs/daily/2026-08-06.md
18:29:32  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
18:29:32  INFO        place_all_stops: checking 1 positions...
18:29:32  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
18:29:32  INFO        [positions] 1/1 (1 valid)
18:29:32  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:29 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.89|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  JBL  P&L +1.8%  $+1.73                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=169 paper_keys=yes dry_run=False
  alpaca positions=38
  FLAG b780|S397|19a3768b missing from Alpaca
  FLAG b298|S353|adb06f59 missing from Alpaca
  FLAG b0|ORPHAN|79c3fa94 missing from Alpaca
  FLAG b317|S355|cfc8d0ff missing from Alpaca
  FLAG b0|ORPHAN|9722ef52 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T14:29:34.418364-04:00 ===

[Run context]
Paper auth OK — equity $142822.37, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 14:29:36,823 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-52.2%) SELL 1 CRWD260807C00217500 @<= 0.23
2026-08-06 14:29:37,043 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+53.1%) SELL 1 UBER260814C00073000 @<= 0.59
2026-08-06 14:29:38,208 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-52.6%) SELL 1 AMD260807C00550000 @<= 0.10
2026-08-06 14:29:38,496 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-81.8%) SELL 2 COP260807P00111000 @<= 0.03
2026-08-06 14:29:40,729 INFO   EXIT [b369|lab0369_s361_w4_1120_1135_r2|S361] stop_loss (-55.6%) SELL 1 AMD260807C00537500 @<= 0.26
2026-08-06 14:29:43,568 INFO   EXIT [b31|lab0031_s203_w4_1120_1135_r2|S203] take_profit (+56.4%) SELL 1 TTD260807P00017000 @<= 0.87
2026-08-06 14:29:43,887 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+75.2%) SELL 2 UBER260828C00075000 @<= 0.89

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $142,822.37                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             157                                     |
|  Broker option positions       34                                      |
|  Unattributed contracts        5 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1304  buckets=268  win=41%                           |
|  Returns   avg=+25.2%  med=-30.8%  p10=-77.7%  p90=+137.7%             |
|  Realized  $+11,201.36                                                 |
|  Raw incl dropped  trades=1838  real=$+9,605.81                        |
|  Today     trades=88  avg=-30.3%  med=-55.4%  real=$-1,609.53          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 260 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (14)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b83  S210 CVNA260807C00073000 x1 stop_loss (-56.5%)                   |
|  ... 9 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (34)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          21    -47.9%   $   -289.23               |
|  AMD260807C00537500            9    -55.6%   $   -281.70               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260807C00042000            7    -39.2%   $   -175.70               |
|  NKE260828C00045000           12    -20.8%   $   -158.00               |
|  NKE260821C00044000           12    -15.9%   $   -120.00               |
|  ... 26 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=9.8s reconcile=0.51s cancel=0.07s manage=8.77s
STATUS: options_morning_bot run complete (PAPER) elapsed=9.8s. run=#6307 https://github.com/28twagg-ops/TradingBot/actions/runs/31125876398
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 53 buckets closed trades, $-1,609.53 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=93 drop=12
Orphan rate: 7.7% (142/1838)
# Options signal frequency

_Generated 2026-08-06T14:29:48.522736_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    25 | WARN | <<<
| Total open lots             |   157 | INFO |
| Total closed lots           |  1229 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.89 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T184543Z

- UTC timestamp: `20260806T184543Z`
- GitHub run: [#6310](https://github.com/28twagg-ops/TradingBot/actions/runs/31126317612)
- Run id: `31126317612`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`23s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T14:45:48.489445-04:00","date":"2026-08-06","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":14.0,"phases_s":{"reconcile":0.71,"cancel":0.23,"manage":12.34},"signals":0,"placed":0,"equity":142346.21,"open_positions":33,"pending_orders":0,"open_lots":152,"submitted_today":138,"filled_today":167,"unattributed_contracts":8,"top_signals":[],"github_run":"6310","github_run_id":"31126317612","status":"ok"}
```

### Live bot full output

```text
18:45:44  INFO      Mode: exits
18:45:45  INFO        Daily log -> logs/daily/2026-08-06.md
18:45:45  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
18:45:45  INFO        place_all_stops: checking 1 positions...
18:45:45  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
18:45:45  INFO        [positions] 1/1 (1 valid)
18:45:46  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         18:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.61|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  JBL  P&L +1.5%  $+1.45                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=157 paper_keys=yes dry_run=False
  alpaca positions=35
  FLAG b0|ORPHAN|d4db12c7 missing from Alpaca
  FLAG b0|ORPHAN|d77c45e7 missing from Alpaca
  FLAG b0|ORPHAN|f1d99105 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T14:45:48.489445-04:00 ===

[Run context]
Paper auth OK — equity $142345.13, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 14:45:51,148 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-50.0%) SELL 2 RBLX260807C00038500 @<= 0.11
2026-08-06 14:45:56,547 INFO   EXIT [b30|lab0030_s203_w4_1120_1135_r1|S203] take_profit (+56.4%) SELL 1 TTD260807P00017000 @<= 0.89
2026-08-06 14:45:57,384 INFO   EXIT [b279|lab0279_s350_w2_1005_1045_r2|S350] stop_loss (-65.2%) SELL 1 COIN260807C00160000 @<= 0.11

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $142,346.21                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             152                                     |
|  Broker option positions       33                                      |
|  Unattributed contracts        8 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1309  buckets=268  win=41%                           |
|  Returns   avg=+25.1%  med=-30.0%  p10=-77.8%  p90=+137.6%             |
|  Realized  $+11,312.92                                                 |
|  Raw incl dropped  trades=1843  real=$+9,717.37                        |
|  Today     trades=93  avg=-28.2%  med=-54.2%  real=$-1,497.97          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 260 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (12)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b83  S210 CVNA260807C00073000 x1 stop_loss (-56.5%)                   |
|  ... 7 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (33)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          21    -65.2%   $   -394.23               |
|  AMD260807C00537500            9    -59.1%   $   -299.70               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260807C00042000            7    -40.7%   $   -182.70               |
|  NKE260828C00045000           12    -22.4%   $   -170.00               |
|  NKE260821C00044000           12    -17.5%   $   -132.00               |
|  ... 25 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=14.0s reconcile=0.71s cancel=0.23s manage=12.34s
STATUS: options_morning_bot run complete (PAPER) elapsed=14.0s. run=#6310 https://github.com/28twagg-ops/TradingBot/actions/runs/31126317612
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 54 buckets closed trades, $-1,497.97 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=93 drop=12
Orphan rate: 7.9% (146/1843)
# Options signal frequency

_Generated 2026-08-06T14:46:08.016069_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   152 | INFO |
| Total closed lots           |  1230 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.61 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T190553Z

- UTC timestamp: `20260806T190553Z`
- GitHub run: [#6314](https://github.com/28twagg-ops/TradingBot/actions/runs/31126621687)
- Run id: `31126621687`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`22s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T15:05:56.637879-04:00","date":"2026-08-06","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":13.0,"phases_s":{"reconcile":0.23,"cancel":0.03,"manage":12.37},"signals":0,"placed":0,"equity":142234.39,"open_positions":32,"pending_orders":0,"open_lots":149,"submitted_today":138,"filled_today":167,"unattributed_contracts":7,"top_signals":[],"github_run":"6314","github_run_id":"31126621687","status":"ok"}
```

### Live bot full output

```text
19:05:54  INFO      Mode: exits
19:05:54  INFO        Daily log -> logs/daily/2026-08-06.md
19:05:54  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
19:05:54  INFO        place_all_stops: checking 1 positions...
19:05:54  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
19:05:54  INFO        [positions] 1/1 (1 valid)
19:05:54  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.86|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  JBL  P&L +1.8%  $+1.70                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=152 paper_keys=yes dry_run=False
  alpaca positions=34
  FLAG b30|S203|72f2174a missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T15:05:56.637879-04:00 ===

[Run context]
Paper auth OK — equity $142234.39, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 15:06:00,974 INFO   EXIT [b863|lab0863_s408_w4_1120_1135_r2|S408] stop_loss (-60.0%) SELL 1 PLTR260807C00175000 @<= 0.03
2026-08-06 15:06:03,814 INFO   EXIT [b795|lab0795_s399_w2_1005_1045_r2|S399] stop_loss (-60.0%) SELL 1 COIN260807C00170000 @<= 0.01
2026-08-06 15:06:05,226 INFO   EXIT [b278|lab0278_s350_w2_1005_1045_r1|S350] stop_loss (-65.2%) SELL 1 COIN260807C00160000 @<= 0.11

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $142,234.39                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             149                                     |
|  Broker option positions       32                                      |
|  Unattributed contracts        7 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1311  buckets=269  win=41%                           |
|  Returns   avg=+25.0%  med=-31.6%  p10=-77.8%  p90=+137.5%             |
|  Realized  $+11,264.92                                                 |
|  Raw incl dropped  trades=1845  real=$+9,669.37                        |
|  Today     trades=95  avg=-28.8%  med=-54.2%  real=$-1,545.97          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 261 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (12)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b83  S210 CVNA260807C00073000 x1 stop_loss (-56.5%)                   |
|  ... 7 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (32)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          20    -65.2%   $   -375.45               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500            8    -46.7%   $   -210.40               |
|  NKE260807C00042000            7    -36.0%   $   -161.70               |
|  NKE260828C00045000           12    -16.1%   $   -122.00               |
|  NKE260821C00044000           12    -14.3%   $   -108.00               |
|  ... 24 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=13.0s reconcile=0.23s cancel=0.03s manage=12.37s
STATUS: options_morning_bot run complete (PAPER) elapsed=13.0s. run=#6314 https://github.com/28twagg-ops/TradingBot/actions/runs/31126621687
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 56 buckets closed trades, $-1,545.97 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=93 drop=12
Orphan rate: 7.9% (146/1845)
# Options signal frequency

_Generated 2026-08-06T15:06:15.152951_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   149 | INFO |
| Total closed lots           |  1232 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.86 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T192047Z

- UTC timestamp: `20260806T192047Z`
- GitHub run: [#6317](https://github.com/28twagg-ops/TradingBot/actions/runs/31126798253)
- Run id: `31126798253`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`18s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T15:20:50.577395-04:00","date":"2026-08-06","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":9.3,"phases_s":{"reconcile":0.2,"cancel":0.03,"manage":8.55},"signals":0,"placed":0,"equity":142473.15,"open_positions":31,"pending_orders":0,"open_lots":147,"submitted_today":138,"filled_today":167,"unattributed_contracts":6,"top_signals":[],"github_run":"6317","github_run_id":"31126798253","status":"ok"}
```

### Live bot full output

```text
19:20:48  INFO      Mode: exits
19:20:48  INFO        Daily log -> logs/daily/2026-08-06.md
19:20:48  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
19:20:48  INFO        place_all_stops: checking 1 positions...
19:20:48  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
19:20:48  INFO        [positions] 1/1 (1 valid)
19:20:48  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.92|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  JBL  P&L +1.9%  $+1.76                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=149 paper_keys=yes dry_run=False
  alpaca positions=34
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T15:20:50.577395-04:00 ===

[Run context]
Paper auth OK — equity $142473.15, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 15:20:58,461 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-60.0%) SELL 1 COIN260807C00170000 @<= 0.01
2026-08-06 15:20:59,193 INFO   EXIT [b819|lab0819_s405_w3_1045_1120_r2|S405] stop_loss (-58.3%) SELL 1 COIN260807C00160000 @<= 0.09

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $142,473.15                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             147                                     |
|  Broker option positions       31                                      |
|  Unattributed contracts        6 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1313  buckets=269  win=41%                           |
|  Returns   avg=+24.8%  med=-32.0%  p10=-77.7%  p90=+137.4%             |
|  Realized  $+11,246.92                                                 |
|  Raw incl dropped  trades=1847  real=$+9,651.37                        |
|  Today     trades=97  avg=-29.4%  med=-54.3%  real=$-1,563.97          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 261 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (12)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b83  S210 CVNA260807C00073000 x1 stop_loss (-56.5%)                   |
|  ... 7 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (31)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          18    -58.3%   $   -301.91               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260807C00042000            7    -43.8%   $   -196.70               |
|  AMD260807C00537500            8    -43.2%   $   -194.40               |
|  NKE260828C00045000           12    -24.0%   $   -182.00               |
|  NKE260821C00044000           12    -20.6%   $   -156.00               |
|  ... 23 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=9.3s reconcile=0.2s cancel=0.03s manage=8.55s
STATUS: options_morning_bot run complete (PAPER) elapsed=9.3s. run=#6317 https://github.com/28twagg-ops/TradingBot/actions/runs/31126798253
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 58 buckets closed trades, $-1,563.97 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=92 drop=13
Orphan rate: 7.9% (146/1847)
# Options signal frequency

_Generated 2026-08-06T15:21:05.458810_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    21 | WARN | <<<
| Total open lots             |   147 | INFO |
| Total closed lots           |  1234 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.92 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T192542Z

- UTC timestamp: `20260806T192542Z`
- GitHub run: [#6318](https://github.com/28twagg-ops/TradingBot/actions/runs/31126861353)
- Run id: `31126861353`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`18s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T15:25:46.081406-04:00","date":"2026-08-06","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":10.3,"phases_s":{"reconcile":0.31,"cancel":0.09,"manage":9.4},"signals":0,"placed":0,"equity":141693.07,"open_positions":30,"pending_orders":0,"open_lots":145,"submitted_today":138,"filled_today":167,"unattributed_contracts":5,"top_signals":[],"github_run":"6318","github_run_id":"31126861353","status":"ok"}
```

### Live bot full output

```text
19:25:43  INFO      Mode: exits
19:25:43  INFO        Daily log -> logs/daily/2026-08-06.md
19:25:43  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
19:25:43  INFO        place_all_stops: checking 1 positions...
19:25:43  INFO        STOP skipped JBL: fractional (0.2749 shares) — software exit will handle it
19:25:43  INFO        [positions] 1/1 (1 valid)
19:25:43  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         19:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.53|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  JBL  P&L +1.5%  $+1.37                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=147 paper_keys=yes dry_run=False
  alpaca positions=33
  FLAG b0|ORPHAN|3b7ad734 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T15:25:46.081406-04:00 ===

[Run context]
Paper auth OK — equity $141677.07, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 15:25:48,975 INFO   EXIT [b368|lab0368_s361_w4_1120_1135_r1|S361] stop_loss (-57.4%) SELL 1 AMD260807C00537500 @<= 0.21
2026-08-06 15:25:50,253 INFO   EXIT [b283|lab0283_s351_w2_1005_1045_r2|S351] stop_loss (-58.3%) SELL 1 COIN260807C00160000 @<= 0.08
2026-08-06 15:25:50,561 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-54.3%) SELL 2 RBLX260807C00037500 @<= 0.13

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $141,693.07                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             145                                     |
|  Broker option positions       30                                      |
|  Unattributed contracts        5 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1315  buckets=269  win=41%                           |
|  Returns   avg=+24.7%  med=-32.0%  p10=-77.8%  p90=+137.3%             |
|  Realized  $+11,162.82                                                 |
|  Raw incl dropped  trades=1849  real=$+9,567.27                        |
|  Today     trades=99  avg=-30.4%  med=-55.6%  real=$-1,648.07          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 261 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (13)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b83  S210 CVNA260807C00073000 x1 stop_loss (-56.5%)                   |
|  ... 8 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (30)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          17    -61.8%   $   -302.14               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500            7    -57.4%   $   -226.10               |
|  NKE260807C00042000            7    -43.8%   $   -196.70               |
|  NKE260828C00045000           12    -24.0%   $   -182.00               |
|  NKE260821C00044000           12    -19.0%   $   -144.00               |
|  ... 22 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=10.3s reconcile=0.31s cancel=0.09s manage=9.4s
STATUS: options_morning_bot run complete (PAPER) elapsed=10.3s. run=#6318 https://github.com/28twagg-ops/TradingBot/actions/runs/31126861353
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 59 buckets closed trades, $-1,648.07 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (147/1849)
# Options signal frequency

_Generated 2026-08-06T15:26:01.427270_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    20 | WARN | <<<
| Total open lots             |   145 | INFO |
| Total closed lots           |  1235 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.53 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T194048Z

- UTC timestamp: `20260806T194048Z`
- GitHub run: [#6321](https://github.com/28twagg-ops/TradingBot/actions/runs/31127042255)
- Run id: `31127042255`
- Live bot: exit=`0`, duration=`216s`
- Options bot: exit=`0`, duration=`25s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T15:44:27.013168-04:00","date":"2026-08-06","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.2,"phases_s":{"reconcile":0.48,"cancel":0.16,"manage":14.91},"signals":0,"placed":0,"equity":141639.98,"open_positions":29,"pending_orders":0,"open_lots":142,"submitted_today":138,"filled_today":167,"unattributed_contracts":4,"top_signals":[],"github_run":"6321","github_run_id":"31127042255","status":"ok"}
```

### Live bot full output

```text
19:40:49  INFO      Mode: evening_prep
19:40:50  INFO        [prep_positions] 1/1 (1 valid)
19:40:50  INFO        Universe cache hit: 903 tickers (tickers_2026-08-06.json)
19:40:51  INFO        [prep_universe] 40/902 (40 valid)
19:40:53  INFO        [prep_universe] 80/902 (80 valid)
19:40:55  INFO        [prep_universe] 120/902 (120 valid)
19:40:56  INFO        [prep_universe] 160/902 (160 valid)
19:40:58  INFO        [prep_universe] 200/902 (199 valid)
19:41:03  INFO        [prep_universe] 240/902 (238 valid)
19:41:16  INFO        [prep_universe] 280/902 (278 valid)
19:41:27  INFO        [prep_universe] 320/902 (318 valid)
19:41:40  INFO        [prep_universe] 360/902 (358 valid)
19:41:51  INFO        [prep_universe] 400/902 (397 valid)
19:42:04  INFO        [prep_universe] 440/902 (437 valid)
19:42:15  INFO        [prep_universe] 480/902 (477 valid)
19:42:28  INFO        [prep_universe] 520/902 (517 valid)
19:42:39  INFO        [prep_universe] 560/902 (557 valid)
19:42:53  INFO        [prep_universe] 600/902 (597 valid)
19:43:03  INFO        [prep_universe] 640/902 (637 valid)
19:43:16  INFO        [prep_universe] 680/902 (677 valid)
19:43:27  INFO        [prep_universe] 720/902 (717 valid)
19:43:40  INFO        [prep_universe] 760/902 (757 valid)
19:43:51  INFO        [prep_universe] 800/902 (797 valid)
19:44:04  INFO        [prep_universe] 840/902 (836 valid)
19:44:14  INFO        [prep_universe] 880/902 (876 valid)
19:44:21  INFO        [prep_universe] 902/902 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      EVENING_PREP|
|  Time                                                         19:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.59|
+========================================================================+

+========================================================================+
|                              EVENING PREP                              |
+========================================================================+
|  Goal                   Precompute exits/signals for next execution run|
|  Plan file                                 logs/plans/evening_plan.json|
|  Regime                                                            BULL|
+========================================================================+

+========================================================================+
|                       OPEN POSITION P&L SNAPSHOT                       |
+========================================================================+
|  Open positions                                                       1|
|  Invested                                                        $95.61|
|  Open P&L                                                        $+1.43|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  JBL      Pullback50      $95.61     $342.57  $347.76  +1.5%   $+1.43  |
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
|  Exit candidates                                                      1|
|  Signal candidates                                                   21|
|  Universe scanned                                                   902|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=145 paper_keys=yes dry_run=False
  alpaca positions=32
  FLAG b0|ORPHAN|85a059fc missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T15:44:27.013168-04:00 ===

[Run context]
Paper auth OK — equity $141639.98, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 15:44:29,435 INFO   EXIT [b900|lab0900_s411_w2_1005_1045_r1|S411] stop_loss (-52.5%) SELL 1 AMD260807C00535000 @<= 0.25
2026-08-06 15:44:30,366 INFO   EXIT [b355|lab0355_s360_w4_1120_1135_r2|S360] stop_loss (-68.0%) SELL 1 AMD260807C00537500 @<= 0.19
2026-08-06 15:44:34,209 INFO   EXIT [b844|lab0844_s407_w2_1005_1045_r1|S407] stop_loss (-52.6%) SELL 1 AMD260807C00550000 @<= 0.06
2026-08-06 15:44:38,736 INFO   EXIT [b282|lab0282_s351_w2_1005_1045_r1|S351] stop_loss (-75.7%) SELL 1 COIN260807C00160000 @<= 0.08
2026-08-06 15:44:38,996 INFO   EXIT [b362|lab0362_s361_w1_0928_1005_r1|S361] stop_loss (-50.1%) SELL 1 NKE260807C00042000 @<= 0.29

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $141,639.98                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             142                                     |
|  Broker option positions       29                                      |
|  Unattributed contracts        4 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1318  buckets=270  win=41%                           |
|  Returns   avg=+24.5%  med=-32.7%  p10=-77.8%  p90=+137.2%             |
|  Realized  $+11,014.62                                                 |
|  Raw incl dropped  trades=1852  real=$+9,419.07                        |
|  Today     trades=102  avg=-31.4%  med=-56.5%  real=$-1,796.27         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 262 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (15)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-92.7%)                 |
|  b96  S211 AMZN260807C00297500 x1 stop_loss (-97.1%)                   |
|  b779 S397 AMZN260807C00295000 x1 stop_loss (-95.0%)                   |
|  b780 S397 AMZN260807C00292500 x1 stop_loss (-96.3%)                   |
|  b83  S210 CVNA260807C00073000 x1 stop_loss (-56.5%)                   |
|  ... 10 more pending exit(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (29)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          17    -75.7%   $   -370.14               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500            7    -68.0%   $   -268.10               |
|  NKE260828C00045000           12    -27.2%   $   -206.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  NKE260821C00044000           12    -23.8%   $   -180.00               |
|  ... 21 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=16.2s reconcile=0.48s cancel=0.16s manage=14.91s
STATUS: options_morning_bot run complete (PAPER) elapsed=16.2s. run=#6321 https://github.com/28twagg-ops/TradingBot/actions/runs/31127042255
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 61 buckets closed trades, $-1,796.27 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (148/1852)
# Options signal frequency

_Generated 2026-08-06T15:44:48.744926_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    19 | WARN | <<<
| Total open lots             |   142 | INFO |
| Total closed lots           |  1237 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=471.53 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T200548Z

- UTC timestamp: `20260806T200548Z`
- GitHub run: [#6326](https://github.com/28twagg-ops/TradingBot/actions/runs/31127345054)
- Run id: `31127345054`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`26s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T16:05:53.281066-04:00","date":"2026-08-06","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.8,"phases_s":{"reconcile":0.72,"cancel":0.23,"manage":15.05},"signals":0,"placed":0,"equity":141058.86,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":138,"filled_today":167,"unattributed_contracts":7,"top_signals":[],"github_run":"6326","github_run_id":"31127345054","status":"ok"}
```

### Live bot full output

```text
20:05:49  INFO      Mode: ext_exits
20:05:50  INFO        Daily log -> logs/daily/2026-08-06.md
20:05:50  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
20:05:50  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.74|
+========================================================================+

+========================================================================+
|                       EXIT CHECK [EXTENDED HRS]                        |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  JBL  P&L +0.6%  $+0.58          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=142 paper_keys=yes dry_run=False
  alpaca positions=30
  FLAG b844|S407|b8c23402 missing from Alpaca
  FLAG b0|ORPHAN|6a7e0d15 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T16:05:53.281066-04:00 ===

[Run context]
Paper auth OK — equity $141058.86, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-06 16:05:55,681 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-100.0%) SELL 1 AMZN260807C00302500 @<= 0.01
2026-08-06 16:05:56,335 INFO   EXIT [b777|lab0777_s397_w1_0928_1005_r2|S397] stop_loss (-100.0%) SELL 1 AMZN260807C00292500 @<= 0.01
2026-08-06 16:05:57,021 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+82.9%) SELL 2 DKNG260807C00023000 @<= 0.01
  EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+82.9%) LIMIT fallback SELL 2 DKNG260807C00023000 @<= 0.01 return=+82.9%
2026-08-06 16:05:58,464 INFO   EXIT [b354|lab0354_s360_w4_1120_1135_r1|S360] stop_loss (-80.5%) SELL 1 AMD260807C00537500 @<= 0.01
  EXIT [b354|lab0354_s360_w4_1120_1135_r1|S360] stop_loss (-80.5%) LIMIT fallback SELL 1 AMD260807C00537500 @<= 0.01 return=-80.5%
2026-08-06 16:05:58,949 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-100.0%) SELL 1 UBER260807C00078000 @<= 0.01
  EXIT [b96|lab0096_s211_w2_1005_1045_r1|S211] stop_loss (-100.0%) SELL failed AMZN260807C00297500: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-06 16:05:59,538 INFO   EXIT [b378|lab0378_s362_w2_1005_1045_r1|S362] stop_loss (-100.0%) SELL 1 AMZN260807C00297500 @<= 0.01
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] stop_loss (-82.2%) SELL failed CVNA260807C00072000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] stop_loss (-82.2%) market+limit failed CVNA260807C00072000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-06 16:06:00,530 INFO   EXIT [b112|lab0112_s212_w3_1045_1120_r1|S212] stop_loss (-82.2%) SELL 1 CVNA260807C00072000 @<= 0.01
  EXIT [b112|lab0112_s212_w3_1045_1120_r1|S212] stop_loss (-82.2%) LIMIT fallback SELL 1 CVNA260807C00072000 @<= 0.01 return=-82.2%
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] stop_loss (-74.5%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] stop_loss (-74.5%) market+limit failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-06 16:06:01,230 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-74.5%) SELL 1 CVNA260807C00071000 @<= 0.01
  EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-74.5%) LIMIT fallback SELL 1 CVNA260807C00071000 @<= 0.01 return=-74.5%
2026-08-06 16:06:02,505 INFO   EXIT [b377|lab0377_s362_w1_0928_1005_r2|S362] stop_loss (-50.1%) SELL 1 NKE260807C00042000 @<= 0.01
  EXIT [b377|lab0377_s362_w1_0928_1005_r2|S362] stop_loss (-50.1%) LIMIT fallback SELL 1 NKE260807C00042000 @<= 0.01 return=-50.1%
  EXIT [b863|lab0863_s408_w4_1120_1135_r2|S408] stop_loss (-60.0%) SELL failed PLTR260807C00175000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-06 16:06:04,602 INFO   EXIT [b862|lab0862_s408_w4_1120_1135_r1|S408] stop_loss (-60.0%) SELL 1 PLTR260807C00175000 @<= 0.01
  EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-90.0%) SELL failed RBLX260807C00038500: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-90.0%) market+limit failed RBLX260807C00038500: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-06 16:06:06,246 INFO   EXIT [b77|lab0077_s209_w3_1045_1120_r2|S209] stop_loss (-72.9%) SELL 1 AMD260807C00535000 @<= 0.01
  EXIT [b77|lab0077_s209_w3_1045_1120_r2|S209] stop_loss (-72.9%) LIMIT fallback SELL 1 AMD260807C00535000 @<= 0.01 return=-72.9%
2026-08-06 16:06:06,963 INFO   EXIT [b295|lab0295_s352_w4_1120_1135_r2|S352] stop_loss (-75.7%) SELL 1 COIN260807C00160000 @<= 0.01
  EXIT [b295|lab0295_s352_w4_1120_1135_r2|S352] stop_loss (-75.7%) LIMIT fallback SELL 1 COIN260807C00160000 @<= 0.01 return=-75.7%
2026-08-06 16:06:08,124 INFO   EXIT [b905|lab0905_s411_w4_1120_1135_r2|S411] stop_loss (-68.3%) SELL 1 AMD260807C00532500 @<= 0.01
  EXIT [b905|lab0905_s411_w4_1120_1135_r2|S411] stop_loss (-68.3%) LIMIT fallback SELL 1 AMD260807C00532500 @<= 0.01 return=-68.3%
  EXIT [b83|lab0083_s210_w2_1005_1045_r2|S210] stop_loss (-82.6%) SELL failed CVNA260807C00073000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b83|lab0083_s210_w2_1005_1045_r2|S210] stop_loss (-82.6%) market+limit failed CVNA260807C00073000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-06 16:06:08,890 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-82.6%) SELL 1 CVNA260807C00073000 @<= 0.01
  EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-82.6%) LIMIT fallback SELL 1 CVNA260807C00073000 @<= 0.01 return=-82.6%
  EXIT [b803|lab0803_s404_w2_1005_1045_r2|S404] stop_loss (-100.0%) SELL failed AMZN260807C00295000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b779|lab0779_s397_w2_1005_1045_r2|S397] stop_loss (-100.0%) SELL failed AMZN260807C00295000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-06 16:06:09,610 INFO   EXIT [b778|lab0778_s397_w2_1005_1045_r1|S397] stop_loss (-100.0%) SELL 1 AMZN260807C00295000 @<= 0.01

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]

[Exit summary]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $141,058.86                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             136                                     |
|  Broker option positions       28                                      |
|  Unattributed contracts        7 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1323  buckets=271  win=41%                           |
|  Returns   avg=+24.2%  med=-33.3%  p10=-77.7%  p90=+137.0%             |
|  Realized  $+10,853.09                                                 |
|  Raw incl dropped  trades=1857  real=$+9,257.54                        |
|  Today     trades=107  avg=-32.8%  med=-56.5%  real=$-1,957.80         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 263 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (15)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b0   ORPHAN DKNG260807C00023000 x2 take_profit (+82.9%)               |
|  b354 S360 AMD260807C00537500 x1 stop_loss (-80.5%)                    |
|  b0   ORPHAN UBER260807C00078000 x1 stop_loss (-100.0%)                |
|  ... 10 more pending exit(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (28)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          16    -75.7%   $   -348.36               |
|  AMD260807C00537500            6    -80.5%   $   -271.80               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=16.8s reconcile=0.72s cancel=0.23s manage=15.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=16.8s. run=#6326 https://github.com/28twagg-ops/TradingBot/actions/runs/31127345054
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 64 buckets closed trades, $-1,957.80 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-06T16:06:15.664077_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    18 | WARN | <<<
| Total open lots             |   136 | INFO |
| Total closed lots           |  1241 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.74 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T203054Z

- UTC timestamp: `20260806T203054Z`
- GitHub run: [#6331](https://github.com/28twagg-ops/TradingBot/actions/runs/31127650086)
- Run id: `31127650086`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T16:30:59.562008-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.16},"signals":0,"placed":0,"equity":140870.86,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":138,"filled_today":167,"unattributed_contracts":7,"top_signals":[],"github_run":"6331","github_run_id":"31127650086","status":"ok"}
```

### Live bot full output

```text
20:30:57  INFO      Mode: ext_exits
20:30:57  INFO        Daily log -> logs/daily/2026-08-06.md
20:30:57  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
20:30:57  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.74|
+========================================================================+

+========================================================================+
|                       EXIT CHECK [EXTENDED HRS]                        |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  JBL  P&L +0.6%  $+0.58          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=136 paper_keys=yes dry_run=False
  alpaca positions=30
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T16:30:59.562008-04:00 ===

[Run context]
After hours (16:30 ET) — exit summary only.
Paper auth OK — equity $140870.86, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,870.86                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             136                                     |
|  Broker option positions       28                                      |
|  Unattributed contracts        7 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1323  buckets=271  win=41%                           |
|  Returns   avg=+24.2%  med=-33.3%  p10=-77.7%  p90=+137.0%             |
|  Realized  $+10,853.09                                                 |
|  Raw incl dropped  trades=1857  real=$+9,257.54                        |
|  Today     trades=107  avg=-32.8%  med=-56.5%  real=$-1,957.80         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 263 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (15)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b0   ORPHAN DKNG260807C00023000 x2 take_profit (+82.9%)               |
|  b354 S360 AMD260807C00537500 x1 stop_loss (-80.5%)                    |
|  b0   ORPHAN UBER260807C00078000 x1 stop_loss (-100.0%)                |
|  ... 10 more pending exit(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (28)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          16    -75.7%   $   -348.36               |
|  AMD260807C00537500            6    -80.5%   $   -271.80               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=0.6s reconcile=0.16s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.6s. run=#6331 https://github.com/28twagg-ops/TradingBot/actions/runs/31127650086
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 64 buckets closed trades, $-1,957.80 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-06T16:31:05.713087_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    18 | WARN | <<<
| Total open lots             |   136 | INFO |
| Total closed lots           |  1241 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.74 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T205551Z

- UTC timestamp: `20260806T205551Z`
- GitHub run: [#6336](https://github.com/28twagg-ops/TradingBot/actions/runs/31127945035)
- Run id: `31127945035`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T16:55:55.725751-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.16},"signals":0,"placed":0,"equity":140662.9,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":138,"filled_today":167,"unattributed_contracts":7,"top_signals":[],"github_run":"6336","github_run_id":"31127945035","status":"ok"}
```

### Live bot full output

```text
20:55:53  INFO      Mode: ext_exits
20:55:53  INFO        Daily log -> logs/daily/2026-08-06.md
20:55:53  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
20:55:53  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         20:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.74|
+========================================================================+

+========================================================================+
|                       EXIT CHECK [EXTENDED HRS]                        |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  JBL  P&L +0.6%  $+0.58          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=136 paper_keys=yes dry_run=False
  alpaca positions=30
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T16:55:55.725751-04:00 ===

[Run context]
After hours (16:55 ET) — exit summary only.
Paper auth OK — equity $140662.90, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,662.90                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             136                                     |
|  Broker option positions       28                                      |
|  Unattributed contracts        7 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1323  buckets=271  win=41%                           |
|  Returns   avg=+24.2%  med=-33.3%  p10=-77.7%  p90=+137.0%             |
|  Realized  $+10,853.09                                                 |
|  Raw incl dropped  trades=1857  real=$+9,257.54                        |
|  Today     trades=107  avg=-32.8%  med=-56.5%  real=$-1,957.80         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 263 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (15)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b0   ORPHAN DKNG260807C00023000 x2 take_profit (+82.9%)               |
|  b354 S360 AMD260807C00537500 x1 stop_loss (-80.5%)                    |
|  b0   ORPHAN UBER260807C00078000 x1 stop_loss (-100.0%)                |
|  ... 10 more pending exit(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (28)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          16    -75.7%   $   -348.36               |
|  AMD260807C00537500            6    -80.5%   $   -271.80               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=0.7s reconcile=0.16s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.7s. run=#6336 https://github.com/28twagg-ops/TradingBot/actions/runs/31127945035
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 64 buckets closed trades, $-1,957.80 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-06T16:56:02.046955_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    18 | WARN | <<<
| Total open lots             |   136 | INFO |
| Total closed lots           |  1241 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.74 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T210542Z

- UTC timestamp: `20260806T210542Z`
- GitHub run: [#6338](https://github.com/28twagg-ops/TradingBot/actions/runs/31128061622)
- Run id: `31128061622`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T17:05:46.678346-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.1,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":140642.86,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":138,"filled_today":167,"unattributed_contracts":7,"top_signals":[],"github_run":"6338","github_run_id":"31128061622","status":"ok"}
```

### Live bot full output

```text
21:05:43  INFO      Mode: ext_exits
21:05:44  INFO        Daily log -> logs/daily/2026-08-06.md
21:05:44  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
21:05:44  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.74|
+========================================================================+

+========================================================================+
|                       EXIT CHECK [EXTENDED HRS]                        |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  JBL  P&L +0.6%  $+0.58          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=136 paper_keys=yes dry_run=False
  alpaca positions=30
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T17:05:46.678346-04:00 ===

[Run context]
After hours (17:05 ET) — exit summary only.
Paper auth OK — equity $140642.86, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,642.86                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             136                                     |
|  Broker option positions       28                                      |
|  Unattributed contracts        7 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1323  buckets=271  win=41%                           |
|  Returns   avg=+24.2%  med=-33.3%  p10=-77.7%  p90=+137.0%             |
|  Realized  $+10,853.09                                                 |
|  Raw incl dropped  trades=1857  real=$+9,257.54                        |
|  Today     trades=107  avg=-32.8%  med=-56.5%  real=$-1,957.80         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 263 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (15)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b0   ORPHAN DKNG260807C00023000 x2 take_profit (+82.9%)               |
|  b354 S360 AMD260807C00537500 x1 stop_loss (-80.5%)                    |
|  b0   ORPHAN UBER260807C00078000 x1 stop_loss (-100.0%)                |
|  ... 10 more pending exit(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (28)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          16    -75.7%   $   -348.36               |
|  AMD260807C00537500            6    -80.5%   $   -271.80               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=1.1s reconcile=0.54s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.1s. run=#6338 https://github.com/28twagg-ops/TradingBot/actions/runs/31128061622
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 64 buckets closed trades, $-1,957.80 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-06T17:05:52.799270_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    18 | WARN | <<<
| Total open lots             |   136 | INFO |
| Total closed lots           |  1241 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.74 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T215048Z

- UTC timestamp: `20260806T215048Z`
- GitHub run: [#6347](https://github.com/28twagg-ops/TradingBot/actions/runs/31128571171)
- Run id: `31128571171`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T17:50:53.202422-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.44},"signals":0,"placed":0,"equity":140666.86,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":138,"filled_today":167,"unattributed_contracts":7,"top_signals":[],"github_run":"6347","github_run_id":"31128571171","status":"ok"}
```

### Live bot full output

```text
21:50:50  INFO      Mode: ext_exits
21:50:50  INFO        Daily log -> logs/daily/2026-08-06.md
21:50:50  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
21:50:51  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.74|
+========================================================================+

+========================================================================+
|                       EXIT CHECK [EXTENDED HRS]                        |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  JBL  P&L +0.6%  $+0.58          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=136 paper_keys=yes dry_run=False
  alpaca positions=30
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T17:50:53.202422-04:00 ===

[Run context]
After hours (17:50 ET) — exit summary only.
Paper auth OK — equity $140666.86, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,666.86                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             136                                     |
|  Broker option positions       28                                      |
|  Unattributed contracts        7 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1323  buckets=271  win=41%                           |
|  Returns   avg=+24.2%  med=-33.3%  p10=-77.7%  p90=+137.0%             |
|  Realized  $+10,853.09                                                 |
|  Raw incl dropped  trades=1857  real=$+9,257.54                        |
|  Today     trades=107  avg=-32.8%  med=-56.5%  real=$-1,957.80         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 263 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (15)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b0   ORPHAN DKNG260807C00023000 x2 take_profit (+82.9%)               |
|  b354 S360 AMD260807C00537500 x1 stop_loss (-80.5%)                    |
|  b0   ORPHAN UBER260807C00078000 x1 stop_loss (-100.0%)                |
|  ... 10 more pending exit(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (28)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          16    -75.7%   $   -348.36               |
|  AMD260807C00537500            6    -80.5%   $   -271.80               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=1.2s reconcile=0.44s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.2s. run=#6347 https://github.com/28twagg-ops/TradingBot/actions/runs/31128571171
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 64 buckets closed trades, $-1,957.80 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-06T17:50:59.560401_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    18 | WARN | <<<
| Total open lots             |   136 | INFO |
| Total closed lots           |  1241 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.74 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T215548Z

- UTC timestamp: `20260806T215548Z`
- GitHub run: [#6348](https://github.com/28twagg-ops/TradingBot/actions/runs/31128627715)
- Run id: `31128627715`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T17:55:52.238697-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.16},"signals":0,"placed":0,"equity":140900.1,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":138,"filled_today":167,"unattributed_contracts":7,"top_signals":[],"github_run":"6348","github_run_id":"31128627715","status":"ok"}
```

### Live bot full output

```text
21:55:49  INFO      Mode: ext_exits
21:55:50  INFO        Daily log -> logs/daily/2026-08-06.md
21:55:50  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
21:55:50  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         21:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.74|
+========================================================================+

+========================================================================+
|                       EXIT CHECK [EXTENDED HRS]                        |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  JBL  P&L +0.6%  $+0.58          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=136 paper_keys=yes dry_run=False
  alpaca positions=30
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T17:55:52.238697-04:00 ===

[Run context]
After hours (17:55 ET) — exit summary only.
Paper auth OK — equity $140900.10, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,900.10                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             136                                     |
|  Broker option positions       28                                      |
|  Unattributed contracts        7 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1323  buckets=271  win=41%                           |
|  Returns   avg=+24.2%  med=-33.3%  p10=-77.7%  p90=+137.0%             |
|  Realized  $+10,853.09                                                 |
|  Raw incl dropped  trades=1857  real=$+9,257.54                        |
|  Today     trades=107  avg=-32.8%  med=-56.5%  real=$-1,957.80         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 263 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (15)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b0   ORPHAN DKNG260807C00023000 x2 take_profit (+82.9%)               |
|  b354 S360 AMD260807C00537500 x1 stop_loss (-80.5%)                    |
|  b0   ORPHAN UBER260807C00078000 x1 stop_loss (-100.0%)                |
|  ... 10 more pending exit(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (28)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          16    -75.7%   $   -348.36               |
|  AMD260807C00537500            6    -80.5%   $   -271.80               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=0.7s reconcile=0.16s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.7s. run=#6348 https://github.com/28twagg-ops/TradingBot/actions/runs/31128627715
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 64 buckets closed trades, $-1,957.80 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-06T17:55:58.738963_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    18 | WARN | <<<
| Total open lots             |   136 | INFO |
| Total closed lots           |  1241 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.74 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T220047Z

- UTC timestamp: `20260806T220047Z`
- GitHub run: [#6349](https://github.com/28twagg-ops/TradingBot/actions/runs/31128683022)
- Run id: `31128683022`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T18:00:50.966529-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.13},"signals":0,"placed":0,"equity":140692.26,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":138,"filled_today":167,"unattributed_contracts":7,"top_signals":[],"github_run":"6349","github_run_id":"31128683022","status":"ok"}
```

### Live bot full output

```text
22:00:48  INFO      Mode: ext_exits
22:00:48  INFO        Daily log -> logs/daily/2026-08-06.md
22:00:48  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
22:00:48  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         22:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.74|
+========================================================================+

+========================================================================+
|                       EXIT CHECK [EXTENDED HRS]                        |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  JBL  P&L +0.6%  $+0.58          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=136 paper_keys=yes dry_run=False
  alpaca positions=30
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T18:00:50.966529-04:00 ===

[Run context]
After hours (18:00 ET) — exit summary only.
Paper auth OK — equity $140692.26, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,692.26                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             136                                     |
|  Broker option positions       28                                      |
|  Unattributed contracts        7 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1323  buckets=271  win=41%                           |
|  Returns   avg=+24.2%  med=-33.3%  p10=-77.7%  p90=+137.0%             |
|  Realized  $+10,853.09                                                 |
|  Raw incl dropped  trades=1857  real=$+9,257.54                        |
|  Today     trades=107  avg=-32.8%  med=-56.5%  real=$-1,957.80         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 263 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (15)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b0   ORPHAN DKNG260807C00023000 x2 take_profit (+82.9%)               |
|  b354 S360 AMD260807C00537500 x1 stop_loss (-80.5%)                    |
|  b0   ORPHAN UBER260807C00078000 x1 stop_loss (-100.0%)                |
|  ... 10 more pending exit(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (28)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          16    -75.7%   $   -348.36               |
|  AMD260807C00537500            6    -80.5%   $   -271.80               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=0.6s reconcile=0.13s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.6s. run=#6349 https://github.com/28twagg-ops/TradingBot/actions/runs/31128683022
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 64 buckets closed trades, $-1,957.80 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-06T18:00:57.254925_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    18 | WARN | <<<
| Total open lots             |   136 | INFO |
| Total closed lots           |  1241 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.74 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T220546Z

- UTC timestamp: `20260806T220546Z`
- GitHub run: [#6350](https://github.com/28twagg-ops/TradingBot/actions/runs/31128749675)
- Run id: `31128749675`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T18:05:49.881490-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.3},"signals":0,"placed":0,"equity":140734.86,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":138,"filled_today":167,"unattributed_contracts":7,"top_signals":[],"github_run":"6350","github_run_id":"31128749675","status":"ok"}
```

### Live bot full output

```text
22:05:47  INFO      Mode: ext_exits
22:05:48  INFO        Daily log -> logs/daily/2026-08-06.md
22:05:48  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
22:05:48  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         22:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.74|
+========================================================================+

+========================================================================+
|                       EXIT CHECK [EXTENDED HRS]                        |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  JBL  P&L +0.6%  $+0.58          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=136 paper_keys=yes dry_run=False
  alpaca positions=30
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T18:05:49.881490-04:00 ===

[Run context]
After hours (18:05 ET) — exit summary only.
Paper auth OK — equity $140734.86, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,734.86                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             136                                     |
|  Broker option positions       28                                      |
|  Unattributed contracts        7 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1323  buckets=271  win=41%                           |
|  Returns   avg=+24.2%  med=-33.3%  p10=-77.7%  p90=+137.0%             |
|  Realized  $+10,853.09                                                 |
|  Raw incl dropped  trades=1857  real=$+9,257.54                        |
|  Today     trades=107  avg=-32.8%  med=-56.5%  real=$-1,957.80         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 263 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (15)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b0   ORPHAN DKNG260807C00023000 x2 take_profit (+82.9%)               |
|  b354 S360 AMD260807C00537500 x1 stop_loss (-80.5%)                    |
|  b0   ORPHAN UBER260807C00078000 x1 stop_loss (-100.0%)                |
|  ... 10 more pending exit(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (28)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          16    -75.7%   $   -348.36               |
|  AMD260807C00537500            6    -80.5%   $   -271.80               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=0.7s reconcile=0.3s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.7s. run=#6350 https://github.com/28twagg-ops/TradingBot/actions/runs/31128749675
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 64 buckets closed trades, $-1,957.80 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-06T18:05:54.961538_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    18 | WARN | <<<
| Total open lots             |   136 | INFO |
| Total closed lots           |  1241 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.74 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T221048Z

- UTC timestamp: `20260806T221048Z`
- GitHub run: [#6351](https://github.com/28twagg-ops/TradingBot/actions/runs/31128806561)
- Run id: `31128806561`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T18:10:52.825494-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.16},"signals":0,"placed":0,"equity":140930.86,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":138,"filled_today":167,"unattributed_contracts":7,"top_signals":[],"github_run":"6351","github_run_id":"31128806561","status":"ok"}
```

### Live bot full output

```text
22:10:50  INFO      Mode: ext_exits
22:10:50  INFO        Daily log -> logs/daily/2026-08-06.md
22:10:50  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
22:10:50  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         22:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.74|
+========================================================================+

+========================================================================+
|                       EXIT CHECK [EXTENDED HRS]                        |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  JBL  P&L +0.6%  $+0.58          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=136 paper_keys=yes dry_run=False
  alpaca positions=30
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T18:10:52.825494-04:00 ===

[Run context]
After hours (18:10 ET) — exit summary only.
Paper auth OK — equity $140930.86, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,930.86                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             136                                     |
|  Broker option positions       28                                      |
|  Unattributed contracts        7 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1323  buckets=271  win=41%                           |
|  Returns   avg=+24.2%  med=-33.3%  p10=-77.7%  p90=+137.0%             |
|  Realized  $+10,853.09                                                 |
|  Raw incl dropped  trades=1857  real=$+9,257.54                        |
|  Today     trades=107  avg=-32.8%  med=-56.5%  real=$-1,957.80         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 263 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (15)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b0   ORPHAN DKNG260807C00023000 x2 take_profit (+82.9%)               |
|  b354 S360 AMD260807C00537500 x1 stop_loss (-80.5%)                    |
|  b0   ORPHAN UBER260807C00078000 x1 stop_loss (-100.0%)                |
|  ... 10 more pending exit(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (28)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          16    -75.7%   $   -348.36               |
|  AMD260807C00537500            6    -80.5%   $   -271.80               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=0.6s reconcile=0.16s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.6s. run=#6351 https://github.com/28twagg-ops/TradingBot/actions/runs/31128806561
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 64 buckets closed trades, $-1,957.80 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-06T18:10:58.992198_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    18 | WARN | <<<
| Total open lots             |   136 | INFO |
| Total closed lots           |  1241 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.74 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260806T221547Z

- UTC timestamp: `20260806T221547Z`
- GitHub run: [#6352](https://github.com/28twagg-ops/TradingBot/actions/runs/31128865541)
- Run id: `31128865541`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T18:15:52.397957-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.5,"phases_s":{"reconcile":0.64},"signals":0,"placed":0,"equity":141142.86,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":138,"filled_today":167,"unattributed_contracts":7,"top_signals":[],"github_run":"6352","github_run_id":"31128865541","status":"ok"}
```

### Live bot full output

```text
22:15:48  INFO      Mode: ext_exits
22:15:49  INFO        Daily log -> logs/daily/2026-08-06.md
22:15:49  INFO        Daily log reconciled -> logs/daily/2026-08-06.md (5 ledger rows)
22:15:49  INFO        Daily log -> logs/daily/2026-08-06.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                         EXT_EXITS|
|  Time                                                         22:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.74|
+========================================================================+

+========================================================================+
|                       EXIT CHECK [EXTENDED HRS]                        |
+========================================================================+
|  Exit log~  stop-0.5% / 3d max  (midline skipped — close already final)|
+------------------------------------------------------------------------+
|  JBL  P&L +0.6%  $+0.58          HOLDING until 9:35am scan (Pullback50)|
+========================================================================+

+========================================================================+
|                          EXTENDED HOURS SELLS                          |
+========================================================================+
|                                                                        |
|  No extended-hours sells this run.                                     |
|                                                                        |
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                         ext_exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                1|
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
  open_lots=136 paper_keys=yes dry_run=False
  alpaca positions=30
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-06T18:15:52.397957-04:00 ===

[Run context]
After hours (18:15 ET) — exit summary only.
Paper auth OK — equity $141142.86, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $141,142.86                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    138                                     |
|  Orders filled today (ledger)  167                                     |
|  Entries placed this run       0                                       |
|  Open virtual lots             136                                     |
|  Broker option positions       28                                      |
|  Unattributed contracts        7 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1323  buckets=271  win=41%                           |
|  Returns   avg=+24.2%  med=-33.3%  p10=-77.7%  p90=+137.0%             |
|  Realized  $+10,853.09                                                 |
|  Raw incl dropped  trades=1857  real=$+9,257.54                        |
|  Today     trades=107  avg=-32.8%  med=-56.5%  real=$-1,957.80         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b197 lab0197_s218_w3_10  3 100% +368.0 +318.8 +737.5 $   +253         |
|  b238 lab0238_s401_w3_10  8 100% +274.1 +273.1 +815.4 $   +832         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  ... 263 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (15)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b0   ORPHAN DKNG260807C00023000 x2 take_profit (+82.9%)               |
|  b354 S360 AMD260807C00537500 x1 stop_loss (-80.5%)                    |
|  b0   ORPHAN UBER260807C00078000 x1 stop_loss (-100.0%)                |
|  ... 10 more pending exit(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (28)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  COIN260807C00160000          16    -75.7%   $   -348.36               |
|  AMD260807C00537500            6    -80.5%   $   -271.80               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-06.log
elapsed=1.5s reconcile=0.64s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.5s. run=#6352 https://github.com/28twagg-ops/TradingBot/actions/runs/31128865541
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_buckets.csv
Summary: 64 buckets closed trades, $-1,957.80 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-06_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-06T18:15:59.430255_

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
## Ledger health — 2026-08-06
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    18 | WARN | <<<
| Total open lots             |   136 | INFO |
| Total closed lots           |  1241 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=470.74 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
