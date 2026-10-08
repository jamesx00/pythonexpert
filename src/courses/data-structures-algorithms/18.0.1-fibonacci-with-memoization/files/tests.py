import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def fib(n):
    memo = {}

    def f(i):
        if i < 2:
            return i
        if i in memo:
            return memo[i]
        memo[i] = f(i - 1) + f(i - 2)
        return memo[i]

    return f(n)

def check(fn, *args):
    return fn(*args)

cases = [
    ('fib', (0,)),
    ('fib', (1,)),
    ('fib', (2,)),
    ('fib', (10,)),
    ('fib', (30,)),
    ('fib', (90,)),
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
