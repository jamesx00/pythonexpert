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
    ([1, 5, 11, 5], True),
    ([1, 2, 3, 5], False),
    ([1, 1], True),
    ([1], False),
    ([2, 2, 3, 5], False),
    ([3, 3, 3, 4, 5], True),
    ([2, 2, 2, 2, 3, 4, 5], True),
]
for index, (nums, expected) in enumerate(cases):
    check(index + 1, lambda: main.can_partition(nums), expected)

# Performance test: 61 even numbers, 2 * ((i * 7) % 23 + 1) for i < 60 plus
# one more 2. They sum to 1442, so each half would need 721, which is odd and
# can't be made from even numbers.
# Budget: 1.0s. Execution service: set of reachable sums ~0.002s; recursion
# memoized on (i, remaining) ~0.01s; trying every subset without a memo is
# interrupted at the budget.
big = [2 * ((i * 7) % 23 + 1) for i in range(60)] + [2]
check(8, lambda: main.can_partition(big), False, time_budget=1.0)

sys.stdout.write(json.dumps(results))
