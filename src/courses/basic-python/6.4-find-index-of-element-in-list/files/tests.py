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

results = {}

def my_get_index(the_list, value):
    for i, v in enumerate(the_list):
        if v == value: return i
    return None

try:
    the_list = [1,2,3]
    lookup_value = 1
    result = my_get_index(the_list, lookup_value)
    assert main.get_index(the_list, lookup_value) == result
    results[1] = True
except Exception:
    results[1] = False

try:
    the_list = [1,2,3]
    lookup_value = 0
    result = my_get_index(the_list, lookup_value)
    assert main.get_index(the_list, lookup_value) == result
    results[2] = True
except Exception:
    results[2] = False

try:
    the_list = ["A", "B", "C"]
    lookup_value = "A"
    result = my_get_index(the_list, lookup_value)
    assert main.get_index(the_list, lookup_value) == result
    results[3] = True
except Exception:
    results[3] = False

try:
    the_list = ["A", "B", "C"]
    lookup_value = "C"
    result = my_get_index(the_list, lookup_value)
    assert main.get_index(the_list, lookup_value) == result
    results[4] = True
except Exception:
    results[4] = False

try:
    the_list = ["A", "B", "C"]
    lookup_value = "a"
    result = my_get_index(the_list, lookup_value)
    assert main.get_index(the_list, lookup_value) == result
    results[5] = True
except Exception:
    results[5] = False

try:
    the_list = ["A", "B", "C"]
    lookup_value = 0
    result = my_get_index(the_list, lookup_value)
    assert main.get_index(the_list, lookup_value) == result
    results[6] = True
except Exception:
    results[6] = False

sys.stdout.write(json.dumps(results))