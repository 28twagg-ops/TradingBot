from __future__ import annotations

from myers.config import ValuationConfig
from myers.data.fundamentals import Fundamentals
from myers.schemas import ValuationResult


def _enterprise_value(f: Fundamentals, price: float | None) -> float | None:
    if f.enterprise_value is not None:
        return f.enterprise_value
    if f.market_cap is None and (price is None or f.shares_outstanding is None):
        return None
    equity = f.market_cap
    if equity is None and price is not None and f.shares_outstanding is not None:
        equity = price * f.shares_outstanding
    debt = f.total_debt or 0.0
    cash = f.cash or 0.0
    if equity is None:
        return None
    return equity + debt - cash


def _dcf_equity_per_share(
    f: Fundamentals,
    *,
    growth: float,
    margin: float,
    wacc: float,
    terminal_growth: float,
    years: int,
) -> float | None:
    """Simple FCFF DCF from revenue * FCF margin proxy, then to equity / share."""
    if f.revenue is None or f.revenue <= 0:
        return None
    if f.shares_outstanding is None or f.shares_outstanding <= 0:
        return None
    # Start from trailing FCF if available, else revenue * margin
    if f.free_cash_flow is not None and f.free_cash_flow > 0:
        fcf0 = f.free_cash_flow
    else:
        fcf0 = f.revenue * margin
    if fcf0 <= 0:
        return None
    if wacc <= terminal_growth:
        return None

    pv = 0.0
    fcf = fcf0
    for t in range(1, years + 1):
        fcf *= 1.0 + growth
        pv += fcf / ((1.0 + wacc) ** t)
    terminal = fcf * (1.0 + terminal_growth) / (wacc - terminal_growth)
    pv += terminal / ((1.0 + wacc) ** years)

    # FCFF approximates firm value; subtract net debt
    net_debt = 0.0
    if f.total_debt is not None:
        net_debt += f.total_debt
    if f.cash is not None:
        net_debt -= f.cash
    equity = pv - net_debt
    if equity <= 0:
        return None
    return equity / f.shares_outstanding


def value_company(
    f: Fundamentals,
    metrics: dict[str, float | None],
    price: float | None,
    cfg: ValuationConfig,
) -> ValuationResult:
    ev = _enterprise_value(f, price)
    ebitda = metrics.get("ebitda")
    ebit = metrics.get("ebit")
    fcf = metrics.get("free_cash_flow")
    ni = f.net_income

    ev_ebitda = (ev / ebitda) if ev and ebitda and ebitda > 0 else None
    ev_ebit = (ev / ebit) if ev and ebit and ebit > 0 else None
    pe = (f.market_cap / ni) if f.market_cap and ni and ni > 0 else None
    if pe is None and price is not None and ni and f.shares_outstanding and ni > 0:
        eps = ni / f.shares_outstanding
        pe = price / eps if eps > 0 else None
    p_fcf = (f.market_cap / fcf) if f.market_cap and fcf and fcf > 0 else None
    fcf_yield = metrics.get("fcf_yield")

    fcf_margin = metrics.get("fcf_margin") or 0.08
    if fcf_margin <= 0:
        fcf_margin = 0.05

    bear = _dcf_equity_per_share(
        f,
        growth=0.01,
        margin=max(0.03, fcf_margin * 0.7),
        wacc=cfg.wacc_default + 0.02,
        terminal_growth=max(0.01, cfg.terminal_growth - 0.005),
        years=cfg.projection_years,
    )
    base = _dcf_equity_per_share(
        f,
        growth=0.04,
        margin=fcf_margin,
        wacc=cfg.wacc_default,
        terminal_growth=cfg.terminal_growth,
        years=cfg.projection_years,
    )
    bull = _dcf_equity_per_share(
        f,
        growth=0.08,
        margin=min(0.25, fcf_margin * 1.2),
        wacc=max(0.06, cfg.wacc_default - 0.01),
        terminal_growth=cfg.terminal_growth + 0.005,
        years=cfg.projection_years,
    )

    mos = None
    if base is not None and price is not None and base > 0:
        mos = (base - price) / base

    implied_g, implied_note = reverse_dcf_implied_growth(
        f,
        price=price,
        margin=fcf_margin,
        wacc=cfg.wacc_default,
        terminal_growth=cfg.terminal_growth,
        years=cfg.projection_years,
    )

    return ValuationResult(
        enterprise_value=ev,
        ev_to_ebitda=ev_ebitda,
        ev_to_ebit=ev_ebit,
        price_to_earnings=pe,
        price_to_fcf=p_fcf,
        fcf_yield=fcf_yield,
        fair_value_bear=bear,
        fair_value_base=base,
        fair_value_bull=bull,
        base_margin_of_safety=mos,
        reverse_dcf_implied_growth=implied_g,
        reverse_dcf_interpretation=implied_note,
        assumptions={
            "wacc_default": cfg.wacc_default,
            "terminal_growth": cfg.terminal_growth,
            "projection_years": cfg.projection_years,
            "fcf_margin_used": fcf_margin,
            "lease_treatment": "excluded (not separated in yfinance feed)",
            "cash_treatment": "total cash equivalents subtracted from EV",
        },
    )


def reverse_dcf_implied_growth(
    f: Fundamentals,
    *,
    price: float | None,
    margin: float,
    wacc: float,
    terminal_growth: float,
    years: int,
) -> tuple[float | None, str]:
    """Solve for constant FCF growth that equates DCF equity/share to market price."""
    if price is None or price <= 0:
        return None, "Insufficient evidence (no price)"
    if f.shares_outstanding is None or f.shares_outstanding <= 0:
        return None, "Insufficient evidence (no share count)"
    if f.free_cash_flow is not None and f.free_cash_flow > 0:
        fcf0 = f.free_cash_flow
    elif f.revenue is not None and f.revenue > 0:
        fcf0 = f.revenue * max(margin, 0.01)
    else:
        return None, "Insufficient evidence (no FCF/revenue)"

    target_equity = price * f.shares_outstanding
    net_debt = (f.total_debt or 0.0) - (f.cash or 0.0)
    target_ev = target_equity + net_debt
    if target_ev <= 0:
        return None, "Insufficient evidence (non-positive target EV)"

    def _pv(growth: float) -> float:
        if wacc <= terminal_growth:
            return float("inf")
        fcf = fcf0
        pv = 0.0
        for t in range(1, years + 1):
            fcf *= 1.0 + growth
            pv += fcf / ((1.0 + wacc) ** t)
        terminal = fcf * (1.0 + terminal_growth) / (wacc - terminal_growth)
        pv += terminal / ((1.0 + wacc) ** years)
        return pv

    # Binary search growth in [-20%, +40%]
    lo, hi = -0.20, 0.40
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if _pv(mid) < target_ev:
            lo = mid
        else:
            hi = mid
    implied = 0.5 * (lo + hi)

    hist = None
    if f.revenue_history and len(f.revenue_history) >= 3:
        try:
            newest, oldest = f.revenue_history[0], f.revenue_history[2]
            if oldest and oldest > 0 and newest and newest > 0:
                hist = (newest / oldest) ** 0.5 - 1.0
        except Exception:
            hist = None

    if implied > 0.20:
        note = "Market expectations appear demanding"
    elif hist is not None and implied > hist + 0.05:
        note = "Market expectations appear demanding vs recent history"
    elif implied < 0.0:
        note = "Market expectations appear conservative (implied decline/flat)"
    elif hist is not None and abs(implied - hist) <= 0.05:
        note = "Market expectations appear reasonable vs recent history"
    else:
        note = "Market expectations appear moderate; compare to industry/risks"
    return implied, note
