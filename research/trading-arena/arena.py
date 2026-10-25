#!/usr/bin/env python3
"""Isolation-first virtual paper accounts; no network, broker, or credential access.

Every buy/sell is a ledger event with sequence, previous hash, current hash.
The hash chain catches accidental/local modifications, not malicious wholesale
rewriting by the party holding the signing keys (no external signing yet).
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
ASSETS = set(CONFIG["allowed_asset_classes"])


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()


def finite(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("expected finite numeric value")
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("not finite")
    return value


class PaperAccount:
    """No shorts, no cross-worker cash transfer, no margin or live orders."""

    def __init__(self, worker_id, initial_usd=100.0):
        if worker_id not in {w["id"] for w in CONFIG["workers"]}:
            raise ValueError("unknown worker")
        if initial_usd != CONFIG["initial_usd"]:
            raise ValueError("all workers must start with the configured capital")
        self.worker_id = worker_id
        self.initial_usd = float(initial_usd)
        self.cash = self.initial_usd
        self.holdings = {}
        self.events = []
        self._previous_hash = "GENESIS"

    def trade(self, *, timestamp, asset_class, symbol, side, qty, price,
              fee=0.0, source_id=""):
        if asset_class not in ASSETS or side not in ("BUY", "SELL"):
            raise ValueError("unsupported asset class or side")
        if asset_class == "crypto" and symbol not in CONFIG["allowed_crypto_symbols"]:
            raise ValueError("unsupported crypto pair")
        if not isinstance(timestamp, str) or not timestamp.endswith("Z"):
            raise ValueError("timestamp must be UTC ISO string ending Z")
        if not isinstance(symbol, str) or not symbol or len(symbol) > 90:
            raise ValueError("invalid symbol")
        if not isinstance(source_id, str) or not source_id.strip():
            raise ValueError("each paper execution needs a market observation identifier")
        qty, price, fee = finite(qty), finite(price), finite(fee)
        if qty <= 0 or price <= 0 or fee < 0:
            raise ValueError("invalid size, price or fee")
        if asset_class == "us_option_long" and qty != int(qty):
            raise ValueError("options require whole contracts")
        if asset_class == "us_equity" and not symbol.isalnum():
            raise ValueError("equity symbols must be simple alphanumerics for this prototype")
        mult = 100 if asset_class == "us_option_long" else 1
        k = asset_class + ":" + symbol
        notional = round(qty * price * mult, 8)
        total = round(notional + fee, 8)
        if side == "BUY":
            if total > self.cash + 1e-9:
                raise ValueError("insufficient virtual cash")
            self.cash = round(self.cash - total, 8)
            self.holdings[k] = round(self.holdings.get(k, 0) + qty, 8)
        else:
            owned = self.holdings.get(k, 0.0)
            if qty > owned + 1e-9:
                raise ValueError("cannot sell more than position")
            next_cash = round(self.cash + notional - fee, 8)
            if next_cash < -1e-8:
                raise ValueError("negative cash after fees")
            self.cash = next_cash
            self.holdings[k] = round(owned - qty, 8)
        event = {"worker": self.worker_id, "seq": len(self.events) + 1,
                 "timestamp": timestamp, "asset_class": asset_class, "symbol": symbol,
                 "side": side, "qty": qty, "price": price, "fee": fee,
                 "multiplier": mult, "source_id": source_id,
                 "balance_after": self.cash, "positions_after": dict(self.holdings),
                 "previous_hash": self._previous_hash}
        event["hash"] = digest(event)
        self.events.append(event)
        self._previous_hash = event["hash"]
        return event

    def statement(self):
        return {"worker": self.worker_id, "initial_usd": self.initial_usd,
                "cash_usd": self.cash, "positions": dict(self.holdings),
                "events": list(self.events)}


def audit_account(statement):
    """Judge 1: independently replay ledger, verify hashes and cash/positions."""
    failures = []
    initial = statement.get("initial_usd")
    wid = statement.get("worker")
    try:
        account = PaperAccount(wid, initial)
        prev = "GENESIS"
        for i, event in enumerate(statement.get("events", []), 1):
            reported_hash = event.get("hash")
            unsealed = {k: v for k, v in event.items() if k != "hash"}
            if event.get("previous_hash") != prev or digest(unsealed) != reported_hash:
                failures.append(f"hash or chain failure at event {i}")
            if event.get("seq") != i or event.get("worker") != wid:
                failures.append(f"identity or sequence failure at event {i}")
            result = account.trade(timestamp=event["timestamp"],
                asset_class=event["asset_class"], symbol=event["symbol"],
                side=event["side"], qty=event["qty"], price=event["price"],
                fee=event["fee"], source_id=event["source_id"])
            if abs(account.cash - event["balance_after"]) > 1e-6:
                failures.append(f"cash mismatch at event {i}")
            if result["positions_after"] != event["positions_after"]:
                failures.append(f"position mismatch at event {i}")
            prev = reported_hash
        if abs(account.cash - statement["cash_usd"]) > 1e-6:
            failures.append("final cash mismatch")
        if account.holdings != statement["positions"]:
            failures.append("final position mismatch")
    except (ValueError, KeyError, TypeError, AttributeError) as exc:
        failures.append("unreplayable or invalid ledger: " + str(exc))
    return {"judge": "J01", "passes": not failures, "findings": failures}


def audit_evidence(statement, trusted_observations=None):
    """Judge 2: citations must match independent price/timestamp observations.

    No independent feed => INCOMPLETE, never 'verified'.
    """
    observations = trusted_observations or {}
    if not statement.get("events"):
        return {"judge": "J02", "passes": None, "findings": ["no trade observations yet"]}
    missing, discrepant = [], []
    for e in statement["events"]:
        ref = e.get("source_id")
        observation = observations.get(ref)
        if observation is None:
            missing.append(ref)
            continue
        try:
            if (observation["symbol"] != e["symbol"] or
                observation["asset_class"] != e["asset_class"] or
                observation["timestamp"] != e["timestamp"] or
                abs(float(observation["execution_price"]) - e["price"]) > 1e-5):
                discrepant.append(ref)
        except (KeyError, ValueError, TypeError):
            discrepant.append(ref)
    findings = [f"unverified observation: {x}" for x in missing]
    findings += [f"price/provenance discrepancy: {x}" for x in discrepant]
    if discrepant:
        return {"judge": "J02", "passes": False, "findings": findings}
    return {"judge": "J02", "passes": None if missing else True,
            "findings": findings if findings else ["observations cross-checked"]}


def audit_risk(statement):
    """Judge 3: independent basic margin and concentration checks."""
    findings = []
    try:
        cash = finite(statement["cash_usd"])
        if cash < -1e-8:
            findings.append("negative cash/margin")
        if abs(finite(statement["initial_usd"]) - 100) > 1e-9:
            findings.append("initial balance not $100")
        for name, units in statement.get("positions", {}).items():
            if finite(units) < -1e-8:
                findings.append("negative holdings for " + name)
        for e in statement.get("events", []):
            if e.get("asset_class") == "us_option_long" and (
                e.get("multiplier") != 100 or e.get("qty") != int(e.get("qty", 0))):
                findings.append("incorrect options contract size")
    except (ValueError, TypeError, KeyError):
        findings.append("invalid risk input")
    return {"judge": "J03", "passes": not findings, "findings": findings}


def council(statement, observations=None):
    votes = [audit_account(statement), audit_evidence(statement, observations),
             audit_risk(statement)]
    hard_veto = any(x["passes"] is False for x in votes)
    yes = sum(x["passes"] is True for x in votes)
    # A split or unverified evidence is not a verified profitable strategy.
    status = ("REJECT_AND_QUARANTINE" if hard_veto else
              "REVIEW_REQUIRED" if any(x["passes"] is None for x in votes) else
              "AUDIT_PASSED" if yes >= 2 else "REVIEW_REQUIRED")
    return {"status": status, "vote_count": yes,
            "judges": votes, "disagreement_training": [
                {"judge": x["judge"], "lesson": other["findings"]}
                for x in votes for other in votes
                if x["passes"] != other["passes"]
            ], "note": "Deterministic reviewer roles, NOT 3 separate LLMs. "
                       "Ledger hash chain is not an externally signed provenance guarantee."}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--demo", action="store_true")
    args = p.parse_args()
    if not args.demo:
        p.error("use --demo; no actual market-data or Alpaca routing is connected")
    worker = PaperAccount("S01")
    worker.trade(timestamp="2026-10-25T12:00:00Z",asset_class="crypto",
                 symbol="BTC/USD", side="BUY",qty=0.0001,price=80000,source_id="SYNTHETIC")
    statement = worker.statement()
    print(json.dumps({"warning": "SYNTHETIC EXAMPLE, NOT MARKET DATA OR TRADING PERFORMANCE",
                      "statement": statement, "council": council(statement)}, indent=2))


if __name__ == "__main__":
    main()
