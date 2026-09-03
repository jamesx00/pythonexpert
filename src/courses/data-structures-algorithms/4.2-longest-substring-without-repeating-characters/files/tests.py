import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(s):
    seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        best = max(best, right - left + 1)
    return best

inputs = [
    ("xyzxyz",),
    ("aaaa",),
    ("",),
    ("pwwkew",),
    ("dvdf",),
    ("abcdefg",),
    ("bbtablud",),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.longest_unique_substring(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
