import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(prices):
    if not prices:
        return 0
    min_price = prices[0]
    best = 0
    for p in prices[1:]:
        if p - min_price > best:
            best = p - min_price
        if p < min_price:
            min_price = p
    return best

inputs = [
    ([9, 2, 7, 1, 5, 3],),
    ([8, 6, 4, 2],),
    ([1, 2, 3, 4, 5],),
    ([5],),
    ([3, 3, 3, 3],),
    ([2, 4, 1, 7],),
    ([7, 1, 5, 3, 6, 4],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.max_profit(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
