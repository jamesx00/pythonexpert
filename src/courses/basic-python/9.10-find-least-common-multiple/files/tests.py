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

def test_find_lcm(start_and_stop):
    # Find the maximum number between start and end
    end = max(start_and_stop)
    start = min(start_and_stop)
    # Initialize the LCM as the maximum number
    lcm = end
    # Keep increasing the LCM until it is divisible by all numbers in the range
    while True:
        divisible_by_all = True
        for num in range(start, end + 1):
            if lcm % num != 0:
                divisible_by_all = False
                break
        if divisible_by_all:
            break
        lcm += end  # Increment by the maximum number for efficiency
    return lcm
    
inputs = [
    ([1,5],),
    ([5,1],),
    ([3,10],),
    ([1,1],),
    ([2,7],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_find_lcm(*i)
        assert main.find_lcm(*i) == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))