import sys
import json
from collections import Counter

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(s, k):
    counts = Counter()
    left = 0
    max_freq = 0
    best = 0
    for right, ch in enumerate(s):
        counts[ch] += 1
        max_freq = max(max_freq, counts[ch])
        while (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best

inputs = [
    ("AABABBA", 1),
    ("ABAB", 2),
    ("AAAA", 0),
    ("ABCDE", 1),
    ("A", 0),
    ("AABBCC", 2),
    ("BAAAB", 2),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.longest_replacement(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
