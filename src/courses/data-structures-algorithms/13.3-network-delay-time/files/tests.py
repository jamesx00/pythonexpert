import sys
import json
import heapq
from collections import defaultdict

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_network_delay_time(times, n, start):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {}
    min_heap = [(0, start)]

    while min_heap:
        d, node = heapq.heappop(min_heap)
        if node in dist:
            continue
        dist[node] = d
        for nei, w in graph[node]:
            if nei not in dist:
                heapq.heappush(min_heap, (d + w, nei))

    if len(dist) != n:
        return -1
    return max(dist.values())

inputs = [
    ([[1, 2, 2], [1, 3, 5], [2, 3, 1], [3, 4, 1]], 4, 1),
    ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2),
    ([[1, 2, 1]], 2, 1),
    ([[1, 2, 1]], 2, 2),
    ([[1, 2, 1], [2, 3, 2], [1, 3, 5]], 3, 1),
    ([[1, 2, 1]], 3, 1),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_network_delay_time(*i)
        assert main.network_delay_time(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
