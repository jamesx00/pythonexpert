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
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([1, 2, 3], 3),
    ([5], 5),
    ([5, 5], 5),
    ([0, 0, 0, 0], 0),
    ([6, 7, 1, 3, 8, 2, 4], 19),
]
for index, (houses, expected) in enumerate(cases):
    check(index + 1, lambda: main.rob_circular(houses), expected)

# Performance test: 200 houses in a circle, 100 at both ends (so they are
# neighbors and can't both be robbed) and (i * 53) % 97 between.
# Budget: 1.0s. Execution service: two linear passes under 0.001s; trying
# every take/skip choice without a memo is interrupted at the budget.
big = [100] + [(i * 53) % 97 for i in range(1, 199)] + [100]
check(8, lambda: main.rob_circular(big), 6771, time_budget=1.0)

sys.stdout.write(json.dumps(results))
