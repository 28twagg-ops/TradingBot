from __future__ import annotations

from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONFIG = ROOT / "config" / "strategy.yaml"


class UniverseConfig(BaseModel):
    min_market_cap: float = 1_000_000_000
    min_avg_dollar_volume: float = 10_000_000
    min_years_financials: int = 3
    exclude_sectors: list[str] = Field(default_factory=list)
    exclude_quote_types: list[str] = Field(default_factory=list)


class ScreeningConfig(BaseModel):
    max_net_debt_to_ebitda: float = 3.0
    min_interest_coverage: float = 3.0
    min_fcf_years_positive: int = 2


class ScoringWeights(BaseModel):
    cash_quality: float = 0.25
    balance_sheet: float = 0.20
    business_quality: float = 0.25
    valuation: float = 0.20
    management_concentration: float = 0.10


class ValuationConfig(BaseModel):
    margin_of_safety_buy: float = 0.25
    wacc_default: float = 0.09
    terminal_growth: float = 0.025
    projection_years: int = 5


class SignalsConfig(BaseModel):
    buy_min_score: float = 70
    buy_min_confidence: str = "MEDIUM"
    watch_min_score: float = 55


class PortfolioConfig(BaseModel):
    max_positions: int = 25
    max_position_weight: float = 0.05
    max_sector_weight: float = 0.25
    allocation: str = "equal_weight"
    rebalance: str = "quarterly"


class BacktestConfig(BaseModel):
    initial_cash: float = 100_000
    commission_bps: float = 5
    slippage_bps: float = 5
    decision_frequency: str = "quarterly"
    benchmark: str = "SPY"
    cash_annual_rate: float = 0.0
    research_mode: Literal["exploratory", "validated"] = "exploratory"


class StrategyConfig(BaseModel):
    model_version: str = "1.1.0"
    universe: UniverseConfig = Field(default_factory=UniverseConfig)
    screening: ScreeningConfig = Field(default_factory=ScreeningConfig)
    scoring_weights: ScoringWeights = Field(default_factory=ScoringWeights)
    valuation: ValuationConfig = Field(default_factory=ValuationConfig)
    signals: SignalsConfig = Field(default_factory=SignalsConfig)
    portfolio: PortfolioConfig = Field(default_factory=PortfolioConfig)
    backtest: BacktestConfig = Field(default_factory=BacktestConfig)
    live_trading_enabled: bool = False


def load_config(path: Path | None = None) -> StrategyConfig:
    p = path or DEFAULT_CONFIG
    raw: dict[str, Any] = {}
    if p.exists():
        raw = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    return StrategyConfig.model_validate(raw)
