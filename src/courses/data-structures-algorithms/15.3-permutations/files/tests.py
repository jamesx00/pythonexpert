import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_permute(nums):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(list(path))
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i + 1:])
            path.pop()

    backtrack([], nums)
    return result

def normalize(perms):
    return sorted(perms)

inputs = [
    ([1, 2, 3],),
    ([0],),
    ([],),
    ([4, 5],),
    ([1, -1],),
    ([1, 2, 3, 4],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = normalize(test_permute(*i))
        assert normalize(main.permute(*i)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
