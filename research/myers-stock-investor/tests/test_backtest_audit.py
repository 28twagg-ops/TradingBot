from __future__ import annotations

from datetime import date

import pandas as pd

from myers.backtesting.performance import (
    max_drawdown,
    spy_total_return_audit,
    summarize_equity,
)
from myers.portfolio.paper import PaperPortfolio
from myers.config import load_config
from myers.schemas import CompanyAnalysis, Confidence, Recommendation, ValuationResult


def test_spy_audit_uses_full_window_not_quarter_start():
    """Synthetic SPY: crash then recovery — full-window return != trough-to-peak."""
    idx = pd.date_range("2020-01-02", periods=10, freq="B")
    # Start 100, crash to 70, end 110
    px = pd.Series([100, 95, 80, 70, 75, 85, 95, 100, 105, 110], index=idx, dtype=float)
    full = spy_total_return_audit(px, idx[0], idx[-1], 100_000)
    assert abs(full["cumulative_return"] - 0.10) < 1e-9  # 100 -> 110

    # Wrong method (old bug): start metrics at crash trough day 3
    trough = px.iloc[3:]
    wrong = summarize_equity(trough / trough.iloc[0] * 100_000)
    assert wrong["cumulative_return"] > 0.40  # 70 -> 110
    assert full["cumulative_return"] < wrong["cumulative_return"]


def test_daily_drawdown_captures_intra_quarter_crash():
    idx = pd.date_range("2020-01-01", periods=5, freq="D")
    # Flat quarters would miss this; daily series must show ~-50% DD
    eq = pd.Series([100, 120, 60, 80, 90], index=idx, dtype=float)
    assert abs(max_drawdown(eq) - (60 / 120 - 1)) < 1e-9


def test_cash_accounting_buy_reduces_cash():
    cfg = load_config()
    port = PaperPortfolio.create(cfg)
    start_cash = port.cash
    port.buy("TEST", price=50.0, weight=0.05, as_of=date(2020, 3, 31), sector="Tech", cfg=cfg)
    assert port.cash < start_cash
    assert "TEST" in port.positions
    assert len(port.trades) == 1
    assert port.trades[0]["simulated"] is True


def test_can_buy_blocks_non_candidate():
    cfg = load_config()
    port = PaperPortfolio.create(cfg)
    a = CompanyAnalysis(
        ticker="X",
        analysis_date=date(2020, 1, 1),
        fundamental_score=90,
        data_confidence=Confidence.HIGH,
        valuation=ValuationResult(base_margin_of_safety=0.4),
        recommendation=Recommendation.WATCH,
    )
    assert port.can_buy(a, cfg, {"X": 10.0}) == "not_buy_candidate"
    assert (
        port.can_buy(a, cfg, {"X": 10.0}, require_buy_candidate=False) is None
        or port.can_buy(a, cfg, {"X": 10.0}, require_buy_candidate=False) != "not_buy_candidate"
    )


def test_summarize_equity_start_end_consistent():
    idx = pd.date_range("2020-01-01", periods=3, freq="D")
    eq = pd.Series([100_000.0, 110_000.0, 194_585.0], index=idx)
    m = summarize_equity(eq)
    assert abs(m["cumulative_return"] - (194_585 / 100_000 - 1)) < 1e-9
    assert abs(m["start_value"] - 100_000) < 1e-9
    assert abs(m["end_value"] - 194_585) < 1e-9
