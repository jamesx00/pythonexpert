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


def run(matrix):
    # A fresh copy of the grid, so the in-place changes can't affect the
    # next test.
    return main.set_zeroes([row[:] for row in matrix])


def run_in_place(matrix):
    # Ignores the return value and reads the grid that was passed in.
    grid = [row[:] for row in matrix]
    main.set_zeroes(grid)
    return grid


cases = [
    ([[1, 2, 3], [4, 0, 6], [7, 8, 9]], [[1, 0, 3], [0, 0, 0], [7, 0, 9]]),
    ([[0, 1], [1, 1]], [[0, 0], [0, 1]]),
    ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
    ([[1, 0, 3], [4, 5, 6], [0, 8, 9]], [[0, 0, 0], [0, 0, 6], [0, 0, 0]]),
    ([[5]], [[5]]),
    ([[0]], [[0]]),
    ([[1, 2, 3, 4], [5, 0, 7, 0], [9, 10, 11, 12]], [[1, 0, 3, 0], [0, 0, 0, 0], [9, 0, 11, 0]]),
]
for index, (matrix, expected) in enumerate(cases):
    check(index + 1, lambda: run(matrix), expected)

check(8, lambda: run_in_place([[1, 2, 3], [4, 0, 6], [7, 8, 9]]), [[1, 0, 3], [0, 0, 0], [7, 0, 9]])

# Performance test: a 600x600 grid with a 0 wherever both the row and the
# column are multiples of 3 (40,000 zeros), and 1 + r * 600 + c everywhere
# else. Rows and columns that are multiples of 3 end up all 0, the rest keep
# their values. Built outside the budget.
# Budget: 1.0s. Execution service: recording zero rows and columns first
# ~0.06s; zeroing a whole row and column for every 0 found is interrupted
# at the budget.
size = 600
big = [[0 if r % 3 == 0 and c % 3 == 0 else 1 + r * size + c for c in range(size)] for r in range(size)]
expected_big = [[0 if r % 3 == 0 or c % 3 == 0 else 1 + r * size + c for c in range(size)] for r in range(size)]
check(9, lambda: run(big), expected_big, time_budget=1.0)

sys.stdout.write(json.dumps(results))
