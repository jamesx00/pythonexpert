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


def run(operations):
    """Runs operations on a new MinHeap and returns what each pop, peek, len,
    list (a copy of _heap) and valid (heap property holds) step observed.
    A pop that raises IndexError records "IndexError"."""
    heap = main.MinHeap()
    observed = []
    for op, *args in operations:
        if op == "push":
            heap.push(*args)
        elif op == "pop":
            try:
                observed.append(heap.pop())
            except IndexError:
                observed.append("IndexError")
        elif op == "peek":
            observed.append(heap.peek())
        elif op == "len":
            observed.append(len(heap))
        elif op == "list":
            observed.append(list(heap._heap))
        elif op == "valid":
            items = heap._heap
            observed.append(all(items[(i - 1) // 2] <= items[i] for i in range(1, len(items))))
    return observed


def imports_heapq():
    for node in ast.walk(ast.parse(inspect.getsource(main))):
        if isinstance(node, ast.Import) and any(a.name == "heapq" for a in node.names):
            return True
        if isinstance(node, ast.ImportFrom) and node.module == "heapq":
            return True
    return False


cases = [
    ([('push', 5), ('push', 3), ('push', 8), ('push', 1), ('list',)], [[1, 3, 8, 5]]),
    ([('push', 7), ('push', 2), ('push', 9), ('peek',), ('len',)], [2, 3]),
    ([('push', 5), ('push', 3), ('push', 8), ('push', 1), ('push', 9), ('push', 2), ('pop',), ('pop',), ('pop',), ('pop',), ('pop',), ('pop',)], [1, 2, 3, 5, 8, 9]),
    ([('push', 5), ('push', 3), ('push', 8), ('push', 1), ('pop',), ('list',)], [1, [3, 5, 8]]),
    ([('push', 2), ('push', 2), ('push', 1), ('push', 1), ('pop',), ('pop',), ('pop',), ('pop',)], [1, 1, 2, 2]),
    ([('push', 4), ('push', 1), ('pop',), ('push', 3), ('push', 0), ('pop',), ('pop',), ('pop',)], [1, 0, 3, 4]),
    ([('pop',), ('push', 1), ('pop',), ('pop',)], ['IndexError', 1, 'IndexError']),
    ([('push', 10), ('push', 9), ('push', 8), ('push', 7), ('push', 6), ('push', 5), ('push', 4), ('push', 3), ('push', 2), ('push', 1), ('valid',), ('peek',)], [True, 1]),
]
for index, (operations, expected) in enumerate(cases):
    check(index + 1, lambda: run(operations), expected)
check(9, imports_heapq, False)


def push_then_pop_all(values):
    heap = main.MinHeap()
    for value in values:
        heap.push(value)
    return [heap.pop() for _ in range(len(values))]


# Performance test: (i * 7919) % 30011 for i in range(30011) is every number
# from 0 to 30,010 exactly once (30,011 is prime), in shuffled order, so
# popping everything returns 0, 1, ..., 30,010.
# Budget: 1.0s. Execution service: sift-up/sift-down heap ~0.20s. A list
# kept sorted with .sort() on every push and pop(0), and min() + remove()
# on every pop, are both interrupted at the budget.
big = [(i * 7919) % 30011 for i in range(30011)]
check(10, lambda: push_then_pop_all(big), list(range(30011)), time_budget=1.0)

sys.stdout.write(json.dumps(results))
