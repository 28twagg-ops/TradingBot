"""Bounded local Ollama model experimentation, telemetry and automatic fallback.

No model downloads, cloud calls, inference, shell commands, broker API or trading
orders are performed here. Only installed local Ollama model names are eligible.
"""
import datetime as dt
import json
import math
import os
from pathlib import Path
import statistics

BASE = "qwen3:4b-instruct"
STRONG = "qwen3:8b"
OTHER = ("gemma3:4b", "llama3.2:3b", "llama3.2:1b")
OK = {"RESEARCHED", "RESEARCH_IDEA_NEEDS_DATA", "RESEARCH_IDEA_NEEDS_REVISION"}
STORE = "model_runtime.json"


def hardware():
    """Optional psutil; unknown is not represented as 0% CPU or free memory."""
    result = {"cpu_percent": None, "free_ram_gb": None, "total_ram_gb": None}
    try:
        import psutil
        m = psutil.virtual_memory()
        result.update(cpu_percent=round(psutil.cpu_percent(interval=0.1), 1),
                      free_ram_gb=round(m.available / (1024**3), 2),
                      total_ram_gb=round(m.total / (1024**3), 2))
    except (ImportError, OSError, AttributeError, RuntimeError):
        pass
    return result


def _median(rows, name):
    vals = [x[name] for x in rows if type(x.get(name)) in (int, float)
            and math.isfinite(x[name]) and x[name] >= 0]
    return round(statistics.median(vals), 2) if vals else None


def score(rows):
    total = len(rows)
    valid = sum(x.get("status") in OK for x in rows)
    return {"attempts": total, "valid_research": valid,
            "valid_percent": round(100 * valid / total, 1) if total else None,
            "median_tokens_per_second": _median(rows, "tokens_per_second"),
            "median_latency_seconds": _median(rows, "elapsed_seconds"),
            "invalid_json_count": sum(x.get("safe_error") == "OLLAMA_INVALID_JSON" for x in rows),
            "median_cpu_percent": _median(rows, "cpu_percent"),
            "median_free_ram_gb": _median(rows, "free_ram_gb")}


class AdaptiveRouter:
    """Single inference lane by default; self-experiment on <=1/4 tasks.

    Bigger models do not inherently yield good trading ideas. Selection only
    weighs validated-format outcomes, speed, and measured system headroom.
    No unfamiliar model is downloaded during the scheduled overnight window.
    """
    def __init__(self, data, installed, preferred=BASE, sample_hardware=None):
        self.path = Path(data) / STORE
        self.installed = list(dict.fromkeys(installed))
        self.preferred = preferred if preferred in self.installed else next(
            (x for x in (BASE, "gemma3:4b", "llama3.2:3b", "llama3.2:1b")
             if x in self.installed), None)
        if not self.preferred:
            raise RuntimeError("OLLAMA_MODEL_NOT_INSTALLED_OR_SERVICE_OFFLINE")
        self.strong = STRONG if STRONG in self.installed and STRONG != self.preferred else None
        self.sample_hardware = sample_hardware or hardware
        self.history = []
        try:
            doc = json.loads(self.path.read_text(encoding="utf-8"))
            if isinstance(doc, dict) and doc.get("schema") == 1:
                self.history = [x for x in doc.get("records", [])[-300:]
                                if isinstance(x, dict)]
        except (OSError, ValueError, TypeError):
            pass
        self.round_index = 0
        self.worker_index = 0
        self.last_choice = self.preferred
        self.reasons = []

    def _rows(self, model):
        # Compare only the most recent 30 responses per installed model.
        return [x for x in self.history if x.get("model") == model][-30:]

    def _capable(self, model, hw):
        if model != STRONG:
            return True
        # An 8B Q4 model ~5.2GB on disk, with additional inference overhead.
        # Unknown free memory is not affirmative evidence for promotion.
        return (type(hw.get("free_ram_gb")) in (int, float)
                and hw["free_ram_gb"] >= 8.0
                and (hw.get("cpu_percent") is None or hw["cpu_percent"] < 88))

    def choose(self, worker=None):
        self.worker_index += 1
        hw = self.sample_hardware()
        base_rows = self._rows(self.preferred)
        high_rows = self._rows(self.strong) if self.strong else []
        high_bad = len(high_rows) >= 2 and (
            score(high_rows[-5:])["valid_percent"] < 60 or
            (score(high_rows[-5:])["median_tokens_per_second"] is not None
             and score(high_rows[-5:])["median_tokens_per_second"] < 4) or
            (score(high_rows[-5:])["median_latency_seconds"] is not None
             and score(high_rows[-5:])["median_latency_seconds"] > 180))
        eligible = (self.strong and self._capable(self.strong, hw)
                    and not high_bad)
        # Spend the first four requests on stable baseline before attempting
        # a larger model. One canary at a time, at most one in four workers.
        canary = bool(eligible and len(base_rows) >= 4 and
                      score(base_rows[-8:])["valid_percent"] >= 70 and
                      self.worker_index % 4 == 1)
        if canary:
            pick = self.strong
            reason = "8B_CANARY_OR_QUALITY_PASS"
        else:
            pick = self.preferred
            reason = ("4B_FALLBACK_OR_BASELINE" if high_bad else
                      "BASELINE_OR_INSUFFICIENT_HEADROOM")
        self.last_choice = pick
        self.reasons.append(reason)
        return pick

    def record(self, event):
        metric = event.get("local_metrics") if isinstance(event, dict) else {}
        metric = metric if isinstance(metric, dict) else {}
        model = event.get("model", self.preferred)
        if model not in self.installed:
            return
        row = {"timestamp": dt.datetime.now(dt.timezone.utc).isoformat(),
               "worker": str(event.get("worker", ""))[:3],
               "model": model,
               "status": str(event.get("status", ""))[:50],
               "safe_error": str(event.get("safe_error", ""))[:40]}
        hw = metric.get("hardware_snapshot", {})
        hw = hw if isinstance(hw, dict) else {}
        for field in ("cpu_percent","free_ram_gb","total_ram_gb"):
            val = hw.get(field)
            if type(val) in (int,float) and math.isfinite(val) and 0 <= val <= 1e9:
                row[field] = round(val,2)
        for k in ("tokens_per_second", "elapsed_seconds", "load_seconds",
                  "eval_count", "prompt_eval_count", "retries"):
            v = metric.get(k)
            if type(v) in (int, float) and math.isfinite(v) and 0 <= v <= 1e9:
                row[k] = round(v, 3)
        self.history.append(row)
        self.history = self.history[-300:]
        self.path.parent.mkdir(parents=True, exist_ok=True)
        target = self.path.with_suffix(".tmp")
        target.write_text(json.dumps({"schema": 1, "records": self.history},
                                      indent=2) + "\n", encoding="utf-8")
        os.replace(target, self.path)

    def summary(self):
        models = [x for x in (self.preferred, self.strong) if x]
        return {"models": {x: score(self._rows(x)) for x in models},
                "last_selected": self.last_choice,
                "last_switch_reason": self.reasons[-1] if self.reasons else "NO_ROUTING_YET",
                "hardware_snapshot": self.sample_hardware(),
                "measurement_note":
                    "CPU is sampled, not continuous; model success means structurally "
                    "accepted research, not validated investment performance."}


def format_report(doc):
    if not isinstance(doc, dict):
        return ""
    rows = ["", "## Adaptive local model telemetry",
            "Success % measures accepted research output, NOT profitable trading.",
            "Ollama response metrics include prompt and generated token counts;",
            "latency and generation throughput are measured separately.", "",
            "| Installed model | Samples | Valid output | Median tokens/s | Median response seconds | CPU sample % | Free RAM GB |",
            "|---|---:|---:|---:|---:|---:|---:|"]
    for model, stats in doc.get("models", {}).items():
        def fmt(v):
            return "Unavailable" if v is None else str(v)
        rows.append("| {} | {} | {} | {} | {} | {} | {} |".format(
            model, stats["attempts"], fmt(stats["valid_percent"])+
            ("%" if stats["valid_percent"] is not None else ""),
            fmt(stats["median_tokens_per_second"]),
            fmt(stats["median_latency_seconds"]),
            fmt(stats["median_cpu_percent"]),fmt(stats["median_free_ram_gb"])))
    hw = doc.get("hardware_snapshot", {})
    rows.append("")
    rows.append("Latest hardware sample: CPU {}%; free RAM {} GB / total {} GB.".format(
        hw.get("cpu_percent") if hw.get("cpu_percent") is not None else "unknown",
        hw.get("free_ram_gb") if hw.get("free_ram_gb") is not None else "unknown",
        hw.get("total_ram_gb") if hw.get("total_ram_gb") is not None else "unknown"))
    rows.append("Last selected: {}; reason: {}.".format(
        doc.get("last_selected"), doc.get("last_switch_reason")))
    rows.append("The laptop must be running and awake for these measurements.")
    return "\n".join(rows) + "\n"
