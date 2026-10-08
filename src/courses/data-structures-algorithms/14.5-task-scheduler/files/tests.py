import sys
import json
from collections import Counter

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(tasks, n):
    counts = Counter(tasks)
    max_count = max(counts.values())
    num_max = sum(1 for c in counts.values() if c == max_count)
    return max(len(tasks), (max_count - 1) * (n + 1) + num_max)

inputs = [
    (['a', 'a', 'a', 'b', 'b'], 2),
    (['a', 'a', 'a', 'b', 'b', 'b'], 0),
    (['a', 'a', 'a', 'a'], 3),
    (['a'], 5),
    (['a', 'b', 'c', 'd'], 2),
    (['a', 'a', 'b', 'b', 'c', 'c'], 2),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.least_interval(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
