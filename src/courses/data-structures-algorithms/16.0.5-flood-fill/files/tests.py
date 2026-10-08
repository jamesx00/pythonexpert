import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def flood_fill(grid, r, c, color):
    original = grid[r][c]
    if original == color:
        return grid
    rows, cols = len(grid), len(grid[0])

    def fill(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != original:
            return
        grid[r][c] = color
        fill(r + 1, c)
        fill(r - 1, c)
        fill(r, c + 1)
        fill(r, c - 1)

    fill(r, c)
    return grid

def check(fn, *args):
    return fn(*args)

cases = [
    ('flood_fill', ([[1, 1, 0], [1, 0, 0], [1, 1, 1]], 0, 0, 2)),
    ('flood_fill', ([[0, 0], [0, 0]], 1, 1, 0)),
    ('flood_fill', ([[5]], 0, 0, 3)),
    ('flood_fill', ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 1, 1, 7)),
    ('flood_fill', ([[3, 3, 3, 4], [4, 3, 4, 4], [3, 3, 3, 3]], 2, 3, 9)),
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
