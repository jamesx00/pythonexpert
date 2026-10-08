import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_min_cost_climbing_stairs(cost):
    n = len(cost)
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]

inputs = [
    ([10, 15, 20],),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1],),
    ([0, 0, 0, 0],),
    ([1, 2],),
    ([5, 3, 4, 2, 6],),
    ([2, 5],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_min_cost_climbing_stairs(*i)
        assert main.min_cost_climbing_stairs(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
