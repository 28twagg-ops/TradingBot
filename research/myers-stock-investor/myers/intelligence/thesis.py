from __future__ import annotations

import os
from typing import Any

from myers.schemas import CompanyAnalysis


def generate_llm_thesis(analysis: CompanyAnalysis) -> dict[str, Any]:
    """Optional LLM narrative. Returns UNKNOWN stub if no API key.

    Never invents financial numbers — only restates provided analysis fields.
    """
    if not os.environ.get("OPENAI_API_KEY"):
        return {
            "status": "UNAVAILABLE",
            "reason": "OPENAI_API_KEY not set",
            "thesis": analysis.investment_thesis,
            "customer_concentration": "UNKNOWN",
            "key_person_risk": "UNKNOWN",
        }
    # Lightweight optional path — keep deterministic fallback if SDK missing.
    try:
        from openai import OpenAI  # type: ignore
    except Exception:
        return {
            "status": "UNAVAILABLE",
            "reason": "openai package not installed",
            "thesis": analysis.investment_thesis,
            "customer_concentration": "UNKNOWN",
            "key_person_risk": "UNKNOWN",
        }

    client = OpenAI()
    prompt = (
        "You are assisting a business-acquirer style equity researcher. "
        "Do NOT invent numbers. Only interpret the JSON facts given. "
        "If customer concentration or key-person data is missing, say UNKNOWN.\n\n"
        f"{analysis.model_dump_json()}"
    )
    resp = client.responses.create(
        model=os.environ.get("OPENAI_MODEL", "gpt-4o-mini"),
        input=prompt,
    )
    text = getattr(resp, "output_text", None) or str(resp)
    return {
        "status": "OK",
        "thesis": text,
        "customer_concentration": "UNKNOWN",
        "key_person_risk": "UNKNOWN",
        "note": "LLM narrative only; scores/valuations remain from deterministic code",
    }
