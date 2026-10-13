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
    ([["JFK", "SFO"], ["SFO", "ATL"], ["ATL", "JFK"], ["JFK", "ATL"]], ["JFK", "ATL", "JFK", "SFO", "ATL"]),
    ([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]], ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),
    ([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]], ["JFK", "NRT", "JFK", "KUL"]),
    ([["JFK", "A"], ["A", "B"], ["B", "JFK"]], ["JFK", "A", "B", "JFK"]),
    ([["JFK", "B"], ["JFK", "A"], ["B", "JFK"]], ["JFK", "B", "JFK", "A"]),
    ([["JFK", "SFO"]], ["JFK", "SFO"]),
]
for index, (tickets, expected) in enumerate(cases):
    check(index + 1, lambda: main.find_itinerary(tickets), expected)

# Performance test: a chain of 26 airports JFK, B01, ..., B25. Each one has
# a round trip to its own side airport (JFK -> Z00 -> JFK, B01 -> Z01 -> B01,
# ...) and a ticket on to the next airport in the chain. "B.." sorts before
# "Z..", so trying the smallest ticket first always leaves the round trip
# behind, and that dead end only shows up at the end of the chain.
# Backtracking then tries about 2^25 routes. The answer takes every round
# trip before moving on: JFK, Z00, JFK, B01, Z01, B01, B02, ...
# Budget: 1.0s. Execution service: Hierholzer's algorithm <0.001s;
# backtracking that tries the smallest ticket first is interrupted at the
# budget.
hubs = ["JFK"] + [f"B{i:02d}" for i in range(1, 26)]
big_tickets = []
big_expected = ["JFK"]
for i, hub in enumerate(hubs):
    side = f"Z{i:02d}"
    big_tickets += [[hub, side], [side, hub]]
    if i > 0:
        big_expected.append(hub)
    big_expected += [side, hub]
for a, b in zip(hubs, hubs[1:]):
    big_tickets.append([a, b])
check(7, lambda: main.find_itinerary(big_tickets), big_expected, time_budget=1.0)

sys.stdout.write(json.dumps(results))
