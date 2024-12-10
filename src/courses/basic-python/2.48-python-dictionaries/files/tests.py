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
    assert type(main.student["name"]) == str
    results[2] = True
except Exception as e:
    results[2] = False

try:
    assert type(main.student["age"]) == int
    results[3] = True
except Exception as e:
    results[3] = False

results[1] = results.get(2) and results.get(3)

sys.stdout.write(json.dumps(results))