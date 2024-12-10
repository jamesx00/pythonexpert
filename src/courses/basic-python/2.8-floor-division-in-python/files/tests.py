import sys
import re
import json

from unittest.mock import patch
patch('builtins.print').start()

try:
    import main
except Exception:
    pass

try:
    assert main.x == 5
    file_content = open('main.py', 'r').read()
    assert re.search('//', file_content) is not None
    sys.stdout.write(json.dumps({1: True}))
except Exception as e:
    sys.stdout.write(json.dumps({1: False}))