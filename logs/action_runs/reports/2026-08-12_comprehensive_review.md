# Daily Comprehensive Action Review — 2026-08-12

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260812T010650Z

- UTC timestamp: `20260812T010650Z`
- GitHub run: [#6816](https://github.com/28twagg-ops/TradingBot/actions/runs/31552479512)
- Run id: `31552479512`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T21:06:55.301884-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":133019.1,"open_positions":22,"pending_orders":0,"open_lots":108,"submitted_today":56,"filled_today":44,"unattributed_contracts":4,"top_signals":[],"github_run":"6816","github_run_id":"31552479512","status":"ok"}
```

### Live bot full output

```text
01:06:51  INFO      Mode: summary
01:06:52  INFO        Daily log -> logs/daily/2026-08-12.md
01:06:52  INFO        Daily log reconciled -> logs/daily/2026-08-12.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $465.92|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $465.92|
|  Cash                                                           $116.46|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $349.46|
|  Open P&L                                                        $-0.13|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ADM      Pullback50      $93.22     $80.46   $80.46   +0.0%   $+0.00  |
|  AES      Pullback50      $93.96     $14.72   $14.70   -0.1%   $-0.13  |
|  AXP      Pullback50      $93.19     $340.66  $340.55  -0.0%   $-0.03  |
|  EXR      Pullback50      $69.08     $146.51  $146.55  +0.0%   $+0.02  |
|                                                                        |
|  Total invested                                                 $349.46|
|  Total open P&L                                                  $-0.13|
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
|  2026-08-11  SELL  DHI  Pullback50  $93.11  P&L $-0.11                 |
|  2026-08-11  SELL  AFL  Pullback50  $93.04  P&L $-0.50                 |
|  2026-08-11  SELL  AIG  Pullback50  $68.71  P&L $-0.41                 |
|  2026-08-11  SELL  ALGN  Pullback50  $93.39  P&L $+0.00                |
|  2026-08-11  SELL  ADM  Pullback50  $13.59  P&L $-0.08                 |
|  2026-08-11  SELL  AAPL  Pullback50  $93.61  P&L $-0.54                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=108 paper_keys=yes dry_run=False
  alpaca positions=24
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T21:06:55.301884-04:00 ===

[Run context]
After hours (21:06 ET) — exit summary only.
Paper auth OK — equity $133019.10, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,019.10                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    56                                      |
|  Orders filled today (ledger)  44                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             108                                     |
|  Broker option positions       22                                      |
|  Unattributed contracts        4 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1877  buckets=316  win=36%                           |
|  Returns   avg=+13.1%  med=-42.9%  p10=-82.6%  p90=+125.0%             |
|  Realized  $+2,776.81                                                  |
|  Raw incl dropped  trades=2411  real=$+1,181.26                        |
|  Today     trades=65  avg=-34.0%  med=-53.9%  real=$-1,055.91          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b834 lab0834_s406_w4_11  4 100% +593.6 +598.5 +1133.3 $    +93        |
|  b383 lab0383_s362_w4_11  2  50% +581.3 +581.3 +1222.6 $   +337        |
|  b382 lab0382_s362_w4_11  2  50% +533.6 +533.6 +1125.8 $   +308        |
|  b860 lab0860_s408_w3_10  8  62% +552.8 +493.9 +1446.7 $   +818        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  ... 308 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b79  lab0079_s209_w4_11  1   0% -94.6 -94.6 -94.6 $    -53       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (10)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN RBLX260814C00041000 x1 stop_loss (-95.5%)                 |
|  b844 S407 AAPL260812C00320000 x1 stop_loss (-90.9%)                   |
|  b820 S405 AAPL260812C00312500 x1 stop_loss (-89.4%)                   |
|  b0   ORPHAN META260814C00657500 x2 stop_loss (-87.0%)                 |
|  b390 S363 AAPL260814C00317500 x1 stop_loss (-73.8%)                   |
|  ... 5 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (22)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260812C00315000          38    -95.3%   $ -1,530.00               |
|  AAPL260814C00317500          21    -73.8%   $   -947.74               |
|  AAPL260817C00320000           7    -74.5%   $   -326.85               |
|  AAPL260812C00312500           4    -89.4%   $   -235.33               |
|  AAPL260812C00317500          10    -95.5%   $   -212.00               |
|  CELH260814C00028000           6   +117.5%   $   +181.50               |
|  NFLX260814C00079000           6    -74.1%   $   -120.00               |
|  META260814C00657500           2    -87.0%   $    -94.00               |
|  ... 14 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-11.log
elapsed=1.3s reconcile=0.6s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.3s. run=#6816 https://github.com/28twagg-ops/TradingBot/actions/runs/31552479512
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.csv
Summary: 49 buckets closed trades, $-1,055.91 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 12.1% (292/2411) ALERT
# Options signal frequency

_Generated 2026-08-11T21:07:02.462341_

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
## Ledger health — 2026-08-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN | <<<
| Missing exit records (post) |   591 | WARN | <<<
| State/ledger mismatches     |    13 | WARN | <<<
| Total open lots             |   108 | INFO |
| Total closed lots           |  1652 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=465.92 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260812T010911Z

- UTC timestamp: `20260812T010911Z`
- GitHub run: [#6817](https://github.com/28twagg-ops/TradingBot/actions/runs/31552613788)
- Run id: `31552613788`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`11s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T21:09:18.589841-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.14},"signals":0,"placed":0,"equity":133019.1,"open_positions":22,"pending_orders":0,"open_lots":108,"submitted_today":56,"filled_today":44,"unattributed_contracts":4,"top_signals":[],"github_run":"6817","github_run_id":"31552613788","status":"ok"}
```

### Live bot full output

```text
01:09:14  INFO      Mode: summary
01:09:15  INFO        Daily log -> logs/daily/2026-08-12.md
01:09:15  INFO        Daily log reconciled -> logs/daily/2026-08-12.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:09 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $465.92|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $465.92|
|  Cash                                                           $116.46|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $349.46|
|  Open P&L                                                        $-0.13|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ADM      Pullback50      $93.22     $80.46   $80.46   +0.0%   $+0.00  |
|  AES      Pullback50      $93.96     $14.72   $14.70   -0.1%   $-0.13  |
|  AXP      Pullback50      $93.19     $340.66  $340.55  -0.0%   $-0.03  |
|  EXR      Pullback50      $69.08     $146.51  $146.55  +0.0%   $+0.02  |
|                                                                        |
|  Total invested                                                 $349.46|
|  Total open P&L                                                  $-0.13|
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
|  2026-08-11  SELL  DHI  Pullback50  $93.11  P&L $-0.11                 |
|  2026-08-11  SELL  AFL  Pullback50  $93.04  P&L $-0.50                 |
|  2026-08-11  SELL  AIG  Pullback50  $68.71  P&L $-0.41                 |
|  2026-08-11  SELL  ALGN  Pullback50  $93.39  P&L $+0.00                |
|  2026-08-11  SELL  ADM  Pullback50  $13.59  P&L $-0.08                 |
|  2026-08-11  SELL  AAPL  Pullback50  $93.61  P&L $-0.54                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=108 paper_keys=yes dry_run=False
  alpaca positions=24
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T21:09:18.589841-04:00 ===

[Run context]
After hours (21:09 ET) — exit summary only.
Paper auth OK — equity $133019.10, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,019.10                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    56                                      |
|  Orders filled today (ledger)  44                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             108                                     |
|  Broker option positions       22                                      |
|  Unattributed contracts        4 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1877  buckets=316  win=36%                           |
|  Returns   avg=+13.1%  med=-42.9%  p10=-82.6%  p90=+125.0%             |
|  Realized  $+2,776.81                                                  |
|  Raw incl dropped  trades=2411  real=$+1,181.26                        |
|  Today     trades=65  avg=-34.0%  med=-53.9%  real=$-1,055.91          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b834 lab0834_s406_w4_11  4 100% +593.6 +598.5 +1133.3 $    +93        |
|  b383 lab0383_s362_w4_11  2  50% +581.3 +581.3 +1222.6 $   +337        |
|  b382 lab0382_s362_w4_11  2  50% +533.6 +533.6 +1125.8 $   +308        |
|  b860 lab0860_s408_w3_10  8  62% +552.8 +493.9 +1446.7 $   +818        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  ... 308 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b79  lab0079_s209_w4_11  1   0% -94.6 -94.6 -94.6 $    -53       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (10)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN RBLX260814C00041000 x1 stop_loss (-95.5%)                 |
|  b844 S407 AAPL260812C00320000 x1 stop_loss (-90.9%)                   |
|  b820 S405 AAPL260812C00312500 x1 stop_loss (-89.4%)                   |
|  b0   ORPHAN META260814C00657500 x2 stop_loss (-87.0%)                 |
|  b390 S363 AAPL260814C00317500 x1 stop_loss (-73.8%)                   |
|  ... 5 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (22)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260812C00315000          38    -95.3%   $ -1,530.00               |
|  AAPL260814C00317500          21    -73.8%   $   -947.74               |
|  AAPL260817C00320000           7    -74.5%   $   -326.85               |
|  AAPL260812C00312500           4    -89.4%   $   -235.33               |
|  AAPL260812C00317500          10    -95.5%   $   -212.00               |
|  CELH260814C00028000           6   +117.5%   $   +181.50               |
|  NFLX260814C00079000           6    -74.1%   $   -120.00               |
|  META260814C00657500           2    -87.0%   $    -94.00               |
|  ... 14 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-11.log
elapsed=0.7s reconcile=0.14s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.7s. run=#6817 https://github.com/28twagg-ops/TradingBot/actions/runs/31552613788
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.csv
Summary: 49 buckets closed trades, $-1,055.91 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 12.1% (292/2411) ALERT
# Options signal frequency

_Generated 2026-08-11T21:09:25.216531_

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
## Ledger health — 2026-08-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN | <<<
| Missing exit records (post) |   591 | WARN | <<<
| State/ledger mismatches     |    13 | WARN | <<<
| Total open lots             |   108 | INFO |
| Total closed lots           |  1652 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=465.92 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260812T032930Z

- UTC timestamp: `20260812T032930Z`
- GitHub run: [#6818](https://github.com/28twagg-ops/TradingBot/actions/runs/31560184906)
- Run id: `31560184906`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-11T23:29:35.383635-04:00","date":"2026-08-11","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":133083.1,"open_positions":22,"pending_orders":0,"open_lots":108,"submitted_today":56,"filled_today":44,"unattributed_contracts":4,"top_signals":[],"github_run":"6818","github_run_id":"31560184906","status":"ok"}
```

### Live bot full output

```text
03:29:31  INFO      Mode: summary
03:29:33  INFO        Daily log -> logs/daily/2026-08-12.md
03:29:33  INFO        Daily log reconciled -> logs/daily/2026-08-12.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         03:29 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.11|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $466.11|
|  Cash                                                           $116.46|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $349.65|
|  Open P&L                                                        $+0.06|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ADM      Pullback50      $93.22     $80.46   $80.46   +0.0%   $+0.00  |
|  AES      Pullback50      $93.96     $14.72   $14.70   -0.1%   $-0.13  |
|  AXP      Pullback50      $93.38     $340.66  $341.25  +0.2%   $+0.16  |
|  EXR      Pullback50      $69.08     $146.51  $146.55  +0.0%   $+0.02  |
|                                                                        |
|  Total invested                                                 $349.65|
|  Total open P&L                                                  $+0.06|
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
|  2026-08-11  SELL  DHI  Pullback50  $93.11  P&L $-0.11                 |
|  2026-08-11  SELL  AFL  Pullback50  $93.04  P&L $-0.50                 |
|  2026-08-11  SELL  AIG  Pullback50  $68.71  P&L $-0.41                 |
|  2026-08-11  SELL  ALGN  Pullback50  $93.39  P&L $+0.00                |
|  2026-08-11  SELL  ADM  Pullback50  $13.59  P&L $-0.08                 |
|  2026-08-11  SELL  AAPL  Pullback50  $93.61  P&L $-0.54                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=108 paper_keys=yes dry_run=False
  alpaca positions=24
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-11T23:29:35.383635-04:00 ===

[Run context]
After hours (23:29 ET) — exit summary only.
Paper auth OK — equity $133083.10, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,083.10                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    56                                      |
|  Orders filled today (ledger)  44                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             108                                     |
|  Broker option positions       22                                      |
|  Unattributed contracts        4 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1877  buckets=316  win=36%                           |
|  Returns   avg=+13.1%  med=-42.9%  p10=-82.6%  p90=+125.0%             |
|  Realized  $+2,776.81                                                  |
|  Raw incl dropped  trades=2411  real=$+1,181.26                        |
|  Today     trades=65  avg=-34.0%  med=-53.9%  real=$-1,055.91          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b834 lab0834_s406_w4_11  4 100% +593.6 +598.5 +1133.3 $    +93        |
|  b383 lab0383_s362_w4_11  2  50% +581.3 +581.3 +1222.6 $   +337        |
|  b382 lab0382_s362_w4_11  2  50% +533.6 +533.6 +1125.8 $   +308        |
|  b860 lab0860_s408_w3_10  8  62% +552.8 +493.9 +1446.7 $   +818        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  lab0091_s210_w6_14  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b281 lab0281_s351_w1_09  5  60% +156.4 +197.9 +346.9 $   +296         |
|  ... 308 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b79  lab0079_s209_w4_11  1   0% -94.6 -94.6 -94.6 $    -53       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (10)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN RBLX260814C00041000 x1 stop_loss (-95.5%)                 |
|  b844 S407 AAPL260812C00320000 x1 stop_loss (-90.9%)                   |
|  b820 S405 AAPL260812C00312500 x1 stop_loss (-89.4%)                   |
|  b0   ORPHAN META260814C00657500 x2 stop_loss (-87.0%)                 |
|  b390 S363 AAPL260814C00317500 x1 stop_loss (-73.8%)                   |
|  ... 5 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (22)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AAPL260812C00315000          38    -95.3%   $ -1,530.00               |
|  AAPL260814C00317500          21    -73.8%   $   -947.74               |
|  AAPL260817C00320000           7    -74.5%   $   -326.85               |
|  AAPL260812C00312500           4    -89.4%   $   -235.33               |
|  AAPL260812C00317500          10    -95.5%   $   -212.00               |
|  CELH260814C00028000           6   +117.5%   $   +181.50               |
|  NFLX260814C00079000           6    -74.1%   $   -120.00               |
|  META260814C00657500           2    -87.0%   $    -94.00               |
|  ... 14 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-11.log
elapsed=1.3s reconcile=0.6s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.3s. run=#6818 https://github.com/28twagg-ops/TradingBot/actions/runs/31560184906
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_buckets.csv
Summary: 49 buckets closed trades, $-1,055.91 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-11_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 12.1% (292/2411) ALERT
# Options signal frequency

_Generated 2026-08-11T23:29:42.481759_

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
## Ledger health — 2026-08-11
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   591 | WARN | <<<
| Missing exit records (post) |   591 | WARN | <<<
| State/ledger mismatches     |    13 | WARN | <<<
| Total open lots             |   108 | INFO |
| Total closed lots           |  1652 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.11 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260812T130051Z

- UTC timestamp: `20260812T130051Z`
- GitHub run: [#6819](https://github.com/28twagg-ops/TradingBot/actions/runs/31599192510)
- Run id: `31599192510`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`12s`

### Options data quality (CLEAN vs TAINTED vs KEEP-only)

| Slice | n | Win% | Med% | Avg% | $ |
|---|---:|---:|---:|---:|---:|
| CLEAN | 738 | 43.9 | -45.3 | +16.0 | $+9,446 |
| TAINTED | 1673 | 33.1 | -39.3 | +9.9 | $-8,265 |
| KEEP-only | 302 | 63.9 | +37.7 | +42.0 | $+5,709 |
| KEEP-only recent | 114 | 60.5 | +50.0 | +51.5 | $+1,683 |

- KEEP strategies (12): S173, S174, S210, S218, S350, S364, S397, S398, S401, S403, S404, S406
- KILL strategies (12): ORPHAN, S165, S207, S211, S212, S217, S351, S354, S355, S360, S405, S408
- Note: KILL/KEEP are advisory - all strategies still trade for ~1 week observation.
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-12T09:00:55.925551-04:00","date":"2026-08-12","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.31},"signals":0,"placed":0,"equity":136324.29,"open_positions":22,"pending_orders":0,"open_lots":108,"submitted_today":0,"filled_today":0,"unattributed_contracts":4,"top_signals":[],"github_run":"6819","github_run_id":"31599192510","status":"ok","data_quality":{"clean":{"n":738,"win":43.9,"med":-45.34,"avg":15.95,"pnl":9445.88},"tainted":{"n":1673,"win":33.11,"med":-39.29,"avg":9.95,"pnl":-8264.62},"keep_only":{"n":302,"win":63.91,"med":37.69,"avg":41.99,"pnl":5709.45},"keep_only_recent":{"n":114,"win":60.53,"med":50.0,"avg":51.55,"pnl":1683.0},"keep_strategies":["S173","S174","S210","S218","S350","S364","S397","S398","S401","S403","S404","S406"],"kill_strategies":["ORPHAN","S165","S207","S211","S212","S217","S351","S354","S355","S360","S405","S408"]}}
```

### Live bot full output

```text
13:00:52  INFO      Mode: summary
13:00:53  INFO        Daily log -> logs/daily/2026-08-12.md
13:00:53  INFO        Daily log reconciled -> logs/daily/2026-08-12.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $466.35|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $466.35|
|  Cash                                                           $116.46|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $349.89|
|  Open P&L                                                        $+0.30|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (4 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ADM      Pullback50      $93.55     $80.46   $80.74   +0.4%   $+0.33  |
|  AES      Pullback50      $94.09     $14.72   $14.72   -0.0%   $-0.00  |
|  AXP      Pullback50      $93.18     $340.66  $340.50  -0.0%   $-0.04  |
|  EXR      Pullback50      $69.08     $146.51  $146.55  +0.0%   $+0.02  |
|                                                                        |
|  Total invested                                                 $349.89|
|  Total open P&L                                                  $+0.30|
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
|  2026-08-11  SELL  DHI  Pullback50  $93.11  P&L $-0.11                 |
|  2026-08-11  SELL  AFL  Pullback50  $93.04  P&L $-0.50                 |
|  2026-08-11  SELL  AIG  Pullback50  $68.71  P&L $-0.41                 |
|  2026-08-11  SELL  ALGN  Pullback50  $93.39  P&L $+0.00                |
|  2026-08-11  SELL  ADM  Pullback50  $13.59  P&L $-0.08                 |
|  2026-08-11  SELL  AAPL  Pullback50  $93.61  P&L $-0.54                |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=108 paper_keys=yes dry_run=False
  alpaca positions=24
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-12T09:00:55.925551-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $136324.29, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|[OPTIONS BOT DAILY VITALS (MATRIX EXPERIMENT)]                          |
+========================================================================+
|-- ACCOUNT STATUS (after_hours) --                                      |
|Equity       : $136,324.29                                              |
|Open Risk    : 108 lots (22 broker pos)                                 |
|Today's Run  : 0 signals -> 0 orders submitted                          |
|                                                                        |
|-- SYSTEM HEALTH --                                                     |
|Zombies      : 4 WARN: See reconcile                                    |
|Lab Status   : 108 Active Lots | 0 Pending Orders                       |
|Auto-Matrix  : (Pending EOD report generation)                          |
+========================================================================+
+========================================================================+
|[DATA QUALITY: CLEAN vs ERRORS vs KEEP-ONLY]                            |
+========================================================================+
|  CLEAN              n=738   win= 43.9%  med= -45.3%  $+9,446           |
|  TAINTED            n=1673  win= 33.1%  med= -39.3%  $-8,265           |
|  KEEP-only          n=302   win= 63.9%  med= +37.7%  $+5,709           |
|  KEEP recent        n=114   win= 60.5%  med= +50.0%  $+1,683           |
|  KEEP(12): S173,S174,S210,S218,S350,S364,S397,S398...                  |
|  KILL(12): ORPHAN,S165,S207,S211,S212,S217,S351,S354...                |
+========================================================================+
+========================================================================+
|[+++ OVERPERFORMING STRATEGIES (n>=10)]                                 |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b832 lab0832_s406_w3_1045..  80%  +138.5%    10                       |
|  b238 lab0238_s401_w3_1045..  79%  +107.1%    14                       |
|  b861 lab0861_s408_w3_1045..  73%  +100.0%    11                       |
|  b365 lab0365_s361_w2_1005..  90%  +82.8%    10                        |
+========================================================================+
|[--- UNDERPERFORMING STRATEGIES (n>=10)]                                |
+========================================================================+
|  BKT  PROFILE                   WIN%   MED%   TOTAL TRADES             |
|  ---------------------------------------------------------             |
|  b84  lab0084_s210_w3_1045..  45%  -81.2%    11                        |
|  b47  lab0047_s205_w4_1120..   4%  -78.0%    28                        |
|  b114 lab0114_s212_w4_1120..   0%  -73.5%    11                        |
|  b113 lab0113_s212_w3_1045..   7%  -71.9%    14                        |
+========================================================================+
+========================================================================+
|[PENDING EXITS (10)]                                                    |
+========================================================================+
|  b0   ORPHAN RBLX260814C00041000 x1 stop_loss (-95.5%)                 |
|  b844 S407 AAPL260812C00320000 x1 stop_loss (-90.9%)                   |
|  b820 S405 AAPL260812C00312500 x1 stop_loss (-89.4%)                   |
|  b0   ORPHAN META260814C00657500 x2 stop_loss (-87.0%)                 |
|  b390 S363 AAPL260814C00317500 x1 stop_loss (-73.8%)                   |
|  ... 5 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|[OPEN OPTIONS (22)]                                                     |
+========================================================================+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|  ---------------------------------------------------------             |
|  AAPL260812C00315000          38    -95.3%   $ -1,530.00               |
|  AAPL260814C00317500          21    -73.8%   $   -947.74               |
|  AAPL260817C00320000           7    -74.5%   $   -326.85               |
|  AAPL260812C00312500           4    -89.4%   $   -235.33               |
|  AAPL260812C00317500          10    -95.5%   $   -212.00               |
|  CELH260814C00028000           6   +117.5%   $   +181.50               |
|  NFLX260814C00079000           6    -74.1%   $   -120.00               |
|  META260814C00657500           2    -87.0%   $    -94.00               |
|  ... 14 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-12.log
elapsed=1.2s reconcile=0.31s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.2s. run=#6819 https://github.com/28twagg-ops/TradingBot/actions/runs/31599192510
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-12_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-12_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-12_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-12_strategy_selection.csv
Summary: keep=0 watch=80 drop=25
Orphan rate: 12.1% (292/2411) ALERT
# Options signal frequency

_Generated 2026-08-12T09:01:03.009854_

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
## Ledger health — 2026-08-12
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   650 | WARN | <<<
| Missing exit records (post) |   650 | WARN | <<<
| State/ledger mismatches     |    13 | WARN | <<<
| Total open lots             |   108 | INFO |
| Total closed lots           |  1652 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-12_data_quality.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-12_data_quality.csv
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality.json
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/latest_data_quality_snippet.md
CLEAN n=738 med=-45.3% | TAINTED n=1673 med=-39.3% | KEEP-only n=302 med=+37.7% | KILL=12 KEEP=12
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=466.35 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
