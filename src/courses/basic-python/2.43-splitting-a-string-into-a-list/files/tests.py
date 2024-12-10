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
    lines = open('main.py', 'r').readlines()
    assert lines[0] == 'text = "USA, Canada, Mexico, Brazil, Argentina, Peru, France, Germany, Italy, Spain"\n'
    results[2] = True
except Exception as e:
    results[2] = False

try:
    file_content = open('main.py', 'r').read()
    assert re.search('\.split\(.*?\)', file_content) is not None
    result = ['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina', 'Peru', 'France', 'Germany', 'Italy', 'Spain']
    assert main.countries == result
    results[1] = True
except Exception as e:
    results[1] = False
    
sys.stdout.write(json.dumps(results))