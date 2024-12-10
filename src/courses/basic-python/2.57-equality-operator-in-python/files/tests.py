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
    assert main.equal is True
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert main.not_equal is False
    results[2] = True
except Exception as e:
    results[2] = False

try:
    file_content = open('main.py', 'r').read()
    assert "==" in file_content
    results[3] = True
except Exception as e:
    results[3] = False

sys.stdout.write(json.dumps(results))