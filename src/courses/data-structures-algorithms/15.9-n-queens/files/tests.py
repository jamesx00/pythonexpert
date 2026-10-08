import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_n_queens(n):
    count = 0
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            backtrack(row + 1)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return count

inputs = [
    (4,),
    (1,),
    (2,),
    (3,),
    (5,),
    (6,),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_n_queens(*i)
        assert main.n_queens(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
