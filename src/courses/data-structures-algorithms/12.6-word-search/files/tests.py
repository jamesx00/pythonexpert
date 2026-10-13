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


cases = [
    (([["C", "A", "T"], ["B", "R", "E"], ["D", "O", "G"]], "CARE"), True),
    (([["C", "A", "T"], ["B", "R", "E"], ["D", "O", "G"]], "DOT"), False),
    (([["A", "B"], ["C", "D"]], "ABDC"), True),
    (([["A", "B"], ["C", "D"]], "ABCD"), False),
    (([["X"]], "X"), True),
    (([["X"]], "XX"), False),
    (([["A", "A", "A"], ["A", "A", "A"]], "AAAAA"), True),
]
for index, (args, expected) in enumerate(cases):
    check(index + 1, lambda: main.word_search(*args), expected)

# Performance test: a 30x30 board where cell (r, c) holds letter
# (7 * r + 3 * c) % 26, so each step right moves 3 letters on and each step
# down 7. The 14-letter word follows 13 cells to the right, then needs an "X",
# which never sits next to a "K". So the word isn't on the board.
# Budget: 1.0s. Execution service: backtracking that stops at the first
# wrong letter ~0.001s; walking every 14-cell path and comparing at the end
# is interrupted at the budget.
board = [[chr(65 + (7 * r + 3 * c) % 26) for c in range(30)] for r in range(30)]
check(8, lambda: main.word_search(board, "ADGJMPSVYBEHKX"), False, time_budget=1.0)

sys.stdout.write(json.dumps(results))
