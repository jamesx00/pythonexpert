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

def test_get_total(numbers):
    return sum(numbers)

inputs = [
    ([0,0,0,0,0],),
    ([1, -2, 3, -4, 5],), 
    ([2.5, 1.5, -3.5, 4.5],),
    ([-10, -20, -30, -40, -50],),
    ([7],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_get_total(*i)
        assert main.get_total(*i) == result
        results[index+1] = True
    except Exception:
        results[index+1] = False

sys.stdout.write(json.dumps(results))