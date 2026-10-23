from __future__ import annotations

from datetime import date, datetime, timezone

from myers.analysis.metrics import compute_metrics
from myers.config import load_config
from myers.data.fundamentals import Fundamentals
from myers.valuation.engine import reverse_dcf_implied_growth, value_company


def _fund() -> Fundamentals:
    f = Fundamentals(
        ticker="TEST",
        retrieved_at=datetime.now(timezone.utc),
        as_of_request=date(2024, 12, 31),
        market_cap=10_000_000_000,
        shares_outstanding=100_000_000,
        enterprise_value=11_000_000_000,
        revenue=4_000_000_000,
        revenue_history=[4e9, 3.7e9, 3.4e9],
        operating_income=800_000_000,
        ebit=800_000_000,
        ebitda=1_000_000_000,
        net_income=600_000_000,
        interest_expense=50_000_000,
        total_debt=2_000_000_000,
        cash=1_000_000_000,
        operating_cash_flow=700_000_000,
        capex=-200_000_000,
        free_cash_flow=500_000_000,
        fcf_history=[500_000_000, 450_000_000, 400_000_000],
    )
    f.mark_missing()
    return f


def test_reverse_dcf_returns_growth_and_note():
    f = _fund()
    g, note = reverse_dcf_implied_growth(
        f,
        price=80.0,
        margin=0.12,
        wacc=0.09,
        terminal_growth=0.025,
        years=5,
    )
    assert g is not None
    assert "expectations" in note.lower() or "evidence" in note.lower()


def test_value_company_includes_reverse_dcf_fields():
    f = _fund()
    m = compute_metrics(f)
    v = value_company(f, m, price=90.0, cfg=load_config().valuation)
    assert v.reverse_dcf_interpretation is not None
