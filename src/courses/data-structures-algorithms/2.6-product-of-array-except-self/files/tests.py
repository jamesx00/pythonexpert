import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_product_except_self(nums):
    n = len(nums)
    output = [1] * n
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]
    return output

inputs = [
    ([2, 3, 4, 5],),
    ([1, 1, 1, 1],),
    ([1, 2],),
    ([-1, 2, -3],),
    ([0, 4, 5],),
    ([3, 0, 0, 6],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_product_except_self(*i)
        assert main.product_except_self(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
