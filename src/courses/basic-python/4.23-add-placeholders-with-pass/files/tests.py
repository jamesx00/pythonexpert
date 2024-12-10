import sys
import re
import json

from unittest.mock import patch, call

file_content = open('main.py', 'r').read()

results = {}

try:
    assert re.search("pass", file_content) is not None
    results[1] = True
except:
    results[1] = False


with patch('builtins.print') as patched_print:

    try:
        import main
        results[2] = True
    except:
        results[2] = False
    
sys.stdout.write(json.dumps(results))