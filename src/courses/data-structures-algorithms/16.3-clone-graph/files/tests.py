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


def run(adj_list):
    """Returns the clone, or a message if the clone shares a list object with
    the input instead of being built from new lists."""
    clone = main.clone_graph(adj_list)
    if clone is adj_list:
        return "returned the input list itself"
    if isinstance(clone, list) and any(
            any(inner is original for original in adj_list) for inner in clone):
        return "reused an inner list from the input"
    return clone


cases = [
    ([[1, 2], [0, 2], [0, 1]], [[1, 2], [0, 2], [0, 1]]),
    ([], []),
    ([[]], [[]]),
    ([[1], [0]], [[1], [0]]),
    ([[1, 3], [0, 2], [1, 3], [0, 2]], [[1, 3], [0, 2], [1, 3], [0, 2]]),
    ([[1], [0, 2], [1]], [[1], [0, 2], [1]]),
    ([[1], [0], [3], [2]], [[1], [0], [3], [2]]),
]
for index, (adj_list, expected) in enumerate(cases):
    check(index + 1, lambda: run(adj_list), expected)

sys.stdout.write(json.dumps(results))
