import sys
import json
from collections import Counter

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_top_k_frequent(nums, k):
    counts = Counter(nums)
    most_common = counts.most_common(k)
    return [n for n, _ in most_common]

inputs = [
    ([5, 5, 5, 1, 1, 9], 2),
    ([1, 2, 2, 3, 3, 3], 1),
    ([4], 1),
    ([7, 7, 8, 8, 9, 9], 3),
    ([1, 1, 1, 2, 2, 3], 2),
    ([-1, -1, 2, 3, 3], 2),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = sorted(test_top_k_frequent(*i))
        assert sorted(main.top_k_frequent(*i)) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
