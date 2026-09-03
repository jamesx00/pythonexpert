import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows, cols = len(matrix), len(matrix[0])
    lo, hi = 0, rows * cols - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // cols][mid % cols]
        if val == target:
            return True
        elif val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False

inputs = [
    ([[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23]], 13),
    ([[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23]], 6),
    ([[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23]], 1),
    ([[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23]], 23),
    ([[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23]], 24),
    ([[5]], 5),
    ([], 3),
    ([[]], 3),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.search_matrix(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
