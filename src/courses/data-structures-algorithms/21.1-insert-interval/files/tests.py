import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_insert_interval(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)
    start, end = new_interval

    while i < n and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1

    result.append([start, end])

    while i < n:
        result.append(intervals[i])
        i += 1

    return result

inputs = [
    ([[1, 3], [6, 9]], [2, 5]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
    ([], [5, 7]),
    ([[1, 5]], [6, 8]),
    ([[1, 5]], [2, 3]),
    ([[3, 5]], [0, 1]),
    ([[1, 3], [4, 6], [8, 10]], [0, 12]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_insert_interval(*i)
        assert main.insert_interval(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
