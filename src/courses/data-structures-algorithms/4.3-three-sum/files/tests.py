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
    ([-2, 0, 1, 1, -1, -4], [[-2, 1, 1], [-1, 0, 1]]),
    ([0, 0, 0], [[0, 0, 0]]),
    ([0, 0, 0, 0], [[0, 0, 0]]),
    ([1, 2, -3], [[-3, 1, 2]]),
    ([1, 2, 3], []),
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
]
for index, (nums, expected) in enumerate(cases):
    check(index + 1, lambda: main.three_sum(nums), expected, normalize=sorted)

# Performance test: 1,000 distinct values, the odd numbers from -999 to 997
# plus -2. Three odd numbers can't sum to zero, so every trio is -2 with two
# odd values a + b = 2, i.e. b = 3, 5, ..., 997 and a = 2 - b.
# Budget: 1.0s. Execution service: sort + two-pointer solution ~0.09s;
# three nested loops are interrupted at the budget.
big = list(range(-999, 998, 2)) + [-2]
expected_big = [sorted([-2, 2 - b, b]) for b in range(3, 998, 2)]
check(7, lambda: main.three_sum(big), expected_big, time_budget=1.0, normalize=sorted)

sys.stdout.write(json.dumps(results))
