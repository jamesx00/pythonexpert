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
    assert main.get_discount(employee=True, years=10) == 20
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert main.get_discount(employee=True, years=5) == 10
    results[2] = True
except Exception as e:
    results[2] = False

try:
    assert main.get_discount(employee=True, years=1) == 10
    results[3] = True
except Exception as e:
    results[3] = False

try:
    assert main.get_discount(employee=False) == 5
    results[4] = True
except Exception as e:
    results[4] = False

try:
    file_content = open('main.py', 'r').read()
    assert re.search('and', file_content) is None
    results[5] = True
except Exception as e:
    results[5] = False

sys.stdout.write(json.dumps(results))