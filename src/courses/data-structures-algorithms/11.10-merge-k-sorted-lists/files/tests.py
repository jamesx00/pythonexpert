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


def build(values):
    """Builds a linked list of main.ListNode nodes holding values."""
    head = None
    for value in reversed(values):
        head = main.ListNode(value, head)
    return head


def to_list(node):
    """Reads the values from node onward. A loop is shown as "<cycle>"
    instead of being followed forever."""
    values = []
    seen = set()
    while node is not None:
        if id(node) in seen:
            values.append("<cycle>")
            break
        seen.add(id(node))
        values.append(node.val)
        node = node.next
    return values


cases = [
    ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
    ([], []),
    ([[]], []),
    ([[5]], [5]),
    ([[1, 2, 3], []], [1, 2, 3]),
    ([[9], [1, 5], [2, 3, 7]], [1, 2, 3, 5, 7, 9]),
]
for index, (lists, expected) in enumerate(cases):
    check(index + 1, lambda: to_list(main.merge_k_lists([build(values) for values in lists])), expected)

# Performance test: 1,000 lists of 50 nodes each, where list j holds
# j, j + 1,000, j + 2,000, ..., so the merged list is 0..49,999. Built
# outside the budget.
# Budget: 1.0s. Execution service: heap solution ~0.08s; merging the lists
# into the result one at a time is interrupted at the budget.
k = 1_000
big = [build(list(range(j, 50_000, k))) for j in range(k)]
check(7, lambda: to_list(main.merge_k_lists(big)), list(range(50_000)), time_budget=1.0)


sys.stdout.write(json.dumps(results))
