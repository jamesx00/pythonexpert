import sys
import json
import heapq

from unittest.mock import patch
patch('builtins.print').start()

import main

def dist(p):
    return p[0] ** 2 + p[1] ** 2

def test_func(points, k):
    heap = [(dist(p), p[0], p[1]) for p in points]
    heapq.heapify(heap)
    closest = heapq.nsmallest(k, heap)
    return sorted(d for d, x, y in closest)

def normalize(points):
    return sorted(dist(p) for p in points)

inputs = [
    ([[1, 1], [4, 4], [0, 1], [3, 3]], 2),
    ([[3, 3], [5, -1], [-2, 4]], 1),
    ([[0, 0], [1, 0], [2, 0]], 2),
    ([[-5, 4], [-6, -1], [3, 1]], 3),
    ([[1, 2], [-1, -2], [1, -2], [-1, 2]], 2),
    ([[7, 7]], 1),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        student = main.k_closest(*i)
        assert len(student) == i[1]
        assert normalize(student) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
