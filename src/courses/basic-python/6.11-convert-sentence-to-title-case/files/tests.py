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
    return ' '.join([word.title() for word in sentence.split(' ')])

inputs = [
    "hello world!",
    "the cat in the hat.",
    "i love coding.",
    "this is a test sentence.",
    "the quick brown fox.",
    "PYTHON PROGRAMMING IS FUN!"
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_convert_to_title(i)
        assert main.convert_to_title(i) == result
        results[index+1] = True
    except Exception:
        results[index+1] = False

sys.stdout.write(json.dumps(results))