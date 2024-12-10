import sys
import re
import json

from unittest.mock import patch

try:
    patched_print = patch('builtins.print')
    patched_print.start()
    import main
    patched_print.stop()
    
except Exception:
    pass

results = {}

try:
    assert callable(main.add_them_up)
    results[1] = True
except Exception:
    results[1] = False

try:
    assert main.add_them_up.__code__.co_argcount == 2
    results[2] = True
except Exception:
    results[2] = False
    

with patch('main.print') as p_print:
    
    try:
        main.add_them_up(1, 2)
        p_print.assert_called_with(3)
        results[3] = True
    except Exception as e:
        results[3] = False

    try:
        main.add_them_up(10, 10)
        p_print.assert_called_with(20)
        results[4] = True
    except Exception as e:
        results[4] = False

sys.stdout.write(json.dumps(results))