import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

cases = [((1, 2), 3), ((0, 0), 0)]
results = {}
for index, (args, expected) in enumerate(cases):
    try:
        results[index + 1] = main.add(*args) == expected
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
