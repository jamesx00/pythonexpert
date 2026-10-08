import sys
import json
import heapq

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(stones):
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        a = -heapq.heappop(heap)
        b = -heapq.heappop(heap)
        if a != b:
            heapq.heappush(heap, -(a - b))
    return -heap[0] if heap else 0

inputs = [
    ([8, 4, 3, 2],),
    ([2, 7, 4, 1, 8, 1],),
    ([1],),
    ([],),
    ([5, 5],),
    ([10, 4, 2, 10],),
    ([3, 3, 3, 3],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.last_stone_weight(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
