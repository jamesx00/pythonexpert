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


import ast
import inspect


def uses_builtin_sort():
    """True if main.py calls sorted() or a .sort() method anywhere."""
    for node in ast.walk(ast.parse(inspect.getsource(main))):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id == "sorted":
                return True
            if isinstance(node.func, ast.Attribute) and node.func.attr == "sort":
                return True
    return False


merge_cases = [
    (([1, 4, 9], [2, 3, 10]), [1, 2, 3, 4, 9, 10]),
    (([], [1, 2]), [1, 2]),
    (([5], []), [5]),
    (([1, 1, 3], [1, 2]), [1, 1, 1, 2, 3]),
    (([6, 7, 8], [1, 2, 3]), [1, 2, 3, 6, 7, 8]),
]
for index, (args, expected) in enumerate(merge_cases):
    check(index + 1, lambda: main.merge(*args), expected)

sort_cases = [
    ([], []),
    ([1], [1]),
    ([3, 1, 2], [1, 2, 3]),
    ([5, -2, 9, 0, -2, 7], [-2, -2, 0, 5, 7, 9]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ([4, 4, 4, 1], [1, 4, 4, 4]),
]
for index, (nums, expected) in enumerate(sort_cases):
    check(index + 6, lambda: main.merge_sort(nums), expected)


def unchanged_after_sorting():
    nums = [3, 1, 2]
    main.merge_sort(nums)
    return nums


check(13, unchanged_after_sorting, [3, 1, 2])
check(14, uses_builtin_sort, False)

# Performance test: (i * 7919) % 20011 for i in range(20011) is every number
# from 0 to 20,010 exactly once (20,011 is prime), in shuffled order.
# Budget: 1.0s. Execution service: merge sort ~0.10s; insertion sort is
# interrupted at the budget.
big = [(i * 7919) % 20011 for i in range(20011)]
check(15, lambda: main.merge_sort(big), list(range(20011)), time_budget=1.0)

sys.stdout.write(json.dumps(results))
