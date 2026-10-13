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
    (3, 5, 8),
    (-2, 3, 1),
    (0, 0, 0),
    (-5, -7, -12),
    (12, -12, 0),
    (100, 250, 350),
    (-1, 1, 0),
    (5, -9, -4),
    (2147483647, -1, 2147483646),
    (1073741824, 1073741823, 2147483647),
    (-2147483648, 2147483647, -1),
    (-2147483648, 0, -2147483648),
]
for index, (a, b, expected) in enumerate(cases):
    # Without the 32-bit mask, the carry loop never ends when one number is
    # negative and the sum isn't (tests 2, 5, 7 and 9): the carry keeps
    # moving left through Python's endless sign bits. A short budget reports
    # that as too slow instead of the whole run being killed.
    # Budget: 0.25s. Execution service: masked loop BENCH_EFF per test.
    check(index + 1, lambda: main.sum_of_two(a, b), expected, time_budget=0.25)

sys.stdout.write(json.dumps(results))
