import re
import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

results = {}

with open('main.py', 'r') as file:
    content = file.read()
    try:
        assert re.search('#.{5}', content) is not None, "Write a \"single-line\" comment with at least 5 characters: Failed X\n"
        results[1] = True
    except AssertionError as e:
        results[1] = False
    
    try:
        assert re.search('(""".{5,}"""|\'\'\'.{5,}\'\'\')', content, flags=re.DOTALL) is not None, "Write a \"multi-line\" comment with at least 5 characters: Failed X\n"
        results[2] = True
    except AssertionError as e:
        results[2] = False
    
sys.stdout.write(json.dumps(results))