# Daily Comprehensive Action Review — 2026-07-28

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260728T010358Z

- UTC timestamp: `20260728T010358Z`
- GitHub run: [#5245](https://github.com/28twagg-ops/TradingBot/actions/runs/30319140771)
- Run id: `30319140771`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T21:04:01.373658-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.3,"phases_s":{"reconcile":0.08},"signals":0,"placed":0,"equity":129286.63,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":[],"github_run":"5245","github_run_id":"30319140771","status":"ok"}
```

### Live bot full output

```text
01:03:59  INFO      Mode: summary
01:03:59  INFO        Daily log -> logs/daily/2026-07-28.md
01:03:59  INFO        Daily log reconciled -> logs/daily/2026-07-28.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:03 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.18|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $486.18|
|  Cash                                                           $486.18|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (0 positions)                         |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  2026-07-27  SELL  EQR  Pullback50  $96.97  P&L $-0.51                 |
|  2026-07-27  SELL  AVB  Pullback50  $96.72  P&L $-0.76                 |
|  2026-07-27  SELL  HUBB  Pullback50  $73.30  P&L $+0.11                |
|  2026-07-27  SELL  NOW  EarningsDrift  $97.43  P&L $-0.03              |
|  2026-07-27  SELL  CBOE  Pullback50  $97.34  P&L $-0.14                |
|  2026-07-27  SELL  CMS  Pullback50  $23.03  P&L $-0.12                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T21:04:01.373658-04:00 ===

[Run context]
After hours (21:04 ET) — exit summary only.
Paper auth OK — equity $129286.63, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $129,286.63                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    102                                     |
|  Orders filled today (ledger)  82                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=273  buckets=27  win=30%                             |
|  Returns   avg=-5.1%  med=-40.0%  p10=-66.2%  p90=+81.8%               |
|  Realized  $+4,423.13                                                  |
|  Raw incl dropped  trades=807  real=$+2,827.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s169_w2_1005_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s200_w2_1005_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s166_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s166_w3_1045_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s170_w2_1005_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s200_w1_0928_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 19 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b20  c020_s165_w3_1045_  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=0.3s reconcile=0.08s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.3s. run=#5245 https://github.com/28twagg-ops/TradingBot/actions/runs/30319140771
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T21:04:06.338852_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 4 | 4 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 18 | 11 | 1.6 | ~23 active signal-days |
| S166 | 2 | 2 | 1.0 | ~38 active signal-days |
| S167 | 5 | 4 | 1.2 | ~30 active signal-days |
| S168 | 4 | 3 | 1.3 | ~29 active signal-days |
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
| w2     |    3 |    2 |    9 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |
| w3     |    4 |    3 |   10 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    37 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 189 | 4 |
| S164 | 211 | 4 |
| S165 | 1657 | 18 |
| S166 | 89 | 2 |
| S167 | 211 | 5 |
| S168 | 144 | 4 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-27
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |     0 | OK |
| Missing exit records (post) |     0 | OK |
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=486.18 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260728T014549Z

- UTC timestamp: `20260728T014549Z`
- GitHub run: [#5246](https://github.com/28twagg-ops/TradingBot/actions/runs/30321162756)
- Run id: `30321162756`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T21:45:52.084973-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.4,"phases_s":{"reconcile":0.11},"signals":0,"placed":0,"equity":129330.63,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":[],"github_run":"5246","github_run_id":"30321162756","status":"ok"}
```

### Live bot full output

```text
01:45:50  INFO      Mode: summary
01:45:50  INFO        Daily log -> logs/daily/2026-07-28.md
01:45:50  INFO        Daily log reconciled -> logs/daily/2026-07-28.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         01:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.18|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $486.18|
|  Cash                                                           $486.18|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (0 positions)                         |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  2026-07-27  SELL  EQR  Pullback50  $96.97  P&L $-0.51                 |
|  2026-07-27  SELL  AVB  Pullback50  $96.72  P&L $-0.76                 |
|  2026-07-27  SELL  HUBB  Pullback50  $73.30  P&L $+0.11                |
|  2026-07-27  SELL  NOW  EarningsDrift  $97.43  P&L $-0.03              |
|  2026-07-27  SELL  CBOE  Pullback50  $97.34  P&L $-0.14                |
|  2026-07-27  SELL  CMS  Pullback50  $23.03  P&L $-0.12                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T21:45:52.084973-04:00 ===

[Run context]
After hours (21:45 ET) — exit summary only.
Paper auth OK — equity $129330.63, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $129,330.63                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    102                                     |
|  Orders filled today (ledger)  82                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=273  buckets=27  win=30%                             |
|  Returns   avg=-5.1%  med=-40.0%  p10=-66.2%  p90=+81.8%               |
|  Realized  $+4,423.13                                                  |
|  Raw incl dropped  trades=807  real=$+2,827.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s169_w2_1005_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s200_w2_1005_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s166_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s166_w3_1045_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s170_w2_1005_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s200_w1_0928_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 19 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b20  c020_s165_w3_1045_  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=0.4s reconcile=0.11s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.4s. run=#5246 https://github.com/28twagg-ops/TradingBot/actions/runs/30321162756
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T21:45:57.211409_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 4 | 4 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 18 | 11 | 1.6 | ~23 active signal-days |
| S166 | 2 | 2 | 1.0 | ~38 active signal-days |
| S167 | 5 | 4 | 1.2 | ~30 active signal-days |
| S168 | 4 | 3 | 1.3 | ~29 active signal-days |
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
| w2     |    3 |    2 |    9 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |
| w3     |    4 |    3 |   10 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    37 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 189 | 4 |
| S164 | 211 | 4 |
| S165 | 1657 | 18 |
| S166 | 89 | 2 |
| S167 | 211 | 5 |
| S168 | 144 | 4 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-27
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |     0 | OK |
| Missing exit records (post) |     0 | OK |
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=486.18 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260728T044849Z

- UTC timestamp: `20260728T044849Z`
- GitHub run: [#5247](https://github.com/28twagg-ops/TradingBot/actions/runs/30329753720)
- Run id: `30329753720`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-28T00:48:54.145360-04:00","date":"2026-07-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.51},"signals":0,"placed":0,"equity":128398.63,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5247","github_run_id":"30329753720","status":"ok"}
```

### Live bot full output

```text
04:48:50  INFO      Mode: summary
04:48:51  INFO        Daily log -> logs/daily/2026-07-28.md
04:48:51  INFO        Daily log reconciled -> logs/daily/2026-07-28.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         04:48 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.18|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $486.18|
|  Cash                                                           $486.18|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (0 positions)                         |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  2026-07-27  SELL  EQR  Pullback50  $96.97  P&L $-0.51                 |
|  2026-07-27  SELL  AVB  Pullback50  $96.72  P&L $-0.76                 |
|  2026-07-27  SELL  HUBB  Pullback50  $73.30  P&L $+0.11                |
|  2026-07-27  SELL  NOW  EarningsDrift  $97.43  P&L $-0.03              |
|  2026-07-27  SELL  CBOE  Pullback50  $97.34  P&L $-0.14                |
|  2026-07-27  SELL  CMS  Pullback50  $23.03  P&L $-0.12                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-28T00:48:54.145360-04:00 ===

[Run context]
After hours (00:48 ET) — exit summary only.
Paper auth OK — equity $128398.63, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $128,398.63                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=273  buckets=27  win=30%                             |
|  Returns   avg=-5.1%  med=-40.0%  p10=-66.2%  p90=+81.8%               |
|  Realized  $+4,423.13                                                  |
|  Raw incl dropped  trades=807  real=$+2,827.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s169_w2_1005_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s200_w2_1005_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s166_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s166_w3_1045_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s170_w2_1005_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s200_w1_0928_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 19 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b20  c020_s165_w3_1045_  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-28.log
elapsed=0.9s reconcile=0.51s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.9s. run=#5247 https://github.com/28twagg-ops/TradingBot/actions/runs/30329753720
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-28T00:48:59.783370_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 4 | 4 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 18 | 11 | 1.6 | ~23 active signal-days |
| S166 | 2 | 2 | 1.0 | ~38 active signal-days |
| S167 | 5 | 4 | 1.2 | ~30 active signal-days |
| S168 | 4 | 3 | 1.3 | ~29 active signal-days |
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
| w2     |    3 |    2 |    9 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |
| w3     |    4 |    3 |   10 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    37 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 189 | 4 |
| S164 | 211 | 4 |
| S165 | 1657 | 18 |
| S166 | 89 | 2 |
| S167 | 211 | 5 |
| S168 | 144 | 4 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    60 | WARN | <<<
| Missing exit records (post) |    60 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=486.18 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260728T130041Z

- UTC timestamp: `20260728T130041Z`
- GitHub run: [#5248](https://github.com/28twagg-ops/TradingBot/actions/runs/30361442665)
- Run id: `30361442665`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-28T09:00:44.969396-04:00","date":"2026-07-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.4,"phases_s":{"reconcile":0.09},"signals":0,"placed":0,"equity":127631.89,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5248","github_run_id":"30361442665","status":"ok"}
```

### Live bot full output

```text
13:00:42  INFO      Mode: summary
13:00:43  INFO        Daily log -> logs/daily/2026-07-28.md
13:00:43  INFO        Daily log reconciled -> logs/daily/2026-07-28.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.18|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $486.18|
|  Cash                                                           $486.18|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (0 positions)                         |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  2026-07-27  SELL  EQR  Pullback50  $96.97  P&L $-0.51                 |
|  2026-07-27  SELL  AVB  Pullback50  $96.72  P&L $-0.76                 |
|  2026-07-27  SELL  HUBB  Pullback50  $73.30  P&L $+0.11                |
|  2026-07-27  SELL  NOW  EarningsDrift  $97.43  P&L $-0.03              |
|  2026-07-27  SELL  CBOE  Pullback50  $97.34  P&L $-0.14                |
|  2026-07-27  SELL  CMS  Pullback50  $23.03  P&L $-0.12                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-28T09:00:44.969396-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $127631.89, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $127,631.89                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=273  buckets=27  win=30%                             |
|  Returns   avg=-5.1%  med=-40.0%  p10=-66.2%  p90=+81.8%               |
|  Realized  $+4,423.13                                                  |
|  Raw incl dropped  trades=807  real=$+2,827.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s169_w2_1005_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s200_w2_1005_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s166_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s166_w3_1045_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s170_w2_1005_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s200_w1_0928_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 19 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b20  c020_s165_w3_1045_  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-28.log
elapsed=0.4s reconcile=0.09s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.4s. run=#5248 https://github.com/28twagg-ops/TradingBot/actions/runs/30361442665
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-28T09:00:50.058302_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 4 | 4 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 18 | 11 | 1.6 | ~23 active signal-days |
| S166 | 2 | 2 | 1.0 | ~38 active signal-days |
| S167 | 5 | 4 | 1.2 | ~30 active signal-days |
| S168 | 4 | 3 | 1.3 | ~29 active signal-days |
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
| w2     |    3 |    2 |    9 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |
| w3     |    4 |    3 |   10 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    37 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 189 | 4 |
| S164 | 211 | 4 |
| S165 | 1657 | 18 |
| S166 | 89 | 2 |
| S167 | 211 | 5 |
| S168 | 144 | 4 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    60 | WARN | <<<
| Missing exit records (post) |    60 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=486.18 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260728T130540Z

- UTC timestamp: `20260728T130540Z`
- GitHub run: [#5249](https://github.com/28twagg-ops/TradingBot/actions/runs/30361833743)
- Run id: `30361833743`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-28T09:05:44.057245-04:00","date":"2026-07-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.8,"phases_s":{"reconcile":0.43},"signals":0,"placed":0,"equity":127431.89,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5249","github_run_id":"30361833743","status":"ok"}
```

### Live bot full output

```text
13:05:41  INFO      Mode: summary
13:05:42  INFO        Daily log -> logs/daily/2026-07-28.md
13:05:42  INFO        Daily log reconciled -> logs/daily/2026-07-28.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.18|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $486.18|
|  Cash                                                           $486.18|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (0 positions)                         |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  2026-07-27  SELL  EQR  Pullback50  $96.97  P&L $-0.51                 |
|  2026-07-27  SELL  AVB  Pullback50  $96.72  P&L $-0.76                 |
|  2026-07-27  SELL  HUBB  Pullback50  $73.30  P&L $+0.11                |
|  2026-07-27  SELL  NOW  EarningsDrift  $97.43  P&L $-0.03              |
|  2026-07-27  SELL  CBOE  Pullback50  $97.34  P&L $-0.14                |
|  2026-07-27  SELL  CMS  Pullback50  $23.03  P&L $-0.12                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-28T09:05:44.057245-04:00 ===

[Run context]
After hours (09:05 ET) — exit summary only.
Paper auth OK — equity $127431.89, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $127,431.89                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=273  buckets=27  win=30%                             |
|  Returns   avg=-5.1%  med=-40.0%  p10=-66.2%  p90=+81.8%               |
|  Realized  $+4,423.13                                                  |
|  Raw incl dropped  trades=807  real=$+2,827.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s169_w2_1005_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s200_w2_1005_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s166_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s166_w3_1045_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s170_w2_1005_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s200_w1_0928_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 19 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b20  c020_s165_w3_1045_  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-28.log
elapsed=0.8s reconcile=0.43s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.8s. run=#5249 https://github.com/28twagg-ops/TradingBot/actions/runs/30361833743
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-28T09:05:47.548400_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 4 | 4 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 18 | 11 | 1.6 | ~23 active signal-days |
| S166 | 2 | 2 | 1.0 | ~38 active signal-days |
| S167 | 5 | 4 | 1.2 | ~30 active signal-days |
| S168 | 4 | 3 | 1.3 | ~29 active signal-days |
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
| w2     |    3 |    2 |    9 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |
| w3     |    4 |    3 |   10 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    37 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 189 | 4 |
| S164 | 211 | 4 |
| S165 | 1657 | 18 |
| S166 | 89 | 2 |
| S167 | 211 | 5 |
| S168 | 144 | 4 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    60 | WARN | <<<
| Missing exit records (post) |    60 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=486.18 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260728T131047Z

- UTC timestamp: `20260728T131047Z`
- GitHub run: [#5250](https://github.com/28twagg-ops/TradingBot/actions/runs/30362222328)
- Run id: `30362222328`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-28T09:10:50.357488-04:00","date":"2026-07-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.19},"signals":0,"placed":0,"equity":127855.89,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5250","github_run_id":"30362222328","status":"ok"}
```

### Live bot full output

```text
13:10:48  INFO      Mode: summary
13:10:48  INFO        Daily log -> logs/daily/2026-07-28.md
13:10:48  INFO        Daily log reconciled -> logs/daily/2026-07-28.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.18|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $486.18|
|  Cash                                                           $486.18|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (0 positions)                         |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  2026-07-27  SELL  EQR  Pullback50  $96.97  P&L $-0.51                 |
|  2026-07-27  SELL  AVB  Pullback50  $96.72  P&L $-0.76                 |
|  2026-07-27  SELL  HUBB  Pullback50  $73.30  P&L $+0.11                |
|  2026-07-27  SELL  NOW  EarningsDrift  $97.43  P&L $-0.03              |
|  2026-07-27  SELL  CBOE  Pullback50  $97.34  P&L $-0.14                |
|  2026-07-27  SELL  CMS  Pullback50  $23.03  P&L $-0.12                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-28T09:10:50.357488-04:00 ===

[Run context]
After hours (09:10 ET) — exit summary only.
Paper auth OK — equity $127855.89, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $127,855.89                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=273  buckets=27  win=30%                             |
|  Returns   avg=-5.1%  med=-40.0%  p10=-66.2%  p90=+81.8%               |
|  Realized  $+4,423.13                                                  |
|  Raw incl dropped  trades=807  real=$+2,827.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s169_w2_1005_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s200_w2_1005_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s166_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s166_w3_1045_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s170_w2_1005_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s200_w1_0928_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 19 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b20  c020_s165_w3_1045_  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-28.log
elapsed=0.5s reconcile=0.19s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.5s. run=#5250 https://github.com/28twagg-ops/TradingBot/actions/runs/30362222328
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-28T09:10:56.080113_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 4 | 4 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 18 | 11 | 1.6 | ~23 active signal-days |
| S166 | 2 | 2 | 1.0 | ~38 active signal-days |
| S167 | 5 | 4 | 1.2 | ~30 active signal-days |
| S168 | 4 | 3 | 1.3 | ~29 active signal-days |
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
| w2     |    3 |    2 |    9 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |
| w3     |    4 |    3 |   10 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    37 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 189 | 4 |
| S164 | 211 | 4 |
| S165 | 1657 | 18 |
| S166 | 89 | 2 |
| S167 | 211 | 5 |
| S168 | 144 | 4 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    60 | WARN | <<<
| Missing exit records (post) |    60 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=486.18 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260728T131540Z

- UTC timestamp: `20260728T131540Z`
- GitHub run: [#5251](https://github.com/28twagg-ops/TradingBot/actions/runs/30362606082)
- Run id: `30362606082`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-28T09:15:45.412098-04:00","date":"2026-07-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.53},"signals":0,"placed":0,"equity":127767.89,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5251","github_run_id":"30362606082","status":"ok"}
```

### Live bot full output

```text
13:15:41  INFO      Mode: summary
13:15:43  INFO        Daily log -> logs/daily/2026-07-28.md
13:15:43  INFO        Daily log reconciled -> logs/daily/2026-07-28.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.18|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $486.18|
|  Cash                                                           $486.18|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (0 positions)                         |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  2026-07-27  SELL  EQR  Pullback50  $96.97  P&L $-0.51                 |
|  2026-07-27  SELL  AVB  Pullback50  $96.72  P&L $-0.76                 |
|  2026-07-27  SELL  HUBB  Pullback50  $73.30  P&L $+0.11                |
|  2026-07-27  SELL  NOW  EarningsDrift  $97.43  P&L $-0.03              |
|  2026-07-27  SELL  CBOE  Pullback50  $97.34  P&L $-0.14                |
|  2026-07-27  SELL  CMS  Pullback50  $23.03  P&L $-0.12                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-28T09:15:45.412098-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $127767.89, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $127,767.89                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=273  buckets=27  win=30%                             |
|  Returns   avg=-5.1%  med=-40.0%  p10=-66.2%  p90=+81.8%               |
|  Realized  $+4,423.13                                                  |
|  Raw incl dropped  trades=807  real=$+2,827.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s169_w2_1005_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s200_w2_1005_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s166_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s166_w3_1045_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s170_w2_1005_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s200_w1_0928_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 19 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b20  c020_s165_w3_1045_  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-28.log
elapsed=1.0s reconcile=0.53s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.0s. run=#5251 https://github.com/28twagg-ops/TradingBot/actions/runs/30362606082
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-28T09:15:51.190797_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 4 | 4 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 18 | 11 | 1.6 | ~23 active signal-days |
| S166 | 2 | 2 | 1.0 | ~38 active signal-days |
| S167 | 5 | 4 | 1.2 | ~30 active signal-days |
| S168 | 4 | 3 | 1.3 | ~29 active signal-days |
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
| w2     |    3 |    2 |    9 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |
| w3     |    4 |    3 |   10 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    37 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 189 | 4 |
| S164 | 211 | 4 |
| S165 | 1657 | 18 |
| S166 | 89 | 2 |
| S167 | 211 | 5 |
| S168 | 144 | 4 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    60 | WARN | <<<
| Missing exit records (post) |    60 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=486.18 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260728T132038Z

- UTC timestamp: `20260728T132038Z`
- GitHub run: [#5252](https://github.com/28twagg-ops/TradingBot/actions/runs/30362985499)
- Run id: `30362985499`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-28T09:20:41.463627-04:00","date":"2026-07-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.34},"signals":0,"placed":0,"equity":128011.89,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5252","github_run_id":"30362985499","status":"ok"}
```

### Live bot full output

```text
13:20:39  INFO      Mode: summary
13:20:40  INFO        Daily log -> logs/daily/2026-07-28.md
13:20:40  INFO        Daily log reconciled -> logs/daily/2026-07-28.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.18|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $486.18|
|  Cash                                                           $486.18|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (0 positions)                         |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  2026-07-27  SELL  EQR  Pullback50  $96.97  P&L $-0.51                 |
|  2026-07-27  SELL  AVB  Pullback50  $96.72  P&L $-0.76                 |
|  2026-07-27  SELL  HUBB  Pullback50  $73.30  P&L $+0.11                |
|  2026-07-27  SELL  NOW  EarningsDrift  $97.43  P&L $-0.03              |
|  2026-07-27  SELL  CBOE  Pullback50  $97.34  P&L $-0.14                |
|  2026-07-27  SELL  CMS  Pullback50  $23.03  P&L $-0.12                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-28T09:20:41.463627-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $128011.89, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $128,011.89                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=273  buckets=27  win=30%                             |
|  Returns   avg=-5.1%  med=-40.0%  p10=-66.2%  p90=+81.8%               |
|  Realized  $+4,423.13                                                  |
|  Raw incl dropped  trades=807  real=$+2,827.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s169_w2_1005_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s200_w2_1005_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s166_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s166_w3_1045_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s170_w2_1005_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s200_w1_0928_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 19 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b20  c020_s165_w3_1045_  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-28.log
elapsed=0.7s reconcile=0.34s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.7s. run=#5252 https://github.com/28twagg-ops/TradingBot/actions/runs/30362985499
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-28T09:20:45.853046_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 4 | 4 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 18 | 11 | 1.6 | ~23 active signal-days |
| S166 | 2 | 2 | 1.0 | ~38 active signal-days |
| S167 | 5 | 4 | 1.2 | ~30 active signal-days |
| S168 | 4 | 3 | 1.3 | ~29 active signal-days |
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
| w2     |    3 |    2 |    9 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |
| w3     |    4 |    3 |   10 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    37 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 189 | 4 |
| S164 | 211 | 4 |
| S165 | 1657 | 18 |
| S166 | 89 | 2 |
| S167 | 211 | 5 |
| S168 | 144 | 4 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    60 | WARN | <<<
| Missing exit records (post) |    60 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=486.18 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260728T132548Z

- UTC timestamp: `20260728T132548Z`
- GitHub run: [#5253](https://github.com/28twagg-ops/TradingBot/actions/runs/30363370450)
- Run id: `30363370450`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-28T09:25:53.006491-04:00","date":"2026-07-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.55},"signals":0,"placed":0,"equity":127687.89,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5253","github_run_id":"30363370450","status":"ok"}
```

### Live bot full output

```text
13:25:50  INFO      Mode: summary
13:25:51  INFO        Daily log -> logs/daily/2026-07-28.md
13:25:51  INFO        Daily log reconciled -> logs/daily/2026-07-28.md (0 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.18|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $486.18|
|  Cash                                                           $486.18|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                   $0.00|
|  Open P&L                                                        $+0.00|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (0 positions)                         |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  2026-07-27  SELL  EQR  Pullback50  $96.97  P&L $-0.51                 |
|  2026-07-27  SELL  AVB  Pullback50  $96.72  P&L $-0.76                 |
|  2026-07-27  SELL  HUBB  Pullback50  $73.30  P&L $+0.11                |
|  2026-07-27  SELL  NOW  EarningsDrift  $97.43  P&L $-0.03              |
|  2026-07-27  SELL  CBOE  Pullback50  $97.34  P&L $-0.14                |
|  2026-07-27  SELL  CMS  Pullback50  $23.03  P&L $-0.12                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-28T09:25:53.006491-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $127687.89, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $127,687.89                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    0                                       |
|  Orders filled today (ledger)  0                                       |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=273  buckets=27  win=30%                             |
|  Returns   avg=-5.1%  med=-40.0%  p10=-66.2%  p90=+81.8%               |
|  Realized  $+4,423.13                                                  |
|  Raw incl dropped  trades=807  real=$+2,827.58                         |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b51  c051_s169_w2_1005_  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b91  c091_s200_w2_1005_  2 100% +222.0 +222.0 +247.0 $   +293         |
|  b31  c031_s166_w4_1120_  2 100% +145.5 +145.5 +175.8 $   +192         |
|  b28  c028_s166_w3_1045_ 22  77% +50.0 +80.0 +102.0 $   +590           |
|  b58  c058_s170_w2_1005_  1 100% +59.1 +59.1 +59.1 $    +25            |
|  b56  c056_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b57  c057_s170_w1_0928_  1 100% +47.7 +47.7 +47.7 $    +21            |
|  b89  c089_s200_w1_0928_  9  56% +84.4 +30.9 +790.0 $    +45           |
|  ... 19 more bucket(s) with exits                                      |
+------------------------------------------------------------------------+
|  Low  b20  c020_s165_w3_1045_  1   0% -88.9 -88.9 -88.9 $     -8       |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-28.log
elapsed=1.0s reconcile=0.55s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.0s. run=#5253 https://github.com/28twagg-ops/TradingBot/actions/runs/30363370450
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-28_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-28T09:25:58.755168_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 4 | 4 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 18 | 11 | 1.6 | ~23 active signal-days |
| S166 | 2 | 2 | 1.0 | ~38 active signal-days |
| S167 | 5 | 4 | 1.2 | ~30 active signal-days |
| S168 | 4 | 3 | 1.3 | ~29 active signal-days |
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
| w2     |    3 |    2 |    9 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |
| w3     |    4 |    3 |   10 |    2 |    4 |    3 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    37 |
| w4     |    4 |    2 |    8 |    2 |    3 |    3 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    31 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 189 | 4 |
| S164 | 211 | 4 |
| S165 | 1657 | 18 |
| S166 | 89 | 2 |
| S167 | 211 | 5 |
| S168 | 144 | 4 |
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

## Notes

- Pre-router-fix (before 2026-07-17 commit `56660c9e`): S163/S166 were starved — expect zeros until a post-fix entry-window gap-down day.
- Controlled layout places one ENTRY per matching bucket×strategy; raw counts inflate, unique underlyings do not.


Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/signal_frequency.md
## Ledger health — 2026-07-28
| Check                       | Count | Status |
|-----------------------------|------:|--------|
| Current stuck (state)       |     0 | OK |
| Orphaned lots (post-stable) |    60 | WARN | <<<
| Missing exit records (post) |    60 | WARN | <<<
| State/ledger mismatches     |     0 | OK |
| Total open lots             |     0 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=486.18 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260728T133043Z

- UTC timestamp: `20260728T133043Z`
- GitHub run: [#5254](https://github.com/28twagg-ops/TradingBot/actions/runs/30363760294)
- Run id: `30363760294`
- Live bot: exit=`0`, duration=`217s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-28T09:25:53.006491-04:00","date":"2026-07-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.55},"signals":0,"placed":0,"equity":127687.89,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5253","github_run_id":"30363370450","status":"ok"}
```

### Live bot full output

```text
13:30:44  INFO      Mode: morning_prep
13:30:44  INFO      Fetching tickers (universe=both)...
13:30:45  INFO        S&P 500: 503
13:30:45  INFO        MidCap 400: 400
13:30:45  INFO        Total: 903 tickers
13:30:46  INFO        [prep_universe] 40/903 (40 valid)
13:30:48  INFO        [prep_universe] 80/903 (80 valid)
13:30:50  INFO        [prep_universe] 120/903 (120 valid)
13:30:51  INFO        [prep_universe] 160/903 (160 valid)
13:30:52  INFO        [prep_universe] 200/903 (199 valid)
13:30:59  INFO        [prep_universe] 240/903 (238 valid)
13:31:09  INFO        [prep_universe] 280/903 (278 valid)
13:31:22  INFO        [prep_universe] 320/903 (318 valid)
13:31:36  INFO        [prep_universe] 360/903 (358 valid)
13:31:48  INFO        [prep_universe] 400/903 (397 valid)
13:31:57  INFO        [prep_universe] 440/903 (437 valid)
13:32:10  INFO        [prep_universe] 480/903 (477 valid)
13:32:23  INFO        [prep_universe] 520/903 (517 valid)
13:32:34  INFO        [prep_universe] 560/903 (557 valid)
13:32:47  INFO        [prep_universe] 600/903 (597 valid)
13:32:59  INFO        [prep_universe] 640/903 (637 valid)
13:33:09  INFO        [prep_universe] 680/903 (677 valid)
13:33:22  INFO        [prep_universe] 720/903 (717 valid)
13:33:35  INFO        [prep_universe] 760/903 (757 valid)
13:33:45  INFO        [prep_universe] 800/903 (797 valid)
13:33:58  INFO        [prep_universe] 840/903 (836 valid)
13:34:11  INFO        [prep_universe] 880/903 (876 valid)
13:34:18  INFO        [prep_universe] 903/903 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.18|
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
|  Open positions                                                       0|
|  Invested                                                         $0.00|
|  Open P&L                                                        $+0.00|
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  Signal candidates                                                   29|
|  Universe scanned                                                   903|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-28T09:34:22.426200-04:00 ===

[Run context]
Paper auth OK — equity $128241.97, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
```

---

## Run 20260728T133606Z

- UTC timestamp: `20260728T133606Z`
- GitHub run: [#5255](https://github.com/28twagg-ops/TradingBot/actions/runs/30364162880)
- Run id: `30364162880`
- Live bot: exit=`0`, duration=`220s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-28T09:25:53.006491-04:00","date":"2026-07-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.55},"signals":0,"placed":0,"equity":127687.89,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5253","github_run_id":"30363370450","status":"ok"}
```

### Live bot full output

```text
13:36:07  INFO      Mode: morning_prep
13:36:08  INFO      Fetching tickers (universe=both)...
13:36:09  INFO        S&P 500: 503
13:36:09  INFO        MidCap 400: 400
13:36:09  INFO        Total: 903 tickers
13:36:10  INFO        [prep_universe] 40/903 (40 valid)
13:36:12  INFO        [prep_universe] 80/903 (80 valid)
13:36:13  INFO        [prep_universe] 120/903 (120 valid)
13:36:15  INFO        [prep_universe] 160/903 (160 valid)
13:36:16  INFO        [prep_universe] 200/903 (199 valid)
13:36:23  INFO        [prep_universe] 240/903 (238 valid)
13:36:34  INFO        [prep_universe] 280/903 (278 valid)
13:36:47  INFO        [prep_universe] 320/903 (318 valid)
13:36:58  INFO        [prep_universe] 360/903 (358 valid)
13:37:11  INFO        [prep_universe] 400/903 (397 valid)
13:37:24  INFO        [prep_universe] 440/903 (437 valid)
13:37:35  INFO        [prep_universe] 480/903 (477 valid)
13:37:48  INFO        [prep_universe] 520/903 (517 valid)
13:37:58  INFO        [prep_universe] 560/903 (557 valid)
13:38:12  INFO        [prep_universe] 600/903 (597 valid)
13:38:22  INFO        [prep_universe] 640/903 (637 valid)
13:38:35  INFO        [prep_universe] 680/903 (677 valid)
13:38:46  INFO        [prep_universe] 720/903 (717 valid)
13:38:59  INFO        [prep_universe] 760/903 (757 valid)
13:39:09  INFO        [prep_universe] 800/903 (797 valid)
13:39:23  INFO        [prep_universe] 840/903 (836 valid)
13:39:36  INFO        [prep_universe] 880/903 (876 valid)
13:39:43  INFO        [prep_universe] 903/903 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.18|
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
|  Open positions                                                       0|
|  Invested                                                         $0.00|
|  Open P&L                                                        $+0.00|
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  Signal candidates                                                   23|
|  Universe scanned                                                   903|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-28T09:39:48.274308-04:00 ===

[Run context]
Paper auth OK — equity $126425.89, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
```

---

## Run 20260728T134101Z

- UTC timestamp: `20260728T134101Z`
- GitHub run: [#5256](https://github.com/28twagg-ops/TradingBot/actions/runs/30364553595)
- Run id: `30364553595`
- Live bot: exit=`0`, duration=`216s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-28T09:25:53.006491-04:00","date":"2026-07-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.55},"signals":0,"placed":0,"equity":127687.89,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5253","github_run_id":"30363370450","status":"ok"}
```

### Live bot full output

```text
13:41:02  INFO      Mode: morning_prep
13:41:03  INFO        Universe cache hit: 903 tickers (tickers_2026-07-28.json)
13:41:04  INFO        [prep_universe] 40/903 (40 valid)
13:41:06  INFO        [prep_universe] 80/903 (80 valid)
13:41:07  INFO        [prep_universe] 120/903 (120 valid)
13:41:08  INFO        [prep_universe] 160/903 (160 valid)
13:41:10  INFO        [prep_universe] 200/903 (199 valid)
13:41:17  INFO        [prep_universe] 240/903 (238 valid)
13:41:28  INFO        [prep_universe] 280/903 (278 valid)
13:41:41  INFO        [prep_universe] 320/903 (318 valid)
13:41:51  INFO        [prep_universe] 360/903 (358 valid)
13:42:05  INFO        [prep_universe] 400/903 (397 valid)
13:42:15  INFO        [prep_universe] 440/903 (437 valid)
13:42:29  INFO        [prep_universe] 480/903 (477 valid)
13:42:42  INFO        [prep_universe] 520/903 (517 valid)
13:42:52  INFO        [prep_universe] 560/903 (557 valid)
13:43:06  INFO        [prep_universe] 600/903 (597 valid)
13:43:16  INFO        [prep_universe] 640/903 (637 valid)
13:43:29  INFO        [prep_universe] 680/903 (677 valid)
13:43:40  INFO        [prep_universe] 720/903 (717 valid)
13:43:53  INFO        [prep_universe] 760/903 (757 valid)
13:44:04  INFO        [prep_universe] 800/903 (797 valid)
13:44:17  INFO        [prep_universe] 840/903 (836 valid)
13:44:27  INFO        [prep_universe] 880/903 (876 valid)
13:44:34  INFO        [prep_universe] 903/903 (899 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.18|
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
|  Open positions                                                       0|
|  Invested                                                         $0.00|
|  Open P&L                                                        $+0.00|
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
|  Signal candidates                                                   22|
|  Universe scanned                                                   903|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-28T09:44:39.644014-04:00 ===

[Run context]
Paper auth OK — equity $126639.21, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
```

---

## Run 20260728T134614Z

- UTC timestamp: `20260728T134614Z`
- GitHub run: [#5257](https://github.com/28twagg-ops/TradingBot/actions/runs/30364956974)
- Run id: `30364956974`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-28T09:25:53.006491-04:00","date":"2026-07-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.55},"signals":0,"placed":0,"equity":127687.89,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5253","github_run_id":"30363370450","status":"ok"}
```

### Live bot full output

```text
13:46:15  INFO      Mode: morning_scan
13:46:15  INFO        Universe cache hit: 903 tickers (tickers_2026-07-28.json)
13:46:16  INFO        [universe] 40/903 (40 valid)
13:46:18  INFO        [universe] 80/903 (80 valid)
13:46:19  INFO        [universe] 120/903 (120 valid)
13:46:21  INFO        [universe] 160/903 (160 valid)
13:46:23  INFO        [universe] 200/903 (199 valid)
13:46:30  INFO        [universe] 240/903 (238 valid)
13:46:43  INFO        [universe] 280/903 (278 valid)
13:46:53  INFO        [universe] 320/903 (318 valid)
13:47:05  INFO        [universe] 360/903 (358 valid)
13:47:18  INFO        [universe] 400/903 (397 valid)
13:47:28  INFO        [universe] 440/903 (437 valid)
13:47:41  INFO        [universe] 480/903 (477 valid)
13:47:54  INFO        [universe] 520/903 (517 valid)
13:48:04  INFO        [universe] 560/903 (557 valid)
13:48:17  INFO        [universe] 600/903 (597 valid)
13:48:30  INFO        [universe] 640/903 (637 valid)
13:48:40  INFO        [universe] 680/903 (677 valid)
13:48:53  INFO        [universe] 720/903 (717 valid)
13:49:06  INFO        [universe] 760/903 (757 valid)
13:49:16  INFO        [universe] 800/903 (797 valid)
13:49:29  INFO        [universe] 840/903 (836 valid)
13:49:42  INFO        [universe] 880/903 (876 valid)
13:49:49  INFO        [universe] 903/903 (899 valid)
13:49:52  INFO        BUY  ALGN  $97.24  [Pullback50]  id=aad4021a-5726-4443-88c6-00d6e8b4381b
13:49:52  INFO        BUY  BG  $97.24  [Pullback50]  id=c38c3531-839b-4c47-974b-dcc7d2729f1b
13:49:52  INFO        BUY  DTE  $97.24  [Pullback50]  id=bbf9a00c-c172-47b7-a248-272f03e3bd2a
13:49:52  INFO        BUY  DHI  $97.24  [Pullback50]  id=60909298-995f-4067-a86c-32f88eb6a99e
13:49:52  INFO        BUY  EQR  $72.93  [Pullback50]  id=41222c45-4311-4b8d-950c-928d28c63248

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:46 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.18|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-28|
|  Universe                                                          both|
|  Mon~  Jul: 52wkLow + Pullback50 (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $486.18|
|  Cash                                                           $486.18|
|  Reserve                                          $24.31  (always kept)|
|  Available                                    $461.87  (for new trades)|
|  Trade size             $97.24  (20% per signal — all strategies equal)|
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
|  Use cached plan                                  no (stale (27360.8m))|
+========================================================================+

+========================================================================+
|                             DATA DOWNLOAD                              |
+========================================================================+
|  Universe: both  |  Alpaca primary / yfinance fallback                 |
+========================================================================+

+========================================================================+
|                              SIGNAL SCAN                               |
+========================================================================+
|  Month: Jul  |  Regime: BULL                                           |
|  Primary: 52wkLow  |  Secondary: Pullback50 (display only — schedule n~|
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  23                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  ALGN     Pullback50      eq     $171.17  44.9   -2.29   50MA bounce (-|
|  BG       Pullback50      eq     $117.74  55.7   -2.03   50MA bounce (-|
|  DTE      Pullback50      eq     $148.61  43.7   -2.87   50MA bounce (+|
|  DHI      Pullback50      eq     $151.31  54.3   -2.28   50MA bounce (+|
|  EQR      Pullback50      eq     $67.84   47.2   -2.45   50MA bounce (+|
|  HBAN     Pullback50      eq     $17.23   46.4   -1.64   50MA bounce (+|
|  JBHT     Pullback50      eq     $281.31  53.8   -2.13   50MA bounce (+|
|  KMI      Pullback50      eq     $31.96   43.5   -1.88   50MA bounce (-|
|  LIN      Pullback50      eq     $518.28  43.5   -2.78   50MA bounce (+|
|  MAA      Pullback50      eq     $135.59  44.3   -3.02   50MA bounce (+|
|  OXY      Pullback50      eq     $55.13   56.5   -2.26   50MA bounce (+|
|  OKE      Pullback50      eq     $89.62   45.0   -2.71   50MA bounce (+|
|  ALLY     Pullback50      eq     $43.82   46.1   -2.13   50MA bounce (-|
|  ALV      Pullback50      eq     $121.57  57.6   -1.84   50MA bounce (+|
|  CAR      Pullback50      eq     $165.61  64.8   -1.34   50MA bounce (-|
|  COLB     Pullback50      eq     $31.04   47.9   -2.33   50MA bounce (+|
|  GBCI     Pullback50      eq     $49.43   45.9   -2.68   50MA bounce (-|
|  IRT      Pullback50      eq     $16.61   44.8   -1.89   50MA bounce (+|
|  LECO     Pullback50      eq     $262.09  66.1   -2.44   50MA bounce (+|
|  NYT      Pullback50      eq     $73.80   51.8   -2.78   50MA bounce (-|
|  PEN      Pullback50      eq     $320.58  61.1   -1.99   50MA bounce (+|
|  SLAB     Pullback50      eq     $217.18  35.6   -1.29   50MA bounce (-|
|  UNM      Pullback50      eq     $87.31   47.9   -2.15   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] ALGN  Pullback50                                   $97.24|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] BG  Pullback50                                     $97.24|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] DTE  Pullback50                                    $97.24|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] DHI  Pullback50                                    $97.24|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    ENTER [eq] EQR  Pullback50                                    $72.93|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|
|    SKIP [eq] HBAN  Pullback50                                     cap 5|
|    SKIP [eq] JBHT  Pullback50                                     cap 5|
|    SKIP [eq] KMI  Pullback50                                      cap 5|
|    SKIP [eq] LIN  Pullback50                                      cap 5|
|    SKIP [eq] MAA  Pullback50                                      cap 5|
|    SKIP [eq] OXY  Pullback50                                      cap 5|
|    SKIP [eq] OKE  Pullback50                                      cap 5|
|    SKIP [eq] ALLY  Pullback50                                     cap 5|
|    SKIP [eq] ALV  Pullback50                                      cap 5|
|    SKIP [eq] CAR  Pullback50                                      cap 5|```

### Options bot full output

```text

## Run 20260728T135125Z

- UTC timestamp: `20260728T135125Z`
- GitHub run: [#5258](https://github.com/28twagg-ops/TradingBot/actions/runs/30365360391)
- Run id: `30365360391`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-28T09:25:53.006491-04:00","date":"2026-07-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.55},"signals":0,"placed":0,"equity":127687.89,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5253","github_run_id":"30363370450","status":"ok"}
```

### Live bot full output

```text
13:51:26  INFO      Mode: morning_scan
13:51:27  INFO        [positions] 5/5 (5 valid)
13:51:27  INFO        SELL LIMIT BG  qty=0.821157711  limit=$118.09  id=a357e2cd-590f-4d7f-9543-362ea31a3107
13:51:58  INFO        SELL LIMIT filled BG (confirmed by position check)
13:51:58  INFO        TX logged: SELL BG  P&L -0.06%
13:51:58  INFO        SELL LIMIT DHI  qty=0.640758656  limit=$151.41  id=7c7334a4-db02-403d-a458-8ae38d8dfa7c
13:52:29  INFO        SELL LIMIT filled DHI (confirmed by position check)
13:52:29  INFO        TX logged: SELL DHI  P&L -0.02%
13:52:29  INFO        Universe cache hit: 903 tickers (tickers_2026-07-28.json)
13:52:30  INFO        [universe] 40/900 (40 valid)
13:52:31  INFO        [universe] 80/900 (80 valid)
13:52:32  INFO        [universe] 120/900 (120 valid)
13:52:33  INFO        [universe] 160/900 (160 valid)
13:52:34  INFO        [universe] 200/900 (199 valid)
13:52:42  INFO        [universe] 240/900 (238 valid)
13:52:55  INFO        [universe] 280/900 (278 valid)
13:53:08  INFO        [universe] 320/900 (318 valid)
13:53:18  INFO        [universe] 360/900 (358 valid)
13:53:31  INFO        [universe] 400/900 (397 valid)
13:53:42  INFO        [universe] 440/900 (437 valid)
13:53:55  INFO        [universe] 480/900 (477 valid)
13:54:08  INFO        [universe] 520/900 (517 valid)
13:54:18  INFO        [universe] 560/900 (557 valid)
13:54:31  INFO        [universe] 600/900 (597 valid)
13:54:42  INFO        [universe] 640/900 (637 valid)
13:54:55  INFO        [universe] 680/900 (677 valid)
13:55:08  INFO        [universe] 720/900 (717 valid)
13:55:18  INFO        [universe] 760/900 (757 valid)
```

### Options bot full output

```text

## Run 20260728T135610Z

- UTC timestamp: `20260728T135610Z`
- GitHub run: [#5259](https://github.com/28twagg-ops/TradingBot/actions/runs/30365769033)
- Run id: `30365769033`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-28T09:25:53.006491-04:00","date":"2026-07-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.55},"signals":0,"placed":0,"equity":127687.89,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5253","github_run_id":"30363370450","status":"ok"}
```

### Live bot full output

```text
13:56:11  INFO      Mode: morning_scan
13:56:12  INFO        [positions] 3/3 (3 valid)
13:56:12  INFO        Universe cache hit: 903 tickers (tickers_2026-07-28.json)
13:56:13  INFO        [universe] 40/900 (40 valid)
13:56:15  INFO        [universe] 80/900 (80 valid)
13:56:16  INFO        [universe] 120/900 (120 valid)
13:56:18  INFO        [universe] 160/900 (160 valid)
13:56:28  INFO        [universe] 200/900 (199 valid)
13:56:41  INFO        [universe] 240/900 (238 valid)
13:56:51  INFO        [universe] 280/900 (278 valid)
13:57:05  INFO        [universe] 320/900 (318 valid)
13:57:15  INFO        [universe] 360/900 (358 valid)
13:57:28  INFO        [universe] 400/900 (397 valid)
13:57:39  INFO        [universe] 440/900 (437 valid)
13:57:52  INFO        [universe] 480/900 (477 valid)
13:58:02  INFO        [universe] 520/900 (517 valid)
13:58:16  INFO        [universe] 560/900 (557 valid)
13:58:29  INFO        [universe] 600/900 (597 valid)
13:58:39  INFO        [universe] 640/900 (637 valid)
13:58:52  INFO        [universe] 680/900 (677 valid)
13:59:03  INFO        [universe] 720/900 (717 valid)
13:59:16  INFO        [universe] 760/900 (757 valid)
13:59:26  INFO        [universe] 800/900 (797 valid)
13:59:39  INFO        [universe] 840/900 (836 valid)
13:59:53  INFO        [universe] 880/900 (876 valid)
13:59:57  INFO        [universe] 900/900 (896 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:56 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.26|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-28|
|  Universe                                                          both|
|  Mon~  Jul: 52wkLow + Pullback50 (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $486.26|
|  Cash                                                           $218.64|
|  Reserve                                          $24.31  (always kept)|
|  Available                                    $194.33  (for new trades)|
|  Trade size             $97.25  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (3 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ALGN     Pullback50      $97.16     $171.32  $171.20  -0.1%   $-0.07  |
|  DTE      Pullback50      $97.41     $149.05  $149.31  +0.2%   $+0.18  |
|  EQR      Pullback50      $73.06     $67.78   $67.91   +0.2%   $+0.14  |
|                                                                        |
|  Total invested                                                 $267.62|
|  Total open P&L                                                  $+0.24|
|  Buys today: 0  |  entry cap: 2  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (27370.7m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  ALGN  P&L -0.1%  $-0.07                                           HOLD|
|  DTE  P&L +0.2%  $+0.18                                            HOLD|
|  EQR  P&L +0.2%  $+0.14                                            HOLD|
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
|  Month: Jul  |  Regime: BULL                                           |
|  Primary: 52wkLow  |  Secondary: Pullback50 (display only — schedule n~|
|  Source                                                       live scan|
+========================================================================+

+========================================================================+
|                         SIGNALS FOUND  --  22                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  BG       Pullback50      eq     $118.98  58.1   -2.00   50MA bounce (+|
|  DHI      Pullback50      eq     $151.59  54.6   -2.25   50MA bounce (+|
|  FFIV     Pullback50      eq     $397.11  41.0   -1.23   50MA bounce (-|
|  HUBB     Pullback50      eq     $488.19  54.2   -1.25   50MA bounce (+|
|  HBAN     Pullback50      eq     $17.25   46.6   -1.62   50MA bounce (+|
|  JBHT     Pullback50      eq     $281.43  53.9   -2.08   50MA bounce (+|
|  KMI      Pullback50      eq     $32.15   46.0   -1.85   50MA bounce (-|
|  NI       Pullback50      eq     $46.38   46.2   -2.30   50MA bounce (-|
|  OXY      Pullback50      eq     $55.24   56.9   -2.22   50MA bounce (+|
|  OKE      Pullback50      eq     $89.84   45.7   -2.65   50MA bounce (+|
|  ROK      Pullback50      eq     $461.45  48.6   -3.14   50MA bounce (+|
|  ALV      Pullback50      eq     $121.92  58.2   -1.72   50MA bounce (+|
|  BHF      Pullback50      eq     $63.56   37.1   -2.14   50MA bounce (+|
|  CMC      Pullback50      eq     $69.97   72.6   -2.80   50MA bounce (-|
|  COLB     Pullback50      eq     $31.07   48.3   -2.28   50MA bounce (+|
|  HOG      Pullback50      eq     $25.09   48.5   -1.96   50MA bounce (-|
|  IRT      Pullback50      eq     $16.67   46.2   -1.87   50MA bounce (+|
|  KNF      Pullback50      eq     $79.98   50.8   -2.53   50MA bounce (+|
|  NYT      Pullback50      eq     $74.14   52.7   -2.76   50MA bounce (+|
|  PEN      Pullback50      eq     $320.51  60.9   -1.96   50MA bounce (+|
|  SLAB     Pullback50      eq     $217.07  34.7   -1.28   50MA bounce (-|
|  UNM      Pullback50      eq     $87.45   48.6   -2.14   50MA bounce (-|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
13:59:59  ERROR       BUY FAILED BG: {"code":40010001,"message":"client_order_id must be unique"}
14:00:00  ERROR       BUY FAILED DHI: {"code":40010001,"message":"client_order_id must be unique"}
14:00:00  INFO        BUY  FFIV  $97.25  [Pullback50]  id=29ed8e4a-481e-4c8d-ba5a-3c8a5f48701e
14:00:00  INFO        BUY  HUBB  $97.07  [Pullback50]  id=5f005ab6-38e4-46af-a85e-790b6b96193a
```

### Options bot full output

```text

## Run 20260728T140138Z

- UTC timestamp: `20260728T140138Z`
- GitHub run: [#5260](https://github.com/28twagg-ops/TradingBot/actions/runs/30366185352)
- Run id: `30366185352`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-28T09:25:53.006491-04:00","date":"2026-07-28","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.55},"signals":0,"placed":0,"equity":127687.89,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5253","github_run_id":"30363370450","status":"ok"}
```

### Live bot full output

```text
14:01:39  INFO      Mode: exits
14:01:40  INFO        Daily log -> logs/daily/2026-07-28.md
14:01:40  INFO        Daily log reconciled -> logs/daily/2026-07-28.md (2 ledger rows)
14:01:40  INFO        place_all_stops: checking 5 positions...
14:01:40  INFO        STOP skipped ALGN: fractional (0.5675 shares) — software exit will handle it
14:01:40  INFO        STOP skipped DTE: fractional (0.6523 shares) — software exit will handle it
14:01:40  INFO        STOP already live EQR @ $67.45
14:01:40  INFO        STOP skipped FFIV: fractional (0.2428 shares) — software exit will handle it
14:01:40  INFO        STOP skipped HUBB: fractional (0.1985 shares) — software exit will handle it
14:01:41  INFO        [positions] 5/5 (5 valid)
14:01:41  INFO        Daily log -> logs/daily/2026-07-28.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.38|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  HUBB  P&L -0.2%  $-0.22                                           HOLD|
|  ALGN  P&L -0.2%  $-0.19                                           HOLD|
|  DTE  P&L +0.2%  $+0.17                                            HOLD|
|  FFIV  P&L +0.3%  $+0.31                                           HOLD|
|  EQR  P&L +0.4%  $+0.29                                            HOLD|
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
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-28T10:01:43.471274-04:00 ===

[Run context]
Paper auth OK — equity $128345.89, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 733 signal(s); top: ['S165:AMD', 'S165:APH', 'S165:AMAT', 'S165:ANET', 'S165:AVGO', 'S165:CARR', 'S165:CAT', 'S165:CNC']
Paper lab: $129126 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
```

---
