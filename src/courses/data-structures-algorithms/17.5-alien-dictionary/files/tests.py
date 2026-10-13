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




def rules(words):
    """The letters in words, and the (before, after) pairs that comparing
    each word with the next one forces."""
    letters = set("".join(words))
    pairs = set()
    for w1, w2 in zip(words, words[1:]):
        for a, b in zip(w1, w2):
            if a != b:
                pairs.add((a, b))
                break
    return letters, pairs


def consistent_with(words):
    """A normalize function for one case. Any order that holds each letter
    once and puts every forced pair the right way round counts as the same
    answer. Anything else, such as "", is compared as it is."""
    letters, pairs = rules(words)

    def normalize(order):
        if not isinstance(order, str) or len(order) != len(letters) or set(order) != letters:
            return order
        pos = {c: i for i, c in enumerate(order)}
        if all(pos[a] < pos[b] for a, b in pairs):
            return "a valid order"
        return order
    return normalize


cases = [
    (["z", "x"], "zx"),
    (["z", "x", "z"], ""),
    (["abc", "ab"], ""),
    (["ac", "ab", "zc", "zb"], "acbz"),
    (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
    (["abc", "abd", "abe"], "abcde"),
    (["ba", "bc", "ac", "cab"], "bac"),
    (["a", "b", "ca", "cb", "a"], ""),
]
for index, (words, expected) in enumerate(cases):
    check(index + 1, lambda: main.alien_order(words), expected, normalize=consistent_with(words))

# Performance test: the 26 letters as one-letter words, from "z" down to
# "a". The only valid order is the alphabet reversed.
# Budget: 1.0s. Execution service: topological sort <0.001s; trying every
# ordering of the letters starts from "abc...z" and would have to go
# through about 26! orderings, so it's interrupted at the budget.
big = [chr(c) for c in range(ord("z"), ord("a") - 1, -1)]
check(9, lambda: main.alien_order(big), "zyxwvutsrqponmlkjihgfedcba", time_budget=1.0, normalize=consistent_with(big))

sys.stdout.write(json.dumps(results))
