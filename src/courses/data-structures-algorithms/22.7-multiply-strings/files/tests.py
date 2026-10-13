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
    (("23", "45"), "1035"),
    (("2", "3"), "6"),
    (("0", "52"), "0"),
    (("123", "456"), "56088"),
    (("999", "999"), "998001"),
    (("0", "0"), "0"),
    (("100", "10"), "1000"),
    (("9999", "99"), "989901"),
]
for index, ((num1, num2), expected) in enumerate(cases):
    check(index + 1, lambda: main.multiply(num1, num2), expected)

# Performance test: two 200-digit numbers, digits from a fixed pattern. The
# expected product comes from Python's own int multiply, outside the budget.
# Budget: 1.0s. Execution service: digit-by-digit multiply ~0.02s; adding
# num1 to itself num2 times is interrupted at the budget.
a = "".join(str((i * 7 + 3) % 10) for i in range(199)) + "1"
b = "9" + "".join(str((i * 3 + 1) % 10) for i in range(199))
check(9, lambda: main.multiply(a, b), str(int(a) * int(b)), time_budget=1.0)

sys.stdout.write(json.dumps(results))
