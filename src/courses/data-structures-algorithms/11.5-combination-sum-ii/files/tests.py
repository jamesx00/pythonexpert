import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_combination_sum2(candidates, target):
    candidates = sorted(candidates)
    result = []

    def backtrack(start, remaining, path):
        if remaining == 0:
            result.append(list(path))
            return
        if remaining < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, remaining - candidates[i], path)
            path.pop()

    backtrack(0, target, [])
    return result

def normalize(combos):
    return sorted(sorted(combo) for combo in combos)

inputs = [
    ([2, 5, 2, 1, 2], 5),
    ([2], 1),
    ([1, 1, 1], 2),
    ([10, 1, 2, 7, 6, 1, 5], 8),
    ([3, 3, 3], 9),
    ([4, 8], 20),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = normalize(test_combination_sum2(*i))
        assert normalize(main.combination_sum2(*i)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
