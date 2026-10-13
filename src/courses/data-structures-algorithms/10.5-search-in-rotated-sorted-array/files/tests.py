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
    (([30, 40, 50, 5, 10, 20], 10), 4),
    (([30, 40, 50, 5, 10, 20], 100), -1),
    (([4, 5, 6, 7, 0, 1, 2], 0), 4),
    (([4, 5, 6, 7, 0, 1, 2], 3), -1),
    (([1], 1), 0),
    (([1], 0), -1),
    (([5, 1, 3], 5), 0),
    (([1, 2, 3, 4, 5], 5), 4),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.search_rotated(*args), expected)

# Performance test: 20,000 searches in 0, 1, ..., 199,999 rotated so that it
# starts at 123,457. Value q < 200,000 sits at index (q - 123,457) % 200,000;
# larger values are missing.
# Budget: 1.0s. Execution service: binary search
# ~0.1s; `nums.index(target)` per search is interrupted at the budget.
big = list(range(123_457, 200_000)) + list(range(123_457))
queries = [(i * 7919) % 220_000 for i in range(20_000)]
check(
    9,
    lambda: [main.search_rotated(big, q) for q in queries],
    [(q - 123_457) % 200_000 if q < 200_000 else -1 for q in queries],
    time_budget=1.0,
)

sys.stdout.write(json.dumps(results))
