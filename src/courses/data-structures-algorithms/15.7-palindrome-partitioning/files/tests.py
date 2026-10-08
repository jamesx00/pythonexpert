import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_partition_palindromes(s):
    result = []

    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(list(path))
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if is_palindrome(piece):
                path.append(piece)
                backtrack(end, path)
                path.pop()

    if s == "":
        return [[]]
    backtrack(0, [])
    return result

def normalize(partitions):
    return sorted(partitions)

inputs = [
    ("aab",),
    ("a",),
    ("",),
    ("aba",),
    ("abc",),
    ("aa",),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = normalize(test_partition_palindromes(*i))
        assert normalize(main.partition_palindromes(*i)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
