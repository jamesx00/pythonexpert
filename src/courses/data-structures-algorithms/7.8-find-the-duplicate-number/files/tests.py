import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_find_duplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow2 = nums[0]
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]
    return slow

inputs = [
    ([1, 3, 4, 2, 2],),
    ([3, 1, 3, 4, 2],),
    ([1, 1],),
    ([2, 2, 2, 2, 2],),
    ([5, 4, 3, 2, 1, 5],),
    ([1, 2, 3, 4, 5, 3],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_find_duplicate(*i)
        assert main.find_duplicate(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
