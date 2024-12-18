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

def test_convert_to_title(sentence):
    return sentence.title()

inputs = [
    ("hello world!",),
    ("the cat in the hat.",), 
    ("i love coding.",),
    ("this is a test sentence.",),
    ("the quick brown fox.",),
]

results = {}

for index, test_args in enumerate(inputs):
    try:
        expected_result = test_convert_to_title(*test_args)
        assert main.convert_to_title(*test_args) == expected_result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))