import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def first_unique(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1

def check(fn, *args):
    return fn(*args)

cases = [
    ('first_unique', ('leetcode',)),
    ('first_unique', ('loveleetcode',)),
    ('first_unique', ('aabb',)),
    ('first_unique', ('',)),
    ('first_unique', ('z',)),
    ('first_unique', ('aabbc',)),
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
