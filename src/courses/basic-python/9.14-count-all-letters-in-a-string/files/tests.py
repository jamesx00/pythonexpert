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
    letter_count = {}

    for char in sentence.lower():
        if char.isalpha():
            letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count
    
inputs = [
    ("Hello World!",),
    ("Python is Fun!",),
    ("Mississippi",),
    ("OpenAI+",),
    ("Abra Kadabra",)
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.count_letters(*i)  == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))