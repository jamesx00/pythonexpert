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

try:
    assert callable(greetings.greet1)
    assert callable(greetings.greet2)
except Exception as e:
    results[1] = False
    results[2] = False
    results[3] = False
    results[4] = False
    exit()

with patch('greetings.greet1') as patched_greet1, patch('greetings.greet2') as patched_greet2:

    try:
        import main
    except Exception as e:
        pass
        
    try:
        main.greet1 == greetings.greet1
        results[1] = True
    except Exception as e:
        results[1] = False
        
    try:
        main.greet2 == greetings.greet2
        results[2] = True
    except Exception as e:
        results[2] = False

    try:
        patched_greet1.assert_called_with("Leena")
        results[3] = True
    except Exception as e:
        results[3] = False

    try:
        patched_greet2.assert_called_with("Dillan")
        results[4] = True
    except Exception as e:
        results[4] = False

sys.stdout.write(json.dumps(results))