import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_sum_of_two(a, b):
    mask = 0xFFFFFFFF
    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    if a > 0x7FFFFFFF:
        a = ~(a ^ mask)
    return a

inputs = [
    (3, 5),
    (-2, 3),
    (0, 0),
    (-5, -7),
    (12, -12),
    (100, 250),
    (-1, 1),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_sum_of_two(*i)
        assert main.sum_of_two(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
