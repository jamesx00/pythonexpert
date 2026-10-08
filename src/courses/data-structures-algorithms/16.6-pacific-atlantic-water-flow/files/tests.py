import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_pacific_atlantic(heights):
    if not heights or not heights[0]:
        return []
    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visited, prev_height):
        if ((r, c) in visited or r < 0 or c < 0 or r >= rows or c >= cols
                or heights[r][c] < prev_height):
            return
        visited.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc, visited, heights[r][c])

    for c in range(cols):
        dfs(0, c, pac, heights[0][c])
        dfs(rows - 1, c, atl, heights[rows - 1][c])
    for r in range(rows):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, cols - 1, atl, heights[r][cols - 1])

    return [list(x) for x in (pac & atl)]

inputs = [
    ([[1, 2, 2], [3, 2, 3], [2, 4, 5]],),
    ([[1]],),
    ([[3, 3], [3, 3]],),
    ([[1, 2, 3]],),
    ([[3], [2], [1]],),
    ([],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = sorted(test_pacific_atlantic(*i))
        assert sorted(main.pacific_atlantic(*i)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
