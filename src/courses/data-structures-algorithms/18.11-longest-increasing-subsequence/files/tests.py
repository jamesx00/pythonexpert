import sys
import json
import bisect

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_length_of_lis(nums):
    tails = []
    for n in nums:
        i = bisect.bisect_left(tails, n)
        if i == len(tails):
            tails.append(n)
        else:
            tails[i] = n
    return len(tails)

inputs = [
    ([0, 3, 1, 6, 2, 2, 7],),
    ([7, 7, 7, 7],),
    ([4, 10, 4, 3, 8, 9],),
    ([5],),
    ([1, 2, 3, 4, 5],),
    ([5, 4, 3, 2, 1],),
    ([9, 1, 4, 2, 3, 3, 7],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_length_of_lis(*i)
        assert main.length_of_lis(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
