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


def run(k, nums, values):
    """Creates KthLargest(k, nums), calls add(value) for each value and
    returns what each add returned, in order."""
    stream = main.KthLargest(k, nums)
    return [stream.add(value) for value in values]


cases = [
    ((2, [3, 8], [5]), [5]),
    ((2, [3, 8], [5, 1]), [5, 5]),
    ((2, [3, 8], [5, 10]), [5, 8]),
    ((1, [], [4, 2, 9]), [4, 4, 9]),
    ((3, [4, 5, 8, 2], [3, 10]), [4, 5]),
    ((2, [-1], [-1, -2]), [-1, -1]),
]
for index, ((k, nums, values), expected) in enumerate(cases):
    check(index + 1, lambda: run(k, nums, values), expected)

# Performance test: k = 1,000, starting values 0..49,999 in a scrambled order
# ((i * 7,919) % 50,000), then add(50,000), add(50,001), ... 50,000 times.
# After adding 50,000 + i the stream holds 0..50,000 + i, so the k-th largest
# is 50,000 + i - 999.
# Budget: 1.0s. Execution service: size-k heap solution ~0.07s; sorting the
# whole stream on every add is interrupted at the budget.
n = 50_000
start = [(i * 7_919) % n for i in range(n)]
adds = list(range(n, 2 * n))
check(7, lambda: run(1_000, start, adds), [v - 999 for v in adds], time_budget=1.0)


sys.stdout.write(json.dumps(results))
