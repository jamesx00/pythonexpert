import sys
import re
import json
import math

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()

try:
    import main
except Exception:
    pass

def test_is_prime(number):
    
    if number == 1:
        return False
    if number == 2:
        return True

    for num in range(2, number):
        if num > math.sqrt(number):
            break
        if number % num == 0:
            return False

    return True
    

inputs = [
    (2,),
    (2,),
    (97,),
    (121,),
    (999,),
    (10007,),
    (99991,),
    (100003,),
    (1000000,),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_is_prime(*i)
        assert main.is_prime(*i) == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))