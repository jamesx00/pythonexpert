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
    (([3, 5, -4, 8], 4), [2, 3]),
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([1, 5, 5, 2], 10), [1, 2]),
    (([-3, 4, 3, 90], 0), [0, 2]),
    (([0, 4, 3, 0], 0), [0, 3]),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.two_sum(*args), expected, normalize=sorted)

# Performance test: 100,000 elements whose only valid pair is the last two.
# Budget: 1.0s. Execution service: hash map solution <0.01s; nested
# loops over every pair are interrupted at the budget.
# Multiples of 4 never sum to 6, and neither does a multiple of 4 plus 1 or 5.
big = [4 * i for i in range(100_000)] + [1, 5]
check(7, lambda: main.two_sum(big, 6), [100_000, 100_001], time_budget=1.0, normalize=sorted)

sys.stdout.write(json.dumps(results))
