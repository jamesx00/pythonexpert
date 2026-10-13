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




def palindrome_in(s):
    """Describes an answer by its length, whether it is a palindrome and
    whether it is a substring of s, for inputs where several longest
    palindromes tie."""
    return lambda p: (len(p), p == p[::-1], p in s)


def noise(n, letters, seed):
    """n letters from a fixed pseudo-random sequence, so the input is the
    same on every run."""
    x = seed
    out = []
    for _ in range(n):
        x = (x * 1103515245 + 12345) % 2**31
        out.append(letters[(x >> 16) % len(letters)])
    return "".join(out)


# "bab" and "aba" are both correct for test 1, and any single letter for
# test 5.
check(1, lambda: main.longest_palindrome("babad"), "bab", normalize=palindrome_in("babad"))
check(2, lambda: main.longest_palindrome("cbbd"), "bb")
check(3, lambda: main.longest_palindrome("a"), "a")
check(4, lambda: main.longest_palindrome("forgeeksskeegfor"), "geeksskeeg")
check(5, lambda: main.longest_palindrome("abcde"), "a", normalize=palindrome_in("abcde"))
check(6, lambda: main.longest_palindrome("racecarxyz"), "racecar")
check(7, lambda: main.longest_palindrome(""), "")

# Performance test: 2,043 characters. A 41-letter palindrome made of a..u
# sits between two stretches of 1,000 pseudo-random "x"/"y" letters, whose
# own palindromes are much shorter.
# Budget: 1.0s. Execution service: expand around centers ~0.003s; an n x n
# palindrome table ~0.37s; checking every substring (O(n^3)) is interrupted
# at the budget.
middle = "abcdefghijklmnopqrst" + "u" + "tsrqponmlkjihgfedcba"
big = noise(1_000, "xy", 5) + "x" + middle + "y" + noise(1_000, "xy", 7)
check(8, lambda: main.longest_palindrome(big), middle, time_budget=1.0)

sys.stdout.write(json.dumps(results))
