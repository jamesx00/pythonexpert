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
    (([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]), True),
    (([[5, 2, 3]], [5, 2, 3]), True),
    (([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]), True),
    (([[3, 4, 5], [4, 5, 6]], [3, 2, 5]), False),
    (([[1, 1, 1]], [2, 2, 2]), False),
    (([[2, 2, 2], [1, 1, 1], [3, 3, 3]], [3, 3, 3]), True),
]
for index, ((triplets, target), expected) in enumerate(cases):
    check(index + 1, lambda: main.merge_triplets(triplets, target), expected)

# Performance test: 10,000 triplets [(i * 7) % 1000, (i * i) % 1000,
# (i * 13 + 5) % 1000] and target [500, 600, 700]. Budget: 1.0s. Execution
# service: one filtering pass ~0.004s; trying every subset of triplets is
# interrupted at the budget.
big = [[(i * 7) % 1000, (i * i) % 1000, (i * 13 + 5) % 1000] for i in range(10_000)]
check(7, lambda: main.merge_triplets(big, [500, 600, 700]), False, time_budget=1.0)

sys.stdout.write(json.dumps(results))
