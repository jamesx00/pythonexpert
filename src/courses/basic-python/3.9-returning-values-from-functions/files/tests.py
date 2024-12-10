import inspect
import re
import sys
import json

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()
    
try:
    import main
except Exception as e:
    sys.stderr.write(json.dumps({}))
    quit()

results = {}

try:
    assert callable(main.add_numbers)
    results[1] = True
except Exception:
    results[1] = False

try:
    assert main.add_numbers.__code__.co_argcount == 2
    results[2] = True
except Exception:
    results[2] = False


try:
    assert main.add_numbers(5, 5) == 10
    results[3] = True
except Exception:
    results[3] = False

try:
    assert main.add_numbers(10, 10) == 20
    results[4] = True
except Exception:
    results[4] = False

sys.stdout.write(json.dumps(results))