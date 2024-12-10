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
    assert main.course_name == "Python Programming"
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert main.course_description.startswith("Learn how to program in Python")
    results[2] = True
except Exception as e:
    results[2] = False

try:
    assert main.course_stars is None
    results[3] = True
except Exception as e:
    results[3] = False

sys.stdout.write(json.dumps(results))