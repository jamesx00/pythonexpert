import sys
import json
import copy
from collections import deque

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def shortest_path(n, edges, start, end):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    dist = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == end:
            return dist[node]
        for neighbor in graph[node]:
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return -1

def check(fn, *args):
    return fn(*args)

cases = [
    ('shortest_path', (4, [[0, 1], [1, 2], [2, 3], [0, 3]], 0, 2)),
    ('shortest_path', (3, [[0, 1]], 0, 2)),
    ('shortest_path', (1, [], 0, 0)),
    ('shortest_path', (6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [0, 5]], 0, 4)),
    ('shortest_path', (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 4, 0)),
    ('shortest_path', (6, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5]], 0, 5)),
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
