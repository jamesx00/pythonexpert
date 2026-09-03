import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main
from collections import Counter

def test_is_n_straight_hand(hand, group_size):
    if len(hand) % group_size != 0:
        return False
    count = Counter(hand)
    for k in sorted(count.keys()):
        needed = count[k]
        if needed == 0:
            continue
        for j in range(k, k + group_size):
            if count[j] < needed:
                return False
            count[j] -= needed
    return True

inputs = [
    ([1, 2, 3, 6, 2, 3, 4, 7, 8], 3),
    ([1, 2, 3, 4, 5], 4),
    ([9, 13, 15, 23, 22, 25, 31, 20, 29, 14, 26, 12, 10, 27, 21, 11, 17, 30, 24, 28, 16, 18, 19, 32], 3),
    ([1, 1, 2, 2, 3, 3], 2),
    ([3, 4, 2, 1], 4),
    ([1, 2, 3], 1),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_is_n_straight_hand(*i)
        assert main.is_n_straight_hand(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
