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
    (([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]), [3, 3, 1, 4]),
    (([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]), [2, -1, 4, 6]),
    (([[1, 5]], [1, 3, 5, 6]), [5, 5, 5, -1]),
    (([], [1, 2, 3]), [-1, -1, -1]),
    (([[1, 10], [1, 3], [4, 10]], [1, 4, 10]), [3, 7, 7]),
    (([[1, 1], [2, 2], [3, 3]], [1, 2, 3, 4]), [1, 1, 1, -1]),
]
for index, ((intervals, queries), expected) in enumerate(cases):
    check(index + 1, lambda: main.min_interval_for_queries(intervals, queries), expected)

# Performance test: 50,000 intervals [2i, 2i + 1] of size 2, plus [0, 200,000]
# of size 200,001, and 50,000 queries spread over 0..249,999 in a fixed
# shuffled order. A query below 100,000 is in a size-2 interval, one up to
# 200,000 only in the big one, and one above that in none.
# Budget: 1.0s. Execution service: sorted queries with a heap ~0.07s;
# checking every interval for every query is interrupted at the budget.
spans = [[2 * i, 2 * i + 1] for i in range(50_000)] + [[0, 200_000]]
qs = [(j * 7919) % 250_000 for j in range(50_000)]
want = [2 if q < 100_000 else 200_001 if q <= 200_000 else -1 for q in qs]
check(7, lambda: main.min_interval_for_queries(spans, qs), want, time_budget=1.0)


sys.stdout.write(json.dumps(results))
