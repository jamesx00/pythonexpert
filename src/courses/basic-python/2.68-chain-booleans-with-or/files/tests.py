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
    assert main.true is True
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert main.false is False
    results[2] = True
except Exception as e:
    results[2] = False

file_content = open('main.py', 'r').read()

try:
    assert re.search('true *=.*?or', file_content) is not None
    results[3] = True
except Exception as e:
    results[3] = False

try:
    assert re.search('false *=.*?or', file_content) is not None
    results[4] = True
except Exception as e:
    results[4] = False

sys.stdout.write(json.dumps(results))