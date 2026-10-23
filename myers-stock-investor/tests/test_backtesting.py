from __future__ import annotations

from datetime import date
from pathlib import Path

from myers.backtesting.performance import cagr, max_drawdown, summarize_equity
from myers.config import load_config
import pandas as pd


def test_performance_helpers():
    idx = pd.date_range("2020-01-01", periods=5, freq="D")
    eq = pd.Series([100, 110, 105, 120, 115], index=idx, dtype=float)
    assert max_drawdown(eq) < 0
    s = summarize_equity(eq)
    assert "cagr" in s
    assert s["terminal"] == 115


def test_config_backtest_defaults():
    cfg = load_config()
    assert cfg.backtest.benchmark == "SPY"
    assert cfg.portfolio.max_position_weight == 0.05
    assert cfg.live_trading_enabled is False
