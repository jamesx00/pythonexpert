import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_can_complete_circuit(gas, cost):
    total = 0
    tank = 0
    start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:
            start = i + 1
            tank = 0
    return start if total >= 0 else -1

inputs = [
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
    ([2, 3, 4], [3, 4, 3]),
    ([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]),
    ([3, 3, 4], [3, 4, 4]),
    ([4, 5, 2, 6, 5, 3], [3, 2, 7, 3, 2, 9]),
    ([7], [6]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_can_complete_circuit(*i)
        assert main.can_complete_circuit(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
