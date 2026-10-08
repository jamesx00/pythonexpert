import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def combine(n, k):
    result = []
    path = []

    def backtrack(start):
        if len(path) == k:
            result.append(path[:])
            return
        for num in range(start, n + 1):
            path.append(num)
            backtrack(num + 1)
            path.pop()

    backtrack(1)
    return result

def check(fn, *args):
    return fn(*args)

cases = [
    ('combine', (4, 2)),
    ('combine', (1, 1)),
    ('combine', (3, 3)),
    ('combine', (5, 1)),
    ('combine', (5, 3)),
    ('combine', (3, 0)),
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
