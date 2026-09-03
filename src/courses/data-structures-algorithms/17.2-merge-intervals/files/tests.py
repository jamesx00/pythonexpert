import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_merge_intervals(intervals):
    if not intervals:
        return []
    ordered = sorted(intervals, key=lambda iv: iv[0])
    result = [ordered[0][:]]
    for start, end in ordered[1:]:
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result

inputs = [
    ([[8, 10], [1, 3], [2, 6]],),
    ([[1, 4], [4, 5]],),
    ([[1, 4], [0, 4]],),
    ([[1, 4], [2, 3]],),
    ([[1, 2], [3, 4], [5, 6]],),
    ([[5, 7]],),
    ([[1, 10], [2, 3], [4, 5], [6, 7]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_merge_intervals(*i)
        assert main.merge_intervals(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
