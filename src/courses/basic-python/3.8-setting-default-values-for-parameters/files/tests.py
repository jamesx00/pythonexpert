import inspect
import re
import sys
import json

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()

results = {}
    
try:
    import main
except Exception as e:
    sys.stdout.write(json.dumps({}))
    quit()

try:
    assert callable(main.print_height)
    results[1] = True
except Exception:
    results[1] = False


try:
    signature = inspect.signature(main.print_height)
    assert 'height' in signature.parameters    
    results[2] = True
except Exception:
    results[2] = False

try:
    signature = inspect.signature(main.print_height)
    assert 'unit' in signature.parameters
    assert signature.parameters['unit'].default == 'cm'
    results[3] = True
except Exception:
    results[3] = False

results[6] = results.get(2) and results.get(3)

with patch('main.print') as p_print:
    try:
        main.print_height(170)
        p_print.assert_called_with("You are 170 cm tall.")
        results[4] = True
    except Exception:
        results[4] = False
    
    try:
        main.print_height(6, "ft")
        p_print.assert_called_with("You are 6 ft tall.")
        results[5] = True
    except Exception:
        results[5] = False

sys.stdout.write(json.dumps(results))