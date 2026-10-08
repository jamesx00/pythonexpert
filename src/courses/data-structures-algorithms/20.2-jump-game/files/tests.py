import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_can_jump(nums):
    reach = 0
    for i, n in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + n)
    return True

inputs = [
    ([2, 3, 1, 1, 4],),
    ([2, 0, 0, 1],),
    ([0],),
    ([1, 0, 1, 0],),
    ([3, 2, 1, 0, 4],),
    ([1, 1, 1, 1],),
    ([5, 0, 0, 0, 0, 0],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_can_jump(*i)
        assert main.can_jump(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
