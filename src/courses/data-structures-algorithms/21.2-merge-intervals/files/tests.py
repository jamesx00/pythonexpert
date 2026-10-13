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
    ([[8, 10], [1, 3], [2, 6]], [[1, 6], [8, 10]]),
    ([[1, 4], [4, 5]], [[1, 5]]),
    ([[1, 4], [0, 4]], [[0, 4]]),
    ([[1, 4], [2, 3]], [[1, 4]]),
    ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),
    ([[5, 7]], [[5, 7]]),
    ([[1, 10], [2, 3], [4, 5], [6, 7]], [[1, 10]]),
]
for index, (intervals, expected) in enumerate(cases):
    check(index + 1, lambda: main.merge_intervals(intervals), expected)

# Performance test: 100,000 intervals, [4i, 4i + 2] and [4i + 1, 4i + 3] for
# i in range(50,000), shuffled by a fixed permutation. Each pair merges into
# [4i, 4i + 3], so the answer has 50,000 intervals.
# Budget: 1.0s. Execution service: sort-and-sweep solution ~0.11s; merging
# overlapping pairs until none are left is interrupted at the budget.
pairs = [[4 * i, 4 * i + 2] for i in range(50_000)] + [[4 * i + 1, 4 * i + 3] for i in range(50_000)]
big = [pairs[(j * 7919) % 100_000] for j in range(100_000)]
check(8, lambda: main.merge_intervals(big), [[4 * i, 4 * i + 3] for i in range(50_000)], time_budget=1.0)


sys.stdout.write(json.dumps(results))
