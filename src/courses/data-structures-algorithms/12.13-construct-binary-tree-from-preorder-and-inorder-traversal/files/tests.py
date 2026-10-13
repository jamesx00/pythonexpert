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


from collections import deque


def build(values):
    """Builds a tree of main.TreeNode nodes from a level-order list, where
    None marks a missing child."""
    if not values or values[0] is None:
        return None
    root = main.TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = main.TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = main.TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def to_list(root):
    """Reads a tree back into a level-order list with None for missing
    children, trailing Nones trimmed. A node reached twice is shown as
    "<loop>" instead of being followed forever."""
    values = []
    seen = set()
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
        elif id(node) in seen:
            values.append("<loop>")
        else:
            seen.add(id(node))
            values.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while values and values[-1] is None:
        values.pop()
    return values


cases = [
    (([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]), [3, 9, 20, None, None, 15, 7]),
    (([-1], [-1]), [-1]),
    (([], []), []),
    (([1, 2, 3], [3, 2, 1]), [1, 2, None, 3]),
    (([1, 2, 3], [1, 2, 3]), [1, None, 2, None, 3]),
    (([5, 3, 1, 4, 8, 7, 9], [1, 3, 4, 5, 7, 8, 9]), [5, 3, 8, 1, 4, 7, 9]),
]
for index, ((preorder, inorder), expected) in enumerate(cases):
    check(index + 1, lambda: to_list(main.build_tree_from_traversals(preorder, inorder)), expected)


sys.stdout.write(json.dumps(results))
