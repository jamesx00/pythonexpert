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


from itertools import product

cases = [
    (("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5),
    (("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0),
    (("a", "c", ["a", "b", "c"]), 2),
    (("hot", "dog", ["hot", "dog"]), 0),
    (("hot", "dog", ["hot", "dot", "dog"]), 3),
    (("cat", "cat", ["cat"]), 1),
    (("same", "cost", []), 0),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.ladder_length(*args), expected)

# Performance test: all 3,125 five-letter words made of the letters a-e,
# from "aaaaa" to "eeeee". Each step changes one letter, so the shortest
# ladder changes all 5 letters: 6 words. Built outside the budget.
# Budget: 1.0s. Execution service: BFS trying every one-letter change
# ~0.14s; comparing every pair of words to find neighbours is interrupted at
# the budget.
big = ["".join(letters) for letters in product("abcde", repeat=5)]
check(8, lambda: main.ladder_length("aaaaa", "eeeee", big), 6, time_budget=1.0)

sys.stdout.write(json.dumps(results))
