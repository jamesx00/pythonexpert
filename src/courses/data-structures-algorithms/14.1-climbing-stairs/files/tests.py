import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_climb_stairs(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

inputs = [
    (2,),
    (3,),
    (4,),
    (5,),
    (1,),
    (0,),
    (10,),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_climb_stairs(*i)
        assert main.climb_stairs(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
