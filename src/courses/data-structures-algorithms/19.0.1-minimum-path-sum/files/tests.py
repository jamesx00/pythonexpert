import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def min_path_sum(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                dp[r][c] = grid[r][c]
            elif r == 0:
                dp[r][c] = dp[r][c - 1] + grid[r][c]
            elif c == 0:
                dp[r][c] = dp[r - 1][c] + grid[r][c]
            else:
                dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])
    return dp[-1][-1]

def check(fn, *args):
    return fn(*args)

cases = [
    ('min_path_sum', ([[1, 3, 1], [1, 5, 1], [4, 2, 1]],)),
    ('min_path_sum', ([[5]],)),
    ('min_path_sum', ([[1, 2, 3]],)),
    ('min_path_sum', ([[1], [2], [3]],)),
    ('min_path_sum', ([[1, 2, 3], [4, 5, 6]],)),
    ('min_path_sum', ([[0, 9, 9, 9], [0, 0, 9, 9], [9, 0, 0, 0], [9, 9, 9, 0]],)),
]

results = {}

for index, (name, args) in enumerate(cases):
    try:
        expected = check(globals()[name], *copy.deepcopy(args))
        assert check(getattr(main, name), *copy.deepcopy(args)) == expected
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
