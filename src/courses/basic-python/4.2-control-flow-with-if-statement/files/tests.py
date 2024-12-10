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
    assert main.is_even(0) is True
    results[1] = True
except Exception:
    results[1] = False

try:
    assert main.is_even(15) is False
    results[2] = True
except Exception:
    results[2] = False

try:
    assert main.is_even(50) is True
    results[3] = True
except Exception:
    results[3] = False

sys.stdout.write(json.dumps(results))