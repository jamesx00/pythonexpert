import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_longest_common_subsequence(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

inputs = [
    ("abcde", "ace"),
    ("abc", "abc"),
    ("abc", "def"),
    ("", "abc"),
    ("bsbininm", "jmjkbkjkv"),
    ("oxcpqrsvwf", "shmtulqrypy"),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_longest_common_subsequence(*i)
        assert main.longest_common_subsequence(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
