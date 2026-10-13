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


import random


def run(board, words):
    # A fresh copy of the board, so an in-place solution can't affect the
    # next test.
    return main.find_words([row[:] for row in board], list(words))


cases = [
    (([["a", "b", "c"], ["e", "f", "g"], ["i", "j", "k"]], ["abc", "abfe", "beg", "aei", "xyz"]), ["abc", "abfe", "aei"]),
    (([["a"]], ["a", "b"]), ["a"]),
    (([["a", "a"]], ["aa", "aaa"]), ["aa"]),
    (([["x", "y"], ["y", "x"]], ["ab", "cd"]), []),
    (([["o", "a"], ["e", "t"]], ["oa", "oe", "eat", "ate"]), ["oa", "oe", "ate"]),
    (([["a", "b"], ["c", "d"]], ["abdc", "abcd", "acdb", "dbac", "aba"]), ["abdc", "acdb", "dbac"]),
]
for index, ((board, words), expected) in enumerate(cases):
    check(index + 1, lambda: run(board, words), expected, normalize=sorted)


# Performance test: a 24x24 board of the letters a-e, and 6,212 words: 499
# traced from random 7-cell paths on the board, so they're all found, and
# 5,713 that are a random 6-cell path plus "z", which isn't on the board, so
# none of them is found. The board and the paths come from
# random.Random(13).
# Budget: 1.0s. Execution service: one DFS guided by a trie ~0.27s; a
# separate board search for each word is interrupted at the budget.
def random_path_word(rng, board, length):
    rows, cols = len(board), len(board[0])
    r, c = rng.randrange(rows), rng.randrange(cols)
    seen = {(r, c)}
    letters = [board[r][c]]
    while len(letters) < length:
        steps = [(r + dr, c + dc) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
                 if 0 <= r + dr < rows and 0 <= c + dc < cols and (r + dr, c + dc) not in seen]
        if not steps:
            break
        r, c = rng.choice(steps)
        seen.add((r, c))
        letters.append(board[r][c])
    return "".join(letters)


rng = random.Random(13)
big_board = [[rng.choice("abcde") for _ in range(24)] for _ in range(24)]
found_words = {random_path_word(rng, big_board, 7) for _ in range(500)}
missing_words = {random_path_word(rng, big_board, 6) + "z" for _ in range(8_000)}
check(7, lambda: run(big_board, sorted(found_words | missing_words)), sorted(found_words),
      time_budget=1.0, normalize=sorted)

sys.stdout.write(json.dumps(results))
