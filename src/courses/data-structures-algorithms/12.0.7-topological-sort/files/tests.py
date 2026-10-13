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


def verdict(n, edges):
    """Returns a normalize function that maps an order to "valid" if it lists
    nodes 0..n-1 once each with every edge pointing forward, "cycle" for [],
    and "invalid" otherwise. Any valid order then matches the example."""
    def normalize(order):
        if order == []:
            return "cycle"
        if sorted(order) != list(range(n)):
            return "invalid"
        position = {node: i for i, node in enumerate(order)}
        if any(position[a] > position[b] for a, b in edges):
            return "invalid"
        return "valid"
    return normalize


cases = [
    ((4, [[0, 1], [0, 2], [1, 3], [2, 3]]), [0, 1, 2, 3]),
    ((2, [[0, 1], [1, 0]]), []),
    ((1, []), [0]),
    ((3, []), [0, 1, 2]),
    ((6, [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]), [4, 5, 2, 0, 3, 1]),
    ((4, [[0, 1], [1, 2], [2, 3], [3, 1]]), []),
]
for index, ((n, edges), expected) in enumerate(cases):
    check(index + 1, lambda: main.topo_sort(n, edges), expected, normalize=verdict(n, edges))

sys.stdout.write(json.dumps(results))
