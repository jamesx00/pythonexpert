import sys
import json
import copy
import heapq

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def k_smallest(nums, k):
    heap = list(nums)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(k)]

def check(fn, *args):
    return fn(*args)

cases = [
    ('k_smallest', ([5, 1, 4, 2, 3], 2)),
    ('k_smallest', ([7, 7, 7], 2)),
    ('k_smallest', ([3, -1, 2], 3)),
    ('k_smallest', ([1, 2, 3], 0)),
    ('k_smallest', ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 4)),
    ('k_smallest', ([4], 1)),
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
