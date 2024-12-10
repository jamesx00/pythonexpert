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

results = {}

try:
    file_content = open('main.py', 'r').read()
    assert re.search('enumerate(.*?)', file_content) is not None
    results[1] = True
except Exception as e:
    results[1] = False

try:
    result = ['Cassandra Sullivan', 'Brooke Stevens', 'Amanda Smith', 'Mary Smith']
    assert main.output == result
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))