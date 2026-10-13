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
    (([1, 4, 6, 2], 8), True),
    (([1, 2, 3], 7), False),
    (([5, 5], 10), True),
    (([5], 10), False),
    (([], 0), False),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.has_pair_with_sum(*args), expected)

# Performance test: 100,000 distinct even numbers, odd target, so no pair
# exists and every element must be examined. Generated deterministically.
# Budget: 1.0s. Execution service (Python 3.10): set-based solution ~0.014s;
# nested-loop solution interrupted at the budget (it needs ~5 billion pair
# checks).
big = list(range(0, 200_000, 2))
check(6, lambda: main.has_pair_with_sum(big, 7), False, time_budget=1.0)

sys.stdout.write(json.dumps(results))
