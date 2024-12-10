import sys
import re
import json

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()

results = {}


numbers = [1, 2, 3, 4, 5]

try:
    import main
except Exception as e:
    pass

try:
    assert main.type_of_object == list
    results[1] = True
except Exception as e:
    results[1] = False

sys.stdout.write(json.dumps(results))