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

def test_find_different_elements(list1, list2):
    result = []
    for v in list1:
        if v not in list2:
            result.append(v)
    for v in list2:
        if v not in list1:
            result.append(v)
    return result
    
inputs = [
    ([1,2,3,4,5], [4,5,6,7,8]),
    (['apple', 'banana', 'grape', 'orange'], ['banana', 'grape', 'kiwi', 'mango']),
    ([1,2,3,4,5], [1,2,3,4,5]),
    ([10, 20, 30, 40], []),
    ([], ['apple', 'banana', 'cherry']),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_find_different_elements(*i)
        assert main.find_different_elements(*i) == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))