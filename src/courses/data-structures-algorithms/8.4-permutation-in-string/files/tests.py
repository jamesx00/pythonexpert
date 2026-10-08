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
    (("abc", "eidbacoo"), True),
    (("abc", "eidboaoo"), False),
    (("ab", "eidbaaooo"), True),
    (("adc", "dcda"), True),
    (("xyz", "xy"), False),
    (("a", "a"), True),
    (("hello", "ooolleoooleh"), False),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.contains_permutation(*args), expected)

# Performance test: a 1,000-letter pattern (500 "a" and 500 "b") and a
# 100,000-letter text that is all "a", so no window matches.
# Budget: 1.0s. Execution service: sliding-count solution ~0.16s;
# sorting every window is interrupted at the budget.
big_pattern = "a" * 500 + "b" * 500
big_text = "a" * 100_000
check(8, lambda: main.contains_permutation(big_pattern, big_text), False, time_budget=1.0)

sys.stdout.write(json.dumps(results))
