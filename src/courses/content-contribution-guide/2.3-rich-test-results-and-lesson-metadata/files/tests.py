import sys
import json
import signal
import time

from unittest.mock import patch
patch('builtins.print').start()

import main

results = {}


class TimeBudgetExceeded(BaseException):
    """BaseException, so a learner's `except Exception` can't swallow it."""


def _on_alarm(signum, frame):
    raise TimeBudgetExceeded()


signal.signal(signal.SIGALRM, _on_alarm)


def check(test_id, call, expected, time_budget=None):
    """Runs one test and records a rich result: got/expected as Python reprs,
    the exception if the learner's code raised, or timed_out if the call is
    still running after time_budget seconds (it is interrupted, so the
    remaining tests still run)."""
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
            "expected": repr(expected),
        }
        return
    results[test_id] = {
        "passed": got == expected,
        "got": repr(got),
        "expected": repr(expected),
    }


cases = [
    (([1, 4, 6, 2], 8), True),
    (([1, 2, 3], 7), False),
    (([5, 5], 10), True),
    (([5], 10), False),
    (([], 0), False),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.has_pair_with_sum(*args), expected)

# Performance test: 100,000 distinct even numbers, odd target, so no pair
# exists and every element must be examined. Generated deterministically.
# Budget: 1.0s. Timings (local Python 3.12, NOT yet the execution service):
# set-based solution ~0.004s; nested-loop solution interrupted at the 1.0s
# budget (it needs ~5 billion pair checks). Real lessons must record timings
# measured on the execution service here instead.
big = list(range(0, 200_000, 2))
check(6, lambda: main.has_pair_with_sum(big, 7), False, time_budget=1.0)

sys.stdout.write(json.dumps(results))
