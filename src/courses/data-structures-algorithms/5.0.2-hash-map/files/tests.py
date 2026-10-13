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
    """Runs operations on a new HashMap and returns what each get, len,
    bucket_count and bucket_size step observed. An operation that raises
    KeyError or TypeError records the exception's name."""
    hash_map = main.HashMap()
    observed = []
    for op, *args in operations:
        try:
            if op == "put":
                hash_map.put(*args)
            elif op == "remove":
                hash_map.remove(*args)
            elif op == "get":
                observed.append(hash_map.get(*args))
            elif op == "len":
                observed.append(len(hash_map))
            elif op == "bucket_count":
                observed.append(hash_map.bucket_count())
            elif op == "bucket_size":
                observed.append(len(hash_map._buckets[args[0]]))
        except (KeyError, TypeError) as e:
            observed.append(type(e).__name__)
    return observed


cases = [
    ([('put', 'a', 1), ('put', 'b', 2), ('get', 'a'), ('get', 'b')], [1, 2]),
    ([('put', 'a', 1), ('put', 'a', 5), ('get', 'a'), ('len',)], [5, 1]),
    ([('put', 1, 'one'), ('put', 9, 'nine'), ('put', 17, 'seventeen'), ('get', 9), ('bucket_size', 1)], ['nine', 3]),
    ([('put', 1, 'one'), ('put', 9, 'nine'), ('put', 17, 'seventeen'), ('remove', 9), ('get', 1), ('get', 17), ('len',), ('get', 9)], ['one', 'seventeen', 2, 'KeyError']),
    ([('put', 'a', 1), ('get', 'b'), ('remove', 'b'), ('len',)], ['KeyError', 'KeyError', 1]),
    ([('put', (1, 2), 'x'), ('get', (1, 2))], ['x']),
    ([('put', [1, 2], 'x'), ('len',)], ['TypeError', 0]),
    ([('put', 1, 10), ('bucket_count',), ('put', 9, 90), ('bucket_count',), ('put', 17, 170), ('bucket_count',), ('put', 25, 250), ('bucket_count',), ('put', 33, 330), ('bucket_count',), ('put', 41, 410), ('bucket_count',), ('put', 49, 490), ('bucket_count',)], [8, 8, 8, 8, 8, 8, 16]),
    ([('put', 1, 10), ('put', 9, 90), ('put', 17, 170), ('put', 25, 250), ('put', 33, 330), ('put', 41, 410), ('put', 49, 490), ('bucket_size', 1), ('bucket_size', 9), ('get', 1), ('get', 9), ('get', 17), ('get', 25), ('get', 33), ('get', 41), ('get', 49)], [4, 3, 10, 90, 170, 250, 330, 410, 490]),
]
for index, (operations, expected) in enumerate(cases):
    check(index + 1, lambda: run(operations), expected)


def put_and_get(n):
    hash_map = main.HashMap()
    for i in range(n):
        hash_map.put(i * 7, i)
    return [len(hash_map), sum(hash_map.get(i * 7) for i in range(n))]


# Performance test: 20,000 puts, then a get for every key.
# Budget: 1.0s. Execution service: resizing solution ~0.06s; never resizing
# (8 buckets of 2,500 pairs each) is interrupted at the budget.
check(10, lambda: put_and_get(20_000), [20_000, 199_990_000], time_budget=1.0)

sys.stdout.write(json.dumps(results))
