import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def _rob_line(houses):
    prev, curr = 0, 0
    for h in houses:
        prev, curr = curr, max(curr, prev + h)
    return curr

def test_rob_circular(houses):
    if len(houses) == 1:
        return houses[0]
    return max(_rob_line(houses[1:]), _rob_line(houses[:-1]))

inputs = [
    ([2, 3, 2],),
    ([1, 2, 3, 1],),
    ([1, 2, 3],),
    ([5],),
    ([5, 5],),
    ([0, 0, 0, 0],),
    ([6, 7, 1, 3, 8, 2, 4],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_rob_circular(*i)
        assert main.rob_circular(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
