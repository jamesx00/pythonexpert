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


def run(n, steps):
    """Creates UnionFind(n), runs each (operation, a, b) step and returns
    what each call returned, in order."""
    uf = main.UnionFind(n)
    returned = []
    for op, a, b in steps:
        if op == "union":
            returned.append(uf.union(a, b))
        else:
            returned.append(uf.connected(a, b))
    return returned


cases = [
    ((3, [("union", 0, 1), ("connected", 0, 1), ("connected", 0, 2)]), [True, True, False]),
    ((3, [("union", 0, 1), ("union", 1, 2), ("connected", 0, 2), ("union", 0, 2)]), [True, True, True, False]),
    ((2, [("connected", 0, 1), ("union", 1, 0), ("connected", 1, 0)]), [False, True, True]),
    ((6, [("union", 0, 1), ("union", 2, 3), ("union", 4, 5), ("connected", 1, 2), ("union", 1, 3), ("connected", 0, 2), ("connected", 0, 4)]), [True, True, True, False, True, True, False]),
    ((4, [("union", 0, 0), ("union", 3, 2), ("union", 2, 3), ("connected", 3, 3)]), [False, True, False, True]),
]
for index, ((n, steps), expected) in enumerate(cases):
    check(index + 1, lambda: run(n, steps), expected)

# Performance test: 800 items joined into one group by union(i, i + 1), then
# 100,000 connected(0, 799) calls. Linking a's root under b's root makes the
# group a single 800-long chain from 0 up to the root 799.
# Budget: 1.0s. Execution service: find with path compression ~0.07s;
# find without path compression, which walks the whole chain on every call,
# is interrupted at the budget.
n = 800
big = [("union", i, i + 1) for i in range(n - 1)] + [("connected", 0, n - 1)] * 100_000
check(6, lambda: run(n, big), [True] * (n - 1) + [True] * 100_000, time_budget=1.0)

sys.stdout.write(json.dumps(results))
