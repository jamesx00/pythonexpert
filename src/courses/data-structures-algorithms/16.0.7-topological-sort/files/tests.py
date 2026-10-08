import sys
import json
import copy
from collections import deque

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def topo_sort(n, edges):
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for a, b in edges:
        graph[a].append(b)
        indegree[b] += 1

    queue = deque(i for i in range(n) if indegree[i] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return order if len(order) == n else []

def check(fn, n, edges):
    order = fn(n, edges)
    if order == []:
        return "cycle"
    position = {node: i for i, node in enumerate(order)}
    if sorted(order) != list(range(n)):
        return "invalid"
    for a, b in edges:
        if position[a] > position[b]:
            return "invalid"
    return "valid"

cases = [
    ('topo_sort', (4, [[0, 1], [0, 2], [1, 3], [2, 3]])),
    ('topo_sort', (2, [[0, 1], [1, 0]])),
    ('topo_sort', (1, [])),
    ('topo_sort', (3, [])),
    ('topo_sort', (6, [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]])),
    ('topo_sort', (4, [[0, 1], [1, 2], [2, 3], [3, 1]])),
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
