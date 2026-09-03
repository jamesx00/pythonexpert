import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_longest_palindrome(s):
    if not s:
        return ""
    start, end = 0, 0

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1

    for i in range(len(s)):
        l1, r1 = expand(i, i)
        if r1 - l1 > end - start:
            start, end = l1, r1
        l2, r2 = expand(i, i + 1)
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]

# indices (1-based) where multiple max-length palindromes exist, so we only
# check length + palindrome-ness + substring membership rather than exact match
ambiguous = {1, 5}

inputs = [
    ("babad",),
    ("cbbd",),
    ("a",),
    ("forgeeksskeegfor",),
    ("abcde",),
    ("racecarxyz",),
    ("",),
]

results = {}

for index, i in enumerate(inputs):
    try:
        expected = test_longest_palindrome(*i)
        actual = main.longest_palindrome(*i)
        if (index + 1) in ambiguous:
            ok = (
                isinstance(actual, str)
                and len(actual) == len(expected)
                and actual == actual[::-1]
                and actual in i[0]
            )
            assert ok
        else:
            assert actual == expected
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
