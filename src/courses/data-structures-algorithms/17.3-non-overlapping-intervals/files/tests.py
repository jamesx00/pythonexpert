import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    ordered = sorted(intervals, key=lambda iv: iv[1])
    removed = 0
    prev_end = ordered[0][1]
    for start, end in ordered[1:]:
        if start < prev_end:
            removed += 1
        else:
            prev_end = end
    return removed

inputs = [
    ([[1, 2], [2, 3], [3, 4], [1, 3]],),
    ([[1, 2], [1, 2], [1, 2]],),
    ([[1, 2], [2, 3]],),
    ([],),
    ([[1, 100], [11, 22], [1, 11], [2, 12]],),
    ([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]],),
    ([[-5, -2], [-3, 1], [2, 5]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_erase_overlap_intervals(*i)
        assert main.erase_overlap_intervals(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
