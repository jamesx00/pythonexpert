import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_coin_change(coins, amount):
    dp = [0] + [float('inf')] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

inputs = [
    ([1, 3, 4], 6),
    ([2, 5], 3),
    ([1], 0),
    ([1, 2, 5], 11),
    ([2], 3),
    ([1, 5, 10, 25], 30),
    ([5, 7], 3),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_coin_change(*i)
        assert main.coin_change(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
