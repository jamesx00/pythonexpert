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

def test_func(sentence):
    cleaned_sentence = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)  # Remove non-alphanumeric characters
    kebab_case = cleaned_sentence.lower().replace(" ", "-")
    return kebab_case

    
inputs = [
    ("Hello World",),
    ("Python Programming Language",),
    ("This Is a Sentence!",),
    ("Coding Is Fun!!!",),
    ("I Love Python*&^%",),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.make_kebab(*i) == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))