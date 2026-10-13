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


def run(operations):
    """Runs (method_name, args) calls on a new Twitter and returns what each
    get_news_feed call returned, in order."""
    twitter = main.Twitter()
    feeds = []
    for name, args in operations:
        returned = getattr(twitter, name)(*args)
        if name == "get_news_feed":
            feeds.append(returned)
    return feeds


cases = [
    ([("post_tweet", (1, 5)), ("follow", (1, 2)), ("post_tweet", (2, 6)), ("get_news_feed", (1,))], [[6, 5]]),
    ([("post_tweet", (1, 5)), ("post_tweet", (2, 6)), ("get_news_feed", (1,))], [[5]]),
    ([("post_tweet", (1, 1)), ("follow", (1, 2)), ("post_tweet", (2, 2)), ("unfollow", (1, 2)), ("get_news_feed", (1,))], [[1]]),
    ([("post_tweet", (1, t)) for t in range(1, 5)] + [("get_news_feed", (1,))], [[4, 3, 2, 1]]),
    ([("follow", (1, 2)), ("post_tweet", (2, 9)), ("post_tweet", (1, 10)), ("get_news_feed", (1,))], [[10, 9]]),
    ([("post_tweet", (5, t)) for t in range(1, 13)] + [("get_news_feed", (5,))], [[12, 11, 10, 9, 8, 7, 6, 5, 4, 3]]),
]
for index, (operations, expected) in enumerate(cases):
    check(index + 1, lambda: run(operations), expected)

# Performance test: user 0 follows users 1..10, who post 50,000 tweets in
# turn (tweet t is posted by user 1 + t % 10), then user 0 reads the feed
# 2,000 times. Every feed is tweets 49,999 down to 49,990.
# Budget: 1.0s. Execution service: heap-merge solution ~0.05s; scanning
# every tweet on each feed call is interrupted at the budget.
big = [("follow", (0, u)) for u in range(1, 11)]
big += [("post_tweet", (1 + t % 10, t)) for t in range(50_000)]
big += [("get_news_feed", (0,))] * 2_000
check(7, lambda: run(big), [list(range(49_999, 49_989, -1))] * 2_000, time_budget=1.0)


sys.stdout.write(json.dumps(results))
