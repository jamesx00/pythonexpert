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
    (("xcaxcxaxxc", "xc"), 8),
    (("mississippi", "mis"), 6),
    (("abc", "abc"), 1),
    (("abc", "abcd"), 0),
    (("aaaa", "aa"), 6),
    (("", "a"), 0),
]
for index, ((s, t), expected) in enumerate(cases):
    check(index + 1, lambda: main.num_distinct(s, t), expected)

# Performance test: s is 200 "a"s, t is 10 "a"s (200 choose 10 ways).
# Budget: 1.0s. Execution service: bottom-up table ~0.001s; memoized
# recursion ~0.002s; recursion without a memo is interrupted at the budget.
check(7, lambda: main.num_distinct("a" * 200, "a" * 10), 22451004309013280, time_budget=1.0)


sys.stdout.write(json.dumps(results))
