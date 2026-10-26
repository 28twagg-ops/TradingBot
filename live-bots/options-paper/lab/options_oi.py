"""
options_oi.py — Open-interest helper (resolves the Phase 1 OI gap).

Alpaca's options *market data* snapshot (OptionsSnapshot) does NOT expose open
interest. OI is available from the *Trading API* contract reference endpoint:
    GET /v2/options/contracts   (alpaca-py: TradingClient.get_option_contracts)
which returns `open_interest` + `open_interest_date` per contract.

NOTE ON LAG: OI is computed end-of-day by the OCC and distributed the next
business morning, so `open_interest` reflects ~1-2 trading days prior. Always
store `open_interest_date` alongside it so downstream code knows the as-of date.

This module has no import-time credential requirement; pass a TradingClient in.
Used by: options_data_collector.py, api_probe_options.py
"""

from __future__ import annotations

import logging
from datetime import date
from typing import Optional

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOptionContractsRequest

log = logging.getLogger(__name__)


def make_trading_client(api_key: str, api_secret: str, paper: bool = True) -> TradingClient:
    """Trading client for reference data (OI is account-agnostic; paper is fine)."""
    return TradingClient(api_key, api_secret, paper=paper)


def fetch_open_interest(
    client: TradingClient,
    underlying: str,
    strike_gte: Optional[float] = None,
    strike_lte: Optional[float] = None,
    exp_gte: Optional[date] = None,
    exp_lte: Optional[date] = None,
    max_pages: int = 10,
) -> dict[str, dict]:
    """Return {contract_symbol: {"open_interest": int|None, "open_interest_date": str|None}}.

    Filters mirror the chain request (strike band + expiry window) so the result
    can be joined to chain snapshots by contract symbol. Paginates up to
    max_pages (1000 contracts/page). Returns {} on error (caller keeps OI=None).
    """
    oi_map: dict[str, dict] = {}
    token: Optional[str] = None
    pages = 0
    while pages < max_pages:
        try:
            req = GetOptionContractsRequest(
                underlying_symbols=[underlying],
                expiration_date_gte=exp_gte,
                expiration_date_lte=exp_lte,
                strike_price_gte=str(strike_gte) if strike_gte is not None else None,
                strike_price_lte=str(strike_lte) if strike_lte is not None else None,
                limit=1000,
                page_token=token,
            )
            resp = client.get_option_contracts(req)
        except Exception as exc:
            log.warning("OI fetch failed for %s: %s", underlying, exc)
            break

        for c in (resp.option_contracts or []):
            oi_raw = getattr(c, "open_interest", None)
            try:
                oi_val = int(oi_raw) if oi_raw is not None else None
            except (TypeError, ValueError):
                oi_val = None
            oi_date = getattr(c, "open_interest_date", None)
            oi_map[c.symbol] = {
                "open_interest": oi_val,
                "open_interest_date": str(oi_date) if oi_date else None,
            }

        token = getattr(resp, "next_page_token", None)
        pages += 1
        if not token:
            break
    return oi_map
