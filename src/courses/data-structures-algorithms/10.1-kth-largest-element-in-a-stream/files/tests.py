import sys
import json
import heapq

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(k, nums, add_vals):
    heap = list(nums)
    heapq.heapify(heap)
    while len(heap) > k:
        heapq.heappop(heap)
    output = []
    for val in add_vals:
        heapq.heappush(heap, val)
        while len(heap) > k:
            heapq.heappop(heap)
        output.append(heap[0])
    return output

def run_main(k, nums, add_vals):
    kth = main.KthLargest(k, nums)
    return [kth.add(val) for val in add_vals]

inputs = [
    (2, [3, 8], [5]),
    (2, [3, 8], [5, 1]),
    (2, [3, 8], [5, 10]),
    (1, [], [4, 2, 9]),
    (3, [4, 5, 8, 2], [3, 10]),
    (2, [], [-1, -1, -2]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert run_main(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
