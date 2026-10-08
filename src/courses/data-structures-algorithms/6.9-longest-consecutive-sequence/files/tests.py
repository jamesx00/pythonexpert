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
    ([9, 1, 4, 2, 3, 100], 4),
    ([], 0),
    ([5], 1),
    ([1, 2, 0, 1], 3),
    ([10, 5, 12, 11, 6, 7], 3),
    ([-2, -1, 0, 1, 2, 8], 5),
]
for index, (nums, expected) in enumerate(cases):
    check(index + 1, lambda: main.longest_consecutive(nums), expected)

# Performance test: one run of 100,000 consecutive values, shuffled by a
# fixed stride (7919 is prime, so every value appears exactly once).
# Budget: 1.0s. Execution service: set solution with the
# run-start check ~0.02s; counting up from every value is interrupted at the
# budget.
big = [(i * 7919) % 100_000 for i in range(100_000)]
check(7, lambda: main.longest_consecutive(big), 100_000, time_budget=1.0)

sys.stdout.write(json.dumps(results))
