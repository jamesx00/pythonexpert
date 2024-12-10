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
        person = main.Person("Abbey", 30)
        patched_print.assert_called_with("Abbey is 30 years old")
        results[1] = True
    except Exception as e:
        results[1] = False

    try:
        person = main.Person("Eric", 40)
        patched_print.assert_called_with("Eric is 40 years old")
        results[2] = True
    except Exception as e:
        results[2] = False

    try:
        assert main.person.age != main.another_person.age
        results[3] = True
    except Exception as e:
        results[3] = False

sys.stdout.write(json.dumps(results))