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
    assert main.get_discount(300) == 10
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert main.get_discount(500) == 20
    results[2] = True
except Exception as e:
    results[2] = False

try:
    assert main.get_discount(1000) == 30
    results[3] = True
except Exception as e:
    results[3] = False

try:
    assert main.get_discount(1500) == 30
    results[4] = True
except Exception as e:
    results[4] = False

sys.stdout.write(json.dumps(results))