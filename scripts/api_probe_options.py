"""
api_probe_options.py — Task 1.1: Options API probe.

Pulls current options chain for 5 test symbols (AAPL, JPM, NVDA, EPAM [MidCap],
SPY), prints field availability, greeks Y/N, bid/ask, spread %, open interest,
contract count, and request timing.

Saves raw output to data/api_probe_<YYYY-MM-DD>.json.
Results notes template: data/api_probe_notes.md (created if absent).

Run:
    ALPACA_API_KEY=... ALPACA_SECRET_KEY=... python scripts/api_probe_options.py

Gate 1A: run without errors, ≥3/5 symbols return data, call counts documented,
greeks availability confirmed, typical ATM spread documented.
"""

from __future__ import annotations

import json
import os
import sys
import time
from datetime import date, timedelta
from pathlib import Path

from alpaca.data.historical import OptionHistoricalDataClient
from alpaca.data.requests import OptionChainRequest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from options_oi import make_trading_client, fetch_open_interest

# ---------------------------------------------------------------------------
# Credentials
# ---------------------------------------------------------------------------
API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_SECRET_KEY")
if not API_KEY or not API_SECRET:
    print("ERROR: Set ALPACA_API_KEY and ALPACA_SECRET_KEY environment variables.")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
_REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = _REPO_ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

PROBE_SYMBOLS = ["AAPL", "JPM", "NVDA", "EPAM", "SPY"]  # EPAM = MidCap representative
TODAY = date.today()
EXPIRY_WINDOW_DAYS = 60          # fetch expirations within next 60 days; filter to 2 nearest
STRIKE_PCT = 0.07                # ±7% around last traded price


def _get_approx_price(snap_dict: dict) -> float | None:
    """Extract approximate underlying price from the first snapshot available."""
    for snap in snap_dict.values():
        lq = snap.latest_quote
        lt = snap.latest_trade
        if lq and lq.ask_price:
            return (lq.bid_price + lq.ask_price) / 2
        if lt and lt.price:
            return lt.price
    return None


def probe_symbol(client: OptionHistoricalDataClient, symbol: str,
                 trading_client=None) -> dict:
    """Probe one symbol: fetch chain, filter to nearest 2 expiries + ±7% strikes."""
    result: dict = {"symbol": symbol, "error": None, "contracts": []}

    t0 = time.monotonic()

    # Step 1: fetch full chain within expiry window to discover available expirations
    try:
        req_all = OptionChainRequest(
            underlying_symbol=symbol,
            expiration_date_gte=TODAY,
            expiration_date_lte=TODAY + timedelta(days=EXPIRY_WINDOW_DAYS),
        )
        chain_all = client.get_option_chain(req_all)  # Dict[str, OptionsSnapshot]
    except Exception as exc:
        result["error"] = str(exc)
        result["elapsed_s"] = round(time.monotonic() - t0, 3)
        return result

    if not chain_all:
        result["error"] = "empty chain"
        result["elapsed_s"] = round(time.monotonic() - t0, 3)
        return result

    # Step 2: find nearest 2 expirations
    expirations: set[str] = set()
    for sym, snap in chain_all.items():
        # Option symbol format: <underlying><YYMMDD><C/P><strike*1000>
        # Expiration is embedded in the symbol but OptionsSnapshot doesn't expose it
        # directly; we derive it from the contract symbol (chars 6-11 after underlying len)
        # E.g. AAPL250117C00150000 -> 250117 -> 2025-01-17
        # More robustly, collect all and sort
        parts = sym[len(symbol):]  # strip underlying prefix
        if len(parts) >= 6:
            date_part = parts[:6]
            try:
                exp = date(2000 + int(date_part[:2]), int(date_part[2:4]), int(date_part[4:6]))
                expirations.add(str(exp))
            except ValueError:
                pass

    nearest_2 = sorted(expirations)[:2]

    # Step 3: estimate underlying price from the chain
    approx_price = _get_approx_price(chain_all)

    # Step 4: fetch filtered chain for nearest 2 expiries
    contracts_info = []
    total_raw_api_calls = 1  # already made one

    for expiry_str in nearest_2:
        expiry = date.fromisoformat(expiry_str)
        req_params: dict = dict(
            underlying_symbol=symbol,
            expiration_date=expiry,
        )
        if approx_price:
            req_params["strike_price_gte"] = round(approx_price * (1 - STRIKE_PCT), 2)
            req_params["strike_price_lte"] = round(approx_price * (1 + STRIKE_PCT), 2)

        try:
            chain = client.get_option_chain(OptionChainRequest(**req_params))
            total_raw_api_calls += 1
        except Exception as exc:
            contracts_info.append({"expiry": expiry_str, "error": str(exc)})
            continue

        # Open interest from the Trading API contracts endpoint (not the chain).
        oi_map: dict = {}
        if trading_client is not None:
            oi_map = fetch_open_interest(
                trading_client, symbol,
                strike_gte=req_params.get("strike_price_gte"),
                strike_lte=req_params.get("strike_price_lte"),
                exp_gte=expiry, exp_lte=expiry,
            )
            total_raw_api_calls += 1

        for contract_sym, snap in chain.items():
            lq = snap.latest_quote
            lt = snap.latest_trade
            greeks = snap.greeks

            bid = lq.bid_price if lq else None
            ask = lq.ask_price if lq else None
            mid = ((bid + ask) / 2) if (bid is not None and ask is not None) else None
            spread_pct = ((ask - bid) / mid * 100) if (mid and mid > 0) else None

            # OI resolved via Trading API contracts endpoint (1-2 day OCC lag).
            oi_rec = oi_map.get(contract_sym, {})
            oi = oi_rec.get("open_interest")

            contracts_info.append({
                "contract_symbol": contract_sym,
                "expiry": expiry_str,
                "bid": bid,
                "ask": ask,
                "mid": mid,
                "spread_pct": round(spread_pct, 2) if spread_pct is not None else None,
                "open_interest": oi,
                "open_interest_date": oi_rec.get("open_interest_date"),
                "last_trade_price": lt.price if lt else None,
                "implied_volatility": snap.implied_volatility,
                "greeks_present": greeks is not None,
                "delta": greeks.delta if greeks else None,
                "gamma": greeks.gamma if greeks else None,
                "theta": greeks.theta if greeks else None,
                "vega": greeks.vega if greeks else None,
                "rho": greeks.rho if greeks else None,
            })

    elapsed = round(time.monotonic() - t0, 3)

    result.update({
        "approx_underlying_price": approx_price,
        "nearest_2_expiries": nearest_2,
        "total_contracts_in_window": len(chain_all),
        "contracts_filtered": len(contracts_info),
        "api_calls_made": total_raw_api_calls,
        "elapsed_s": elapsed,
        "greeks_present": any(c.get("greeks_present") for c in contracts_info),
        "contracts": contracts_info,
    })
    return result


def main() -> None:
    client = OptionHistoricalDataClient(API_KEY, API_SECRET)
    trading_client = make_trading_client(API_KEY, API_SECRET, paper=True)
    output: dict = {"probe_date": str(TODAY), "symbols": {}}

    for sym in PROBE_SYMBOLS:
        print(f"\n{'='*60}")
        print(f"Probing {sym} …")
        res = probe_symbol(client, sym, trading_client=trading_client)
        output["symbols"][sym] = res

        if res.get("error"):
            print(f"  ERROR: {res['error']}")
        else:
            n_contracts = res["contracts_filtered"]
            print(f"  Underlying price: {res['approx_underlying_price']}")
            print(f"  Nearest 2 expiries: {res['nearest_2_expiries']}")
            print(f"  Contracts in ±7%/2-expiry window: {n_contracts}")
            print(f"  Total contracts in 60d window: {res['total_contracts_in_window']}")
            print(f"  API calls made: {res['api_calls_made']}")
            print(f"  Elapsed: {res['elapsed_s']}s")
            print(f"  Greeks present: {res['greeks_present']}")

            # Print a sample ATM contract
            atm_candidates = [
                c for c in res["contracts"]
                if c.get("bid") and c.get("ask") and not c.get("error")
            ]
            if atm_candidates:
                sample = atm_candidates[len(atm_candidates) // 2]
                print(f"  Sample contract ({sample['contract_symbol']}):")
                print(f"    bid={sample['bid']} ask={sample['ask']} "
                      f"mid={sample['mid']} spread%={sample['spread_pct']}")
                print(f"    IV={sample['implied_volatility']} "
                      f"delta={sample['delta']} theta={sample['theta']}")

    # Save raw output
    out_path = DATA_DIR / f"api_probe_{TODAY}.json"
    out_path.write_text(json.dumps(output, indent=2, default=str), encoding="utf-8")
    print(f"\nRaw output saved: {out_path}")

    # Summary for Gate 1A
    successes = sum(
        1 for v in output["symbols"].values()
        if not v.get("error") and v.get("contracts_filtered", 0) > 0
    )
    print(f"\nGate 1A: {successes}/5 symbols returned data "
          f"({'PASS' if successes >= 3 else 'FAIL - need 3+'}).")

    # Notes template
    notes_path = DATA_DIR / "api_probe_notes.md"
    if not notes_path.exists():
        notes_path.write_text(
            f"# Options API Probe Notes — {TODAY}\n\n"
            "## Gate 1A Checklist\n"
            "- [ ] Probe ran without errors\n"
            "- [ ] ≥3/5 symbols returned options data\n"
            "- [ ] Call count per symbol documented\n"
            "- [ ] Greeks availability confirmed\n"
            "- [ ] Typical ATM bid-ask spread documented\n\n"
            "## Findings\n\n"
            f"See `data/api_probe_{TODAY}.json` for raw output.\n\n"
            "### Call counts (fill in after run)\n\n"
            "### Greeks availability\n\n"
            "### Typical ATM spread %\n\n"
            "### Rate limit observations\n",
            encoding="utf-8",
        )
        print(f"Notes template created: {notes_path}")


if __name__ == "__main__":
    main()
