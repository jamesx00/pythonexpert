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


def preorder(node):
    if node is None:
        return []
    return [node.key] + preorder(node.left) + preorder(node.right)


def run(keys, operations):
    """Inserts keys into a new BST, then runs operations and returns what
    each inorder, preorder (read from the nodes) and contains step observed."""
    tree = main.BST()
    for key in keys:
        tree.insert(key)
    observed = []
    for op, *args in operations:
        if op == "insert":
            tree.insert(*args)
        elif op == "delete":
            tree.delete(*args)
        elif op == "contains":
            observed.append(tree.contains(*args))
        elif op == "inorder":
            observed.append(tree.inorder())
        elif op == "preorder":
            observed.append(preorder(tree.root))
    return observed


cases = [
    ([5, 3, 8, 1, 4], [('inorder',)], [[1, 3, 4, 5, 8]]),
    ([5, 3, 8, 1, 4], [('preorder',)], [[5, 3, 1, 4, 8]]),
    ([5, 3, 8, 1, 4], [('contains', 4), ('contains', 6)], [True, False]),
    ([], [('contains', 1), ('inorder',)], [False, []]),
    ([5, 5, 3], [('inorder',)], [[3, 5]]),
    ([5, 3, 8, 1, 4], [('delete', 1), ('preorder',)], [[5, 3, 4, 8]]),
    ([5, 3, 8, 1], [('delete', 3), ('preorder',)], [[5, 1, 8]]),
    ([5, 3, 8, 1, 4, 7, 9], [('delete', 3), ('preorder',), ('contains', 3)], [[5, 4, 1, 8, 7, 9], False]),
    ([5, 3, 8, 7, 9, 6], [('delete', 5), ('preorder',)], [[6, 3, 8, 7, 9]]),
    ([5, 3, 8], [('delete', 4), ('preorder',)], [[5, 3, 8]]),
    ([5], [('delete', 5), ('inorder',), ('insert', 2), ('inorder',)], [[], [2]]),

]
for index, (keys, operations, expected) in enumerate(cases):
    check(index + 1, lambda: run(keys, operations), expected)

sys.stdout.write(json.dumps(results))
