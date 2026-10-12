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
    (("abc", "def", "adbcef"), True),
    (("abc", "def", "abdecf"), True),
    (("", "", ""), True),
    (("abc", "", "abc"), True),
    (("aabcc", "dbbca", "aadbbbaccc"), False),
    (("ab", "bc", "babc"), True),
    (("ab", "ac", "acab"), True),
]
for index, ((s1, s2, s3), expected) in enumerate(cases):
    check(index + 1, lambda: main.is_interleave(s1, s2, s3), expected)

# Performance test: s1 and s2 are 100 "a"s each, s3 is 199 "a"s then a "b".
# Every way of interleaving the "a"s fails only at the last character.
# Budget: 1.0s. Execution service: bottom-up table ~0.003s; memoized
# recursion ~0.008s; recursion without a memo is interrupted at the budget.
check(8, lambda: main.is_interleave("a" * 100, "a" * 100, "a" * 199 + "b"), False, time_budget=1.0)


sys.stdout.write(json.dumps(results))
