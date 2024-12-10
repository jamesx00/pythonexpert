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

def test_remove_duplicates(values):
    result = []
    for v in values:
        if v not in result:
            result.append(v)
    return result

inputs = [
    [1, 1, 1, 1, 1],
    ['a', "A", 'b', 'b', 'B', 'B'],
    [],
    [True, False, True, False],
    ['apple', 'banana', 'banana', 'banana'],
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_remove_duplicates(i)
        assert main.remove_duplicates(i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))