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
    assert main.wanted_element == main.my_list[1][1]
    results[1] = True
except Exception as e:
    results[1] = False

file_content = open('main.py', 'r').read()

try:
    assert re.search('\[-?[0-9]\]', file_content) is not None
    results[2] = True
except Exception as e:
    results[2] = False

try:
    assert file_content.startswith("my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\n")
    results[3] = True
except Exception as e:
    results[3] = False

sys.stdout.write(json.dumps(results))