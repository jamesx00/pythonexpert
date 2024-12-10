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
    lines = open('main.py', 'r').readlines()
    assert lines[0] == 'my_list = ["A", "B", "C", "D"]\n'
    results[3] = True
except Exception as e:
    results[3] = False

try:
    assert main.my_list == ["A", "B", "C", "D", "E", "F"]
    results[1] = True
except Exception as e:
    results[1] = False

try:
    file_content = open('main.py', 'r').read()
    assert re.search('\.extend\(.*?\)', file_content) is not None
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))