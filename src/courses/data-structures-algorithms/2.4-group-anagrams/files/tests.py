import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_group_anagrams(words):
    groups = {}
    for w in words:
        key = "".join(sorted(w))
        groups.setdefault(key, []).append(w)
    return list(groups.values())

def normalize(groups):
    return sorted(tuple(sorted(g)) for g in groups)

inputs = [
    (["bat", "tab", "eat", "tea", "owl"],),
    ([],),
    ([""],),
    (["abc", "cba", "bca", "xyz"],),
    (["a", "a", "a"],),
    (["cat", "dog"],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = normalize(test_group_anagrams(*i))
        assert normalize(main.group_anagrams(*i)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
