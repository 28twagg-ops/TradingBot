from __future__ import annotations

from myers.config import StrategyConfig
from myers.data.fundamentals import Fundamentals
from myers.data.market import avg_dollar_volume
from datetime import date


def excluded_reason(f: Fundamentals, cfg: StrategyConfig, as_of: date) -> str | None:
    """Return exclusion reason or None if eligible for research universe."""
    qt = (f.quote_type or "").upper()
    for bad in cfg.universe.exclude_quote_types:
        if bad.upper() in qt:
            return f"quote_type={f.quote_type}"

    sector = f.sector or ""
    industry = f.industry or ""
    blob = f"{sector} {industry}".lower()
    for ex in cfg.universe.exclude_sectors:
        if ex.lower() in blob:
            return f"excluded_sector={sector or industry}"

    if f.market_cap is not None and f.market_cap < cfg.universe.min_market_cap:
        return f"market_cap<{cfg.universe.min_market_cap}"

    adv = avg_dollar_volume(f.ticker, as_of)
    if adv is not None and adv < cfg.universe.min_avg_dollar_volume:
        return f"avg_dollar_volume<{cfg.universe.min_avg_dollar_volume}"

    if len(f.revenue_history) < min(3, cfg.universe.min_years_financials):
        # Soft: only exclude if we have essentially no history
        if len(f.revenue_history) == 0 and f.revenue is None:
            return "insufficient_financial_history"

    return None
