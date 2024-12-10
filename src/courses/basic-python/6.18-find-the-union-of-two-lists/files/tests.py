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

def test_find_union(list1, list2):
    result = []
    for v in list1:
        result.append(v)
    for v in list2:
        if v not in result:
            result.append(v)
    return result

inputs = [
    ([1, 2, 3, 4, 5, 6, 7], [4, 5, 6, 7, 8]),
    ([5, 6, 7, 8], [6, 7, 8, 9, 10, 11]), 
    ([1, 2, 3], [4, 5, 6]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_find_union(*i)
        assert main.find_union(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))