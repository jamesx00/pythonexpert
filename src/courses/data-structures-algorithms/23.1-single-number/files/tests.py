import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_single_number(nums):
    result = 0
    for n in nums:
        result ^= n
    return result

inputs = [
    ([4, 1, 2, 1, 2],),
    ([1],),
    ([2, 2, 1],),
    ([7, 3, 5, 4, 5, 3, 4],),
    ([-1, -1, -2],),
    ([0, 1, 0],),
    ([9, 5, 9],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_single_number(*i)
        assert main.single_number(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
