import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_reverse_integer(x):
    sign = -1 if x < 0 else 1
    digits = abs(x)
    reversed_num = 0
    while digits:
        reversed_num = reversed_num * 10 + digits % 10
        digits //= 10
    reversed_num *= sign
    if reversed_num < -2147483648 or reversed_num > 2147483647:
        return 0
    return reversed_num

inputs = [
    (513,),
    (-120,),
    (0,),
    (100,),
    (1563847412,),
    (-2147483648,),
    (7,),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_reverse_integer(*i)
        assert main.reverse_integer(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
