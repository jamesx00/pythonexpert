import sys
import json
import math

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(piles, h):
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        hours = sum(math.ceil(p / mid) for p in piles)
        if hours <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo

inputs = [
    ([3, 6, 7, 11], 8),
    ([30, 11, 23, 4, 20], 5),
    ([30, 11, 23, 4, 20], 6),
    ([1, 1, 1, 1], 4),
    ([1000000000], 2),
    ([5], 1),
    ([2, 4, 8], 6),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.min_eating_speed(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
