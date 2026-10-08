import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(nums):
    nums = sorted(nums)
    n = len(nums)
    triplets = []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return triplets

inputs = [
    ([-2, 0, 1, 1, -1, -4],),
    ([0, 0, 0],),
    ([0, 0, 0, 0],),
    ([1, 2, -3],),
    ([1, 2, 3],),
    ([-1, 0, 1, 2, -1, -4],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = sorted(test_func(*i))
        actual = sorted(main.three_sum(*i))
        assert actual == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
