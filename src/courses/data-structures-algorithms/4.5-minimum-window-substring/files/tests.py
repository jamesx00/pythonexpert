import sys
import json
from collections import Counter

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(text, chars):
    if not chars or not text:
        return ""
    need = Counter(chars)
    missing = len(chars)
    left = 0
    best = (float("inf"), 0, 0)
    for right, ch in enumerate(text):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right + 1)
            need[text[left]] += 1
            if need[text[left]] > 0:
                missing += 1
            left += 1
    return "" if best[0] == float("inf") else text[best[1]:best[2]]

inputs = [
    ("ADOBECODEBANC", "ABC"),
    ("aa", "aa"),
    ("a", "aa"),
    ("abc", "b"),
    ("acbbaca", "aba"),
    ("xyz", "w"),
    ("aaflslflsldkalskaaa", "aaa"),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.min_window(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
