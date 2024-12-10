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
    assert main.my_list[-1] == 'Four'
    results[1] = True
except Exception as e:
    results[1] = False

try:
    file_content = open('main.py', 'r').read()
    assert re.search('\[-?[0-9]?\]', file_content) is not None
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))