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
    assert main.comma == ","
    file_content = open('main.py', 'r').read()
    assert re.search('\[\d\]', file_content) is not None
    sys.stdout.write(json.dumps({1: True}))
except Exception as e:
    sys.stdout.write(json.dumps({1: False}))