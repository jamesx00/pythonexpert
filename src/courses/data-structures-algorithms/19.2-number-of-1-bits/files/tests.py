import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_count_set_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

inputs = [
    (11,),
    (0,),
    (1,),
    (128,),
    (255,),
    (1023,),
    (4294967295,),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_count_set_bits(*i)
        assert main.count_set_bits(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
