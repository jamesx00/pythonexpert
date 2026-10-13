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
    (([5, 5, 5, 1, 1, 9], 2), [5, 1]),
    (([1, 2, 2, 3, 3, 3], 1), [3]),
    (([4], 1), [4]),
    (([7, 7, 8, 8, 9, 9], 3), [7, 8, 9]),
    (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
    (([-1, -1, 2, 3, 3], 2), [-1, 3]),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.top_k_frequent(*args), expected, normalize=sorted)

# Performance test: 100,000 values, 50,000 of them distinct. Values 0-9
# appear 5,000 times each; every other value appears once.
# Budget: 1.0s. Execution service: Counter solution ~0.01s;
# calling nums.count(n) for every distinct value is interrupted at the budget.
big = [i % 10 for i in range(50_000)] + list(range(10, 50_010))
check(7, lambda: main.top_k_frequent(big, 10), list(range(10)), time_budget=1.0, normalize=sorted)

sys.stdout.write(json.dumps(results))
