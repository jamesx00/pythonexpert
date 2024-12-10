import sys
import re
import json
import math
import os
from unittest.mock import patch, ANY

results = {}

patched_print = patch('builtins.print')
patched_print.start()

try:
    module_files = os.listdir('greetings')
    assert "__init__.py" in module_files
    results[1] = True
except Exception as e:
    results[1] = False

try:
    module_files = os.listdir('greetings')
    assert "functions.py" in module_files
    results[2] = True
except Exception as e:
    results[2] = False

try:
    from greetings import functions
    assert callable(functions.greet)
    results[3] = True
except Exception as e:
    results[3] = False

try:
    assert 'greetings.py' not in os.listdir()
    results[4] = True
except Exception as e:
    results[4] = False

try:
    with patch('greetings.functions.greet') as patched_greet:

        try:
            import main
        except Exception as e:
            pass

        try:
            assert main.functions == functions
            results[5] = True
        except Exception as e:
            results[5] = False
        
        if results[5] is False:
            try:
                assert main.greet == functions.greet
                results[5] = True
            except Exception as e:
                results[5] = False
        
        try:
            patched_greet.assert_called_with("Alice")
            results[6] = True
        except Exception as e:
            results[6] = False

except Exception as e:
    results[5] = False
    results[6] = False

        

sys.stdout.write(json.dumps(results))