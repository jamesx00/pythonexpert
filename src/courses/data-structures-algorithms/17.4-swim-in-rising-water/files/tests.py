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
    ([[0, 1], [2, 3]], 3),
    ([[0, 2], [1, 3]], 3),
    ([[0]], 0),
    ([[3, 2], [0, 1]], 3),
    ([[0, 1, 2], [1, 2, 3], [2, 3, 4]], 4),
    ([[0, 4, 2], [1, 3, 5], [6, 7, 8]], 8),
    ([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]], 16),
]
for index, (grid, expected) in enumerate(cases):
    check(index + 1, lambda: main.swim_in_water(grid), expected)

# Performance test: a 100x100 grid holding 0 to 9,999 in a scrambled order:
# the cells are ranked by (i * 2654435761) % 2**32, where i = r * 100 + c.
# Budget: 1.0s. Execution service: Dijkstra on the max height ~0.02s;
# binary search on t with a BFS each time ~0.1s; trying t = 0, 1, 2, ...
# with a BFS each time is interrupted at the budget.
n = 100
keys = [(i * 2654435761) % 2**32 for i in range(n * n)]
ranks = [0] * (n * n)
for rank, i in enumerate(sorted(range(n * n), key=lambda i: keys[i])):
    ranks[i] = rank
big = [ranks[r * n:(r + 1) * n] for r in range(n)]
check(8, lambda: main.swim_in_water(big), 7219, time_budget=1.0)

sys.stdout.write(json.dumps(results))
