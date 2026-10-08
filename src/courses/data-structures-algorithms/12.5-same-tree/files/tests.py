import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_is_same_tree(p_values, q_values):
    p = main.build_tree(p_values)
    q = main.build_tree(q_values)

    def same(a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

    return same(p, q)

inputs = [
    ([1, 2, 3], [1, 2, 3]),
    ([1, 2], [1, None, 2]),
    ([1, 2, 1], [1, 1, 2]),
    ([], []),
    ([1], []),
    ([5, 3, 8, 1, 4], [5, 3, 8, 1, 4]),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_is_same_tree(*i)
        p = main.build_tree(i[0])
        q = main.build_tree(i[1])
        assert main.is_same_tree(p, q) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
