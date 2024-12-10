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

def test_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

inputs = [
    (5, ),
    (0, ),
    (10, )
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_factorial(*i)
        assert main.factorial(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))