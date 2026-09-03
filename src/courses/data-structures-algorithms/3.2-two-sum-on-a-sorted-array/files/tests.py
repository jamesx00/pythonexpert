import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return None

inputs = [
    ([1, 3, 4, 7, 11], 10),
    ([-4, -1, 0, 3, 8], 4),
    ([2, 5], 7),
    ([1, 2, 3, 4, 6], 10),
    ([-6, -3, -1, 2, 9], -9),
    ([0, 0, 3, 5], 0),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.two_sum_sorted(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
