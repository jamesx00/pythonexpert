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

def test_endswith(main, sub):
    return main.endswith(sub)

results = {}

inputs = [
    ("PythonExpert is amazing!", "amazing!"),
    ("The quick brown fox jumps over the lazy dog.", "lazy dog."), 
    ("Hello, World!", "world!"),
    ("Python programming is awesome!", "awesome"),
    ("I love coding!", "coding!"),
]

for index, i in enumerate(inputs):
    try:
        result = test_endswith(*i)
        assert main.endswith(*i) == result
        results[index+1] = True
    except Exception:
        results[index+1] = False

sys.stdout.write(json.dumps(results))