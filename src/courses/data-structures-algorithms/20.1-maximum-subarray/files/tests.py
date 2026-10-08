import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_max_subarray(nums):
    max_sum = cur = nums[0]
    for n in nums[1:]:
        cur = max(n, cur + n)
        max_sum = max(max_sum, cur)
    return max_sum

inputs = [
    ([3, -2, 5, -1, 4],),
    ([-3, 1, -8, 4, 6],),
    ([-5],),
    ([1, 2, 3, 4],),
    ([-2, -1, -3, -4],),
    ([5, 4, -1, 7, 8],),
    ([0, 0, 0, 3, -1],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_max_subarray(*i)
        assert main.max_subarray(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
