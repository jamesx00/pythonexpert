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
        assert (type(main.person.age) == int or type(main.person.age) == float) and 1 <= main.person.age <= 100
        results[1] = True
    except Exception as e:
        results[1] = False

    try:
        assert (type(main.another_person.age) == int or type(main.another_person.age) == float) and 1 <= main.person.age <= 100
        results[2] = True
    except Exception as e:
        results[2] = False

    try:
        assert main.person.age != main.another_person.age
        results[3] = True
    except Exception as e:
        results[3] = False

sys.stdout.write(json.dumps(results))