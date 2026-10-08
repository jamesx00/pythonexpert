import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo

def check(fn, *args):
    return fn(*args)

cases = [
    ('lower_bound', ([1, 3, 3, 5], 3)),
    ('lower_bound', ([1, 3, 3, 5], 4)),
    ('lower_bound', ([1, 3, 3, 5], 0)),
    ('lower_bound', ([1, 3, 3, 5], 9)),
    ('lower_bound', ([], 5)),
    ('lower_bound', ([2, 2, 2, 2], 2)),
    ('lower_bound', ([1, 2, 4, 8, 16, 32, 64], 17)),
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
