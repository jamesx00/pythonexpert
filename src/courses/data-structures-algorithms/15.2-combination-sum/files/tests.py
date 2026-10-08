import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_combination_sum(candidates, target):
    result = []

    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(list(path))
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i], path)
            path.pop()

    backtrack(0, target, [])
    return result

def normalize(combos):
    return sorted(sorted(combo) for combo in combos)

inputs = [
    ([2, 3, 5], 8),
    ([2], 1),
    ([1], 3),
    ([3, 4, 6], 12),
    ([7, 11], 5),
    ([2, 4], 8),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = normalize(test_combination_sum(*i))
        assert normalize(main.combination_sum(*i)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
