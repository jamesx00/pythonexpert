import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_reverse_bits(n):
    result = 0
    for i in range(32):
        bit = (n >> i) & 1
        result |= bit << (31 - i)
    return result

inputs = [
    (1,),
    (0,),
    (4294967295,),
    (43261596,),
    (2147483648,),
    (2,),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_reverse_bits(*i)
        assert main.reverse_bits(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
