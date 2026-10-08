import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_count_components(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    return len({find(x) for x in range(n)})

inputs = [
    (5, [[0, 1], [1, 2], [3, 4]]),
    (5, []),
    (4, [[0, 1], [1, 2], [2, 3]]),
    (1, []),
    (6, [[0, 1], [2, 3], [4, 5]]),
    (3, [[0, 1], [0, 2], [1, 2]]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_count_components(*i)
        assert main.count_components(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
