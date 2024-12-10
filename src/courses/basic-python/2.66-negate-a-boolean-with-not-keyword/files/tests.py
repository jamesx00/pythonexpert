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
    assert main.true is True
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert main.false is False
    results[2] = True
except Exception as e:
    results[2] = False

try:
    assert main.not_has_a is False
    results[3] = True
except Exception as e:
    results[3] = False

try:
    assert main.not_has_z is True
    results[4] = True
except Exception as e:
    results[4] = False

try:
    assert main.not_has_name is False
    results[5] = True
except Exception as e:
    results[5] = False

try:
    assert main.not_has_salary is True
    results[6] = True
except Exception as e:
    results[6] = False

sys.stdout.write(json.dumps(results))