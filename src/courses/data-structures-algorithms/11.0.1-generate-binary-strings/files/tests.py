import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def binary_strings(n):
    result = []
    path = []

    def backtrack():
        if len(path) == n:
            result.append("".join(path))
            return
        for ch in "01":
            path.append(ch)
            backtrack()
            path.pop()

    backtrack()
    return result

def check(fn, *args):
    return fn(*args)

cases = [
    ('binary_strings', (2,)),
    ('binary_strings', (1,)),
    ('binary_strings', (0,)),
    ('binary_strings', (3,)),
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
