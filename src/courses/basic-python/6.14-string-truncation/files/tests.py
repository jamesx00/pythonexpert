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

def test_truncate(sentence, max_length):
    if len(sentence) <= max_length:
        return sentence
    return sentence[:max_length] + '...'

inputs = [
    ("Hello, World!", 8),
    ("The quick brown fox jumps over the lazy dog", 20), 
    ("Lorem ipsum dolor sit amet", 25),
    ("Python programming is fun", 30),
    ("abcdefghijklmnopqrstuvwxyz", 5),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_truncate(*i)
        assert main.truncate(*i) == result
        results[index+1] = True
    except Exception:
        results[index+1] = False

sys.stdout.write(json.dumps(results))