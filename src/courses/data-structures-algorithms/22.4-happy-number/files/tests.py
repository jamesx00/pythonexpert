import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1

inputs = [
    (19,),
    (2,),
    (1,),
    (7,),
    (4,),
    (100,),
    (89,),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.is_happy(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
