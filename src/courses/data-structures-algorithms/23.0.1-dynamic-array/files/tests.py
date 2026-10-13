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


def run(operations):
    """Runs (method, argument) operations on a new DynamicArray and returns
    what each get, len, capacity and block (slots in _data) step observed.
    A get that raises IndexError records "IndexError"."""
    array = main.DynamicArray()
    observed = []
    for op, *args in operations:
        if op == "append":
            array.append(*args)
        elif op == "insert_front":
            array.insert_front(*args)
        elif op == "get":
            try:
                observed.append(array.get(*args))
            except IndexError:
                observed.append("IndexError")
        elif op == "len":
            observed.append(len(array))
        elif op == "capacity":
            observed.append(array.capacity())
        elif op == "block":
            observed.append(len(array._data))
    return observed


cases = [
    ([('append', 10), ('append', 20), ('append', 30), ('get', 0), ('get', 1), ('get', 2)], [10, 20, 30]),
    ([('append', 'a'), ('capacity',), ('append', 'b'), ('capacity',), ('append', 'c'), ('capacity',), ('append', 'd'), ('capacity',), ('append', 'e'), ('capacity',)], [1, 2, 4, 4, 8]),
    ([('append', 1), ('append', 2), ('append', 3), ('append', 4), ('append', 5), ('len',), ('block',)], [5, 8]),
    ([('append', 2), ('append', 3), ('insert_front', 1), ('get', 0), ('get', 1), ('get', 2), ('len',)], [1, 2, 3, 3]),
    ([('insert_front', 'a'), ('append', 'b'), ('insert_front', 'z'), ('get', 0), ('get', 1), ('get', 2), ('capacity',)], ['z', 'a', 'b', 4]),
    ([('append', 7), ('append', 8), ('get', 2), ('get', -1)], ['IndexError', 'IndexError']),
]
for index, (operations, expected) in enumerate(cases):
    check(index + 1, lambda: run(operations), expected)


def append_many(n):
    array = main.DynamicArray()
    for i in range(n):
        array.append(i)
    return [len(array), array.capacity(), array.get(0), array.get(n - 1)]


# Performance test: 200,000 appends to one array.
# Budget: 1.0s. Execution service: doubling solution ~0.09s; growing the
# block by one slot per resize (a full copy on every append) is interrupted
# at the budget.
check(7, lambda: append_many(200_000), [200_000, 262_144, 0, 199_999], time_budget=1.0)

sys.stdout.write(json.dumps(results))
