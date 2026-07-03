"""
options_lab.py — Virtual $500-bucket experiment grid for the paper options bot.

Each bucket is an independent experiment cell with its own BUY and SELL rules.
The same signal can fire in every active bucket (different limits, stops, sizing).

    active_buckets = len(BUCKET_EXPERIMENTS) when OPTIONS_PAPER_UNLIMITED=1 (default)
                   else min(len(BUCKET_EXPERIMENTS), floor(equity / 500))

Each bucket uses a fixed $500 virtual equity (OPTIONS_VIRTUAL_BUCKET_USD).

Tracking (the hard part):
  - Every order tagged:  LB<bucket>|<strategy>|<YYYYMMDD>  (entry)
                         LX<bucket>|<strategy>|<lot_id>     (exit)
  - lab_state.json holds virtual lots with lot_id + bucket_id
  - reconcile_with_broker() syncs lots vs Alpaca positions each run
  - lab_ledger.csv is the long-term audit trail

Edit BUCKET_EXPERIMENTS below to add buy/sell/stop variants.
"""

from __future__ import annotations

import csv
import itertools
import json
import os
import re
import uuid
from dataclasses import asdict, dataclass, field, fields
from datetime import date, timedelta
from pathlib import Path
from typing import Any

# Each bucket is a fixed $500 virtual experiment cell (paper treats equity as unlimited).
VIRTUAL_BUCKET_USD = float(os.environ.get("OPTIONS_VIRTUAL_BUCKET_USD", "500"))
# When 1 (default), all defined profiles run regardless of broker equity.
PAPER_UNLIMITED_BUCKETS = os.environ.get("OPTIONS_PAPER_UNLIMITED", "1") != "0"
TARGET_BUCKET_PROFILES = int(os.environ.get("OPTIONS_BUCKET_COUNT", "100"))
STATE_VERSION = 3

REPO_ROOT = Path(__file__).resolve().parent.parent
TRIAL_ROOT = REPO_ROOT / "logs" / "options_trial"
STATE_PATH = TRIAL_ROOT / "_state" / "lab_state.json"
LEDGER_PATH = TRIAL_ROOT / "_ledger" / "master_ledger.csv"
BUCKETS_PATH = TRIAL_ROOT / "_state" / "lab_buckets.json"
STRATEGIES_PATH = TRIAL_ROOT / "_state" / "strategies.json"

# Legacy path (pre-trial folder split)
_LEGACY_STATE = REPO_ROOT / "logs" / "options" / "lab_state.json"

_LEDGER_FIELDS = [
    "ts", "event", "bucket_id", "profile", "strategy_id", "lot_id",
    "symbol", "occ", "qty", "limit", "fill_price", "cost",
    "return_pct", "pnl_usd", "reason", "buy_offset", "sell_offset",
    "take_profit", "stop_loss", "spread_frac", "detail",
]


@dataclass
class BucketProfile:
    """Execution experiment for one virtual $500 bucket."""
    bucket_id: int
    name: str
    # --- BUY ---
    buy_limit_offset: float = -0.01   # from ask (negative = below ask); 0 = at ask
    buy_at_mid: bool = False          # if True, limit = mid instead of ask+offset
    max_premium: float = 75.0
    max_spread_frac: float = 0.25
    min_open_interest: int = 100
    account_cap: float = 0.20         # max fraction of $500 in open option premium
    max_contracts: int = 1
    # --- SELL ---
    sell_limit_offset: float = -0.01  # from bid (negative = below bid)
    sell_at_mid: bool = False
    take_profit: float = 0.50
    stop_loss: float = -0.50
    eod_only: bool = False            # skip intraday stops; exit at EOD only
    market_exit_eod: bool = True      # use market order after EOD_MARKET if limit fails


# Experiment grid — generated up to TARGET_BUCKET_PROFILES variants.
def _build_bucket_experiments(target: int | None = None) -> list[BucketProfile]:
    n = target if target is not None else TARGET_BUCKET_PROFILES
    n = max(8, min(n, 200))

    core = [
        BucketProfile(0, "baseline",
                      buy_limit_offset=-0.01, sell_limit_offset=-0.01,
                      max_premium=75, account_cap=0.95,
                      take_profit=0.50, stop_loss=-0.50),
        BucketProfile(1, "patient_buy",
                      buy_limit_offset=-0.05, sell_limit_offset=-0.01,
                      max_premium=60, account_cap=0.95,
                      take_profit=0.45, stop_loss=-0.40),
        BucketProfile(2, "aggressive_buy",
                      buy_at_mid=True, sell_limit_offset=-0.02,
                      max_premium=90, account_cap=0.95,
                      take_profit=0.55, stop_loss=-0.45),
        BucketProfile(3, "tight_stops",
                      buy_limit_offset=-0.01, sell_limit_offset=-0.01,
                      max_premium=50, account_cap=0.95,
                      take_profit=0.30, stop_loss=-0.25),
        BucketProfile(4, "wide_stops",
                      buy_limit_offset=-0.02, sell_limit_offset=-0.02,
                      max_premium=80, account_cap=0.95,
                      take_profit=0.80, stop_loss=-0.60),
        BucketProfile(5, "eod_only",
                      buy_limit_offset=-0.01, sell_limit_offset=-0.01,
                      max_premium=75, account_cap=0.95,
                      eod_only=True, take_profit=0.99, stop_loss=-0.99),
        BucketProfile(6, "loose_spread",
                      buy_limit_offset=-0.01, max_spread_frac=0.35,
                      max_premium=70, account_cap=0.95,
                      take_profit=0.50, stop_loss=-0.50),
        BucketProfile(7, "tight_spread",
                      buy_limit_offset=-0.01, max_spread_frac=0.15,
                      max_premium=65, account_cap=0.95,
                      take_profit=0.40, stop_loss=-0.35),
    ]
    if n <= len(core):
        return core[:n]

    buy_offs = [-0.10, -0.08, -0.05, -0.03, -0.02, -0.01, 0.0]
    sell_offs = [-0.05, -0.03, -0.02, -0.01, 0.0]
    tps = [0.20, 0.30, 0.40, 0.50, 0.60, 0.75, 0.90]
    sls = [-0.20, -0.30, -0.40, -0.50, -0.65]
    spreads = [0.12, 0.18, 0.25, 0.32]
    profiles = list(core)
    seen = {(
        p.buy_limit_offset, p.sell_limit_offset, p.take_profit, p.stop_loss,
        p.max_spread_frac, p.buy_at_mid, p.eod_only,
    ) for p in core}

    for buy, sell, tp, sl, spread in itertools.product(
            buy_offs, sell_offs, tps, sls, spreads):
        if len(profiles) >= n:
            break
        for buy_mid, eod in ((False, False), (True, False), (False, True)):
            if len(profiles) >= n:
                break
            key = (buy, sell, tp, sl, spread, buy_mid, eod)
            if key in seen:
                continue
            seen.add(key)
            idx = len(profiles)
            tag = "mid" if buy_mid else ("eod" if eod else "lim")
            name = f"g{idx:03d}_{tag}_tp{int(tp * 100)}_sl{int(abs(sl) * 100)}"
            profiles.append(BucketProfile(
                idx, name,
                buy_limit_offset=buy,
                buy_at_mid=buy_mid,
                sell_limit_offset=sell,
                max_spread_frac=spread,
                max_premium=90,
                account_cap=0.95,
                take_profit=tp,
                stop_loss=sl,
                eod_only=eod,
            ))
    return profiles[:n]


BUCKET_EXPERIMENTS: list[BucketProfile] = _build_bucket_experiments()

# Per-strategy tweaks layered on top of bucket profile (signal-specific narrowing).
STRATEGY_TWEAKS: dict[str, dict[str, Any]] = {
    "S173": {"max_premium": 100, "account_cap": 0.25, "take_profit": 0.60, "stop_loss": -0.40},
    "S174": {},
    "S165": {"max_premium": 50, "account_cap": 0.15, "take_profit": 0.35, "stop_loss": -0.30},
    "S166": {"max_premium": 80, "take_profit": 0.70},
    "S163": {},
}


@dataclass
class EffectiveArm:
    """Merged bucket + strategy experiment for one trade."""
    bucket_id: int
    profile_name: str
    strategy_id: str
    virtual_equity: float = VIRTUAL_BUCKET_USD
    buy_limit_offset: float = -0.01
    buy_at_mid: bool = False
    max_premium: float = 75.0
    max_spread_frac: float = 0.25
    min_open_interest: int = 100
    account_cap: float = 0.20
    max_contracts: int = 1
    sell_limit_offset: float = -0.01
    sell_at_mid: bool = False
    take_profit: float = 0.50
    stop_loss: float = -0.50
    eod_only: bool = False
    market_exit_eod: bool = True

    @property
    def bucket_key(self) -> str:
        return f"b{self.bucket_id}"


@dataclass
class VirtualLot:
    lot_id: str
    bucket_id: int
    profile_name: str
    strategy_id: str
    occ_symbol: str
    underlying: str
    qty: int
    entry_cost: float = 0.0
    entry_price: float = 0.0          # per-share premium at fill
    buy_limit_offset: float = -0.01
    sell_limit_offset: float = -0.01
    sell_at_mid: bool = False
    take_profit: float = 0.50
    stop_loss: float = -0.50
    eod_only: bool = False
    market_exit_eod: bool = True
    entry_date: str = ""
    entry_order_id: str = ""


@dataclass
class PendingOrder:
    order_id: str
    bucket_id: int
    strategy_id: str
    occ_symbol: str
    underlying: str
    qty: int
    limit: float
    profile_name: str
    submitted: str = ""


@dataclass
class LabState:
    version: int = STATE_VERSION
    lots: list[VirtualLot] = field(default_factory=list)
    pending_orders: list[PendingOrder] = field(default_factory=list)
    bucket_open_premium: dict[str, float] = field(default_factory=dict)

    def open_premium_for_bucket(self, bucket_id: int) -> float:
        return float(self.bucket_open_premium.get(f"b{bucket_id}", 0.0))

    def lots_for_occ(self, occ: str) -> list[VirtualLot]:
        return [l for l in self.lots if l.occ_symbol == occ and l.qty > 0]

    def bucket_has_strategy(self, bucket_id: int, strategy_id: str) -> bool:
        return any(l.bucket_id == bucket_id and l.strategy_id == strategy_id and l.qty > 0
                   for l in self.lots)

    def bucket_holds_underlying(self, bucket_id: int, underlying: str) -> bool:
        return any(l.bucket_id == bucket_id and l.underlying == underlying and l.qty > 0
                   for l in self.lots)

    def pending_for_bucket_strategy(self, bucket_id: int, strategy_id: str) -> bool:
        return any(p.bucket_id == bucket_id and p.strategy_id == strategy_id
                   for p in self.pending_orders)


def trial_root() -> Path:
    return TRIAL_ROOT


def bucket_dir(bucket_id: int, profile_name: str) -> Path:
    slug = f"b{bucket_id}_{profile_name}"
    return TRIAL_ROOT / "buckets" / slug


def ensure_trial_layout() -> None:
    """Create options_trial tree (separate from rubber_band logs/)."""
    for sub in ("_state", "_ledger", "runs", "buckets", "simulations"):
        (TRIAL_ROOT / sub).mkdir(parents=True, exist_ok=True)
    for b in BUCKET_EXPERIMENTS:
        d = bucket_dir(b.bucket_id, b.name)
        d.mkdir(parents=True, exist_ok=True)
        profile_path = d / "profile.json"
        if not profile_path.exists():
            profile_path.write_text(
                json.dumps(asdict(b), indent=2), encoding="utf-8"
            )
        readme = d / "README.txt"
        if not readme.exists():
            readme.write_text(
                f"Bucket b{b.bucket_id} ({b.name}) — virtual ${VIRTUAL_BUCKET_USD:.0f}\n"
                f"  ledger.csv      — this bucket's trades only\n"
                f"  profile.json    — frozen experiment parameters\n"
                f"  summary.md      — auto-generated stats (options_lab_report.py)\n",
                encoding="utf-8",
            )
    if not STRATEGIES_PATH.exists():
        STRATEGIES_PATH.write_text(json.dumps({
            "paper_strategies": ["S173", "S174", "S165", "S166", "S163"],
            "strategy_tweaks": STRATEGY_TWEAKS,
        }, indent=2), encoding="utf-8")


def _merge_arm(bucket: BucketProfile, strategy_id: str,
               equity: float = VIRTUAL_BUCKET_USD) -> EffectiveArm:
    tweaks = STRATEGY_TWEAKS.get(strategy_id, {})
    vals = {f.name: getattr(bucket, f.name) for f in fields(BucketProfile)
            if f.name not in ("bucket_id", "name")}
    for k, v in tweaks.items():
        if k in vals:
            vals[k] = v
    ve = VIRTUAL_BUCKET_USD
    vals["max_premium"] = min(float(vals["max_premium"]), ve * vals["account_cap"])
    return EffectiveArm(
        bucket_id=bucket.bucket_id,
        profile_name=bucket.name,
        strategy_id=strategy_id,
        virtual_equity=ve,
        **vals,
    )


def active_bucket_count(equity: float) -> int:
    if PAPER_UNLIMITED_BUCKETS:
        return len(BUCKET_EXPERIMENTS)
    if equity <= 0:
        return 1
    funded = max(1, int(equity // VIRTUAL_BUCKET_USD))
    return min(funded, len(BUCKET_EXPERIMENTS))


def bucket_virtual_equity(equity: float = 0) -> float:
    return VIRTUAL_BUCKET_USD


def active_buckets(equity: float) -> list[BucketProfile]:
    return BUCKET_EXPERIMENTS[:active_bucket_count(equity)]


def arms_for_signal(strategy_id: str, equity: float) -> list[EffectiveArm]:
    return [_merge_arm(b, strategy_id, equity) for b in active_buckets(equity)]


def size_for_arm(arm: EffectiveArm, state: LabState, contract_cost: float) -> int:
    cap = arm.account_cap * arm.virtual_equity
    headroom = cap - state.open_premium_for_bucket(arm.bucket_id)
    if contract_cost <= 0 or headroom < contract_cost:
        return 0
    affordable = int(headroom // contract_cost)
    return max(0, min(arm.max_contracts, affordable))


def entry_limit_price(arm: EffectiveArm, bid: float, ask: float, mid: float) -> float:
    if arm.buy_at_mid:
        return round(max(0.01, mid), 2)
    return round(max(0.01, ask + arm.buy_limit_offset), 2)


def exit_limit_price(lot: VirtualLot, bid: float, ask: float, mid: float) -> float:
    if lot.sell_at_mid:
        return round(max(0.01, mid), 2)
    return round(max(0.01, bid + lot.sell_limit_offset), 2)


def make_entry_client_order_id(bucket_id: int, strategy_id: str,
                               today: date | None = None) -> str:
    d = (today or date.today()).strftime("%Y%m%d")
    return f"LB{bucket_id}|{strategy_id}|{d}"[:48]


def make_exit_client_order_id(bucket_id: int, strategy_id: str, lot_id: str) -> str:
    short = lot_id.replace("-", "")[:6]
    return f"LX{bucket_id}|{strategy_id}|{short}"[:48]


def parse_lab_client_order_id(cid: str) -> dict[str, Any] | None:
    if not cid:
        return None
    m = re.match(r"^L([BX])(\d+)\|([^|]+)\|", cid)
    if not m:
        return None
    return {
        "side": "entry" if m.group(1) == "B" else "exit",
        "bucket_id": int(m.group(2)),
        "strategy_id": m.group(3),
    }


def _rebuild_bucket_premium(state: LabState) -> None:
    prem: dict[str, float] = {}
    for lot in state.lots:
        if lot.qty <= 0:
            continue
        k = f"b{lot.bucket_id}"
        prem[k] = prem.get(k, 0.0) + lot.entry_cost
    state.bucket_open_premium = prem


def load_state() -> LabState:
    ensure_trial_layout()
    path = STATE_PATH
    if not path.exists() and _LEGACY_STATE.exists():
        path = _LEGACY_STATE
    if not path.exists():
        return LabState()
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        lots = [VirtualLot(**x) for x in raw.get("lots", [])]
        pending = [PendingOrder(**x) for x in raw.get("pending_orders", [])]
        st = LabState(
            version=raw.get("version", 1),
            lots=lots,
            pending_orders=pending,
            bucket_open_premium=raw.get("bucket_open_premium", {}),
        )
        _rebuild_bucket_premium(st)
        return st
    except Exception:
        return LabState()


def save_state(state: LabState) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    _rebuild_bucket_premium(state)
    payload = {
        "version": STATE_VERSION,
        "lots": [asdict(l) for l in state.lots if l.qty > 0],
        "pending_orders": [asdict(p) for p in state.pending_orders],
        "bucket_open_premium": state.bucket_open_premium,
        "updated": date.today().isoformat(),
    }
    STATE_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    _write_buckets_snapshot(state)


def _write_buckets_snapshot(state: LabState) -> None:
    """Human-readable bucket summary for monitoring."""
    rows = []
    for b in BUCKET_EXPERIMENTS:
        rows.append({
            "bucket_id": b.bucket_id,
            "profile": b.name,
            "open_premium": round(state.open_premium_for_bucket(b.bucket_id), 2),
            "open_lots": sum(1 for l in state.lots if l.bucket_id == b.bucket_id and l.qty > 0),
        })
    BUCKETS_PATH.parent.mkdir(parents=True, exist_ok=True)
    BUCKETS_PATH.write_text(json.dumps(rows, indent=2), encoding="utf-8")


def new_lot_id() -> str:
    return uuid.uuid4().hex[:12]


def register_pending(state: LabState, arm: EffectiveArm, occ: str, underlying: str,
                     qty: int, limit: float, order_id: str) -> None:
    state.pending_orders.append(PendingOrder(
        order_id=str(order_id),
        bucket_id=arm.bucket_id,
        strategy_id=arm.strategy_id,
        occ_symbol=occ,
        underlying=underlying,
        qty=qty,
        limit=limit,
        profile_name=arm.profile_name,
        submitted=date.today().isoformat(),
    ))
    save_state(state)


def confirm_fill(state: LabState, arm: EffectiveArm, occ: str, underlying: str,
                 qty: int, entry_cost: float, entry_price: float,
                 order_id: str = "") -> VirtualLot:
    """Move pending order to confirmed virtual lot."""
    state.pending_orders = [
        p for p in state.pending_orders
        if not (p.order_id == order_id or (
            p.bucket_id == arm.bucket_id and p.strategy_id == arm.strategy_id
            and p.occ_symbol == occ and p.qty == qty
        ))
    ]
    lot = VirtualLot(
        lot_id=new_lot_id(),
        bucket_id=arm.bucket_id,
        profile_name=arm.profile_name,
        strategy_id=arm.strategy_id,
        occ_symbol=occ,
        underlying=underlying,
        qty=qty,
        entry_cost=entry_cost,
        entry_price=entry_price,
        buy_limit_offset=arm.buy_limit_offset,
        sell_limit_offset=arm.sell_limit_offset,
        sell_at_mid=arm.sell_at_mid,
        take_profit=arm.take_profit,
        stop_loss=arm.stop_loss,
        eod_only=arm.eod_only,
        market_exit_eod=arm.market_exit_eod,
        entry_date=date.today().isoformat(),
        entry_order_id=order_id,
    )
    state.lots.append(lot)
    save_state(state)
    return lot


def register_entry_immediate(state: LabState, arm: EffectiveArm, occ: str,
                             underlying: str, qty: int, entry_cost: float,
                             entry_price: float, order_id: str = "") -> VirtualLot:
    """Optimistic entry on submit (reconcile will fix if unfilled)."""
    return confirm_fill(state, arm, occ, underlying, qty, entry_cost, entry_price, order_id)


def register_exit(state: LabState, lot: VirtualLot, qty: int) -> None:
    if lot.qty <= qty:
        lot.qty = 0
    else:
        freed_frac = qty / (lot.qty + qty) if lot.qty else 1.0
        lot.entry_cost *= (1 - freed_frac)
        lot.qty -= qty
    state.lots = [l for l in state.lots if l.qty > 0]
    save_state(state)


def exit_reason_for_lot(lot: VirtualLot, plpc: float, eod: bool) -> str | None:
    if eod:
        return "EOD"
    if lot.eod_only:
        return None
    if plpc >= lot.take_profit:
        return f"take_profit ({plpc * 100:+.1f}%)"
    if plpc <= lot.stop_loss:
        return f"stop_loss ({plpc * 100:+.1f}%)"
    return None


def append_ledger(row: dict) -> None:
    ensure_trial_layout()
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    hdr = not LEDGER_PATH.exists()
    out = {k: row.get(k, "") for k in _LEDGER_FIELDS}
    with open(LEDGER_PATH, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=_LEDGER_FIELDS, extrasaction="ignore")
        if hdr:
            w.writeheader()
        w.writerow(out)
    bid = row.get("bucket_id", "")
    profile = row.get("profile", "")
    if bid != "" and profile:
        bpath = bucket_dir(int(bid), str(profile)) / "ledger.csv"
        bpath.parent.mkdir(parents=True, exist_ok=True)
        hdr_b = not bpath.exists()
        with open(bpath, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=_LEDGER_FIELDS, extrasaction="ignore")
            if hdr_b:
                w.writeheader()
            w.writerow(out)


def _read_ledger_rows() -> list[dict]:
    if not LEDGER_PATH.exists():
        return []
    with open(LEDGER_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _ledger_realized_pnl(rows: list[dict]) -> tuple[float, float, dict[str, float]]:
    """Return (all_time_usd, today_usd, per_bucket_key_usd) from closed trades."""
    today = date.today().isoformat()
    lots: dict[str, dict] = {}
    realized_all = 0.0
    realized_today = 0.0
    by_bucket: dict[str, float] = {}

    for r in rows:
        ev = r.get("event")
        lot_id = r.get("lot_id") or ""
        if ev == "entry" and lot_id:
            try:
                lots[lot_id] = {
                    "cost": float(r.get("cost") or 0),
                    "qty": max(1, int(float(r.get("qty") or 1))),
                    "bucket_id": r.get("bucket_id", ""),
                    "profile": r.get("profile", ""),
                }
            except (TypeError, ValueError):
                pass
            continue
        if ev != "exit" or not lot_id:
            continue

        pnl: float | None = None
        if r.get("pnl_usd"):
            try:
                pnl = float(r["pnl_usd"])
            except (TypeError, ValueError):
                pnl = None
        if pnl is None:
            lot = lots.get(lot_id)
            if lot and r.get("return_pct"):
                try:
                    exit_qty = max(1, int(float(r.get("qty") or lot["qty"])))
                    entry_qty = lot["qty"] or exit_qty
                    cost_sold = lot["cost"] * (exit_qty / entry_qty)
                    pnl = cost_sold * float(r["return_pct"]) / 100.0
                    if exit_qty >= entry_qty:
                        lots.pop(lot_id, None)
                    else:
                        lot["cost"] -= cost_sold
                        lot["qty"] -= exit_qty
                except (TypeError, ValueError, ZeroDivisionError):
                    pnl = None

        if pnl is None:
            continue
        realized_all += pnl
        if str(r.get("ts", "")).startswith(today) or str(r.get("date", "")) == today:
            realized_today += pnl
        key = f"b{r.get('bucket_id', '?')}|{r.get('profile', '?')}"
        by_bucket[key] = by_bucket.get(key, 0.0) + pnl

    return realized_all, realized_today, by_bucket


def _open_pnl_stats(
    state: LabState,
    positions: list[dict] | None,
) -> tuple[float, float, float, dict[str, float]]:
    """
    Return (virtual_open_pnl_usd, premium_deployed_usd, broker_open_pnl_usd,
            per_bucket_open_usd).
    Virtual open P&L attributes broker unrealized P&L to lots by entry_cost share.
    """
    by_bucket: dict[str, float] = {}
    premium = 0.0
    virtual_open = 0.0

    if not positions:
        for lot in state.lots:
            if lot.qty <= 0:
                continue
            premium += lot.entry_cost
        return virtual_open, premium, 0.0, by_bucket

    occ_map = {p.get("symbol", ""): p for p in positions}
    broker_open = sum(float(p.get("unrealized_pl", 0) or 0) for p in positions)

    for lot in state.lots:
        if lot.qty <= 0:
            continue
        premium += lot.entry_cost
        pos = occ_map.get(lot.occ_symbol)
        if pos:
            lot_pnl = float(pos.get("unrealized_pl", 0) or 0)
            pos_cost = abs(float(pos.get("cost_basis", 0) or 0))
            if pos_cost > 0 and lot.entry_cost < pos_cost:
                lot_pnl *= lot.entry_cost / pos_cost
            elif pos.get("plpc") is not None:
                lot_pnl = lot.entry_cost * float(pos["plpc"])
        else:
            lot_pnl = 0.0
        virtual_open += lot_pnl
        key = f"b{lot.bucket_id}|{lot.profile_name}"
        by_bucket[key] = by_bucket.get(key, 0.0) + lot_pnl

    return virtual_open, premium, broker_open, by_bucket


def max_active_buckets(equity: float) -> int:
    if PAPER_UNLIMITED_BUCKETS:
        return len(BUCKET_EXPERIMENTS)
    if equity <= 0:
        return 1
    return max(1, int(equity // VIRTUAL_BUCKET_USD))


def format_trial_stats(
    state: LabState,
    equity: float | None = None,
    positions: list[dict] | None = None,
) -> list[str]:
    """Human-readable stats block for terminal + run log."""
    today = date.today().isoformat()
    lines: list[str] = []
    lines.append("=" * 56)
    lines.append("OPTIONS TRIAL STATS")
    lines.append("=" * 56)

    if equity is not None:
        nb = active_bucket_count(equity)
        fundable = max_active_buckets(equity)
        lines.append(f"Account equity: ${equity:,.2f}")
        lines.append(
            f"Active buckets: {nb} of {len(BUCKET_EXPERIMENTS)} profiles "
            f"(${VIRTUAL_BUCKET_USD:,.0f} virtual each)"
            + (" — paper unlimited mode" if PAPER_UNLIMITED_BUCKETS else "")
        )
        if not PAPER_UNLIMITED_BUCKETS and fundable < len(BUCKET_EXPERIMENTS):
            lines.append(
                f"  Note: equity funds {fundable} x ${VIRTUAL_BUCKET_USD:.0f} buckets; "
                f"set OPTIONS_PAPER_UNLIMITED=1 to run all profiles."
            )
    else:
        nb = len(BUCKET_EXPERIMENTS)
        lines.append("Account equity: (not connected)")

    rows = _read_ledger_rows()
    realized_all, realized_today, realized_by_bucket = _ledger_realized_pnl(rows)
    open_virtual, open_premium, broker_open, open_by_bucket = _open_pnl_stats(
        state, positions)

    lines.append("")
    lines.append("P&L summary")
    lines.append(f"  Realized (sold):     ${realized_all:+,.2f} all-time"
                 f"  |  ${realized_today:+,.2f} today")
    if positions is not None:
        lines.append(
            f"  Open (not sold yet): ${open_virtual:+,.2f} unrealized (virtual lots)"
        )
        if broker_open and abs(broker_open - open_virtual) > 0.01:
            lines.append(
                f"                       ${broker_open:+,.2f} unrealized (broker total)"
            )
    else:
        lines.append("  Open (not sold yet): (connect broker for live unrealized P&L)")
    lines.append(f"  Premium deployed:    ${open_premium:,.2f} in open positions")
    lines.append(
        f"  Combined P&L:        ${realized_all + open_virtual:+,.2f} "
        f"(realized + open virtual)"
    )

    today_rows = [r for r in rows if str(r.get("ts", "")).startswith(today)
                  or str(r.get("date", "")) == today]
    entries_today = sum(1 for r in today_rows if r.get("event") == "entry")
    exits_today = sum(1 for r in today_rows if r.get("event") == "exit")
    all_exits = [r for r in rows if r.get("event") == "exit" and r.get("return_pct")]
    rets = []
    for r in all_exits:
        try:
            rets.append(float(r["return_pct"]))
        except Exception:
            pass

    lines.append("")
    lines.append("Ledger (master)")
    lines.append(f"  Total events:     {len(rows)}")
    lines.append(f"  Today entries:    {entries_today}")
    lines.append(f"  Today exits:      {exits_today}")
    if rets:
        wins = sum(1 for x in rets if x > 0)
        lines.append(f"  All-time exits:   {len(rets)}  wins {wins/len(rets):.0%}")
        lines.append(f"  Avg return/trade: {sum(rets)/len(rets):+.1f}%  "
                     f"median {sorted(rets)[len(rets)//2]:+.1f}%")
    else:
        lines.append("  All-time exits:   0 (no completed trades yet)")

    lines.append("")
    lines.append("Open virtual lots (by bucket)")
    any_lot = False
    active_profiles = BUCKET_EXPERIMENTS[:nb if equity else len(BUCKET_EXPERIMENTS)]
    shown = 0
    quiet = 0
    for b in active_profiles:
        blots = [l for l in state.lots if l.bucket_id == b.bucket_id and l.qty > 0]
        prem = state.open_premium_for_bucket(b.bucket_id)
        bkey = f"b{b.bucket_id}|{b.name}"
        rpnl = realized_by_bucket.get(bkey, 0.0)
        opnl = open_by_bucket.get(bkey, 0.0)
        has_activity = bool(blots or prem > 0 or rpnl or opnl)
        if has_activity:
            any_lot = True
        if not has_activity:
            quiet += 1
            continue
        if shown >= 20:
            continue
        shown += 1
        lot_detail = ", ".join(
            f"{l.strategy_id}:{l.underlying}x{l.qty}" for l in blots[:4]
        )
        if len(blots) > 4:
            lot_detail += f" +{len(blots)-4} more"
        lines.append(
            f"  b{b.bucket_id} {b.name:22s}  prem=${prem:6.0f}  "
            f"real=${rpnl:+6.2f}  open=${opnl:+6.2f}  "
            f"lots={len(blots)}  [{lot_detail or '-'}]"
        )
        lines.append(
            f"       buy: {'mid' if b.buy_at_mid else f'ask{b.buy_limit_offset:+.2f}'}  "
            f"sell: bid{b.sell_limit_offset:+.2f}  "
            f"tp={b.take_profit:+.0%} sl={b.stop_loss:+.0%}"
        )
    if quiet and shown < len(active_profiles):
        lines.append(f"  ({quiet} quiet bucket profiles omitted — no trades yet)")
    if not any_lot:
        lines.append("  (no open lots across active profiles)")

    if state.pending_orders:
        lines.append("")
        lines.append(f"Pending orders: {len(state.pending_orders)}")
        for p in state.pending_orders[:5]:
            lines.append(
                f"  b{p.bucket_id} {p.strategy_id} {p.underlying} "
                f"limit={p.limit:.2f}"
            )

    if positions is not None:
        lines.append("")
        lines.append("Alpaca option positions")
        if positions:
            for pos in positions:
                sym = pos.get("symbol", "?")
                qty = pos.get("qty", 0)
                plpc = pos.get("plpc", 0.0)
                upl = float(pos.get("unrealized_pl", 0) or 0)
                cost = float(pos.get("cost_basis", 0) or 0)
                lines.append(
                    f"  {sym}  qty={qty}  cost=${cost:,.2f}  "
                    f"return={plpc*100:+.1f}%  open P&L=${upl:+,.2f}"
                )
        else:
            lines.append("  (none)")

    if rows:
        lines.append("")
        lines.append("Per-bucket exit stats (all time)")
        by_bucket: dict[str, list[float]] = {}
        for r in all_exits:
            try:
                key = f"b{r.get('bucket_id','?')}|{r.get('profile','?')}"
                by_bucket.setdefault(key, []).append(float(r["return_pct"]))
            except Exception:
                pass
        for key in sorted(by_bucket):
            vals = by_bucket[key]
            r_usd = realized_by_bucket.get(key, 0.0)
            lines.append(
                f"  {key:22s}  n={len(vals):3d}  "
                f"avg={sum(vals)/len(vals):+.1f}%  "
                f"med={sorted(vals)[len(vals)//2]:+.1f}%  "
                f"realized=${r_usd:+,.2f}"
            )

    lines.append("=" * 56)
    return lines


def print_trial_stats(
    state: LabState,
    equity: float | None = None,
    positions: list[dict] | None = None,
    log_fn=None,
) -> None:
    for line in format_trial_stats(state, equity, positions):
        if log_fn:
            log_fn(line)
        print(line, flush=True)


def reconcile_with_broker(trade, state: LabState, log_fn=print) -> LabState:
    """
    Sync virtual lots with Alpaca positions and recent LAB-tagged fills.
    Fixes drift from unfilled orders, partial fills, or manual closes.
    """
    from alpaca.trading.requests import GetOrdersRequest
    from alpaca.trading.enums import QueryOrderStatus

    occ_re = re.compile(r"^[A-Z]+\d{6}[CP]\d{8}$")

    def _is_opt(sym: str) -> bool:
        return bool(occ_re.match(sym or ""))

    try:
        equity = float(trade.get_account().equity)
    except Exception:
        equity = VIRTUAL_BUCKET_USD

    # --- current option positions ---
    pos_by_occ: dict[str, Any] = {}
    try:
        for p in trade.get_all_positions():
            sym = getattr(p, "symbol", "")
            ac = str(getattr(p, "asset_class", "") or "")
            if "option" in ac.lower() or _is_opt(sym):
                pos_by_occ[sym] = p
    except Exception as exc:
        log_fn(f"  reconcile: position read failed: {exc}")
        return state

    # --- drop lots for closed positions ---
    alive_occs = set(pos_by_occ)
    before = len(state.lots)
    state.lots = [l for l in state.lots if l.occ_symbol in alive_occs and l.qty > 0]
    if len(state.lots) < before:
        log_fn(f"  reconcile: removed {before - len(state.lots)} stale lot(s)")

    # --- qty alignment per OCC ---
    for occ, pos in pos_by_occ.items():
        try:
            pos_qty = int(float(getattr(pos, "qty", 0)))
        except Exception:
            continue
        if pos_qty <= 0:
            continue
        lots = state.lots_for_occ(occ)
        lot_qty = sum(l.qty for l in lots)
        if lot_qty == pos_qty:
            continue
        if lot_qty > pos_qty:
            trim = lot_qty - pos_qty
            for lot in sorted(lots, key=lambda x: x.entry_date):
                if trim <= 0:
                    break
                cut = min(lot.qty, trim)
                lot.qty -= cut
                trim -= cut
            state.lots = [l for l in state.lots if l.qty > 0]
            log_fn(f"  reconcile: trimmed {occ} lots to match pos qty {pos_qty}")
        elif lot_qty < pos_qty:
            orphan = pos_qty - lot_qty
            m = re.match(r"^([A-Z]+)", occ)
            und = m.group(1) if m else occ[:4]
            cost = abs(float(getattr(pos, "cost_basis", 0) or 0))
            per = cost / pos_qty if pos_qty else 0
            state.lots.append(VirtualLot(
                lot_id=new_lot_id(),
                bucket_id=0,
                profile_name="orphan_reconcile",
                strategy_id="UNKNOWN",
                occ_symbol=occ,
                underlying=und,
                qty=orphan,
                entry_cost=per * orphan,
                entry_price=per / 100 if per else 0,
                entry_date=date.today().isoformat(),
            ))
            log_fn(f"  reconcile: added orphan lot {occ} qty={orphan} (bucket 0)")

    # --- process recent filled LAB orders -> confirm pending ---
    try:
        req = GetOrdersRequest(status=QueryOrderStatus.CLOSED, limit=200)
        orders = trade.get_orders(req)
    except Exception:
        orders = []

    for o in orders or []:
        cid = getattr(o, "client_order_id", "") or ""
        parsed = parse_lab_client_order_id(cid)
        if not parsed or parsed["side"] != "entry":
            continue
        status = str(getattr(o, "status", "") or "").lower()
        if status not in ("filled", "partially_filled"):
            continue
        filled_qty = int(float(getattr(o, "filled_qty", 0) or 0))
        if filled_qty <= 0:
            continue
        occ = getattr(o, "symbol", "")
        if not _is_opt(occ):
            continue
        if any(l.entry_order_id == str(o.id) for l in state.lots):
            continue
        bucket_id = parsed["bucket_id"]
        strat = parsed["strategy_id"]
        bucket = next((b for b in BUCKET_EXPERIMENTS if b.bucket_id == bucket_id), None)
        if not bucket:
            continue
        arm = _merge_arm(bucket, strat, equity)
        try:
            fill_px = float(getattr(o, "filled_avg_price", 0) or 0)
        except Exception:
            fill_px = 0.0
        entry_cost = fill_px * 100 * filled_qty
        m = re.match(r"^([A-Z]+)", occ)
        und = m.group(1) if m else occ[:4]
        confirm_fill(state, arm, occ, und, filled_qty, entry_cost, fill_px, str(o.id))
        state.pending_orders = [p for p in state.pending_orders if p.order_id != str(o.id)]

    # --- clear old pending (unfilled > 1 day) ---
    cutoff = (date.today() - timedelta(days=1)).isoformat()
    stale = [p for p in state.pending_orders if p.submitted < cutoff]
    if stale:
        state.pending_orders = [p for p in state.pending_orders if p.submitted >= cutoff]
        log_fn(f"  reconcile: cleared {len(stale)} stale pending order(s)")

    _rebuild_bucket_premium(state)
    save_state(state)
    return state
