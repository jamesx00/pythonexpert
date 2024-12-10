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
        name = "Abbey"
        age = 30
        test_person = main.Person(name, age)

        try:
            assert test_person.name == name
            results[2] = True
        except Exception as e:
            results[2] = False

        try:
            assert test_person.age == age
            results[3] = True
        except Exception as e:
            results[3] = False

        results[1] = results[2] and results[3]
    except Exception as e:
        results[1] = False
    
    try:
        name = "Eric"
        age = 40
        test_person = main.Person(name, age)

        try:
            assert test_person.name == name
            results[5] = True
        except Exception as e:
            results[5] = False

        try:
            assert test_person.age == age
            results[6] = True
        except Exception as e:
            results[6] = False

        results[4] = results[5] and results[6]
    except Exception as e:
        results[4] = False

sys.stdout.write(json.dumps(results))