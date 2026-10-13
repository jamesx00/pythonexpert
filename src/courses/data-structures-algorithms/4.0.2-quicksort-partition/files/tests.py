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


def run_partition(nums, lo, hi):
    """Partitions a copy of nums and returns (returned index, list afterwards)."""
    nums = list(nums)
    p = main.partition(nums, lo, hi)
    return p, nums


def partitioned(lo, hi):
    """A normalize function for one case. Any correct partition of lo..hi
    counts: it compares the returned index, the pivot, the items on each side
    (in any order) and the untouched items outside the range."""
    def normalize(result):
        p, nums = result
        return (p, nums[:lo], sorted(nums[lo:p]), nums[p], sorted(nums[p + 1:hi + 1]), nums[hi + 1:])
    return normalize


partition_cases = [
    (([3, 8, 2, 5, 1, 4, 7, 6], 0, 7), (5, [3, 2, 5, 1, 4, 6, 7, 8])),
    (([9, 7, 5, 3, 1], 0, 4), (0, [1, 7, 5, 3, 9])),
    (([1, 2, 3, 4, 5], 0, 4), (4, [1, 2, 3, 4, 5])),
    (([4, 4, 4, 4], 0, 3), (0, [4, 4, 4, 4])),
    (([7], 0, 0), (0, [7])),
    (([10, 3, 9, 1, 8, 2, 0], 1, 5), (2, [10, 1, 2, 3, 8, 9, 0])),
    (([5, -1, 3, -1, 0, 3], 0, 5), (3, [-1, -1, 0, 3, 3, 5])),
]
for index, (args, expected) in enumerate(partition_cases):
    check(index + 1, lambda: run_partition(*args), expected, normalize=partitioned(args[1], args[2]))


def run_quicksort(nums):
    nums = list(nums)
    main.quicksort(nums)
    return nums


quicksort_cases = [
    ([3, 6, 1, 8, 2, 9, 2], [1, 2, 2, 3, 6, 8, 9]),
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
]
for index, (nums, expected) in enumerate(quicksort_cases):
    check(index + 8, lambda: run_quicksort(nums), expected)

check(10, uses_builtin_sort, False)

sys.stdout.write(json.dumps(results))
