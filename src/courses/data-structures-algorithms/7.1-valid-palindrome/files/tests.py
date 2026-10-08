import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

inputs = [
    ("A man, a plan, a canal, Panama",),
    ("Not a palindrome!",),
    ("",),
    ("..,,!!",),
    ("Was it a car or a cat I saw?",),
    ("race a car",),
    ("12321",),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.is_palindrome(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
