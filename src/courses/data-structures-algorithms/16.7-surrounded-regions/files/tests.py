import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_surrounded_regions(board):
    board = [row[:] for row in board]
    rows, cols = len(board), len(board[0]) if board else 0
    safe = set()

    def dfs(r, c):
        if (r, c) in safe or r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
            return
        safe.add((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O' and (r, c) not in safe:
                board[r][c] = 'X'
    return board

inputs = [
    ([["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]],),
    ([["O", "X"], ["X", "X"]],),
    ([["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]],),
    ([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "X", "X"]],),
    ([["O"]],),
    ([["X"]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        original = [row[:] for row in i[0]]
        result = test_surrounded_regions(original)
        assert main.surrounded_regions([row[:] for row in i[0]]) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
