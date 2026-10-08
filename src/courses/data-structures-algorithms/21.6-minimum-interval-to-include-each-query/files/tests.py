import sys
import json
import heapq

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_min_interval_for_queries(intervals, queries):
    ordered = sorted(intervals, key=lambda iv: iv[0])
    answer = [-1] * len(queries)
    order = sorted(range(len(queries)), key=lambda i: queries[i])

    heap = []
    idx = 0
    for qi in order:
        q = queries[qi]
        while idx < len(ordered) and ordered[idx][0] <= q:
            start, end = ordered[idx]
            heapq.heappush(heap, (end - start + 1, end))
            idx += 1
        while heap and heap[0][1] < q:
            heapq.heappop(heap)
        if heap:
            answer[qi] = heap[0][0]

    return answer

inputs = [
    ([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5]),
    ([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22]),
    ([[1, 5]], [1, 3, 5, 6]),
    ([], [1, 2, 3]),
    ([[1, 10], [1, 3], [4, 10]], [1, 4, 10]),
    ([[1, 1], [2, 2], [3, 3]], [1, 2, 3, 4]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_min_interval_for_queries(*i)
        assert main.min_interval_for_queries(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
