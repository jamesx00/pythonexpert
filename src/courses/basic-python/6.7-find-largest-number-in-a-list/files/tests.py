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

results = {}

try:
    numbers = [5, 10, 15, 20, 25]
    result = max(numbers)
    assert main.get_largest_number(numbers) == result
    results[1] = True
except Exception:
    results[1] = False

try:
    numbers = [x * 100 for x in range(1, 6)]
    result = max(numbers)
    assert main.get_largest_number(numbers) == result
    results[2] = True
except Exception:
    results[2] = False

try:
    numbers = [-10, -5, -20, -15, -25]
    result = max(numbers)
    assert main.get_largest_number(numbers) == result
    results[3] = True
except Exception:
    results[3] = False

try:
    numbers = [9, 7, 5, 3, 1, -1]
    result = max(numbers)
    assert main.get_largest_number(numbers) == result
    results[4] = True
except Exception:
    results[4] = False

sys.stdout.write(json.dumps(results))