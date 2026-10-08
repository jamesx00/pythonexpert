import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def max_sum_k(nums, k):
    window = sum(nums[:k])
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]
        best = max(best, window)
    return best

def check(fn, *args):
    return fn(*args)

cases = [
    ('max_sum_k', ([2, 1, 5, 1, 3, 2], 3)),
    ('max_sum_k', ([1, 2, 3], 3)),
    ('max_sum_k', ([5], 1)),
    ('max_sum_k', ([-1, -2, -3, -4], 2)),
    ('max_sum_k', ([1, 9, -1, -2, 7, 3, -1, 2], 4)),
    ('max_sum_k', ([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3)),
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
