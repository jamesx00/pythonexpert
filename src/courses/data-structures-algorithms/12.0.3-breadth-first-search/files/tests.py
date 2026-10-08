import sys
import json
import copy
from collections import deque

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def bfs_order(n, edges, start):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def check(fn, *args):
    return fn(*args)

cases = [
    ('bfs_order', (4, [[0, 1], [0, 2], [1, 3]], 0)),
    ('bfs_order', (1, [], 0)),
    ('bfs_order', (5, [[0, 1], [1, 2], [2, 0], [3, 4]], 0)),
    ('bfs_order', (6, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], 0)),
    ('bfs_order', (6, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], 3)),
    ('bfs_order', (5, [[0, 4], [0, 1], [1, 2], [2, 3], [3, 4]], 0)),
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
