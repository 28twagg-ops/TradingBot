# Options Data Source Evaluations (Master Plan v3, Section 9)

Generated: 2026-06-25
Context: small ($500) retail options bot. Currently uses Alpaca for stock data.
Needs 1-minute stock + options data (chains, greeks, IV, OI, bid/ask) for the
S&P 500 + S&P 400 MidCap universe (~900 symbols).

Verification: prices/capabilities checked against vendor docs and 2026 web
sources on 2026-06-25. Anything not directly confirmed is marked NEEDS-VERIFY.

---

## TL;DR recommendation

- **Development / backtest dataset (now):** keep the plan's own approach —
  **self-collect** Alpaca 1-minute stock + options snapshots forward via
  `options_data_collector.py`. This is the only way to get intraday 1-min
  options history for free, because no free vendor sells historical *intraday*
  options data. Use `yfinance` only for current-snapshot engine debugging
  (it has NO historical option prices).
- **Open interest (resolves the Phase 1 blocker):** Alpaca's option *chain*
  snapshot does NOT include OI. Use the Trading API endpoint
  `GET /v2/options/contracts/{symbol_or_id}` which returns `open_interest`
  and `open_interest_date`. Expect a 1-2 business-day OCC lag (true of all
  providers). Wire this into the collector (batch ATM +/-7% strikes).
- **Live data:** Alpaca Basic = indicative (15-min delayed) options feed,
  free. For real-time OPRA you need **Algo Trader Plus** (paid). Start on the
  free indicative feed for paper trading; only pay once a strategy clears the
  paper gate.
- **Best free *historical* (EOD) source:** WRDS / OptionMetrics IvyDB IF
  Oklahoma State subscribes. EOD only (not intraday), but gold-standard back
  to 1996 — worth ~1 hour to check OSU access. Good for daily-hold validation,
  not intraday scalps.

---

## Source-by-source

### 1. Alpaca (current provider)

| Field | Detail |
|-------|--------|
| Chains / quotes | `OptionHistoricalDataClient.get_option_chain` -> bid/ask, size |
| Greeks / IV | Included in chain snapshot (delta, gamma, theta, vega, rho, IV) |
| Open interest | NOT in chain. Use Trading API `GET /v2/options/contracts/{symbol_or_id}` -> `open_interest` + `open_interest_date` (1-2 day OCC lag) |
| Free (Basic) feed | Indicative pricing feed, 15-min delayed; historical limited to latest 15 min; 200 req/min |
| Paid (Algo Trader Plus) | Real-time OPRA feed; no historical restriction; 10,000 req/min. Individual price ~\$99/mo NEEDS-VERIFY (partner "Standard" tiers run \$500-\$2,000/mo + \$1,000 options add-on) |
| Historical depth | Option data since **Feb 2024** only |
| Verdict | KEEP as primary. Free indicative feed is enough for paper trading + forward self-collection. Resolves OI via the contracts endpoint. |

Key consequence: because Basic blocks pulling *old* historical, the plan's
forward self-collection (store 1-min snapshots daily) is the correct path to a
backtestable intraday dataset at zero cost.

### 2. yfinance

| Field | Detail |
|-------|--------|
| Chains | `Ticker.option_chain(expiry)` -> calls/puts with bid/ask, volume, OI, IV |
| Greeks | NOT provided (IV only) |
| History | **Current snapshot ONLY** — no historical option prices |
| Latency | ~15-min delayed, unofficial Yahoo scrape (can break without notice) |
| Cost | Free |
| Verdict | DEV/debug ONLY (matches plan). Cannot backtest historical option P&L. Useful to sanity-check chain structure and the engine's data loader. |

### 3. Polygon.io (rebranded "Massive", Oct 2025)

| Field | Detail |
|-------|--------|
| Free tier | Stocks only, EOD, ~5 calls/min. **No free options data.** |
| Options Developer | ~\$79-99/mo, 15-min delayed, greeks/IV/OI, ~4-10yr history |
| Options Advanced | \$199/mo, real-time greeks/IV, tick history, websockets |
| Verdict | SUPPLEMENT (paid). Only compelling if you want deep *historical intraday* options for backtesting and are willing to pay. Not needed at Tier 0. Pricing/branding in flux post-rebrand — NEEDS-VERIFY at massive.com/pricing?product=options |

### 4. WRDS / OptionMetrics (IvyDB) via OSU

| Field | Detail |
|-------|--------|
| Coverage | Gold-standard historical US options: EOD prices, IV, greeks, OI, volume |
| Depth | Back to ~1996 |
| Granularity | **EOD only** (no intraday/1-min) |
| Latency | Academic, not real-time |
| Cost | Free *if* the university subscribes; via wrds.wharton.upenn.edu with OSU credentials |
| Verdict | BEST FREE HISTORICAL if available — but EOD only, so good for daily/multi-day hold validation, not the morning intraday scalps. ACTION: confirm OSU subscribes to WRDS *and* the OptionMetrics module (many schools have WRDS but not OptionMetrics). NEEDS-VERIFY. |

### 5. CBOE DataShop

| Field | Detail |
|-------|--------|
| Data | Historical options (incl. intraday/tick) sold per-dataset |
| Free | Limited sample datasets only |
| Cost | Mostly paid, can be expensive for full intraday history |
| Verdict | NOT useful free; only if a specific paid historical slice is needed. NEEDS-VERIFY current sample availability. |

### 6. Schwab API (former TD Ameritrade)

| Field | Detail |
|-------|--------|
| Data | Real-time options chains with greeks for brokerage customers (post TDA->Schwab migration) |
| Auth | OAuth; requires a Schwab brokerage account + developer app approval |
| History | Shallow; not a backtesting source |
| Cost | Free for account holders |
| Verdict | POSSIBLE free real-time supplement if you have/open a Schwab account. Adds complexity (separate auth) with little benefit over Alpaca for this bot. Low priority. NEEDS-VERIFY post-migration API status. |

---

## Concrete next steps

1. **Wire OI into the collector** using `GET /v2/options/contracts/{symbol_or_id}`
   (batch ATM +/-7% strikes), and store `open_interest_date` so the sim knows
   the lag. This removes the Phase 1 OI TODO. (Highest value, do first.)
2. **Run the Gate 1A probe** (`api_probe_options.py`) with live keys to confirm
   greeks/IV presence and real spread %, on the free indicative feed.
3. **Check OSU WRDS access** (~1 hour): log in at wrds.wharton.upenn.edu; confirm
   the OptionMetrics/IvyDB module is included. If yes, it becomes the EOD
   validation backstop for daily-hold mechanics.
4. **Stay free until a strategy clears the paper gate.** Only consider paid
   real-time (Alpaca Algo Trader Plus, or Polygon/Massive Advanced) once a
   variant is proven and you need real-time OPRA for live fills.
