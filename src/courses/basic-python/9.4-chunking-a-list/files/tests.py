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

def test_chunk_it_up(the_list, length):
    result = []
    sublist = []
    for i, value in enumerate(the_list):
        if len(sublist) == length:
            result.append(sublist)
            sublist = []
        elif i == len(the_list) -1:
            result.append(sublist)
        sublist.append(value)
    return result

inputs = [
    ([1, 2, 3, 4, 5, 6, 7, 8], 2),
    (['apple', 'banana', 'orange', 'grape', 'kiwi', 'mango'], 4), 
    ([True, False, True, True], 1),
    ([10, 20, 30, 40, 50], 6),
    ([],3),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_chunk_it_up(*i)
        assert main.chunk_it_up(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))