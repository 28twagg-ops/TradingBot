# Daily Comprehensive Action Review — 2026-08-07

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260807T001202Z

- UTC timestamp: `20260807T001202Z`
- GitHub run: [#6373](https://github.com/28twagg-ops/TradingBot/actions/runs/31133752988)
- Run id: `31133752988`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T20:12:06.185917-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.6,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":141498.86,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":138,"filled_today":167,"unattributed_contracts":7,"top_signals":[],"github_run":"6373","github_run_id":"31133752988","status":"ok"}
```

### Live bot full output

```text
00:12:03  INFO      Mode: summary
00:12:04  INFO        Daily log -> logs/daily/2026-08-07.md
00:12:04  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         00:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.74|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $470.74|
|  Cash                                                           $375.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $94.76|
|  Open P&L                                                        $+0.58|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  JBL      Pullback50      $94.76     $342.57  $344.67  +0.6%   $+0.58  |
|                                                                        |
|  Total invested                                                  $94.76|
|  Total open P&L                                                  $+0.58|
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
|  2026-08-06  SELL  GEV  Pullback50  $93.51  P&L $-0.67                 |
|  2026-08-06  SELL  GS  Pullback50  $94.20  P&L $+0.13                  |
|  2026-08-06  SELL  DOV  Pullback50  $93.98  P&L $-0.11                 |
|  2026-08-06  SELL  AVB  Pullback50  $94.61  P&L $+1.05                 |
|  2026-08-06  SELL  AES  Pullback50  $93.56  P&L $-0.10                 |
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
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
=== options_morning_bot (PAPER) 2026-08-06T20:12:06.185917-04:00 ===

[Run context]
After hours (20:12 ET) — exit summary only.
Paper auth OK — equity $141498.86, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $141,498.86                             |
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
elapsed=0.6s reconcile=0.11s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.6s. run=#6373 https://github.com/28twagg-ops/TradingBot/actions/runs/31133752988
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

_Generated 2026-08-06T20:12:12.285946_

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

## Run 20260807T021018Z

- UTC timestamp: `20260807T021018Z`
- GitHub run: [#6374](https://github.com/28twagg-ops/TradingBot/actions/runs/31140342156)
- Run id: `31140342156`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-06T22:10:21.716020-04:00","date":"2026-08-06","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.2,"phases_s":{"reconcile":0.51},"signals":0,"placed":0,"equity":141058.86,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":138,"filled_today":167,"unattributed_contracts":7,"top_signals":[],"github_run":"6374","github_run_id":"31140342156","status":"ok"}
```

### Live bot full output

```text
02:10:19  INFO      Mode: summary
02:10:19  INFO        Daily log -> logs/daily/2026-08-07.md
02:10:19  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         02:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.74|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $470.74|
|  Cash                                                           $375.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $94.76|
|  Open P&L                                                        $+0.58|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  JBL      Pullback50      $94.76     $342.57  $344.67  +0.6%   $+0.58  |
|                                                                        |
|  Total invested                                                  $94.76|
|  Total open P&L                                                  $+0.58|
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
|  2026-08-06  SELL  GEV  Pullback50  $93.51  P&L $-0.67                 |
|  2026-08-06  SELL  GS  Pullback50  $94.20  P&L $+0.13                  |
|  2026-08-06  SELL  DOV  Pullback50  $93.98  P&L $-0.11                 |
|  2026-08-06  SELL  AVB  Pullback50  $94.61  P&L $+1.05                 |
|  2026-08-06  SELL  AES  Pullback50  $93.56  P&L $-0.10                 |
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
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
=== options_morning_bot (PAPER) 2026-08-06T22:10:21.716020-04:00 ===

[Run context]
After hours (22:10 ET) — exit summary only.
Paper auth OK — equity $141058.86, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
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
elapsed=1.2s reconcile=0.51s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.2s. run=#6374 https://github.com/28twagg-ops/TradingBot/actions/runs/31140342156
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

_Generated 2026-08-06T22:10:26.261084_

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

## Run 20260807T043220Z

- UTC timestamp: `20260807T043220Z`
- GitHub run: [#6375](https://github.com/28twagg-ops/TradingBot/actions/runs/31147686732)
- Run id: `31147686732`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T00:32:25.195193-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.6,"phases_s":{"reconcile":0.66},"signals":0,"placed":0,"equity":140974.86,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":0,"filled_today":0,"unattributed_contracts":7,"top_signals":[],"github_run":"6375","github_run_id":"31147686732","status":"ok"}
```

### Live bot full output

```text
04:32:21  INFO      Mode: summary
04:32:22  INFO        Daily log -> logs/daily/2026-08-07.md
04:32:22  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         04:32 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $470.74|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $470.74|
|  Cash                                                           $375.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $94.76|
|  Open P&L                                                        $+0.58|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  JBL      Pullback50      $94.76     $342.57  $344.67  +0.6%   $+0.58  |
|                                                                        |
|  Total invested                                                  $94.76|
|  Total open P&L                                                  $+0.58|
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
|  2026-08-06  SELL  GEV  Pullback50  $93.51  P&L $-0.67                 |
|  2026-08-06  SELL  GS  Pullback50  $94.20  P&L $+0.13                  |
|  2026-08-06  SELL  DOV  Pullback50  $93.98  P&L $-0.11                 |
|  2026-08-06  SELL  AVB  Pullback50  $94.61  P&L $+1.05                 |
|  2026-08-06  SELL  AES  Pullback50  $93.56  P&L $-0.10                 |
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
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
=== options_morning_bot (PAPER) 2026-08-07T00:32:25.195193-04:00 ===

[Run context]
After hours (00:32 ET) — exit summary only.
Paper auth OK — equity $140974.86, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $140,974.86                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=1.6s reconcile=0.66s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.6s. run=#6375 https://github.com/28twagg-ops/TradingBot/actions/runs/31147686732
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-07T00:32:32.428958_

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
## Ledger health — 2026-08-07
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

## Run 20260807T130131Z

- UTC timestamp: `20260807T130131Z`
- GitHub run: [#6376](https://github.com/28twagg-ops/TradingBot/actions/runs/31180620236)
- Run id: `31180620236`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T09:01:36.107991-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.64},"signals":0,"placed":0,"equity":143853.71,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":0,"filled_today":0,"unattributed_contracts":7,"top_signals":[],"github_run":"6376","github_run_id":"31180620236","status":"ok"}
```

### Live bot full output

```text
13:01:32  INFO      Mode: summary
13:01:33  INFO        Daily log -> logs/daily/2026-08-07.md
13:01:33  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.99|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $472.99|
|  Cash                                                           $375.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $97.01|
|  Open P&L                                                        $+2.83|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  JBL      Pullback50      $97.01     $342.57  $352.88  +3.0%   $+2.83  |
|                                                                        |
|  Total invested                                                  $97.01|
|  Total open P&L                                                  $+2.83|
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
|  2026-08-06  SELL  GEV  Pullback50  $93.51  P&L $-0.67                 |
|  2026-08-06  SELL  GS  Pullback50  $94.20  P&L $+0.13                  |
|  2026-08-06  SELL  DOV  Pullback50  $93.98  P&L $-0.11                 |
|  2026-08-06  SELL  AVB  Pullback50  $94.61  P&L $+1.05                 |
|  2026-08-06  SELL  AES  Pullback50  $93.56  P&L $-0.10                 |
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
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
=== options_morning_bot (PAPER) 2026-08-07T09:01:36.107991-04:00 ===

[Run context]
After hours (09:01 ET) — exit summary only.
Paper auth OK — equity $143853.71, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,853.71                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
|  AMD260807C00537500            6    -80.8%   $   -277.64               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=1.3s reconcile=0.64s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.3s. run=#6376 https://github.com/28twagg-ops/TradingBot/actions/runs/31180620236
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-07T09:01:43.128850_

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
## Ledger health — 2026-08-07
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
equity=472.99 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T130401Z

- UTC timestamp: `20260807T130401Z`
- GitHub run: [#6377](https://github.com/28twagg-ops/TradingBot/actions/runs/31180813932)
- Run id: `31180813932`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T09:04:05.532825-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.17},"signals":0,"placed":0,"equity":143753.71,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":0,"filled_today":0,"unattributed_contracts":7,"top_signals":[],"github_run":"6377","github_run_id":"31180813932","status":"ok"}
```

### Live bot full output

```text
13:04:03  INFO      Mode: summary
13:04:03  INFO        Daily log -> logs/daily/2026-08-07.md
13:04:03  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:04 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.99|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $472.99|
|  Cash                                                           $375.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $97.01|
|  Open P&L                                                        $+2.83|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  JBL      Pullback50      $97.01     $342.57  $352.88  +3.0%   $+2.83  |
|                                                                        |
|  Total invested                                                  $97.01|
|  Total open P&L                                                  $+2.83|
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
|  2026-08-06  SELL  GEV  Pullback50  $93.51  P&L $-0.67                 |
|  2026-08-06  SELL  GS  Pullback50  $94.20  P&L $+0.13                  |
|  2026-08-06  SELL  DOV  Pullback50  $93.98  P&L $-0.11                 |
|  2026-08-06  SELL  AVB  Pullback50  $94.61  P&L $+1.05                 |
|  2026-08-06  SELL  AES  Pullback50  $93.56  P&L $-0.10                 |
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
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
=== options_morning_bot (PAPER) 2026-08-07T09:04:05.532825-04:00 ===

[Run context]
After hours (09:04 ET) — exit summary only.
Paper auth OK — equity $143753.71, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,753.71                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
|  AMD260807C00537500            6    -80.8%   $   -277.64               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=0.7s reconcile=0.17s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.7s. run=#6377 https://github.com/28twagg-ops/TradingBot/actions/runs/31180813932
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-07T09:04:12.165540_

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
## Ledger health — 2026-08-07
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
equity=472.99 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T130543Z

- UTC timestamp: `20260807T130543Z`
- GitHub run: [#6378](https://github.com/28twagg-ops/TradingBot/actions/runs/31181002814)
- Run id: `31181002814`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T09:05:47.808084-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":143845.71,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":0,"filled_today":0,"unattributed_contracts":7,"top_signals":[],"github_run":"6378","github_run_id":"31181002814","status":"ok"}
```

### Live bot full output

```text
13:05:45  INFO      Mode: summary
13:05:45  INFO        Daily log -> logs/daily/2026-08-07.md
13:05:45  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.99|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $472.99|
|  Cash                                                           $375.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $97.01|
|  Open P&L                                                        $+2.83|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  JBL      Pullback50      $97.01     $342.57  $352.88  +3.0%   $+2.83  |
|                                                                        |
|  Total invested                                                  $97.01|
|  Total open P&L                                                  $+2.83|
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
|  2026-08-06  SELL  GEV  Pullback50  $93.51  P&L $-0.67                 |
|  2026-08-06  SELL  GS  Pullback50  $94.20  P&L $+0.13                  |
|  2026-08-06  SELL  DOV  Pullback50  $93.98  P&L $-0.11                 |
|  2026-08-06  SELL  AVB  Pullback50  $94.61  P&L $+1.05                 |
|  2026-08-06  SELL  AES  Pullback50  $93.56  P&L $-0.10                 |
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
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
=== options_morning_bot (PAPER) 2026-08-07T09:05:47.808084-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $143845.71, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,845.71                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
|  AMD260807C00537500            6    -80.8%   $   -277.64               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=0.5s reconcile=0.11s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.5s. run=#6378 https://github.com/28twagg-ops/TradingBot/actions/runs/31181002814
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-07T09:05:53.878368_

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
## Ledger health — 2026-08-07
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
equity=472.99 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T131117Z

- UTC timestamp: `20260807T131117Z`
- GitHub run: [#6379](https://github.com/28twagg-ops/TradingBot/actions/runs/31181378609)
- Run id: `31181378609`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T09:11:22.060627-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.16},"signals":0,"placed":0,"equity":143605.71,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":0,"filled_today":0,"unattributed_contracts":7,"top_signals":[],"github_run":"6379","github_run_id":"31181378609","status":"ok"}
```

### Live bot full output

```text
13:11:19  INFO      Mode: summary
13:11:19  INFO        Daily log -> logs/daily/2026-08-07.md
13:11:19  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:11 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.79|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $472.79|
|  Cash                                                           $375.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $96.81|
|  Open P&L                                                        $+2.63|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  JBL      Pullback50      $96.81     $342.57  $352.14  +2.8%   $+2.63  |
|                                                                        |
|  Total invested                                                  $96.81|
|  Total open P&L                                                  $+2.63|
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
|  2026-08-06  SELL  GEV  Pullback50  $93.51  P&L $-0.67                 |
|  2026-08-06  SELL  GS  Pullback50  $94.20  P&L $+0.13                  |
|  2026-08-06  SELL  DOV  Pullback50  $93.98  P&L $-0.11                 |
|  2026-08-06  SELL  AVB  Pullback50  $94.61  P&L $+1.05                 |
|  2026-08-06  SELL  AES  Pullback50  $93.56  P&L $-0.10                 |
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
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
=== options_morning_bot (PAPER) 2026-08-07T09:11:22.060627-04:00 ===

[Run context]
After hours (09:11 ET) — exit summary only.
Paper auth OK — equity $143605.71, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,605.71                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
|  AMD260807C00537500            6    -80.8%   $   -277.64               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=0.7s reconcile=0.16s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.7s. run=#6379 https://github.com/28twagg-ops/TradingBot/actions/runs/31181378609
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-07T09:11:28.458585_

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
## Ledger health — 2026-08-07
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
equity=472.79 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T131551Z

- UTC timestamp: `20260807T131551Z`
- GitHub run: [#6380](https://github.com/28twagg-ops/TradingBot/actions/runs/31181759441)
- Run id: `31181759441`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T09:15:56.421578-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.3,"phases_s":{"reconcile":0.6},"signals":0,"placed":0,"equity":143672.11,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":0,"filled_today":0,"unattributed_contracts":7,"top_signals":[],"github_run":"6380","github_run_id":"31181759441","status":"ok"}
```

### Live bot full output

```text
13:15:53  INFO      Mode: summary
13:15:54  INFO        Daily log -> logs/daily/2026-08-07.md
13:15:54  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.49|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $472.49|
|  Cash                                                           $375.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $96.51|
|  Open P&L                                                        $+2.33|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  JBL      Pullback50      $96.51     $342.57  $351.03  +2.5%   $+2.33  |
|                                                                        |
|  Total invested                                                  $96.51|
|  Total open P&L                                                  $+2.33|
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
|  2026-08-06  SELL  GEV  Pullback50  $93.51  P&L $-0.67                 |
|  2026-08-06  SELL  GS  Pullback50  $94.20  P&L $+0.13                  |
|  2026-08-06  SELL  DOV  Pullback50  $93.98  P&L $-0.11                 |
|  2026-08-06  SELL  AVB  Pullback50  $94.61  P&L $+1.05                 |
|  2026-08-06  SELL  AES  Pullback50  $93.56  P&L $-0.10                 |
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
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
=== options_morning_bot (PAPER) 2026-08-07T09:15:56.421578-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $143672.11, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,672.11                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
|  AMD260807C00537500            6    -80.8%   $   -277.64               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=1.3s reconcile=0.6s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.3s. run=#6380 https://github.com/28twagg-ops/TradingBot/actions/runs/31181759441
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-07T09:16:03.397164_

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
## Ledger health — 2026-08-07
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
equity=472.49 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T132040Z

- UTC timestamp: `20260807T132040Z`
- GitHub run: [#6381](https://github.com/28twagg-ops/TradingBot/actions/runs/31182138991)
- Run id: `31182138991`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T09:20:43.688331-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.12},"signals":0,"placed":0,"equity":143741.71,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":0,"filled_today":0,"unattributed_contracts":7,"top_signals":[],"github_run":"6381","github_run_id":"31182138991","status":"ok"}
```

### Live bot full output

```text
13:20:41  INFO      Mode: summary
13:20:41  INFO        Daily log -> logs/daily/2026-08-07.md
13:20:41  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.49|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $472.49|
|  Cash                                                           $375.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $96.51|
|  Open P&L                                                        $+2.33|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  JBL      Pullback50      $96.51     $342.57  $351.03  +2.5%   $+2.33  |
|                                                                        |
|  Total invested                                                  $96.51|
|  Total open P&L                                                  $+2.33|
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
|  2026-08-06  SELL  GEV  Pullback50  $93.51  P&L $-0.67                 |
|  2026-08-06  SELL  GS  Pullback50  $94.20  P&L $+0.13                  |
|  2026-08-06  SELL  DOV  Pullback50  $93.98  P&L $-0.11                 |
|  2026-08-06  SELL  AVB  Pullback50  $94.61  P&L $+1.05                 |
|  2026-08-06  SELL  AES  Pullback50  $93.56  P&L $-0.10                 |
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
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
=== options_morning_bot (PAPER) 2026-08-07T09:20:43.688331-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $143741.71, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,741.71                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
|  AMD260807C00537500            6    -80.8%   $   -277.64               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=0.5s reconcile=0.12s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.5s. run=#6381 https://github.com/28twagg-ops/TradingBot/actions/runs/31182138991
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-07T09:20:49.789926_

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
## Ledger health — 2026-08-07
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
equity=472.49 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T132554Z

- UTC timestamp: `20260807T132554Z`
- GitHub run: [#6382](https://github.com/28twagg-ops/TradingBot/actions/runs/31182524525)
- Run id: `31182524525`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T09:25:58.031988-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.45},"signals":0,"placed":0,"equity":143661.71,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":0,"filled_today":0,"unattributed_contracts":7,"top_signals":[],"github_run":"6382","github_run_id":"31182524525","status":"ok"}
```

### Live bot full output

```text
13:25:55  INFO      Mode: summary
13:25:56  INFO        Daily log -> logs/daily/2026-08-07.md
13:25:56  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.49|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $472.49|
|  Cash                                                           $375.98|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                  $96.51|
|  Open P&L                                                        $+2.33|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (1 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  JBL      Pullback50      $96.51     $342.57  $351.03  +2.5%   $+2.33  |
|                                                                        |
|  Total invested                                                  $96.51|
|  Total open P&L                                                  $+2.33|
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
|  2026-08-06  SELL  GEV  Pullback50  $93.51  P&L $-0.67                 |
|  2026-08-06  SELL  GS  Pullback50  $94.20  P&L $+0.13                  |
|  2026-08-06  SELL  DOV  Pullback50  $93.98  P&L $-0.11                 |
|  2026-08-06  SELL  AVB  Pullback50  $94.61  P&L $+1.05                 |
|  2026-08-06  SELL  AES  Pullback50  $93.56  P&L $-0.10                 |
|  2026-08-05  SELL  NVST  EarningsDrift  $94.33  P&L $-0.22             |
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
=== options_morning_bot (PAPER) 2026-08-07T09:25:58.031988-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $143661.71, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $143,661.71                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
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
|  AMD260807C00537500            6    -80.8%   $   -277.64               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           12    -30.2%   $   -228.00               |
|  NKE260828C00045000           12    -25.6%   $   -194.00               |
|  NKE260807C00042000            6    -50.1%   $   -192.60               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=1.0s reconcile=0.45s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.0s. run=#6382 https://github.com/28twagg-ops/TradingBot/actions/runs/31182524525
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=91 drop=14
Orphan rate: 8.0% (149/1857)
# Options signal frequency

_Generated 2026-08-07T09:26:03.383070_

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
## Ledger health — 2026-08-07
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
equity=472.49 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T133044Z

- UTC timestamp: `20260807T133044Z`
- GitHub run: [#6383](https://github.com/28twagg-ops/TradingBot/actions/runs/31182914866)
- Run id: `31182914866`
- Live bot: exit=`0`, duration=`217s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T09:25:58.031988-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.45},"signals":0,"placed":0,"equity":143661.71,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":0,"filled_today":0,"unattributed_contracts":7,"top_signals":[],"github_run":"6382","github_run_id":"31182524525","status":"ok"}
```

### Live bot full output

```text
13:30:45  INFO      Mode: morning_prep
13:30:45  INFO        [prep_positions] 1/1 (1 valid)
13:30:45  INFO      Fetching tickers (universe=both)...
13:30:45  INFO        S&P 500: 503
13:30:46  INFO        MidCap 400: 400
13:30:46  INFO        Total: 903 tickers
13:30:47  INFO        [prep_universe] 40/902 (40 valid)
13:30:49  INFO        [prep_universe] 80/902 (80 valid)
13:30:51  INFO        [prep_universe] 120/902 (120 valid)
13:30:52  INFO        [prep_universe] 160/902 (160 valid)
13:30:54  INFO        [prep_universe] 200/902 (199 valid)
13:30:59  INFO        [prep_universe] 240/902 (238 valid)
13:31:12  INFO        [prep_universe] 280/902 (278 valid)
13:31:23  INFO        [prep_universe] 320/902 (318 valid)
13:31:36  INFO        [prep_universe] 360/902 (358 valid)
13:31:48  INFO        [prep_universe] 400/902 (397 valid)
13:32:00  INFO        [prep_universe] 440/902 (437 valid)
13:32:10  INFO        [prep_universe] 480/902 (477 valid)
13:32:23  INFO        [prep_universe] 520/902 (517 valid)
13:32:35  INFO        [prep_universe] 560/902 (557 valid)
13:32:48  INFO        [prep_universe] 600/902 (597 valid)
13:32:58  INFO        [prep_universe] 640/902 (637 valid)
13:33:12  INFO        [prep_universe] 680/902 (677 valid)
13:33:22  INFO        [prep_universe] 720/902 (717 valid)
13:33:36  INFO        [prep_universe] 760/902 (757 valid)
13:33:46  INFO        [prep_universe] 800/902 (797 valid)
13:33:59  INFO        [prep_universe] 840/902 (836 valid)
13:34:12  INFO        [prep_universe] 880/902 (876 valid)
13:34:19  INFO        [prep_universe] 902/902 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.37|
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
|  Open positions                                                       1|
|  Invested                                                        $95.39|
|  Open P&L                                                        $+1.21|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  JBL      Pullback50      $95.39     $342.57  $346.96  +1.3%   $+1.21  |
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
|  Signal candidates                                                   32|
|  Universe scanned                                                   902|
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
=== options_morning_bot (PAPER) 2026-08-07T09:34:23.662102-04:00 ===

[Run context]
Paper auth OK — equity $143020.49, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 09:34:27,000 INFO   EXIT [b451|lab0451_s367_w3_1045_1120_r2|S367] stop_loss (-70.8%) SELL 1 NKE260904C00045000 @<= 0.22
2026-08-07 09:34:27,121 INFO   EXIT [b891|lab0891_s410_w4_1120_1135_r2|S410] take_profit (+98.0%) SELL 1 PATH260807C00013500 @<= 1.00
2026-08-07 09:34:27,250 INFO   EXIT [b419|lab0419_s365_w1_0928_1005_r2|S365] stop_loss (-82.5%) SELL 1 NKE260821C00044000 @<= 0.01
2026-08-07 09:34:27,371 INFO   EXIT [b194|lab0194_s218_w2_1005_1045_r1|S218] stop_loss (-100.0%) SELL 1 DKNG260807C00023000 @<= 0.01
2026-08-07 09:34:27,577 INFO   EXIT [b393|lab0393_s363_w2_1005_1045_r2|S363] stop_loss (-51.8%) SELL 1 MARA260814C00011500 @<= 0.21
2026-08-07 09:34:27,980 INFO   EXIT [b183|lab0183_s217_w3_1045_1120_r2|S217] stop_loss (-85.0%) SELL 1 RBLX260807C00038500 @<= 0.01
2026-08-07 09:34:28,259 INFO   EXIT [b329|lab0329_s357_w1_0928_1005_r2|S357] stop_loss (-81.0%) SELL 1 NKE260828C00045000 @<= 0.09
2026-08-07 09:34:29,571 INFO   EXIT [b76|lab0076_s209_w3_1045_1120_r1|S209] stop_loss (-62.7%) SELL 1 AMD260807C00535000 @<= 0.19
2026-08-07 09:34:30,976 INFO   EXIT [b904|lab0904_s411_w4_1120_1135_r1|S411] stop_loss (-98.4%) SELL 1 AMD260807C00532500 @<= 0.01
2026-08-07 09:34:31,115 INFO   EXIT [b886|lab0886_s410_w2_1005_1045_r1|S410] take_profit (+101.5%) SELL 1 PATH260807C00013000 @<= 1.32
2026-08-07 09:34:31,248 INFO   EXIT [b411|lab0411_s364_w4_1120_1135_r2|S364] stop_loss (-60.9%) SELL 1 MARA260814C00012000 @<= 0.16
  EXIT [b83|lab0083_s210_w2_1005_1045_r2|S210] stop_loss (-82.6%) SELL failed CVNA260807C00073000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] stop_loss (-82.2%) SELL failed CVNA260807C00072000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 09:34:33,049 INFO   EXIT [b84|lab0084_s210_w3_1045_1120_r1|S210] stop_loss (-82.2%) SELL 1 CVNA260807C00072000 @<= 0.03
2026-08-07 09:34:33,317 INFO   EXIT [b376|lab0376_s362_w1_0928_1005_r1|S362] stop_loss (-98.4%) SELL 1 NKE260807C00042000 @<= 0.01
2026-08-07 09:34:33,614 INFO   EXIT [b834|lab0834_s406_w4_1120_1135_r1|S406] take_profit (+57.4%) SELL 1 PLTR260807C00165000 @<= 0.31
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] stop_loss (-74.5%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 09:34:34,360 INFO   EXIT [b294|lab0294_s352_w4_1120_1135_r1|S352] stop_loss (-72.2%) SELL 1 COIN260807C00160000 @<= 0.05
2026-08-07 09:34:34,465 INFO   EXIT [b889|lab0889_s410_w3_1045_1120_r2|S410] stop_loss (-69.9%) SELL 1 MARA260807C00010500 @<= 0.23
2026-08-07 09:34:34,776 INFO   EXIT [b98|lab0098_s211_w3_1045_1120_r1|S211] stop_loss (-80.0%) SELL 1 PLTR260807C00172500 @<= 0.01
2026-08-07 09:34:38,563 INFO   EXIT [b79|lab0079_s209_w4_1120_1135_r2|S209] stop_loss (-98.3%) SELL 1 AMD260807C00537500 @<= 0.02

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260807T133612Z

- UTC timestamp: `20260807T133612Z`
- GitHub run: [#6384](https://github.com/28twagg-ops/TradingBot/actions/runs/31183317916)
- Run id: `31183317916`
- Live bot: exit=`0`, duration=`218s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T09:25:58.031988-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.45},"signals":0,"placed":0,"equity":143661.71,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":0,"filled_today":0,"unattributed_contracts":7,"top_signals":[],"github_run":"6382","github_run_id":"31182524525","status":"ok"}
```

### Live bot full output

```text
13:36:13  INFO      Mode: morning_prep
13:36:14  INFO        [prep_positions] 1/1 (1 valid)
13:36:14  INFO      Fetching tickers (universe=both)...
13:36:14  INFO        S&P 500: 503
13:36:15  INFO        MidCap 400: 400
13:36:15  INFO        Total: 903 tickers
13:36:16  INFO        [prep_universe] 40/902 (40 valid)
13:36:18  INFO        [prep_universe] 80/902 (80 valid)
13:36:19  INFO        [prep_universe] 120/902 (120 valid)
13:36:21  INFO        [prep_universe] 160/902 (160 valid)
13:36:22  INFO        [prep_universe] 200/902 (199 valid)
13:36:30  INFO        [prep_universe] 240/902 (238 valid)
13:36:40  INFO        [prep_universe] 280/902 (278 valid)
13:36:53  INFO        [prep_universe] 320/902 (318 valid)
13:37:04  INFO        [prep_universe] 360/902 (358 valid)
13:37:17  INFO        [prep_universe] 400/902 (397 valid)
13:37:28  INFO        [prep_universe] 440/902 (437 valid)
13:37:41  INFO        [prep_universe] 480/902 (477 valid)
13:37:51  INFO        [prep_universe] 520/902 (517 valid)
13:38:05  INFO        [prep_universe] 560/902 (557 valid)
13:38:18  INFO        [prep_universe] 600/902 (597 valid)
13:38:28  INFO        [prep_universe] 640/902 (637 valid)
13:38:41  INFO        [prep_universe] 680/902 (677 valid)
13:38:51  INFO        [prep_universe] 720/902 (717 valid)
13:39:05  INFO        [prep_universe] 760/902 (757 valid)
13:39:18  INFO        [prep_universe] 800/902 (797 valid)
13:39:28  INFO        [prep_universe] 840/902 (836 valid)
13:39:41  INFO        [prep_universe] 880/902 (876 valid)
13:39:48  INFO        [prep_universe] 902/902 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.67|
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
|  Open positions                                                       1|
|  Invested                                                        $95.69|
|  Open P&L                                                        $+1.51|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  JBL      Pullback50      $95.69     $342.57  $348.05  +1.6%   $+1.51  |
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
  open_lots=136 paper_keys=yes dry_run=False
  alpaca positions=27
  FLAG b77|S209|b575fd49 missing from Alpaca
  FLAG b76|S209|4bf621ac missing from Alpaca
  FLAG b905|S411|dc4bd756 missing from Alpaca
  FLAG b904|S411|016a6eb3 missing from Alpaca
  FLAG b0|ORPHAN|6f0bf7f1 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T09:39:52.734576-04:00 ===

[Run context]
Paper auth OK — equity $142048.17, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 09:39:56,577 INFO   EXIT [b328|lab0328_s357_w1_0928_1005_r1|S357] stop_loss (-81.0%) SELL 1 NKE260828C00045000 @<= 0.09
2026-08-07 09:39:57,034 INFO   EXIT [b287|lab0287_s351_w4_1120_1135_r2|S351] stop_loss (-68.7%) SELL 1 COIN260807C00160000 @<= 0.06
2026-08-07 09:39:57,800 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-98.4%) SELL 4 NKE260807C00042000 @<= 0.01
2026-08-07 09:39:57,924 INFO   EXIT [b771|lab0771_s396_w2_1005_1045_r2|S396] stop_loss (-83.6%) SELL 1 MARA260807C00010500 @<= 0.13
2026-08-07 09:39:58,077 INFO   EXIT [b418|lab0418_s365_w1_0928_1005_r1|S365] stop_loss (-82.5%) SELL 1 NKE260821C00044000 @<= 0.01
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] take_profit (+52.9%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 09:39:58,672 INFO   EXIT [b84|lab0084_s210_w3_1045_1120_r1|S210] stop_loss (-80.0%) SELL 1 PLTR260807C00172500 @<= 0.01
2026-08-07 09:39:58,819 INFO   EXIT [b182|lab0182_s217_w3_1045_1120_r1|S217] stop_loss (-85.0%) SELL 1 RBLX260807C00038500 @<= 0.04
2026-08-07 09:39:59,111 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-51.2%) SELL 1 DKNG260807C00023000 @<= 0.17
2026-08-07 09:39:59,503 INFO   EXIT [b392|lab0392_s363_w2_1005_1045_r1|S363] stop_loss (-65.9%) SELL 1 MARA260814C00011500 @<= 0.18
  EXIT [b83|lab0083_s210_w2_1005_1045_r2|S210] stop_loss (-73.9%) SELL failed CVNA260807C00073000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 09:40:00,139 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+57.4%) SELL 3 PLTR260807C00165000 @<= 0.31
2026-08-07 09:40:00,291 INFO   EXIT [b887|lab0887_s410_w2_1005_1045_r2|S410] take_profit (+125.4%) SELL 1 PATH260807C00013000 @<= 1.52
2026-08-07 09:40:02,951 INFO   EXIT [b890|lab0890_s410_w4_1120_1135_r1|S410] take_profit (+104.0%) SELL 1 PATH260807C00013500 @<= 0.99

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260807T134106Z

- UTC timestamp: `20260807T134106Z`
- GitHub run: [#6385](https://github.com/28twagg-ops/TradingBot/actions/runs/31183722113)
- Run id: `31183722113`
- Live bot: exit=`0`, duration=`216s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T09:25:58.031988-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.45},"signals":0,"placed":0,"equity":143661.71,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":0,"filled_today":0,"unattributed_contracts":7,"top_signals":[],"github_run":"6382","github_run_id":"31182524525","status":"ok"}
```

### Live bot full output

```text
13:41:07  INFO      Mode: morning_prep
13:41:07  INFO        [prep_positions] 1/1 (1 valid)
13:41:07  INFO        Universe cache hit: 903 tickers (tickers_2026-08-07.json)
13:41:08  INFO        [prep_universe] 40/902 (40 valid)
13:41:10  INFO        [prep_universe] 80/902 (80 valid)
13:41:11  INFO        [prep_universe] 120/902 (120 valid)
13:41:13  INFO        [prep_universe] 160/902 (160 valid)
13:41:14  INFO        [prep_universe] 200/902 (199 valid)
13:41:21  INFO        [prep_universe] 240/902 (238 valid)
13:41:34  INFO        [prep_universe] 280/902 (278 valid)
13:41:45  INFO        [prep_universe] 320/902 (318 valid)
13:41:58  INFO        [prep_universe] 360/902 (358 valid)
13:42:11  INFO        [prep_universe] 400/902 (397 valid)
13:42:21  INFO        [prep_universe] 440/902 (437 valid)
13:42:34  INFO        [prep_universe] 480/902 (477 valid)
13:42:45  INFO        [prep_universe] 520/902 (517 valid)
13:42:58  INFO        [prep_universe] 560/902 (557 valid)
13:43:10  INFO        [prep_universe] 600/902 (597 valid)
13:43:20  INFO        [prep_universe] 640/902 (637 valid)
13:43:33  INFO        [prep_universe] 680/902 (677 valid)
13:43:46  INFO        [prep_universe] 720/902 (717 valid)
13:43:56  INFO        [prep_universe] 760/902 (757 valid)
13:44:10  INFO        [prep_universe] 800/902 (797 valid)
13:44:23  INFO        [prep_universe] 840/902 (836 valid)
13:44:33  INFO        [prep_universe] 880/902 (876 valid)
13:44:40  INFO        [prep_universe] 902/902 (898 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $471.64|
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
|  Open positions                                                       1|
|  Invested                                                        $95.66|
|  Open P&L                                                        $+1.48|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  JBL      Pullback50      $95.66     $342.57  $347.95  +1.6%   $+1.48  |
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
|  Signal candidates                                                   28|
|  Universe scanned                                                   902|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=136 paper_keys=yes dry_run=False
  alpaca positions=22
  FLAG b376|S362|8a6028c7 missing from Alpaca
  FLAG b834|S406|3c198b2a missing from Alpaca
  FLAG b76|S209|4bf621ac missing from Alpaca
  FLAG b98|S211|9a45331c missing from Alpaca
  FLAG b84|S210|97e03bb7 missing from Alpaca
  FLAG b0|ORPHAN|a2e0625d missing from Alpaca
  FLAG b904|S411|016a6eb3 missing from Alpaca
  FLAG b891|S410|0fcf0f01 missing from Alpaca
  FLAG b890|S410|33773978 missing from Alpaca
  FLAG b194|S218|1f74d736 missing from Alpaca
  FLAG b0|ORPHAN|53cf98d7 missing from Alpaca
  FLAG b0|ORPHAN|6f0bf7f1 missing from Alpaca
  FLAG b0|ORPHAN|e69292db missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T09:44:44.675529-04:00 ===

[Run context]
Paper auth OK — equity $142579.82, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 09:44:45,880 INFO   EXIT [b888|lab0888_s410_w3_1045_1120_r1|S410] stop_loss (-79.5%) SELL 1 MARA260807C00010500 @<= 0.16
2026-08-07 09:44:46,541 INFO   EXIT [b286|lab0286_s351_w4_1120_1135_r1|S351] stop_loss (-65.2%) SELL 1 COIN260807C00160000 @<= 0.11
2026-08-07 09:44:46,669 INFO   EXIT [b408|lab0408_s364_w3_1045_1120_r1|S364] stop_loss (-61.8%) SELL 1 MARA260814C00011500 @<= 0.20
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] take_profit (+56.9%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b83|lab0083_s210_w2_1005_1045_r2|S210] stop_loss (-56.5%) SELL failed CVNA260807C00073000: {"code":40010001,"message":"client_order_id must be unique"}

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260807T134610Z

- UTC timestamp: `20260807T134610Z`
- GitHub run: [#6386](https://github.com/28twagg-ops/TradingBot/actions/runs/31184131693)
- Run id: `31184131693`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T09:25:58.031988-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.45},"signals":0,"placed":0,"equity":143661.71,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":0,"filled_today":0,"unattributed_contracts":7,"top_signals":[],"github_run":"6382","github_run_id":"31182524525","status":"ok"}
```

### Live bot full output

```text
13:46:12  INFO      Mode: morning_scan
13:46:13  INFO        [positions] 1/1 (1 valid)
13:46:13  INFO        SELL LIMIT JBL  qty=0.274920308  limit=$349.79  id=f0542b3b-2e6b-4678-a8e8-01c77f619019
13:46:43  INFO        SELL LIMIT not filled for JBL, falling back to market
13:46:43  INFO        SELL MARKET JBL closed
13:46:45  INFO        TX logged: SELL JBL  P&L 2.31%
13:46:45  INFO        Universe cache hit: 903 tickers (tickers_2026-08-07.json)
13:46:46  INFO        [universe] 40/903 (40 valid)
13:46:47  INFO        [universe] 80/903 (80 valid)
13:46:49  INFO        [universe] 120/903 (120 valid)
13:46:50  INFO        [universe] 160/903 (160 valid)
13:46:51  INFO        [universe] 200/903 (199 valid)
13:46:58  INFO        [universe] 240/903 (238 valid)
13:47:12  INFO        [universe] 280/903 (278 valid)
13:47:22  INFO        [universe] 320/903 (318 valid)
13:47:35  INFO        [universe] 360/903 (358 valid)
13:47:46  INFO        [universe] 400/903 (397 valid)
13:47:59  INFO        [universe] 440/903 (437 valid)
13:48:10  INFO        [universe] 480/903 (477 valid)
13:48:23  INFO        [universe] 520/903 (517 valid)
13:48:36  INFO        [universe] 560/903 (557 valid)
13:48:46  INFO        [universe] 600/903 (597 valid)
13:48:59  INFO        [universe] 640/903 (637 valid)
13:49:12  INFO        [universe] 680/903 (677 valid)
13:49:22  INFO        [universe] 720/903 (717 valid)
13:49:35  INFO        [universe] 760/903 (757 valid)
13:49:48  INFO        [universe] 800/903 (797 valid)
13:49:59  INFO        [universe] 840/903 (836 valid)
13:50:11  INFO        [universe] 880/903 (876 valid)
13:50:18  INFO        [universe] 903/903 (899 valid)
```

### Options bot full output

```text

## Run 20260807T135111Z

- UTC timestamp: `20260807T135111Z`
- GitHub run: [#6387](https://github.com/28twagg-ops/TradingBot/actions/runs/31184541326)
- Run id: `31184541326`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T09:25:58.031988-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.45},"signals":0,"placed":0,"equity":143661.71,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":0,"filled_today":0,"unattributed_contracts":7,"top_signals":[],"github_run":"6382","github_run_id":"31182524525","status":"ok"}
```

### Live bot full output

```text
13:51:12  INFO      Mode: morning_scan
13:51:13  INFO        [positions] 5/5 (5 valid)
13:51:13  INFO        SELL LIMIT DOV  qty=0.445179655  limit=$211.80  id=7cb5c805-5972-4335-981f-805d35e4893a
13:51:43  INFO        SELL LIMIT filled DOV (confirmed by position check)
13:51:43  INFO        TX logged: SELL DOV  P&L 0.02%
13:51:43  INFO        Universe cache hit: 903 tickers (tickers_2026-08-07.json)
13:51:44  INFO        [universe] 40/899 (40 valid)
13:51:46  INFO        [universe] 80/899 (80 valid)
13:51:47  INFO        [universe] 120/899 (120 valid)
13:51:48  INFO        [universe] 160/899 (160 valid)
13:51:50  INFO        [universe] 200/899 (199 valid)
13:51:57  INFO        [universe] 240/899 (238 valid)
13:52:08  INFO        [universe] 280/899 (278 valid)
13:52:21  INFO        [universe] 320/899 (318 valid)
13:52:32  INFO        [universe] 360/899 (358 valid)
13:52:45  INFO        [universe] 400/899 (397 valid)
13:52:58  INFO        [universe] 440/899 (437 valid)
13:53:08  INFO        [universe] 480/899 (477 valid)
13:53:21  INFO        [universe] 520/899 (517 valid)
13:53:34  INFO        [universe] 560/899 (557 valid)
13:53:44  INFO        [universe] 600/899 (597 valid)
13:53:57  INFO        [universe] 640/899 (637 valid)
13:54:08  INFO        [universe] 680/899 (677 valid)
13:54:21  INFO        [universe] 720/899 (717 valid)
13:54:34  INFO        [universe] 760/899 (757 valid)
13:54:45  INFO        [universe] 800/899 (797 valid)
13:54:58  INFO        [universe] 840/899 (836 valid)
13:55:08  INFO        [universe] 880/899 (876 valid)
13:55:15  INFO        [universe] 899/899 (895 valid)
```

### Options bot full output

```text

## Run 20260807T135608Z

- UTC timestamp: `20260807T135608Z`
- GitHub run: [#6388](https://github.com/28twagg-ops/TradingBot/actions/runs/31184959350)
- Run id: `31184959350`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T09:25:58.031988-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.45},"signals":0,"placed":0,"equity":143661.71,"open_positions":28,"pending_orders":0,"open_lots":136,"submitted_today":0,"filled_today":0,"unattributed_contracts":7,"top_signals":[],"github_run":"6382","github_run_id":"31182524525","status":"ok"}
```

### Live bot full output

```text
13:56:09  INFO      Mode: morning_scan
13:56:09  INFO        [positions] 4/4 (4 valid)
13:56:09  INFO        SELL order cancelled CNC  type=OrderType.STOP  id=bf8e749c-b458-4f48-b30b-02e4427aca36
13:56:09  INFO        SELL LIMIT CNC  qty=1.460149632  limit=$64.81  id=94904ea8-3502-4b78-877a-cc3b9526dae4
13:56:39  INFO        SELL LIMIT filled CNC (confirmed by position check)
13:56:39  INFO        TX logged: SELL CNC  P&L 0.38%
13:56:39  INFO        Universe cache hit: 903 tickers (tickers_2026-08-07.json)
13:56:40  INFO        [universe] 40/900 (40 valid)
13:56:42  INFO        [universe] 80/900 (80 valid)
13:56:43  INFO        [universe] 120/900 (120 valid)
13:56:44  INFO        [universe] 160/900 (160 valid)
13:56:45  INFO        [universe] 200/900 (199 valid)
13:56:53  INFO        [universe] 240/900 (238 valid)
13:57:06  INFO        [universe] 280/900 (278 valid)
13:57:16  INFO        [universe] 320/900 (318 valid)
13:57:29  INFO        [universe] 360/900 (358 valid)
13:57:42  INFO        [universe] 400/900 (397 valid)
13:57:53  INFO        [universe] 440/900 (437 valid)
13:58:06  INFO        [universe] 480/900 (477 valid)
13:58:16  INFO        [universe] 520/900 (517 valid)
13:58:29  INFO        [universe] 560/900 (557 valid)
13:58:42  INFO        [universe] 600/900 (597 valid)
13:58:55  INFO        [universe] 640/900 (637 valid)
13:59:05  INFO        [universe] 680/900 (677 valid)
13:59:18  INFO        [universe] 720/900 (717 valid)
13:59:28  INFO        [universe] 760/900 (757 valid)
13:59:41  INFO        [universe] 800/900 (797 valid)
13:59:54  INFO        [universe] 840/900 (836 valid)
14:00:04  INFO        [universe] 880/900 (876 valid)
14:00:11  INFO        [universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.24|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-08-07|
|  Universe                                                          both|
|  Mo~  Aug: VolumeSpike + 52wkLow (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $472.24|
|  Cash                                                           $117.96|
|  Reserve                                          $23.61  (always kept)|
|  Available                                     $94.35  (for new trades)|
|  Trade size             $94.45  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (4 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  AAPL     Pullback50      $94.56     $311.48  $311.82  +0.1%   $+0.10  |
|  BBY      Pullback50      $95.16     $80.12   $80.72   +0.7%   $+0.70  |
|  CNC      Pullback50      $94.82     $64.69   $64.94   +0.4%   $+0.36  |
|  ESS      Pullback50      $69.74     $286.19  $285.29  -0.3%   $-0.22  |
|                                                                        |
|  Total invested                                                 $354.29|
|  Total open P&L                                                  $+0.95|
|  Buys today: 0  |  entry cap: 1  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (41770.7m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  ESS  P&L -0.3%  $-0.22                                            HOLD|
|  AAPL  P&L +0.1%  $+0.10                                           HOLD|
|  CNC  P&L +0.4%  $+0.36                           EXIT: midline (+0.4%)|
|  BBY  P&L +0.7%  $+0.70                                            HOLD|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 1 | filled 1 | partial 0 | pending 0 | failed 0|
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
|                         SIGNALS FOUND  --  28                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  AES      Pullback50      eq     $14.72   41.0   -2.94   50MA bounce (+|
|  GOOG     Pullback50      eq     $355.30  51.7   -2.04   50MA bounce (+|
|  DOV      Pullback50      eq     $212.35  52.6   -1.43   50MA bounce (-|
|  ES       Pullback50      eq     $72.02   39.2   -2.17   50MA bounce (+|
|  FTV      Pullback50      eq     $61.11   50.4   -2.13   50MA bounce (+|
|  DOC      Pullback50      eq     $21.18   35.0   -2.86   50MA bounce (+|
|  HUM      Pullback50      eq     $372.22  36.6   -1.69   50MA bounce (-|
|  MS       Pullback50      eq     $214.12  53.7   -2.20   50MA bounce (-|
|  PCG      Pullback50      eq     $17.09   44.5   -1.37   50MA bounce (+|
|  O        Pullback50      eq     $62.65   26.6   -3.27   50MA bounce (-|
|  SWKS     Pullback50      eq     $67.68   66.8   -1.72   50MA bounce (+|
|  TTWO     Pullback50      eq     $235.36  46.4   -1.73   50MA bounce (+|
|  VTRS     Pullback50      eq     $16.65   46.1   -2.09   50MA bounce (+|
|  ALSN     Pullback50      eq     $117.62  55.8   -2.14   50MA bounce (+|
|  ALV      Pullback50      eq     $123.03  61.8   -1.84   50MA bounce (+|
|  BC       Pullback50      eq     $81.52   56.6   -2.32   50MA bounce (+|
|  BKH      Pullback50      eq     $72.99   41.1   -2.22   50MA bounce (-|
|  BWA      Pullback50      eq     $67.58   69.8   -2.16   50MA bounce (-|
|  CBT      Pullback50      eq     $87.36   46.8   -1.45   50MA bounce (-|
|  COLB     Pullback50      eq     $31.04   30.9   -2.19   50MA bounce (-|
|  CUZ      Pullback50      eq     $30.09   37.0   -2.23   50MA bounce (+|
|  EXP      Pullback50      eq     $216.01  60.9   -2.00   50MA bounce (+|
|  FR       Pullback50      eq     $63.61   22.0   -2.95   50MA bounce (-|
|  KRC      Pullback50      eq     $37.84   38.6   -1.94   50MA bounce (-|
|  NNN      Pullback50      eq     $47.02   26.8   -1.95   50MA bounce (+|
|  NWE      Pullback50      eq     $70.69   43.3   -2.35   50MA bounce (-|14:00:14  INFO        BUY  AES  $94.45  [Pullback50]  id=da983e81-2c51-4d6f-ba76-b314832ff046
14:00:14  INFO        BUY  GOOG  $94.45  [Pullback50]  id=42274797-dd03-43be-956e-706d082ef7d3
```

### Options bot full output

```text

## Run 20260807T140111Z

- UTC timestamp: `20260807T140111Z`
- GitHub run: [#6389](https://github.com/28twagg-ops/TradingBot/actions/runs/31185381191)
- Run id: `31185381191`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`128s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T10:01:17.076246-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (11 new)","elapsed_s":118.8,"phases_s":{"reconcile":0.6,"cancel":0.13,"manage":21.74,"scan":73.32,"entries":19.53,"reconcile2":2.72},"signals":99,"placed":11,"equity":141934.7,"open_positions":20,"pending_orders":4,"open_lots":107,"submitted_today":11,"filled_today":7,"unattributed_contracts":3,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S202:TTD","S203:ARM"],"github_run":"6389","github_run_id":"31185381191","status":"ok"}
```

### Live bot full output

```text
14:01:12  INFO      Mode: exits
14:01:13  INFO        Daily log -> logs/daily/2026-08-07.md
14:01:13  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (2 ledger rows)
14:01:13  INFO        place_all_stops: checking 5 positions...
14:01:13  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
14:01:13  INFO        STOP-MARKET placed AES  qty=6 (pos=6.4132)  stop=$14.65  id=1c245d07-0e69-461b-ae22-8db8e521e9b7
14:01:13  INFO        STOP already live BBY @ $79.72
14:01:13  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
14:01:13  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
14:01:14  INFO        [positions] 5/5 (5 valid)
14:01:14  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.66|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ESS  P&L -0.3%  $-0.22                                            HOLD|
|  GOOG  P&L -0.1%  $-0.08                                           HOLD|
|  AES  P&L -0.0%  $-0.03                                            HOLD|
|  AAPL  P&L +0.2%  $+0.16                                           HOLD|
|  BBY  P&L +1.3%  $+1.24                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=108 paper_keys=yes dry_run=False
  alpaca positions=20
  FLAG b887|S410|69709dd2 missing from Alpaca
  FLAG b182|S217|e1631bd3 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T10:01:17.076246-04:00 ===

[Run context]
Paper auth OK — equity $141934.70, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 10:01:19,957 INFO   EXIT [b770|lab0770_s396_w2_1005_1045_r1|S396] stop_loss (-97.3%) SELL 1 MARA260807C00010500 @<= 0.03
2026-08-07 10:01:21,815 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-82.6%) SELL 4 COIN260807C00160000 @<= 0.06
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] take_profit (+65.9%) SELL failed CVNA260807C00072000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 10:01:23,476 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+65.9%) SELL 1 CVNA260807C00072000 @<= 0.55
2026-08-07 10:01:27,938 INFO   EXIT [b80|lab0080_s210_w1_0928_1005_r1|S210] take_profit (+300.0%) SELL 1 PLTR260807C00175000 @<= 0.20
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] take_profit (+119.6%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 10:01:34,959 INFO   EXIT [b78|lab0078_s209_w4_1120_1135_r1|S209] stop_loss (-98.3%) SELL 1 AMD260807C00537500 @<= 0.02
2026-08-07 10:01:39,865 INFO   EXIT [b395|lab0395_s363_w3_1045_1120_r2|S363] stop_loss (-79.9%) SELL 1 MARA260814C00011500 @<= 0.11

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 99 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S202:TTD', 'S203:ARM']
Paper lab: $141855 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 82 no tradeable call, 76 pending order
Placed 11 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $141,934.70                             |
|  Signals this run              99                                      |
|  Orders submitted (session)    11                                      |
|  Orders filled today (ledger)  7                                       |
|  Entries placed this run       11                                      |
|  Open virtual lots             107                                     |
|  Broker option positions       20                                      |
|  Unattributed contracts        3 (orphan reconcile)                    |
|  Pending orders                4                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1380  buckets=283  win=40%                           |
|  Returns   avg=+21.0%  med=-35.3%  p10=-78.8%  p90=+133.3%             |
|  Realized  $+9,273.47                                                  |
|  Raw incl dropped  trades=1914  real=$+7,677.92                        |
|  Today     trades=36  avg=-59.3%  med=-73.0%  real=$-1,095.71          |
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
|  ... 275 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (4)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S212:AAPL(2), S403:AAPL(2)              |
+------------------------------------------------------------------------+
|  b108 S212 AAPL     limit=0.51                                         |
|  b109 S212 AAPL     limit=0.51                                         |
|  b262 S403 AAPL     limit=0.51                                         |
|  b263 S403 AAPL     limit=0.51                                         |
+========================================================================+
+========================================================================+
|  PENDING EXITS (8)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 3 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (20)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  MARA260814C00011500          12    -79.9%   $   -477.60               |
|  NKE260828C00045000           10    -43.0%   $   -271.67               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  MARA260814C00012000           6    -87.0%   $   -200.00               |
|  COIN260807C00160000           8    -79.1%   $   -182.18               |
|  ... 12 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=118.8s reconcile=0.6s cancel=0.13s manage=21.74s scan=73.32s entries=19.53s
STATUS: options_morning_bot run complete (PAPER) elapsed=118.8s. run=#6389 https://github.com/28twagg-ops/TradingBot/actions/runs/31185381191
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 28 buckets closed trades, $-1,095.71 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=90 drop=15
Orphan rate: 8.5% (163/1914)
# Options signal frequency

_Generated 2026-08-07T10:03:21.587083_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    12 | WARN | <<<
| Total open lots             |   107 | INFO |
| Total closed lots           |  1284 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=472.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T140542Z

- UTC timestamp: `20260807T140542Z`
- GitHub run: [#6390](https://github.com/28twagg-ops/TradingBot/actions/runs/31185813241)
- Run id: `31185813241`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`91s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T10:05:46.934514-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (15 new)","elapsed_s":82.7,"phases_s":{"reconcile":0.29,"cancel":0.02,"manage":6.01,"scan":67.79,"entries":7.84,"reconcile2":0.31},"signals":104,"placed":15,"equity":141150.35,"open_positions":21,"pending_orders":15,"open_lots":109,"submitted_today":26,"filled_today":11,"unattributed_contracts":1,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S202:TTD","S203:MSTR"],"github_run":"6390","github_run_id":"31185813241","status":"ok"}
```

### Live bot full output

```text
14:05:43  INFO      Mode: exits
14:05:44  INFO        Daily log -> logs/daily/2026-08-07.md
14:05:44  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
14:05:44  INFO        place_all_stops: checking 5 positions...
14:05:44  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
14:05:44  INFO        STOP already live AES @ $14.65
14:05:44  INFO        STOP already live BBY @ $79.72
14:05:44  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
14:05:44  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
14:05:44  INFO        [positions] 5/5 (5 valid)
14:05:44  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $472.87|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ESS  P&L -0.3%  $-0.22                                            HOLD|
|  GOOG  P&L -0.1%  $-0.06                                           HOLD|
|  AES  P&L +0.0%  $+0.00                                            HOLD|
|  AAPL  P&L +0.2%  $+0.23                                           HOLD|
|  BBY  P&L +1.4%  $+1.36                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=107 paper_keys=yes dry_run=False
  alpaca positions=22
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T10:05:46.934514-04:00 ===

[Run context]
Paper auth OK — equity $141150.35, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 10:05:47,920 INFO   EXIT [b818|lab0818_s405_w3_1045_1120_r1|S405] stop_loss (-82.6%) SELL 1 COIN260807C00160000 @<= 0.06
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] take_profit (+147.1%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] take_profit (+95.6%) SELL failed CVNA260807C00072000: {"code":40010001,"message":"client_order_id must be unique"}

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 104 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S202:TTD', 'S203:MSTR']
Paper lab: $141576 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 110 no tradeable call, 54 already attempted today, 141 pending order
Placed 15 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $141,150.35                             |
|  Signals this run              104                                     |
|  Orders submitted (session)    26                                      |
|  Orders filled today (ledger)  11                                      |
|  Entries placed this run       15                                      |
|  Open virtual lots             109                                     |
|  Broker option positions       21                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                15                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1384  buckets=283  win=40%                           |
|  Returns   avg=+20.7%  med=-35.5%  p10=-79.2%  p90=+132.9%             |
|  Realized  $+9,032.37                                                  |
|  Raw incl dropped  trades=1918  real=$+7,436.82                        |
|  Today     trades=37  avg=-60.0%  med=-74.5%  real=$-1,124.71          |
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
|  ... 275 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  6   0% -80.3 -98.4 -98.6 $   -303       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (15)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S218:UNH(4), S212:AAPL(2), S403:AAPL(2) |
+------------------------------------------------------------------------+
|  b108 S212 AAPL     limit=0.51                                         |
|  b109 S212 AAPL     limit=0.51                                         |
|  b262 S403 AAPL     limit=0.51                                         |
|  b263 S403 AAPL     limit=0.51                                         |
|  b26  S203 DKNG     limit=0.37                                         |
|  ... 10 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  PENDING EXITS (8)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 3 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (21)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  MARA260814C00011500          12    -81.9%   $   -489.60               |
|  NKE260828C00045000           10    -43.0%   $   -271.67               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  MARA260814C00012000           6    -84.3%   $   -194.00               |
|  NKE260821C00044000           10    -28.6%   $   -180.00               |
|  ... 13 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=82.7s reconcile=0.29s cancel=0.02s manage=6.01s scan=67.79s entries=7.84s
STATUS: options_morning_bot run complete (PAPER) elapsed=82.7s. run=#6390 https://github.com/28twagg-ops/TradingBot/actions/runs/31185813241
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 29 buckets closed trades, $-1,124.71 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=90 drop=15
Orphan rate: 8.6% (165/1918)
# Options signal frequency

_Generated 2026-08-07T10:07:15.259973_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    12 | WARN | <<<
| Total open lots             |   109 | INFO |
| Total closed lots           |  1286 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=472.89 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T141047Z

- UTC timestamp: `20260807T141047Z`
- GitHub run: [#6391](https://github.com/28twagg-ops/TradingBot/actions/runs/31186223372)
- Run id: `31186223372`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`103s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T10:10:53.560270-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":94.3,"phases_s":{"reconcile":0.67,"cancel":0.15,"manage":16.53,"scan":67.2,"entries":8.12,"reconcile2":0.76},"signals":107,"placed":0,"equity":141198.12,"open_positions":22,"pending_orders":8,"open_lots":116,"submitted_today":26,"filled_today":18,"unattributed_contracts":2,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S202:TTD","S203:MSTR"],"github_run":"6391","github_run_id":"31186223372","status":"ok"}
```

### Live bot full output

```text
14:10:49  INFO      Mode: exits
14:10:49  INFO        Daily log -> logs/daily/2026-08-07.md
14:10:49  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
14:10:50  INFO        place_all_stops: checking 5 positions...
14:10:50  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
14:10:50  INFO        STOP already live AES @ $14.65
14:10:50  INFO        STOP already live BBY @ $79.72
14:10:50  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
14:10:50  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
14:10:50  INFO        [positions] 5/5 (5 valid)
14:10:51  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.49|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ESS  P&L -0.1%  $-0.08                                            HOLD|
|  AES  P&L -0.0%  $-0.03                                            HOLD|
|  GOOG  P&L +0.1%  $+0.06                                           HOLD|
|  AAPL  P&L +0.3%  $+0.28                                           HOLD|
|  BBY  P&L +1.8%  $+1.70                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=109 paper_keys=yes dry_run=False
  alpaca positions=24
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T10:10:53.560270-04:00 ===

[Run context]
Paper auth OK — equity $141232.12, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 10:10:59,042 INFO   EXIT [b789|lab0789_s398_w3_1045_1120_r2|S398] stop_loss (-82.6%) SELL 1 COIN260807C00160000 @<= 0.06
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] take_profit (+162.7%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] take_profit (+92.6%) SELL failed CVNA260807C00072000: {"code":40010001,"message":"client_order_id must be unique"}

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 107 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S202:TTD', 'S203:MSTR']
Paper lab: $140341 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 44 no tradeable call, 64 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $141,198.12                             |
|  Signals this run              107                                     |
|  Orders submitted (session)    26                                      |
|  Orders filled today (ledger)  18                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             116                                     |
|  Broker option positions       22                                      |
|  Unattributed contracts        2 (orphan reconcile)                    |
|  Pending orders                8                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1385  buckets=283  win=40%                           |
|  Returns   avg=+20.6%  med=-35.5%  p10=-79.2%  p90=+132.8%             |
|  Realized  $+9,008.37                                                  |
|  Raw incl dropped  trades=1919  real=$+7,412.82                        |
|  Today     trades=37  avg=-60.0%  med=-74.5%  real=$-1,124.71          |
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
|  ... 275 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  7   0% -75.5 -98.2 -98.6 $   -327       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (8)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S218:UNH(4), S203:DKNG(2), S212:UBER(2) |
+------------------------------------------------------------------------+
|  b26  S203 DKNG     limit=0.37                                         |
|  b27  S203 DKNG     limit=0.37                                         |
|  b110 S212 UBER     limit=0.42                                         |
|  b111 S212 UBER     limit=0.42                                         |
|  b192 S218 UNH      limit=0.40                                         |
|  ... 3 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (9)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 4 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (22)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  MARA260814C00011500          12    -83.9%   $   -501.60               |
|  NKE260828C00045000           10    -43.0%   $   -271.67               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  MARA260814C00012000           6    -84.3%   $   -194.00               |
|  NKE260821C00044000           10    -28.6%   $   -180.00               |
|  ... 14 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=94.3s reconcile=0.67s cancel=0.15s manage=16.53s scan=67.2s entries=8.12s
STATUS: options_morning_bot run complete (PAPER) elapsed=94.3s. run=#6391 https://github.com/28twagg-ops/TradingBot/actions/runs/31186223372
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 29 buckets closed trades, $-1,124.71 realized
STALE WARNING: 4 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=90 drop=15
Orphan rate: 8.6% (165/1919)
# Options signal frequency

_Generated 2026-08-07T10:12:33.429269_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     1 | WARN | <<<
| Orphaned lots (post-stable) |   439 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    13 | WARN | <<<
| Total open lots             |   116 | INFO |
| Total closed lots           |  1287 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.51 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T141545Z

- UTC timestamp: `20260807T141545Z`
- GitHub run: [#6392](https://github.com/28twagg-ops/TradingBot/actions/runs/31186634029)
- Run id: `31186634029`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T10:10:53.560270-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":94.3,"phases_s":{"reconcile":0.67,"cancel":0.15,"manage":16.53,"scan":67.2,"entries":8.12,"reconcile2":0.76},"signals":107,"placed":0,"equity":141198.12,"open_positions":22,"pending_orders":8,"open_lots":116,"submitted_today":26,"filled_today":18,"unattributed_contracts":2,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S202:TTD","S203:MSTR"],"github_run":"6391","github_run_id":"31186223372","status":"ok"}
```

### Live bot full output

```text
14:15:46  INFO      Mode: exits
14:15:47  INFO        Daily log -> logs/daily/2026-08-07.md
14:15:47  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
14:15:47  INFO        place_all_stops: checking 5 positions...
14:15:47  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
14:15:47  INFO        STOP already live AES @ $14.65
14:15:47  INFO        STOP already live BBY @ $79.72
14:15:47  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
14:15:47  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
14:15:47  INFO        [positions] 5/5 (5 valid)
14:15:48  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.61|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ESS  P&L -0.1%  $-0.04                                            HOLD|
|  AES  P&L -0.0%  $-0.03                                            HOLD|
|  GOOG  P&L +0.1%  $+0.11                                           HOLD|
|  AAPL  P&L +0.2%  $+0.16                                           HOLD|
|  BBY  P&L +2.0%  $+1.87                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=116 paper_keys=yes dry_run=False
  alpaca positions=24
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T10:15:50.165426-04:00 ===

[Run context]
Paper auth OK — equity $140648.00, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] take_profit (+117.6%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 10:15:57,709 INFO   EXIT [b236|lab0236_s401_w2_1005_1045_r1|S401] stop_loss (-55.8%) SELL 1 TSLA260810C00342500 @<= 0.22
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] take_profit (+54.1%) SELL failed CVNA260807C00072000: {"code":40010001,"message":"client_order_id must be unique"}

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
```

---

## Run 20260807T141750Z

- UTC timestamp: `20260807T141750Z`
- GitHub run: [#6393](https://github.com/28twagg-ops/TradingBot/actions/runs/31186774836)
- Run id: `31186774836`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`82s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T10:17:54.619932-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":72.7,"phases_s":{"reconcile":0.16,"cancel":0.02,"manage":4.33,"scan":62.16,"entries":5.45,"reconcile2":0.19},"signals":119,"placed":1,"equity":141503.98,"open_positions":23,"pending_orders":8,"open_lots":115,"submitted_today":27,"filled_today":19,"unattributed_contracts":2,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S200:TTD","S202:TTD"],"github_run":"6393","github_run_id":"31186774836","status":"ok"}
```

### Live bot full output

```text
14:17:51  INFO      Mode: exits
14:17:52  INFO        Daily log -> logs/daily/2026-08-07.md
14:17:52  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
14:17:52  INFO        place_all_stops: checking 5 positions...
14:17:52  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
14:17:52  INFO        STOP already live AES @ $14.65
14:17:52  INFO        STOP already live BBY @ $79.72
14:17:52  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
14:17:52  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
14:17:52  INFO        [positions] 5/5 (5 valid)
14:17:52  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:17 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.43|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.10                                            HOLD|
|  ESS  P&L -0.0%  $-0.03                                            HOLD|
|  GOOG  P&L +0.0%  $+0.04                                           HOLD|
|  AAPL  P&L +0.3%  $+0.32                                           HOLD|
|  BBY  P&L +1.7%  $+1.64                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=116 paper_keys=yes dry_run=False
  alpaca positions=24
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T10:17:54.619932-04:00 ===

[Run context]
Paper auth OK — equity $141503.98, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] take_profit (+123.5%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-50.0%) SELL failed DKNG260814P00021500: {"buy_limit_price":"0.37","code":40310000,"existing_order_id":"48f34570-a984-4d90-af5e-8d9b9353a433","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, sell limit price should be greater than existing buy limit price","sell_limit_price":"0.21"}
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] take_profit (+83.7%) SELL failed CVNA260807C00072000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 10:17:59,200 INFO   EXIT [b424|lab0424_s365_w4_1120_1135_r1|S365] stop_loss (-51.5%) SELL 1 AAPL260814C00330000 @<= 0.30

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 119 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S200:TTD', 'S202:TTD']
Paper lab: $141580 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 66 no tradeable call, 89 pending order
Placed 1 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $141,503.98                             |
|  Signals this run              119                                     |
|  Orders submitted (session)    27                                      |
|  Orders filled today (ledger)  19                                      |
|  Entries placed this run       1                                       |
|  Open virtual lots             115                                     |
|  Broker option positions       23                                      |
|  Unattributed contracts        2 (orphan reconcile)                    |
|  Pending orders                8                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1387  buckets=284  win=40%                           |
|  Returns   avg=+20.5%  med=-36.4%  p10=-79.2%  p90=+132.5%             |
|  Realized  $+8,945.37                                                  |
|  Raw incl dropped  trades=1921  real=$+7,349.82                        |
|  Today     trades=39  avg=-59.7%  med=-71.4%  real=$-1,187.71          |
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
|  ... 276 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  7   0% -75.5 -98.2 -98.6 $   -327       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (8)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S218:UNH(4), S203:DKNG(2), S212:UBER(2) |
+------------------------------------------------------------------------+
|  b26  S203 DKNG     limit=0.37                                         |
|  b27  S203 DKNG     limit=0.37                                         |
|  b110 S212 UBER     limit=0.42                                         |
|  b111 S212 UBER     limit=0.42                                         |
|  b192 S218 UNH      limit=0.40                                         |
|  ... 3 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (9)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 4 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (23)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  MARA260814C00011500          12    -83.9%   $   -501.60               |
|  NKE260828C00045000           10    -43.0%   $   -271.67               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  MARA260814C00012000           6    -87.0%   $   -200.00               |
|  COIN260807C00160000           7    -89.6%   $   -180.41               |
|  ... 15 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=72.7s reconcile=0.16s cancel=0.02s manage=4.33s scan=62.16s entries=5.45s
STATUS: options_morning_bot run complete (PAPER) elapsed=72.7s. run=#6393 https://github.com/28twagg-ops/TradingBot/actions/runs/31186774836
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 31 buckets closed trades, $-1,187.71 realized
STALE WARNING: 3 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=90 drop=15
Orphan rate: 8.6% (165/1921)
# Options signal frequency

_Generated 2026-08-07T10:19:13.021986_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   438 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    13 | WARN | <<<
| Total open lots             |   115 | INFO |
| Total closed lots           |  1289 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.46 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T142042Z

- UTC timestamp: `20260807T142042Z`
- GitHub run: [#6394](https://github.com/28twagg-ops/TradingBot/actions/runs/31187046498)
- Run id: `31187046498`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`79s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T10:20:46.643005-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (3 new)","elapsed_s":70.3,"phases_s":{"reconcile":0.18,"cancel":0.05,"manage":7.37,"scan":56.31,"entries":5.6,"reconcile2":0.19},"signals":139,"placed":3,"equity":141942.41,"open_positions":23,"pending_orders":11,"open_lots":115,"submitted_today":30,"filled_today":19,"unattributed_contracts":2,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S200:TTD","S202:TTD"],"github_run":"6394","github_run_id":"31187046498","status":"ok"}
```

### Live bot full output

```text
14:20:43  INFO      Mode: exits
14:20:44  INFO        Daily log -> logs/daily/2026-08-07.md
14:20:44  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
14:20:44  INFO        place_all_stops: checking 5 positions...
14:20:44  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
14:20:44  INFO        STOP already live AES @ $14.65
14:20:44  INFO        STOP already live BBY @ $79.72
14:20:44  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
14:20:44  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
14:20:44  INFO        [positions] 5/5 (5 valid)
14:20:44  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.72|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.10                                            HOLD|
|  GOOG  P&L +0.0%  $+0.03                                           HOLD|
|  ESS  P&L +0.1%  $+0.05                                            HOLD|
|  AAPL  P&L +0.5%  $+0.52                                           HOLD|
|  BBY  P&L +1.8%  $+1.66                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=115 paper_keys=yes dry_run=False
  alpaca positions=25
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T10:20:46.643005-04:00 ===

[Run context]
Paper auth OK — equity $141942.41, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] take_profit (+92.6%) SELL failed CVNA260807C00072000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] take_profit (+158.8%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 139 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S200:TTD', 'S202:TTD']
Paper lab: $142110 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 86 no tradeable call, 66 pending order
Placed 3 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $141,942.41                             |
|  Signals this run              139                                     |
|  Orders submitted (session)    30                                      |
|  Orders filled today (ledger)  19                                      |
|  Entries placed this run       3                                       |
|  Open virtual lots             115                                     |
|  Broker option positions       23                                      |
|  Unattributed contracts        2 (orphan reconcile)                    |
|  Pending orders                11                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1387  buckets=284  win=40%                           |
|  Returns   avg=+20.5%  med=-36.4%  p10=-79.2%  p90=+132.5%             |
|  Realized  $+8,945.37                                                  |
|  Raw incl dropped  trades=1921  real=$+7,349.82                        |
|  Today     trades=39  avg=-59.7%  med=-71.4%  real=$-1,187.71          |
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
|  ... 276 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  7   0% -75.5 -98.2 -98.6 $   -327       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (11)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S218:UNH(4), S203:DKNG(2), S212:UBER(2) |
+------------------------------------------------------------------------+
|  b26  S203 DKNG     limit=0.37                                         |
|  b27  S203 DKNG     limit=0.37                                         |
|  b110 S212 UBER     limit=0.42                                         |
|  b111 S212 UBER     limit=0.42                                         |
|  b192 S218 UNH      limit=0.40                                         |
|  ... 6 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (9)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 4 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (23)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  MARA260814C00011500          12    -79.9%   $   -477.60               |
|  NKE260828C00045000           10    -43.0%   $   -271.67               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  MARA260814C00012000           6    -84.3%   $   -194.00               |
|  NKE260821C00044000           10    -28.6%   $   -180.00               |
|  ... 15 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=70.3s reconcile=0.18s cancel=0.05s manage=7.37s scan=56.31s entries=5.6s
STATUS: options_morning_bot run complete (PAPER) elapsed=70.3s. run=#6394 https://github.com/28twagg-ops/TradingBot/actions/runs/31187046498
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 31 buckets closed trades, $-1,187.71 realized
STALE WARNING: 3 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=90 drop=15
Orphan rate: 8.6% (165/1921)
# Options signal frequency

_Generated 2026-08-07T10:22:02.517365_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   438 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    13 | WARN | <<<
| Total open lots             |   115 | INFO |
| Total closed lots           |  1289 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.72 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T142552Z

- UTC timestamp: `20260807T142552Z`
- GitHub run: [#6395](https://github.com/28twagg-ops/TradingBot/actions/runs/31187467369)
- Run id: `31187467369`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`79s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T10:25:56.459556-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":70.5,"phases_s":{"reconcile":0.23,"cancel":0.02,"manage":7.73,"scan":58.37,"entries":3.38,"reconcile2":0.31},"signals":139,"placed":2,"equity":142715.91,"open_positions":23,"pending_orders":11,"open_lots":114,"submitted_today":32,"filled_today":21,"unattributed_contracts":2,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S200:TTD","S202:TTD"],"github_run":"6395","github_run_id":"31187467369","status":"ok"}
```

### Live bot full output

```text
14:25:53  INFO      Mode: exits
14:25:54  INFO        Daily log -> logs/daily/2026-08-07.md
14:25:54  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
14:25:54  INFO        place_all_stops: checking 5 positions...
14:25:54  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
14:25:54  INFO        STOP already live AES @ $14.65
14:25:54  INFO        STOP already live BBY @ $79.72
14:25:54  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
14:25:54  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
14:25:54  INFO        [positions] 5/5 (5 valid)
14:25:54  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.86|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.10                                            HOLD|
|  GOOG  P&L -0.0%  $-0.04                                           HOLD|
|  ESS  P&L +0.1%  $+0.09                                            HOLD|
|  AAPL  P&L +0.8%  $+0.73                                           HOLD|
|  BBY  P&L +1.7%  $+1.61                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=115 paper_keys=yes dry_run=False
  alpaca positions=25
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T10:25:56.459556-04:00 ===

[Run context]
Paper auth OK — equity $142715.91, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 10:25:58,330 INFO   EXIT [b788|lab0788_s398_w3_1045_1120_r1|S398] stop_loss (-58.3%) SELL 1 COIN260807C00160000 @<= 0.13
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] take_profit (+116.3%) SELL failed CVNA260807C00072000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-62.5%) SELL failed DKNG260814P00021500: {"buy_limit_price":"0.37","code":40310000,"existing_order_id":"48f34570-a984-4d90-af5e-8d9b9353a433","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, sell limit price should be greater than existing buy limit price","sell_limit_price":"0.16"}
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] take_profit (+172.5%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 10:26:04,283 INFO   EXIT [b265|lab0265_s403_w2_1005_1045_r2|S403] take_profit (+62.3%) SELL 1 AAPL260810C00317500 @<= 0.83

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 139 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S200:TTD', 'S202:TTD']
Paper lab: $142925 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 81 no tradeable call, 72 pending order
Placed 2 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $142,715.91                             |
|  Signals this run              139                                     |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  21                                      |
|  Entries placed this run       2                                       |
|  Open virtual lots             114                                     |
|  Broker option positions       23                                      |
|  Unattributed contracts        2 (orphan reconcile)                    |
|  Pending orders                11                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1390  buckets=284  win=40%                           |
|  Returns   avg=+20.4%  med=-36.5%  p10=-79.2%  p90=+132.1%             |
|  Realized  $+8,935.37                                                  |
|  Raw incl dropped  trades=1924  real=$+7,339.82                        |
|  Today     trades=41  avg=-57.5%  med=-71.4%  real=$-1,186.71          |
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
|  ... 276 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  7   0% -75.5 -98.2 -98.6 $   -327       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (11)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S218:UNH(4), S203:DKNG(2), S212:UBER(2) |
+------------------------------------------------------------------------+
|  b26  S203 DKNG     limit=0.37                                         |
|  b27  S203 DKNG     limit=0.37                                         |
|  b110 S212 UBER     limit=0.42                                         |
|  b111 S212 UBER     limit=0.42                                         |
|  b192 S218 UNH      limit=0.40                                         |
|  ... 6 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (8)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 3 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (23)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  MARA260814C00011500          12    -79.9%   $   -477.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  MARA260814C00012000           6    -84.3%   $   -194.00               |
|  NKE260828C00045000           10    -28.8%   $   -181.67               |
|  NKE260821C00044000           10    -25.4%   $   -160.00               |
|  ... 15 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=70.5s reconcile=0.23s cancel=0.02s manage=7.73s scan=58.37s entries=3.38s
STATUS: options_morning_bot run complete (PAPER) elapsed=70.5s. run=#6395 https://github.com/28twagg-ops/TradingBot/actions/runs/31187467369
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 33 buckets closed trades, $-1,186.71 realized
STALE WARNING: 3 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=90 drop=15
Orphan rate: 8.6% (165/1924)
# Options signal frequency

_Generated 2026-08-07T10:27:12.699095_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   438 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    14 | WARN | <<<
| Total open lots             |   114 | INFO |
| Total closed lots           |  1292 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.86 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T143051Z

- UTC timestamp: `20260807T143051Z`
- GitHub run: [#6396](https://github.com/28twagg-ops/TradingBot/actions/runs/31187888934)
- Run id: `31187888934`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`102s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T10:30:56.164878-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":92.8,"phases_s":{"reconcile":0.49,"cancel":0.09,"manage":22.6,"scan":60.57,"entries":8.01,"reconcile2":0.4},"signals":120,"placed":0,"equity":142683.71,"open_positions":23,"pending_orders":9,"open_lots":112,"submitted_today":32,"filled_today":23,"unattributed_contracts":2,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S200:TTD","S202:TTD"],"github_run":"6396","github_run_id":"31187888934","status":"ok"}
```

### Live bot full output

```text
14:30:52  INFO      Mode: exits
14:30:53  INFO        Daily log -> logs/daily/2026-08-07.md
14:30:53  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
14:30:53  INFO        place_all_stops: checking 5 positions...
14:30:53  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
14:30:53  INFO        STOP already live AES @ $14.65
14:30:53  INFO        STOP already live BBY @ $79.72
14:30:53  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
14:30:53  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
14:30:53  INFO        [positions] 5/5 (5 valid)
14:30:53  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.28|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.13                                            HOLD|
|  GOOG  P&L +0.1%  $+0.05                                           HOLD|
|  ESS  P&L +0.4%  $+0.30                                            HOLD|
|  AAPL  P&L +0.8%  $+0.80                                           HOLD|
|  BBY  P&L +1.8%  $+1.68                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=114 paper_keys=yes dry_run=False
  alpaca positions=25
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T10:30:56.164878-04:00 ===

[Run context]
Paper auth OK — equity $142680.71, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] take_profit (+154.9%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 10:31:09,042 INFO   EXIT [b27|lab0027_s203_w2_1005_1045_r2|S203] stop_loss (-63.6%) SELL 1 DKNG260814P00021500 @<= 0.15
2026-08-07 10:31:09,594 INFO   EXIT [b394|lab0394_s363_w3_1045_1120_r1|S363] stop_loss (-77.9%) SELL 1 MARA260814C00011500 @<= 0.12
2026-08-07 10:31:14,536 INFO   EXIT [b264|lab0264_s403_w2_1005_1045_r1|S403] take_profit (+62.3%) SELL 1 AAPL260810C00317500 @<= 0.82
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] take_profit (+92.6%) SELL failed CVNA260807C00072000: {"code":40010001,"message":"client_order_id must be unique"}

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 120 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S200:TTD', 'S202:TTD']
Paper lab: $142733 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 62 no tradeable call, 7 already attempted today, 61 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $142,683.71                             |
|  Signals this run              120                                     |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  23                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             112                                     |
|  Broker option positions       23                                      |
|  Unattributed contracts        2 (orphan reconcile)                    |
|  Pending orders                9                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1394  buckets=285  win=40%                           |
|  Returns   avg=+20.2%  med=-36.6%  p10=-79.2%  p90=+131.9%             |
|  Realized  $+8,881.37                                                  |
|  Raw incl dropped  trades=1928  real=$+7,285.82                        |
|  Today     trades=45  avg=-55.7%  med=-70.9%  real=$-1,240.71          |
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
|  ... 277 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  7   0% -75.5 -98.2 -98.6 $   -327       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (9)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S218:UNH(4), S212:UBER(2), S406:CVX(2)  |
+------------------------------------------------------------------------+
|  b110 S212 UBER     limit=0.42                                         |
|  b111 S212 UBER     limit=0.42                                         |
|  b192 S218 UNH      limit=0.40                                         |
|  b193 S218 UNH      limit=0.40                                         |
|  b194 S218 UNH      limit=0.40                                         |
|  ... 4 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (7)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 2 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (23)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  MARA260814C00011500          11    -77.9%   $   -426.80               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  AAPL260810C00317500           4    +90.6%   $   +192.00               |
|  MARA260814C00012000           6    -81.7%   $   -188.00               |
|  NKE260828C00045000           10    -28.8%   $   -181.67               |
|  ... 15 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=92.8s reconcile=0.49s cancel=0.09s manage=22.6s scan=60.57s entries=8.01s
STATUS: options_morning_bot run complete (PAPER) elapsed=92.8s. run=#6396 https://github.com/28twagg-ops/TradingBot/actions/runs/31187888934
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 37 buckets closed trades, $-1,240.71 realized
STALE WARNING: 3 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=90 drop=15
Orphan rate: 8.6% (165/1928)
# Options signal frequency

_Generated 2026-08-07T10:32:34.494216_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   438 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    14 | WARN | <<<
| Total open lots             |   112 | INFO |
| Total closed lots           |  1296 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T143544Z

- UTC timestamp: `20260807T143544Z`
- GitHub run: [#6397](https://github.com/28twagg-ops/TradingBot/actions/runs/31188318249)
- Run id: `31188318249`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`92s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T10:35:48.640934-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":83.4,"phases_s":{"reconcile":0.17,"cancel":0.02,"manage":17.49,"scan":60.49,"entries":4.59,"reconcile2":0.24},"signals":118,"placed":0,"equity":142949.67,"open_positions":23,"pending_orders":9,"open_lots":110,"submitted_today":32,"filled_today":23,"unattributed_contracts":2,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S200:TTD","S202:TTD"],"github_run":"6397","github_run_id":"31188318249","status":"ok"}
```

### Live bot full output

```text
14:35:46  INFO      Mode: exits
14:35:46  INFO        Daily log -> logs/daily/2026-08-07.md
14:35:46  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
14:35:46  INFO        place_all_stops: checking 5 positions...
14:35:46  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
14:35:46  INFO        STOP already live AES @ $14.65
14:35:46  INFO        STOP already live BBY @ $79.72
14:35:46  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
14:35:46  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
14:35:46  INFO        [positions] 5/5 (5 valid)
14:35:46  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.16|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GOOG  P&L -0.2%  $-0.15                                           HOLD|
|  AES  P&L -0.1%  $-0.13                                            HOLD|
|  ESS  P&L +0.3%  $+0.24                                            HOLD|
|  AAPL  P&L +0.9%  $+0.83                                           HOLD|
|  BBY  P&L +1.9%  $+1.79                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=112 paper_keys=yes dry_run=False
  alpaca positions=25
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T10:35:48.640934-04:00 ===

[Run context]
Paper auth OK — equity $142945.67, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 10:35:50,398 INFO   EXIT [b263|lab0263_s403_w1_0928_1005_r2|S403] take_profit (+58.5%) SELL 1 AAPL260810C00317500 @<= 0.86
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] take_profit (+110.4%) SELL failed CVNA260807C00072000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 10:35:58,483 INFO   EXIT [b167|lab0167_s216_w2_1005_1045_r2|S216] take_profit (+59.6%) SELL 1 TSLA260810C00340000 @<= 0.76
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] take_profit (+172.5%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 10:36:04,045 INFO   EXIT [b26|lab0026_s203_w2_1005_1045_r1|S203] stop_loss (-76.6%) SELL 1 DKNG260814P00021500 @<= 0.06

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 118 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S200:TTD', 'S202:TTD']
Paper lab: $142650 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 62 no tradeable call, 14 already attempted today, 59 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $142,949.67                             |
|  Signals this run              118                                     |
|  Orders submitted (session)    32                                      |
|  Orders filled today (ledger)  23                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             110                                     |
|  Broker option positions       23                                      |
|  Unattributed contracts        2 (orphan reconcile)                    |
|  Pending orders                9                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1396  buckets=285  win=40%                           |
|  Returns   avg=+20.2%  med=-36.6%  p10=-79.2%  p90=+131.9%             |
|  Realized  $+8,882.37                                                  |
|  Raw incl dropped  trades=1930  real=$+7,286.82                        |
|  Today     trades=47  avg=-53.7%  med=-70.9%  real=$-1,239.71          |
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
|  ... 277 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  7   0% -75.5 -98.2 -98.6 $   -327       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (9)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S218:UNH(4), S212:UBER(2), S406:CVX(2)  |
+------------------------------------------------------------------------+
|  b110 S212 UBER     limit=0.42                                         |
|  b111 S212 UBER     limit=0.42                                         |
|  b192 S218 UNH      limit=0.40                                         |
|  b193 S218 UNH      limit=0.40                                         |
|  b194 S218 UNH      limit=0.40                                         |
|  ... 4 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (8)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 3 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (23)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  MARA260814C00011500          11    -77.9%   $   -426.80               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  MARA260814C00012000           6    -81.7%   $   -188.00               |
|  NKE260828C00045000           10    -27.2%   $   -171.67               |
|  NKE260821C00044000           10    -23.8%   $   -150.00               |
|  ... 15 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=83.4s reconcile=0.17s cancel=0.02s manage=17.49s scan=60.49s entries=4.59s
STATUS: options_morning_bot run complete (PAPER) elapsed=83.4s. run=#6397 https://github.com/28twagg-ops/TradingBot/actions/runs/31188318249
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 39 buckets closed trades, $-1,239.71 realized
STALE WARNING: 3 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=90 drop=15
Orphan rate: 8.6% (165/1930)
# Options signal frequency

_Generated 2026-08-07T10:37:17.600129_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   438 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    14 | WARN | <<<
| Total open lots             |   110 | INFO |
| Total closed lots           |  1298 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.14 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T144450Z

- UTC timestamp: `20260807T144450Z`
- GitHub run: [#6398](https://github.com/28twagg-ops/TradingBot/actions/runs/31188736894)
- Run id: `31188736894`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T10:35:48.640934-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":83.4,"phases_s":{"reconcile":0.17,"cancel":0.02,"manage":17.49,"scan":60.49,"entries":4.59,"reconcile2":0.24},"signals":118,"placed":0,"equity":142949.67,"open_positions":23,"pending_orders":9,"open_lots":110,"submitted_today":32,"filled_today":23,"unattributed_contracts":2,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S200:TTD","S202:TTD"],"github_run":"6397","github_run_id":"31188318249","status":"ok"}
```

### Live bot full output

```text
14:44:51  INFO      Mode: exits
14:44:51  INFO        Daily log -> logs/daily/2026-08-07.md
14:44:51  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
14:44:52  INFO        place_all_stops: checking 5 positions...
14:44:52  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
14:44:52  INFO        STOP already live AES @ $14.65
14:44:52  INFO        STOP already live BBY @ $79.72
14:44:52  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
14:44:52  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
14:44:52  INFO        [positions] 5/5 (5 valid)
14:44:52  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:44 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.85|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GOOG  P&L -0.3%  $-0.27                                           HOLD|
|  AES  P&L -0.1%  $-0.06                                            HOLD|
|  ESS  P&L +0.6%  $+0.39                                            HOLD|
|  AAPL  P&L +0.9%  $+0.82                                           HOLD|
|  BBY  P&L +1.5%  $+1.42                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=110 paper_keys=yes dry_run=False
  alpaca positions=26
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T10:44:55.099350-04:00 ===

[Run context]
Paper auth OK — equity $142384.58, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] take_profit (+176.5%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] take_profit (+151.9%) SELL failed CVNA260807C00072000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 10:45:03,001 INFO   EXIT [b166|lab0166_s216_w2_1005_1045_r1|S216] take_profit (+97.9%) SELL 1 TSLA260810C00340000 @<= 0.87
2026-08-07 10:45:09,296 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-79.2%) SELL 2 DKNG260814P00021500 @<= 0.09
2026-08-07 10:45:12,542 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+82.1%) SELL 1 META260810C00620000 @<= 0.68

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
```

---

## Run 20260807T144613Z

- UTC timestamp: `20260807T144613Z`
- GitHub run: [#6399](https://github.com/28twagg-ops/TradingBot/actions/runs/31189158939)
- Run id: `31189158939`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`80s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T10:46:17.708588-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (14 new)","elapsed_s":71.4,"phases_s":{"reconcile":0.21,"cancel":0.03,"manage":9.4,"scan":56.35,"entries":4.28,"reconcile2":0.72},"signals":140,"placed":14,"equity":142668.54,"open_positions":26,"pending_orders":13,"open_lots":114,"submitted_today":46,"filled_today":33,"unattributed_contracts":1,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S200:TTD","S202:TTD"],"github_run":"6399","github_run_id":"31189158939","status":"ok"}
```

### Live bot full output

```text
14:46:14  INFO      Mode: exits
14:46:15  INFO        Daily log -> logs/daily/2026-08-07.md
14:46:15  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
14:46:15  INFO        place_all_stops: checking 5 positions...
14:46:15  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
14:46:15  INFO        STOP already live AES @ $14.65
14:46:15  INFO        STOP already live BBY @ $79.72
14:46:15  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
14:46:15  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
14:46:15  INFO        [positions] 5/5 (5 valid)
14:46:15  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.97|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GOOG  P&L -0.3%  $-0.26                                           HOLD|
|  AES  P&L -0.1%  $-0.06                                            HOLD|
|  ESS  P&L +0.6%  $+0.43                                            HOLD|
|  AAPL  P&L +0.9%  $+0.82                                           HOLD|
|  BBY  P&L +1.6%  $+1.48                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=110 paper_keys=yes dry_run=False
  alpaca positions=25
  FLAG b166|S216|8f071924 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T10:46:17.708588-04:00 ===

[Run context]
Paper auth OK — equity $142668.54, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
  EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] take_profit (+193.3%) SELL failed CVNA260807C00072000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 10:46:21,966 INFO   EXIT [b237|lab0237_s401_w2_1005_1045_r2|S401] take_profit (+89.7%) SELL 1 META260810C00620000 @<= 0.71
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] take_profit (+229.4%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 10:46:24,290 INFO   EXIT [b239|lab0239_s401_w3_1045_1120_r2|S401] take_profit (+62.0%) SELL 1 TSLA260810C00342500 @<= 0.78
2026-08-07 10:46:26,741 INFO   EXIT [b236|lab0236_s401_w2_1005_1045_r1|S401] take_profit (+52.6%) SELL 1 META260810C00630000 @<= 0.25
  EXIT [b83|lab0083_s210_w2_1005_1045_r2|S210] take_profit (+87.0%) SELL failed CVNA260807C00073000: {"code":40010001,"message":"client_order_id must be unique"}

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 140 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S200:TTD', 'S202:TTD']
Paper lab: $142907 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 101 no tradeable call, 65 pending order
Placed 14 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $142,668.54                             |
|  Signals this run              140                                     |
|  Orders submitted (session)    46                                      |
|  Orders filled today (ledger)  33                                      |
|  Entries placed this run       14                                      |
|  Open virtual lots             114                                     |
|  Broker option positions       26                                      |
|  Unattributed contracts        1 (orphan reconcile)                    |
|  Pending orders                13                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1404  buckets=285  win=40%                           |
|  Returns   avg=+20.2%  med=-36.5%  p10=-79.2%  p90=+131.6%             |
|  Realized  $+8,963.37                                                  |
|  Raw incl dropped  trades=1938  real=$+7,367.82                        |
|  Today     trades=53  avg=-42.2%  med=-68.2%  real=$-1,120.71          |
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
|  ... 277 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  7   0% -75.5 -98.2 -98.6 $   -327       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (13)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S218:UNH(6), S212:UBER(2), S406:CVX(2)  |
+------------------------------------------------------------------------+
|  b110 S212 UBER     limit=0.42                                         |
|  b111 S212 UBER     limit=0.42                                         |
|  b192 S218 UNH      limit=0.40                                         |
|  b193 S218 UNH      limit=0.40                                         |
|  b194 S218 UNH      limit=0.40                                         |
|  ... 8 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (7)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 2 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (26)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  MARA260814C00011500          11    -77.9%   $   -426.80               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  MARA260814C00012000           6    -81.7%   $   -188.00               |
|  NKE260828C00045000           10    -27.2%   $   -171.67               |
|  NKE260821C00044000           10    -27.0%   $   -170.00               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=71.4s reconcile=0.21s cancel=0.03s manage=9.4s scan=56.35s entries=4.28s
STATUS: options_morning_bot run complete (PAPER) elapsed=71.4s. run=#6399 https://github.com/28twagg-ops/TradingBot/actions/runs/31189158939
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 42 buckets closed trades, $-1,120.71 realized
STALE WARNING: 3 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=90 drop=15
Orphan rate: 8.6% (166/1938)
# Options signal frequency

_Generated 2026-08-07T10:47:34.643892_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   438 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    16 | WARN | <<<
| Total open lots             |   114 | INFO |
| Total closed lots           |  1305 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.97 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T145043Z

- UTC timestamp: `20260807T145043Z`
- GitHub run: [#6400](https://github.com/28twagg-ops/TradingBot/actions/runs/31189578404)
- Run id: `31189578404`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`98s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T10:50:48.773618-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":88.8,"phases_s":{"reconcile":1.64,"cancel":0.09,"manage":14.16,"scan":57.66,"entries":12.64,"reconcile2":2.06},"signals":140,"placed":1,"equity":142838.77,"open_positions":26,"pending_orders":12,"open_lots":116,"submitted_today":47,"filled_today":35,"unattributed_contracts":4,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S200:TTD","S202:TTD"],"github_run":"6400","github_run_id":"31189578404","status":"ok"}
```

### Live bot full output

```text
14:50:45  INFO      Mode: exits
14:50:46  INFO        Daily log -> logs/daily/2026-08-07.md
14:50:46  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
14:50:46  INFO        place_all_stops: checking 5 positions...
14:50:46  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
14:50:46  INFO        STOP already live AES @ $14.65
14:50:46  INFO        STOP already live BBY @ $79.72
14:50:46  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
14:50:46  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
14:50:46  INFO        [positions] 5/5 (5 valid)
14:50:46  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.70|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  GOOG  P&L -0.4%  $-0.40                                           HOLD|
|  AES  P&L -0.0%  $-0.03                                            HOLD|
|  ESS  P&L +0.7%  $+0.52                                            HOLD|
|  AAPL  P&L +0.8%  $+0.72                                           HOLD|
|  BBY  P&L +1.4%  $+1.34                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=114 paper_keys=yes dry_run=False
  alpaca positions=29
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T10:50:48.773618-04:00 ===

[Run context]
Paper auth OK — equity $142856.77, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 10:50:52,839 INFO   EXIT [b238|lab0238_s401_w3_1045_1120_r1|S401] take_profit (+83.1%) SELL 1 TSLA260810C00342500 @<= 0.87
2026-08-07 10:50:56,137 INFO   EXIT [b409|lab0409_s364_w3_1045_1120_r2|S364] stop_loss (-75.9%) SELL 1 MARA260814C00011500 @<= 0.09
2026-08-07 10:50:58,464 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+59.0%) SELL 1 META260810C00620000 @<= 0.63
2026-08-07 10:51:02,804 INFO   EXIT [b85|lab0085_s210_w3_1045_1120_r2|S210] take_profit (+175.6%) SELL 1 CVNA260807C00072000 @<= 0.90
  EXIT [b83|lab0083_s210_w2_1005_1045_r2|S210] take_profit (+69.6%) SELL failed CVNA260807C00073000: {"code":40010001,"message":"client_order_id must be unique"}
  EXIT [b114|lab0114_s212_w4_1120_1135_r1|S212] take_profit (+211.8%) SELL failed CVNA260807C00071000: {"code":40010001,"message":"client_order_id must be unique"}

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 140 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S200:TTD', 'S202:TTD']
Paper lab: $142610 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 94 no tradeable call, 37 already attempted today, 33 pending order
Placed 1 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $142,838.77                             |
|  Signals this run              140                                     |
|  Orders submitted (session)    47                                      |
|  Orders filled today (ledger)  35                                      |
|  Entries placed this run       1                                       |
|  Open virtual lots             116                                     |
|  Broker option positions       26                                      |
|  Unattributed contracts        4 (orphan reconcile)                    |
|  Pending orders                12                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1428  buckets=286  win=39%                           |
|  Returns   avg=+19.6%  med=-36.6%  p10=-79.4%  p90=+130.5%             |
|  Realized  $+9,024.31                                                  |
|  Raw incl dropped  trades=1962  real=$+7,428.76                        |
|  Today     trades=57  avg=-37.3%  med=-68.2%  real=$-1,091.71          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b238 lab0238_s401_w3_10  9 100% +255.2 +273.1 +815.4 $   +877         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b410 lab0410_s364_w4_11  3 100% +168.7 +233.3 +233.3 $   +183         |
|  ... 278 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  7   0% -75.5 -98.2 -98.6 $   -327       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (12)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S218:UNH(4), S212:UBER(2), S406:CVX(2)  |
+------------------------------------------------------------------------+
|  b110 S212 UBER     limit=0.42                                         |
|  b111 S212 UBER     limit=0.42                                         |
|  b192 S218 UNH      limit=0.40                                         |
|  b193 S218 UNH      limit=0.40                                         |
|  b194 S218 UNH      limit=0.40                                         |
|  ... 7 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (7)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 2 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (26)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  MARA260814C00011500           9    -75.9%   $   -340.20               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  NKE260821C00044000           10    -33.3%   $   -210.00               |
|  MARA260814C00012000           6    -81.7%   $   -188.00               |
|  NKE260828C00045000           10    -25.6%   $   -161.67               |
|  ... 18 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=88.8s reconcile=1.64s cancel=0.09s manage=14.16s scan=57.66s entries=12.64s
STATUS: options_morning_bot run complete (PAPER) elapsed=88.8s. run=#6400 https://github.com/28twagg-ops/TradingBot/actions/runs/31189578404
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 46 buckets closed trades, $-1,091.71 realized
STALE WARNING: 3 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=87 drop=18
Orphan rate: 9.0% (176/1962)
# Options signal frequency

_Generated 2026-08-07T10:52:23.184976_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   438 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   116 | INFO |
| Total closed lots           |  1319 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.7 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T151053Z

- UTC timestamp: `20260807T151053Z`
- GitHub run: [#6404](https://github.com/28twagg-ops/TradingBot/actions/runs/31191246312)
- Run id: `31191246312`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`91s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T11:10:58.155805-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (5 new)","elapsed_s":82.5,"phases_s":{"reconcile":0.54,"cancel":0.05,"manage":11.16,"scan":58.77,"entries":11.07,"reconcile2":0.38},"signals":141,"placed":5,"equity":142598.82,"open_positions":27,"pending_orders":8,"open_lots":121,"submitted_today":52,"filled_today":44,"unattributed_contracts":2,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S200:TTD","S202:TTD"],"github_run":"6404","github_run_id":"31191246312","status":"ok"}
```

### Live bot full output

```text
15:10:55  INFO      Mode: exits
15:10:55  INFO        Daily log -> logs/daily/2026-08-07.md
15:10:55  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
15:10:55  INFO        place_all_stops: checking 5 positions...
15:10:55  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
15:10:55  INFO        STOP already live AES @ $14.65
15:10:55  INFO        STOP already live BBY @ $79.72
15:10:55  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
15:10:55  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
15:10:55  INFO        [positions] 5/5 (5 valid)
15:10:55  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.26|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.06                                            HOLD|
|  GOOG  P&L +0.3%  $+0.28                                           HOLD|
|  ESS  P&L +0.4%  $+0.31                                            HOLD|
|  AAPL  P&L +0.8%  $+0.76                                           HOLD|
|  BBY  P&L +1.5%  $+1.40                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=116 paper_keys=yes dry_run=False
  alpaca positions=28
  FLAG b0|ORPHAN|81fef23e missing from Alpaca
  FLAG b0|ORPHAN|14061cc7 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T11:10:58.155805-04:00 ===

[Run context]
Paper auth OK — equity $142598.82, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 11:11:01,783 INFO   EXIT [b165|lab0165_s216_w1_0928_1005_r2|S216] take_profit (+55.7%) SELL 1 TSLA260810C00342500 @<= 0.71
2026-08-07 11:11:06,662 INFO   EXIT [b115|lab0115_s212_w4_1120_1135_r2|S212] take_profit (+252.9%) SELL 1 CVNA260807C00071000 @<= 1.81
2026-08-07 11:11:08,782 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-75.7%) SELL 4 COIN260807C00160000 @<= 0.08
2026-08-07 11:11:08,998 INFO   EXIT [b309|lab0309_s354_w3_1045_1120_r2|S354] stop_loss (-75.9%) SELL 1 MARA260814C00011500 @<= 0.09
  EXIT [b83|lab0083_s210_w2_1005_1045_r2|S210] take_profit (+139.1%) SELL failed CVNA260807C00073000: {"code":40010001,"message":"client_order_id must be unique"}

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 141 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S200:TTD', 'S202:TTD']
Paper lab: $142567 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 94 no tradeable call, 40 already attempted today, 63 pending order
Placed 5 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $142,598.82                             |
|  Signals this run              141                                     |
|  Orders submitted (session)    52                                      |
|  Orders filled today (ledger)  44                                      |
|  Entries placed this run       5                                       |
|  Open virtual lots             121                                     |
|  Broker option positions       27                                      |
|  Unattributed contracts        2 (orphan reconcile)                    |
|  Pending orders                8                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1433  buckets=286  win=39%                           |
|  Returns   avg=+19.5%  med=-36.7%  p10=-79.3%  p90=+130.1%             |
|  Realized  $+9,012.47                                                  |
|  Raw incl dropped  trades=1967  real=$+7,416.92                        |
|  Today     trades=62  avg=-34.5%  med=-66.6%  real=$-1,103.55          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  2 100% +320.0 +320.0 +320.0 $   +160         |
|  b238 lab0238_s401_w3_10  9 100% +255.2 +273.1 +815.4 $   +877         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b410 lab0410_s364_w4_11  3 100% +168.7 +233.3 +233.3 $   +183         |
|  ... 278 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b108 lab0108_s212_w1_09  7   0% -75.5 -98.2 -98.6 $   -327       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (8)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S212:UBER(2), S364:CVX(2), S412:CVX(2)  |
+------------------------------------------------------------------------+
|  b110 S212 UBER     limit=0.42                                         |
|  b111 S212 UBER     limit=0.42                                         |
|  b408 S364 CVX      limit=0.52                                         |
|  b916 S412 CVX      limit=0.52                                         |
|  b917 S412 CVX      limit=0.52                                         |
|  ... 3 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (8)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 3 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (27)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  MARA260814C00011500           8    -75.9%   $   -302.40               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           10    -39.7%   $   -250.00               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  NKE260828C00045000           10    -35.1%   $   -221.67               |
|  MARA260814C00012000           6    -81.7%   $   -188.00               |
|  ... 19 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=82.5s reconcile=0.54s cancel=0.05s manage=11.16s scan=58.77s entries=11.07s
STATUS: options_morning_bot run complete (PAPER) elapsed=82.5s. run=#6404 https://github.com/28twagg-ops/TradingBot/actions/runs/31191246312
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 49 buckets closed trades, $-1,103.55 realized
STALE WARNING: 3 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=87 drop=18
Orphan rate: 9.0% (178/1967)
# Options signal frequency

_Generated 2026-08-07T11:12:26.502549_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   438 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    14 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  1322 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.26 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T152126Z

- UTC timestamp: `20260807T152126Z`
- GitHub run: [#6407](https://github.com/28twagg-ops/TradingBot/actions/runs/31192070366)
- Run id: `31192070366`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`91s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T11:21:31.045437-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (7 new)","elapsed_s":81.9,"phases_s":{"reconcile":0.18,"cancel":0.02,"manage":9.7,"scan":63.68,"entries":6.39,"reconcile2":1.52},"signals":141,"placed":7,"equity":142046.56,"open_positions":28,"pending_orders":8,"open_lots":122,"submitted_today":59,"filled_today":51,"unattributed_contracts":4,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S200:TTD","S202:TTD"],"github_run":"6407","github_run_id":"31192070366","status":"ok"}
```

### Live bot full output

```text
15:21:27  INFO      Mode: exits
15:21:28  INFO        Daily log -> logs/daily/2026-08-07.md
15:21:28  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
15:21:28  INFO        place_all_stops: checking 5 positions...
15:21:28  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
15:21:28  INFO        STOP already live AES @ $14.65
15:21:28  INFO        STOP already live BBY @ $79.72
15:21:28  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
15:21:28  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
15:21:28  INFO        [positions] 5/5 (5 valid)
15:21:28  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:21 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.98|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.0%  $-0.03                                            HOLD|
|  GOOG  P&L +0.2%  $+0.18                                           HOLD|
|  ESS  P&L +0.4%  $+0.29                                            HOLD|
|  AAPL  P&L +0.5%  $+0.50                                           HOLD|
|  BBY  P&L +1.6%  $+1.48                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=121 paper_keys=yes dry_run=False
  alpaca positions=30
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T11:21:31.045437-04:00 ===

[Run context]
Paper auth OK — equity $142046.56, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 11:21:33,231 INFO   EXIT [b819|lab0819_s405_w3_1045_1120_r2|S405] stop_loss (-75.7%) SELL 1 COIN260807C00160000 @<= 0.04
2026-08-07 11:21:34,667 INFO   EXIT [b308|lab0308_s354_w3_1045_1120_r1|S354] stop_loss (-77.9%) SELL 1 MARA260814C00011500 @<= 0.12
2026-08-07 11:21:37,214 INFO   EXIT [b164|lab0164_s216_w1_0928_1005_r1|S216] take_profit (+55.7%) SELL 1 TSLA260810C00342500 @<= 0.75
2026-08-07 11:21:40,505 INFO   EXIT [b325|lab0325_s356_w3_1045_1120_r2|S356] stop_loss (-51.5%) SELL 1 AAPL260814C00330000 @<= 0.26

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 141 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S200:TTD', 'S202:TTD']
Paper lab: $142156 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 128 no tradeable call, 23 pending order
Placed 7 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $142,046.56                             |
|  Signals this run              141                                     |
|  Orders submitted (session)    59                                      |
|  Orders filled today (ledger)  51                                      |
|  Entries placed this run       7                                       |
|  Open virtual lots             122                                     |
|  Broker option positions       28                                      |
|  Unattributed contracts        4 (orphan reconcile)                    |
|  Pending orders                8                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1452  buckets=289  win=39%                           |
|  Returns   avg=+19.3%  med=-37.0%  p10=-79.6%  p90=+131.0%             |
|  Realized  $+8,815.73                                                  |
|  Raw incl dropped  trades=1986  real=$+7,220.18                        |
|  Today     trades=66  avg=-34.3%  med=-66.6%  real=$-1,206.64          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b238 lab0238_s401_w3_10  9 100% +255.2 +273.1 +815.4 $   +877         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b410 lab0410_s364_w4_11  3 100% +168.7 +233.3 +233.3 $   +183         |
|  ... 281 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (8)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S212:UBER(3), S364:CVX(2), S412:CVX(2)  |
+------------------------------------------------------------------------+
|  b110 S212 UBER     limit=0.42                                         |
|  b111 S212 UBER     limit=0.42                                         |
|  b408 S364 CVX      limit=0.52                                         |
|  b916 S412 CVX      limit=0.52                                         |
|  b917 S412 CVX      limit=0.52                                         |
|  ... 3 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (8)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 3 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (28)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  MARA260814C00011500           8    -77.9%   $   -310.40               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  NKE260821C00044000           10    -38.1%   $   -240.00               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  NKE260828C00045000           10    -35.1%   $   -221.67               |
|  MARA260814C00012000           6    -81.7%   $   -188.00               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=81.9s reconcile=0.18s cancel=0.02s manage=9.7s scan=63.68s entries=6.39s
STATUS: options_morning_bot run complete (PAPER) elapsed=81.9s. run=#6407 https://github.com/28twagg-ops/TradingBot/actions/runs/31192070366
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 52 buckets closed trades, $-1,206.64 realized
STALE WARNING: 2 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=87 drop=18
Orphan rate: 9.4% (186/1986)
# Options signal frequency

_Generated 2026-08-07T11:22:58.486606_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   437 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   122 | INFO |
| Total closed lots           |  1333 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.99 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T152555Z

- UTC timestamp: `20260807T152555Z`
- GitHub run: [#6408](https://github.com/28twagg-ops/TradingBot/actions/runs/31192492221)
- Run id: `31192492221`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`88s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T11:25:59.616881-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (4 new)","elapsed_s":80.9,"phases_s":{"reconcile":2.06,"cancel":0.14,"manage":15.03,"scan":44.51,"entries":17.96,"reconcile2":0.54},"signals":144,"placed":4,"equity":142500.27,"open_positions":28,"pending_orders":11,"open_lots":120,"submitted_today":63,"filled_today":52,"unattributed_contracts":4,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S200:TTD","S202:TTD"],"github_run":"6408","github_run_id":"31192492221","status":"ok"}
```

### Live bot full output

```text
15:25:56  INFO      Mode: exits
15:25:56  INFO        Daily log -> logs/daily/2026-08-07.md
15:25:56  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
15:25:56  INFO        place_all_stops: checking 5 positions...
15:25:56  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
15:25:57  INFO        STOP already live AES @ $14.65
15:25:57  INFO        STOP already live BBY @ $79.72
15:25:57  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
15:25:57  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
15:25:57  INFO        [positions] 5/5 (5 valid)
15:25:57  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.86|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.06                                            HOLD|
|  GOOG  P&L +0.2%  $+0.23                                           HOLD|
|  ESS  P&L +0.4%  $+0.29                                            HOLD|
|  AAPL  P&L +0.6%  $+0.54                                           HOLD|
|  BBY  P&L +1.4%  $+1.29                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=122 paper_keys=yes dry_run=False
  alpaca positions=30
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T11:25:59.616881-04:00 ===

[Run context]
Paper auth OK — equity $142500.27, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 11:26:05,481 INFO   EXIT [b81|lab0081_s210_w1_0928_1005_r2|S210] take_profit (+59.3%) SELL 1 NVDA260810C00230000 @<= 0.44
  EXIT [b83|lab0083_s210_w2_1005_1045_r2|S210] take_profit (+65.2%) SELL failed CVNA260807C00073000: {"code":40010001,"message":"client_order_id must be unique"}
2026-08-07 11:26:07,592 INFO   EXIT [b407|lab0407_s364_w2_1005_1045_r2|S364] stop_loss (-73.9%) SELL 1 MARA260814C00011500 @<= 0.14
2026-08-07 11:26:09,299 INFO   EXIT [b240|lab0240_s401_w4_1120_1135_r1|S401] take_profit (+125.2%) SELL 1 TSLA260810C00342500 @<= 1.03

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 144 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S200:TTD', 'S202:TTD']
Paper lab: $142553 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 104 no tradeable call, 18 already attempted today, 63 pending order
Placed 4 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $142,500.27                             |
|  Signals this run              144                                     |
|  Orders submitted (session)    63                                      |
|  Orders filled today (ledger)  52                                      |
|  Entries placed this run       4                                       |
|  Open virtual lots             120                                     |
|  Broker option positions       28                                      |
|  Unattributed contracts        4 (orphan reconcile)                    |
|  Pending orders                11                                      |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1461  buckets=289  win=39%                           |
|  Returns   avg=+19.2%  med=-37.0%  p10=-79.6%  p90=+130.3%             |
|  Realized  $+8,800.73                                                  |
|  Raw incl dropped  trades=1995  real=$+7,205.18                        |
|  Today     trades=69  avg=-31.5%  med=-65.4%  real=$-1,170.64          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b238 lab0238_s401_w3_10  9 100% +255.2 +273.1 +815.4 $   +877         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b410 lab0410_s364_w4_11  3 100% +168.7 +233.3 +233.3 $   +183         |
|  ... 281 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (11)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S212:UBER(3), S364:CVX(2), S412:CVX(2)  |
+------------------------------------------------------------------------+
|  b110 S212 UBER     limit=0.42                                         |
|  b111 S212 UBER     limit=0.42                                         |
|  b408 S364 CVX      limit=0.52                                         |
|  b916 S412 CVX      limit=0.52                                         |
|  b917 S412 CVX      limit=0.52                                         |
|  ... 6 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (8)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 3 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (28)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  MARA260814C00011500           7    -73.9%   $   -257.60               |
|  NKE260821C00044000           10    -38.1%   $   -240.00               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  NKE260828C00045000           10    -35.1%   $   -221.67               |
|  MARA260814C00012000           6    -79.1%   $   -182.00               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=80.9s reconcile=2.06s cancel=0.14s manage=15.03s scan=44.51s entries=17.96s
STATUS: options_morning_bot run complete (PAPER) elapsed=80.9s. run=#6408 https://github.com/28twagg-ops/TradingBot/actions/runs/31192492221
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 55 buckets closed trades, $-1,170.64 realized
STALE WARNING: 2 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=86 drop=19
Orphan rate: 9.3% (186/1995)
# Options signal frequency

_Generated 2026-08-07T11:27:24.960019_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   437 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   120 | INFO |
| Total closed lots           |  1342 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.85 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T153055Z

- UTC timestamp: `20260807T153055Z`
- GitHub run: [#6409](https://github.com/28twagg-ops/TradingBot/actions/runs/31192910251)
- Run id: `31192910251`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`102s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T11:31:01.043051-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (1 new)","elapsed_s":95.0,"phases_s":{"reconcile":0.55,"cancel":0.15,"manage":27.53,"scan":50.06,"entries":15.43,"reconcile2":0.61},"signals":142,"placed":1,"equity":142679.29,"open_positions":30,"pending_orders":9,"open_lots":121,"submitted_today":64,"filled_today":55,"unattributed_contracts":4,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S200:TTD","S202:TTD"],"github_run":"6409","github_run_id":"31192910251","status":"ok"}
```

### Live bot full output

```text
15:30:57  INFO      Mode: exits
15:30:57  INFO        Daily log -> logs/daily/2026-08-07.md
15:30:57  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
15:30:58  INFO        place_all_stops: checking 5 positions...
15:30:58  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
15:30:58  INFO        STOP already live AES @ $14.65
15:30:58  INFO        STOP already live BBY @ $79.72
15:30:58  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
15:30:58  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
15:30:58  INFO        [positions] 5/5 (5 valid)
15:30:58  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.18|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.06                                            HOLD|
|  ESS  P&L +0.2%  $+0.16                                            HOLD|
|  GOOG  P&L +0.3%  $+0.33                                           HOLD|
|  AAPL  P&L +0.6%  $+0.55                                           HOLD|
|  BBY  P&L +1.7%  $+1.64                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=120 paper_keys=yes dry_run=False
  alpaca positions=32
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T11:31:01.043051-04:00 ===

[Run context]
Paper auth OK — equity $142679.29, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 11:31:20,168 INFO   EXIT [b237|lab0237_s401_w2_1005_1045_r2|S401] take_profit (+156.7%) SELL 1 TSLA260810C00342500 @<= 1.22
2026-08-07 11:31:21,728 INFO   EXIT [b82|lab0082_s210_w2_1005_1045_r1|S210] take_profit (+66.7%) SELL 1 NVDA260810C00230000 @<= 0.42

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 142 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S200:TTD', 'S202:TTD']
Paper lab: $142690 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 96 no tradeable call, 18 already attempted today, 83 pending order
Placed 1 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $142,679.29                             |
|  Signals this run              142                                     |
|  Orders submitted (session)    64                                      |
|  Orders filled today (ledger)  55                                      |
|  Entries placed this run       1                                       |
|  Open virtual lots             121                                     |
|  Broker option positions       30                                      |
|  Unattributed contracts        4 (orphan reconcile)                    |
|  Pending orders                9                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1463  buckets=289  win=39%                           |
|  Returns   avg=+19.4%  med=-37.0%  p10=-79.6%  p90=+130.9%             |
|  Realized  $+8,893.73                                                  |
|  Raw incl dropped  trades=1997  real=$+7,298.18                        |
|  Today     trades=71  avg=-27.4%  med=-62.9%  real=$-1,077.64          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b238 lab0238_s401_w3_10  9 100% +255.2 +273.1 +815.4 $   +877         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b410 lab0410_s364_w4_11  3 100% +168.7 +233.3 +233.3 $   +183         |
|  ... 281 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (9)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S212:UBER(2), S364:CVX(2), S412:CVX(2)  |
+------------------------------------------------------------------------+
|  b110 S212 UBER     limit=0.42                                         |
|  b111 S212 UBER     limit=0.42                                         |
|  b408 S364 CVX      limit=0.52                                         |
|  b916 S412 CVX      limit=0.52                                         |
|  b917 S412 CVX      limit=0.52                                         |
|  ... 4 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  PENDING EXITS (8)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 3 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (30)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  MARA260814C00011500           7    -73.9%   $   -257.60               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  NKE260828C00045000           10    -35.1%   $   -221.67               |
|  NKE260821C00044000           10    -34.9%   $   -220.00               |
|  MARA260814C00012000           6    -79.1%   $   -182.00               |
|  ... 22 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=95.0s reconcile=0.55s cancel=0.15s manage=27.53s scan=50.06s entries=15.43s
STATUS: options_morning_bot run complete (PAPER) elapsed=95.0s. run=#6409 https://github.com/28twagg-ops/TradingBot/actions/runs/31192910251
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 56 buckets closed trades, $-1,077.64 realized
STALE WARNING: 2 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=86 drop=19
Orphan rate: 9.3% (186/1997)
# Options signal frequency

_Generated 2026-08-07T11:32:40.559498_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   437 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  1344 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.18 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T153548Z

- UTC timestamp: `20260807T153548Z`
- GitHub run: [#6410](https://github.com/28twagg-ops/TradingBot/actions/runs/31193337573)
- Run id: `31193337573`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`87s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T11:35:52.991565-04:00","date":"2026-08-07","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":80.7,"phases_s":{"reconcile":0.63,"cancel":0.13,"manage":17.29,"scan":47.8,"entries":13.79,"reconcile2":0.5},"signals":142,"placed":0,"equity":142602.95,"open_positions":30,"pending_orders":4,"open_lots":122,"submitted_today":64,"filled_today":60,"unattributed_contracts":4,"top_signals":["S165:TTD","S164:TTD","S168:TTD","S167:TTD","S166:TTD","S163:TTD","S200:TTD","S202:TTD"],"github_run":"6410","github_run_id":"31193337573","status":"ok"}
```

### Live bot full output

```text
15:35:49  INFO      Mode: exits
15:35:50  INFO        Daily log -> logs/daily/2026-08-07.md
15:35:50  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
15:35:50  INFO        place_all_stops: checking 5 positions...
15:35:50  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
15:35:50  INFO        STOP already live AES @ $14.65
15:35:50  INFO        STOP already live BBY @ $79.72
15:35:50  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
15:35:50  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
15:35:51  INFO        [positions] 5/5 (5 valid)
15:35:51  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.76|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.06                                            HOLD|
|  GOOG  P&L +0.2%  $+0.18                                           HOLD|
|  ESS  P&L +0.2%  $+0.15                                            HOLD|
|  AAPL  P&L +0.3%  $+0.31                                           HOLD|
|  BBY  P&L +1.8%  $+1.67                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=121 paper_keys=yes dry_run=False
  alpaca positions=32
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T11:35:52.991565-04:00 ===

[Run context]
Paper auth OK — equity $142602.95, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 11:36:07,246 INFO   EXIT [b80|lab0080_s210_w1_0928_1005_r1|S210] take_profit (+66.7%) SELL 1 NVDA260810C00230000 @<= 0.43
2026-08-07 11:36:08,282 INFO   EXIT [b324|lab0324_s356_w3_1045_1120_r1|S356] stop_loss (-54.8%) SELL 1 AAPL260814C00330000 @<= 0.24

[Scan + entries]
Scanning 117 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419] …
Fetched daily bars for 114/117 symbols
Found 142 signal(s); top: ['S165:TTD', 'S164:TTD', 'S168:TTD', 'S167:TTD', 'S166:TTD', 'S163:TTD', 'S200:TTD', 'S202:TTD']
Paper lab: $142288 broker equity -> 1024 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 96 no tradeable call, 48 already attempted today
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $142,602.95                             |
|  Signals this run              142                                     |
|  Orders submitted (session)    64                                      |
|  Orders filled today (ledger)  60                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             122                                     |
|  Broker option positions       30                                      |
|  Unattributed contracts        4 (orphan reconcile)                    |
|  Pending orders                4                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1467  buckets=290  win=40%                           |
|  Returns   avg=+19.5%  med=-37.0%  p10=-79.6%  p90=+130.6%             |
|  Realized  $+8,992.73                                                  |
|  Raw incl dropped  trades=2001  real=$+7,397.18                        |
|  Today     trades=73  avg=-26.1%  med=-61.7%  real=$-1,082.64          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b238 lab0238_s401_w3_10  9 100% +255.2 +273.1 +815.4 $   +877         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b410 lab0410_s364_w4_11  3 100% +168.7 +233.3 +233.3 $   +183         |
|  ... 282 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (4)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S364:CVX(2), S412:CVX(2)                |
+------------------------------------------------------------------------+
|  b408 S364 CVX      limit=0.52                                         |
|  b916 S412 CVX      limit=0.52                                         |
|  b917 S412 CVX      limit=0.52                                         |
|  b409 S364 CVX      limit=0.53                                         |
+========================================================================+
+========================================================================+
|  PENDING EXITS (8)                                                     |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 3 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (30)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  MARA260814C00011500           7    -73.9%   $   -257.60               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  NKE260821C00044000           10    -34.9%   $   -220.00               |
|  NKE260828C00045000           10    -33.5%   $   -211.67               |
|  MARA260814C00012000           6    -79.1%   $   -182.00               |
|  ... 22 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=80.7s reconcile=0.63s cancel=0.13s manage=17.29s scan=47.8s entries=13.79s
STATUS: options_morning_bot run complete (PAPER) elapsed=80.7s. run=#6410 https://github.com/28twagg-ops/TradingBot/actions/runs/31193337573
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 57 buckets closed trades, $-1,082.64 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=86 drop=19
Orphan rate: 9.3% (186/2001)
# Options signal frequency

_Generated 2026-08-07T11:37:18.077954_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   436 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   122 | INFO |
| Total closed lots           |  1348 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.84 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T154043Z

- UTC timestamp: `20260807T154043Z`
- GitHub run: [#6411](https://github.com/28twagg-ops/TradingBot/actions/runs/31193755451)
- Run id: `31193755451`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`20s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T11:40:47.456327-04:00","date":"2026-08-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":11.9,"phases_s":{"reconcile":0.13,"cancel":0.08,"manage":11.2},"signals":0,"placed":0,"equity":142326.91,"open_positions":29,"pending_orders":4,"open_lots":122,"submitted_today":64,"filled_today":60,"unattributed_contracts":2,"top_signals":[],"github_run":"6411","github_run_id":"31193755451","status":"ok"}
```

### Live bot full output

```text
15:40:44  INFO      Mode: exits
15:40:45  INFO        Daily log -> logs/daily/2026-08-07.md
15:40:45  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
15:40:45  INFO        place_all_stops: checking 5 positions...
15:40:45  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
15:40:45  INFO        STOP already live AES @ $14.65
15:40:45  INFO        STOP already live BBY @ $79.72
15:40:45  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
15:40:45  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
15:40:45  INFO        [positions] 5/5 (5 valid)
15:40:45  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.05|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.0%  $-0.03                                            HOLD|
|  GOOG  P&L +0.2%  $+0.23                                           HOLD|
|  ESS  P&L +0.3%  $+0.19                                            HOLD|
|  AAPL  P&L +0.4%  $+0.34                                           HOLD|
|  BBY  P&L +1.9%  $+1.76                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=122 paper_keys=yes dry_run=False
  alpaca positions=32
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T11:40:47.456327-04:00 ===

[Run context]
Paper auth OK — equity $142326.91, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
Cancelled 4 unfilled LAB entry order(s).
2026-08-07 11:40:57,819 INFO   EXIT [b0|orphan_reconcile|ORPHAN] take_profit (+55.6%) SELL 1 NVDA260810C00230000 @<= 0.43
2026-08-07 11:40:58,786 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-53.1%) SELL 2 AAPL260814C00330000 @<= 0.25

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $142,326.91                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    64                                      |
|  Orders filled today (ledger)  60                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             122                                     |
|  Broker option positions       29                                      |
|  Unattributed contracts        2 (orphan reconcile)                    |
|  Pending orders                4                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1467  buckets=290  win=40%                           |
|  Returns   avg=+19.5%  med=-37.0%  p10=-79.6%  p90=+130.6%             |
|  Realized  $+8,992.73                                                  |
|  Raw incl dropped  trades=2001  real=$+7,397.18                        |
|  Today     trades=73  avg=-26.1%  med=-61.7%  real=$-1,082.64          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b238 lab0238_s401_w3_10  9 100% +255.2 +273.1 +815.4 $   +877         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b410 lab0410_s364_w4_11  3 100% +168.7 +233.3 +233.3 $   +183         |
|  ... 282 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING ORDERS (4)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S364:CVX(2), S412:CVX(2)                |
+------------------------------------------------------------------------+
|  b408 S364 CVX      limit=0.52                                         |
|  b916 S412 CVX      limit=0.52                                         |
|  b917 S412 CVX      limit=0.52                                         |
|  b409 S364 CVX      limit=0.53                                         |
+========================================================================+
+========================================================================+
|  PENDING EXITS (10)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 5 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (29)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  MARA260814C00011500           7    -73.9%   $   -257.60               |
|  AMD260807C00537500            4    -98.3%   $   -225.09               |
|  NKE260821C00044000           10    -33.3%   $   -210.00               |
|  NKE260828C00045000           10    -30.3%   $   -191.67               |
|  MARA260814C00012000           6    -81.7%   $   -188.00               |
|  ... 21 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=11.9s reconcile=0.13s cancel=0.08s manage=11.2s
STATUS: options_morning_bot run complete (PAPER) elapsed=11.9s. run=#6411 https://github.com/28twagg-ops/TradingBot/actions/runs/31193755451
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 57 buckets closed trades, $-1,082.64 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=86 drop=19
Orphan rate: 9.3% (186/2001)
# Options signal frequency

_Generated 2026-08-07T11:41:04.841847_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   436 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    15 | WARN | <<<
| Total open lots             |   122 | INFO |
| Total closed lots           |  1348 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=474.05 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T154546Z

- UTC timestamp: `20260807T154546Z`
- GitHub run: [#6412](https://github.com/28twagg-ops/TradingBot/actions/runs/31194166682)
- Run id: `31194166682`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`18s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T11:45:51.013431-04:00","date":"2026-08-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":8.5,"phases_s":{"reconcile":0.17,"cancel":0.04,"manage":7.89},"signals":0,"placed":0,"equity":142107.54,"open_positions":29,"pending_orders":0,"open_lots":121,"submitted_today":64,"filled_today":60,"unattributed_contracts":5,"top_signals":[],"github_run":"6412","github_run_id":"31194166682","status":"ok"}
```

### Live bot full output

```text
15:45:48  INFO      Mode: exits
15:45:48  INFO        Daily log -> logs/daily/2026-08-07.md
15:45:48  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
15:45:48  INFO        place_all_stops: checking 5 positions...
15:45:48  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
15:45:48  INFO        STOP already live AES @ $14.65
15:45:48  INFO        STOP already live BBY @ $79.72
15:45:48  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
15:45:48  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
15:45:48  INFO        [positions] 5/5 (5 valid)
15:45:48  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.93|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.06                                            HOLD|
|  ESS  P&L +0.3%  $+0.19                                            HOLD|
|  GOOG  P&L +0.3%  $+0.28                                           HOLD|
|  AAPL  P&L +0.3%  $+0.30                                           HOLD|
|  BBY  P&L +1.8%  $+1.66                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=122 paper_keys=yes dry_run=False
  alpaca positions=31
  FLAG b0|ORPHAN|278174ae missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T11:45:51.013431-04:00 ===

[Run context]
Paper auth OK — equity $142107.54, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 11:45:56,581 INFO   EXIT [b845|lab0845_s407_w2_1005_1045_r2|S407] stop_loss (-60.0%) SELL 1 CVX260814C00200000 @<= 0.05

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $142,107.54                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    64                                      |
|  Orders filled today (ledger)  60                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             121                                     |
|  Broker option positions       29                                      |
|  Unattributed contracts        5 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1468  buckets=290  win=40%                           |
|  Returns   avg=+19.4%  med=-37.0%  p10=-79.6%  p90=+130.5%             |
|  Realized  $+8,941.03                                                  |
|  Raw incl dropped  trades=2002  real=$+7,345.48                        |
|  Today     trades=74  avg=-26.4%  med=-60.8%  real=$-1,134.34          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b238 lab0238_s401_w3_10  9 100% +255.2 +273.1 +815.4 $   +877         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b410 lab0410_s364_w4_11  3 100% +168.7 +233.3 +233.3 $   +183         |
|  ... 282 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (10)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 5 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (29)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  MARA260814C00011500           7    -73.9%   $   -257.60               |
|  AMD260807C00537500            4   -100.0%   $   -229.09               |
|  NKE260821C00044000           10    -33.3%   $   -210.00               |
|  NKE260828C00045000           10    -30.3%   $   -191.67               |
|  MARA260814C00012000           6    -81.7%   $   -188.00               |
|  ... 21 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=8.5s reconcile=0.17s cancel=0.04s manage=7.89s
STATUS: options_morning_bot run complete (PAPER) elapsed=8.5s. run=#6412 https://github.com/28twagg-ops/TradingBot/actions/runs/31194166682
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 57 buckets closed trades, $-1,134.34 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=86 drop=19
Orphan rate: 9.3% (187/2002)
# Options signal frequency

_Generated 2026-08-07T11:46:05.154870_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   436 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    14 | WARN | <<<
| Total open lots             |   121 | INFO |
| Total closed lots           |  1348 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.93 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T155044Z

- UTC timestamp: `20260807T155044Z`
- GitHub run: [#6413](https://github.com/28twagg-ops/TradingBot/actions/runs/31194579676)
- Run id: `31194579676`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`25s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T11:50:50.146839-04:00","date":"2026-08-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":16.7,"phases_s":{"reconcile":0.56,"cancel":0.21,"manage":15.1},"signals":0,"placed":0,"equity":142553.82,"open_positions":28,"pending_orders":0,"open_lots":119,"submitted_today":64,"filled_today":60,"unattributed_contracts":7,"top_signals":[],"github_run":"6413","github_run_id":"31194579676","status":"ok"}
```

### Live bot full output

```text
15:50:45  INFO      Mode: exits
15:50:46  INFO        Daily log -> logs/daily/2026-08-07.md
15:50:46  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
15:50:46  INFO        place_all_stops: checking 5 positions...
15:50:46  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
15:50:46  INFO        STOP already live AES @ $14.65
15:50:46  INFO        STOP already live BBY @ $79.72
15:50:46  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
15:50:46  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
15:50:47  INFO        [positions] 5/5 (5 valid)
15:50:47  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.69|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.06                                            HOLD|
|  GOOG  P&L +0.1%  $+0.11                                           HOLD|
|  AAPL  P&L +0.2%  $+0.20                                           HOLD|
|  ESS  P&L +0.4%  $+0.27                                            HOLD|
|  BBY  P&L +1.7%  $+1.61                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=121 paper_keys=yes dry_run=False
  alpaca positions=30
  FLAG b0|ORPHAN|333d0a59 missing from Alpaca
  State updated with reconciled lots.
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T11:50:50.146839-04:00 ===

[Run context]
Paper auth OK — equity $142553.82, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174
2026-08-07 11:51:01,357 INFO   EXIT [b267|lab0267_s403_w3_1045_1120_r2|S403] stop_loss (-50.0%) SELL 1 AAPL260810C00320000 @<= 0.21
2026-08-07 11:51:05,519 INFO   EXIT [b0|orphan_reconcile|ORPHAN] stop_loss (-60.0%) SELL 1 CVX260814C00200000 @<= 0.09

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $142,553.82                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    64                                      |
|  Orders filled today (ledger)  60                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             119                                     |
|  Broker option positions       28                                      |
|  Unattributed contracts        7 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1470  buckets=290  win=39%                           |
|  Returns   avg=+19.4%  med=-37.0%  p10=-79.6%  p90=+130.4%             |
|  Realized  $+8,918.18                                                  |
|  Raw incl dropped  trades=2004  real=$+7,322.63                        |
|  Today     trades=76  avg=-26.8%  med=-60.0%  real=$-1,157.19          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b238 lab0238_s401_w3_10  9 100% +255.2 +273.1 +815.4 $   +877         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b410 lab0410_s364_w4_11  3 100% +168.7 +233.3 +233.3 $   +183         |
|  ... 282 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (10)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 5 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (28)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  MARA260814C00011500           7    -73.9%   $   -257.60               |
|  AMD260807C00537500            4   -100.0%   $   -229.09               |
|  NKE260821C00044000           10    -34.9%   $   -220.00               |
|  NKE260828C00045000           10    -33.5%   $   -211.67               |
|  MARA260814C00012000           6    -81.7%   $   -188.00               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=16.7s reconcile=0.56s cancel=0.21s manage=15.1s
STATUS: options_morning_bot run complete (PAPER) elapsed=16.7s. run=#6413 https://github.com/28twagg-ops/TradingBot/actions/runs/31194579676
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 58 buckets closed trades, $-1,157.19 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=86 drop=19
Orphan rate: 9.4% (188/2004)
# Options signal frequency

_Generated 2026-08-07T11:51:12.611541_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   436 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    13 | WARN | <<<
| Total open lots             |   119 | INFO |
| Total closed lots           |  1349 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.69 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260807T155549Z

- UTC timestamp: `20260807T155549Z`
- GitHub run: [#6414](https://github.com/28twagg-ops/TradingBot/actions/runs/31194992882)
- Run id: `31194992882`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`26s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T11:55:54.249320-04:00","date":"2026-08-07","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":17.9,"phases_s":{"reconcile":0.22,"cancel":0.09,"manage":16.74},"signals":0,"placed":0,"equity":142114.82,"open_positions":28,"pending_orders":0,"open_lots":119,"submitted_today":64,"filled_today":60,"unattributed_contracts":7,"top_signals":[],"github_run":"6414","github_run_id":"31194992882","status":"ok"}
```

### Live bot full output

```text
15:55:50  INFO      Mode: exits
15:55:51  INFO        Daily log -> logs/daily/2026-08-07.md
15:55:51  INFO        Daily log reconciled -> logs/daily/2026-08-07.md (3 ledger rows)
15:55:51  INFO        place_all_stops: checking 5 positions...
15:55:51  INFO        STOP skipped AAPL: fractional (0.3033 shares) — software exit will handle it
15:55:51  INFO        STOP already live AES @ $14.65
15:55:51  INFO        STOP already live BBY @ $79.72
15:55:51  INFO        STOP skipped ESS: fractional (0.2445 shares) — software exit will handle it
15:55:51  INFO        STOP skipped GOOG: fractional (0.2661 shares) — software exit will handle it
15:55:51  INFO        [positions] 5/5 (5 valid)
15:55:52  INFO        Daily log -> logs/daily/2026-08-07.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $473.69|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  AES  P&L -0.1%  $-0.06                                            HOLD|
|  GOOG  P&L +0.2%  $+0.15                                           HOLD|
|  AAPL  P&L +0.2%  $+0.22                                           HOLD|
|  ESS  P&L +0.3%  $+0.24                                            HOLD|
|  BBY  P&L +1.7%  $+1.58                                            HOLD|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           5|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  0 attempted  |  0 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                5|
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
  open_lots=119 paper_keys=yes dry_run=False
  alpaca positions=30
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T11:55:54.249320-04:00 ===

[Run context]
Paper auth OK — equity $142114.82, account PA36KS87UPRS

[Setup]
Active buckets: 1024 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219, S220, S221, S400, S401, S402, S403, S350, S351, S352, S353, S354, S355, S356, S357, S358, S359, S360, S361, S362, S363, S364, S365, S366, S367, S368, S369, S370, S371, S372, S373, S374, S375, S376, S377, S378, S379, S380, S381, S382, S383, S384, S385, S386, S387, S388, S389, S390, S391, S392, S393, S394, S413, S414, S415, S416, S417, S418, S395, S396, S397, S398, S399, S404, S405, S406, S407, S408, S409, S410, S411, S412, S413, S414, S415, S416, S417, S418, S419
Dropped (no new entries; ex-reflected P&L): S173, S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $142,114.82                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    64                                      |
|  Orders filled today (ledger)  60                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             119                                     |
|  Broker option positions       28                                      |
|  Unattributed contracts        7 (orphan reconcile)                    |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1470  buckets=290  win=39%                           |
|  Returns   avg=+19.4%  med=-37.0%  p10=-79.6%  p90=+130.4%             |
|  Realized  $+8,918.18                                                  |
|  Raw incl dropped  trades=2004  real=$+7,322.63                        |
|  Today     trades=76  avg=-26.8%  med=-60.0%  real=$-1,157.19          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b238 lab0238_s401_w3_10  9 100% +255.2 +273.1 +815.4 $   +877         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b410 lab0410_s364_w4_11  3 100% +168.7 +233.3 +233.3 $   +183         |
|  ... 282 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (10)                                                    |
+------------------------------------------------------------------------+
|  b0   ORPHAN AMZN260807C00302500 x1 stop_loss (-100.0%)                |
|  b777 S397 AMZN260807C00292500 x1 stop_loss (-100.0%)                  |
|  b378 S362 AMZN260807C00297500 x1 stop_loss (-100.0%)                  |
|  b778 S397 AMZN260807C00295000 x1 stop_loss (-100.0%)                  |
|  b411 S364 MARA260814C00012000 x1 stop_loss (-60.9%)                   |
|  ... 5 more pending exit(s)                                            |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (28)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  MARA260814C00011500           7    -75.9%   $   -264.60               |
|  NKE260821C00044000           10    -36.5%   $   -230.00               |
|  AMD260807C00537500            4   -100.0%   $   -229.09               |
|  NKE260828C00045000           10    -33.5%   $   -211.67               |
|  MARA260814C00012000           6    -81.7%   $   -188.00               |
|  ... 20 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=17.9s reconcile=0.22s cancel=0.09s manage=16.74s
STATUS: options_morning_bot run complete (PAPER) elapsed=17.9s. run=#6414 https://github.com/28twagg-ops/TradingBot/actions/runs/31194992882
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 58 buckets closed trades, $-1,157.19 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=86 drop=19
Orphan rate: 9.4% (188/2004)
# Options signal frequency

_Generated 2026-08-07T11:56:17.764703_

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
## Ledger health — 2026-08-07
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |   436 | WARN | <<<
| Missing exit records (post) |   436 | WARN | <<<
| State/ledger mismatches     |    13 | WARN | <<<
| Total open lots             |   119 | INFO |
| Total closed lots           |  1349 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=473.69 router=CONFIRMED leaderboard_rows=105
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 14 | 43% | +0.39% | -0.69% | -1.92% | 1.95 | 1.6d | $+3.40 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
