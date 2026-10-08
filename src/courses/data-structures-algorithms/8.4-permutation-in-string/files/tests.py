import sys
import json
from collections import Counter

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(pattern, text):
    need = Counter(pattern)
    have = Counter()
    L = len(pattern)
    if L > len(text):
        return False
    for i in range(L):
        have[text[i]] += 1
    if have == need:
        return True
    for i in range(L, len(text)):
        have[text[i]] += 1
        have[text[i - L]] -= 1
        if have[text[i - L]] == 0:
            del have[text[i - L]]
        if have == need:
            return True
    return False

inputs = [
    ("abc", "eidbacoo"),
    ("abc", "eidboaoo"),
    ("ab", "eidbaaooo"),
    ("adc", "dcda"),
    ("xyz", "xy"),
    ("a", "a"),
    ("hello", "ooolleoooleh"),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.contains_permutation(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
