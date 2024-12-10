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
    assert main.multiply_by_five.__name__ == '<lambda>'
    results[1] = True
except Exception:
    results[1] = False

try:
    assert main.multiply_by_five(2) == 10
    results[2] = True
except Exception:
    results[2] = False

try:
    assert main.multiply_by_five(10) == 50
    results[3] = True
except Exception:
    results[3] = False

sys.stdout.write(json.dumps(results))