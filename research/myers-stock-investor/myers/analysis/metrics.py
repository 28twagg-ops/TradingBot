from __future__ import annotations

from myers.data.fundamentals import Fundamentals


def _div(a: float | None, b: float | None) -> float | None:
    if a is None or b is None or b == 0:
        return None
    return a / b


def compute_metrics(f: Fundamentals) -> dict[str, float | None]:
    """Deterministic Myers-style financial metrics. Missing -> None (never 0-fill)."""
    rev = f.revenue
    cogs = None
    if f.gross_profit is not None and rev is not None:
        cogs = rev - f.gross_profit

    net_debt = None
    if f.total_debt is not None and f.cash is not None:
        net_debt = f.total_debt - f.cash
    elif f.total_debt is not None:
        net_debt = f.total_debt

    fcf = f.free_cash_flow
    if fcf is None and f.operating_cash_flow is not None and f.capex is not None:
        fcf = f.operating_cash_flow + f.capex  # capex stored negative

    m: dict[str, float | None] = {
        "revenue": rev,
        "revenue_cagr_3y": _cagr(f.revenue_history, 3),
        "gross_margin": _div(f.gross_profit, rev),
        "operating_margin": _div(f.operating_income, rev),
        "ebitda_margin": _div(f.ebitda, rev),
        "net_margin": _div(f.net_income, rev),
        "ebitda": f.ebitda,
        "ebit": f.ebit,
        "net_debt": net_debt,
        "net_debt_to_ebitda": _div(net_debt, f.ebitda) if f.ebitda and f.ebitda > 0 else None,
        "interest_coverage": _div(f.ebit, f.interest_expense)
        if f.interest_expense and f.interest_expense > 0
        else None,
        "current_ratio": _div(f.current_assets, f.current_liabilities),
        "operating_cash_flow": f.operating_cash_flow,
        "free_cash_flow": fcf,
        "fcf_margin": _div(fcf, rev),
        "fcf_yield": _div(fcf, f.market_cap),
        "cash_conversion": _div(f.operating_cash_flow, f.net_income)
        if f.net_income and f.net_income > 0
        else None,
        "fcf_positive_years": float(sum(1 for x in f.fcf_history if x > 0))
        if f.fcf_history
        else None,
        "dso": _dso(f.receivables, rev),
        "dio": _dio(f.inventory, cogs),
        "dpo": _dpo(f.payables, cogs),
        "roic": _roic(f),
        "market_cap": f.market_cap,
        "shares_outstanding": f.shares_outstanding,
        "enterprise_value": f.enterprise_value,
        "total_debt": f.total_debt,
        "cash": f.cash,
    }
    # Cash conversion cycle
    if m["dso"] is not None and m["dio"] is not None and m["dpo"] is not None:
        m["ccc"] = m["dso"] + m["dio"] - m["dpo"]
    else:
        m["ccc"] = None
    return m


def _cagr(history_newest_first: list[float], years: int) -> float | None:
    if not history_newest_first or len(history_newest_first) < years:
        return None
    newest = history_newest_first[0]
    oldest = history_newest_first[years - 1]
    if oldest is None or oldest <= 0 or newest is None or newest <= 0:
        return None
    return (newest / oldest) ** (1.0 / (years - 1)) - 1.0


def _dso(ar: float | None, rev: float | None, days: float = 365.0) -> float | None:
    if ar is None or rev is None or rev <= 0:
        return None
    return ar / rev * days


def _dio(inv: float | None, cogs: float | None, days: float = 365.0) -> float | None:
    if inv is None or cogs is None or cogs <= 0:
        return None
    return inv / cogs * days


def _dpo(ap: float | None, cogs: float | None, days: float = 365.0) -> float | None:
    if ap is None or cogs is None or cogs <= 0:
        return None
    return ap / cogs * days


def _roic(f: Fundamentals) -> float | None:
    if f.operating_income is None:
        return None
    nopat = f.operating_income * 0.79  # default 21% tax heuristic when unknown
    invested = None
    if f.equity is not None and f.total_debt is not None and f.cash is not None:
        invested = f.equity + f.total_debt - f.cash
    elif f.total_assets is not None and f.current_liabilities is not None:
        invested = f.total_assets - f.current_liabilities
    if invested is None or invested <= 0:
        return None
    return nopat / invested
