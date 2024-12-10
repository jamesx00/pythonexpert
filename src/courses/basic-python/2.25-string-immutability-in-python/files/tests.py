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
    assert main.string == "How are you doing?"
    results[1] = True
except Exception as e:
    results[1] = False

try:
    lines = open('main.py', 'r').readlines()
    assert lines[0].startswith('string = "How are you doing!"')
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))