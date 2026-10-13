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
    ("xyzxyz", 3),
    ("aaaa", 1),
    ("", 0),
    ("pwwkew", 3),
    ("dvdf", 3),
    ("abcdefg", 7),
    ("bbtablud", 6),
]
for index, (s, expected) in enumerate(cases):
    check(index + 1, lambda: main.longest_unique_substring(s), expected)

# Performance test: 100,000 characters cycling through 20,000 distinct
# characters, so every window of 20,000 is repeat-free.
# Budget: 1.0s. Execution service: sliding-window solution ~0.05s; restarting a set from every
# start index is interrupted at the budget.
big = "".join(chr(0x4E00 + i % 20_000) for i in range(100_000))
check(8, lambda: main.longest_unique_substring(big), 20_000, time_budget=1.0)

sys.stdout.write(json.dumps(results))
