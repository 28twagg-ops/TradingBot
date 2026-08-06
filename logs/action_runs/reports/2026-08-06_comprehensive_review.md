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
