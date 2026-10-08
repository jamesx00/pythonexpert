import sys
import json
from collections import deque

from unittest.mock import patch
patch('builtins.print').start()

import main

INF = 2147483647

def test_islands_and_treasure(grid):
    grid = [row[:] for row in grid]
    rows, cols = len(grid), len(grid[0]) if grid else 0
    q = deque()
    visited = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                q.append((r, c))
                visited.add((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in visited and grid[nr][nc] == INF):
                grid[nr][nc] = grid[r][c] + 1
                visited.add((nr, nc))
                q.append((nr, nc))
    return grid

inputs = [
    ([[INF, -1, 0], [INF, INF, INF], [0, -1, INF]],),
    ([[0]],),
    ([[-1]],),
    ([[INF]],),
    ([[0, INF, INF]],),
    ([[0, -1, INF]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        original = [row[:] for row in i[0]]
        result = test_islands_and_treasure(original)
        assert main.islands_and_treasure(i[0]) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
