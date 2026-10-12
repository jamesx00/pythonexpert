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


def normalize(subsets):
    return sorted(sorted(subset) for subset in subsets)


cases = [
    ([1, 2, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]),
    ([0], [[], [0]]),
    ([], [[]]),
    ([4, 4, 4], [[], [4], [4, 4], [4, 4, 4]]),
    ([1, 2, 3], [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
    ([2, 1, 2, 1], [[], [1], [2], [1, 1], [1, 2], [2, 2], [1, 1, 2], [1, 2, 2], [1, 1, 2, 2]]),
]
for index, (nums, expected) in enumerate(cases):
    check(index + 1, lambda: main.subsets_with_dup(nums), expected, normalize=normalize)

# Performance test: 22 values, [1, 2] repeated 11 times. A distinct subset is
# just a count of 1s (0 to 11) and a count of 2s (0 to 11), so there are only
# 144 of them, out of 2 ** 22 (about 4 million) ways to pick positions.
# Budget: 1.0s. Execution service: sort + skip duplicates under 0.001s;
# building all 2 ** 22 subsets and removing duplicates with a set is
# interrupted at the budget.
big = [1, 2] * 11
expected_big = [[1] * ones + [2] * twos for ones in range(12) for twos in range(12)]
check(7, lambda: main.subsets_with_dup(big), expected_big, time_budget=1.0, normalize=normalize)

sys.stdout.write(json.dumps(results))
