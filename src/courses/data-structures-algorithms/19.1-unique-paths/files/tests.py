import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_count_paths(rows, cols):
    dp = [[1] * cols for _ in range(rows)]
    for r in range(1, rows):
        for c in range(1, cols):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    return dp[rows - 1][cols - 1]

inputs = [
    (2, 3),
    (3, 2),
    (1, 1),
    (3, 3),
    (1, 5),
    (4, 4),
    (5, 6),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_count_paths(*i)
        assert main.count_paths(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
