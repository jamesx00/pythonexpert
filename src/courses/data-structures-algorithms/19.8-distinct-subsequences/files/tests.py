import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_num_distinct(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]
    return dp[n][m]

inputs = [
    ("xcaxcxaxxc", "xc"),
    ("mississippi", "mis"),
    ("abc", "abc"),
    ("abc", "abcd"),
    ("aaaa", "aa"),
    ("", "a"),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_num_distinct(*i)
        assert main.num_distinct(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
