import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_subsets_with_dup(nums):
    nums = sorted(nums)
    result = []

    def backtrack(start, path):
        result.append(list(path))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result

def normalize(subsets_list):
    return sorted(sorted(subset) for subset in subsets_list)

inputs = [
    ([1, 2, 2],),
    ([0],),
    ([],),
    ([4, 4, 4],),
    ([1, 2, 3],),
    ([2, 1, 2, 1],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = normalize(test_subsets_with_dup(*i))
        assert normalize(main.subsets_with_dup(*i)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
