import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

inputs = [
    ([-4, 0, 3, 9, 14, 22], 9),
    ([-4, 0, 3, 9, 14, 22], 10),
    ([1, 2, 3, 4, 5], 1),
    ([1, 2, 3, 4, 5], 5),
    ([], 5),
    ([7], 7),
    ([7], 3),
    ([2, 4, 6, 8, 10, 12, 14], 12),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.binary_search(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
