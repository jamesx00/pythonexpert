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

def test_func(the_list, *args):
    result = []
    for v in the_list:
        if v not in args: result.append(v)
    return result
    
inputs = [
    ([True, False, None],),
    ([1, 2, 3, 3, 4], 3),
    ([1, 1, 2, 2, 3, 4, 5, 6], 1, 2),
    (["Apple", "Banana", "Cherry"], "Apple", "Banana", "Cherry"),
    (["Hello, 123", "OpenAI GPT-3.5", 42, "Python Programming", 9876, "Data Science 101", 777, "Machine Learning", 1234, "Web Development"], [42, 9876, 777, 1234]),
]

results = {}

try:
    main.remove_values([1, 2, 3, 4, 5], 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    results[0] = True
except Exception as e:
    results[0] = False

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.remove_values(*i) == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))