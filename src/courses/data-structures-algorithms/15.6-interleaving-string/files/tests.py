import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_is_interleave(s1, s2, s3):
    n, m = len(s1), len(s2)
    if n + m != len(s3):
        return False
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            ok = False
            if i > 0 and dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                ok = True
            if not ok and j > 0 and dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                ok = True
            dp[i][j] = ok
    return dp[n][m]

inputs = [
    ("abc", "def", "adbcef"),
    ("abc", "def", "abdecf"),
    ("", "", ""),
    ("abc", "", "abc"),
    ("aabcc", "dbbca", "aadbbbaccc"),
    ("ab", "bc", "babc"),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_is_interleave(*i)
        assert main.is_interleave(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
