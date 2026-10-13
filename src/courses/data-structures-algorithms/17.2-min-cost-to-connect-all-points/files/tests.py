import sys
import json
import signal

from unittest.mock import patch
patch('builtins.print').start()

import main

results = {}


class TimeBudgetExceeded(BaseException):
    """BaseException, so a learner's `except Exception` can't swallow it."""


def _on_alarm(signum, frame):
    raise TimeBudgetExceeded()


signal.signal(signal.SIGALRM, _on_alarm)


def _show(value):
    text = repr(value)
    return text if len(text) <= 300 else text[:300] + "..."


def check(test_id, call, expected, time_budget=None, normalize=None):
    """Runs one test and records a rich result: got/expected as Python reprs,
    the exception if the learner's code raised, or timed_out if the call is
    still running after time_budget seconds (it is interrupted, so the
    remaining tests still run). normalize, if given, is applied to both
    values before comparing, for answers whose order doesn't matter."""
    try:
        if time_budget is not None:
            signal.setitimer(signal.ITIMER_REAL, time_budget)
        try:
            got = call()
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)
    except TimeBudgetExceeded:
        results[test_id] = {"passed": False, "timed_out": True}
        return
    except Exception as e:
        results[test_id] = {
            "passed": False,
            "error": f"{type(e).__name__}: {e}",
            "expected": _show(expected),
        }
        return
    try:
        if normalize is None:
            passed = got == expected
        else:
            passed = normalize(got) == normalize(expected)
    except Exception:
        passed = False
    results[test_id] = {
        "passed": bool(passed),
        "got": _show(got),
        "expected": _show(expected),
    }




cases = [
    ([[0, 0], [2, 2], [3, 10]], 13),
    ([[0, 0], [2, 2]], 4),
    ([[0, 0]], 0),
    ([[0, 0], [1, 1], [1, 0], [-1, 1]], 4),
    ([[3, 12], [-2, 5], [-4, 1]], 18),
    ([[0, 0], [5, 0], [10, 0], [15, 0]], 15),
]
for index, (points, expected) in enumerate(cases):
    check(index + 1, lambda: main.min_cost_connect_points(points), expected)

# Performance test: 500 points spread over a 10,007 x 10,007 square.
# Budget: 1.0s. Execution service: Prim with a best-edge array ~0.07s; Prim
# with a heap ~0.11s; Kruskal over all pairs ~0.13s; Prim that rescans every
# (tree, non-tree) pair for each new point is interrupted at the budget.
big = [[(i * 7919) % 10007, (i * 104729) % 10007] for i in range(500)]
check(7, lambda: main.min_cost_connect_points(big), 219497, time_budget=1.0)

sys.stdout.write(json.dumps(results))
