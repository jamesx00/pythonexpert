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
    ((2, [[1, 0]]), True),
    ((2, [[1, 0], [0, 1]]), False),
    ((4, [[1, 0], [2, 1], [3, 2]]), True),
    ((3, [[0, 1], [1, 2], [2, 0]]), False),
    ((1, []), True),
    ((5, [[1, 0], [2, 0], [3, 1], [3, 2]]), True),
    ((2, []), True),
    ((1, [[0, 0]]), False),
    ((5, [[1, 0], [2, 1], [4, 3], [3, 4]]), False),
]
for index, ((num_courses, prerequisites), expected) in enumerate(cases):
    check(index + 1, lambda: main.can_finish(num_courses, prerequisites), expected)

# Performance test: 20,000 courses in 50 separate chains of 400. In each
# chain, course i needs courses i + 1 and i + 2, so the last course of a
# chain must come first. No cycles, so the answer is True. Chains of 400
# keep a recursive DFS well inside Python's recursion limit.
# Budget: 1.0s. Execution service: DFS with visiting/done states ~0.03s;
# taking the courses whose prerequisites are done, one pass over all
# courses at a time (400 passes), is interrupted at the budget, and so is a
# DFS that forgets which courses are already done.
chains, length = 50, 400
big = []
for start in range(0, chains * length, length):
    for i in range(start, start + length - 1):
        big.append([i, i + 1])
        if i + 2 < start + length:
            big.append([i, i + 2])
check(10, lambda: main.can_finish(chains * length, big), True, time_budget=1.0)

sys.stdout.write(json.dumps(results))
