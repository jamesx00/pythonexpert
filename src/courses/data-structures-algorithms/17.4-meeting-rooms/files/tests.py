import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_can_attend_all_meetings(intervals):
    ordered = sorted(intervals, key=lambda iv: iv[0])
    for i in range(1, len(ordered)):
        if ordered[i][0] < ordered[i - 1][1]:
            return False
    return True

inputs = [
    ([[0, 30], [5, 10], [15, 20]],),
    ([[7, 10], [2, 4]],),
    ([],),
    ([[1, 5]],),
    ([[1, 5], [5, 8]],),
    ([[1, 5], [4, 8]],),
    ([[3, 6], [9, 12], [1, 2]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_can_attend_all_meetings(*i)
        assert main.can_attend_all_meetings(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
