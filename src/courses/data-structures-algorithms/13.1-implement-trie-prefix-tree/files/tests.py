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
    """Runs ("insert", word), ("search", word) and ("starts_with", prefix)
    calls on a new Trie and returns what each search and starts_with call
    returned, in order (insert calls are not recorded)."""
    trie = main.Trie()
    returned = []
    for method, arg in operations:
        if method == "insert":
            trie.insert(arg)
        else:
            returned.append(getattr(trie, method)(arg))
    return returned


cases = [
    ([("insert", "cat"), ("search", "cat")], [True]),
    ([("insert", "cat"), ("search", "ca"), ("starts_with", "ca")], [False, True]),
    ([("insert", "bat"), ("insert", "bath"), ("search", "bat"), ("search", "bath"), ("search", "ba")], [True, True, False]),
    ([("starts_with", "z")], [False]),
    ([("insert", "apple"), ("insert", "app"), ("search", "app"), ("starts_with", "appl"), ("search", "appl")], [True, True, False]),
    ([("insert", "wolf"), ("insert", "wolf"), ("search", "wolf"), ("starts_with", "wo")], [True, True]),
    ([("insert", "car"), ("search", "cart"), ("starts_with", "cart"), ("starts_with", "car")], [False, False, True]),
]
for index, (operations, expected) in enumerate(cases):
    check(index + 1, lambda: run(operations), expected)


# Performance test: insert 10,000 six-letter words (word i is 97 * i written
# in base 10 with the digits spelled a-j, padded to 6 letters), then make four
# queries per word: search(word) is True, search(word[:5]) is False,
# starts_with(word[:4]) is True and starts_with(word[:3] + "z") is False.
# Budget: 1.0s. Execution service: trie ~0.07s; a set of words plus a scan
# of every word for starts_with is interrupted at the budget.
def word(i):
    return "".join("abcdefghij"[int(d)] for d in str(i).zfill(6))


n = 10_000
words = [word(97 * i) for i in range(n)]
big = [("insert", w) for w in words]
for w in words:
    big += [("search", w), ("search", w[:5]), ("starts_with", w[:4]), ("starts_with", w[:3] + "z")]
check(8, lambda: run(big), [True, False, True, False] * n, time_budget=1.0)

sys.stdout.write(json.dumps(results))
