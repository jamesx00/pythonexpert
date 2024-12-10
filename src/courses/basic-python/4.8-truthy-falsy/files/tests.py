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
    assert main.is_empty_string("") == True
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert main.is_empty_string("Not Empty") == False
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))