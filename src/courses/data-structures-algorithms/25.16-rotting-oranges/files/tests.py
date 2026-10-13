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
    ([[2, 1, 0], [1, 1, 0], [0, 1, 2]], 2),
    ([[0, 2]], 0),
    ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
    ([[0, 0, 0]], 0),
    ([[1]], -1),
    ([[2]], 0),
    ([[2, 1, 1, 1, 1]], 4),
    ([[2, 1, 1, 1, 2]], 2),
]
for index, (grid, expected) in enumerate(cases):
    check(index + 1, lambda: main.oranges_rotting([row[:] for row in grid]), expected)

# Performance test: a 101x100 grid where the fresh oranges form one winding
# path: every even row is full of oranges, and each odd row has a single
# orange that links to the next even row, at the right end and the left end
# in turn. The only rotten orange is at the start of the path, (0, 0), so the
# rot needs 5,149 minutes to reach the far end. Built outside the budget.
# Budget: 1.0s. Execution service: multi-source BFS ~0.01s; rescanning the
# whole grid once per minute is interrupted at the budget.
rows, cols = 101, 100
big = []
for r in range(rows):
    if r % 2 == 0:
        big.append([1] * cols)
    else:
        row = [0] * cols
        row[cols - 1 if r % 4 == 1 else 0] = 1
        big.append(row)
big[0][0] = 2
check(9, lambda: main.oranges_rotting(big), 5149, time_budget=1.0)

sys.stdout.write(json.dumps(results))
