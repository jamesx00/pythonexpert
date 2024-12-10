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
    assert main.result == 40
    file_content = open('main.py', 'r').read()
    assert re.search('([^r]int|float)\(', file_content) is not None
    results[1] = True
except Exception as e:
    results[1] = False

try:
    lines = open('main.py', 'r').readlines()
    assert lines[0] == 'string_number = "20"\n'
    assert lines[1] == 'number = 20\n'
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))