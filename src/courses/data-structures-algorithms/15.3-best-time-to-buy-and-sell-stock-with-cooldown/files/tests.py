import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_max_profit(prices):
    if not prices:
        return 0
    n = len(prices)
    hold = [0] * n
    sold = [0] * n
    rest = [0] * n
    hold[0] = -prices[0]
    for i in range(1, n):
        hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])
        sold[i] = hold[i - 1] + prices[i]
        rest[i] = max(rest[i - 1], sold[i - 1])
    return max(sold[-1], rest[-1])

inputs = [
    ([1, 3, 2, 8, 4, 9],),
    ([1, 2, 3, 0, 2],),
    ([1],),
    ([],),
    ([5, 4, 3, 2, 1],),
    ([2, 1, 4, 5, 2, 9, 7],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_max_profit(*i)
        assert main.max_profit(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
