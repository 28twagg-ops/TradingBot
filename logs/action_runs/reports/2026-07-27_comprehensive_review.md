# Daily Comprehensive Action Review — 2026-07-27

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260727T020322Z

- UTC timestamp: `20260727T020322Z`
- GitHub run: [#5104](https://github.com/28twagg-ops/TradingBot/actions/runs/30231215892)
- Run id: `30231215892`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-24T21:04:07.294619-04:00","date":"2026-07-24","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.7,"phases_s":{"reconcile":1.37},"signals":0,"placed":0,"equity":130247.41,"open_positions":1,"pending_orders":0,"open_lots":1,"submitted_today":101,"filled_today":111,"unattributed_contracts":0,"top_signals":[],"github_run":"5103","github_run_id":"30137697666","status":"ok"}
```

### Live bot full output

```text
02:03:23  INFO      Mode: weekly
02:03:24  INFO        Weekly summary -> logs/weekly/2026-W31.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                            WEEKLY|
|  Time                                                         02:03 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.05|
+========================================================================+

+========================================================================+
|              RUBBER BAND BOT  |  Week 31 / 2026  |  LIVE               |
+========================================================================+
+------------------------------------------------------------------------+
|  Date                                                 2026-07-27  (Jul)|
|  Regime                                                            BULL|
|  Strate~  52wkLow  +  Pullback50 (display only — schedule not enforced)|
|  Execution                      Summary mode only (no orders submitted)|
|  Buys today                                                           0|
|  Cash-based cap             4933 max trades with current available cash|
+------------------------------------------------------------------------+
|  Equity           $486.05       Cash             $73.64                |
|  Invested         $412.41       Available        $49.34                |
|  Open P&L         $+3.42        Realized P&L     $-0.28                |
+------------------------------------------------------------------------+
|  This week          0 buys  |  27 sells  |  Win rate 41%  |  P&L $+4.34|
|  All ti~  1017 trades  |  Avg hold 1.8d  |  Return -4.5%  |  P&L $-0.28|
+------------------------------------------------------------------------+
|  TICKER  STRATEGY       INVESTED   ENTRY     NOW       P&L%      P&L$  |
+------------------------------------------------------------------------+
|  ABNB    Pullback50     $97.40     $139.66   $140.21   +0.4%     $+0.38|
|  CARR    Pullback50     $97.49     $67.80    $68.88    +1.6%     $+1.53|
|  CL      Pullback50     $97.36     $90.74    $90.75    +0.0%     $+0.01|
|  DTE     Pullback50     $97.38     $147.63   $149.46   +1.2%     $+1.19|
|  LNT     Pullback50     $22.77     $73.97    $74.94    +1.3%     $+0.30|
+------------------------------------------------------------------------+
|  Next month                               Aug:  VolumeSpike  +  52wkLow|
+========================================================================+

+========================================================================+
|                        YEAR-BY-YEAR PERFORMANCE                        |
+========================================================================+
|  YEAR   START     END       RETURN    P&L $       TRADES   WIN%        |
+------------------------------------------------------------------------+
|  2026   $509      $487      -4.3%     $-21.88     1017     31.6% ✗     |
+------------------------------------------------------------------------+
|  Profitable years                                             0/1  (0%)|
|  Best  year                                      2026   -4.3%   $-21.88|
|  Worst year                                      2026   -4.3%   $-21.88|
+========================================================================+
```

### Options bot full output

```text
Weekend — skip options paper bot
```

---

## Run 20260727T055848Z

- UTC timestamp: `20260727T055848Z`
- GitHub run: [#5105](https://github.com/28twagg-ops/TradingBot/actions/runs/30241253215)
- Run id: `30241253215`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T01:58:52.948228-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.46},"signals":0,"placed":0,"equity":134067.91,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5105","github_run_id":"30241253215","status":"ok"}
```

### Live bot full output

```text
05:58:49  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         05:58 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $486.05|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $486.05|
|  Cash                                                            $73.64|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $412.41|
|  Open P&L                                                        $+3.42|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABNB     Pullback50      $97.40     $139.66  $140.21  +0.4%   $+0.38  |
|  CARR     Pullback50      $97.49     $67.80   $68.88   +1.6%   $+1.53  |
|  CL       Pullback50      $97.36     $90.74   $90.75   +0.0%   $+0.01  |
|  DTE      Pullback50      $97.38     $147.63  $149.46  +1.2%   $+1.19  |
|  LNT      Pullback50      $22.77     $73.97   $74.94   +1.3%   $+0.30  |
|                                                                        |
|  Total invested                                                 $412.41|
|  Total open P&L                                                  $+3.42|
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
|  2026-07-24  SELL  CHD  Pullback50  $97.41  P&L $+0.12                 |
|  2026-07-24  SELL  CI  Pullback50  $97.40  P&L $+0.93                  |
|  2026-07-24  SELL  AEP  Pullback50  $99.33  P&L $+2.96                 |
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=1 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T01:58:52.948228-04:00 ===

[Run context]
After hours (01:58 ET) — exit summary only.
Paper auth OK — equity $134067.91, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $134,067.91                             |
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
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=1.0s reconcile=0.46s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.0s. run=#5105 https://github.com/28twagg-ops/TradingBot/actions/runs/30241253215
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T01:58:58.695745_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 3 | 3 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 17 | 10 | 1.7 | ~23 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 4 | 3 | 1.3 | ~29 active signal-days |
| S168 | 3 | 2 | 1.5 | ~25 active signal-days |
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
| w1     |    1 |    1 |    5 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    16 |
| w2     |    2 |    2 |    8 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 175 | 3 |
| S164 | 211 | 4 |
| S165 | 1643 | 17 |
| S166 | 75 | 1 |
| S167 | 197 | 4 |
| S168 | 130 | 3 |
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
equity=486.05 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T130040Z

- UTC timestamp: `20260727T130040Z`
- GitHub run: [#5106](https://github.com/28twagg-ops/TradingBot/actions/runs/30268271131)
- Run id: `30268271131`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T09:00:44.422734-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.9,"phases_s":{"reconcile":0.46},"signals":0,"placed":0,"equity":133519.91,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5106","github_run_id":"30268271131","status":"ok"}
```

### Live bot full output

```text
13:00:41  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $488.04|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $488.04|
|  Cash                                                            $73.64|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $414.40|
|  Open P&L                                                        $+5.41|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABNB     Pullback50      $99.13     $139.66  $142.70  +2.2%   $+2.11  |
|  CARR     Pullback50      $97.59     $67.80   $68.95   +1.7%   $+1.63  |
|  CL       Pullback50      $97.52     $90.74   $90.90   +0.2%   $+0.17  |
|  DTE      Pullback50      $97.38     $147.63  $149.46  +1.2%   $+1.19  |
|  LNT      Pullback50      $22.77     $73.97   $74.94   +1.3%   $+0.30  |
|                                                                        |
|  Total invested                                                 $414.40|
|  Total open P&L                                                  $+5.41|
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
|  2026-07-24  SELL  CHD  Pullback50  $97.41  P&L $+0.12                 |
|  2026-07-24  SELL  CI  Pullback50  $97.40  P&L $+0.93                  |
|  2026-07-24  SELL  AEP  Pullback50  $99.33  P&L $+2.96                 |
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
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
=== options_morning_bot (PAPER) 2026-07-27T09:00:44.422734-04:00 ===

[Run context]
After hours (09:00 ET) — exit summary only.
Paper auth OK — equity $133519.91, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,519.91                             |
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
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=0.9s reconcile=0.46s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.9s. run=#5106 https://github.com/28twagg-ops/TradingBot/actions/runs/30268271131
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T09:00:49.397754_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 3 | 3 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 17 | 10 | 1.7 | ~23 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 4 | 3 | 1.3 | ~29 active signal-days |
| S168 | 3 | 2 | 1.5 | ~25 active signal-days |
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
| w1     |    1 |    1 |    5 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    16 |
| w2     |    2 |    2 |    8 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 175 | 3 |
| S164 | 211 | 4 |
| S165 | 1643 | 17 |
| S166 | 75 | 1 |
| S167 | 197 | 4 |
| S168 | 130 | 3 |
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
equity=488.04 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T130611Z

- UTC timestamp: `20260727T130611Z`
- GitHub run: [#5107](https://github.com/28twagg-ops/TradingBot/actions/runs/30268635225)
- Run id: `30268635225`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T09:06:14.574100-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.17},"signals":0,"placed":0,"equity":133723.91,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5107","github_run_id":"30268635225","status":"ok"}
```

### Live bot full output

```text
13:06:12  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:06 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $488.04|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $488.04|
|  Cash                                                            $73.64|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $414.40|
|  Open P&L                                                        $+5.41|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABNB     Pullback50      $99.13     $139.66  $142.70  +2.2%   $+2.11  |
|  CARR     Pullback50      $97.59     $67.80   $68.95   +1.7%   $+1.63  |
|  CL       Pullback50      $97.52     $90.74   $90.90   +0.2%   $+0.17  |
|  DTE      Pullback50      $97.38     $147.63  $149.46  +1.2%   $+1.19  |
|  LNT      Pullback50      $22.77     $73.97   $74.94   +1.3%   $+0.30  |
|                                                                        |
|  Total invested                                                 $414.40|
|  Total open P&L                                                  $+5.41|
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
|  2026-07-24  SELL  CHD  Pullback50  $97.41  P&L $+0.12                 |
|  2026-07-24  SELL  CI  Pullback50  $97.40  P&L $+0.93                  |
|  2026-07-24  SELL  AEP  Pullback50  $99.33  P&L $+2.96                 |
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
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
=== options_morning_bot (PAPER) 2026-07-27T09:06:14.574100-04:00 ===

[Run context]
After hours (09:06 ET) — exit summary only.
Paper auth OK — equity $133723.91, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,723.91                             |
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
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=0.5s reconcile=0.17s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.5s. run=#5107 https://github.com/28twagg-ops/TradingBot/actions/runs/30268635225
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T09:06:19.657536_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 3 | 3 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 17 | 10 | 1.7 | ~23 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 4 | 3 | 1.3 | ~29 active signal-days |
| S168 | 3 | 2 | 1.5 | ~25 active signal-days |
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
| w1     |    1 |    1 |    5 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    16 |
| w2     |    2 |    2 |    8 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 175 | 3 |
| S164 | 211 | 4 |
| S165 | 1643 | 17 |
| S166 | 75 | 1 |
| S167 | 197 | 4 |
| S168 | 130 | 3 |
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
equity=488.04 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T131040Z

- UTC timestamp: `20260727T131040Z`
- GitHub run: [#5108](https://github.com/28twagg-ops/TradingBot/actions/runs/30269009024)
- Run id: `30269009024`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T09:10:44.435455-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.4,"phases_s":{"reconcile":0.14},"signals":0,"placed":0,"equity":133643.91,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5108","github_run_id":"30269009024","status":"ok"}
```

### Live bot full output

```text
13:10:41  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $488.04|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $488.04|
|  Cash                                                            $73.64|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $414.40|
|  Open P&L                                                        $+5.41|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABNB     Pullback50      $99.13     $139.66  $142.70  +2.2%   $+2.11  |
|  CARR     Pullback50      $97.59     $67.80   $68.95   +1.7%   $+1.63  |
|  CL       Pullback50      $97.52     $90.74   $90.90   +0.2%   $+0.17  |
|  DTE      Pullback50      $97.38     $147.63  $149.46  +1.2%   $+1.19  |
|  LNT      Pullback50      $22.77     $73.97   $74.94   +1.3%   $+0.30  |
|                                                                        |
|  Total invested                                                 $414.40|
|  Total open P&L                                                  $+5.41|
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
|  2026-07-24  SELL  CHD  Pullback50  $97.41  P&L $+0.12                 |
|  2026-07-24  SELL  CI  Pullback50  $97.40  P&L $+0.93                  |
|  2026-07-24  SELL  AEP  Pullback50  $99.33  P&L $+2.96                 |
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
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
=== options_morning_bot (PAPER) 2026-07-27T09:10:44.435455-04:00 ===

[Run context]
After hours (09:10 ET) — exit summary only.
Paper auth OK — equity $133643.91, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,643.91                             |
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
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=0.4s reconcile=0.14s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.4s. run=#5108 https://github.com/28twagg-ops/TradingBot/actions/runs/30269009024
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T09:10:49.465246_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 3 | 3 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 17 | 10 | 1.7 | ~23 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 4 | 3 | 1.3 | ~29 active signal-days |
| S168 | 3 | 2 | 1.5 | ~25 active signal-days |
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
| w1     |    1 |    1 |    5 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    16 |
| w2     |    2 |    2 |    8 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 175 | 3 |
| S164 | 211 | 4 |
| S165 | 1643 | 17 |
| S166 | 75 | 1 |
| S167 | 197 | 4 |
| S168 | 130 | 3 |
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
equity=488.04 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T131539Z

- UTC timestamp: `20260727T131539Z`
- GitHub run: [#5109](https://github.com/28twagg-ops/TradingBot/actions/runs/30269395743)
- Run id: `30269395743`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T09:15:41.806062-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.5,"phases_s":{"reconcile":0.21},"signals":0,"placed":0,"equity":133491.91,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5109","github_run_id":"30269395743","status":"ok"}
```

### Live bot full output

```text
13:15:39  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $488.01|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $488.01|
|  Cash                                                            $73.64|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $414.37|
|  Open P&L                                                        $+5.37|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABNB     Pullback50      $99.10     $139.66  $142.65  +2.1%   $+2.08  |
|  CARR     Pullback50      $97.59     $67.80   $68.95   +1.7%   $+1.63  |
|  CL       Pullback50      $97.52     $90.74   $90.90   +0.2%   $+0.17  |
|  DTE      Pullback50      $97.38     $147.63  $149.46  +1.2%   $+1.19  |
|  LNT      Pullback50      $22.77     $73.97   $74.94   +1.3%   $+0.30  |
|                                                                        |
|  Total invested                                                 $414.37|
|  Total open P&L                                                  $+5.37|
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
|  2026-07-24  SELL  CHD  Pullback50  $97.41  P&L $+0.12                 |
|  2026-07-24  SELL  CI  Pullback50  $97.40  P&L $+0.93                  |
|  2026-07-24  SELL  AEP  Pullback50  $99.33  P&L $+2.96                 |
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
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
=== options_morning_bot (PAPER) 2026-07-27T09:15:41.806062-04:00 ===

[Run context]
After hours (09:15 ET) — exit summary only.
Paper auth OK — equity $133491.91, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,491.91                             |
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
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=0.5s reconcile=0.21s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.5s. run=#5109 https://github.com/28twagg-ops/TradingBot/actions/runs/30269395743
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T09:15:46.965172_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 3 | 3 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 17 | 10 | 1.7 | ~23 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 4 | 3 | 1.3 | ~29 active signal-days |
| S168 | 3 | 2 | 1.5 | ~25 active signal-days |
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
| w1     |    1 |    1 |    5 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    16 |
| w2     |    2 |    2 |    8 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 175 | 3 |
| S164 | 211 | 4 |
| S165 | 1643 | 17 |
| S166 | 75 | 1 |
| S167 | 197 | 4 |
| S168 | 130 | 3 |
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
equity=488.01 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T132037Z

- UTC timestamp: `20260727T132037Z`
- GitHub run: [#5110](https://github.com/28twagg-ops/TradingBot/actions/runs/30269784923)
- Run id: `30269784923`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T09:20:41.449969-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.53},"signals":0,"placed":0,"equity":133450.83,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5110","github_run_id":"30269784923","status":"ok"}
```

### Live bot full output

```text
13:20:38  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $488.01|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $488.01|
|  Cash                                                            $73.64|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $414.37|
|  Open P&L                                                        $+5.37|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABNB     Pullback50      $99.10     $139.66  $142.65  +2.1%   $+2.08  |
|  CARR     Pullback50      $97.59     $67.80   $68.95   +1.7%   $+1.63  |
|  CL       Pullback50      $97.52     $90.74   $90.90   +0.2%   $+0.17  |
|  DTE      Pullback50      $97.38     $147.63  $149.46  +1.2%   $+1.19  |
|  LNT      Pullback50      $22.77     $73.97   $74.94   +1.3%   $+0.30  |
|                                                                        |
|  Total invested                                                 $414.37|
|  Total open P&L                                                  $+5.37|
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
|  2026-07-24  SELL  CHD  Pullback50  $97.41  P&L $+0.12                 |
|  2026-07-24  SELL  CI  Pullback50  $97.40  P&L $+0.93                  |
|  2026-07-24  SELL  AEP  Pullback50  $99.33  P&L $+2.96                 |
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
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
=== options_morning_bot (PAPER) 2026-07-27T09:20:41.449969-04:00 ===

[Run context]
After hours (09:20 ET) — exit summary only.
Paper auth OK — equity $133450.83, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,450.83                             |
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
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=1.0s reconcile=0.53s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.0s. run=#5110 https://github.com/28twagg-ops/TradingBot/actions/runs/30269784923
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T09:20:47.099843_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 3 | 3 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 17 | 10 | 1.7 | ~23 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 4 | 3 | 1.3 | ~29 active signal-days |
| S168 | 3 | 2 | 1.5 | ~25 active signal-days |
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
| w1     |    1 |    1 |    5 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    16 |
| w2     |    2 |    2 |    8 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 175 | 3 |
| S164 | 211 | 4 |
| S165 | 1643 | 17 |
| S166 | 75 | 1 |
| S167 | 197 | 4 |
| S168 | 130 | 3 |
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
equity=488.01 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T132542Z

- UTC timestamp: `20260727T132542Z`
- GitHub run: [#5111](https://github.com/28twagg-ops/TradingBot/actions/runs/30270174127)
- Run id: `30270174127`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T09:25:46.778135-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":133163.91,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5111","github_run_id":"30270174127","status":"ok"}
```

### Live bot full output

```text
13:25:43  INFO      Mode: summary

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                           SUMMARY|
|  Time                                                         13:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $488.01|
+========================================================================+

+========================================================================+
|                             ACCOUNT STATUS                             |
+========================================================================+
|  Equity                                                         $488.01|
|  Cash                                                            $73.64|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Total invested                                                 $414.37|
|  Open P&L                                                        $+5.37|
+========================================================================+

+========================================================================+
|                        HOLDINGS  (5 positions)                         |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABNB     Pullback50      $99.10     $139.66  $142.65  +2.1%   $+2.08  |
|  CARR     Pullback50      $97.59     $67.80   $68.95   +1.7%   $+1.63  |
|  CL       Pullback50      $97.52     $90.74   $90.90   +0.2%   $+0.17  |
|  DTE      Pullback50      $97.38     $147.63  $149.46  +1.2%   $+1.19  |
|  LNT      Pullback50      $22.77     $73.97   $74.94   +1.3%   $+0.30  |
|                                                                        |
|  Total invested                                                 $414.37|
|  Total open P&L                                                  $+5.37|
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
|  2026-07-24  SELL  CHD  Pullback50  $97.41  P&L $+0.12                 |
|  2026-07-24  SELL  CI  Pullback50  $97.40  P&L $+0.93                  |
|  2026-07-24  SELL  AEP  Pullback50  $99.33  P&L $+2.96                 |
|  2026-07-23  SELL  FIX  Pullback50  $96.39  P&L $+0.32                 |
|  2026-07-23  SELL  C  Pullback50  $69.34  P&L $-0.52                   |
|  2026-07-23  SELL  CHD  Pullback50  $95.22  P&L $-1.19                 |
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
=== options_morning_bot (PAPER) 2026-07-27T09:25:46.778135-04:00 ===

[Run context]
After hours (09:25 ET) — exit summary only.
Paper auth OK — equity $133163.91, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $133,163.91                             |
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
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=1.0s reconcile=0.54s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=1.0s. run=#5111 https://github.com/28twagg-ops/TradingBot/actions/runs/30270174127
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T09:25:52.470917_

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

## Per-strategy summary (unique underlyings)

| Strategy | Unique entries | Active days | Avg unique / active day | Est. active days to n=30 exits* |
|----------|---------------:|------------:|------------------------:|--------------------------------|
| S163 | 3 | 3 | 1.0 | ~38 active signal-days |
| S164 | 4 | 3 | 1.3 | ~29 active signal-days |
| S165 | 17 | 10 | 1.7 | ~23 active signal-days |
| S166 | 1 | 1 | 1.0 | ~38 active signal-days |
| S167 | 4 | 3 | 1.3 | ~29 active signal-days |
| S168 | 3 | 2 | 1.5 | ~25 active signal-days |
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
| w1     |    1 |    1 |    5 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    7 |    1 |    16 |
| w2     |    2 |    2 |    8 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 175 | 3 |
| S164 | 211 | 4 |
| S165 | 1643 | 17 |
| S166 | 75 | 1 |
| S167 | 197 | 4 |
| S168 | 130 | 3 |
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
equity=488.01 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T133042Z

- UTC timestamp: `20260727T133042Z`
- GitHub run: [#5112](https://github.com/28twagg-ops/TradingBot/actions/runs/30270559977)
- Run id: `30270559977`
- Live bot: exit=`0`, duration=`218s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T09:25:46.778135-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":133163.91,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5111","github_run_id":"30270174127","status":"ok"}
```

### Live bot full output

```text
13:30:43  INFO      Mode: morning_prep
13:30:44  INFO        [prep_positions] 5/5 (5 valid)
13:30:44  INFO      Fetching tickers (universe=both)...
13:30:45  INFO        S&P 500: 503
13:30:45  INFO        MidCap 400: 400
13:30:45  INFO        Total: 903 tickers
13:30:46  INFO        [prep_universe] 40/898 (40 valid)
13:30:48  INFO        [prep_universe] 80/898 (80 valid)
13:30:49  INFO        [prep_universe] 120/898 (120 valid)
13:30:50  INFO        [prep_universe] 160/898 (160 valid)
13:30:52  INFO        [prep_universe] 200/898 (199 valid)
13:30:59  INFO        [prep_universe] 240/898 (238 valid)
13:31:10  INFO        [prep_universe] 280/898 (278 valid)
13:31:24  INFO        [prep_universe] 320/898 (318 valid)
13:31:34  INFO        [prep_universe] 360/898 (358 valid)
13:31:48  INFO        [prep_universe] 400/898 (397 valid)
13:31:58  INFO        [prep_universe] 440/898 (437 valid)
13:32:12  INFO        [prep_universe] 480/898 (477 valid)
13:32:22  INFO        [prep_universe] 520/898 (517 valid)
13:32:35  INFO        [prep_universe] 560/898 (557 valid)
13:32:46  INFO        [prep_universe] 600/898 (597 valid)
13:32:59  INFO        [prep_universe] 640/898 (637 valid)
13:33:12  INFO        [prep_universe] 680/898 (677 valid)
13:33:23  INFO        [prep_universe] 720/898 (717 valid)
13:33:36  INFO        [prep_universe] 760/898 (757 valid)
13:33:47  INFO        [prep_universe] 800/898 (797 valid)
13:34:00  INFO        [prep_universe] 840/898 (836 valid)
13:34:10  INFO        [prep_universe] 880/898 (876 valid)
13:34:17  INFO        [prep_universe] 898/898 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $489.99|
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
|  Open positions                                                       5|
|  Invested                                                       $416.35|
|  Open P&L                                                        $+7.36|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABNB     Pullback50      $100.69    $139.66  $144.94  +3.8%   $+3.67  |
|  CARR     Pullback50      $98.14     $67.80   $69.34   +2.3%   $+2.18  |
|  CL       Pullback50      $98.33     $90.74   $91.66   +1.0%   $+0.98  |
|  DTE      Pullback50      $96.42     $147.63  $147.98  +0.2%   $+0.23  |
|  LNT      Pullback50      $22.77     $73.97   $74.94   +1.3%   $+0.30  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  CARR      OrderType.STOP    1         None        68.48               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      5|
|  Signal candidates                                                   27|
|  Universe scanned                                                   898|
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
=== options_morning_bot (PAPER) 2026-07-27T09:34:21.587779-04:00 ===

[Run context]
Paper auth OK — equity $132235.91, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
```

---

## Run 20260727T133603Z

- UTC timestamp: `20260727T133603Z`
- GitHub run: [#5113](https://github.com/28twagg-ops/TradingBot/actions/runs/30270955114)
- Run id: `30270955114`
- Live bot: exit=`0`, duration=`220s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T09:25:46.778135-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":133163.91,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5111","github_run_id":"30270174127","status":"ok"}
```

### Live bot full output

```text
13:36:04  INFO      Mode: morning_prep
13:36:06  INFO        [prep_positions] 5/5 (5 valid)
13:36:06  INFO      Fetching tickers (universe=both)...
13:36:06  INFO        S&P 500: 503
13:36:06  INFO        MidCap 400: 400
13:36:06  INFO        Total: 903 tickers
13:36:08  INFO        [prep_universe] 40/898 (40 valid)
13:36:09  INFO        [prep_universe] 80/898 (80 valid)
13:36:10  INFO        [prep_universe] 120/898 (120 valid)
13:36:12  INFO        [prep_universe] 160/898 (160 valid)
13:36:13  INFO        [prep_universe] 200/898 (199 valid)
13:36:20  INFO        [prep_universe] 240/898 (238 valid)
13:36:34  INFO        [prep_universe] 280/898 (278 valid)
13:36:44  INFO        [prep_universe] 320/898 (318 valid)
13:36:57  INFO        [prep_universe] 360/898 (358 valid)
13:37:08  INFO        [prep_universe] 400/898 (397 valid)
13:37:21  INFO        [prep_universe] 440/898 (437 valid)
13:37:31  INFO        [prep_universe] 480/898 (477 valid)
13:37:45  INFO        [prep_universe] 520/898 (517 valid)
13:37:58  INFO        [prep_universe] 560/898 (557 valid)
13:38:08  INFO        [prep_universe] 600/898 (597 valid)
13:38:22  INFO        [prep_universe] 640/898 (637 valid)
13:38:32  INFO        [prep_universe] 680/898 (677 valid)
13:38:45  INFO        [prep_universe] 720/898 (717 valid)
13:38:56  INFO        [prep_universe] 760/898 (757 valid)
13:39:09  INFO        [prep_universe] 800/898 (797 valid)
13:39:19  INFO        [prep_universe] 840/898 (836 valid)
13:39:33  INFO        [prep_universe] 880/898 (876 valid)
13:39:39  INFO        [prep_universe] 898/898 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $490.41|
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
|  Open positions                                                       5|
|  Invested                                                       $416.78|
|  Open P&L                                                        $+7.78|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABNB     Pullback50      $100.47    $139.66  $144.62  +3.6%   $+3.45  |
|  CARR     Pullback50      $98.55     $67.80   $69.62   +2.7%   $+2.59  |
|  CL       Pullback50      $98.27     $90.74   $91.60   +0.9%   $+0.92  |
|  DTE      Pullback50      $96.79     $147.63  $148.55  +0.6%   $+0.60  |
|  LNT      Pullback50      $22.70     $73.97   $74.70   +1.0%   $+0.22  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  CARR      OrderType.STOP    1         None        68.48               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      5|
|  Signal candidates                                                   34|
|  Universe scanned                                                   898|
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
=== options_morning_bot (PAPER) 2026-07-27T09:39:44.747346-04:00 ===

[Run context]
Paper auth OK — equity $131911.91, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
```

---

## Run 20260727T134101Z

- UTC timestamp: `20260727T134101Z`
- GitHub run: [#5114](https://github.com/28twagg-ops/TradingBot/actions/runs/30271344795)
- Run id: `30271344795`
- Live bot: exit=`0`, duration=`217s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T09:25:46.778135-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":133163.91,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5111","github_run_id":"30270174127","status":"ok"}
```

### Live bot full output

```text
13:41:01  INFO      Mode: morning_prep
13:41:02  INFO        [prep_positions] 5/5 (5 valid)
13:41:02  INFO        Universe cache hit: 903 tickers (tickers_2026-07-27.json)
13:41:03  INFO        [prep_universe] 40/898 (40 valid)
13:41:05  INFO        [prep_universe] 80/898 (80 valid)
13:41:06  INFO        [prep_universe] 120/898 (120 valid)
13:41:07  INFO        [prep_universe] 160/898 (160 valid)
13:41:09  INFO        [prep_universe] 200/898 (199 valid)
13:41:16  INFO        [prep_universe] 240/898 (238 valid)
13:41:29  INFO        [prep_universe] 280/898 (278 valid)
13:41:42  INFO        [prep_universe] 320/898 (318 valid)
13:41:52  INFO        [prep_universe] 360/898 (358 valid)
13:42:05  INFO        [prep_universe] 400/898 (397 valid)
13:42:18  INFO        [prep_universe] 440/898 (437 valid)
13:42:28  INFO        [prep_universe] 480/898 (477 valid)
13:42:41  INFO        [prep_universe] 520/898 (517 valid)
13:42:54  INFO        [prep_universe] 560/898 (557 valid)
13:43:04  INFO        [prep_universe] 600/898 (597 valid)
13:43:17  INFO        [prep_universe] 640/898 (637 valid)
13:43:30  INFO        [prep_universe] 680/898 (677 valid)
13:43:43  INFO        [prep_universe] 720/898 (717 valid)
13:43:53  INFO        [prep_universe] 760/898 (757 valid)
13:44:05  INFO        [prep_universe] 800/898 (797 valid)
13:44:18  INFO        [prep_universe] 840/898 (836 valid)
13:44:29  INFO        [prep_universe] 880/898 (876 valid)
13:44:35  INFO        [prep_universe] 898/898 (894 valid)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_PREP|
|  Time                                                         13:41 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $490.76|
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
|  Open positions                                                       5|
|  Invested                                                       $417.12|
|  Open P&L                                                        $+8.13|
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  ABNB     Pullback50      $100.31    $139.66  $144.39  +3.4%   $+3.29  |
|  CARR     Pullback50      $98.50     $67.80   $69.59   +2.6%   $+2.54  |
|  CL       Pullback50      $98.53     $90.74   $91.84   +1.2%   $+1.18  |
|  DTE      Pullback50      $97.08     $147.63  $149.00  +0.9%   $+0.89  |
|  LNT      Pullback50      $22.71     $73.97   $74.73   +1.0%   $+0.23  |
+========================================================================+

+========================================================================+
|                            OPEN SELL ORDERS                            |
+========================================================================+
|  Count                                                                1|
|  TICKER    TYPE              QTY       LIMIT       STOP                |
+------------------------------------------------------------------------+
|  CARR      OrderType.STOP    1         None        68.48               |
+========================================================================+

+========================================================================+
|                              PREP SUMMARY                              |
+========================================================================+
|  Saved                                                              yes|
|  Exit candidates                                                      5|
|  Signal candidates                                                   36|
|  Universe scanned                                                   898|
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
=== options_morning_bot (PAPER) 2026-07-27T09:44:39.884068-04:00 ===

[Run context]
Paper auth OK — equity $131480.03, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
```

---

## Run 20260727T134601Z

- UTC timestamp: `20260727T134601Z`
- GitHub run: [#5115](https://github.com/28twagg-ops/TradingBot/actions/runs/30271735776)
- Run id: `30271735776`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T09:25:46.778135-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":133163.91,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5111","github_run_id":"30270174127","status":"ok"}
```

### Live bot full output

```text
13:46:02  INFO      Mode: morning_scan
13:46:03  INFO        [positions] 5/5 (5 valid)
13:46:04  INFO        SELL LIMIT DTE  qty=0.651561335  limit=$148.97  id=c97a7651-cc13-4204-8a93-ee2ff76c77d5
13:46:24  INFO        SELL LIMIT not filled for DTE, falling back to market
13:46:24  WARNING     SELL DTE: {"available":"0","code":40310000,"existing_qty":"0.651561335","held_for_orders":"0.651561335","message":"insufficient qty available for order (requested: 0.651561335, available: 0)","symbol":"DTE"}
13:46:25  INFO        SELL LIMIT LNT  qty=0.303842305  limit=$74.78  id=988371df-2072-4d41-973a-c52a12ec7d9d
13:46:45  INFO        SELL LIMIT filled LNT (confirmed by position check)
13:46:45  INFO        TX logged: SELL LNT  P&L 1.18%
13:46:45  INFO        SELL LIMIT CL  qty=1.072869139  limit=$91.73  id=428bef15-81ec-45c7-b914-111f014403b0
13:47:06  INFO        SELL LIMIT filled CL (confirmed by position check)
13:47:06  INFO        TX logged: SELL CL  P&L 1.2%
13:47:06  INFO        SELL order cancelled CARR  type=OrderType.STOP  id=1dc8d077-e605-474d-bff1-e811869c8b14
13:47:06  INFO        SELL LIMIT CARR  qty=1.415380984  limit=$69.20  id=18160796-23e7-46d3-81a8-0dee7af93385
13:47:27  INFO        SELL LIMIT filled CARR (confirmed by position check)
13:47:27  INFO        TX logged: SELL CARR  P&L 2.29%
13:47:27  INFO        SELL LIMIT ABNB  qty=0.694697045  limit=$143.75  id=7132372d-d9f4-4ad3-ad1e-ea6249d07ee5
13:47:48  INFO        SELL LIMIT filled ABNB (confirmed by position check)
13:47:48  INFO        TX logged: SELL ABNB  P&L 3.14%
13:47:48  INFO        Universe cache hit: 903 tickers (tickers_2026-07-27.json)
13:47:49  INFO        [universe] 40/902 (40 valid)
13:47:51  INFO        [universe] 80/902 (80 valid)
13:47:52  INFO        [universe] 120/902 (120 valid)
13:47:53  INFO        [universe] 160/902 (160 valid)
13:47:55  INFO        [universe] 200/902 (199 valid)
13:48:02  INFO        [universe] 240/902 (238 valid)
13:48:12  INFO        [universe] 280/902 (278 valid)
13:48:26  INFO        [universe] 320/902 (318 valid)
13:48:36  INFO        [universe] 360/902 (358 valid)
13:48:49  INFO        [universe] 400/902 (397 valid)
13:49:03  INFO        [universe] 440/902 (437 valid)
13:49:13  INFO        [universe] 480/902 (477 valid)
13:49:26  INFO        [universe] 520/902 (517 valid)
13:49:37  INFO        [universe] 560/902 (557 valid)
13:49:50  INFO        [universe] 600/902 (597 valid)
13:50:01  INFO        [universe] 640/902 (637 valid)
13:50:14  INFO        [universe] 680/902 (677 valid)
```

### Options bot full output

```text

## Run 20260727T135105Z

- UTC timestamp: `20260727T135105Z`
- GitHub run: [#5116](https://github.com/28twagg-ops/TradingBot/actions/runs/30272131822)
- Run id: `30272131822`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T09:25:46.778135-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":133163.91,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5111","github_run_id":"30270174127","status":"ok"}
```

### Live bot full output

```text
13:51:06  INFO      Mode: morning_scan
13:51:07  INFO        [positions] 1/1 (1 valid)
13:51:08  INFO        SELL LIMIT DTE  qty=0.651561335  limit=$148.41  id=8cd79e7a-d104-4d90-b24d-54daffff0c30
13:51:28  INFO        SELL LIMIT filled DTE (confirmed by position check)
13:51:28  INFO        TX logged: SELL DTE  P&L 0.73%
13:51:28  INFO        Universe cache hit: 903 tickers (tickers_2026-07-27.json)
13:51:29  INFO        [universe] 40/903 (40 valid)
13:51:30  INFO        [universe] 80/903 (80 valid)
13:51:31  INFO        [universe] 120/903 (120 valid)
13:51:32  INFO        [universe] 160/903 (160 valid)
13:51:34  INFO        [universe] 200/903 (199 valid)
13:51:41  INFO        [universe] 240/903 (238 valid)
13:51:54  INFO        [universe] 280/903 (278 valid)
13:52:07  INFO        [universe] 320/903 (318 valid)
13:52:17  INFO        [universe] 360/903 (358 valid)
13:52:30  INFO        [universe] 400/903 (397 valid)
13:52:43  INFO        [universe] 440/903 (437 valid)
13:52:53  INFO        [universe] 480/903 (477 valid)
13:53:06  INFO        [universe] 520/903 (517 valid)
13:53:19  INFO        [universe] 560/903 (557 valid)
13:53:29  INFO        [universe] 600/903 (597 valid)
13:53:42  INFO        [universe] 640/903 (637 valid)
13:53:55  INFO        [universe] 680/903 (677 valid)
13:54:05  INFO        [universe] 720/903 (717 valid)
13:54:18  INFO        [universe] 760/903 (757 valid)
13:54:28  INFO        [universe] 800/903 (797 valid)
13:54:41  INFO        [universe] 840/903 (836 valid)
13:54:54  INFO        [universe] 880/903 (876 valid)
13:55:01  INFO        [universe] 903/903 (899 valid)
13:55:03  INFO        BUY  ALGN  $97.94  [Pullback50]  id=ff99fcce-19dd-4151-bb3e-a0b01e00f7cb

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                      MORNING_SCAN|
|  Time                                                         13:51 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $489.72|
+========================================================================+

+========================================================================+
|                   RUBBER BAND BOT v8  --  DAILY SCAN                   |
+========================================================================+
|  Mode                                                      *** LIVE ***|
|  Date                                                        2026-07-27|
|  Universe                                                          both|
|  Mon~  Jul: 52wkLow + Pullback50 (display only — schedule not enforced)|
|  Disabled                GapDown, VolumeSpike (see DISABLED_STRATEGIES)|
|  Regime                                                            BULL|
|  Exit                                      midline / stop-0.5% / 3d max|
+========================================================================+

+========================================================================+
|                                ACCOUNT                                 |
+========================================================================+
|  Equity                                                         $489.72|
|  Cash                                                           $392.83|
|  Reserve                                          $24.49  (always kept)|
|  Available                                    $368.34  (for new trades)|
|  Trade size             $97.94  (20% per signal — all strategies equal)|
+========================================================================+

+========================================================================+
|                           HOLDINGS  (1 open)                           |
+========================================================================+
|  TICKER   STRATEGY        INVESTED   ENTRY    NOW      P&L%    P&L$    |
+------------------------------------------------------------------------+
|  DTE      Pullback50      $96.89     $147.63  $148.71  +0.7%   $+0.70  |
|                                                                        |
|  Total invested                                                  $96.89|
|  Total open P&L                                                  $+0.70|
|  Buys today: 0  |  entry cap: 4  |  max open: 5                        |
+========================================================================+

+========================================================================+
|                               PLAN CACHE                               |
+========================================================================+
|  Mode                                                           morning|
|  File                                      logs/plans/morning_plan.json|
|  Use cached plan                                  no (stale (25925.6m))|
+========================================================================+

+========================================================================+
|          EXIT EVALUATION  (EOD -- midline + stop + max-hold)           |
+========================================================================+
|  DTE  P&L +0.7%  $+0.70                       EXIT: max_hold 4d (+0.7%)|
+========================================================================+

+========================================================================+
|                           EXIT EVAL SUMMARY                            |
+========================================================================+
|  Exit eval    attempted 1 | filled 1 | partial 0 | pending 0 | failed 0|
|  Other skips     already logged today 0  |  no price data 0  |  holds 0|
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
|                         SIGNALS FOUND  --  24                          |
+========================================================================+
|  TICKER   STRATEGY        TIER   PRICE    RSI    VOL_Z   TRIGGER       |
+------------------------------------------------------------------------+
|  ALGN     Pullback50      eq     $171.44  34.7   -1.95   50MA bounce (-|
|  APA      Pullback50      eq     $35.77   60.8   -2.67   50MA bounce (+|
|  CMS      Pullback50      eq     $74.58   36.6   -2.58   50MA bounce (+|
|  DRI      Pullback50      eq     $202.53  47.4   -3.00   50MA bounce (+|
|  DVN      Pullback50      eq     $44.20   60.8   -2.25   50MA bounce (-|
|  EQR      Pullback50      eq     $67.65   36.5   -2.44   50MA bounce (+|
|  FFIV     Pullback50      eq     $400.95  42.4   -2.62   50MA bounce (+|
|  HUBB     Pullback50      eq     $490.00  57.4   -2.30   50MA bounce (+|
|  MAR      Pullback50      eq     $380.01  49.4   -2.96   50MA bounce (+|
|  PG       Pullback50      eq     $148.36  40.5   -2.65   50MA bounce (+|
|  RL       Pullback50      eq     $382.66  44.9   -2.80   50MA bounce (+|
|  STLD     Pullback50      eq     $248.36  70.1   -2.81   50MA bounce (+|
|  TJX      Pullback50      eq     $156.07  56.0   -3.05   50MA bounce (-|
|  WST      Pullback50      eq     $333.19  35.0   -1.75   50MA bounce (-|
|  WY       Pullback50      eq     $24.17   59.3   -2.60   50MA bounce (+|
|  ALLY     Pullback50      eq     $43.77   41.3   -2.04   50MA bounce (-|
|  BHF      Pullback50      eq     $63.44   36.9   -2.07   50MA bounce (-|
|  BC       Pullback50      eq     $81.52   59.9   -2.75   50MA bounce (+|
|  CART     Pullback50      eq     $43.78   29.8   -2.56   50MA bounce (-|
|  EVR      Pullback50      eq     $348.60  50.9   -3.40   50MA bounce (+|
|  IRT      Pullback50      eq     $16.56   34.6   -1.93   50MA bounce (-|
|  PEN      Pullback50      eq     $319.28  53.3   -2.06   50MA bounce (-|
|  TREX     Pullback50      eq     $44.19   39.2   -1.84   50MA bounce (+|
|  TXNM     Pullback50      eq     $58.44   84.5   -0.87   50MA bounce (+|
|                                                                        |
+========================================================================+

+========================================================================+
|                              ENTRY ORDERS                              |
+========================================================================+
|    ENTER [eq] ALGN  Pullback50                                   $97.94|
|    BUY SUBMITTED [e~  fill pending — batched confirmation after entries|13:55:03  INFO        BUY  APA  $97.94  [Pullback50]  id=c14973b5-72e4-4692-9489-bb2a3435be65
13:55:04  INFO        BUY  CMS  $97.94  [Pullback50]  id=78497760-b8e1-4d47-ac2f-5f55c3c920c6
13:55:04  INFO        BUY  DRI  $97.94  [Pullback50]  id=5d32b724-6e7e-45db-ad23-dd90429e3252
13:55:04  INFO        BUY  DVN  $73.38  [Pullback50]  id=d378f49c-2ee2-4f4a-aecb-d5809bbff941
```

### Options bot full output

```text

## Run 20260727T135639Z

- UTC timestamp: `20260727T135639Z`
- GitHub run: [#5117](https://github.com/28twagg-ops/TradingBot/actions/runs/30272537767)
- Run id: `30272537767`
- Live bot: exit=`0`, duration=`0s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T09:25:46.778135-04:00","date":"2026-07-27","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":1.0,"phases_s":{"reconcile":0.54},"signals":0,"placed":0,"equity":133163.91,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":0,"filled_today":0,"unattributed_contracts":0,"top_signals":[],"github_run":"5111","github_run_id":"30270174127","status":"ok"}
```

### Live bot full output

```text
13:56:39  INFO      Mode: morning_scan
13:56:41  INFO        [positions] 5/5 (5 valid)
13:56:41  INFO        SELL LIMIT DVN  qty=1.656806069  limit=$44.14  id=60c4428c-eee6-4bb1-b974-72492c4e6d7a
13:57:12  INFO        SELL LIMIT filled DVN (confirmed by position check)
13:57:12  INFO        TX logged: SELL DVN  P&L -0.3%
13:57:12  INFO        SELL LIMIT APA  qty=2.734866003  limit=$35.73  id=ed6063c0-039c-41a3-b79b-27921b79a773
13:57:43  INFO        SELL LIMIT filled APA (confirmed by position check)
13:57:43  INFO        TX logged: SELL APA  P&L -0.18%
13:57:43  INFO        SELL LIMIT DRI  qty=0.483351924  limit=$201.61  id=275a3fbb-2568-43b7-8c1c-fa58ea4d069a
13:58:14  INFO        SELL LIMIT filled DRI (confirmed by position check)
13:58:14  INFO        TX logged: SELL DRI  P&L -0.14%
13:58:14  INFO        Universe cache hit: 903 tickers (tickers_2026-07-27.json)
13:58:15  INFO        [universe] 40/901 (40 valid)
13:58:16  INFO        [universe] 80/901 (80 valid)
13:58:17  INFO        [universe] 120/901 (120 valid)
13:58:19  INFO        [universe] 160/901 (160 valid)
13:58:20  INFO        [universe] 200/901 (199 valid)
13:58:27  INFO        [universe] 240/901 (238 valid)
13:58:41  INFO        [universe] 280/901 (278 valid)
13:58:51  INFO        [universe] 320/901 (318 valid)
13:59:04  INFO        [universe] 360/901 (358 valid)
13:59:15  INFO        [universe] 400/901 (397 valid)
13:59:28  INFO        [universe] 440/901 (437 valid)
13:59:38  INFO        [universe] 480/901 (477 valid)
13:59:52  INFO        [universe] 520/901 (517 valid)
14:00:05  INFO        [universe] 560/901 (557 valid)
14:00:15  INFO        [universe] 600/901 (597 valid)
```

### Options bot full output

```text

## Run 20260727T140102Z

- UTC timestamp: `20260727T140102Z`
- GitHub run: [#5118](https://github.com/28twagg-ops/TradingBot/actions/runs/30272934206)
- Run id: `30272934206`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`183s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T10:01:07.866249-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (24 new)","elapsed_s":176.0,"phases_s":{"reconcile":0.09,"cancel":0.03,"manage":0.02,"scan":164.59,"entries":10.76,"reconcile2":0.18},"signals":305,"placed":24,"equity":130683.91,"open_positions":5,"pending_orders":15,"open_lots":10,"submitted_today":24,"filled_today":9,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5118","github_run_id":"30272934206","status":"ok"}
```

### Live bot full output

```text
14:01:03  INFO      Mode: exits
14:01:03  INFO        Daily log -> logs/daily/2026-07-27.md
14:01:03  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (5 ledger rows)
14:01:03  INFO        place_all_stops: checking 2 positions...
14:01:03  INFO        STOP skipped ALGN: fractional (0.5700 shares) — software exit will handle it
14:01:03  INFO        STOP-MARKET placed CMS  qty=1 (pos=1.3097)  stop=$74.40  id=13c276ab-bee9-4536-bdbe-2b60ca844e43
14:01:04  INFO        [positions] 2/2 (2 valid)
14:01:04  INFO        SELL MARKET [urgent] ALGN closed
14:01:06  INFO        TX logged: SELL ALGN  P&L -0.89%
14:01:06  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.86|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  ALGN  P&L -0.9%  $-0.87                        EXIT: stop_loss (-0.9%)|
|  CMS  P&L -0.1%  $-0.06                                            HOLD|
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
|  ALGN                                        -0.89%  (threshold -0.50%)|
|  Count                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-27T10:01:07.866249-04:00 ===

[Run context]
Paper auth OK — equity $130683.91, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 305 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $130200 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 104 no tradeable call, 482 pending order
Placed 24 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $130,683.91                             |
|  Signals this run              305                                     |
|  Orders submitted (session)    24                                      |
|  Orders filled today (ledger)  9                                       |
|  Entries placed this run       24                                      |
|  Open virtual lots             10                                      |
|  Broker option positions       5                                       |
|  Pending orders                15                                      |
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
|  PENDING ORDERS (15)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:APA(2), S168:APA(2), S167:APA(2)   |
+------------------------------------------------------------------------+
|  b16  S165 APA      limit=0.21                                         |
|  b17  S165 APA      limit=0.21                                         |
|  b40  S168 APA      limit=0.33                                         |
|  b41  S168 APA      limit=0.33                                         |
|  b32  S167 APA      limit=0.21                                         |
|  ... 10 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (5)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CCL260731P00027000            2    -15.1%   $    -22.00               |
|  UBER260731C00069000           2    -10.9%   $    -10.00               |
|  EQT260731C00053000            2     -6.6%   $     -8.00               |
|  GOOGL260729C00340000          2     -5.6%   $     -8.00               |
|  IBM260731C00235000            2     -5.6%   $     -6.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=176.0s reconcile=0.09s cancel=0.03s manage=0.02s scan=164.59s entries=10.76s
STATUS: options_morning_bot run complete (PAPER) elapsed=176.0s. run=#5118 https://github.com/28twagg-ops/TradingBot/actions/runs/30272934206
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T10:04:08.548055_

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
| w2     |    2 |    2 |    8 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 177 | 4 |
| S164 | 211 | 4 |
| S165 | 1645 | 18 |
| S166 | 77 | 2 |
| S167 | 199 | 5 |
| S168 | 132 | 4 |
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
| 2026-07-27 |    2 |    0 |    2 |    2 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    10 |

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
| State/ledger mismatches     |     1 | WARN | <<<
| Total open lots             |    10 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=487.92 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T140540Z

- UTC timestamp: `20260727T140540Z`
- GitHub run: [#5119](https://github.com/28twagg-ops/TradingBot/actions/runs/30273339135)
- Run id: `30273339135`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`202s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T10:05:43.996506-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (24 new)","elapsed_s":194.2,"phases_s":{"reconcile":0.2,"cancel":0.03,"manage":0.01,"scan":180.89,"entries":12.62,"reconcile2":0.19},"signals":311,"placed":24,"equity":130423.51,"open_positions":2,"pending_orders":30,"open_lots":8,"submitted_today":48,"filled_today":18,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5119","github_run_id":"30273339135","status":"ok"}
```

### Live bot full output

```text
14:05:41  INFO      Mode: exits
14:05:41  INFO        Daily log -> logs/daily/2026-07-27.md
14:05:41  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
14:05:41  INFO        place_all_stops: checking 1 positions...
14:05:41  INFO        STOP already live CMS @ $74.4
14:05:41  INFO        [positions] 1/1 (1 valid)
14:05:41  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.97|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.0%  $-0.01                                            HOLD|
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
  open_lots=10 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=7
  zombies_flagged=10
  FLAG b232|S218|91f7c383 zombie age_min=846 notional=$46.00 occ=UBER260731C00069000 action=submitted:e7a43092-25b5-4dd6-88c7-ce0be86bbfd9
  FLAG b225|S217|a565916f zombie age_min=846 notional=$54.00 occ=IBM260731C00235000 action=submitted:5ee75bb9-368a-4f53-99fb-c8fbf477e2b6
  FLAG b224|S217|9a98fe85 zombie age_min=846 notional=$54.00 occ=IBM260731C00235000 action=submitted:c32733a3-6f7b-412f-ad19-a3c45e9bd5cb
  FLAG b217|S216|6dad20ef zombie age_min=846 notional=$72.00 occ=GOOGL260729C00340000 action=submitted:b8204c80-91a0-4346-bd72-72b5f6c7e809
  FLAG b216|S216|23cf3a61 zombie age_min=846 notional=$72.00 occ=GOOGL260729C00340000 action=submitted:7005821d-f6ca-4a84-aba7-fe8a6775062d
  FLAG b169|S210|572036c5 zombie age_min=846 notional=$61.00 occ=EQT260731C00053000 action=submitted:ad7c9047-6647-4670-92e0-b31446b55083
  FLAG b168|S210|7047a66f zombie age_min=846 notional=$61.00 occ=EQT260731C00053000 action=submitted:67624cbe-e15f-4d2f-b924-59e4a7f00133
  FLAG b113|S203|f94b6b17 zombie age_min=846 notional=$73.00 occ=CCL260731P00027000 action=submitted:363f652b-d9c4-4a1f-bc67-d9514b86c9ab
  FLAG b112|S203|c1fc75dc zombie age_min=846 notional=$73.00 occ=CCL260731P00027000 action=submitted:c157cfb5-0042-4553-b308-90515044ef2d
  FLAG b0|ORPHAN|4d1c58bf zombie age_min=846 notional=$46.00 occ=UBER260731C00069000 action=submitted:a0344d3b-22f0-4186-b6e1-79f0523753d5
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T10:05:43.996506-04:00 ===

[Run context]
Paper auth OK — equity $130423.51, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 311 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $131078 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 142 no tradeable call, 194 already attempted today, 884 pending order
Placed 24 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $130,423.51                             |
|  Signals this run              311                                     |
|  Orders submitted (session)    48                                      |
|  Orders filled today (ledger)  18                                      |
|  Entries placed this run       24                                      |
|  Open virtual lots             8                                       |
|  Broker option positions       2                                       |
|  Pending orders                30                                      |
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
|  PENDING ORDERS (30)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:APA(4), S168:APA(4), S167:APA(4)   |
+------------------------------------------------------------------------+
|  b16  S165 APA      limit=0.21                                         |
|  b17  S165 APA      limit=0.21                                         |
|  b40  S168 APA      limit=0.33                                         |
|  b41  S168 APA      limit=0.33                                         |
|  b32  S167 APA      limit=0.21                                         |
|  ... 25 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  APA260731C00036000            6    -18.1%   $    -78.00               |
|  EQT260731C00053000            2     -8.6%   $    -10.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=194.2s reconcile=0.2s cancel=0.03s manage=0.01s scan=180.89s entries=12.62s
STATUS: options_morning_bot run complete (PAPER) elapsed=194.2s. run=#5119 https://github.com/28twagg-ops/TradingBot/actions/runs/30273339135
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T10:09:02.935373_

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
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 181 | 4 |
| S164 | 211 | 4 |
| S165 | 1647 | 18 |
| S166 | 81 | 2 |
| S167 | 201 | 5 |
| S168 | 134 | 4 |
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
| 2026-07-27 |    6 |    0 |    4 |    6 |    4 |    4 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    24 |

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
| Total open lots             |     8 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=487.97 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T141040Z

- UTC timestamp: `20260727T141040Z`
- GitHub run: [#5120](https://github.com/28twagg-ops/TradingBot/actions/runs/30273749840)
- Run id: `30273749840`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`205s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T10:10:45.374263-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":196.6,"phases_s":{"reconcile":0.57,"cancel":0.15,"manage":1.49,"scan":180.08,"entries":13.24,"reconcile2":0.51},"signals":294,"placed":0,"equity":130319.11,"open_positions":6,"pending_orders":10,"open_lots":26,"submitted_today":48,"filled_today":38,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5120","github_run_id":"30273749840","status":"ok"}
```

### Live bot full output

```text
14:10:41  INFO      Mode: exits
14:10:41  INFO        Daily log -> logs/daily/2026-07-27.md
14:10:41  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
14:10:41  INFO        place_all_stops: checking 1 positions...
14:10:42  INFO        STOP already live CMS @ $74.4
14:10:42  INFO        [positions] 1/1 (1 valid)
14:10:42  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.89|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.1%  $-0.09                                            HOLD|
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
  open_lots=8 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=7
  zombies_flagged=8
  FLAG b171|S210|6ec8bccd zombie age_min=851 notional=$58.00 occ=EQT260731C00053000 action=submitted:7ec81cd3-f044-4776-9ee8-63ec53514eab
  FLAG b170|S210|b1ad505b zombie age_min=851 notional=$58.00 occ=EQT260731C00053000 action=submitted:f925f76e-b41d-4117-954d-e257b5fc313f
  FLAG b147|S207|9e3443ba zombie age_min=851 notional=$72.00 occ=APA260731C00036000 action=error:{"bid":"0.55","buy_limit_price":"0.69","code":40310000,"existing_order_id":"551ead37-7ee5-4f51-9799-766b6be67364","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b146|S207|34bc38f2 zombie age_min=851 notional=$72.00 occ=APA260731C00036000 action=error:{"bid":"0.55","buy_limit_price":"0.69","code":40310000,"existing_order_id":"551ead37-7ee5-4f51-9799-766b6be67364","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b3|S163|00070998 zombie age_min=851 notional=$72.00 occ=APA260731C00036000 action=error:{"bid":"0.55","buy_limit_price":"0.69","code":40310000,"existing_order_id":"551ead37-7ee5-4f51-9799-766b6be67364","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b2|S163|21913e86 zombie age_min=851 notional=$72.00 occ=APA260731C00036000 action=error:{"bid":"0.55","buy_limit_price":"0.69","code":40310000,"existing_order_id":"551ead37-7ee5-4f51-9799-766b6be67364","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b27|S166|899bb57d zombie age_min=851 notional=$72.00 occ=APA260731C00036000 action=error:{"bid":"0.55","buy_limit_price":"0.69","code":40310000,"existing_order_id":"551ead37-7ee5-4f51-9799-766b6be67364","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b26|S166|9234dbb5 zombie age_min=851 notional=$72.00 occ=APA260731C00036000 action=error:{"bid":"0.55","buy_limit_price":"0.69","code":40310000,"existing_order_id":"551ead37-7ee5-4f51-9799-766b6be67364","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T10:10:45.374263-04:00 ===

[Run context]
Paper auth OK — equity $130319.11, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 294 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $129881 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 52 no tradeable call, 48 already attempted today, 266 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $130,319.11                             |
|  Signals this run              294                                     |
|  Orders submitted (session)    48                                      |
|  Orders filled today (ledger)  38                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             26                                      |
|  Broker option positions       6                                       |
|  Pending orders                10                                      |
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
|  PENDING ORDERS (10)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:APA(2), S167:APA(2), S212:CMG(2)   |
+------------------------------------------------------------------------+
|  b16  S165 APA      limit=0.21                                         |
|  b17  S165 APA      limit=0.21                                         |
|  b32  S167 APA      limit=0.21                                         |
|  b33  S167 APA      limit=0.21                                         |
|  b184 S212 CMG      limit=0.69                                         |
|  ... 5 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (6)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  APA260731C00036000           12    -27.7%   $   -234.00               |
|  APA260731C00037000            6    -25.0%   $    -48.00               |
|  CVX260731C00205000            2    -31.1%   $    -28.00               |
|  GOOGL260729C00342500          2    -12.1%   $    -16.00               |
|  ADBE260731C00255000           2     -8.1%   $    -12.00               |
|  UBER260731C00069000           2     -2.2%   $     -2.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=196.6s reconcile=0.57s cancel=0.15s manage=1.49s scan=180.08s entries=13.24s
STATUS: options_morning_bot run complete (PAPER) elapsed=196.6s. run=#5120 https://github.com/28twagg-ops/TradingBot/actions/runs/30273749840
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T10:14:06.680822_

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
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 183 | 4 |
| S164 | 211 | 4 |
| S165 | 1649 | 18 |
| S166 | 83 | 2 |
| S167 | 203 | 5 |
| S168 | 138 | 4 |
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
| 2026-07-27 |    8 |    0 |    6 |    8 |    6 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
| Total open lots             |    26 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=487.89 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T141628Z

- UTC timestamp: `20260727T141628Z`
- GitHub run: [#5121](https://github.com/28twagg-ops/TradingBot/actions/runs/30274154523)
- Run id: `30274154523`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`186s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T10:16:33.611920-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":177.5,"phases_s":{"reconcile":0.09,"cancel":0.02,"manage":0.02,"scan":172.42,"entries":4.65,"reconcile2":0.09},"signals":297,"placed":0,"equity":130458.39,"open_positions":1,"pending_orders":8,"open_lots":2,"submitted_today":48,"filled_today":40,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5121","github_run_id":"30274154523","status":"ok"}
```

### Live bot full output

```text
14:16:29  INFO      Mode: exits
14:16:30  INFO        Daily log -> logs/daily/2026-07-27.md
14:16:30  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
14:16:30  INFO        place_all_stops: checking 1 positions...
14:16:30  INFO        STOP already live CMS @ $74.4
14:16:30  INFO        [positions] 1/1 (1 valid)
14:16:30  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.87|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.1%  $-0.11                                            HOLD|
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
  open_lots=26 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=8
  zombies_flagged=26
  FLAG b147|S207|9e3443ba zombie age_min=857 notional=$72.00 occ=APA260731C00036000 action=submitted:db7a5d0d-82b9-460f-9988-f861ca60b20e
  FLAG b146|S207|34bc38f2 zombie age_min=857 notional=$72.00 occ=APA260731C00036000 action=submitted:4941a7ab-33cd-4513-bdbc-91b20541c445
  FLAG b3|S163|00070998 zombie age_min=857 notional=$72.00 occ=APA260731C00036000 action=submitted:5f5adb47-bed3-449d-8277-438ed55a8ce6
  FLAG b2|S163|21913e86 zombie age_min=857 notional=$72.00 occ=APA260731C00036000 action=submitted:6453f92d-54fb-448b-8c37-f6ded4b8ad93
  FLAG b27|S166|899bb57d zombie age_min=857 notional=$72.00 occ=APA260731C00036000 action=submitted:92f7dcd4-e299-4065-9e41-ab168bd6305b
  FLAG b26|S166|9234dbb5 zombie age_min=857 notional=$72.00 occ=APA260731C00036000 action=submitted:eaef8ccb-5dcf-4bda-b6e9-303bd4e78558
  FLAG b187|S212|6c29d694 zombie age_min=857 notional=$74.00 occ=ADBE260731C00255000 action=submitted:192e67af-8c2a-4723-b91c-c9077d6c75f6
  FLAG b186|S212|84e9639c zombie age_min=857 notional=$74.00 occ=ADBE260731C00255000 action=submitted:b7894ee4-768f-4bc3-a888-bd857172988a
  FLAG b145|S207|3627b182 zombie age_min=857 notional=$45.00 occ=CVX260731C00205000 action=submitted:bd9c8d7e-2f15-4a11-8003-ccb62b07876b
  FLAG b144|S207|c55ab2cc zombie age_min=857 notional=$45.00 occ=CVX260731C00205000 action=submitted:e502cfc6-23fa-4b2d-9407-bd0782526fe8
  FLAG b1|S163|b0b42ff8 zombie age_min=857 notional=$32.00 occ=APA260731C00037000 action=submitted:b3bcadd1-f70f-43cd-8605-fc1853b1ec73
  FLAG b0|S163|6de41cda zombie age_min=857 notional=$32.00 occ=APA260731C00037000 action=submitted:96ef18d6-766a-47bd-a29a-c28d70a01a3e
  FLAG b25|S166|75a3fed6 zombie age_min=857 notional=$32.00 occ=APA260731C00037000 action=submitted:24331a0a-20f2-4fc5-94b0-4abc1e811d02
  FLAG b24|S166|ca4af1ac zombie age_min=857 notional=$32.00 occ=APA260731C00037000 action=submitted:c4c37816-71cd-4dc7-acb1-a6a0a54868da
  FLAG b41|S168|71a198a4 zombie age_min=857 notional=$32.00 occ=APA260731C00037000 action=submitted:677f209d-06eb-418b-997f-94663d2c0644
  FLAG b40|S168|8f246766 zombie age_min=857 notional=$32.00 occ=APA260731C00037000 action=submitted:61bcdd84-3d76-402b-9ed4-0bbef5b82174
  FLAG b235|S218|38b802da zombie age_min=857 notional=$45.00 occ=UBER260731C00069000 action=submitted:dc1e9a01-0298-4fa5-89d1-7d0ba5fda5b4
  FLAG b234|S218|cbe7a51d zombie age_min=857 notional=$45.00 occ=UBER260731C00069000 action=submitted:41c2c926-8e93-4eb7-9028-99a9937eb4d3
  FLAG b219|S216|17bc9075 zombie age_min=857 notional=$66.00 occ=GOOGL260729C00342500 action=submitted:3e52b4a3-53e9-45ce-81d0-2543c62274c5
  FLAG b218|S216|d56cfd97 zombie age_min=857 notional=$66.00 occ=GOOGL260729C00342500 action=submitted:a12fa81d-e7c1-4d62-b06d-7eeeeadd3a35
  FLAG b35|S167|b974cb22 zombie age_min=857 notional=$69.00 occ=APA260731C00036000 action=submitted:da5ffb14-0b7b-4eac-81f6-7d49581dc785
  FLAG b34|S167|3674b8c5 zombie age_min=857 notional=$69.00 occ=APA260731C00036000 action=submitted:424f0dad-50ab-4467-9dba-d4dcb2d99c95
  FLAG b43|S168|df69b113 zombie age_min=857 notional=$69.00 occ=APA260731C00036000 action=submitted:509a6fd4-dd87-4f37-b42c-75e4702f79e3
  FLAG b42|S168|70feddcf zombie age_min=857 notional=$69.00 occ=APA260731C00036000 action=submitted:67d85753-92d4-4481-8c87-aac3ce758ccb
  FLAG b19|S165|eec21382 zombie age_min=857 notional=$69.00 occ=APA260731C00036000 action=submitted:4269d956-4d9a-4c54-8639-2ca38f92d0d6
  FLAG b18|S165|2af00a35 zombie age_min=857 notional=$69.00 occ=APA260731C00036000 action=submitted:b4e00b5f-6109-4d74-b64b-f0350358ba55
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T10:16:33.611920-04:00 ===

[Run context]
Paper auth OK — equity $130458.39, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 297 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $130176 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 52 no tradeable call, 510 already attempted today, 32 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $130,458.39                             |
|  Signals this run              297                                     |
|  Orders submitted (session)    48                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             2                                       |
|  Broker option positions       1                                       |
|  Pending orders                8                                       |
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
|  PENDING ORDERS (8)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:APA(2), S167:APA(2), S212:CMG(2)   |
+------------------------------------------------------------------------+
|  b16  S165 APA      limit=0.21                                         |
|  b17  S165 APA      limit=0.21                                         |
|  b32  S167 APA      limit=0.21                                         |
|  b33  S167 APA      limit=0.21                                         |
|  b184 S212 CMG      limit=0.69                                         |
|  ... 3 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  IBM260731C00235000            2    -11.5%   $    -12.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=177.5s reconcile=0.09s cancel=0.02s manage=0.02s scan=172.42s entries=4.65s
STATUS: options_morning_bot run complete (PAPER) elapsed=177.5s. run=#5121 https://github.com/28twagg-ops/TradingBot/actions/runs/30274154523
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T10:19:35.790989_

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
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 183 | 4 |
| S164 | 211 | 4 |
| S165 | 1649 | 18 |
| S166 | 83 | 2 |
| S167 | 203 | 5 |
| S168 | 138 | 4 |
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
| 2026-07-27 |    8 |    0 |    6 |    8 |    6 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
| Total open lots             |     2 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=487.87 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T142045Z

- UTC timestamp: `20260727T142045Z`
- GitHub run: [#5122](https://github.com/28twagg-ops/TradingBot/actions/runs/30274556317)
- Run id: `30274556317`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`199s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T10:20:50.208204-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":192.5,"phases_s":{"reconcile":0.35,"cancel":0.13,"manage":0.13,"scan":179.42,"entries":11.64,"reconcile2":0.34},"signals":300,"placed":0,"equity":129934.31,"open_positions":0,"pending_orders":8,"open_lots":0,"submitted_today":48,"filled_today":40,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5122","github_run_id":"30274556317","status":"ok"}
```

### Live bot full output

```text
14:20:46  INFO      Mode: exits
14:20:47  INFO        Daily log -> logs/daily/2026-07-27.md
14:20:47  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
14:20:47  INFO        place_all_stops: checking 1 positions...
14:20:47  INFO        STOP already live CMS @ $74.4
14:20:48  INFO        [positions] 1/1 (1 valid)
14:20:48  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.74|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.2%  $-0.24                                            HOLD|
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
  open_lots=2 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=2
  FLAG b227|S217|af325de3 zombie age_min=861 notional=$52.00 occ=IBM260731C00235000 action=submitted:f8a0e961-fc80-4182-99e1-b59f33212e85
  FLAG b226|S217|11b1eaab zombie age_min=861 notional=$52.00 occ=IBM260731C00235000 action=submitted:1992021c-b714-4ed2-a6c9-680f8251a35d
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T10:20:50.208204-04:00 ===

[Run context]
Paper auth OK — equity $129934.31, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 300 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $129488 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 52 no tradeable call, 534 already attempted today, 14 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,934.31                             |
|  Signals this run              300                                     |
|  Orders submitted (session)    48                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                8                                       |
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
|  PENDING ORDERS (8)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:APA(2), S167:APA(2), S212:CMG(2)   |
+------------------------------------------------------------------------+
|  b16  S165 APA      limit=0.21                                         |
|  b17  S165 APA      limit=0.21                                         |
|  b32  S167 APA      limit=0.21                                         |
|  b33  S167 APA      limit=0.21                                         |
|  b184 S212 CMG      limit=0.69                                         |
|  ... 3 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=192.5s reconcile=0.35s cancel=0.13s manage=0.13s scan=179.42s entries=11.64s
STATUS: options_morning_bot run complete (PAPER) elapsed=192.5s. run=#5122 https://github.com/28twagg-ops/TradingBot/actions/runs/30274556317
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T10:24:07.443645_

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
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 183 | 4 |
| S164 | 211 | 4 |
| S165 | 1649 | 18 |
| S166 | 83 | 2 |
| S167 | 203 | 5 |
| S168 | 138 | 4 |
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
| 2026-07-27 |    8 |    0 |    6 |    8 |    6 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
equity=487.74 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T142540Z

- UTC timestamp: `20260727T142540Z`
- GitHub run: [#5123](https://github.com/28twagg-ops/TradingBot/actions/runs/30274965975)
- Run id: `30274965975`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`189s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T10:25:43.503402-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":182.8,"phases_s":{"reconcile":0.07,"cancel":0.02,"manage":0.03,"scan":177.59,"entries":4.75,"reconcile2":0.08},"signals":311,"placed":0,"equity":129224.31,"open_positions":0,"pending_orders":8,"open_lots":0,"submitted_today":48,"filled_today":40,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5123","github_run_id":"30274965975","status":"ok"}
```

### Live bot full output

```text
14:25:41  INFO      Mode: exits
14:25:41  INFO        Daily log -> logs/daily/2026-07-27.md
14:25:41  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
14:25:41  INFO        place_all_stops: checking 1 positions...
14:25:41  INFO        STOP already live CMS @ $74.4
14:25:41  INFO        [positions] 1/1 (1 valid)
14:25:41  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $488.04|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.1%  $+0.06                                            HOLD|
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
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T10:25:43.503402-04:00 ===

[Run context]
Paper auth OK — equity $129224.31, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 311 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $128950 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 52 no tradeable call, 556 already attempted today, 14 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,224.31                             |
|  Signals this run              311                                     |
|  Orders submitted (session)    48                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                8                                       |
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
|  PENDING ORDERS (8)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:APA(2), S167:APA(2), S212:CMG(2)   |
+------------------------------------------------------------------------+
|  b16  S165 APA      limit=0.21                                         |
|  b17  S165 APA      limit=0.21                                         |
|  b32  S167 APA      limit=0.21                                         |
|  b33  S167 APA      limit=0.21                                         |
|  b184 S212 CMG      limit=0.69                                         |
|  ... 3 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=182.8s reconcile=0.07s cancel=0.02s manage=0.03s scan=177.59s entries=4.75s
STATUS: options_morning_bot run complete (PAPER) elapsed=182.8s. run=#5123 https://github.com/28twagg-ops/TradingBot/actions/runs/30274965975
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T10:28:51.186769_

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
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 183 | 4 |
| S164 | 211 | 4 |
| S165 | 1649 | 18 |
| S166 | 83 | 2 |
| S167 | 203 | 5 |
| S168 | 138 | 4 |
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
| 2026-07-27 |    8 |    0 |    6 |    8 |    6 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
equity=488.04 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T143106Z

- UTC timestamp: `20260727T143106Z`
- GitHub run: [#5124](https://github.com/28twagg-ops/TradingBot/actions/runs/30275367571)
- Run id: `30275367571`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`127s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T10:31:11.643306-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":122.1,"phases_s":{"reconcile":0.25,"cancel":0.09,"manage":0.09,"scan":111.0,"entries":10.05,"reconcile2":0.24},"signals":299,"placed":0,"equity":128318.31,"open_positions":0,"pending_orders":8,"open_lots":0,"submitted_today":48,"filled_today":40,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5124","github_run_id":"30275367571","status":"ok"}
```

### Live bot full output

```text
14:31:09  INFO      Mode: exits
14:31:09  INFO        Daily log -> logs/daily/2026-07-27.md
14:31:09  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
14:31:09  INFO        place_all_stops: checking 1 positions...
14:31:10  INFO        STOP already live CMS @ $74.4
14:31:10  INFO        [positions] 1/1 (1 valid)
14:31:10  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:31 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.99|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.0%  $+0.01                                            HOLD|
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
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T10:31:11.643306-04:00 ===

[Run context]
Paper auth OK — equity $128318.31, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $128570 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 52 no tradeable call, 528 already attempted today, 18 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,318.31                             |
|  Signals this run              299                                     |
|  Orders submitted (session)    48                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                8                                       |
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
|  PENDING ORDERS (8)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:APA(2), S167:APA(2), S212:CMG(2)   |
+------------------------------------------------------------------------+
|  b16  S165 APA      limit=0.21                                         |
|  b17  S165 APA      limit=0.21                                         |
|  b32  S167 APA      limit=0.21                                         |
|  b33  S167 APA      limit=0.21                                         |
|  b184 S212 CMG      limit=0.69                                         |
|  ... 3 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=122.1s reconcile=0.25s cancel=0.09s manage=0.09s scan=111.0s entries=10.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=122.1s. run=#5124 https://github.com/28twagg-ops/TradingBot/actions/runs/30275367571
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T10:33:16.795982_

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
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 183 | 4 |
| S164 | 211 | 4 |
| S165 | 1649 | 18 |
| S166 | 83 | 2 |
| S167 | 203 | 5 |
| S168 | 138 | 4 |
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
| 2026-07-27 |    8 |    0 |    6 |    8 |    6 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
equity=487.99 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T143424Z

- UTC timestamp: `20260727T143424Z`
- GitHub run: [#5125](https://github.com/28twagg-ops/TradingBot/actions/runs/30275677255)
- Run id: `30275677255`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T10:31:11.643306-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":122.1,"phases_s":{"reconcile":0.25,"cancel":0.09,"manage":0.09,"scan":111.0,"entries":10.05,"reconcile2":0.24},"signals":299,"placed":0,"equity":128318.31,"open_positions":0,"pending_orders":8,"open_lots":0,"submitted_today":48,"filled_today":40,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5124","github_run_id":"30275367571","status":"ok"}
```

### Live bot full output

```text
14:34:25  INFO      Mode: exits
14:34:26  INFO        Daily log -> logs/daily/2026-07-27.md
14:34:26  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
14:34:26  INFO        place_all_stops: checking 1 positions...
14:34:26  INFO        STOP already live CMS @ $74.4
14:34:27  INFO        [positions] 1/1 (1 valid)
14:34:27  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:34 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $488.01|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.0%  $+0.03                                            HOLD|
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
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T10:34:29.306843-04:00 ===

[Run context]
Paper auth OK — equity $128212.31, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
```

---

## Run 20260727T143618Z

- UTC timestamp: `20260727T143618Z`
- GitHub run: [#5126](https://github.com/28twagg-ops/TradingBot/actions/runs/30275772059)
- Run id: `30275772059`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`170s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T10:36:22.950756-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":163.6,"phases_s":{"reconcile":0.15,"cancel":0.05,"manage":0.12,"scan":154.78,"entries":8.08,"reconcile2":0.15},"signals":310,"placed":0,"equity":128231.39,"open_positions":0,"pending_orders":8,"open_lots":0,"submitted_today":48,"filled_today":40,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5126","github_run_id":"30275772059","status":"ok"}
```

### Live bot full output

```text
14:36:19  INFO      Mode: exits
14:36:20  INFO        Daily log -> logs/daily/2026-07-27.md
14:36:20  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
14:36:20  INFO        place_all_stops: checking 1 positions...
14:36:20  INFO        STOP already live CMS @ $74.4
14:36:20  INFO        [positions] 1/1 (1 valid)
14:36:21  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:36 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $488.08|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.1%  $+0.10                                            HOLD|
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
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T10:36:22.950756-04:00 ===

[Run context]
Paper auth OK — equity $128231.39, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 310 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $127699 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 52 no tradeable call, 548 already attempted today, 20 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,231.39                             |
|  Signals this run              310                                     |
|  Orders submitted (session)    48                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                8                                       |
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
|  PENDING ORDERS (8)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:APA(2), S167:APA(2), S212:CMG(2)   |
+------------------------------------------------------------------------+
|  b16  S165 APA      limit=0.21                                         |
|  b17  S165 APA      limit=0.21                                         |
|  b32  S167 APA      limit=0.21                                         |
|  b33  S167 APA      limit=0.21                                         |
|  b184 S212 CMG      limit=0.69                                         |
|  ... 3 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=163.6s reconcile=0.15s cancel=0.05s manage=0.12s scan=154.78s entries=8.08s
STATUS: options_morning_bot run complete (PAPER) elapsed=163.6s. run=#5126 https://github.com/28twagg-ops/TradingBot/actions/runs/30275772059
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T10:39:11.188982_

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
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 183 | 4 |
| S164 | 211 | 4 |
| S165 | 1649 | 18 |
| S166 | 83 | 2 |
| S167 | 203 | 5 |
| S168 | 138 | 4 |
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
| 2026-07-27 |    8 |    0 |    6 |    8 |    6 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
equity=488.08 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T144050Z

- UTC timestamp: `20260727T144050Z`
- GitHub run: [#5127](https://github.com/28twagg-ops/TradingBot/actions/runs/30276174868)
- Run id: `30276174868`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`166s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T10:40:55.443272-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":159.0,"phases_s":{"reconcile":0.36,"cancel":0.13,"manage":0.13,"scan":146.09,"entries":11.4,"reconcile2":0.39},"signals":322,"placed":0,"equity":127280.35,"open_positions":0,"pending_orders":8,"open_lots":0,"submitted_today":48,"filled_today":40,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5127","github_run_id":"30276174868","status":"ok"}
```

### Live bot full output

```text
14:40:52  INFO      Mode: exits
14:40:52  INFO        Daily log -> logs/daily/2026-07-27.md
14:40:52  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
14:40:52  INFO        place_all_stops: checking 1 positions...
14:40:52  INFO        STOP already live CMS @ $74.4
14:40:53  INFO        [positions] 1/1 (1 valid)
14:40:53  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $488.41|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.4%  $+0.43                                            HOLD|
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
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T10:40:55.443272-04:00 ===

[Run context]
Paper auth OK — equity $127276.35, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 322 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $127220 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 52 no tradeable call, 572 already attempted today, 20 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $127,280.35                             |
|  Signals this run              322                                     |
|  Orders submitted (session)    48                                      |
|  Orders filled today (ledger)  40                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                8                                       |
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
|  PENDING ORDERS (8)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S165:APA(2), S167:APA(2), S212:CMG(2)   |
+------------------------------------------------------------------------+
|  b16  S165 APA      limit=0.21                                         |
|  b17  S165 APA      limit=0.21                                         |
|  b32  S167 APA      limit=0.21                                         |
|  b33  S167 APA      limit=0.21                                         |
|  b184 S212 CMG      limit=0.69                                         |
|  ... 3 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=159.0s reconcile=0.36s cancel=0.13s manage=0.13s scan=146.09s entries=11.4s
STATUS: options_morning_bot run complete (PAPER) elapsed=159.0s. run=#5127 https://github.com/28twagg-ops/TradingBot/actions/runs/30276174868
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T10:43:39.001746_

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
| w3     |    3 |    3 |    9 |    1 |    3 |    2 |    0 |    0 |    0 |    0 |    0 |    7 |    4 |    32 |
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 183 | 4 |
| S164 | 211 | 4 |
| S165 | 1649 | 18 |
| S166 | 83 | 2 |
| S167 | 203 | 5 |
| S168 | 138 | 4 |
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
| 2026-07-27 |    8 |    0 |    6 |    8 |    6 |    8 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    36 |

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
equity=488.41 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T144542Z

- UTC timestamp: `20260727T144542Z`
- GitHub run: [#5128](https://github.com/28twagg-ops/TradingBot/actions/runs/30276584321)
- Run id: `30276584321`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`204s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T10:45:47.351618-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (28 new)","elapsed_s":196.5,"phases_s":{"reconcile":0.45,"cancel":0.15,"manage":0.14,"scan":163.51,"entries":31.08,"reconcile2":0.55},"signals":323,"placed":28,"equity":128058.31,"open_positions":6,"pending_orders":20,"open_lots":16,"submitted_today":76,"filled_today":56,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5128","github_run_id":"30276584321","status":"ok"}
```

### Live bot full output

```text
14:45:43  INFO      Mode: exits
14:45:44  INFO        Daily log -> logs/daily/2026-07-27.md
14:45:44  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
14:45:44  INFO        place_all_stops: checking 1 positions...
14:45:44  INFO        STOP already live CMS @ $74.4
14:45:45  INFO        [positions] 1/1 (1 valid)
14:45:45  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:45 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $488.34|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L +0.4%  $+0.36                                            HOLD|
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
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T10:45:47.351618-04:00 ===

[Run context]
Paper auth OK — equity $128058.31, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 323 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $128596 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 110 no tradeable call, 574 already attempted today, 580 pending order
Placed 28 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,058.31                             |
|  Signals this run              323                                     |
|  Orders submitted (session)    76                                      |
|  Orders filled today (ledger)  56                                      |
|  Entries placed this run       28                                      |
|  Open virtual lots             16                                      |
|  Broker option positions       6                                       |
|  Pending orders                20                                      |
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
|  PENDING ORDERS (20)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:APA(4), S167:APA(4), S211:FIS(4)   |
+------------------------------------------------------------------------+
|  b16  S165 APA      limit=0.21                                         |
|  b17  S165 APA      limit=0.21                                         |
|  b32  S167 APA      limit=0.21                                         |
|  b33  S167 APA      limit=0.21                                         |
|  b184 S212 CMG      limit=0.69                                         |
|  ... 15 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (6)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  APA260731C00036000            6    -14.1%   $    -54.00               |
|  CCL260731P00026500            2    -12.9%   $    -16.00               |
|  ADBE260731C00260000           2     -9.1%   $    -10.00               |
|  OXY260731C00057000            2     -8.3%   $    -10.00               |
|  UBER260731C00069000           2     -9.1%   $     -8.00               |
|  EQT260731C00054000            2    -11.1%   $     -6.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=196.5s reconcile=0.45s cancel=0.15s manage=0.14s scan=163.51s entries=31.08s
STATUS: options_morning_bot run complete (PAPER) elapsed=196.5s. run=#5128 https://github.com/28twagg-ops/TradingBot/actions/runs/30276584321
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T10:49:08.507314_

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
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 187 | 4 |
| S164 | 211 | 4 |
| S165 | 1651 | 18 |
| S166 | 87 | 2 |
| S167 | 205 | 5 |
| S168 | 142 | 4 |
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
| 2026-07-27 |   12 |    0 |    8 |   12 |    8 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    52 |

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
| Total open lots             |    16 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=488.34 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T145039Z

- UTC timestamp: `20260727T145039Z`
- GitHub run: [#5129](https://github.com/28twagg-ops/TradingBot/actions/runs/30276993297)
- Run id: `30276993297`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`205s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T10:50:45.601753-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":196.5,"phases_s":{"reconcile":0.52,"cancel":0.15,"manage":0.96,"scan":184.01,"entries":9.9,"reconcile2":0.37},"signals":316,"placed":0,"equity":129394.67,"open_positions":3,"pending_orders":14,"open_lots":12,"submitted_today":76,"filled_today":62,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5129","github_run_id":"30276993297","status":"ok"}
```

### Live bot full output

```text
14:50:40  INFO      Mode: exits
14:50:41  INFO        Daily log -> logs/daily/2026-07-27.md
14:50:41  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
14:50:41  INFO        place_all_stops: checking 1 positions...
14:50:41  INFO        STOP already live CMS @ $74.4
14:50:41  INFO        [positions] 1/1 (1 valid)
14:50:42  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.96|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.0%  $-0.02                                            HOLD|
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
  open_lots=16 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=9
  zombies_flagged=16
  FLAG b229|S217|b9c21811 zombie age_min=891 notional=$44.00 occ=UBER260731C00069000 action=submitted:6580e9eb-182c-4076-81cd-9ef231522957
  FLAG b228|S217|6756d9c2 zombie age_min=891 notional=$44.00 occ=UBER260731C00069000 action=submitted:c0072238-6b1d-4b31-98a8-51aad6a270dd
  FLAG b189|S212|a454bb5b zombie age_min=891 notional=$55.00 occ=ADBE260731C00260000 action=submitted:a5c7a443-42c8-494f-bd2e-45197685b0e1
  FLAG b188|S212|973ae97a zombie age_min=891 notional=$55.00 occ=ADBE260731C00260000 action=submitted:13dc881e-0d85-4864-a136-d1aad897ffa7
  FLAG b173|S210|4f227b7b zombie age_min=891 notional=$27.00 occ=EQT260731C00054000 action=submitted:2d55612d-d2ca-4f82-a006-5b82291b6e92
  FLAG b172|S210|b7ab0322 zombie age_min=891 notional=$27.00 occ=EQT260731C00054000 action=submitted:3efa0c1f-23c8-45f4-a5ee-742352ccc581
  FLAG b149|S207|13258b2a zombie age_min=891 notional=$60.00 occ=OXY260731C00057000 action=submitted:a8d268c7-15a1-4eef-9fff-a8663fd2071d
  FLAG b148|S207|53356136 zombie age_min=891 notional=$60.00 occ=OXY260731C00057000 action=submitted:f2cec566-21a0-46c7-b6ee-37c80022e482
  FLAG b117|S203|d2dea346 zombie age_min=891 notional=$62.00 occ=CCL260731P00026500 action=submitted:d93c7ba0-74e2-4460-ae37-96d62d1ae5aa
  FLAG b116|S203|27682ee7 zombie age_min=891 notional=$62.00 occ=CCL260731P00026500 action=submitted:f8c5a583-40b8-40d8-bb1e-56cb9ad33737
  FLAG b5|S163|c1702e3e zombie age_min=891 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.54","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b4|S163|a6e411fc zombie age_min=891 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.54","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b29|S166|0af1b983 zombie age_min=891 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.54","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b28|S166|2fc7986f zombie age_min=891 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.54","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b45|S168|98d4f3f9 zombie age_min=891 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.54","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b44|S168|5bc996b4 zombie age_min=891 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.54","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T10:50:45.601753-04:00 ===

[Run context]
Paper auth OK — equity $129394.67, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 316 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $129582 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 40 no tradeable call, 288 already attempted today, 156 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,394.67                             |
|  Signals this run              316                                     |
|  Orders submitted (session)    76                                      |
|  Orders filled today (ledger)  62                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             12                                      |
|  Broker option positions       3                                       |
|  Pending orders                14                                      |
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
|  PENDING ORDERS (14)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:APA(4), S167:APA(4), S212:CMG(2)   |
+------------------------------------------------------------------------+
|  b16  S165 APA      limit=0.21                                         |
|  b17  S165 APA      limit=0.21                                         |
|  b32  S167 APA      limit=0.21                                         |
|  b33  S167 APA      limit=0.21                                         |
|  b184 S212 CMG      limit=0.69                                         |
|  ... 9 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (3)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  FIS260731C00044000            4    -30.0%   $    -60.00               |
|  APA260731C00036000            6     -7.8%   $    -30.00               |
|  CMCSA260731C00023000          2    -16.7%   $    -12.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=196.5s reconcile=0.52s cancel=0.15s manage=0.96s scan=184.01s entries=9.9s
STATUS: options_morning_bot run complete (PAPER) elapsed=196.5s. run=#5129 https://github.com/28twagg-ops/TradingBot/actions/runs/30276993297
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T10:54:06.784332_

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
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 187 | 4 |
| S164 | 211 | 4 |
| S165 | 1651 | 18 |
| S166 | 87 | 2 |
| S167 | 205 | 5 |
| S168 | 142 | 4 |
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
| 2026-07-27 |   12 |    0 |    8 |   12 |    8 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    52 |

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
| Total open lots             |    12 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=487.96 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T145540Z

- UTC timestamp: `20260727T145540Z`
- GitHub run: [#5130](https://github.com/28twagg-ops/TradingBot/actions/runs/30277409170)
- Run id: `30277409170`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`157s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T10:55:44.091987-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":150.5,"phases_s":{"reconcile":0.08,"cancel":0.02,"manage":0.12,"scan":145.98,"entries":3.94,"reconcile2":0.08},"signals":312,"placed":0,"equity":129895.55,"open_positions":1,"pending_orders":14,"open_lots":6,"submitted_today":76,"filled_today":62,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5130","github_run_id":"30277409170","status":"ok"}
```

### Live bot full output

```text
14:55:41  INFO      Mode: exits
14:55:42  INFO        Daily log -> logs/daily/2026-07-27.md
14:55:42  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
14:55:42  INFO        place_all_stops: checking 1 positions...
14:55:42  INFO        STOP already live CMS @ $74.4
14:55:42  INFO        [positions] 1/1 (1 valid)
14:55:42  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         14:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.73|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.3%  $-0.25                                            HOLD|
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
  open_lots=12 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=5
  zombies_flagged=12
  FLAG b5|S163|c1702e3e zombie age_min=896 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.59","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b4|S163|a6e411fc zombie age_min=896 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.59","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b29|S166|0af1b983 zombie age_min=896 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.59","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b28|S166|2fc7986f zombie age_min=896 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.59","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b45|S168|98d4f3f9 zombie age_min=896 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.59","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b44|S168|5bc996b4 zombie age_min=896 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.59","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b237|S218|7756341e zombie age_min=896 notional=$36.00 occ=CMCSA260731C00023000 action=submitted:18dd49d2-cd10-4d1b-bb88-3a727f596d6e
  FLAG b236|S218|825609a2 zombie age_min=896 notional=$36.00 occ=CMCSA260731C00023000 action=submitted:112b480f-7bd5-4b03-b08a-87de4c2e7c77
  FLAG b181|S211|5bdaf1a3 zombie age_min=896 notional=$50.00 occ=FIS260731C00044000 action=submitted:3c11033d-3d86-4fad-9c01-8d46d2a650d1
  FLAG b180|S211|f5620306 zombie age_min=896 notional=$50.00 occ=FIS260731C00044000 action=submitted:cec11c47-9387-4a5c-851d-91b1e3a4da79
  FLAG b179|S211|a401f6b2 zombie age_min=896 notional=$50.00 occ=FIS260731C00044000 action=submitted:3a1d0725-096d-4dcb-99c1-5bf4dccab732
  FLAG b178|S211|af80b5b2 zombie age_min=896 notional=$50.00 occ=FIS260731C00044000 action=submitted:5784c3db-171a-44f4-813d-fa801068e44b
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T10:55:44.091987-04:00 ===

[Run context]
Paper auth OK — equity $129895.55, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 312 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $130300 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 40 no tradeable call, 334 already attempted today, 154 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,895.55                             |
|  Signals this run              312                                     |
|  Orders submitted (session)    76                                      |
|  Orders filled today (ledger)  62                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             6                                       |
|  Broker option positions       1                                       |
|  Pending orders                14                                      |
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
|  PENDING ORDERS (14)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S165:APA(4), S167:APA(4), S212:CMG(2)   |
+------------------------------------------------------------------------+
|  b16  S165 APA      limit=0.21                                         |
|  b17  S165 APA      limit=0.21                                         |
|  b32  S167 APA      limit=0.21                                         |
|  b33  S167 APA      limit=0.21                                         |
|  b184 S212 CMG      limit=0.69                                         |
|  ... 9 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  APA260731C00036000            6    -12.5%   $    -48.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=150.5s reconcile=0.08s cancel=0.02s manage=0.12s scan=145.98s entries=3.94s
STATUS: options_morning_bot run complete (PAPER) elapsed=150.5s. run=#5130 https://github.com/28twagg-ops/TradingBot/actions/runs/30277409170
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T10:58:19.147648_

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
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 187 | 4 |
| S164 | 211 | 4 |
| S165 | 1651 | 18 |
| S166 | 87 | 2 |
| S167 | 205 | 5 |
| S168 | 142 | 4 |
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
| 2026-07-27 |   12 |    0 |    8 |   12 |    8 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    52 |

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
| Total open lots             |     6 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=487.73 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T150050Z

- UTC timestamp: `20260727T150050Z`
- GitHub run: [#5131](https://github.com/28twagg-ops/TradingBot/actions/runs/30277824310)
- Run id: `30277824310`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`219s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T11:00:55.410609-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":211.5,"phases_s":{"reconcile":0.4,"cancel":0.15,"manage":0.87,"scan":199.74,"entries":9.29,"reconcile2":0.43},"signals":326,"placed":0,"equity":130673.55,"open_positions":2,"pending_orders":10,"open_lots":10,"submitted_today":76,"filled_today":66,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5131","github_run_id":"30277824310","status":"ok"}
```

### Live bot full output

```text
15:00:51  INFO      Mode: exits
15:00:52  INFO        Daily log -> logs/daily/2026-07-27.md
15:00:52  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
15:00:52  INFO        place_all_stops: checking 1 positions...
15:00:52  INFO        STOP already live CMS @ $74.4
15:00:52  INFO        [positions] 1/1 (1 valid)
15:00:52  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.78|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.2%  $-0.19                                            HOLD|
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
  open_lots=6 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=6
  FLAG b5|S163|c1702e3e zombie age_min=901 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.56","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b4|S163|a6e411fc zombie age_min=901 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.56","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b29|S166|0af1b983 zombie age_min=901 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.56","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b28|S166|2fc7986f zombie age_min=901 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.56","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b45|S168|98d4f3f9 zombie age_min=901 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.56","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b44|S168|5bc996b4 zombie age_min=901 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.56","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T11:00:55.410609-04:00 ===

[Run context]
Paper auth OK — equity $130673.55, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 326 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $130267 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 40 no tradeable call, 350 already attempted today, 166 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $130,673.55                             |
|  Signals this run              326                                     |
|  Orders submitted (session)    76                                      |
|  Orders filled today (ledger)  66                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             10                                      |
|  Broker option positions       2                                       |
|  Pending orders                10                                      |
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
|  PENDING ORDERS (10)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S212:CMG(2), S203:CCL(2), S165:APA(2)   |
+------------------------------------------------------------------------+
|  b184 S212 CMG      limit=0.69                                         |
|  b185 S212 CMG      limit=0.69                                         |
|  b114 S203 CCL      limit=0.66                                         |
|  b115 S203 CCL      limit=0.66                                         |
|  b20  S165 APA      limit=0.61                                         |
|  ... 5 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  APA260731C00036000            6    -12.5%   $    -48.00               |
|  APA260731C00037500            4     -9.5%   $     -8.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=211.5s reconcile=0.4s cancel=0.15s manage=0.87s scan=199.74s entries=9.29s
STATUS: options_morning_bot run complete (PAPER) elapsed=211.5s. run=#5131 https://github.com/28twagg-ops/TradingBot/actions/runs/30277824310
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T11:04:31.725225_

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
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 187 | 4 |
| S164 | 211 | 4 |
| S165 | 1653 | 18 |
| S166 | 87 | 2 |
| S167 | 207 | 5 |
| S168 | 142 | 4 |
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
| 2026-07-27 |   12 |    0 |   10 |   12 |   10 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    56 |

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
| Total open lots             |    10 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=487.79 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T150708Z

- UTC timestamp: `20260727T150708Z`
- GitHub run: [#5132](https://github.com/28twagg-ops/TradingBot/actions/runs/30278251196)
- Run id: `30278251196`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T11:00:55.410609-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":211.5,"phases_s":{"reconcile":0.4,"cancel":0.15,"manage":0.87,"scan":199.74,"entries":9.29,"reconcile2":0.43},"signals":326,"placed":0,"equity":130673.55,"open_positions":2,"pending_orders":10,"open_lots":10,"submitted_today":76,"filled_today":66,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5131","github_run_id":"30277824310","status":"ok"}
```

### Live bot full output

```text
15:07:09  INFO      Mode: exits
15:07:09  INFO        Daily log -> logs/daily/2026-07-27.md
15:07:09  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
15:07:09  INFO        place_all_stops: checking 1 positions...
15:07:10  INFO        STOP already live CMS @ $74.4
15:07:10  INFO        [positions] 1/1 (1 valid)
15:07:10  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:07 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.75|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.2%  $-0.23                                            HOLD|
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
  open_lots=10 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=4
  zombies_flagged=10
  FLAG b5|S163|c1702e3e zombie age_min=907 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.56","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b4|S163|a6e411fc zombie age_min=907 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.56","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b29|S166|0af1b983 zombie age_min=907 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.56","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b28|S166|2fc7986f zombie age_min=907 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.56","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b45|S168|98d4f3f9 zombie age_min=907 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.56","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b44|S168|5bc996b4 zombie age_min=907 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.56","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b33|S167|6bf61178 zombie age_min=907 notional=$21.00 occ=APA260731C00037500 action=submitted:72ee4893-da5f-4592-b0c1-d747ec6aba45
  FLAG b32|S167|d81c5e4c zombie age_min=907 notional=$21.00 occ=APA260731C00037500 action=submitted:da359794-f079-4b27-b68c-b5545b429ce2
  FLAG b17|S165|33779a06 zombie age_min=907 notional=$21.00 occ=APA260731C00037500 action=submitted:49fc5609-3831-4bd6-b1db-73edc441c61b
  FLAG b16|S165|3bcef6ba zombie age_min=907 notional=$21.00 occ=APA260731C00037500 action=submitted:b513ceb2-b229-4b24-bcb5-45f55e3c7b2b
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T11:07:13.142126-04:00 ===

[Run context]
Paper auth OK — equity $130114.55, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 323 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $130095 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
```

---

## Run 20260727T151159Z

- UTC timestamp: `20260727T151159Z`
- GitHub run: [#5133](https://github.com/28twagg-ops/TradingBot/actions/runs/30278665608)
- Run id: `30278665608`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`0s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T11:00:55.410609-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":211.5,"phases_s":{"reconcile":0.4,"cancel":0.15,"manage":0.87,"scan":199.74,"entries":9.29,"reconcile2":0.43},"signals":326,"placed":0,"equity":130673.55,"open_positions":2,"pending_orders":10,"open_lots":10,"submitted_today":76,"filled_today":66,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5131","github_run_id":"30277824310","status":"ok"}
```

### Live bot full output

```text
15:12:00  INFO      Mode: exits
15:12:01  INFO        Daily log -> logs/daily/2026-07-27.md
15:12:01  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
15:12:01  INFO        place_all_stops: checking 1 positions...
15:12:01  INFO        STOP already live CMS @ $74.4
15:12:02  INFO        [positions] 1/1 (1 valid)
15:12:02  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:12 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.69|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.3%  $-0.29                                            HOLD|
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
  open_lots=10 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=10
  FLAG b5|S163|c1702e3e zombie age_min=912 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.52","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b4|S163|a6e411fc zombie age_min=912 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.52","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b29|S166|0af1b983 zombie age_min=912 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.52","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b28|S166|2fc7986f zombie age_min=912 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.52","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b45|S168|98d4f3f9 zombie age_min=912 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.52","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b44|S168|5bc996b4 zombie age_min=912 notional=$64.00 occ=APA260731C00036000 action=error:{"bid":"0.52","buy_limit_price":"0.61","code":40310000,"existing_order_id":"439aaff2-e52d-4fa1-9f1a-c19313eb4b37","message":"potential wash trade detected. use complex orders","reject_reason":"buy order exists, quote bid should be greater than existing buy limit price"}
  FLAG b33|S167|6bf61178 zombie age_min=912 notional=$21.00 occ=APA260731C00037500 action=no_broker_position
  FLAG b32|S167|d81c5e4c zombie age_min=912 notional=$21.00 occ=APA260731C00037500 action=no_broker_position
  FLAG b17|S165|33779a06 zombie age_min=912 notional=$21.00 occ=APA260731C00037500 action=no_broker_position
  FLAG b16|S165|3bcef6ba zombie age_min=912 notional=$21.00 occ=APA260731C00037500 action=no_broker_position
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T11:12:04.651813-04:00 ===

[Run context]
Paper auth OK — equity $129927.39, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 317 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $129609 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 40 no tradeable call, 336 already attempted today, 162 pending order
Placed 0 new entry order(s).
```

---

## Run 20260727T151614Z

- UTC timestamp: `20260727T151614Z`
- GitHub run: [#5134](https://github.com/28twagg-ops/TradingBot/actions/runs/30279075149)
- Run id: `30279075149`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`117s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T11:16:20.290465-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":111.9,"phases_s":{"reconcile":0.21,"cancel":0.06,"manage":0.25,"scan":104.42,"entries":6.49,"reconcile2":0.21},"signals":313,"placed":0,"equity":129371.19,"open_positions":1,"pending_orders":6,"open_lots":4,"submitted_today":76,"filled_today":70,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5134","github_run_id":"30279075149","status":"ok"}
```

### Live bot full output

```text
15:16:17  INFO      Mode: exits
15:16:18  INFO        Daily log -> logs/daily/2026-07-27.md
15:16:18  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
15:16:18  INFO        place_all_stops: checking 1 positions...
15:16:18  INFO        STOP already live CMS @ $74.4
15:16:18  INFO        [positions] 1/1 (1 valid)
15:16:18  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:16 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.73|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.3%  $-0.25                                            HOLD|
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
  open_lots=6 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=6
  FLAG b5|S163|c1702e3e zombie age_min=916 notional=$64.00 occ=APA260731C00036000 action=submitted:eda60e94-080a-4b21-ae01-b2ed9ce66dc8
  FLAG b4|S163|a6e411fc zombie age_min=916 notional=$64.00 occ=APA260731C00036000 action=submitted:187547d0-3949-439f-988b-6ef6f86e18e8
  FLAG b29|S166|0af1b983 zombie age_min=916 notional=$64.00 occ=APA260731C00036000 action=submitted:4b544dbe-b8a2-4ee3-a08c-ff0a569a58c7
  FLAG b28|S166|2fc7986f zombie age_min=916 notional=$64.00 occ=APA260731C00036000 action=submitted:18397d3a-2c38-4991-b16f-fc23803309ef
  FLAG b45|S168|98d4f3f9 zombie age_min=916 notional=$64.00 occ=APA260731C00036000 action=submitted:d673d335-e3f2-428a-bd87-62aee4f14d49
  FLAG b44|S168|5bc996b4 zombie age_min=916 notional=$64.00 occ=APA260731C00036000 action=submitted:a734fab7-aaa5-4206-8935-e3ce873e60af
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T11:16:20.290465-04:00 ===

[Run context]
Paper auth OK — equity $129371.19, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 313 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $129105 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 40 no tradeable call, 426 already attempted today, 80 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,371.19                             |
|  Signals this run              313                                     |
|  Orders submitted (session)    76                                      |
|  Orders filled today (ledger)  70                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             4                                       |
|  Broker option positions       1                                       |
|  Pending orders                6                                       |
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
|  PENDING ORDERS (6)                                                    |
+------------------------------------------------------------------------+
|  Top groups                    S212:CMG(2), S203:CCL(2), S216:GOOG(2)  |
+------------------------------------------------------------------------+
|  b184 S212 CMG      limit=0.69                                         |
|  b185 S212 CMG      limit=0.69                                         |
|  b114 S203 CCL      limit=0.66                                         |
|  b115 S203 CCL      limit=0.66                                         |
|  b220 S216 GOOG     limit=0.67                                         |
|  ... 1 more pending order(s)                                           |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  APA260731C00036000            4    -13.4%   $    -32.80               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=111.9s reconcile=0.21s cancel=0.06s manage=0.25s scan=104.42s entries=6.49s
STATUS: options_morning_bot run complete (PAPER) elapsed=111.9s. run=#5134 https://github.com/28twagg-ops/TradingBot/actions/runs/30279075149
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T11:18:15.317641_

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
| w4     |    3 |    2 |    7 |    1 |    2 |    2 |    0 |    0 |    0 |    0 |    0 |    6 |    3 |    26 |

Windows (ET): w1 09:28–10:05 · w2 10:05–10:45 · w3 10:45–11:20 · w4 11:20–11:35. Parsed from controlled-layout profile names in ENTRY log lines.

## Raw vs unique totals

| Strategy | Raw log lines (includes multi-bucket duplicates) | Unique underlying symbols |
|----------|-------------------------------------------------:|--------------------------:|
| S163 | 187 | 4 |
| S164 | 211 | 4 |
| S165 | 1655 | 18 |
| S166 | 87 | 2 |
| S167 | 209 | 5 |
| S168 | 142 | 4 |
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
| 2026-07-27 |   12 |    0 |   12 |   12 |   12 |   12 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    60 |

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
| Total open lots             |     4 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=487.73 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T152037Z

- UTC timestamp: `20260727T152037Z`
- GitHub run: [#5135](https://github.com/28twagg-ops/TradingBot/actions/runs/30279482961)
- Run id: `30279482961`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`189s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T11:20:40.272596-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (24 new)","elapsed_s":181.9,"phases_s":{"reconcile":0.09,"cancel":0.04,"manage":0.27,"scan":171.69,"entries":9.46,"reconcile2":0.14},"signals":308,"placed":24,"equity":129597.07,"open_positions":4,"pending_orders":23,"open_lots":7,"submitted_today":100,"filled_today":77,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5135","github_run_id":"30279482961","status":"ok"}
```

### Live bot full output

```text
15:20:38  INFO      Mode: exits
15:20:38  INFO        Daily log -> logs/daily/2026-07-27.md
15:20:38  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
15:20:38  INFO        place_all_stops: checking 1 positions...
15:20:38  INFO        STOP already live CMS @ $74.4
15:20:38  INFO        [positions] 1/1 (1 valid)
15:20:38  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.71|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.3%  $-0.27                                            HOLD|
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
  open_lots=4 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=4
  zombies_flagged=4
  FLAG b37|S167|73f7d2eb zombie age_min=921 notional=$57.00 occ=APA260731C00036000 action=submitted:11249b0d-4635-47b1-8b11-3be4e7b717d9
  FLAG b36|S167|f4593917 zombie age_min=921 notional=$57.00 occ=APA260731C00036000 action=submitted:3fd97bc1-2b0a-4787-b779-ae98592492a7
  FLAG b21|S165|f26b2eca zombie age_min=921 notional=$57.00 occ=APA260731C00036000 action=submitted:97a9f009-b908-4419-a5ce-2b3abfb669fe
  FLAG b20|S165|e18c1d74 zombie age_min=921 notional=$57.00 occ=APA260731C00036000 action=submitted:d7e9d221-6240-4192-a333-9eaaa8d56b57
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T11:20:40.272596-04:00 ===

[Run context]
Paper auth OK — equity $129597.07, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174
  cancel failed APA260731C00036000: {"code":42210000,"message":"order is already in \"filled\" state"}
  cancel failed APA260731C00036000: {"code":42210000,"message":"order is already in \"filled\" state"}
  cancel failed APA260731C00036000: {"code":42210000,"message":"order is already in \"filled\" state"}

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 308 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $129185 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 106 no tradeable call, 498 already attempted today, 604 pending order
Placed 24 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,597.07                             |
|  Signals this run              308                                     |
|  Orders submitted (session)    100                                     |
|  Orders filled today (ledger)  77                                      |
|  Entries placed this run       24                                      |
|  Open virtual lots             7                                       |
|  Broker option positions       4                                       |
|  Pending orders                23                                      |
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
|  PENDING ORDERS (23)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S203:CCL(4), S216:GOOG(2), S165:APA(2)  |
+------------------------------------------------------------------------+
|  b114 S203 CCL      limit=0.66                                         |
|  b115 S203 CCL      limit=0.66                                         |
|  b220 S216 GOOG     limit=0.67                                         |
|  b221 S216 GOOG     limit=0.67                                         |
|  b22  S165 APA      limit=0.60                                         |
|  ... 18 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (4)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  IBM260731C00232500            2    -13.0%   $    -18.00               |
|  CVX260731C00202500            2    -11.5%   $    -14.00               |
|  CMG260731C00035000            2     -4.4%   $     -6.00               |
|  CMCSA260731C00023500          1    -21.7%   $     -5.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=181.9s reconcile=0.09s cancel=0.04s manage=0.27s scan=171.69s entries=9.46s
STATUS: options_morning_bot run complete (PAPER) elapsed=181.9s. run=#5135 https://github.com/28twagg-ops/TradingBot/actions/runs/30279482961
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T11:23:46.851452_

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
| Total open lots             |     7 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=487.71 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T152541Z

- UTC timestamp: `20260727T152541Z`
- GitHub run: [#5136](https://github.com/28twagg-ops/TradingBot/actions/runs/30279875743)
- Run id: `30279875743`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`170s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T11:25:45.697273-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (2 new)","elapsed_s":162.7,"phases_s":{"reconcile":0.38,"cancel":0.12,"manage":0.88,"scan":151.86,"entries":8.58,"reconcile2":0.32},"signals":303,"placed":2,"equity":129204.77,"open_positions":2,"pending_orders":22,"open_lots":3,"submitted_today":102,"filled_today":80,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5136","github_run_id":"30279875743","status":"ok"}
```

### Live bot full output

```text
15:25:42  INFO      Mode: exits
15:25:42  INFO        Daily log -> logs/daily/2026-07-27.md
15:25:42  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
15:25:42  INFO        place_all_stops: checking 1 positions...
15:25:43  INFO        STOP already live CMS @ $74.4
15:25:43  INFO        [positions] 1/1 (1 valid)
15:25:43  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.69|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.3%  $-0.29                                            HOLD|
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
  open_lots=7 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=7
  zombies_flagged=7
  FLAG b185|S212|d40609f7 zombie age_min=926 notional=$68.00 occ=CMG260731C00035000 action=submitted:6994a156-d96d-46d4-a709-7bab7989fe6c
  FLAG b184|S212|90bc72ba zombie age_min=926 notional=$68.00 occ=CMG260731C00035000 action=submitted:838e7ac8-c86e-4344-9b63-ef89affe3f5d
  FLAG b238|S218|d4e4dfb4 zombie age_min=926 notional=$23.00 occ=CMCSA260731C00023500 action=submitted:1451c451-f683-4f85-84cc-851df1f50cd1
  FLAG b231|S217|fa73e596 zombie age_min=926 notional=$69.00 occ=IBM260731C00232500 action=submitted:9603f9f6-06e7-49f7-b204-d1074a8539dc
  FLAG b230|S217|c53e59fe zombie age_min=926 notional=$69.00 occ=IBM260731C00232500 action=submitted:f1eee7e5-5217-4f64-aff4-3cc15559947e
  FLAG b151|S207|8e3e3a62 zombie age_min=926 notional=$61.00 occ=CVX260731C00202500 action=submitted:e6d22747-c5fb-4ec5-8482-960c4a5e10d5
  FLAG b150|S207|118cf2c7 zombie age_min=926 notional=$61.00 occ=CVX260731C00202500 action=submitted:e20faf8b-acc9-4e1d-9241-cc959e5e9b1d
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T11:25:45.697273-04:00 ===

[Run context]
Paper auth OK — equity $129205.85, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 303 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $128953 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 42 no tradeable call, 41 already attempted today, 324 pending order
Placed 2 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $129,204.77                             |
|  Signals this run              303                                     |
|  Orders submitted (session)    102                                     |
|  Orders filled today (ledger)  80                                      |
|  Entries placed this run       2                                       |
|  Open virtual lots             3                                       |
|  Broker option positions       2                                       |
|  Pending orders                22                                      |
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
|  PENDING ORDERS (22)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S203:CCL(4), S216:GOOG(2), S165:APA(2)  |
+------------------------------------------------------------------------+
|  b114 S203 CCL      limit=0.66                                         |
|  b115 S203 CCL      limit=0.66                                         |
|  b220 S216 GOOG     limit=0.67                                         |
|  b221 S216 GOOG     limit=0.67                                         |
|  b22  S165 APA      limit=0.60                                         |
|  ... 17 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (2)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  CMCSA260731C00023500          1    -21.7%   $     -5.00               |
|  ADBE260731C00260000           2     -3.3%   $     -4.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=162.7s reconcile=0.38s cancel=0.12s manage=0.88s scan=151.86s entries=8.58s
STATUS: options_morning_bot run complete (PAPER) elapsed=162.7s. run=#5136 https://github.com/28twagg-ops/TradingBot/actions/runs/30279875743
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T11:28:33.026671_

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
| Total open lots             |     3 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=487.69 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T153043Z

- UTC timestamp: `20260727T153043Z`
- GitHub run: [#5137](https://github.com/28twagg-ops/TradingBot/actions/runs/30280279025)
- Run id: `30280279025`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`217s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T11:30:48.445491-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":210.0,"phases_s":{"reconcile":0.44,"cancel":0.15,"manage":2.42,"scan":196.53,"entries":9.45,"reconcile2":0.4},"signals":300,"placed":0,"equity":128950.67,"open_positions":1,"pending_orders":20,"open_lots":2,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5137","github_run_id":"30280279025","status":"ok"}
```

### Live bot full output

```text
15:30:44  INFO      Mode: exits
15:30:45  INFO        Daily log -> logs/daily/2026-07-27.md
15:30:45  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
15:30:45  INFO        place_all_stops: checking 1 positions...
15:30:45  INFO        STOP already live CMS @ $74.4
15:30:46  INFO        [positions] 1/1 (1 valid)
15:30:46  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.61|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.4%  $-0.37                                            HOLD|
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
  open_lots=3 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=5
  zombies_flagged=3
  FLAG b239|S218|b6c4032b zombie age_min=931 notional=$23.00 occ=CMCSA260731C00023500 action=submitted:b4c86e64-a79e-42c0-812f-4d82b28cf829
  FLAG b191|S212|1f551868 zombie age_min=931 notional=$60.00 occ=ADBE260731C00260000 action=submitted:57d44162-af27-44f0-838c-620aa8152c0a
  FLAG b190|S212|be15ea75 zombie age_min=931 notional=$60.00 occ=ADBE260731C00260000 action=submitted:d1f3e0d4-b6dc-4b0a-9df5-f5ac2e80fae1
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T11:30:48.445491-04:00 ===

[Run context]
Paper auth OK — equity $128950.67, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 300 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $128119 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 40 no tradeable call, 234 already attempted today, 248 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,950.67                             |
|  Signals this run              300                                     |
|  Orders submitted (session)    102                                     |
|  Orders filled today (ledger)  82                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             2                                       |
|  Broker option positions       1                                       |
|  Pending orders                20                                      |
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
|  PENDING ORDERS (20)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S203:CCL(4), S216:GOOG(2), S165:APA(2)  |
+------------------------------------------------------------------------+
|  b114 S203 CCL      limit=0.66                                         |
|  b115 S203 CCL      limit=0.66                                         |
|  b220 S216 GOOG     limit=0.67                                         |
|  b221 S216 GOOG     limit=0.67                                         |
|  b22  S165 APA      limit=0.60                                         |
|  ... 15 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (1)                                                      |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  GOOGL260729C00342500          2    -23.2%   $    -26.00               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=210.0s reconcile=0.44s cancel=0.15s manage=2.42s scan=196.53s entries=9.45s
STATUS: options_morning_bot run complete (PAPER) elapsed=210.0s. run=#5137 https://github.com/28twagg-ops/TradingBot/actions/runs/30280279025
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T11:34:23.139690_

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
| Total open lots             |     2 | INFO |
| Total closed lots           |   318 | INFO |
| Pre-cutoff audit debt       |     0 | INFO |
| Transition audit debt       |   744 | INFO |

Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/ledger_health.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/dashboard.html
equity=487.61 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T153544Z

- UTC timestamp: `20260727T153544Z`
- GitHub run: [#5138](https://github.com/28twagg-ops/TradingBot/actions/runs/30280685663)
- Run id: `30280685663`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`181s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T11:35:48.907189-04:00","date":"2026-07-27","mode":"entry+manage","header":"entry+manage (0 new)","elapsed_s":173.9,"phases_s":{"reconcile":0.39,"cancel":0.15,"manage":0.14,"scan":162.3,"entries":9.77,"reconcile2":0.38},"signals":299,"placed":0,"equity":128075.03,"open_positions":0,"pending_orders":20,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":["S165:APA","S165:CF","S165:CVX","S165:COP","S165:DVN","S165:FANG","S165:DOW","S165:EOG"],"github_run":"5138","github_run_id":"30280685663","status":"ok"}
```

### Live bot full output

```text
15:35:45  INFO      Mode: exits
15:35:46  INFO        Daily log -> logs/daily/2026-07-27.md
15:35:46  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
15:35:46  INFO        place_all_stops: checking 1 positions...
15:35:46  INFO        STOP already live CMS @ $74.4
15:35:46  INFO        [positions] 1/1 (1 valid)
15:35:47  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.66|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.3%  $-0.32                                            HOLD|
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
  open_lots=2 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=3
  zombies_flagged=2
  FLAG b223|S216|2395d023 zombie age_min=936 notional=$56.00 occ=GOOGL260729C00342500 action=submitted:b6b2a768-1b3d-4e8a-8b59-efedc763398b
  FLAG b222|S216|a684daad zombie age_min=936 notional=$56.00 occ=GOOGL260729C00342500 action=submitted:579a4dd3-2d22-44a5-bffb-a6be66ca9356
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T11:35:48.907189-04:00 ===

[Run context]
Paper auth OK — equity $128075.03, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Scan + entries]
Scanning 903 symbols for [S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219] …
Fetched daily bars for 903/903 symbols
Found 299 signal(s); top: ['S165:APA', 'S165:CF', 'S165:CVX', 'S165:COP', 'S165:DVN', 'S165:FANG', 'S165:DOW', 'S165:EOG']
Paper lab: $127982 broker equity -> 248 bucket(s) ($500 virtual each, unlimited paper)
  Skipped: 42 no tradeable call, 310 already attempted today, 246 pending order
Placed 0 new entry order(s).

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          entry+manage                            |
|  Equity                        $128,075.03                             |
|  Signals this run              299                                     |
|  Orders submitted (session)    102                                     |
|  Orders filled today (ledger)  82                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                20                                      |
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
|  PENDING ORDERS (20)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S203:CCL(4), S216:GOOG(2), S165:APA(2)  |
+------------------------------------------------------------------------+
|  b114 S203 CCL      limit=0.66                                         |
|  b115 S203 CCL      limit=0.66                                         |
|  b220 S216 GOOG     limit=0.67                                         |
|  b221 S216 GOOG     limit=0.67                                         |
|  b22  S165 APA      limit=0.60                                         |
|  ... 15 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=173.9s reconcile=0.39s cancel=0.15s manage=0.14s scan=162.3s entries=9.77s
STATUS: options_morning_bot run complete (PAPER) elapsed=173.9s. run=#5138 https://github.com/28twagg-ops/TradingBot/actions/runs/30280685663
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T11:38:47.439465_

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
equity=487.66 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T154038Z

- UTC timestamp: `20260727T154038Z`
- GitHub run: [#5139](https://github.com/28twagg-ops/TradingBot/actions/runs/30281078941)
- Run id: `30281078941`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T11:40:41.093807-04:00","date":"2026-07-27","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":0.7,"phases_s":{"reconcile":0.16,"cancel":0.2,"manage":0.02},"signals":0,"placed":0,"equity":127949.03,"open_positions":0,"pending_orders":20,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":[],"github_run":"5139","github_run_id":"30281078941","status":"ok"}
```

### Live bot full output

```text
15:40:39  INFO      Mode: exits
15:40:39  INFO        Daily log -> logs/daily/2026-07-27.md
15:40:39  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
15:40:39  INFO        place_all_stops: checking 1 positions...
15:40:39  INFO        STOP already live CMS @ $74.4
15:40:39  INFO        [positions] 1/1 (1 valid)
15:40:39  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:40 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.77|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.2%  $-0.21                                            HOLD|
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
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T11:40:41.093807-04:00 ===

[Run context]
Paper auth OK — equity $127949.03, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174
Cancelled 20 unfilled LAB entry order(s).

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $127,949.03                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    102                                     |
|  Orders filled today (ledger)  82                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             0                                       |
|  Broker option positions       0                                       |
|  Pending orders                20                                      |
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
|  PENDING ORDERS (20)                                                   |
+------------------------------------------------------------------------+
|  Top groups                    S203:CCL(4), S216:GOOG(2), S165:APA(2)  |
+------------------------------------------------------------------------+
|  b114 S203 CCL      limit=0.66                                         |
|  b115 S203 CCL      limit=0.66                                         |
|  b220 S216 GOOG     limit=0.67                                         |
|  b221 S216 GOOG     limit=0.67                                         |
|  b22  S165 APA      limit=0.60                                         |
|  ... 15 more pending order(s)                                          |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (0)                                                      |
+------------------------------------------------------------------------+
|  No open option positions                                              |
+========================================================================+
Full detail: logs/options_trial/runs/2026-07-27.log
elapsed=0.7s reconcile=0.16s cancel=0.2s manage=0.02s
STATUS: options_morning_bot run complete (PAPER) elapsed=0.7s. run=#5139 https://github.com/28twagg-ops/TradingBot/actions/runs/30281078941
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T11:40:46.480700_

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
equity=487.77 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T154724Z

- UTC timestamp: `20260727T154724Z`
- GitHub run: [#5140](https://github.com/28twagg-ops/TradingBot/actions/runs/30281471603)
- Run id: `30281471603`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T11:47:29.344761-04:00","date":"2026-07-27","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.8,"phases_s":{"reconcile":0.39,"cancel":0.22,"manage":0.15},"signals":0,"placed":0,"equity":128427.67,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":[],"github_run":"5140","github_run_id":"30281471603","status":"ok"}
```

### Live bot full output

```text
15:47:25  INFO      Mode: exits
15:47:26  INFO        Daily log -> logs/daily/2026-07-27.md
15:47:26  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
15:47:26  INFO        place_all_stops: checking 1 positions...
15:47:27  INFO        STOP already live CMS @ $74.4
15:47:27  INFO        [positions] 1/1 (1 valid)
15:47:27  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:47 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.53|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.5%  $-0.45                                            HOLD|
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
  open_lots=0 pending_exits=0 paper_keys=yes dry_run=False
  alpaca open sell orders=0 positions=2
  zombies_flagged=0
options_reconcile: done
Layout: controlled:248:c000_s163_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:248:c000_s163_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      248
=== options_morning_bot (PAPER) 2026-07-27T11:47:29.344761-04:00 ===

[Run context]
Paper auth OK — equity $128427.67, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $128,427.67                             |
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
elapsed=1.8s reconcile=0.39s cancel=0.22s manage=0.15s
STATUS: options_morning_bot run complete (PAPER) elapsed=1.8s. run=#5140 https://github.com/28twagg-ops/TradingBot/actions/runs/30281471603
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T11:47:35.859782_

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
equity=487.53 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T155057Z

- UTC timestamp: `20260727T155057Z`
- GitHub run: [#5141](https://github.com/28twagg-ops/TradingBot/actions/runs/30281862115)
- Run id: `30281862115`
- Live bot: exit=`0`, duration=`4s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T11:51:02.522687-04:00","date":"2026-07-27","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":0.5,"phases_s":{"reconcile":0.09,"cancel":0.04,"manage":0.03},"signals":0,"placed":0,"equity":128432.63,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":[],"github_run":"5141","github_run_id":"30281862115","status":"ok"}
```

### Live bot full output

```text
15:50:58  INFO      Mode: exits
15:50:58  INFO        Daily log -> logs/daily/2026-07-27.md
15:50:58  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (9 ledger rows)
15:50:58  INFO        place_all_stops: checking 1 positions...
15:50:58  INFO        STOP skipped CMS: fractional (0.3097 shares) — software exit will handle it
15:50:58  INFO        [positions] 1/1 (1 valid)
15:50:58  INFO        SELL MARKET [urgent] CMS closed
15:51:00  INFO        TX logged: SELL CMS  P&L -0.53%
15:51:00  INFO        Daily log -> logs/daily/2026-07-27.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:50 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.45|
+========================================================================+

+========================================================================+
|                               EXIT CHECK                               |
+========================================================================+
|  Exit logic                   stop-0.5% / 3d max  (midline at EOD only)|
+------------------------------------------------------------------------+
|  CMS  P&L -0.5%  $-0.12                         EXIT: stop_loss (-0.5%)|
+========================================================================+

+========================================================================+
|                            EXIT RUN SUMMARY                            |
+========================================================================+
|  Mode                                                             exits|
|  Candidates                                                           1|
|  Deferred/Skipped                                      already logged 0|
|  Data skips                                             no price data 0|
|  Se~  1 attempted  |  1 filled  |  0 partial  |  0 pending  |  0 failed|
|  Holds                                                                0|
|  Logged exits                                                         1|
+========================================================================+

+========================================================================+
|                      STOP-LOSS BREACHES THIS RUN                       |
+========================================================================+
|  CMS                                         -0.53%  (threshold -0.50%)|
|  Count                                                                1|
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
=== options_morning_bot (PAPER) 2026-07-27T11:51:02.522687-04:00 ===

[Run context]
Paper auth OK — equity $128432.63, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $128,432.63                             |
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
elapsed=0.5s reconcile=0.09s cancel=0.04s manage=0.03s
STATUS: options_morning_bot run complete (PAPER) elapsed=0.5s. run=#5141 https://github.com/28twagg-ops/TradingBot/actions/runs/30281862115
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T11:51:07.867360_

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
equity=487.44 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T155535Z

- UTC timestamp: `20260727T155535Z`
- GitHub run: [#5142](https://github.com/28twagg-ops/TradingBot/actions/runs/30282257211)
- Run id: `30282257211`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T11:55:38.541602-04:00","date":"2026-07-27","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":0.4,"phases_s":{"reconcile":0.07,"cancel":0.03,"manage":0.02},"signals":0,"placed":0,"equity":128440.63,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":[],"github_run":"5142","github_run_id":"30282257211","status":"ok"}
```

### Live bot full output

```text
15:55:36  INFO      Mode: exits
15:55:36  INFO        Daily log -> logs/daily/2026-07-27.md
15:55:36  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (10 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         15:55 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.44|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
=== options_morning_bot (PAPER) 2026-07-27T11:55:38.541602-04:00 ===

[Run context]
Paper auth OK — equity $128440.63, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $128,440.63                             |
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
elapsed=0.4s reconcile=0.07s cancel=0.03s manage=0.02s
STATUS: options_morning_bot run complete (PAPER) elapsed=0.4s. run=#5142 https://github.com/28twagg-ops/TradingBot/actions/runs/30282257211
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T11:55:43.610316_

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
equity=487.44 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T160042Z

- UTC timestamp: `20260727T160042Z`
- GitHub run: [#5143](https://github.com/28twagg-ops/TradingBot/actions/runs/30282660826)
- Run id: `30282660826`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T12:00:46.762064-04:00","date":"2026-07-27","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":0.4,"phases_s":{"reconcile":0.1,"cancel":0.03,"manage":0.02},"signals":0,"placed":0,"equity":129400.63,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":[],"github_run":"5143","github_run_id":"30282660826","status":"ok"}
```

### Live bot full output

```text
16:00:44  INFO      Mode: exits
16:00:45  INFO        Daily log -> logs/daily/2026-07-27.md
16:00:45  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (10 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:00 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.44|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
=== options_morning_bot (PAPER) 2026-07-27T12:00:46.762064-04:00 ===

[Run context]
Paper auth OK — equity $129400.63, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $129,400.63                             |
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
elapsed=0.4s reconcile=0.1s cancel=0.03s manage=0.02s
STATUS: options_morning_bot run complete (PAPER) elapsed=0.4s. run=#5143 https://github.com/28twagg-ops/TradingBot/actions/runs/30282660826
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T12:00:51.790624_

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
equity=487.44 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T160540Z

- UTC timestamp: `20260727T160540Z`
- GitHub run: [#5144](https://github.com/28twagg-ops/TradingBot/actions/runs/30283067604)
- Run id: `30283067604`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`6s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T12:05:44.663628-04:00","date":"2026-07-27","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":0.7,"phases_s":{"reconcile":0.2,"cancel":0.09,"manage":0.06},"signals":0,"placed":0,"equity":130024.63,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":[],"github_run":"5144","github_run_id":"30283067604","status":"ok"}
```

### Live bot full output

```text
16:05:42  INFO      Mode: exits
16:05:43  INFO        Daily log -> logs/daily/2026-07-27.md
16:05:43  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (10 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:05 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.44|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
=== options_morning_bot (PAPER) 2026-07-27T12:05:44.663628-04:00 ===

[Run context]
Paper auth OK — equity $130024.63, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $130,024.63                             |
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
elapsed=0.7s reconcile=0.2s cancel=0.09s manage=0.06s
STATUS: options_morning_bot run complete (PAPER) elapsed=0.7s. run=#5144 https://github.com/28twagg-ops/TradingBot/actions/runs/30283067604
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T12:05:49.188797_

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
equity=487.44 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T161050Z

- UTC timestamp: `20260727T161050Z`
- GitHub run: [#5145](https://github.com/28twagg-ops/TradingBot/actions/runs/30283465253)
- Run id: `30283465253`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`9s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T12:10:54.503725-04:00","date":"2026-07-27","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.3,"phases_s":{"reconcile":0.39,"cancel":0.22,"manage":0.15},"signals":0,"placed":0,"equity":130099.03,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":[],"github_run":"5145","github_run_id":"30283465253","status":"ok"}
```

### Live bot full output

```text
16:10:51  INFO      Mode: exits
16:10:52  INFO        Daily log -> logs/daily/2026-07-27.md
16:10:52  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (10 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:10 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.44|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
=== options_morning_bot (PAPER) 2026-07-27T12:10:54.503725-04:00 ===

[Run context]
Paper auth OK — equity $130098.63, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $130,099.03                             |
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
elapsed=1.3s reconcile=0.39s cancel=0.22s manage=0.15s
STATUS: options_morning_bot run complete (PAPER) elapsed=1.3s. run=#5145 https://github.com/28twagg-ops/TradingBot/actions/runs/30283465253
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T12:11:00.639695_

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
equity=487.44 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T161543Z

- UTC timestamp: `20260727T161543Z`
- GitHub run: [#5146](https://github.com/28twagg-ops/TradingBot/actions/runs/30283853574)
- Run id: `30283853574`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T12:15:46.178571-04:00","date":"2026-07-27","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":0.8,"phases_s":{"reconcile":0.15,"cancel":0.04,"manage":0.03},"signals":0,"placed":0,"equity":129298.63,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":[],"github_run":"5146","github_run_id":"30283853574","status":"ok"}
```

### Live bot full output

```text
16:15:44  INFO      Mode: exits
16:15:44  INFO        Daily log -> logs/daily/2026-07-27.md
16:15:44  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (10 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:15 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.44|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
=== options_morning_bot (PAPER) 2026-07-27T12:15:46.178571-04:00 ===

[Run context]
Paper auth OK — equity $129298.63, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $129,298.63                             |
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
elapsed=0.8s reconcile=0.15s cancel=0.04s manage=0.03s
STATUS: options_morning_bot run complete (PAPER) elapsed=0.8s. run=#5146 https://github.com/28twagg-ops/TradingBot/actions/runs/30283853574
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T12:15:51.587367_

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
equity=487.44 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T162041Z

- UTC timestamp: `20260727T162041Z`
- GitHub run: [#5147](https://github.com/28twagg-ops/TradingBot/actions/runs/30284232078)
- Run id: `30284232078`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T12:20:44.914879-04:00","date":"2026-07-27","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.1,"phases_s":{"reconcile":0.33,"cancel":0.18,"manage":0.13},"signals":0,"placed":0,"equity":129038.71,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":[],"github_run":"5147","github_run_id":"30284232078","status":"ok"}
```

### Live bot full output

```text
16:20:42  INFO      Mode: exits
16:20:43  INFO        Daily log -> logs/daily/2026-07-27.md
16:20:43  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (10 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:20 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.44|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
=== options_morning_bot (PAPER) 2026-07-27T12:20:44.914879-04:00 ===

[Run context]
Paper auth OK — equity $129038.71, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $129,038.71                             |
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
elapsed=1.1s reconcile=0.33s cancel=0.18s manage=0.13s
STATUS: options_morning_bot run complete (PAPER) elapsed=1.1s. run=#5147 https://github.com/28twagg-ops/TradingBot/actions/runs/30284232078
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T12:20:49.626220_

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
equity=487.44 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T162544Z

- UTC timestamp: `20260727T162544Z`
- GitHub run: [#5148](https://github.com/28twagg-ops/TradingBot/actions/runs/30284610321)
- Run id: `30284610321`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`7s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T12:25:47.906672-04:00","date":"2026-07-27","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":0.8,"phases_s":{"reconcile":0.18,"cancel":0.07,"manage":0.05},"signals":0,"placed":0,"equity":129904.63,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":[],"github_run":"5148","github_run_id":"30284610321","status":"ok"}
```

### Live bot full output

```text
16:25:45  INFO      Mode: exits
16:25:46  INFO        Daily log -> logs/daily/2026-07-27.md
16:25:46  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (10 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:25 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.44|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
=== options_morning_bot (PAPER) 2026-07-27T12:25:47.906672-04:00 ===

[Run context]
Paper auth OK — equity $129904.63, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $129,904.63                             |
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
elapsed=0.8s reconcile=0.18s cancel=0.07s manage=0.05s
STATUS: options_morning_bot run complete (PAPER) elapsed=0.8s. run=#5148 https://github.com/28twagg-ops/TradingBot/actions/runs/30284610321
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T12:25:53.297955_

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
equity=487.44 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T163050Z

- UTC timestamp: `20260727T163050Z`
- GitHub run: [#5149](https://github.com/28twagg-ops/TradingBot/actions/runs/30284982600)
- Run id: `30284982600`
- Live bot: exit=`0`, duration=`3s`
- Options bot: exit=`0`, duration=`5s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T12:30:54.494894-04:00","date":"2026-07-27","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":0.7,"phases_s":{"reconcile":0.2,"cancel":0.1,"manage":0.06},"signals":0,"placed":0,"equity":130527.95,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":[],"github_run":"5149","github_run_id":"30284982600","status":"ok"}
```

### Live bot full output

```text
16:30:52  INFO      Mode: exits
16:30:52  INFO        Daily log -> logs/daily/2026-07-27.md
16:30:52  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (10 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:30 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.44|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
=== options_morning_bot (PAPER) 2026-07-27T12:30:54.494894-04:00 ===

[Run context]
Paper auth OK — equity $130527.95, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $130,527.95                             |
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
elapsed=0.7s reconcile=0.2s cancel=0.1s manage=0.06s
STATUS: options_morning_bot run complete (PAPER) elapsed=0.7s. run=#5149 https://github.com/28twagg-ops/TradingBot/actions/runs/30284982600
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T12:30:58.246645_

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
equity=487.44 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---

## Run 20260727T163544Z

- UTC timestamp: `20260727T163544Z`
- GitHub run: [#5150](https://github.com/28twagg-ops/TradingBot/actions/runs/30285363100)
- Run id: `30285363100`
- Live bot: exit=`0`, duration=`2s`
- Options bot: exit=`0`, duration=`8s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-07-27T12:35:48.429296-04:00","date":"2026-07-27","mode":"manage-only","header":"manage-only (past entry window)","elapsed_s":1.1,"phases_s":{"reconcile":0.3,"cancel":0.17,"manage":0.11},"signals":0,"placed":0,"equity":129646.63,"open_positions":0,"pending_orders":0,"open_lots":0,"submitted_today":102,"filled_today":82,"unattributed_contracts":0,"top_signals":[],"github_run":"5150","github_run_id":"30285363100","status":"ok"}
```

### Live bot full output

```text
16:35:45  INFO      Mode: exits
16:35:46  INFO        Daily log -> logs/daily/2026-07-27.md
16:35:46  INFO        Daily log reconciled -> logs/daily/2026-07-27.md (10 ledger rows)

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                             EXITS|
|  Time                                                         16:35 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $487.44|
+========================================================================+

+========================================================================+
|                             MORNING CHECK                              |
+========================================================================+
|                                                                        |
|  No open positions.                                                    |
|                                                                        |
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
=== options_morning_bot (PAPER) 2026-07-27T12:35:48.429296-04:00 ===

[Run context]
Paper auth OK — equity $129646.63, account PA36KS87UPRS

[Setup]
Active buckets: 248 | Strategies: S165, S164, S168, S167, S166, S163, S169, S170, S171, S172, S175, S200, S201, S202, S203, S204, S205, S206, S207, S208, S209, S210, S211, S212, S213, S214, S215, S216, S217, S218, S219
Dropped (no new entries; ex-reflected P&L): S173, S174

[Manage only]
Past entry window; manage/exit only.

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          manage-only                             |
|  Equity                        $129,646.63                             |
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
elapsed=1.1s reconcile=0.3s cancel=0.17s manage=0.11s
STATUS: options_morning_bot run complete (PAPER) elapsed=1.1s. run=#5150 https://github.com/28twagg-ops/TradingBot/actions/runs/30285363100
Evaluation complete: 30 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_buckets.csv
Summary: 0 buckets closed trades, $+0.00 realized
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-07-27_strategy_selection.csv
Summary: keep=0 watch=30 drop=3
Orphan rate: 2.7% (22/807)
# Options signal frequency

_Generated 2026-07-27T12:35:54.145543_

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
equity=487.44 router=CONFIRMED leaderboard_rows=33
Wrote /home/runner/work/TradingBot/TradingBot/logs/rubber_band_report.md
| 1 | MomReversal | 9 | 33% | +0.31% | -0.78% | -1.14% | 4.09 | 1.3d | $+1.33 | WATCH |
| 2 | unknown | 32 | 19% | -0.03% | -0.59% | -1.27% | 1.44 | 0.0d | $+0.29 | ACTIVE |
```

---
