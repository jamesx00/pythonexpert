import sys
import re
import json

from unittest.mock import patch

p_print = patch('builtins.print')
p_print.start()

try:
    import main
except Exception:
    pass

results = {}

try:
    assert main.person == main.copy_person
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert id(main.person) != id(main.copy_person)
    results[2] = True
except Exception as e:
    results[2] = False


sys.stdout.write(json.dumps(results))