import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

from functools import lru_cache

def test_longest_increasing_path(matrix):
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])

    @lru_cache(maxsize=None)
    def dfs(r, c):
        best = 1
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                best = max(best, 1 + dfs(nr, nc))
        return best

    result = max(dfs(r, c) for r in range(rows) for c in range(cols))
    dfs.cache_clear()
    return result

inputs = [
    ([[5, 1, 6], [4, 2, 7], [3, 8, 9]],),
    ([[1]],),
    ([[7, 7, 7], [7, 7, 7]],),
    ([[1, 2, 3], [8, 9, 4], [7, 6, 5]],),
    ([[10, 20], [15, 25]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_longest_increasing_path(*i)
        assert main.longest_increasing_path(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
