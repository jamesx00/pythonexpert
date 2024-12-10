import sys
import re
import json

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()

try:
    import main
except Exception:
    pass

def test_startswith(main, sub):
    return main.startswith(sub)

inputs = [
    ("PythonExpert is amazing!", "PythonExpert"),
    ("The quick brown fox jumps over the lazy dog.", "The quick"),
    ("Hello, world!", "hello"),
    ("Python programming is awesome!", "Python"),
    ("I love coding!", "coding"),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_startswith(*i)
        assert main.startswith(*i) == result
        results[index+1] = True
    except Exception:
        results[index+1] = False
    
sys.stdout.write(json.dumps(results))