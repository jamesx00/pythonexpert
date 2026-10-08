import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_edit_distance(a, b):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[n][m]

inputs = [
    ("plane", "plant"),
    ("abc", "abc"),
    ("", "abc"),
    ("draft", "crate"),
    ("sunday", "saturday"),
    ("a", "b"),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_edit_distance(*i)
        assert main.edit_distance(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
