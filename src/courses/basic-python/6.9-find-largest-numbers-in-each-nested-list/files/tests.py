import sys
import re
import json

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()

try:
    import main
except Exception:
    pass

def test_find_largest_numbers(lists):
    result = []
    for l in lists:
        if len(l) == 0:
            result.append(None)
        else:
            result.append(max(l))
    return result

results = {}

inputs = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], []],
    [[15, 25, 35], [45, 55, 65], [], [75, 85, 95], [105, 115, 125]],
    [[100, 200, 300], [400, 500, 600], [700, 800, 900], [1000, 1100, 1200]],
    [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9], [-10, -11, -12]],
    [[], [], [], []],
]

for index, i in enumerate(inputs):
    try:
        result = test_find_largest_numbers(i)
        assert main.find_largest_numbers(i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False
    
sys.stdout.write(json.dumps(results))