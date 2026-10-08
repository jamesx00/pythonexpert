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
    """Runs ("set", key, value, timestamp) and ("get", key, timestamp) calls on
    a new TimeMap and returns what each get() returned, in order."""
    store = main.TimeMap()
    returned = []
    for op in operations:
        if op[0] == "set":
            store.set(*op[1:])
        else:
            returned.append(store.get(*op[1:]))
    return returned


temp = [("set", "temp", "72F", 1), ("set", "temp", "75F", 4)]
cases = [
    ([("set", "temp", "72F", 1), ("get", "temp", 1)], ["72F"]),
    (temp + [("get", "temp", 2)], ["72F"]),
    (temp + [("get", "temp", 4)], ["75F"]),
    (temp + [("get", "temp", 10)], ["75F"]),
    (temp + [("get", "temp", 0)], [""]),
    ([("get", "missing", 5)], [""]),
    ([("set", "a", "1", 1), ("set", "a", "2", 2), ("set", "a", "3", 3), ("get", "a", 3), ("get", "a", 2)], ["3", "2"]),
]
for index, (operations, expected) in enumerate(cases):
    check(index + 1, lambda: run(operations), expected)

# Performance test: 50,000 sets of one key at timestamps 2, 4, ..., 100,000
# (the value is the timestamp as a string), then 50,000 gets. The latest
# timestamp <= t is t rounded down to even, or none when t < 2.
# Budget: 1.0s. Execution service: bisect solution
# ~0.11s; scanning a key's entries in get() is interrupted at the budget.
big = [("set", "k", str(t), t) for t in range(2, 100_001, 2)]
times = [(i * 7919) % 100_001 for i in range(50_000)]
big += [("get", "k", t) for t in times]
check(8, lambda: run(big), [str(t - t % 2) if t >= 2 else "" for t in times], time_budget=1.0)

sys.stdout.write(json.dumps(results))
