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
    ([[1, 2, 2], [3, 2, 3], [2, 4, 5]], [[0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]),
    ([[1]], [[0, 0]]),
    ([[3, 3], [3, 3]], [[0, 0], [0, 1], [1, 0], [1, 1]]),
    ([[1, 2, 3]], [[0, 0], [0, 1], [0, 2]]),
    ([[3], [2], [1]], [[0, 0], [1, 0], [2, 0]]),
    ([], []),
    ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]]),
]
for index, (heights, expected) in enumerate(cases):
    check(index + 1, lambda: main.pacific_atlantic(heights), expected, normalize=sorted)

# Performance test: a 100x100 grid where cell (r, c) has height r + c. Water
# only flows up or left, so every cell reaches the Pacific, but only the
# bottom row and the right column (199 cells) reach the Atlantic.
# Budget: 1.0s. Execution service: one search inland from each ocean ~0.02s;
# a separate downhill search from every cell is interrupted at the budget.
size = 100
big = [[r + c for c in range(size)] for r in range(size)]
expected_big = [[size - 1, c] for c in range(size)] + [[r, size - 1] for r in range(size - 1)]
check(8, lambda: main.pacific_atlantic(big), expected_big, time_budget=1.0, normalize=sorted)

sys.stdout.write(json.dumps(results))
