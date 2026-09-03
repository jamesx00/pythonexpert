import sys
import json
import heapq

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_min_cost_connect_points(points):
    n = len(points)
    if n <= 1:
        return 0

    visited = [False] * n
    min_heap = [(0, 0)]
    total = 0
    connected = 0

    while min_heap and connected < n:
        cost, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total += cost
        connected += 1
        for v in range(n):
            if not visited[v]:
                dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                heapq.heappush(min_heap, (dist, v))

    return total

inputs = [
    ([[0, 0], [2, 2], [3, 10]],),
    ([[0, 0], [2, 2]],),
    ([[0, 0]],),
    ([[0, 0], [1, 1], [1, 0], [-1, 1]],),
    ([[3, 12], [-2, 5], [-4, 1]],),
    ([[0, 0], [5, 0], [10, 0], [15, 0]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_min_cost_connect_points(*i)
        assert main.min_cost_connect_points(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
