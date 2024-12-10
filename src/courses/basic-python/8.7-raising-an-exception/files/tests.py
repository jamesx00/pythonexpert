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
        assert main.divide_the_number(4, 2) == 2
        results[1] = True
    except Exception as e:
        results[1] = False
    
    try:
        assert main.divide_the_number(10, 4) == 2.5
        results[2] = True
    except Exception as e:
        results[2] = False
    
    try:
        try:
            main.divide_the_number(10, 0)
        except ZeroDivisionError as e:
            if str(e) == "You cannot divide by zero!":
                results[3] = True
    except Exception as e:
        results[3] = False

    try:
        try:
            main.divide_the_number(10, "Hello")
        except TypeError as e:
            if str(e) == "You cannot divide a number with a string!":
                results[4] = True
    except Exception as e:
        results[4] = False
    
sys.stdout.write(json.dumps(results))