import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_min_jumps(nums):
    jumps = 0
    cur_end = 0
    farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps

inputs = [
    ([2, 3, 1, 1, 4],),
    ([0],),
    ([1, 1, 1, 1],),
    ([2, 1, 1, 1, 1],),
    ([5, 1, 1, 1, 1],),
    ([1, 2, 3],),
    ([2, 3, 0, 1, 4],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_min_jumps(*i)
        assert main.min_jumps(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
