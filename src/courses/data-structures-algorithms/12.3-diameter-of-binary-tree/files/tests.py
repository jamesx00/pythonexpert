import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_diameter_of_binary_tree(values):
    root = main.build_tree(values)
    best = [0]

    def height(node):
        if node is None:
            return 0
        left = height(node.left)
        right = height(node.right)
        best[0] = max(best[0], left + right)
        return 1 + max(left, right)

    height(root)
    return best[0]

inputs = [
    ([1, 2, 3, 4, 5],),
    ([1, 2],),
    ([],),
    ([1],),
    ([1, 2, None, 3, None, 4, None, 5],),
    ([1, None, 2, None, 3],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_diameter_of_binary_tree(*i)
        root = main.build_tree(*i)
        assert main.diameter_of_binary_tree(root) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
