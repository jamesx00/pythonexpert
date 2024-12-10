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

results = {}

def test_get_longest_word(sentence):
    words = sentence.split(' ')
    longest_word = None
    for word in words:
        if longest_word is None: longest_word = word
        if len(word) > len(longest_word): longest_word = word
    return longest_word

try:
    sentence = "Hello world"
    result = test_get_longest_word(sentence)
    assert main.get_longest_word(sentence) == result
    results[1] = True
except Exception:
    results[1] = False

try:
    sentence = "The cat in the hat"
    result = test_get_longest_word(sentence)
    assert main.get_longest_word(sentence) == result
    results[2] = True
except Exception:
    results[2] = False

try:
    sentence = "Today is a beautiful day"
    result = test_get_longest_word(sentence)
    assert main.get_longest_word(sentence) == result
    results[3] = True
except Exception:
    results[3] = False

try:
    sentence = "Python is a powerful programming language"
    result = test_get_longest_word(sentence)
    assert main.get_longest_word(sentence) == result
    results[4] = True
except Exception:
    results[4] = False
    
try:
    sentence = "The quick brown fox jumps over the lazy dog"
    result = test_get_longest_word(sentence)
    assert main.get_longest_word(sentence) == result
    results[5] = True
except Exception:
    results[5] = False

sys.stdout.write(json.dumps(results))