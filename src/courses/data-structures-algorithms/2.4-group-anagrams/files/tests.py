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


def normalize(groups):
    return sorted(sorted(group) for group in groups)


cases = [
    (["bat", "tab", "eat", "tea", "owl"], [["bat", "tab"], ["eat", "tea"], ["owl"]]),
    ([], []),
    ([""], [[""]]),
    (["abc", "cba", "bca", "xyz"], [["abc", "cba", "bca"], ["xyz"]]),
    (["a", "a", "a"], [["a", "a", "a"]]),
    (["cat", "dog"], [["cat"], ["dog"]]),
]
for index, (words, expected) in enumerate(cases):
    check(index + 1, lambda: main.group_anagrams(words), expected, normalize=normalize)

# Performance test: 20,000 words in 10,000 groups of two. Word i repeats
# "a", "b", "c" and "d" once more than each decimal digit of i, so no two
# groups share the same letter counts, and its reversal is the other member
# of its group.
# Budget: 1.0s. Execution service: sorted-key dict solution ~0.03s;
# comparing each word against every existing group is interrupted at the budget.
def word_for(i):
    digits = f"{i:04d}"
    return "".join(letter * (int(d) + 1) for letter, d in zip("abcd", digits))


big_groups = [[word_for(i), word_for(i)[::-1]] for i in range(10_000)]
big = [word for group in big_groups for word in group]
check(7, lambda: main.group_anagrams(big), big_groups, time_budget=1.0, normalize=normalize)

sys.stdout.write(json.dumps(results))
