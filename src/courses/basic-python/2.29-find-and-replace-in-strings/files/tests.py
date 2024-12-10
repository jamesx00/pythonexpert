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
    assert main.new_sentence == main.sentence.replace("A", "_")
    results[1] = True
except Exception as e:
    results[1] = False

try:
    file_content = open('main.py', 'r').read()
    assert re.search('replace\(', file_content) is not None
    results[2] = True
except Exception as e:
    results[2] = False

try:
    lines = open('main.py', 'r').readlines()
    assert lines[0] == 'sentence = "YOU CANNOT COMPARE APPLES AND ORANGES."\n'
    results[3] = True
except Exception as e:
    results[3] = False

sys.stdout.write(json.dumps(results))