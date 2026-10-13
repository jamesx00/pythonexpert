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
    ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
    ([[1, 2], [1, 2], [1, 2]], 2),
    ([[1, 2], [2, 3]], 0),
    ([], 0),
    ([[1, 100], [11, 22], [1, 11], [2, 12]], 2),
    ([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]], 2),
    ([[-5, -2], [-3, 1], [2, 5]], 1),
]
for index, (intervals, expected) in enumerate(cases):
    check(index + 1, lambda: main.erase_overlap_intervals(intervals), expected)

# Performance test: 100,000 intervals [i, i + 2] for i in range(100,000),
# shuffled by a fixed permutation. Each one overlaps its neighbours, and the
# ones with an even start only touch, so 50,000 are kept and 50,000 removed.
# Budget: 1.0s. Execution service: greedy by end time ~0.05s; an O(n^2)
# dynamic programming solution is interrupted at the budget.
spans = [[i, i + 2] for i in range(100_000)]
big = [spans[(j * 7919) % 100_000] for j in range(100_000)]
check(8, lambda: main.erase_overlap_intervals(big), 50_000, time_budget=1.0)


sys.stdout.write(json.dumps(results))
