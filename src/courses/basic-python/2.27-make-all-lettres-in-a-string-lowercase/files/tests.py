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
    assert main.lowercase_string == main.string.lower()
    file_content = open('main.py', 'r').read()
    assert re.search('lower\(\)', file_content) is not None
    results[1] = True
except Exception as e:
    results[1] = False

try:
    lines = open('main.py', 'r').readlines()
    assert lines[0] == 'string = "HE STRIVES TO KEEP THE BEST LAWN IN THE NEIGHBORHOOD."\n'
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))