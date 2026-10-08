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
    (([1, 3, 4, 7, 11], 10), [1, 3]),
    (([-4, -1, 0, 3, 8], 4), [0, 4]),
    (([2, 5], 7), [0, 1]),
    (([1, 2, 3, 4, 6], 10), [3, 4]),
    (([-6, -3, -1, 2, 9], -9), [0, 1]),
    (([0, 0, 3, 5], 0), [0, 1]),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.two_sum_sorted(*args), expected)

# Performance test: 100,000 sorted values whose only valid pair is the
# middle two (multiples of 4, except for 1 and 5).
# Budget: 1.0s. Execution service: two-pointer solution
# ~0.02s; nested loops over every pair are interrupted at the budget.
big = [4 * i - 200_000 for i in range(50_000)] + [1, 5] + [4 * i + 8 for i in range(50_000)]
check(7, lambda: main.two_sum_sorted(big, 6), [50_000, 50_001], time_budget=1.0)

sys.stdout.write(json.dumps(results))
