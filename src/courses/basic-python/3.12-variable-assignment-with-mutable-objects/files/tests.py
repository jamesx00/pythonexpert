import sys
import re
import json
import math

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()

try:
    import main
except Exception:
    pass

results = {}


try:
    assert main.animal_a == {"type": "Dog", "name": "Fluffy"}
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert main.animal_b == {"type": "Dog", "name": "Fluffy"}
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))