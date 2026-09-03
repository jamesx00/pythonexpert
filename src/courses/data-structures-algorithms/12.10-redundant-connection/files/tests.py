import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_find_redundant_connection(edges):
    parent = {}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        parent.setdefault(a, a)
        parent.setdefault(b, b)

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return [a, b]
        parent[ra] = rb
    return []

inputs = [
    ([[1, 2], [1, 3], [2, 3]],),
    ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]],),
    ([[1, 2], [1, 3], [1, 4], [3, 4]],),
    ([[1, 4], [3, 4], [1, 3], [1, 2]],),
    ([[1, 2], [2, 3], [1, 3]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_find_redundant_connection(*i)
        assert main.find_redundant_connection(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
