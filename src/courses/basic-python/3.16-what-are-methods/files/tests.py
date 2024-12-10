import sys
import re
import json

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()

try:
    import main
except Exception:
    pass

results = {}

try:
    file_content = open('main.py', 'r').read()
    assert re.search('\.title\(\)', file_content) is not None
    assert main.sentence == "Python Is An Amazing Programming Language!"
    results[1] = True
except Exception:
    results[1] = False

sys.stdout.write(json.dumps(results))