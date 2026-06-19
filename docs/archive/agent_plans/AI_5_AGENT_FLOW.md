# AI 5-Agent Flow (TradingBot)

Use this flow for any non-trivial bot change (execution logic, exits, sizing, simulation assumptions).

## Roles (run in parallel)

1. **Builder**
   - Implements the requested change.
   - Keeps fallback behavior to current live method.

2. **Tester**
   - Runs targeted checks (`py_compile`, focused sim tests, log sanity checks).
   - Reports pass/fail with exact commands and outputs.

3. **Critic**
   - Tries to break the change.
   - Looks for edge cases, regressions, hidden assumptions, and false confidence.

4. **Risk/Execution Analyst**
   - Focuses on real-world fill behavior, slippage, PDT constraints, and broker limitations.
   - Verifies behavior under fractional shares and gap scenarios.

5. **Integrator (final gate)**
   - Compares findings from all 4 agents.
   - Produces one merged recommendation:
     - ship now
     - ship with guardrails
     - do not ship

## Required Outputs Before Shipping

- **Code diff** from Builder.
- **Test evidence** from Tester (not just "looks good").
- **Failure modes** from Critic.
- **Execution-risk summary** from Risk/Execution Analyst.
- **Final go/no-go decision** from Integrator.

## Decision Rules

- If Critic finds a high-severity regression: **do not ship**.
- If Tester cannot reproduce expected behavior: **do not ship**.
- If Risk analyst says change violates PDT or worsens stop execution without fallback: **do not ship**.
- If all 4 lanes are acceptable: ship with Integrator summary.

## Fallback Rule (mandatory)

Every execution enhancement must have explicit fallback to current method.

Example pattern:
- Try new method (quote-aware limit, adaptive timeout, etc.)
- If quote/submit/fill check fails -> fallback to current `do_sell` path
- Log fallback reason in output for audit

## When To Use This

Use the 5-agent flow when:
- touching `rubber_band_bot.py` execution paths (`do_sell`, exits, stop handling),
- changing stop logic or schedule behavior,
- changing simulation assumptions in `simulations/validation_sim.py`,
- making any change that could affect live P&L.

Skip full flow only for tiny, low-risk changes (comments, formatting, docs-only).

