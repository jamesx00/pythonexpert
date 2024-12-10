import sys
import re
import json
import math

from unittest.mock import patch

patched_print = patch("builtins.print")
patched_print.start()

try:
    import main
except Exception:
    pass

patched_print.stop()

results = {}

with patch('builtins.print') as patched_print:

    try:
        person = main.Person("samson craig", 30, "male", "software engineer")

        try:
            assert person.first_name == "Samson"
            results[2] = True
        except Exception as e:
            results[2] = False
        
        try:
            assert person.last_name == "Craig"
            results[3] = True
        except Exception as e:
            results[3] = False
        
        try:
            assert person.age == 30
            results[4] = True
        except Exception as e:
            results[4] = False
        
        try:
            assert person.occupation == "software engineer"
            results[5] = True
        except Exception as e:
            results[5] = False
        
        try:
            person.introduce()
            patched_print.assert_called_with("Hello, my name is Samson. I am 30 years old. I am a male working as a software engineer.")
            results[6] = True
        except Exception as e:
            results[6] = False
        
        try:
            person.celebrate_birthday()
            assert person.age == 31
            results[7] = True
        except Exception as e:
            results[7] = False

        try:
            person.introduce()
            patched_print.assert_called_with("Hello, my name is Samson. I am 31 years old. I am a male working as a software engineer.")
            results[8] = True
        except Exception as e:
            results[8] = False
        
        try:
            person.change_job("data analyst")
            assert person.occupation == "data analyst"
            results[9] = True
        except Exception as e:
            results[9] = False
        
        try:
            person.introduce()
            patched_print.assert_called_with("Hello, my name is Samson. I am 31 years old. I am a male working as a data analyst.")
            results[10] = True
        except Exception as e:
            results[10] = False
            
        results[1] = len(results.values()) == 9 and all(results.values())
    except Exception as e:
        results[1] = False

sys.stdout.write(json.dumps(results))