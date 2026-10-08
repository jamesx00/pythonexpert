import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_subsets(nums):
    result = [[]]
    for n in nums:
        result += [subset + [n] for subset in result]
    return result

def normalize(subsets_list):
    return sorted(sorted(subset) for subset in subsets_list)

inputs = [
    ([1, 2, 3],),
    ([],),
    ([5],),
    ([4, 7],),
    ([0, -1],),
    ([1, 2, 3, 4],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = normalize(test_subsets(*i))
        assert normalize(main.subsets(*i)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
