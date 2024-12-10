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

def test_calculate_range_sum(start_and_end):
    lower = min(start_and_end)
    higher = max(start_and_end)
    return sum(range(lower, higher + 1))
    
inputs = [
    ([1,5],),
    ([10, 0],),
    ([-5, -1],),
    ([0, -10],),
    ([105, 100],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_calculate_range_sum(*i)
        assert main.calculate_range_sum(*i) == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))