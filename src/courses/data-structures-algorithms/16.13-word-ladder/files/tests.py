import sys
import json
import string
from collections import deque

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_ladder_length(start_word, end_word, word_list):
    words = set(word_list)
    if end_word not in words:
        return 0
    if start_word == end_word:
        return 1

    q = deque([(start_word, 1)])
    visited = {start_word}
    while q:
        word, length = q.popleft()
        if word == end_word:
            return length
        for i in range(len(word)):
            for ch in string.ascii_lowercase:
                candidate = word[:i] + ch + word[i + 1:]
                if candidate in words and candidate not in visited:
                    visited.add(candidate)
                    q.append((candidate, length + 1))
    return 0

inputs = [
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),
    ("a", "c", ["a", "b", "c"]),
    ("hot", "dog", ["hot", "dog"]),
    ("hot", "dog", ["hot", "dot", "dog"]),
    ("cat", "cat", ["cat"]),
    ("same", "cost", []),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_ladder_length(*i)
        assert main.ladder_length(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
