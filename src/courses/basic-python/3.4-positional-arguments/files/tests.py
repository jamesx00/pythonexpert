import sys
import re
import json

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()
    
    
try:
    import main
except Exception:
    sys.stdout.write(json.dumps({1: False}))
    quit()

file_content = open('main.py', 'r').read()

try:
    assert re.search('greet\(.*?\)(?!:)', file_content) is not None
    sys.stdout.write(json.dumps({1: True}))
except Exception:
    sys.stdout.write(json.dumps({1: False}))