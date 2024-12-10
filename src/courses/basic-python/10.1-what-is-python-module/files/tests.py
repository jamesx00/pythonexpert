import sys
import re
import json
import math
import os

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()

try:
    import main
except Exception:
    pass


results = {}

try:
    assert 'greetings.py' in os.listdir()
    results[1] = True
except Exception as e:
    results[1] = False

try:
    import greetings
    assert callable(greetings.greet)
    results[2] = True
except Exception:
    results[2] = False

sys.stdout.write(json.dumps(results))