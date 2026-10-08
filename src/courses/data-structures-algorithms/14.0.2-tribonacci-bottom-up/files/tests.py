import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def tribonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    a, b, c = 0, 1, 1
    for _ in range(n - 2):
        a, b, c = b, c, a + b + c
    return c

def check(fn, *args):
    return fn(*args)

cases = [
    ('tribonacci', (0,)),
    ('tribonacci', (1,)),
    ('tribonacci', (2,)),
    ('tribonacci', (4,)),
    ('tribonacci', (25,)),
    ('tribonacci', (37,)),
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
