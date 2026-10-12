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


def normalize(combinations):
    return sorted(sorted(combination) for combination in combinations)


cases = [
    (([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    (([2], 1), []),
    (([1], 3), [[1, 1, 1]]),
    (([3, 4, 6], 12), [[3, 3, 3, 3], [3, 3, 6], [4, 4, 4], [6, 6]]),
    (([7, 11], 5), []),
    (([2, 4], 8), [[2, 2, 2, 2], [2, 2, 4], [4, 4]]),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.combination_sum(*args), expected, normalize=normalize)

# Performance test: candidates [2, 3, 5, 7] and target 50. There are only
# 158 combinations: for each count of 7s, 5s and 3s, the rest must be an
# even number, filled with 2s.
# Budget: 1.0s. Execution service: backtracking with a start index ~0.001s;
# trying every ordering and removing duplicates with a set is interrupted at
# the budget.
expected_big = [
    [2] * (rest // 2) + [3] * threes + [5] * fives + [7] * sevens
    for sevens in range(50 // 7 + 1)
    for fives in range((50 - 7 * sevens) // 5 + 1)
    for threes in range((50 - 7 * sevens - 5 * fives) // 3 + 1)
    for rest in [50 - 7 * sevens - 5 * fives - 3 * threes]
    if rest % 2 == 0
]
check(7, lambda: main.combination_sum([2, 3, 5, 7], 50), expected_big, time_budget=1.0, normalize=normalize)

sys.stdout.write(json.dumps(results))
