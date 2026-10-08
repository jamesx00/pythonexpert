import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def move_zeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1

def check(fn, nums):
    fn(nums)
    return nums

cases = [
    ('move_zeroes', ([0, 1, 0, 3, 12],)),
    ('move_zeroes', ([0],)),
    ('move_zeroes', ([1, 2, 3],)),
    ('move_zeroes', ([0, 0, 1],)),
    ('move_zeroes', ([4, 0, 5, 0, 0, 6],)),
    ('move_zeroes', ([],)),
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
