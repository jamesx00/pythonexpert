import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def next_greater(nums):
    result = [-1] * len(nums)
    stack = []
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            result[stack.pop()] = x
        stack.append(i)
    return result

def check(fn, *args):
    return fn(*args)

cases = [
    ('next_greater', ([2, 1, 3, 2, 4],)),
    ('next_greater', ([5, 4, 3],)),
    ('next_greater', ([1, 2, 3],)),
    ('next_greater', ([],)),
    ('next_greater', ([7],)),
    ('next_greater', ([3, 3, 4],)),
    ('next_greater', ([4, 1, 2, 5, 3],)),
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
