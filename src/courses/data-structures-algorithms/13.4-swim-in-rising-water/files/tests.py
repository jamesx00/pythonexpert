import sys
import json
import heapq

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_swim_in_water(grid):
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    min_heap = [(grid[0][0], 0, 0)]
    visited[0][0] = True
    result = 0

    while min_heap:
        t, r, c = heapq.heappop(min_heap)
        result = max(result, t)
        if r == n - 1 and c == n - 1:
            return result
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                heapq.heappush(min_heap, (grid[nr][nc], nr, nc))

    return result

inputs = [
    ([[0, 1], [2, 3]],),
    ([[0, 2], [1, 3]],),
    ([[0]],),
    ([[3, 2], [0, 1]],),
    ([[0, 1, 2], [1, 2, 3], [2, 3, 4]],),
    ([[0, 4, 2], [1, 3, 5], [6, 7, 8]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_swim_in_water(*i)
        assert main.swim_in_water(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
