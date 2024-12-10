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

    text = "Python is awesome!"
    
    try:
        assert main.MyStr(text).__str__() == text
        results[1] = True
    except Exception as e:
        results[1] = False

    try:
        assert main.MyUpperStr(text).__str__() == text.upper()
        results[2] = True
    except Exception as e:
        results[2] = False

sys.stdout.write(json.dumps(results))