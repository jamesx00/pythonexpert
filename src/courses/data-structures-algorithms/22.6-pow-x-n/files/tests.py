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


def approx(value):
    # Floating-point results can differ in the last few digits depending on
    # the order of the multiplications, so compare them rounded.
    return round(value, 6)


cases = [
    ((2.0, 10), 1024.0),
    ((2.0, -2), 0.25),
    ((2.1, 3), 9.261),
    ((5.0, 0), 1.0),
    ((1.0, 1000), 1.0),
    ((-2.0, 3), -8.0),
    ((0.5, 4), 0.0625),
    ((-3.0, -3), -0.037037),
]
for index, ((x, n), expected) in enumerate(cases):
    check(index + 1, lambda: main.my_pow(x, n), expected, normalize=approx)

# Performance test: n = 1,000,000,000. (1 + 1/n) ** n is close to e.
# Budget: 1.0s. Execution service: squaring under 0.01s; multiplying x into
# the result n times is interrupted at the budget.
check(9, lambda: main.my_pow(1.000000001, 1_000_000_000), 2.718282, time_budget=1.0, normalize=approx)

sys.stdout.write(json.dumps(results))
