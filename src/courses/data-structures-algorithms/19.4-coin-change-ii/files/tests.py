import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_count_ways(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]

inputs = [
    (5, [1, 2, 5]),
    (3, [2]),
    (10, [10]),
    (0, [1, 2, 3]),
    (7, [2, 3, 5]),
    (4, [1, 2, 3]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_count_ways(*i)
        assert main.count_ways(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
