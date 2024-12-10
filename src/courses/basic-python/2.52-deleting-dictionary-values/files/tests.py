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
    assert "salary" not in main.employee
    results[1] = True
except Exception as e:
    results[1] = False

try:
    file_content = open('main.py', 'r').read()
    assert re.search("del employee\[.*?\]", file_content) is not None
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))