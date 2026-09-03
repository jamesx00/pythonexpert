import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_encode(words):
    return "".join(f"{len(w)}#{w}" for w in words)

def test_decode(encoded):
    words = []
    i = 0
    while i < len(encoded):
        j = i
        while encoded[j] != "#":
            j += 1
        length = int(encoded[i:j])
        start = j + 1
        words.append(encoded[start:start + length])
        i = start + length
    return words

inputs = [
    (["cat", "dog"],),
    ([],),
    ([""],),
    (["4:cats", "dogs"],),
    (["a", "", "bb", ""],),
    (["hello world", "foo#bar"],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        words = i[0]
        result = test_decode(test_encode(words))
        assert main.decode(main.encode(words)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
