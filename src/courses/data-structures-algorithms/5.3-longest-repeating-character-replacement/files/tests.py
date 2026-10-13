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
    (("AABABBA", 1), 4),
    (("ABAB", 2), 4),
    (("AAAA", 0), 4),
    (("ABCDE", 1), 2),
    (("A", 0), 1),
    (("AABBCC", 2), 4),
    (("BAAAB", 2), 5),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.longest_replacement(*args), expected)

# Performance test: "ABAB...", 100,000 characters, with k = 1,000. A window
# of length L holds ceil(L / 2) of one letter, so it needs floor(L / 2)
# changes, and the longest window that needs at most 1,000 is L = 2,001.
# Budget: 1.0s. Execution service: sliding-window solution ~0.12s; extending a window from every
# start index is interrupted at the budget.
big = "AB" * 50_000
check(8, lambda: main.longest_replacement(big, 1_000), 2_001, time_budget=1.0)

sys.stdout.write(json.dumps(results))
