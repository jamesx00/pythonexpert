import inspect
import re
import sys
import json

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()
    
try:
    import main
except Exception as e:
    sys.stderr.write(json.dumps({}))
    quit()

results = {}
try:
    assert main.global_number == 30
    results[1] = True
except Exception:
    results[1] = False

original_lines = """global_number = 20

def change_global_number():
    # 
    
    # 
    global_number = 30
    
change_global_number()
print(global_number)""".split('\n')

try:
    submitted_lines = open('main.py', 'r').read().split('\n')
    for index, (original_line, submitted_line) in enumerate(zip(original_lines, submitted_lines)):
        assert index in [3,4,5] or original_line.startswith(submitted_line)
    results[2] = True
except Exception as e:
    results[2] = False
    
sys.stdout.write(json.dumps(results))