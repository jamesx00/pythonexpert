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
    (("plane", "plant"), 1),
    (("abc", "abc"), 0),
    (("", "abc"), 3),
    (("draft", "crate"), 3),
    (("sunday", "saturday"), 3),
    (("a", "b"), 1),
]
for index, ((a, b), expected) in enumerate(cases):
    check(index + 1, lambda: main.edit_distance(a, b), expected)

# Performance test: two 150-character strings over "abcde".
# Budget: 1.0s. Execution service: bottom-up table ~0.014s; memoized
# recursion ~0.017s; recursion without a memo is interrupted at the budget.
a = "".join("abcde"[i * i % 5] for i in range(150))
b = "".join("abcde"[(i * 3 + 1) % 5] for i in range(150))
check(7, lambda: main.edit_distance(a, b), 91, time_budget=1.0)


sys.stdout.write(json.dumps(results))
