import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_is_anagram(word_one, word_two):
    if len(word_one) != len(word_two):
        return False
    return sorted(word_one) == sorted(word_two)

inputs = [
    ("stone", "tones"),
    ("stone", "toness"),
    ("rat", "tar"),
    ("rat", "car"),
    ("", ""),
    ("aabbcc", "abcabc"),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_is_anagram(*i)
        assert main.is_anagram(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
