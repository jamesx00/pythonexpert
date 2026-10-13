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
    (([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3),
    (([2, 3, 4], [3, 4, 3]), -1),
    (([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]), 4),
    (([3, 3, 4], [3, 4, 4]), -1),
    (([4, 5, 2, 6, 5, 3], [3, 2, 7, 3, 2, 9]), -1),
    (([7], [6]), 0),
    (([3, 1, 1], [1, 2, 2]), 0),
]
for index, ((gas, cost), expected) in enumerate(cases):
    check(index + 1, lambda: main.can_complete_circuit(gas, cost), expected)

# Performance test: 20,000 stations. The first 19,998 each gain 1 charge, the
# next costs 20,000 more than it gives, and the last gains 3, so only the
# last station works, and every other start runs out at the expensive one.
# Budget: 1.0s. Execution service: one pass with a running tank ~0.003s;
# trying every start (O(n^2)) is interrupted at the budget.
gas = [2] * 19_998 + [0, 4]
cost = [1] * 19_998 + [20_000, 1]
check(8, lambda: main.can_complete_circuit(gas, cost), 19_999, time_budget=1.0)

sys.stdout.write(json.dumps(results))
