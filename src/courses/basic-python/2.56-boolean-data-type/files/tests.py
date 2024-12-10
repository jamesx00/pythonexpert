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
    assert main.true is True
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert main.false is False
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))