import sys
import re
import json

from unittest.mock import patch

p_print = patch('builtins.print')
p_print.start()

results = {}

try:
    import main
except Exception:
    pass

students = ['Rhonda Hart', 'Ernest Aguirre', 'Sean Jackson']
scores = [60, 70, 80]

try:
    results = [f"{student}: {score}" for student, score in zip(students, scores)]
    assert main.results == results
    results[1] = True
except Exception as e:
    results[1] = False

try:
    file_content = open('main.py', 'r').read()
    assert re.search('zip(.*?)', file_content) is not None
    results[2] = True
except Exception as e:
    results[2] = False

sys.stdout.write(json.dumps(results))