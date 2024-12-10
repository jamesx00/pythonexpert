import sys
import re
import json

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()

tests = []

try:
    import main
except IndentationError as e:
    tests.append(False)
except Exception as e:
    tests.append(True)

file_lines = open('main.py', 'r').readlines()

try:
    assert len(file_lines) >= 3
    assert file_lines[1].startswith('  print')
    assert file_lines[2].startswith('  print')
    tests.append(True)
except Exception:
    tests.append(False)

sys.stdout.write(json.dumps({1: all(tests)}))