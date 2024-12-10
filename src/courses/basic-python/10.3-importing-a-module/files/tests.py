import sys
import re
import json
import math
import os
from unittest.mock import patch, ANY

patched_print = patch('builtins.print')
patched_print.start()

try:
    import greetings
except Exception as e:
    pass

results = {}

with patch('greetings.greet') as patched_greet:

    try:
        import main
    except Exception as e:
        pass

    try:
        main.greetings
        results[1] = True
    except Exception as e:
        results[1] = False

    try:
        patched_greet.assert_called()
        results[2] = True
    except Exception as e:
        results[2] = False

sys.stdout.write(json.dumps(results))