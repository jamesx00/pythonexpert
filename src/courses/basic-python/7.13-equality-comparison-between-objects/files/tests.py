import sys
import re
import json
import inspect

from unittest.mock import patch

results = {}

with patch('builtins.print') as patched_print:

    text1 = "Hello World"
    text2 = "Python is awesome!"

    try:
        import main
    except Exception as e:
        pass

    try:
        obj1 = main.MyStr(text1)
        obj2 = main.MyStr(text1)
        assert obj1 == obj2
        results[1] = True
    except Exception as e:
        results[1] = False
    
    try:
        obj1 = main.MyStr(text1)
        obj2 = main.MyStr(text2)
        assert obj1 != obj2
        results[2] = True
    except Exception as e:
        results[2] = False

sys.stdout.write(json.dumps(results))