import sys
import re
import json

from unittest.mock import patch

results = {}

with patch('builtins.print') as patched_print:

    try:
        import main
        results[1] = True
    except Exception:
        results[1] = False

    try:
        patched_print.assert_called_with("Hello World!")
        results[2] = True
    except Exception as e:
        results[2] = False

    sys.stdout.write(json.dumps(results))