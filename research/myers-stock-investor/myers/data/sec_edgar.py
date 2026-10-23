from __future__ import annotations

import os
from typing import Any

import requests

SEC_FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"


def _headers() -> dict[str, str]:
    ua = os.environ.get(
        "SEC_USER_AGENT",
        "MyersStockInvestor research@example.com",
    )
    return {"User-Agent": ua, "Accept": "application/json"}


def normalize_cik(cik: str | int) -> str:
    return str(cik).strip().zfill(10)


def fetch_company_facts(cik: str | int, timeout: float = 30.0) -> dict[str, Any] | None:
    """Fetch SEC XBRL company facts. Returns None on failure (never fabricates)."""
    url = SEC_FACTS_URL.format(cik=normalize_cik(cik))
    try:
        r = requests.get(url, headers=_headers(), timeout=timeout)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None


def latest_fact_value(facts: dict[str, Any], taxonomy: str, tag: str) -> float | None:
    try:
        units = facts["facts"][taxonomy][tag]["units"]
    except Exception:
        return None
    # Prefer USD
    series = units.get("USD") or next(iter(units.values()), None)
    if not series:
        return None
    # Prefer 10-K / FY filed most recently
    best = None
    best_filed = ""
    for row in series:
        form = (row.get("form") or "").upper()
        if form not in ("10-K", "10-K/A", "20-F"):
            continue
        filed = row.get("filed") or ""
        if filed >= best_filed:
            best_filed = filed
            best = row.get("val")
    try:
        return float(best) if best is not None else None
    except Exception:
        return None
