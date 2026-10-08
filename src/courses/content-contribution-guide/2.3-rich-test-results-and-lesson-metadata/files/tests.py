import sys
import json
import time

from unittest.mock import patch
patch('builtins.print').start()

import main

results = {}


def check(test_id, call, expected, time_budget=None):
    """Runs one test and records a rich result: got/expected as Python reprs,
    the exception if the learner's code raised, or timed_out if it ran longer
    than time_budget seconds."""
    try:
        start = time.perf_counter()
        got = call()
        elapsed = time.perf_counter() - start
    except Exception as e:
        results[test_id] = {
            "passed": False,
            "error": f"{type(e).__name__}: {e}",
            "expected": repr(expected),
        }
        return
    if time_budget is not None and elapsed > time_budget:
        results[test_id] = {"passed": False, "timed_out": True}
        return
    results[test_id] = {
        "passed": got == expected,
        "got": repr(got),
        "expected": repr(expected),
    }


cases = [
    (([1, 4, 6, 2], 8), True),
    (([1, 2, 3], 7), False),
    (([5, 5], 10), True),
    (([5], 10), False),
    (([], 0), False),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.has_pair_with_sum(*args), expected)

# Performance test: 100,000 distinct even numbers, odd target, so no pair
# exists and every element must be examined. Generated deterministically.
# Budget: 1.0s. Measured locally (Python 3.12, laptop): set-based solution
# ~0.01s; nested-loop solution doesn't finish in minutes. Calibrate against
# the execution service and record its timings here.
big = list(range(0, 200_000, 2))
check(6, lambda: main.has_pair_with_sum(big, 7), False, time_budget=1.0)

sys.stdout.write(json.dumps(results))
