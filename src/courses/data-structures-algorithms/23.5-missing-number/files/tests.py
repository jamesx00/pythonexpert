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
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ([0], 1),
    ([1], 0),
    ([1, 2], 0),
    ([5, 3, 0, 1, 4], 2),
]
for index, (nums, expected) in enumerate(cases):
    check(index + 1, lambda: main.missing_number(nums), expected)

# Performance test: 50,000 numbers, (i * 7919) % 50,001 for i in 0..50,000
# (every value 0..50,000 once, shuffled) with 50,000 removed. Budget: 1.0s.
# Execution service: XOR loop ~BENCH_EFF; checking `x not in nums` for every
# candidate x (O(n^2)) is interrupted at the budget.
big = [(i * 7919) % 50_001 for i in range(50_001)]
big.remove(50_000)
check(8, lambda: main.missing_number(big), 50_000, time_budget=1.0)

sys.stdout.write(json.dumps(results))
