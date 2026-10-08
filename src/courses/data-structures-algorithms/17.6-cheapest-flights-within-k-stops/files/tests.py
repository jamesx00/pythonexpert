import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_find_cheapest_price(n, flights, src, dst, k):
    prices = [float("inf")] * n
    prices[src] = 0

    for _ in range(k + 1):
        updated = prices[:]
        for u, v, w in flights:
            if prices[u] != float("inf") and prices[u] + w < updated[v]:
                updated[v] = prices[u] + w
        prices = updated

    return prices[dst] if prices[dst] != float("inf") else -1

inputs = [
    (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1),
    (3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0),
    (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 5]], 0, 3, 1),
    (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 5]], 0, 3, 2),
    (3, [[0, 1, 100]], 0, 2, 5),
    (2, [[0, 1, 10]], 0, 1, 0),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_find_cheapest_price(*i)
        assert main.find_cheapest_price(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
