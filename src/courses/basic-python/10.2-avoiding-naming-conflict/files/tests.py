import sys
import re
import json
import math
import os
from unittest.mock import patch, ANY

results = {}

with patch('builtins.print') as patched_print:

    try:
        import greetings
    except Exception as e:
        pass

    with patch('greetings.greet') as patched_greet:

        try:
            import main
        except Exception as e:
            pass

        try:
            assert main.g == greetings.greet
            results[1] = True
        except Exception as e:
            results[1] = False
        
        try:
            patched_greet.assert_called_with("Cory")
            results[2] = True
        except Exception as e:
            results[2] = False

        

sys.stdout.write(json.dumps(results))