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

def test_func(target):
    fib_nums = [0, 1]  # Start with the first two Fibonacci numbers
    while fib_nums[-1] < target:
        next_fib = fib_nums[-1] + fib_nums[-2]  # Compute the next Fibonacci number
        if next_fib > target:
            break
        fib_nums.append(next_fib)
    return fib_nums
    
inputs = [
    (1,),
    (10, ),
    (20, ),
    (100, ),
    (1000, ),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.find_fibonacci(*i) == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))