import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]

inputs = [
    ([11, 15, 19, 2, 5, 8],),
    ([1, 2, 3, 4],),
    ([4, 1, 2, 3],),
    ([3, 4, 1, 2],),
    ([2, 3, 4, 1],),
    ([9],),
    ([2, 1],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.find_min(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
