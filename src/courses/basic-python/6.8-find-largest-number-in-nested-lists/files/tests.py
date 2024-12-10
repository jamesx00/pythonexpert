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

def test_find_largest_number(lists):
    return max([max(l) for l in lists])

results = {}

try:
    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    result = test_find_largest_number(input)
    assert main.find_largest_number(input) == result
    results[1] = True
except Exception:
    results[1] = False

try:
    input = [[15, 25, 35], [45, 55, 65], [75, 85, 95], [105, 115, 125]]
    result = test_find_largest_number(input)
    assert main.find_largest_number(input) == result
    results[2] = True
except Exception:
    results[2] = False

try:
    input = [[100, 200, 300], [400, 500, 600], [700, 800, 900], [1000, 1100, 1200]]
    result = test_find_largest_number(input)
    assert main.find_largest_number(input) == result
    results[3] = True
except Exception:
    results[3] = False

try:
    input = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9], [-10, -11, -12]]
    result = test_find_largest_number(input)
    assert main.find_largest_number(input) == result
    results[4] = True
except Exception:
    results[4] = False

try:
    input = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    result = test_find_largest_number(input)
    assert main.find_largest_number(input) == result
    results[5] = True
except Exception:
    results[5] = False

sys.stdout.write(json.dumps(results))