import sys
import json
from collections import deque

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0]) if grid else 0
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while q:
        r, c, t = q.popleft()
        minutes = max(minutes, t)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                q.append((nr, nc, t + 1))
    return -1 if fresh > 0 else minutes

inputs = [
    ([[2, 1, 0], [1, 1, 0], [0, 1, 2]],),
    ([[0, 2]],),
    ([[2, 1, 1], [0, 1, 1], [1, 0, 1]],),
    ([[0, 0, 0]],),
    ([[1]],),
    ([[2]],),
    ([[2, 1, 1, 1, 1]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        grid_copy = [row[:] for row in i[0]]
        result = test_oranges_rotting(grid_copy)
        assert main.oranges_rotting([row[:] for row in i[0]]) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
