import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n - 1 not in num_set:
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

inputs = [
    ([9, 1, 4, 2, 3, 100],),
    ([],),
    ([5],),
    ([1, 2, 0, 1],),
    ([10, 5, 12, 11, 6, 7],),
    ([-2, -1, 0, 1, 2, 8],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_longest_consecutive(*i)
        assert main.longest_consecutive(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
