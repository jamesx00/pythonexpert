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


INF = 2147483647


def run(grid):
    # A fresh copy of the grid, so the in-place changes can't affect the next
    # test.
    return main.islands_and_treasure([row[:] for row in grid])


cases = [
    ([[INF, -1, 0], [INF, INF, INF], [0, -1, INF]], [[2, -1, 0], [1, 2, 1], [0, -1, 2]]),
    ([[0]], [[0]]),
    ([[-1]], [[-1]]),
    ([[INF]], [[INF]]),
    ([[0, INF, INF]], [[0, 1, 2]]),
    ([[0, -1, INF]], [[0, -1, INF]]),
    ([[0, INF, INF, INF, 0]], [[0, 1, 2, 1, 0]]),
]
for index, (grid, expected) in enumerate(cases):
    check(index + 1, lambda: run(grid), expected)

# Performance test: a 200x200 grid of open ground with a chest on every cell
# of row 0, so the distance of cell (r, c) is just r. Built outside the
# budget.
# Budget: 1.0s. Execution service: one BFS from all chests at once ~0.05s;
# a separate BFS from each of the 200 chests is interrupted at the budget.
size = 200
big = [[0] * size] + [[INF] * size for _ in range(size - 1)]
check(8, lambda: run(big), [[r] * size for r in range(size)], time_budget=1.0)

sys.stdout.write(json.dumps(results))
