import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_partition_labels(s):
    last = {c: i for i, c in enumerate(s)}
    result = []
    start = end = 0
    for i, c in enumerate(s):
        end = max(end, last[c])
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result

inputs = [
    ("abacbc",),
    ("abcabc",),
    ("aaaa",),
    ("abcdef",),
    ("eccbbbeee",),
    ("aabbccddeeff",),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_partition_labels(*i)
        assert main.partition_labels(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
