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

def test_func(the_list):
    mode_count = {}
    max_count = 0
    modes = []

    for item in the_list:
        mode_count[item] = mode_count.get(item, 0) + 1
        max_count = max(max_count, mode_count[item])

    for item, count in mode_count.items():
        if count == max_count:
            modes.append(item)

    return modes
    
inputs = [
    ([1, "apple", "apple", "banana", 1, None, "apple"],),
    ([1, 2, 3, "apple", "banana", 2, "banana", None],),
    (["apple", "orange", "apple", "banana", None, None, "banana", "orange", "apple"],),
    ([None, None, None, None, None,],),
    ([1, "1", 2, "2", 3, "3"],)
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.find_the_mode(*i)  == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))