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


def run(board):
    # A fresh copy of the board, so the in-place changes can't affect the
    # next test.
    return main.surrounded_regions([row[:] for row in board])


cases = [
    ([["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]], [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]),
    ([["O", "X"], ["X", "X"]], [["O", "X"], ["X", "X"]]),
    ([["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]], [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]),
    ([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "X", "X"]], [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]]),
    ([["O"]], [["O"]]),
    ([["X"]], [["X"]]),
    ([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]], [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]),
    ([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "X", "O", "X"]], [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "X", "O", "X"]]),
]
for index, (board, expected) in enumerate(cases):
    check(index + 1, lambda: run(board), expected)


# Performance test: a 211x211 board cut into a 10x10 layout of 20x20 blocks
# of "O", with a line of "X" between blocks and around the edge. In the top
# row of blocks, every other block also has its top edge cells turned to "O",
# so 5 blocks touch the border and stay. The other 95 are captured. Built
# outside the budget.
# Budget: 1.0s. Execution service: one search from the border ~0.01s; a
# separate search from every "O" to see if it escapes is interrupted at the
# budget.
def escapes(r, c):
    return r <= 20 and (c // 21) % 2 == 0


size = 211
big = [["X"] * size for _ in range(size)]
expected_big = [["X"] * size for _ in range(size)]
for r in range(size):
    for c in range(size):
        if (r % 21 and c % 21) or (r == 0 and c % 21 and escapes(r, c)):
            big[r][c] = "O"
            if escapes(r, c):
                expected_big[r][c] = "O"
check(9, lambda: run(big), expected_big, time_budget=1.0)

sys.stdout.write(json.dumps(results))
