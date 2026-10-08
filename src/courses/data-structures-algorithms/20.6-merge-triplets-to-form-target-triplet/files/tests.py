import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_merge_triplets(triplets, target):
    best = [0, 0, 0]
    for t in triplets:
        if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
            best = [max(best[i], t[i]) for i in range(3)]
    return best == target

inputs = [
    ([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]),
    ([[5, 2, 3]], [5, 2, 3]),
    ([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]),
    ([[3, 4, 5], [4, 5, 6]], [3, 2, 5]),
    ([[1, 1, 1]], [2, 2, 2]),
    ([[2, 2, 2], [1, 1, 1], [3, 3, 3]], [3, 3, 3]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_merge_triplets(*i)
        assert main.merge_triplets(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
