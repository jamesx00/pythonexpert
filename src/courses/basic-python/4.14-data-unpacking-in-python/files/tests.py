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
    assert main.name == "Jane Smith"
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert main.age == 28
    results[2] = True
except Exception as e:
    results[2] = False

try:
    assert main.department == "Marketing"
    results[3] = True
except Exception as e:
    results[3] = False

try:
    file_content = open('main.py', 'r').read()
    assert re.search('name.*?age.*?department', file_content) is not None
    results[4] = True
except Exception as e:
    results[4] = False

sys.stdout.write(json.dumps(results))