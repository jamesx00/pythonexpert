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
    ((3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1), 200),
    ((3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0), 500),
    ((4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 5]], 0, 3, 1), 5),
    ((4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 5]], 0, 3, 2), 3),
    ((3, [[0, 1, 100]], 0, 2, 5), -1),
    ((2, [[0, 1, 10]], 0, 1, 0), 10),
    ((4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1), 6),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.find_cheapest_price(*args), expected)

# Performance test: 66 airports. Airport 0 flies to each of 8 airports in
# layer 1, every airport in a layer flies to all 8 in the next layer, and
# the 8 airports in layer 8 fly to airport 65. That's 464 flights, and every
# route from 0 to 65 makes exactly 8 stops, so k = 8 allows all 8^8 (about
# 16.8 million) of them. Prices are fixed numbers from 1 to 50.
# Budget: 1.0s. Execution service: Bellman-Ford limited to k + 1 rounds
# ~0.001s; a DFS over every route is interrupted at the budget.
layers, width = 8, 8
dst = layers * width + 1
big_flights = [[0, 1 + i, 1 + (i * 7) % 50] for i in range(width)]
for j in range(layers - 1):
    for a in range(width):
        for b in range(width):
            big_flights.append([1 + j * width + a, 1 + (j + 1) * width + b, 1 + (a * 7 + b * 13 + j * 3) % 50])
big_flights += [[1 + (layers - 1) * width + i, dst, 1 + (i * 11) % 50] for i in range(width)]
check(8, lambda: main.find_cheapest_price(dst + 1, big_flights, 0, dst, layers), 22, time_budget=1.0)

sys.stdout.write(json.dumps(results))
