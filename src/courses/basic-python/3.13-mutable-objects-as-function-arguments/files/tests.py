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

list_input = [1, 2, 3]

try:
    result = main.add_to_list(list_input, 4)
    assert result == [1, 2, 3, 4]
    results[1] = True
except Exception as e:
    results[1] = False

try:
    result = main.add_to_list(list_input, 4)
    assert id(list_input) != id(result)
    results[2] = True
except Exception as e:
    results[2] = False


sys.stdout.write(json.dumps(results))