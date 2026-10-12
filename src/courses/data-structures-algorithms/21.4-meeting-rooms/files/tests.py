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
    ([[0, 30], [5, 10], [15, 20]], False),
    ([[7, 10], [2, 4]], True),
    ([], True),
    ([[1, 5]], True),
    ([[1, 5], [5, 8]], True),
    ([[1, 5], [4, 8]], False),
    ([[3, 6], [9, 12], [1, 2]], True),
]
for index, (intervals, expected) in enumerate(cases):
    check(index + 1, lambda: main.can_attend_all_meetings(intervals), expected)

# Performance test: 100,000 meetings [2i, 2i + 1] for i in range(100,000),
# shuffled by a fixed permutation. None overlap, so every pair has to be
# ruled out.
# Budget: 1.0s. Execution service: sort-then-compare-neighbours solution
# ~0.05s; checking every pair is interrupted at the budget.
slots = [[2 * i, 2 * i + 1] for i in range(100_000)]
big = [slots[(j * 7919) % 100_000] for j in range(100_000)]
check(8, lambda: main.can_attend_all_meetings(big), True, time_budget=1.0)


sys.stdout.write(json.dumps(results))
