import sys
import re
import json

from unittest.mock import patch

results = {}

with patch('builtins.print') as patched_print:

    try:
        import main
        assert main.message == "He said, \"Don't forget to bring your umbrella!\""
        results[1] = True
    except Exception as e:
        results[1] = False

sys.stdout.write(json.dumps(results))