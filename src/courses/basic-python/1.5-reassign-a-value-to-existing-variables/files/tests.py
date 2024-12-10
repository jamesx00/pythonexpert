import sys, re, json

from unittest.mock import patch
patch('builtins.print').start()

import main

results = {}

try:
    assert main.x == 20
    results[1] = True
except Exception as e:
    results[1] = False

try:
    content = open('main.py', 'r').readlines()
    assert content[0].startswith("x = 10")
except Exception as e:
    results[1] = False

sys.stdout.write(json.dumps(results))