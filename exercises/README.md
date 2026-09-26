# Exercises — E-Ink Refresh

A hands-on companion to Lesson 2 in the interactive tour: the actual math behind the Refresh &
Ghosting Simulator tab — why partial refresh leaves a residual ghost, why a full refresh clears it
exactly, and how many partial refreshes it actually takes to converge on a fixed target.

## Setup

```bash
# from this exercises/ folder
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install pytest
```

## Run the tests

```bash
pytest -v
```

You'll see 8 failing tests — every function in `eink_refresh.py` currently raises `NotImplementedError`.

## What to do

Open `eink_refresh.py`. Implement in this order:

1. `apply_partial_refresh` — the real partial-update behavior: move part of the way, not all the way.
2. `apply_full_refresh` — a full refresh snaps every pixel to its target exactly.
3. `ghost_score` — the metric the Simulator's ghosting gauge is actually computing.
4. `partial_refreshes_to_converge` — how many partial-only refreshes it takes before ghosting drops
   below a threshold, if the target stops changing.

## When you're done

All 8 tests passing means you understand the real tradeoff this project's Common Mistakes list warns
about: partial-only refreshing is faster per update, but the ghosting it leaves behind only clears with
a periodic full refresh — not with "just a few more" partial ones on a target that keeps changing.
