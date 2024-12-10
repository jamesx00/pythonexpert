import sys
import re
import json

from unittest.mock import patch

results = {}

with patch('builtins.print') as patched_print:

    try:
        import main
        main.is_positive_or_negative(1)
        patched_print.assert_called_with("The number is positive.")
        results[1] = True
    except Exception as e:
        results[1] = False

    try:
        import main
        main.is_positive_or_negative(-1)
        patched_print.assert_called_with("The number is negative.")
        results[2] = True
    except Exception as e:
        results[2] = False

sys.stdout.write(json.dumps(results))