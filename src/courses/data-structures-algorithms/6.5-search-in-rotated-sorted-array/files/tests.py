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
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

inputs = [
    ([30, 40, 50, 5, 10, 20], 10),
    ([30, 40, 50, 5, 10, 20], 100),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([4, 5, 6, 7, 0, 1, 2], 3),
    ([1], 1),
    ([1], 0),
    ([5, 1, 3], 5),
    ([1, 2, 3, 4, 5], 5),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.search_rotated(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
