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
    """Runs (method, argument) pairs on a new MinStack and returns what each
    top() and get_min() call returned, in order."""
    stack = main.MinStack()
    returned = []
    for op, arg in operations:
        if op == "push":
            stack.push(arg)
        elif op == "pop":
            stack.pop()
        else:
            returned.append(getattr(stack, op)())
    return returned


cases = [
    ([("push", 5), ("push", 3), ("push", 7), ("get_min", None)], [3]),
    ([("push", 5), ("push", 3), ("push", 7), ("pop", None), ("get_min", None)], [3]),
    ([("push", 5), ("push", 3), ("push", 7), ("pop", None), ("pop", None), ("get_min", None)], [5]),
    ([("push", -2), ("push", 0), ("push", -3), ("get_min", None), ("pop", None), ("top", None), ("get_min", None)], [-3, 0, -2]),
    ([("push", 1), ("push", 1), ("push", 1), ("get_min", None), ("pop", None), ("get_min", None), ("pop", None), ("get_min", None)], [1, 1, 1]),
    ([("push", 4), ("top", None), ("get_min", None)], [4, 4]),
]
for index, (operations, expected) in enumerate(cases):
    check(index + 1, lambda: run(operations), expected)

# Performance test: push 100,000, 99,999, ..., 1, calling get_min() after
# each push, so each call returns the value just pushed.
# Budget: 1.0s. Execution service: min-stack solution ~0.07s; calling
# min() over the whole stack in get_min() is interrupted at the budget.
big = []
for value in range(100_000, 0, -1):
    big += [("push", value), ("get_min", None)]
check(7, lambda: run(big), list(range(100_000, 0, -1)), time_budget=1.0)

sys.stdout.write(json.dumps(results))
