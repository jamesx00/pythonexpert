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
    ([11, 15, 19, 2, 5, 8], 2),
    ([1, 2, 3, 4], 1),
    ([4, 1, 2, 3], 1),
    ([3, 4, 1, 2], 1),
    ([2, 3, 4, 1], 1),
    ([9], 9),
    ([2, 1], 1),
]
for index, (nums, expected) in enumerate(cases):
    check(index + 1, lambda: main.find_min(nums), expected)

# Performance test: 5,000 calls on 0, 1, ..., 199,999 rotated so that it
# starts at 123,457. The minimum is always 0.
# Budget: 1.0s. Execution service: binary search
# ~0.02s; min(nums) per call is interrupted at the budget.
big = list(range(123_457, 200_000)) + list(range(123_457))
check(8, lambda: [main.find_min(big) for _ in range(5_000)], [0] * 5_000, time_budget=1.0)

sys.stdout.write(json.dumps(results))
