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
    ([2, 1, 5, 6, 2, 3], 10),
    ([2, 4], 4),
    ([1, 1, 1, 1], 4),
    ([6, 2, 5, 4, 5, 1, 6], 12),
    ([5], 5),
    ([0, 0, 0], 0),
]
for index, (heights, expected) in enumerate(cases):
    check(index + 1, lambda: main.largest_rectangle_area(heights), expected)

# Performance test: 100,000 bars of heights 1, 2, ..., 100,000. The best
# rectangle starting at bar i is (i + 1) tall and 100,000 - i wide, which
# peaks at 50,000 * 50,001 when i = 49,999.
# Budget: 1.0s. Execution service: monotonic-stack
# solution ~0.07s; trying every pair of edges is interrupted at the budget.
big = list(range(1, 100_001))
check(7, lambda: main.largest_rectangle_area(big), 50_000 * 50_001, time_budget=1.0)

sys.stdout.write(json.dumps(results))
