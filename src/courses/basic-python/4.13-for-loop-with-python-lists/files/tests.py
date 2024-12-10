import sys
import re
import json

from unittest.mock import patch

p_print = patch('builtins.print')
p_print.start()

try:
    import main
except Exception:
    pass

try:
    assert main.total == 110
    file_content = open('main.py', 'r').read()
    assert re.search('for.*?:', file_content) is not None
    sys.stdout.write(json.dumps({1: True}))
except Exception as e:
    sys.stdout.write(json.dumps({1: False}))