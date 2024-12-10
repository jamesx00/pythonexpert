import sys
import re
import json

from unittest.mock import patch

p_print = patch('builtins.print')
p_print.start()

try:
    import main
except Exception:
    pass

results = {}

try:
    assert "George" in main.properties
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert 35 in main.properties
    results[2] = True
except Exception as e:
    results[2] = False

try:
    assert 'M' in main.properties
    results[3] = True
except Exception as e:
    results[3] = False

sys.stdout.write(json.dumps(results))