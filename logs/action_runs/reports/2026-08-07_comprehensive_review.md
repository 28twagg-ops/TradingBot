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
