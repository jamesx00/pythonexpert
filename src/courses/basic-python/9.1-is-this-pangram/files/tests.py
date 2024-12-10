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

def test_pangram(sentence):
    characters = "abcdefghijklmnopqrstuvwxyz"
    upper_characters = characters.upper()
    for c, uc in zip(characters, upper_characters):
        if c not in sentence and uc not in sentence:
            return False
    return True
    

inputs = [
    ("The quick brown fox jumps over the lazy dog.",),
    ("Pack my box with five dozen liquor jugs.",), 
    ("Python is an amazing programming language.",),
    ("Mr. Jock, TV quiz PhD, bags few lynx.",),
    ("Lorem ipsum dolor sit amet, consectetur adipiscing elit.",),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_pangram(*i)
        assert main.is_this_pangram(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))