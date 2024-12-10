import sys
import re
import json
import inspect

from unittest.mock import patch

results = {}

with patch('builtins.print') as patched_print:

    try:
        import main
    except Exception as e:
        pass

    try:
        assert issubclass(main.MyUpperStr, main.MyStr)
        results[1] = True
    except Exception as e:
        results[1] = False

sys.stdout.write(json.dumps(results))