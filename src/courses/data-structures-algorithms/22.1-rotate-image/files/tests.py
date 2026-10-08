import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

inputs = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
    ([[1, 2], [3, 4]],),
    ([[5]],),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],),
    ([[1, -2], [-3, 4]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        arg_copy = [row[:] for row in i[0]]
        result = test_func([row[:] for row in i[0]])
        assert main.rotate(arg_copy) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
