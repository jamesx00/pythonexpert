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
    result = "Hello"[::-1]
    assert main.reverse_a_string("Hello") == result
    results[1] = True
except Exception:
    results[1] = False


try:
    input = "Python is so easy!"
    result = input[::-1]
    assert main.reverse_a_string(input) == result
    results[2] = True
except Exception:
    results[2] = False

try:
    input = "12345"
    result = input[::-1]
    assert main.reverse_a_string(input) == result
    results[3] = True
except Exception:
    results[3] = False

try:
    input = "123!@#"
    result = input[::-1]
    assert main.reverse_a_string(input) == result
    results[4] = True
except Exception:
    results[4] = False

try:
    input = "Hello World!"
    result = input[::-1]
    assert main.reverse_a_string(input) == result
    results[5] = True
except Exception:
    results[5] = False

sys.stdout.write(json.dumps(results))