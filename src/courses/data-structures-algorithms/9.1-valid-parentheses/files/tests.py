import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack

inputs = [
    ("()",),
    ("()[]{}",),
    ("(]",),
    ("([)]",),
    ("{[]}",),
    ("(",),
    ("",),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.is_valid(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
