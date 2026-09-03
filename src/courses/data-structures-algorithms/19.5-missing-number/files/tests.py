import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_missing_number(nums):
    n = len(nums)
    result = n
    for i in range(n):
        result ^= i ^ nums[i]
    return result

inputs = [
    ([3, 0, 1],),
    ([0, 1],),
    ([9, 6, 4, 2, 3, 5, 7, 0, 1],),
    ([0],),
    ([1],),
    ([1, 2],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_missing_number(*i)
        assert main.missing_number(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
