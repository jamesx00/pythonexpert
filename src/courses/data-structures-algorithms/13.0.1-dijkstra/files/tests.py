import sys
import json
import copy
import heapq

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def dijkstra(n, edges, start):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))

    dist = [float("inf")] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for nxt, w in graph[node]:
            if d + w < dist[nxt]:
                dist[nxt] = d + w
                heapq.heappush(heap, (dist[nxt], nxt))
    return [x if x != float("inf") else -1 for x in dist]

def check(fn, *args):
    return fn(*args)

cases = [
    ('dijkstra', (3, [[0, 1, 4], [0, 2, 1], [2, 1, 2]], 0)),
    ('dijkstra', (1, [], 0)),
    ('dijkstra', (3, [[0, 1, 5]], 0)),
    ('dijkstra', (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]], 0)),
    ('dijkstra', (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]], 2)),
    ('dijkstra', (5, [[0, 1, 2], [0, 2, 6], [1, 2, 3], [1, 3, 8], [2, 3, 0], [3, 4, 1]], 0)),
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
