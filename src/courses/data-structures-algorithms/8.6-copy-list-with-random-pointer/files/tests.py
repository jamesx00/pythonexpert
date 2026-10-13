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


def build_random(values, randoms):
    """Builds a list of main.Node nodes holding values, where node i's random
    pointer goes to node randoms[i] (or None)."""
    nodes = [main.Node(value) for value in values]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    for node, r in zip(nodes, randoms):
        node.random = None if r is None else nodes[r]
    return nodes[0] if nodes else None


def nodes_of(head):
    nodes = []
    seen = set()
    while head is not None and id(head) not in seen:
        seen.add(id(head))
        nodes.append(head)
        head = head.next
    return nodes


def to_pairs(head):
    """Describes a list as (value, index of the random target) pairs."""
    nodes = nodes_of(head)
    position = {id(node): i for i, node in enumerate(nodes)}
    pairs = []
    for node in nodes:
        if node.random is None:
            pairs.append((node.val, None))
        else:
            pairs.append((node.val, position.get(id(node.random), "outside the list")))
    return pairs


def run(head):
    """Copies the list and returns the copy's pairs, or a message if the copy
    shares nodes with the original or the original was changed."""
    originals = {id(node) for node in nodes_of(head)}
    before = to_pairs(head)
    copy = main.copy_random_list(head)
    copied = nodes_of(copy)
    if any(id(node) in originals for node in copied):
        return "the copy reuses nodes from the original list"
    if any(node.random is not None and id(node.random) in originals for node in copied):
        return "a random pointer in the copy points into the original list"
    if to_pairs(head) != before:
        return "the original list was changed"
    return to_pairs(copy)


cases = [
    (([7, 13, 11, 10, 1], [None, 0, 4, 2, 0]), [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)]),
    (([1, 2], [1, 1]), [(1, 1), (2, 1)]),
    (([3], [0]), [(3, 0)]),
    (([], []), []),
    (([5, 6, 7], [None, None, None]), [(5, None), (6, None), (7, None)]),
    (([1, 2, 3, 4], [3, 2, 1, 0]), [(1, 3), (2, 2), (3, 1), (4, 0)]),
]
for index, ((values, randoms), expected) in enumerate(cases):
    check(index + 1, lambda: run(build_random(values, randoms)), expected)

# Performance test: 10,000 nodes holding 0..9,999, where node i's random
# pointer goes to node (i * 7,919) % 10,000. Built outside the budget.
# Budget: 1.0s. Execution service: hash-map solution ~0.06s; finding each
# random target by walking from the head is interrupted at the budget.
n = 10_000
big_randoms = [(i * 7_919) % n for i in range(n)]
big = build_random(list(range(n)), big_randoms)
check(7, lambda: run(big), list(zip(range(n), big_randoms)), time_budget=1.0)


sys.stdout.write(json.dumps(results))
