import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_can_partition(nums):
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = {0}
    for n in nums:
        dp |= {n + x for x in dp if n + x <= target}
    return target in dp

inputs = [
    ([1, 5, 11, 5],),
    ([1, 2, 3, 5],),
    ([1, 1],),
    ([1],),
    ([2, 2, 3, 5],),
    ([3, 3, 3, 4, 5],),
    ([2, 2, 2, 2, 3, 4, 5],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_can_partition(*i)
        assert main.can_partition(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
