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
    ([[5, 1, 6], [4, 2, 7], [3, 8, 9]], 4),
    ([[1]], 1),
    ([[7, 7, 7], [7, 7, 7]], 1),
    ([[1, 2, 3], [8, 9, 4], [7, 6, 5]], 9),
    ([[10, 20], [15, 25]], 3),
]
for index, (matrix, expected) in enumerate(cases):
    check(index + 1, lambda: main.longest_increasing_path(matrix), expected)

# Performance test: a 100 x 100 grid, cell (r, c) = r + c. Every path that
# only moves right or down is increasing, so there are exponentially many.
# Budget: 1.0s. Execution service: DFS with a memo ~0.021s; DFS without
# a memo is interrupted at the budget.
big = [[r + c for c in range(100)] for r in range(100)]
check(6, lambda: main.longest_increasing_path(big), 199, time_budget=1.0)


sys.stdout.write(json.dumps(results))
