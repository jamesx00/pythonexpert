import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_max_product_subarray(nums):
    res = nums[0]
    cur_max = cur_min = nums[0]
    for n in nums[1:]:
        candidates = (n, cur_max * n, cur_min * n)
        cur_max = max(candidates)
        cur_min = min(candidates)
        res = max(res, cur_max)
    return res

inputs = [
    ([2, 3, -2, 4],),
    ([-2, 0, -1],),
    ([-2, 3, -4],),
    ([5],),
    ([-3],),
    ([2, -5, -2, -4, 3],),
    ([0, 2, -3, 4, -1, 0],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_max_product_subarray(*i)
        assert main.max_product_subarray(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
