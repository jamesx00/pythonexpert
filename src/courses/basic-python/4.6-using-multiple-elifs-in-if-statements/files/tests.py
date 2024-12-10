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
    assert main.get_grade(90) == "A"
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert main.get_grade(80) == "B"
    results[2] = True
except Exception as e:
    results[2] = False

try:
    assert main.get_grade(70) == "C"
    results[3] = True
except Exception as e:
    results[3] = False

try:
    assert main.get_grade(60) == "D"
    results[4] = True
except Exception as e:
    results[4] = False

try:
    assert main.get_grade(50) == "F"
    results[5] = True
except Exception as e:
    results[5] = False

sys.stdout.write(json.dumps(results))