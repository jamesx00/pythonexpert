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
    assert type(main.full_name) == str
    results[1] = True
except Exception as e:
    results[1] = False

try:
    file_content = open('main.py', 'r').read()
    assert re.search('\+', file_content) is not None
    results[2] = True
except Exception as e:
    results[2] = False

try:
    assert main.full_name.find(' ') not in [-1, 0]
    assert main.full_name[-1] != ' '
    results[3] = True
except Exception as e:
    results[3] = False

sys.stdout.write(json.dumps(results))