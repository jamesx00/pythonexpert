import sys
import re
import json

from unittest.mock import patch
patch('builtins.print').start()

try:
    import main
except Exception:
    pass

results = {}

try:
    assert main.has_english is False
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert main.has_javascript is True
    results[2] = True
except Exception as e:
    results[2] = False



sys.stdout.write(json.dumps(results))