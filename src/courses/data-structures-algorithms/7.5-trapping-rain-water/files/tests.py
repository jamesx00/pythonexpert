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
    ([0, 1, 0, 2, 1, 0, 3, 1, 0, 2], 7),
    ([4, 2, 3], 1),
    ([1, 1, 1], 0),
    ([5, 4, 1, 2], 1),
    ([], 0),
    ([3, 0, 0, 2, 0, 4], 10),
]
for index, (heights, expected) in enumerate(cases):
    check(index + 1, lambda: main.trap_rain_water(heights), expected)

# Performance test: 100,000 positions, a wall of height 2 at each end and a
# repeating 0, 1 pattern in between, so every inner position fills to 2:
# 49,999 zeros hold 2 each and 49,999 ones hold 1 each.
# Budget: 1.0s. Execution service: two-pointer solution
# ~0.04s; rescanning both sides for every position is interrupted at the budget.
big = [2] + [i % 2 for i in range(99_998)] + [2]
check(7, lambda: main.trap_rain_water(big), 49_999 * 2 + 49_999, time_budget=1.0)

sys.stdout.write(json.dumps(results))
