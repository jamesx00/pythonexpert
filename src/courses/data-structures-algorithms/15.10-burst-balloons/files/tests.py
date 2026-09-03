import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_max_coins(nums):
    balloons = [1] + nums + [1]
    n = len(balloons)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            best = 0
            for k in range(left + 1, right):
                coins = balloons[left] * balloons[k] * balloons[right] + dp[left][k] + dp[k][right]
                best = max(best, coins)
            dp[left][right] = best
    return dp[0][n - 1]

inputs = [
    ([4, 2, 6, 9],),
    ([1, 5],),
    ([7],),
    ([3, 3],),
    ([2, 4, 3],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_max_coins(*i)
        assert main.max_coins(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
