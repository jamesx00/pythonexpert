import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_rob(houses):
    prev, curr = 0, 0
    for h in houses:
        prev, curr = curr, max(curr, prev + h)
    return curr

inputs = [
    ([2, 7, 9, 3, 1],),
    ([1, 2, 3, 1],),
    ([2, 1, 1, 2],),
    ([5],),
    ([5, 1],),
    ([0, 0, 0],),
    ([4, 1, 2, 7, 5, 3, 1],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_rob(*i)
        assert main.rob(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
