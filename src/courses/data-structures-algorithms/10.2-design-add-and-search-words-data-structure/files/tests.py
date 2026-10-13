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
    """Runs ("add_word", word) and ("search", pattern) calls on a new
    WordDictionary and returns what each search call returned, in order
    (add_word calls are not recorded)."""
    dictionary = main.WordDictionary()
    returned = []
    for method, arg in operations:
        if method == "add_word":
            dictionary.add_word(arg)
        else:
            returned.append(dictionary.search(arg))
    return returned


cases = [
    ([("add_word", "dog"), ("search", "dog")], [True]),
    ([("add_word", "dog"), ("search", "cat")], [False]),
    ([("add_word", "dog"), ("search", ".og")], [True]),
    ([("add_word", "dog"), ("search", "d.g"), ("search", "do.")], [True, True]),
    ([("add_word", "bear"), ("add_word", "beat"), ("search", "bea."), ("search", "bean")], [True, False]),
    ([("add_word", "a"), ("search", "."), ("search", "..")], [True, False]),
    ([("search", "...")], [False]),
    ([("add_word", "card"), ("search", "car"), ("search", "car."), ("search", "...")], [False, True, False]),
    ([("add_word", "ab"), ("add_word", "cd"), ("search", "a."), ("search", ".d"), ("search", "c.d")], [True, True, False]),
]
for index, (operations, expected) in enumerate(cases):
    check(index + 1, lambda: run(operations), expected)


# Performance test: add all 10,000 four-letter words over the letters a-j
# (word i is i written in base 10 with the digits spelled a-j), then make
# 4,000 searches, each with two dots: 2,000 patterns like "b.c." or "..cd"
# that match, and 2,000 like "bz.." or "..zd" with a "z" that match nothing.
# Budget: 1.0s. Execution service: trie ~0.05s; comparing the pattern with
# every stored word is interrupted at the budget.
def word(i):
    return "".join("abcdefghij"[int(d)] for d in str(i).zfill(4))


n = 10_000
big = [("add_word", word(i)) for i in range(n)]
for i in range(2_000):
    w = word(5 * i)
    if i % 2:
        big += [("search", w[0] + "." + w[2] + "."), ("search", w[0] + "z..")]
    else:
        big += [("search", ".." + w[2:]), ("search", "..z" + w[3])]
check(10, lambda: run(big), [True, False] * 2_000, time_budget=1.0)

sys.stdout.write(json.dumps(results))
