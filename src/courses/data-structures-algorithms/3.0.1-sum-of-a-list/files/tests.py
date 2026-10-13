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


def calls_itself(name, *args):
    """True if main.<name>(*args) calls itself at least once, through its
    module-level name, before returning."""
    original = getattr(main, name)
    calls = 0

    def counting(*a, **kw):
        nonlocal calls
        calls += 1
        return original(*a, **kw)

    setattr(main, name, counting)
    try:
        counting(*args)
    finally:
        setattr(main, name, original)
    return calls > 1


cases = [
    ([[]], 0),
    ([[5]], 5),
    ([[1, 2, 3, 4]], 10),
    ([[-3, 7, -1]], 3),
    ([[0, 0, 0]], 0),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.sum_list(*args), expected)

check(6, lambda: main.sum_list(list(range(500))), 124750)
check(7, lambda: calls_itself("sum_list", [1, 2, 3]), True)

sys.stdout.write(json.dumps(results))
