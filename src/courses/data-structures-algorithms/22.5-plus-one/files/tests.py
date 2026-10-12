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
    ([1, 2, 9], [1, 3, 0]),
    ([9, 9], [1, 0, 0]),
    ([1, 2, 3], [1, 2, 4]),
    ([0], [1]),
    ([4, 3, 2, 9], [4, 3, 3, 0]),
    ([9], [1, 0]),
    ([8, 9, 9, 9], [9, 0, 0, 0]),
]
for index, (digits, expected) in enumerate(cases):
    check(index + 1, lambda: main.plus_one(digits), expected)

# Performance test: 300,000 digits, a 1 followed by 299,999 nines. Every 9
# turns into a 0 and the 1 becomes a 2.
# Budget: 1.0s. Execution service: carrying from the right ~0.02s; turning
# the digits into an int and back (quadratic in the number of digits) is
# interrupted at the budget.
big = [1] + [9] * 299_999
check(8, lambda: main.plus_one(big), [2] + [0] * 299_999, time_budget=1.0)

sys.stdout.write(json.dumps(results))
