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
    assert main.x == 20
    file_content = open('main.py', 'r').read()
    assert re.search('\+', file_content) is not None
    results[1] = True
except Exception as e:
    results[1] = False

sys.stdout.write(json.dumps(results))