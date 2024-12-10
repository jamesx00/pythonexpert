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
        assert main.Human.arms == 2
        results[1] = True
    except Exception as e:
        results[1] = False

    try:
        assert main.regular_human.arms == 2
        results[2] = True
    except Exception as e:
        results[2] = False
    
    try:
        assert main.fake_human.arms == 10
        results[3] = True
    except Exception as e:
        results[3] = False

sys.stdout.write(json.dumps(results))