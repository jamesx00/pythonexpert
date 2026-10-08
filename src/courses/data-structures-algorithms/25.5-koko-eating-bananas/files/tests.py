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
    (([3, 6, 7, 11], 8), 4),
    (([30, 11, 23, 4, 20], 5), 30),
    (([30, 11, 23, 4, 20], 6), 23),
    (([1, 1, 1, 1], 4), 1),
    (([1000000000], 2), 500000000),
    (([5], 1), 5),
    (([2, 4, 8], 6), 3),
]
for index, (args, expected) in enumerate(cases):
    # Test 5 has a single pile of 1,000,000,000 bananas, so trying speeds one
    # by one never finishes. Give every test the same budget so that run is
    # reported as too slow instead of the whole run being killed.
    check(index + 1, lambda: main.min_eating_speed(*args), expected, time_budget=1.0)

# Performance test: 1,000 piles of 1,000,000 bananas and 2,000 hours, so
# each pile must take 2 hours and the slowest speed is 500,000.
# Budget: 1.0s. Execution service: binary search ~0.002s;
# trying speeds 1, 2, 3, ... is interrupted at the budget (and on test 5).
big = [1_000_000] * 1_000
check(8, lambda: main.min_eating_speed(big, 2_000), 500_000, time_budget=1.0)

sys.stdout.write(json.dumps(results))
