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
    (([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]]),
    (([2], 1), []),
    (([1, 1, 1], 2), [[1, 1]]),
    (([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
    (([3, 3, 3], 9), [[3, 3, 3]]),
    (([4, 8], 20), []),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.combination_sum2(*args), expected, normalize=normalize)

# Performance test: 30 candidates, fifteen 1s, ten 2s and five 3s, with
# target 15. A combination is just how many 3s and 2s it uses, with 1s
# filling the rest, so there are only 27 of them.
# Budget: 1.0s. Execution service: sort + skip duplicates under 0.001s;
# picking positions without the duplicate skip and removing duplicates with
# a set at the end is interrupted at the budget.
big = [1] * 15 + [2] * 10 + [3] * 5
expected_big = [
    [1] * (15 - 2 * twos - 3 * threes) + [2] * twos + [3] * threes
    for threes in range(6)
    for twos in range(11)
    if 15 - 2 * twos - 3 * threes >= 0
]
check(7, lambda: main.combination_sum2(big, 15), expected_big, time_budget=1.0, normalize=normalize)

sys.stdout.write(json.dumps(results))
