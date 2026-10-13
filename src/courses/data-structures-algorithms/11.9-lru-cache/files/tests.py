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


def run(capacity, operations):
    """Runs ("put", key, value) and ("get", key) calls on a new LRUCache and
    returns what each call returned, in order (None for put)."""
    cache = main.LRUCache(capacity)
    returned = []
    for op in operations:
        if op[0] == "put":
            returned.append(cache.put(op[1], op[2]))
        else:
            returned.append(cache.get(op[1]))
    return returned


cases = [
    ((2, [("put", 1, 10), ("put", 2, 20), ("get", 1), ("put", 3, 30), ("get", 2), ("get", 3)]), [None, None, 10, None, -1, 30]),
    ((1, [("put", 1, 1), ("get", 1), ("put", 2, 2), ("get", 1), ("get", 2)]), [None, 1, None, -1, 2]),
    ((2, [("put", 1, 1), ("put", 2, 2), ("put", 3, 3), ("get", 1), ("get", 3)]), [None, None, None, -1, 3]),
    ((3, [("put", 1, 1), ("put", 2, 2), ("get", 1), ("put", 3, 3), ("put", 4, 4), ("get", 2), ("get", 1), ("get", 4)]), [None, None, 1, None, None, -1, 1, 4]),
    ((2, [("get", 1), ("put", 1, 100), ("get", 1)]), [-1, None, 100]),
    ((2, [("put", 1, 1), ("put", 1, 2), ("get", 1)]), [None, None, 2]),
]
for index, ((capacity, operations), expected) in enumerate(cases):
    check(index + 1, lambda: run(capacity, operations), expected)

# Performance test: capacity 30,000. Put keys 0..29,999 (value = key), get
# them back from 29,999 down to 0 (so key 29,999 becomes the least recently
# used), put 30,000 new keys (each evicts one old key), then get 0 and 59,999.
# Budget: 1.0s. Execution service: OrderedDict / linked-list solution
# ~0.05s; keeping the usage order in a plain list (list.remove on every
# get) is interrupted at the budget.
n = 30_000
big = [("put", k, k) for k in range(n)]
big += [("get", k) for k in range(n - 1, -1, -1)]
big += [("put", k, k) for k in range(n, 2 * n)]
big += [("get", 0), ("get", 2 * n - 1)]
expected = [None] * n + list(range(n - 1, -1, -1)) + [None] * n + [-1, 2 * n - 1]
check(7, lambda: run(n, big), expected, time_budget=1.0)


sys.stdout.write(json.dumps(results))
