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


def run(operations):
    """Runs ("add", point) and ("count", point) calls on a new DetectSquares
    and returns what each count call returned, in order."""
    squares = main.DetectSquares()
    counts = []
    for op, point in operations:
        if op == "add":
            squares.add(point)
        else:
            counts.append(squares.count(point))
    return counts


first = [("add", [3, 10]), ("add", [11, 2]), ("add", [3, 2])]
square = [("add", [0, 0]), ("add", [0, 2]), ("add", [2, 0]), ("add", [2, 2])]
cases = [
    (first + [("count", [11, 10])], [1]),
    (first + [("count", [11, 10]), ("count", [14, 8])], [1, 0]),
    (first + [("count", [11, 10]), ("count", [14, 8]), ("add", [11, 10]), ("count", [13, 6])], [1, 0, 0]),
    (square + [("count", [0, 0])], [1]),
    (square + [("count", [0, 0]), ("add", [0, 0]), ("count", [0, 0]), ("count", [2, 2])], [1, 1, 2]),
    ([("count", [5, 5])], [0]),
    (square + [("add", [2, 2]), ("count", [0, 0]), ("count", [4, 4])], [2, 0]),
    ([("add", [1, 1]), ("add", [1, 3]), ("add", [3, 1]), ("add", [-1, 1]), ("add", [-1, 3]), ("count", [3, 3]), ("count", [1, 1])], [1, 1]),
]
for index, (operations, expected) in enumerate(cases):
    check(index + 1, lambda: run(operations), expected)

# Performance test: every point of a 2,000 x 10 grid (x from 0 to 1,999,
# y from 0 to 9) added once, then 5,000 count calls at grid points in a
# fixed shuffled order. For a query at (x, y), each other y2 in its column
# gives side d = y2 - y, and a square to the right (x + d) and to the left
# (x - d) when that column is still on the grid.
# Budget: 1.0s. Execution service: only checking points in the query's
# column ~0.08s; scanning every added point for each count is interrupted
# at the budget.
def grid_squares(x, y):
    total = 0
    for y2 in range(10):
        if y2 != y:
            d = y2 - y
            total += (0 <= x + d < 2000) + (0 <= x - d < 2000)
    return total


big = [("add", [x, y]) for x in range(2000) for y in range(10)]
queries = [((j * 7919) % 2000, j % 10) for j in range(5000)]
big += [("count", [x, y]) for x, y in queries]
check(9, lambda: run(big), [grid_squares(x, y) for x, y in queries], time_budget=1.0)

sys.stdout.write(json.dumps(results))
