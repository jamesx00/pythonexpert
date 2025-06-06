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
        assert type(main.MyStr) == type
        results[1] = True
    except Exception as e:
        results[1] = False
    
    try:
        assert type(main.MyStr("Python is amazing!")) == main.MyStr
        results[2] = True
    except Exception as e:
        results[2] = False

sys.stdout.write(json.dumps(results))