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
    (([4, 2, 9, 1, 6, 3], 3), [9, 9, 9, 6]),
    (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
    (([5], 1), [5]),
    (([9, 8, 7, 6], 2), [9, 8, 7]),
    (([1, 1, 1, 1], 2), [1, 1, 1]),
    (([2, 4, 6, 8, 10], 5), [10]),
    (([-1, -3, -2, -5], 2), [-1, -2, -2]),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.window_max(*args), expected)

# Performance test: 100,000 values falling from 99,999 to 0 with k = 50,000,
# so each window's maximum is its first value.
# Budget: 1.0s. Execution service: monotonic-deque solution
# ~0.03s; max() over every window is interrupted at the budget.
big = list(range(99_999, -1, -1))
check(8, lambda: main.window_max(big, 50_000), list(range(99_999, 49_998, -1)), time_budget=1.0)

sys.stdout.write(json.dumps(results))
