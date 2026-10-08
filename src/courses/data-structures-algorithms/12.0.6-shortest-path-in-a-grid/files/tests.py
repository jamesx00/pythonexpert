import sys
import json
import copy
from collections import deque

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def grid_shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1
    dist = {(0, 0): 0}
    queue = deque([(0, 0)])
    while queue:
        r, c = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return dist[(r, c)]
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols
                    and grid[nr][nc] == 0 and (nr, nc) not in dist):
                dist[(nr, nc)] = dist[(r, c)] + 1
                queue.append((nr, nc))
    return -1

def check(fn, *args):
    return fn(*args)

cases = [
    ('grid_shortest_path', ([[0, 0, 0], [1, 1, 0], [0, 0, 0]],)),
    ('grid_shortest_path', ([[0]],)),
    ('grid_shortest_path', ([[0, 1], [1, 0]],)),
    ('grid_shortest_path', ([[1, 0], [0, 0]],)),
    ('grid_shortest_path', ([[0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]],)),
    ('grid_shortest_path', ([[0, 0], [0, 0]],)),
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
