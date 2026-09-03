import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []

inputs = [
    ([3, 5, -4, 8], 4),
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([1, 5, 5, 2], 10),
    ([-3, 4, 3, 90], 0),
    ([0, 4, 3, 0], 0),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = sorted(test_two_sum(*i))
        assert sorted(main.two_sum(*i)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
