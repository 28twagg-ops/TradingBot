from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from typing import Any

import numpy as np
import pandas as pd
import yfinance as yf


def _safe_float(x: Any) -> float | None:
    try:
        if x is None or (isinstance(x, float) and np.isnan(x)):
            return None
        v = float(x)
        if np.isnan(v) or np.isinf(v):
            return None
        return v
    except Exception:
        return None


def _series_last(df: pd.DataFrame | None, row_names: list[str]) -> float | None:
    if df is None or df.empty:
        return None
    for name in row_names:
        if name in df.index:
            s = df.loc[name].dropna()
            if len(s):
                return _safe_float(s.iloc[0])  # yfinance columns newest-first
    # case-insensitive fallback
    lower_map = {str(i).lower(): i for i in df.index}
    for name in row_names:
        key = name.lower()
        if key in lower_map:
            s = df.loc[lower_map[key]].dropna()
            if len(s):
                return _safe_float(s.iloc[0])
    return None


def _series_history(df: pd.DataFrame | None, row_names: list[str], n: int = 5) -> list[float]:
    if df is None or df.empty:
        return []
    for name in row_names:
        idx = None
        if name in df.index:
            idx = name
        else:
            lower_map = {str(i).lower(): i for i in df.index}
            if name.lower() in lower_map:
                idx = lower_map[name.lower()]
        if idx is None:
            continue
        s = df.loc[idx].dropna()
        vals = [_safe_float(v) for v in s.tolist()[:n]]
        return [v for v in vals if v is not None]
    return []


@dataclass
class Fundamentals:
    ticker: str
    retrieved_at: datetime
    as_of_request: date
    company_name: str | None = None
    sector: str | None = None
    industry: str | None = None
    quote_type: str | None = None
    currency: str = "USD"
    market_cap: float | None = None
    shares_outstanding: float | None = None
    enterprise_value: float | None = None
    # Income
    revenue: float | None = None
    revenue_history: list[float] = field(default_factory=list)
    gross_profit: float | None = None
    operating_income: float | None = None
    ebit: float | None = None
    ebitda: float | None = None
    net_income: float | None = None
    interest_expense: float | None = None
    # Balance
    total_debt: float | None = None
    cash: float | None = None
    current_assets: float | None = None
    current_liabilities: float | None = None
    total_assets: float | None = None
    equity: float | None = None
    receivables: float | None = None
    inventory: float | None = None
    payables: float | None = None
    # Cash flow
    operating_cash_flow: float | None = None
    capex: float | None = None
    free_cash_flow: float | None = None
    fcf_history: list[float] = field(default_factory=list)
    # Meta
    source: str = "yfinance"
    missing: list[str] = field(default_factory=list)

    def mark_missing(self) -> None:
        required = {
            "revenue": self.revenue,
            "operating_income": self.operating_income,
            "net_income": self.net_income,
            "operating_cash_flow": self.operating_cash_flow,
            "total_debt": self.total_debt,
            "cash": self.cash,
            "market_cap": self.market_cap,
        }
        self.missing = [k for k, v in required.items() if v is None]


def fetch_fundamentals(ticker: str, as_of: date | None = None) -> Fundamentals:
    """Fetch latest available fundamentals for ticker.

    NOTE: yfinance does not provide true point-in-time restatement-aware
    fundamentals. Callers must disclose this limitation in reports/backtests.
    """
    as_of = as_of or date.today()
    t = yf.Ticker(ticker)
    info = {}
    try:
        info = t.info or {}
    except Exception:
        info = {}

    try:
        income = t.financials
    except Exception:
        income = None
    try:
        balance = t.balance_sheet
    except Exception:
        balance = None
    try:
        cashflow = t.cashflow
    except Exception:
        cashflow = None

    rev = _series_last(income, ["Total Revenue", "Operating Revenue", "Revenue"])
    gp = _series_last(income, ["Gross Profit"])
    opinc = _series_last(income, ["Operating Income", "EBIT"])
    ebit = _series_last(income, ["EBIT", "Operating Income"])
    ni = _series_last(income, ["Net Income", "Net Income Common Stockholders"])
    interest = _series_last(income, ["Interest Expense", "Interest Expense Non Operating"])

    ebitda = _safe_float(info.get("ebitda"))
    if ebitda is None and ebit is not None:
        da = _series_last(cashflow, ["Depreciation And Amortization", "Depreciation"])
        if da is not None:
            ebitda = ebit + abs(da)

    cash = _series_last(
        balance,
        ["Cash And Cash Equivalents", "Cash Cash Equivalents And Short Term Investments", "Cash"],
    )
    if cash is None:
        cash = _safe_float(info.get("totalCash"))

    debt = _series_last(balance, ["Total Debt", "Long Term Debt"])
    if debt is None:
        # Compose short + long if present
        st = _series_last(balance, ["Current Debt", "Short Long Term Debt"])
        lt = _series_last(balance, ["Long Term Debt"])
        if st is not None or lt is not None:
            debt = (st or 0.0) + (lt or 0.0)
    if debt is None:
        debt = _safe_float(info.get("totalDebt"))

    ca = _series_last(balance, ["Current Assets"])
    cl = _series_last(balance, ["Current Liabilities"])
    ta = _series_last(balance, ["Total Assets"])
    eq = _series_last(balance, ["Stockholders Equity", "Total Equity Gross Minority Interest"])
    ar = _series_last(balance, ["Receivables", "Net Receivables", "Accounts Receivable"])
    inv = _series_last(balance, ["Inventory"])
    ap = _series_last(balance, ["Accounts Payable", "Payables"])

    cfo = _series_last(
        cashflow,
        ["Operating Cash Flow", "Cash Flow From Continuing Operating Activities"],
    )
    if cfo is None:
        cfo = _safe_float(info.get("operatingCashflow"))

    capex = _series_last(cashflow, ["Capital Expenditure", "Capital Expenditures"])
    if capex is not None:
        capex = -abs(capex)  # normalize as outflow negative

    fcf = _safe_float(info.get("freeCashflow"))
    if fcf is None and cfo is not None and capex is not None:
        fcf = cfo + capex  # capex negative

    rev_hist = _series_history(income, ["Total Revenue", "Revenue"], n=5)
    # FCF history approximate from cashflow statements
    cfo_hist = _series_history(
        cashflow, ["Operating Cash Flow", "Cash Flow From Continuing Operating Activities"], n=5
    )
    capex_hist = _series_history(cashflow, ["Capital Expenditure", "Capital Expenditures"], n=5)
    fcf_hist: list[float] = []
    if cfo_hist and capex_hist:
        for i in range(min(len(cfo_hist), len(capex_hist))):
            fcf_hist.append(cfo_hist[i] - abs(capex_hist[i]))
    elif fcf is not None:
        fcf_hist = [fcf]

    mcap = _safe_float(info.get("marketCap"))
    shares = _safe_float(info.get("sharesOutstanding"))
    ev = _safe_float(info.get("enterpriseValue"))

    fund = Fundamentals(
        ticker=ticker.upper(),
        retrieved_at=datetime.now(timezone.utc),
        as_of_request=as_of,
        company_name=info.get("longName") or info.get("shortName"),
        sector=info.get("sector"),
        industry=info.get("industry"),
        quote_type=info.get("quoteType"),
        currency=info.get("currency") or "USD",
        market_cap=mcap,
        shares_outstanding=shares,
        enterprise_value=ev,
        revenue=rev or _safe_float(info.get("totalRevenue")),
        revenue_history=rev_hist,
        gross_profit=gp,
        operating_income=opinc,
        ebit=ebit or opinc,
        ebitda=ebitda,
        net_income=ni or _safe_float(info.get("netIncomeToCommon")),
        interest_expense=abs(interest) if interest is not None else None,
        total_debt=debt,
        cash=cash,
        current_assets=ca,
        current_liabilities=cl,
        total_assets=ta,
        equity=eq,
        receivables=ar,
        inventory=inv,
        payables=ap,
        operating_cash_flow=cfo,
        capex=capex,
        free_cash_flow=fcf,
        fcf_history=fcf_hist,
    )
    fund.mark_missing()
    return fund
