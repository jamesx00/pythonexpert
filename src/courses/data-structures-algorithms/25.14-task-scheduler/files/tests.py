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
    ((["a", "a", "a", "b", "b"], 2), 7),
    ((["a", "a", "a", "b", "b", "b"], 0), 6),
    ((["a", "a", "a", "a"], 3), 13),
    ((["a"], 5), 1),
    ((["a", "b", "c", "d"], 2), 4),
    ((["a", "a", "b", "b", "c", "c"], 2), 6),
]
for index, ((tasks, n), expected) in enumerate(cases):
    check(index + 1, lambda: main.least_interval(tasks, n), expected)

# Performance test: 10,000 "a" tasks plus one each of "b".."z", with n = 1,000.
# The "a"s need 9,999 gaps of 1,000 slots each, so the answer is
# 9,999 * 1,001 + 1 = 10,009,000 slots.
# Budget: 1.0s. Execution service: counting solution ~0.001s; a heap
# simulation that jumps over idle stretches ~0.01s; simulating the schedule
# one slot at a time is interrupted at the budget.
big = ["a"] * 10_000 + [chr(c) for c in range(ord("b"), ord("z") + 1)]
check(7, lambda: main.least_interval(big, 1_000), 10_009_000, time_budget=1.0)


sys.stdout.write(json.dumps(results))
