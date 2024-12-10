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

results = {}

try:
    list_input = [1, 2]
    result = main.add_list_item(3, list_input)
    assert result == [1, 2, 3]
    results[1] = True
except Exception as e:
    results[1] = False

try:
    result_1 = main.add_list_item(1)
    result_2 = main.add_list_item(2)
    assert result_1 == [1]
    assert result_2 == [2]
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))