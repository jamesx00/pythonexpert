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
    ([2, 3, 4, 5], [60, 40, 30, 24]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([1, 2], [2, 1]),
    ([-1, 2, -3], [-6, 3, -2]),
    ([0, 4, 5], [20, 0, 0]),
    ([3, 0, 0, 6], [0, 0, 0, 0]),
]
for index, (nums, expected) in enumerate(cases):
    check(index + 1, lambda: main.product_except_self(nums), expected)

# Performance test: 100,000 elements, a 2 followed by 99,999 ones, so the
# answer is a 1 followed by 99,999 twos.
# Budget: 1.0s. Execution service: prefix/suffix solution
# ~0.02s; a nested loop per index is interrupted at the budget.
big = [2] + [1] * 99_999
check(7, lambda: main.product_except_self(big), [1] + [2] * 99_999, time_budget=1.0)

sys.stdout.write(json.dumps(results))
