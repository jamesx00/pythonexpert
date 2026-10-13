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


def squared_distances(points):
    """The points' squared distances from the origin, sorted, for comparing
    answers where several points tie."""
    return sorted(x * x + y * y for x, y in points)


cases = [
    (([[1, 1], [4, 4], [0, 1], [3, 3]], 2), [[0, 1], [1, 1]]),
    (([[3, 3], [5, -1], [-2, 4]], 1), [[3, 3]]),
    (([[0, 0], [1, 0], [2, 0]], 2), [[0, 0], [1, 0]]),
    (([[-5, 4], [-6, -1], [3, 1]], 3), [[-5, 4], [-6, -1], [3, 1]]),
]
for index, ((points, k), expected) in enumerate(cases):
    check(index + 1, lambda: main.k_closest(points, k), expected, normalize=sorted)

# All four points are at squared distance 5, so any two of them are correct.
check(5, lambda: main.k_closest([[1, 2], [-1, -2], [1, -2], [-1, 2]], 2), [[1, 2], [-1, -2]], normalize=squared_distances)
check(6, lambda: main.k_closest([[7, 7]], 1), [[7, 7]])


sys.stdout.write(json.dumps(results))
