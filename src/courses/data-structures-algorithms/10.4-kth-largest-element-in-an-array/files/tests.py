import sys
import json
import heapq

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(nums, k):
    return heapq.nlargest(k, nums)[-1]

inputs = [
    ([7, 2, 9, 4, 9], 2),
    ([3, 1, 5, 12, 8, 2], 3),
    ([1], 1),
    ([2, 2, 2, 2], 3),
    ([-1, -5, -3, 0], 1),
    ([10, 20, 30, 40, 50], 5),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.find_kth_largest(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
