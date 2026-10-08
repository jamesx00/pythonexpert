import sys
import json
from collections import deque

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(nums, k):
    dq = deque()
    result = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] <= n:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

inputs = [
    ([4, 2, 9, 1, 6, 3], 3),
    ([1, 3, -1, -3, 5, 3, 6, 7], 3),
    ([5], 1),
    ([9, 8, 7, 6], 2),
    ([1, 1, 1, 1], 2),
    ([2, 4, 6, 8, 10], 5),
    ([-1, -3, -2, -5], 2),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.window_max(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
