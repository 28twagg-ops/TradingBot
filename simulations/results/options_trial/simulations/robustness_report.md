# Options Robustness Tests
Source: catalog_historical_2026-07-03_merged_with_pct.csv


## 1. Baseline top-5 (symbol-mean return %)
strategy_id            strategy_name  symbols  total_filled  avg_return_pct  med_return_pct  pct_positive_syms
       S173    MomReversal long call      904    53650.0000          2.3969          1.5492             0.9392
       S174 RubberBand long call EOD      902    83816.0000          0.8433          0.4895             0.9956
       S165  GapDown long call 3 DTE      902    88460.0000          0.4966         -0.1925             0.9279
       S166      GapDown strong call      903    50227.0000          0.3975         -0.0816             0.9048
       S163  A1 GapDown ATM call EOD      902   104472.0000          0.2657         -0.0852             0.9069

## 2. After dropping top 5% symbol outliers per strategy
strategy_id            strategy_name  symbols  total_filled  avg_return_pct  med_return_pct  pct_positive_syms
       S173    MomReversal long call      858    50286.0000          2.2263          1.4962             0.9359
       S174 RubberBand long call EOD      856    78183.0000          0.7979          0.4764             0.9953
       S165  GapDown long call 3 DTE      856    83057.0000          0.4474         -0.2042             0.9241
       S166      GapDown strong call      857    47134.0000          0.3513         -0.0929             0.8996
       S163  A1 GapDown ATM call EOD      856    98503.0000          0.2376         -0.0923             0.9019

## 3. Robust filter (avg>0, median>0, 50+ symbols)
strategy_id            strategy_name  symbols  total_filled  avg_return_pct  med_return_pct  pct_positive_syms
       S173    MomReversal long call      904    53650.0000          2.3969          1.5492             0.9392
       S174 RubberBand long call EOD      902    83816.0000          0.8433          0.4895             0.9956

## 4. Fill-weighted avg return/trade (top 5): 76.43%

### S173 symbol distribution: p10=112.18% p50=234.37% p90=363.64% pct_pos=94%

### S174 symbol distribution: p10=53.06% p50=79.39% p90=122.47% pct_pos=100%

### S165 symbol distribution: p10=6.22% p50=46.16% p90=93.49% pct_pos=93%

### S166 symbol distribution: p10=0.33% p50=38.06% p90=80.30% pct_pos=90%

### S163 symbol distribution: p10=1.56% p50=25.27% p90=52.81% pct_pos=91%

## 6. Bootstrap 50-trade $500 proxy (12% premium/trade)
  median ending return: 11063.7%
  5th percentile:       3811.1%
  95th percentile:      39112.9%
  % simulations loss:   0.0%

## 7. Full universe robust top 15 (for challenger ideas)
strategy_id              strategy_name          category  symbols  total_filled  avg_return_pct  med_return_pct
       S173      MomReversal long call     equity_signal      904    53650.0000          2.3969          1.5492
       S020       Long put 52wk low BD  directional_long      882     1313.0000          1.1054          0.6378
       S192        Power hour fade put          intraday      904    55232.0000          0.9614          0.5497
       S030        Short put failed BD directional_short      904    39569.0000          0.5010          0.5449
       S185      ORB breakout call 15m          intraday      902   176330.0000          0.8887          0.5331
       S029       Short call failed BO directional_short      904    44170.0000          0.5033          0.5320
       S186      ORB breakdown put 15m          intraday      902   183670.0000          0.8528          0.5258
       S018    Long put sector laggard  directional_long      901    38497.0000          0.9884          0.5069
       S017    Long call sector leader  directional_long      900    37913.0000          1.0795          0.4931
       S174   RubberBand long call EOD     equity_signal      902    83816.0000          0.8433          0.4895
       S019     Long call 52wk high BO  directional_long      898     8173.0000          0.7937          0.4865
       S190    Midday consolidation BO          intraday      902   214130.0000          0.7642          0.4262
       S170 Pullback50 long call 3 DTE     equity_signal      900   194640.0000          0.8548          0.4015
       S193         10AM reversal call          intraday      904   138598.0000          0.7481          0.3875
       S188     VWAP reclaim long call          intraday      902   281373.0000          0.5946          0.2778