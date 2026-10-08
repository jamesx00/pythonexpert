import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(digits):
    digits = digits[:]
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

inputs = [
    ([1, 2, 9],),
    ([9, 9],),
    ([1, 2, 3],),
    ([0],),
    ([4, 3, 2, 9],),
    ([9],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.plus_one(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
