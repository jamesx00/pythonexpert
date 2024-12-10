import sys, re
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

results = {}

try:
    assert main.x == 10, "Assign x with the number 10: Failed X"
    results[1] = True
except Exception as e:
    results[1] = False

try:
    content = open('main.py', 'r').read()
    assert main.y == 10, "Assign y with the variable x: Failed X"
    assert re.search('y *= *x', content) is not None, "Assign y with the variable x: Failed X"
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))