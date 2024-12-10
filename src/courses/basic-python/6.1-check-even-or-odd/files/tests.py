import sys
import re
import json

from unittest.mock import patch

results = {}

try:
    patched_print = patch('builtins.print')
    patched_print.start()
    import main
    print_print.end()
except Exception:
    pass

try:
    with patch('builtins.print') as patched_print:
        message = "Number 0 is even"
        main.is_even_or_odd(0)
        patched_print.assert_called_with(message)
        results[1] = True
except Exception:
    results[1] = False

try:
    with patch('builtins.print') as patched_print:
        message = "Number 5 is odd"
        main.is_even_or_odd(5)
        patched_print.assert_called_with(message)
        results[2] = True
except Exception:
    results[2] = False

try:
    with patch('builtins.print') as patched_print:
        message = "Number 10 is even"
        main.is_even_or_odd(10)
        patched_print.assert_called_with(message)
        results[3] = True
except Exception:
    results[3] = False

try:
    with patch('builtins.print') as patched_print:
        message = "Number 999 is odd"
        main.is_even_or_odd(999)
        patched_print.assert_called_with(message)
        results[4] = True
except Exception:
    results[4] = False

sys.stdout.write(json.dumps(results))