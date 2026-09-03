import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_check_valid_string(s):
    lo = hi = 0
    for c in s:
        if c == '(':
            lo += 1
            hi += 1
        elif c == ')':
            lo -= 1
            hi -= 1
        else:
            lo -= 1
            hi += 1
        if hi < 0:
            return False
        lo = max(lo, 0)
    return lo == 0

inputs = [
    ("()",),
    ("(*)",),
    ("(*))",),
    ("(((*",),
    ("())",),
    (")(",),
    ("*",),
    ("((*)",),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_check_valid_string(*i)
        assert main.check_valid_string(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
