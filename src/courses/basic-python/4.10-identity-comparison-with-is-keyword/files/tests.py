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
    assert main.is_true_or_false(True) == True
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert main.is_true_or_false(False) == True
    results[2] = True
except Exception as e:
    results[2] = False

try:
    assert main.is_true_or_false(None) == False
    results[3] = True
except Exception as e:
    results[3] = False

try:
    assert main.is_true_or_false(1) == False
    results[4] = True
except Exception as e:
    results[4] = False

try:
    assert main.is_true_or_false(0) == False
    results[5] = True
except Exception as e:
    results[5] = False

try:
    assert main.is_true_or_false([1, 2, 3]) == False
    results[6] = True
except Exception as e:
    results[6] = False

try:
    assert main.is_true_or_false([]) == False
    results[7] = True
except Exception as e:
    results[7] = False

sys.stdout.write(json.dumps(results))