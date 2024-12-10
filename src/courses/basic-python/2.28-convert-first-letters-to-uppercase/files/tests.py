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
    assert main.title == main.sentence.title()
    file_content = open('main.py', 'r').read()
    assert re.search('title\(\)', file_content) is not None
    results[1] = True
except Exception as e:
    results[1] = False

try:
    lines = open('main.py', 'r').readlines()
    assert lines[0] == 'sentence = "Egg whites can be used as a natural hair conditioner."\n'
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))