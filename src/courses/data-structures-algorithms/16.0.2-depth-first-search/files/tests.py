import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def dfs_order(n, edges, start):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    order = []

    def visit(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order

def check(fn, *args):
    return fn(*args)

cases = [
    ('dfs_order', (4, [[0, 1], [0, 2], [1, 3]], 0)),
    ('dfs_order', (1, [], 0)),
    ('dfs_order', (5, [[0, 1], [1, 2], [2, 0], [3, 4]], 0)),
    ('dfs_order', (5, [[0, 1], [1, 2], [2, 0], [3, 4]], 4)),
    ('dfs_order', (6, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], 0)),
    ('dfs_order', (6, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], 3)),
]

results = {}

for index, (name, args) in enumerate(cases):
    try:
        expected = check(globals()[name], *copy.deepcopy(args))
        assert check(getattr(main, name), *copy.deepcopy(args)) == expected
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
