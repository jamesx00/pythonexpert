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
    assert main.uppercase_string == main.string.upper()
    file_content = open('main.py', 'r').read()
    assert re.search('upper\(\)', file_content) is not None
    results[1] = True
except Exception as e:
    results[1] = False

try:
    lines = open('main.py', 'r').readlines()
    assert lines[0] == 'string = "The fog was so dense even a laser decided it was not worth the effort."\n'
    results[2] = True
except Exception as e:
    results[2] = False


sys.stdout.write(json.dumps(results))