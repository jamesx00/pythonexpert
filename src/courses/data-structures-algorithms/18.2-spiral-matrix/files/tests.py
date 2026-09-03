import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(matrix):
    if not matrix or not matrix[0]:
        return []
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result

inputs = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],),
    ([[1]],),
    ([[1, 2], [3, 4]],),
    ([[1], [2], [3]],),
    ([],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.spiral_order(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
