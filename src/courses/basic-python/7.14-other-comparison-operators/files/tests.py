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
        assert main.MyStr("1") == main.MyStr("1")
        results[1] = True
    except Exception as e:
        results[1] = False
    
    try:
        assert (main.MyStr("1") != main.MyStr("1")) == False
        results[2] = True
    except Exception as e:
        results[2] = False
    
    try:
        assert (main.MyStr("1") < main.MyStr("1")) == False
        results[3] = True
    except Exception as e:
        results[3] = False
    
    try:
        assert (main.MyStr("1") > main.MyStr("1")) == False
        results[4] = True
    except Exception as e:
        results[4] = False

    try:
        assert main.MyStr("1") <= main.MyStr("1")
        results[5] = True
    except Exception as e:
        results[5] = False

    try:
        assert main.MyStr("1") >= main.MyStr("1")
        results[6] = True
    except Exception as e:
        results[6] = False

sys.stdout.write(json.dumps(results))