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
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([-2, 3, -4], 24),
    ([5], 5),
    ([-3], -3),
    ([2, -5, -2, -4, 3], 24),
    ([0, 2, -3, 4, -1, 0], 24),
]
for index, (nums, expected) in enumerate(cases):
    check(index + 1, lambda: main.max_product_subarray(nums), expected)

# Performance test: 10,000 numbers, mostly 1 and -1, with -2 at every
# multiple of 997. The whole list multiplies to 2 ** 11 = 2048.
# Budget: 1.0s. Execution service: one pass ~0.007s; trying every subarray
# (O(n^2)) is interrupted at the budget.
big = [-2 if i % 997 == 0 else -1 if i % 3 == 1 else 1 for i in range(10_000)]
check(8, lambda: main.max_product_subarray(big), 2048, time_budget=1.0)

sys.stdout.write(json.dumps(results))
