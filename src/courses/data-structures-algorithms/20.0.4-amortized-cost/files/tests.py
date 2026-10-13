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


import re


def canonical(answer):
    """Normalizes Big-O notation so that, for example, "O(n^2)", "O(n\u00b2)",
    "o(N ** 2)" and "n^2" compare equal, as do "O(n * m)" and "O(m * n)"."""
    s = str(answer).lower()
    s = s.replace("\u00b2", "^2").replace("\u00b3", "^3").replace("**", "^")
    s = re.sub(r"[\s*()\u00b7\u00d7\u2082]", "", s).replace("log2", "log")
    if s.startswith("o"):
        s = s[1:]
    terms = []
    for term in s.split("+"):
        if re.fullmatch(r"[a-z]+", term) and "log" not in term:
            term = "".join(sorted(term))
        terms.append(term)
    return "+".join(sorted(terms))


cases = [
    ("build_list_complexity", "O(n)"),
    ("append_one_complexity", "O(n)"),
    ("append_amortized_complexity", "O(1)"),
    ("fill_grow_by_ten_complexity", "O(n^2)"),
    ("next_greater_complexity", "O(n)"),
]
for index, (name, expected) in enumerate(cases):
    check(index + 1, lambda: getattr(main, name)(), expected, normalize=canonical)

sys.stdout.write(json.dumps(results))
