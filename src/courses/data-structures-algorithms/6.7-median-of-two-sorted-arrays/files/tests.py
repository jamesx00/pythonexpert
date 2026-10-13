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
    (([1, 3], [2]), 2.0),
    (([1, 2], [3, 4]), 2.5),
    (([], [1]), 1.0),
    (([2], []), 2.0),
    (([1, 2, 3], [4, 5, 6, 7]), 4.0),
    (([-5, -3, -1], [-4, -2]), -3.0),
    (([1, 1, 1], [1, 1]), 1.0),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.find_median_sorted_arrays(*args), expected)

# Performance test: 2,000 calls on the 100,000 even and 100,000 odd numbers
# below 200,000. Together they are 0..199,999, whose median is 99,999.5.
# Budget: 1.0s. Execution service: partition binary search
# ~0.004s; sorted(nums1 + nums2) per call is interrupted at the budget.
evens = list(range(0, 200_000, 2))
odds = list(range(1, 200_000, 2))
check(
    8,
    lambda: [main.find_median_sorted_arrays(evens, odds) for _ in range(2_000)],
    [99_999.5] * 2_000,
    time_budget=1.0,
)

sys.stdout.write(json.dumps(results))
