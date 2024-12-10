import sys
import re
import json
import math

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()

try:
    import main
except Exception:
    pass

def test_replace_text(sentence, old, new):
    if old[0].isupper():
        replace = new[0].upper() + new[1:]
    if old[0].islower():
        replace = new[0].lower() + new[1:]
    return sentence.replace(old, replace)
    
inputs = [
    ("Python is a popular programming language.", "Python", "javaScript",),
    ("The Quick Brown Fox Jumps Over The Lazy Dog.", "Quick", "fast",),
    ("The quick brown fox jumps over the lazy dog.", "quick", "Fast",),
    ("I have a cat and a dog. My cat's name is Whiskers.", "Whiskers", "coco",),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_replace_text(*i)
        assert main.replace_text(*i) == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))