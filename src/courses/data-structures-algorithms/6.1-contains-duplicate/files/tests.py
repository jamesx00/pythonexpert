import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_has_duplicate(nums):
    return len(set(nums)) != len(nums)

inputs = [
    ([4, 2, 7, 2, 9],),
    ([4, 2, 7, 9],),
    ([1, 1, 1, 1],),
    ([],),
    ([5],),
    ([10, 20, 30, 40, 10],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_has_duplicate(*i)
        assert main.has_duplicate(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
