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
    assert type(main.my_grocery) == list
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert len(main.my_grocery) >= 5
    results[2] = True
except Exception as e:
    results[2] = False
    
try:
    assert len(main.my_grocery) > 0
    for item in main.my_grocery:
        assert len(item) >= 2 and type(item[0]) == str
    results[3] = True
except Exception as e:
    results[3] = False

try:
    assert len(main.my_grocery) > 0
    for item in main.my_grocery:
        assert len(item) >= 2 and type(item[1]) == int
    results[4] = True
except Exception as e:
    results[4] = False

sys.stdout.write(json.dumps(results))