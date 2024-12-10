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
        text = "Python is awesome!"
        sentence = main.MyStr(text)
        assert sentence.text == text
        results[1] = True
        results[2] = True
    except Exception as e:
        results[1] = False
        results[2] = False
    
    try:
        text = "Programming is fun"
        sentence = main.MyStr(text)
        assert sentence.text == text
        results[3] = True
        results[4] = True
    except Exception as e:
        results[3] = False
        results[4] = False

    try:
        text = "Python is awesome!"
        sentence = main.MyStr(text)
        assert sentence.__str__() == text
        results[5] = True
    except Exception as e:
        results[5] = False

sys.stdout.write(json.dumps(results))