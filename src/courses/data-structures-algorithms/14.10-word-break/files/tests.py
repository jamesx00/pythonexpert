import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_word_break(s, word_dict):
    words = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[n]

inputs = [
    ("pineapplepen", ["pine", "apple", "pen"]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
    ("leetcode", ["leet", "code"]),
    ("applepenapple", ["apple", "pen"]),
    ("aaaaaaa", ["aaaa", "aaa"]),
    ("aaaaaaab", ["aaaa", "aaa"]),
    ("", ["a"]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_word_break(*i)
        assert main.word_break(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
