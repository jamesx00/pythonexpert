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
    ((3, [[0, 1, 4], [0, 2, 1], [2, 1, 2]], 0), [0, 3, 1]),
    ((1, [], 0), [0]),
    ((3, [[0, 1, 5]], 0), [0, 5, -1]),
    ((4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]], 0), [0, 1, 2, 3]),
    ((4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]], 2), [-1, -1, 0, 1]),
    ((5, [[0, 1, 2], [0, 2, 6], [1, 2, 3], [1, 3, 8], [2, 3, 0], [3, 4, 1]], 0), [0, 2, 5, 5, 6]),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.dijkstra(*args), expected)

# Performance test: 20,000 nodes in a line. Each node i has an edge to i + 1
# costing 2 and an edge to i + 2 costing 3, so the cheapest cost to an even
# node 2m is 3m (all skip edges) and to an odd node 2m + 1 is 3m + 2.
# The edges are listed from the far end backwards, so each round of
# Bellman-Ford only settles about two more nodes.
# Budget: 1.0s. Execution service: Dijkstra with a heap ~0.03s; Bellman-Ford
# and Dijkstra with a linear scan for the closest node are interrupted at
# the budget.
n = 20_000
big_edges = []
for i in range(n - 2, -1, -1):
    big_edges.append([i, i + 1, 2])
    if i + 2 < n:
        big_edges.append([i, i + 2, 3])
big_expected = [3 * (i // 2) + 2 * (i % 2) for i in range(n)]
check(7, lambda: main.dijkstra(n, big_edges, 0), big_expected, time_budget=1.0)

sys.stdout.write(json.dumps(results))
