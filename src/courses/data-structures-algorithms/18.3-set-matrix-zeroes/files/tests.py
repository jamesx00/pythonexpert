import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(matrix):
    rows, cols = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
    for r in range(rows):
        for c in range(cols):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0
    return matrix

inputs = [
    ([[1, 2, 3], [4, 0, 6], [7, 8, 9]],),
    ([[0, 1], [1, 1]],),
    ([[1, 2], [3, 4]],),
    ([[1, 0, 3], [4, 5, 6], [0, 8, 9]],),
    ([[5]],),
    ([[0]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        arg_copy = [row[:] for row in i[0]]
        result = test_func([row[:] for row in i[0]])
        assert main.set_zeroes(arg_copy) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
