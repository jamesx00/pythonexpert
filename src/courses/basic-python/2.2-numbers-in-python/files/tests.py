import json
import sys

from unittest.mock import patch
patch('builtins.print').start()

try:
    import main
except Exception:
    pass

results = {}

try:
    assert type(main.x) == int
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert type(main.y) == float
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))