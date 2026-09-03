import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    result = 1.0
    base = x
    while n > 0:
        if n % 2 == 1:
            result *= base
        base *= base
        n //= 2
    return result

inputs = [
    (2.0, 10),
    (2.0, -2),
    (2.1, 3),
    (5.0, 0),
    (1.0, 1000),
    (-2.0, 3),
    (0.5, 4),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert round(main.my_pow(*i), 9) == round(result, 9)
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
