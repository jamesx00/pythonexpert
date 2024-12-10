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

def test_func(sentence):
    check = sentence.lower()
    current_character = None
    for i, c in enumerate(check):
        current_character = c

        if i == 0 and c == check[i + 1]:
            continue
        
        if i == len(check) - 1 and c != check[i - 1]:
            return c
        
        if check[i - 1] == c or c == check[i + 1]:
            continue
        
        return current_character

    return None
    
inputs = [
    ("aabbccdd",),
    ("aabbccd",),
    ("abcd",),
    ("001112222233454",),
    ("aaABbbcC00==5665OO",),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.find_first_non_repeated_character(*i) == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))