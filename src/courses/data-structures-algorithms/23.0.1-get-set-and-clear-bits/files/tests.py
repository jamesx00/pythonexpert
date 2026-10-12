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
    ("get_bit", 5, 0, 1),
    ("get_bit", 5, 1, 0),
    ("get_bit", 8, 3, 1),
    ("set_bit", 5, 1, 7),
    ("set_bit", 5, 2, 5),
    ("set_bit", 0, 4, 16),
    ("clear_bit", 5, 0, 4),
    ("clear_bit", 5, 1, 5),
    ("clear_bit", 255, 7, 127),
    ("get_bit", 8, 10, 0),
    ("set_bit", 0, 40, 1099511627776),
    ("clear_bit", 1099511627777, 40, 1),
]
for index, (name, x, i, expected) in enumerate(cases):
    check(index + 1, lambda: getattr(main, name)(x, i), expected)

sys.stdout.write(json.dumps(results))
