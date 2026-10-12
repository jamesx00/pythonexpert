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
    """Runs ("add_num", num) and ("find_median",) calls on a new MedianFinder
    and returns what each find_median call returned, in order."""
    finder = main.MedianFinder()
    medians = []
    for op in operations:
        if op[0] == "add_num":
            finder.add_num(op[1])
        else:
            medians.append(finder.find_median())
    return medians


cases = [
    ([("add_num", 5), ("add_num", 1), ("find_median",)], [3.0]),
    ([("add_num", 5), ("add_num", 1), ("add_num", 3), ("find_median",)], [3]),
    ([("add_num", 2), ("find_median",)], [2]),
    ([("add_num", 6), ("add_num", 2), ("add_num", 9), ("add_num", 1), ("find_median",)], [4.0]),
    ([("add_num", -5), ("add_num", -2), ("add_num", -10), ("find_median",)], [-5]),
    ([("add_num", 1), ("add_num", 1), ("add_num", 1), ("add_num", 1), ("find_median",)], [1.0]),
]
for index, (operations, expected) in enumerate(cases):
    check(index + 1, lambda: run(operations), expected)

# Performance test: 100,000 add_num calls, each followed by find_median.
# The numbers alternate low and high: 0, 1,000,000, 1, 999,999, 2, ...
# After the low number j the median is j. After the high number that
# follows it, it's (j + 1,000,000 - j) / 2 = 500,000.0.
# Budget: 1.0s. Execution service: two-heap solution ~0.22s; sorting on
# every find_median is interrupted at the budget.
big = []
expected = []
for j in range(50_000):
    big += [("add_num", j), ("find_median",), ("add_num", 1_000_000 - j), ("find_median",)]
    expected += [j, 500_000.0]
check(7, lambda: run(big), expected, time_budget=1.0)


sys.stdout.write(json.dumps(results))
