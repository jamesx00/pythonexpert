import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

from functools import lru_cache

def test_count_target_sums(nums, target):
    n = len(nums)

    @lru_cache(maxsize=None)
    def dp(i, total):
        if i == n:
            return 1 if total == target else 0
        return dp(i + 1, total + nums[i]) + dp(i + 1, total - nums[i])

    result = dp(0, 0)
    dp.cache_clear()
    return result

inputs = [
    ([1, 1, 1, 1, 1], 3),
    ([1], 1),
    ([1], 0),
    ([0, 0, 0, 0, 0, 0, 0, 0, 1], 1),
    ([2, 3, 1, 4], 2),
    ([1, 2, 1], 0),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_count_target_sums(*i)
        assert main.count_target_sums(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
