import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_valid_tree(n, edges):
    if len(edges) != n - 1:
        return False
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb

    return len({find(x) for x in range(n)}) == 1

inputs = [
    (4, [[0, 1], [1, 2], [2, 3]]),
    (4, [[0, 1], [1, 2], [2, 3], [1, 3]]),
    (5, [[0, 1], [2, 3]]),
    (1, []),
    (3, [[0, 1], [1, 2], [0, 2]]),
    (2, [[0, 1]]),
    (2, []),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_valid_tree(*i)
        assert main.valid_tree(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
