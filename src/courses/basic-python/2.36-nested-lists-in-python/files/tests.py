import sys
import re
import json

from unittest.mock import patch
patch('builtins.print').start()

try:
    import main
except Exception:
    pass

results = {}

try:
    assert len(main.my_nested_list) == 3
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert len(main.my_nested_list) == 3
    for item in main.my_nested_list:
        assert type(item) == list
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))