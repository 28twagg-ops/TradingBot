# June 10 Incident Report
Generated: 2026-06-16 11:45 UTC

## Summary
- Stop-loss investigations logged: **12**
- Buys on 2026-06-10: **19**
- Sells on 2026-06-10: **12**
- PDT-deferred entries: **12**

## Afternoon stop breaches (same-day entries)

| Time | Ticker | Strategy | Breach P&L | Root cause | Sold same day? |
|------|--------|----------|------------|------------|----------------|
| 2026-06-10 14:00 | AA | GapDown | -2.13% | PDT guard deferred exit | no |
| 2026-06-10 14:00 | FCX | Pullback50 | -1.08% | PDT guard deferred exit | no |
| 2026-06-10 14:00 | GLW | Pullback50 | -0.96% | PDT guard deferred exit | no |
| 2026-06-10 14:00 | HL | GapDown | -0.80% | PDT guard deferred exit | no |
| 2026-06-10 14:00 | MU | GapDown | -1.41% | PDT guard deferred exit | no |
| 2026-06-10 14:15 | BILL | GapDown | -2.91% | PDT guard deferred exit | no |
| 2026-06-10 14:15 | PEGA | GapDown | -2.10% | PDT guard deferred exit | no |
| 2026-06-10 14:15 | SNPS | Pullback50 | -0.58% | PDT guard deferred exit | no |
| 2026-06-10 14:45 | NEM | GapDown | -1.09% | PDT guard deferred exit | no |
| 2026-06-10 15:00 | NVDA | Pullback50 | -0.87% | PDT guard deferred exit | no |
| 2026-06-10 15:15 | ORCL | GapDown | -1.09% | PDT guard deferred exit | no |
| 2026-06-10 19:00 | HAL | Pullback50 | -0.60% | PDT guard deferred exit | no |

## Execution audit (June 10)

| Action | Ticker | Expected | Actual | Slippage% | Method |
|--------|--------|----------|--------|-----------|--------|
| SELL | ABNB | 129.635 | 129.5 | -0.1041 | market_fallback |
| SELL | AME | 228.37 | 228.37 | 0.0 | market_fallback |
| SELL | AVGO | 383.295 | 383.16 | -0.0352 | limit_fill_position_check |
| SELL | COIN | 154.1479 | 154.172 | 0.0156 | limit_fill_position_check |
| SELL | DE | 577.0 | 577.0 | 0.0 | market_fallback |
| SELL | EME | 812.23 | 812.23 | 0.0 | market_fallback |
| SELL | NOVT | 158.87 | 159.57 | 0.4406 | market_fallback |
| SELL | NOW | 105.095 | 105.038 | -0.0542 | limit_fill_position_check |
| SELL | CB | 327.01 | 327.064 | 0.0165 | limit_fill_position_check |
| SELL | DRI | 203.055 | 202.698 | -0.1758 | limit_fill_position_check |
| SELL | GATX | 175.76 | 175.76 | 0.0 | market_fallback |
| BUY | JBHT | 279.01 | 279.01 | 0.0 | market_submit |
| BUY | MU | 927.52 | 927.52 | 0.0 | market_submit |
| BUY | NEM | 96.74 | 96.74 | 0.0 | market_submit |
| BUY | ODFL | 233.18 | 233.18 | 0.0 | market_submit |
| BUY | ORCL | 208.48 | 208.48 | 0.0 | market_submit |
| BUY | AA | 71.16 | 71.16 | 0.0 | market_submit |
| BUY | BILL | 33.99 | 33.99 | 0.0 | market_submit |
| BUY | HL | 14.46 | 14.46 | 0.0 | market_submit |
| BUY | KNX | 78.78 | 78.78 | 0.0 | market_submit |
| BUY | PEGA | 33.82 | 33.82 | 0.0 | market_submit |
| BUY | SAIA | 453.83 | 453.83 | 0.0 | market_submit |
| BUY | XPO | 216.91 | 216.91 | 0.0 | market_submit |
| BUY | GLW | 176.95 | 176.95 | 0.0 | market_submit |
| BUY | EA | 203.38 | 203.38 | 0.0 | market_submit |
| BUY | FCX | 64.4 | 64.4 | 0.0 | market_submit |
| BUY | HAL | 40.08 | 40.08 | 0.0 | market_submit |
| BUY | NVDA | 205.61 | 205.61 | 0.0 | market_submit |
| BUY | OKE | 88.96 | 88.96 | 0.0 | market_submit |
| BUY | SNPS | 471.23 | 471.23 | 0.0 | market_submit |
| SELL | CL | 89.695 | 89.686 | -0.01 | limit_fill_position_check |

## End-of-day open P&L (daily log): **$-10.00**

## Diagnosis
- Same-day buys could not exit on stop breach due to strict PDT guard.
- Fractional positions (~$20) skip broker GTC stops; software exit was deferred.
- Morning scan ~22 min after exits (universe fetch bottleneck).

## Recommended fixes (implemented in pipeline update)
- Prep/execute split with plan cache; parallel fetch; paper-relaxed same-day stop exits.