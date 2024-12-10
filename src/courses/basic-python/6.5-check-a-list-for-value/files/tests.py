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

try:
    the_list = [1,2,3]
    lookup_value = 1
    result = lookup_value in the_list
    assert main.does_list_contain(the_list, lookup_value) == result
    results[1] = True
except Exception:
    results[1] = False

try:
    the_list = [1,2,3]
    lookup_value = 0
    result = lookup_value in the_list
    assert main.does_list_contain(the_list, lookup_value) == result
    results[2] = True
except Exception:
    results[2] = False

try:
    the_list = ["A", "B", "C"]
    lookup_value = "A"
    result = lookup_value in the_list
    assert main.does_list_contain(the_list, lookup_value) == result
    results[3] = True
except Exception:
    results[3] = False

try:
    the_list = ["A", "B", "C"]
    lookup_value = "a"
    result = lookup_value in the_list
    assert main.does_list_contain(the_list, lookup_value) == result
    results[4] = True
except Exception:
    results[4] = False

try:
    the_list = ["A", "B", "C"]
    lookup_value = "0"
    result = lookup_value in the_list
    assert main.does_list_contain(the_list, lookup_value) == result
    results[5] = True
except Exception:
    results[5] = False

sys.stdout.write(json.dumps(results))