import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_count_palindromic_substrings(s):
    n = len(s)
    count = 0

    def expand(l, r):
        c = 0
        while l >= 0 and r < n and s[l] == s[r]:
            c += 1
            l -= 1
            r += 1
        return c

    for i in range(n):
        count += expand(i, i)
        count += expand(i, i + 1)
    return count

inputs = [
    ("aaa",),
    ("abc",),
    ("",),
    ("aba",),
    ("abba",),
    ("racecar",),
    ("z",),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_count_palindromic_substrings(*i)
        assert main.count_palindromic_substrings(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
