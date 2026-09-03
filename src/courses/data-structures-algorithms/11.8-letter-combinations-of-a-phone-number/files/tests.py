import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

DIGIT_MAP = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

def test_letter_combinations(digits):
    if not digits:
        return []
    result = []

    def backtrack(index, path):
        if index == len(digits):
            result.append("".join(path))
            return
        for letter in DIGIT_MAP[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return result

def normalize(combos):
    return sorted(combos)

inputs = [
    ("23",),
    ("",),
    ("2",),
    ("7",),
    ("9",),
    ("79",),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = normalize(test_letter_combinations(*i))
        assert normalize(main.letter_combinations(*i)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
