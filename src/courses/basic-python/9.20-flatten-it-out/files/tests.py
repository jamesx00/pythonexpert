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

def test_func(input_list):
    flattened_list = []
    for item in input_list:
        if isinstance(item, list):
            flattened_list.extend(test_func(item))
        else:
            flattened_list.append(item)
    return flattened_list

    
inputs = [
    ([5, 6, 7, 8],),
    ([[1], [2], [3], [4]],),
    ([1, [2, 3], [4, [5, 6]]],),
    ([7, [8, 9, [10]], 11],),
    (['a', ['b', ['c', 'd']]],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.flatten_list(*i) == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))