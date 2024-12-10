import sys
import re
import json

from unittest.mock import patch

results = {}

with patch('builtins.print') as patched_print:

    

    try:
        import main
        assert main.area == 50
        results[1] = True
    except Exception as e:
        results[1] = False

    try:
        patched_print.assert_called_with("The area of the square is 50")
        results[2] = True
    except Exception as e:
        results[2] = False

sys.stdout.write(json.dumps(results))