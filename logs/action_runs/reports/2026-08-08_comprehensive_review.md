# Daily Comprehensive Action Review — 2026-08-08

_Auto-generated from GitHub Actions run output. This document appends every run for the day._

## Run 20260808T000142Z

- UTC timestamp: `20260808T000142Z`
- GitHub run: [#6521](https://github.com/28twagg-ops/TradingBot/actions/runs/31228892186)
- Run id: `31228892186`
- Live bot: exit=`0`, duration=`1s`
- Options bot: exit=`0`, duration=`10s`
- Options structured summary (latest JSON):
```json
{"ts_et":"2026-08-07T20:01:45.739188-04:00","date":"2026-08-07","mode":"after_hours","header":"after hours (exit summary)","elapsed_s":0.7,"phases_s":{"reconcile":0.1},"signals":0,"placed":0,"equity":141981.52,"open_positions":18,"pending_orders":0,"open_lots":103,"submitted_today":64,"filled_today":60,"unattributed_contracts":0,"top_signals":[],"github_run":"6521","github_run_id":"31228892186","status":"ok"}
```

### Live bot full output

```text
00:01:43  INFO      Mode: weekly
00:01:43  INFO        Weekly summary -> logs/weekly/2026-W32.md

+========================================================================+
|  RUBBER BAND BOT  v8                                                   |
+------------------------------------------------------------------------+
|  Mode                                                            WEEKLY|
|  Time                                                         00:01 UTC|
|  Regime                                                            BULL|
|  Universe                                                          both|
|  Equity                                                         $474.20|
+========================================================================+

+========================================================================+
|              RUBBER BAND BOT  |  Week 32 / 2026  |  LIVE               |
+========================================================================+
+------------------------------------------------------------------------+
|  Date                                                 2026-08-08  (Aug)|
|  Regime                                                            BULL|
|  Strat~  VolumeSpike  +  52wkLow (display only — schedule not enforced)|
|  Execution                      Summary mode only (no orders submitted)|
|  Buys today                                                           0|
|  Cash-based cap             9396 max trades with current available cash|
+------------------------------------------------------------------------+
|  Equity           $474.20       Cash             $117.67               |
|  Invested         $356.53       Available        $93.96                |
|  Open P&L         $+3.22        Realized P&L     $-5.16                |
+------------------------------------------------------------------------+
|  This week          0 buys  |  26 sells  |  Win rate 42%  |  P&L $+7.86|
|  All ti~  1090 trades  |  Avg hold 1.8d  |  Return -6.8%  |  P&L $-5.16|
+------------------------------------------------------------------------+
|  TICKER  STRATEGY       INVESTED   ENTRY     NOW       P&L%      P&L$  |
+------------------------------------------------------------------------+
|  AAPL    Pullback50     $94.97     $311.48   $313.15   +0.5%     $+0.51|
|  AES     Pullback50     $94.47     $14.72    $14.73    +0.0%     $+0.03|
|  BBY     Pullback50     $96.67     $80.12    $82.00    +2.3%     $+2.21|
|  ESS     Pullback50     $70.43     $286.19   $288.10   +0.7%     $+0.47|
+------------------------------------------------------------------------+
|  Next month                               Sep:  GapDown  +  VolumeSpike|
+========================================================================+

+========================================================================+
|                        YEAR-BY-YEAR PERFORMANCE                        |
+========================================================================+
|  YEAR   START     END       RETURN    P&L $       TRADES   WIN%        |
+------------------------------------------------------------------------+
|  2026   $509      $474      -6.9%     $-34.96     1090     31.8% ✗     |
+------------------------------------------------------------------------+
|  Profitable years                                             0/1  (0%)|
|  Best  year                                      2026   -6.9%   $-34.96|
|  Worst year                                      2026   -6.9%   $-34.96|
+========================================================================+
```

### Options bot full output

```text
options_reconcile: state=/home/runner/work/TradingBot/TradingBot/logs/options_trial/_state/lab_state.json
  open_lots=103 paper_keys=yes dry_run=False
  alpaca positions=20
options_reconcile: done
Layout: controlled:1024:lab0000_s200_w1_0928_1005_r1 (layout changed controlled:100:c000_s173_w1_0928_1005_r1 -> controlled:1024:lab0000_s200_w1_0928_1005_r1)
Trial layout: /home/runner/work/TradingBot/TradingBot/logs/options_trial
Docs:         skipped (local docs unavailable on this runner)
Buckets:      1024
=== options_morning_bot (PAPER) 2026-08-07T20:01:45.739188-04:00 ===

[Run context]
After hours (20:01 ET) — exit summary only.
Paper auth OK — equity $141981.52, account PA36KS87UPRS

[Exit summary]

[Portfolio snapshot]
+========================================================================+
|  OPTIONS BOT SUMMARY                                                   |
+------------------------------------------------------------------------+
|  Mode                          after_hours                             |
|  Equity                        $141,981.52                             |
|  Signals this run              0                                       |
|  Orders submitted (session)    64                                      |
|  Orders filled today (ledger)  60                                      |
|  Entries placed this run       0                                       |
|  Open virtual lots             103                                     |
|  Broker option positions       18                                      |
|  Pending orders                0                                       |
+========================================================================+
+========================================================================+
|  BUCKET LEADERBOARD (reflected ex-S173,S174)                           |
+------------------------------------------------------------------------+
|  Reflected trades=1480  buckets=290  win=39%                           |
|  Returns   avg=+18.9%  med=-37.0%  p10=-79.4%  p90=+129.5%             |
|  Realized  $+8,662.66                                                  |
|  Raw incl dropped  trades=2014  real=$+7,067.11                        |
|  Today     trades=86  avg=-30.0%  med=-59.7%  real=$-1,412.71          |
+------------------------------------------------------------------------+
|  BKT PROFILE               N  WIN  AVG%   MED%   BEST%  REAL$          |
+------------------------------------------------------------------------+
|  b383 lab0383_s362_w4_11  1 100% +1222.6 +1222.6 +1222.6 $   +379      |
|  b382 lab0382_s362_w4_11  1 100% +1125.8 +1125.8 +1125.8 $   +349      |
|  b860 lab0860_s408_w3_10  7  71% +638.1 +954.5 +1446.7 $   +833        |
|  b268 lab0268_s403_w4_11  3  67% +186.5 +320.0 +320.0 $   +115         |
|  b281 lab0281_s351_w1_09  4  75% +209.5 +272.4 +346.9 $   +310         |
|  b51  lab0051_s206_w2_10  1 100% +263.6 +263.6 +263.6 $   +174         |
|  b410 lab0410_s364_w4_11  3 100% +168.7 +233.3 +233.3 $   +183         |
|  b849 lab0849_s407_w4_11  5  60% +104.6 +229.2 +229.2 $   +115         |
|  ... 282 more bucket(s) with exits                                     |
+------------------------------------------------------------------------+
|  Low  b802 lab0802_s404_w2_10  5  40% -37.8 -98.2 -98.4 $   -100       |
+========================================================================+
+========================================================================+
|  PENDING EXITS (4)                                                     |
+------------------------------------------------------------------------+
|  b193 S218 UNH260814C00435000 x1 stop_loss (-55.1%)                    |
|  b0   ORPHAN TSLA260810C00347500 x3 stop_loss (-63.6%)                 |
|  b397 S363 MARA260814C00012000 x1 stop_loss (-87.0%)                   |
|  b406 S364 MARA260814C00011500 x1 stop_loss (-83.9%)                   |
+========================================================================+
+========================================================================+
|  OPEN OPTIONS (18)                                                     |
+------------------------------------------------------------------------+
|  SYMBOL                      QTY    RET%        OPEN P&L               |
|------------------------------------------------------------------------|
|  AMZN260807C00295000          34   -100.0%   $ -1,371.33               |
|  AMZN260807C00292500          16   -100.0%   $   -861.60               |
|  NKE260821C00044000           10    -49.2%   $   -310.00               |
|  MARA260814C00011500           7    -83.9%   $   -292.60               |
|  NKE260828C00045000           10    -44.6%   $   -281.67               |
|  AMZN260807C00297500           8   -100.0%   $   -271.38               |
|  AMD260807C00537500            4   -100.0%   $   -229.09               |
|  MARA260814C00012000           6    -87.0%   $   -200.00               |
|  ... 10 more position(s)                                               |
+========================================================================+
Full detail: logs/options_trial/runs/2026-08-07.log
elapsed=0.7s reconcile=0.1s
STATUS: options_morning_bot after-hours summary (PAPER) elapsed=0.7s. run=#6521 https://github.com/28twagg-ops/TradingBot/actions/runs/31228892186
Evaluation complete: 100 strategies evaluated, 0 killed, 0 promote candidates.
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_buckets.csv
Summary: 61 buckets closed trades, $-1,412.71 realized
STALE WARNING: 1 bucket(s) with open lots and last_entry >5d
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.md
Wrote /home/runner/work/TradingBot/TradingBot/logs/options_trial/reports/2026-08-07_strategy_selection.csv
Summary: keep=0 watch=86 drop=19
Orphan rate: 9.5% (192/2014)
# Options signal frequency

_Generated 2026-08-07T20:01:51.997799_

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
| State/ledger mismatches     |     9 | WARN | <<<
| Total open lots             |   103 | INFO |
| Total closed lots           |  1355 | INFO |
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

