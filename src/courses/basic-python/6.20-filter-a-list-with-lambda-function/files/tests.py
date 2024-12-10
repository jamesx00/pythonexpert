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

def test_filter_list(the_list, condition):
    return [x for x in the_list if condition(x)]

inputs = [
    ([-2, -1, 0, 1, 2, 3, 4, 5], lambda x: x >= 0),
    ([10.0, 15, 2, 2.5, 9, -1, 9.9], lambda x: type(x) == int),
    ([1, "b", 3, "d", 5, "f"], lambda x: type(x) == str),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_filter_list(*i)
        assert main.filter_list(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))