# live-bots/

Runtime trading systems. Ledgers stay under repo-root `logs/` (not here).

| Package | Entry (wrapper) | Canonical |
|---|---|---|
| rubber-band | `python rubber_band_bot.py` | `rubber-band/rubber_band_bot.py` |
| options-paper | `python scripts/options_morning_bot.py` | `options-paper/bot/` (+ lab/strategies/reporting) |
| options-micro | `python scripts/options_live_micro.py` | `options-micro/options_live_micro.py` |
| shared | collectors / log helpers | `shared/` |

Live options **entries** are gated off in GHA (`LIVE_OPTIONS_ENTRIES=0`).
