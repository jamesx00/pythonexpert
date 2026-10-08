import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_clone_graph(adj_list):
    if not adj_list:
        return []

    clones = {}

    def dfs(node):
        if node in clones:
            return clones[node]
        clones[node] = []
        for neighbor in adj_list[node]:
            clones[node].append(neighbor)
        for neighbor in adj_list[node]:
            dfs(neighbor)
        return clones[node]

    dfs(0)
    return [clones[i] for i in range(len(adj_list))]

inputs = [
    ([[1, 2], [0, 2], [0, 1]],),
    ([],),
    ([[]],),
    ([[1], [0]],),
    ([[1, 3], [0, 2], [1, 3], [0, 2]],),
    ([[1], [0, 2], [1]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_clone_graph(*i)
        cloned = main.clone_graph(*i)
        assert cloned == result
        assert cloned is not i[0]
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
