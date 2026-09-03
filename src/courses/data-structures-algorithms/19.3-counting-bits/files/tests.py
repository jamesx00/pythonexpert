import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_count_bits(n):
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)
    return result

inputs = [
    (5,),
    (0,),
    (1,),
    (2,),
    (8,),
    (15,),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_count_bits(*i)
        assert main.count_bits(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
