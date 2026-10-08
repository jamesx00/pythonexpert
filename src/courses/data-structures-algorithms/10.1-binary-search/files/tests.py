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
    (([-4, 0, 3, 9, 14, 22], 9), 3),
    (([-4, 0, 3, 9, 14, 22], 10), -1),
    (([1, 2, 3, 4, 5], 1), 0),
    (([1, 2, 3, 4, 5], 5), 4),
    (([], 5), -1),
    (([7], 7), 0),
    (([7], 3), -1),
    (([2, 4, 6, 8, 10, 12, 14], 12), 5),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.binary_search(*args), expected)

# Performance test: 20,000 searches in a list of the 200,000 even numbers
# 0, 2, ..., 399,998. An even q is at index q // 2; an odd q is missing.
# Budget: 1.0s. Execution service: binary search ~0.08s;
# `nums.index(target)` per search is interrupted at the budget.
big = list(range(0, 400_000, 2))
queries = [(i * 7919) % 400_000 for i in range(20_000)]
check(
    9,
    lambda: [main.binary_search(big, q) for q in queries],
    [q // 2 if q % 2 == 0 else -1 for q in queries],
    time_budget=1.0,
)

sys.stdout.write(json.dumps(results))
