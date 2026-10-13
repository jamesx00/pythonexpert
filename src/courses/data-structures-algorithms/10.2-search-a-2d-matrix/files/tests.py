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


grid = [[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23]]
cases = [
    ((grid, 13), True),
    ((grid, 6), False),
    ((grid, 1), True),
    ((grid, 23), True),
    ((grid, 24), False),
    (([[5]], 5), True),
    (([], 3), False),
    (([[]], 3), False),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.search_matrix(*args), expected)

# Performance test: 20,000 searches in a 500 x 400 grid holding the even
# numbers 0, 2, ..., 399,998 in order. Only even values are present.
# Budget: 1.0s. Execution service: binary search ~0.1s;
# `target in row` over every row is interrupted at the budget.
big = [[2 * (r * 400 + c) for c in range(400)] for r in range(500)]
queries = [(i * 7919) % 400_000 for i in range(20_000)]
check(
    9,
    lambda: [main.search_matrix(big, q) for q in queries],
    [q % 2 == 0 for q in queries],
    time_budget=1.0,
)

sys.stdout.write(json.dumps(results))
