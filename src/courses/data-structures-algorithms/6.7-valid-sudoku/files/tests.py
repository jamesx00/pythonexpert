import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def empty_board():
    return [["." for _ in range(9)] for _ in range(9)]

def board_with(cells):
    b = empty_board()
    for r, c, v in cells:
        b[r][c] = v
    return b

def test_is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == ".":
                continue
            box = (r // 3) * 3 + (c // 3)
            if v in rows[r] or v in cols[c] or v in boxes[box]:
                return False
            rows[r].add(v)
            cols[c].add(v)
            boxes[box].add(v)
    return True

board_1 = board_with([(0, 0, "8"), (1, 1, "8")])
board_2 = empty_board()
board_3 = board_with([(4, 2, "3"), (4, 7, "3")])
board_4 = board_with([(1, 5, "7"), (6, 5, "7")])
board_5 = board_with([(i, i, str(i + 1)) for i in range(9)])
board_6 = board_with([(0, 0, "5"), (4, 4, "5")])

inputs = [
    (board_1,),
    (board_2,),
    (board_3,),
    (board_4,),
    (board_5,),
    (board_6,),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_is_valid_sudoku(*i)
        assert main.is_valid_sudoku(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
