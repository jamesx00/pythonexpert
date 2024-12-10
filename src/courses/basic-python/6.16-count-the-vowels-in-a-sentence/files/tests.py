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

def test_count_vowels(sentence):
    result = 0
    for c in sentence:
        if c.lower() in ['a', 'e', 'i', 'o', 'u']:
            result += 1
    return result

inputs = [
    ("Hello, World!",),
    ("Python is Awesome",), 
    ("Quick brown fox jumps over the lazy dog",),
    ("THIS SENTENCE HAS VOWELS",),
    ("",),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_count_vowels(*i)
        assert main.count_vowels(*i) == result
        results[index+1] = True
    except Exception:
        results[index+1] = False

sys.stdout.write(json.dumps(results))