from __future__ import annotations

from datetime import date, datetime

from myers.analysis.metrics import compute_metrics
from myers.data.fundamentals import Fundamentals
from myers.strategy.scoring import assess_confidence, build_category_scores, total_score
from myers.config import load_config
from myers.valuation.engine import value_company
from myers.strategy.signals import determine_recommendation
from myers.schemas import Confidence


def _sample_fund(**overrides) -> Fundamentals:
    base = dict(
        ticker="TEST",
        retrieved_at=datetime.utcnow(),
        as_of_request=date(2024, 12, 31),
        company_name="Test Co",
        sector="Industrials",
        industry="Machinery",
        quote_type="EQUITY",
        market_cap=12_000_000_000,
        shares_outstanding=100_000_000,
        enterprise_value=13_000_000_000,
        revenue=5_000_000_000,
        revenue_history=[5_000_000_000, 4_600_000_000, 4_200_000_000, 3_900_000_000],
        gross_profit=2_000_000_000,
        operating_income=900_000_000,
        ebit=900_000_000,
        ebitda=1_200_000_000,
        net_income=700_000_000,
        interest_expense=80_000_000,
        total_debt=2_000_000_000,
        cash=1_000_000_000,
        current_assets=3_000_000_000,
        current_liabilities=1_500_000_000,
        total_assets=8_000_000_000,
        equity=4_000_000_000,
        receivables=600_000_000,
        inventory=400_000_000,
        payables=350_000_000,
        operating_cash_flow=850_000_000,
        capex=-250_000_000,
        free_cash_flow=600_000_000,
        fcf_history=[600_000_000, 500_000_000, 450_000_000],
    )
    base.update(overrides)
    f = Fundamentals(**base)
    f.mark_missing()
    return f


def test_net_debt_and_fcf():
    f = _sample_fund()
    m = compute_metrics(f)
    assert m["net_debt"] == 1_000_000_000
    assert abs(m["net_debt_to_ebitda"] - (1_000_000_000 / 1_200_000_000)) < 1e-9
    assert m["free_cash_flow"] == 600_000_000
    assert m["interest_coverage"] == 900_000_000 / 80_000_000
    assert m["fcf_margin"] == 600_000_000 / 5_000_000_000


def test_missing_not_zero_filled():
    f = _sample_fund(ebitda=None, free_cash_flow=None, operating_cash_flow=None, capex=None)
    m = compute_metrics(f)
    assert m["ebitda"] is None
    assert m["net_debt_to_ebitda"] is None
    assert m["free_cash_flow"] is None


def test_ev_ebitda_example():
    f = _sample_fund(enterprise_value=12_000_000_000, ebitda=2_000_000_000)
    m = compute_metrics(f)
    v = value_company(f, m, price=70.0, cfg=load_config().valuation)
    assert v.ev_to_ebitda == 6.0


def test_expensive_quality_is_watch_not_auto_buy():
    cfg = load_config()
    f = _sample_fund(market_cap=50_000_000_000, enterprise_value=52_000_000_000)
    m = compute_metrics(f)
    # Force rich price vs tiny DCF by using huge share count / low fcf path
    f.shares_outstanding = 10_000_000
    f.free_cash_flow = 50_000_000
    m = compute_metrics(f)
    v = value_company(f, m, price=400.0, cfg=cfg.valuation)
    cats = build_category_scores(f, m, v, cfg)
    score = total_score(cats, cfg)
    conf = assess_confidence(f, m)
    # Even with decent score, insufficient MOS => not BUY
    if v.base_margin_of_safety is not None and v.base_margin_of_safety < cfg.valuation.margin_of_safety_buy:
        rec, reasons, _ = determine_recommendation(
            score=max(score, cfg.signals.buy_min_score),
            confidence=Confidence.HIGH,
            valuation=v,
            metrics=m,
            cfg=cfg,
        )
        assert rec.value in ("WATCH", "SELL_CANDIDATE")
        assert any("margin of safety" in r.lower() or "WATCH" in r for r in reasons)


def test_live_trading_flag_default_false():
    cfg = load_config()
    assert cfg.live_trading_enabled is False
