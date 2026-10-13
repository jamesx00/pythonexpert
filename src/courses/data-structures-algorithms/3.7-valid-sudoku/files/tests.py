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


def board_with(cells):
    board = [["." for _ in range(9)] for _ in range(9)]
    for r, c, v in cells:
        board[r][c] = v
    return board


cases = [
    (board_with([(0, 0, "8"), (1, 1, "8")]), False),
    (board_with([]), True),
    (board_with([(4, 2, "3"), (4, 7, "3")]), False),
    (board_with([(1, 5, "7"), (6, 5, "7")]), False),
    (board_with([(i, i, str(i + 1)) for i in range(9)]), True),
    (board_with([(0, 0, "5"), (4, 4, "5")]), True),
]
for index, (board, expected) in enumerate(cases):
    check(index + 1, lambda: main.is_valid_sudoku(board), expected)

sys.stdout.write(json.dumps(results))
