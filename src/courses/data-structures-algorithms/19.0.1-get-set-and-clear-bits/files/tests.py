import sys
import json
import copy

from unittest.mock import patch
patch('builtins.print').start()

import main
from main import *

def get_bit(x, i):
    return (x >> i) & 1


def set_bit(x, i):
    return x | (1 << i)


def clear_bit(x, i):
    return x & ~(1 << i)

def check(fn, *args):
    return fn(*args)

cases = [
    ('get_bit', (5, 0)),
    ('get_bit', (5, 1)),
    ('get_bit', (8, 3)),
    ('set_bit', (5, 1)),
    ('set_bit', (5, 2)),
    ('set_bit', (0, 4)),
    ('clear_bit', (5, 0)),
    ('clear_bit', (5, 1)),
    ('clear_bit', (255, 7)),
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
