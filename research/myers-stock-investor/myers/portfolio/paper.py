from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from myers.config import StrategyConfig
from myers.schemas import CompanyAnalysis, Recommendation


@dataclass
class Position:
    ticker: str
    shares: float
    avg_cost: float
    sector: str | None = None
    opened: str = ""


@dataclass
class PaperPortfolio:
    cash: float
    positions: dict[str, Position] = field(default_factory=dict)
    trades: list[dict] = field(default_factory=list)

    @classmethod
    def create(cls, cfg: StrategyConfig) -> "PaperPortfolio":
        return cls(cash=cfg.backtest.initial_cash)

    def equity(self, prices: dict[str, float]) -> float:
        total = self.cash
        for t, p in self.positions.items():
            total += p.shares * prices.get(t, p.avg_cost)
        return total

    def sector_weights(self, prices: dict[str, float]) -> dict[str, float]:
        eq = self.equity(prices)
        if eq <= 0:
            return {}
        out: dict[str, float] = {}
        for t, p in self.positions.items():
            sec = p.sector or "Unknown"
            out[sec] = out.get(sec, 0.0) + p.shares * prices.get(t, p.avg_cost) / eq
        return out

    def can_buy(
        self,
        analysis: CompanyAnalysis,
        cfg: StrategyConfig,
        prices: dict[str, float],
        *,
        require_buy_candidate: bool = True,
        max_positions_override: int | None = None,
    ) -> str | None:
        if require_buy_candidate and analysis.recommendation != Recommendation.BUY_CANDIDATE:
            return "not_buy_candidate"
        if analysis.ticker in self.positions:
            return "already_held"
        max_pos = max_positions_override or cfg.portfolio.max_positions
        if len(self.positions) >= max_pos:
            return "max_positions"
        eq = self.equity(prices)
        target = eq * cfg.portfolio.max_position_weight
        if self.cash < target * 0.5:
            return "insufficient_cash"
        sec = analysis.sector or "Unknown"
        sw = self.sector_weights(prices)
        if sw.get(sec, 0.0) >= cfg.portfolio.max_sector_weight:
            return "max_sector_weight"
        return None

    def buy(
        self,
        ticker: str,
        price: float,
        weight: float,
        as_of: date,
        sector: str | None,
        cfg: StrategyConfig,
    ) -> dict | None:
        eq = self.equity({ticker: price, **{k: v.avg_cost for k, v in self.positions.items()}})
        notional = min(self.cash, eq * min(weight, cfg.portfolio.max_position_weight))
        if notional <= 0 or price <= 0:
            return None
        cost = notional * (1 + (cfg.backtest.commission_bps + cfg.backtest.slippage_bps) / 10000)
        if cost > self.cash:
            notional = self.cash / (1 + (cfg.backtest.commission_bps + cfg.backtest.slippage_bps) / 10000)
            cost = self.cash
        shares = notional / price
        self.cash -= cost
        self.positions[ticker] = Position(
            ticker=ticker,
            shares=shares,
            avg_cost=price,
            sector=sector,
            opened=as_of.isoformat(),
        )
        trade = {
            "date": as_of.isoformat(),
            "side": "BUY",
            "ticker": ticker,
            "shares": shares,
            "price": price,
            "cost": cost,
            "simulated": True,
        }
        self.trades.append(trade)
        return trade

    def sell_all(self, ticker: str, price: float, as_of: date, cfg: StrategyConfig) -> dict | None:
        pos = self.positions.pop(ticker, None)
        if pos is None or price <= 0:
            return None
        proceeds = pos.shares * price
        proceeds *= 1 - (cfg.backtest.commission_bps + cfg.backtest.slippage_bps) / 10000
        self.cash += proceeds
        trade = {
            "date": as_of.isoformat(),
            "side": "SELL",
            "ticker": ticker,
            "shares": pos.shares,
            "price": price,
            "proceeds": proceeds,
            "simulated": True,
        }
        self.trades.append(trade)
        return trade

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "cash": self.cash,
            "positions": {k: v.__dict__ for k, v in self.positions.items()},
            "trades": self.trades,
        }
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
